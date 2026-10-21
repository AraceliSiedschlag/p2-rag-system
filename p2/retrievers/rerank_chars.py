"""Ablation of rerank: the same reranker, but Claude sees the first 2,500 characters of each candidate instead of 600.

Everything else is rerank's: the first stage (hybrid), 20 candidates, the prompt, the schema and the model.
p2 score compares this system with rerank, named by BASE below.
"""

from __future__ import annotations

from p2.retrievers.rerank import Rerank

NEEDS_CLAUDE = True
BASE = "rerank"
PASSAGE_CHARS = 2500


class RerankChars(Rerank):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.passage_chars = PASSAGE_CHARS


def build(corpus, cfg):
    return RerankChars(corpus, cfg)
