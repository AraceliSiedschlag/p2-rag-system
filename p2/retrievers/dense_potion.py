"""Second ablation (stretch option 4): dense with potion-retrieval-32M instead of bge-small-en-v1.5.

Everything else is dense's: the same chunks (p2.toml [chunking]), the same cosine search, the same
best-chunk lift to documents. Only the embedding model changes.
p2 score compares this system with dense, named by BASE below.
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers.dense import Dense

NEEDS_CLAUDE = False
BASE = "dense"
MODEL = embed.POTION


class DensePotion(Dense):
    def __init__(self, corpus, cfg):
        settings = dict(cfg.table("dense"), model=MODEL)
        super().__init__(corpus, cfg.replace(tables={**cfg.tables, "dense": settings}))


def build(corpus, cfg):
    return DensePotion(corpus, cfg)
