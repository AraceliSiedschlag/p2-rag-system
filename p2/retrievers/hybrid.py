"""Your hybrid retriever (stage 1): fuse the rankings of two systems into one.

This file is yours to write. Until you write it, build() raises NotImplementedError, and p2 skips
the system and lists it as to do.

Where the idea is:
- the 13 lab's pipeline.py in the course repo (class/13-rag-pipeline/lab/starter/pipeline.py):
  rrf() is reciprocal rank fusion with k = 60, where each document scores the sum of 1 / (60 + rank)
  over the rankings it appears in, and command_fuse() fuses bm25 with an embedder;
- get the two systems you fuse with p2.retrievers.build("bm25", corpus, cfg) and
  build("dense", corpus, cfg), so each index is built once per run;
- fuse full rankings, not top-10 lists (ask each system for len(corpus.docs) documents), because a
  document that is 11th in both lists can belong in the fused top 10;
- order the fused documents with p2.runfile.order(), so equal scores fall in document id order.

If you want `p2 answer` to work with hybrid, also give it search_chunks(text, k): the same fusion over chunk rankings.
"""

from __future__ import annotations

from collections import defaultdict

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False


def rrf(rankings, k: int, weights) -> list[tuple[str, float]]:
    """Weighted reciprocal rank fusion: each id scores the sum of weight / (k + rank) over the rankings it appears in."""
    scores: dict[str, float] = defaultdict(float)
    for ranking, weight in zip(rankings, weights):
        for rank, (item, _score) in enumerate(ranking, 1):
            scores[item] += weight / (k + rank)
    return order(scores.items())


class Hybrid:
    def __init__(self, corpus, cfg):
        settings = cfg.table("hybrid")
        self.names = list(settings.get("systems", ["bm25", "dense"]))
        self.k = int(settings.get("k", 60))
        self.weights = [float(w) for w in settings.get("weights", [1] * len(self.names))]
        if len(self.weights) != len(self.names):
            raise ValueError(f"[hybrid] in p2.toml has {len(self.names)} systems but {len(self.weights)} weights; give one weight per system.")
        # Built through the registry, so a run of several systems builds each index once.
        self.systems = [retrievers.build(name, corpus, cfg) for name in self.names]
        self.depth = int(settings.get("depth", 0))
        self.n_docs = len(corpus.docs)
        self.n_chunks = len(corpus.chunks(cfg.chunk_words, cfg.chunk_overlap))

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        # Fuse deep rankings, not top-k lists: a document 11th in both can belong in the fused top 10.
        # With depth set, a document a system ranks below it gets no vote from that system.
        n = self.depth or self.n_docs
        return rrf([s.search(text, n) for s in self.systems], self.k, self.weights)[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        n = self.depth or self.n_chunks
        return rrf([s.search_chunks(text, n) for s in self.systems], self.k, self.weights)[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
