"""Your reranker (stage 1): ask Claude to reorder a first-stage system's top 20.

This file is yours to write. Until you write it, build() raises NotImplementedError, and p2 skips
the system and lists it as to do. NEEDS_CLAUDE = True tells p2 that searching calls claude -p, so
CI never regenerates this system's runs; you produce them on your machine and commit them.

Where the idea is:
- the 13 lab's pipeline.py in the course repo (class/13-rag-pipeline/lab/starter/pipeline.py):
  rerank_one() shows the top 20 as numbered passages, RERANK_SCHEMA forces the reply into
  {"order": [20 numbers]}, a reply that is not each number once keeps the original order, and the
  documents below the 20 keep their order underneath;
- when you port RERANK_SCHEMA, also give its items "minimum": 1 and "maximum": 20 (the number of
  passages), so Claude cannot answer with a number that names no passage: the lab's schema only
  fixes how many numbers come back, and a reply such as [12, 2, 60, ...] silently keeps the first-stage order;
- make every call through p2.claude.call(prompt, schema, model=cfg.model,
  cache_dir=p2.claude.cache_folder(cfg)), which launches claude -p the way the lab does, caches
  replies, and records the tokens in the run's trace (traces/, which you commit with the run file:
  p2 check reads it, because CI never calls Claude to run this system again);
- get the first stage with p2.retrievers.build("hybrid", corpus, cfg).

`p2 answer --system rerank` also needs search_chunks(text, k): the same reranking over the first
stage's top 20 chunks (hybrid's search_chunks gives them).

A reranker over 20 candidates is one call per query: 20 calls for the practice queries, 40 for the
test queries. Try two queries first, and look at what Claude sees, before the full run.
"""

from __future__ import annotations

import sys

from p2 import claude, retrievers

NEEDS_CLAUDE = True

PROMPT = """Below are {n} passages from the US federal mine safety and health regulations (30 CFR), numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


def schema(n: int) -> dict:
    # minimum and maximum keep every number a real passage; the counts keep the list exactly n long.
    item = {"type": "integer", "minimum": 1, "maximum": n}
    return {
        "type": "object",
        "properties": {"order": {"type": "array", "items": item, "minItems": n, "maxItems": n}},
        "required": ["order"],
    }


class Rerank:
    def __init__(self, corpus, cfg):
        settings = cfg.table("rerank")
        self.first_name = settings.get("first_stage", "hybrid")
        self.candidates = int(settings.get("candidates", 20))
        self.passage_chars = int(settings.get("passage_chars", 600))
        self.first = retrievers.build(self.first_name, corpus, cfg)
        self.cfg = cfg
        self.model = cfg.model  # recorded in the run's trace
        self.doc_text = {docid: doc.text for docid, doc in corpus.docs.items()}
        self.chunk_text = {c.id: c.text for c in corpus.chunks(cfg.chunk_words, cfg.chunk_overlap)}

    def _rerank(self, query: str, ranked: list[tuple[str, float]], texts: dict[str, str]) -> list[str]:
        """The ids of `ranked` with its top `candidates` in Claude's order and the rest underneath, unchanged."""
        ids = [i for i, _ in ranked]
        top, rest = ids[: self.candidates], ids[self.candidates :]
        if len(top) < 2:
            return ids
        passages = "\n\n".join(f"[{n}] {texts[i][: self.passage_chars]}" for n, i in enumerate(top, 1))
        prompt = PROMPT.format(n=len(top), query=query, passages=passages)
        reply = claude.call(prompt, schema(len(top)), model=self.cfg.model, cache_dir=claude.cache_folder(self.cfg))
        new = (reply.output or {}).get("order")
        if reply.error or not isinstance(new, list) or sorted(new) != list(range(1, len(top) + 1)):
            # A broken reply keeps the first stage's order rather than guessing.
            print(f"rerank: kept the {self.first_name} order for {query[:60]!r} ({reply.error or f'reply was not each of 1 to {len(top)} once'})", file=sys.stderr)
            return ids
        return [top[n - 1] for n in new] + rest

    @staticmethod
    def _scored(ids: list[str], k: int) -> list[tuple[str, float]]:
        # Scores only carry the order: best first, strictly decreasing.
        return [(i, float(len(ids) - r)) for r, i in enumerate(ids)][:k]

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        ranked = self.first.search(text, max(k, self.candidates))
        return self._scored(self._rerank(text, ranked, self.doc_text), k)

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        ranked = self.first.search_chunks(text, max(k, self.candidates))
        return self._scored(self._rerank(text, ranked, self.chunk_text), k)


def build(corpus, cfg):
    return Rerank(corpus, cfg)
