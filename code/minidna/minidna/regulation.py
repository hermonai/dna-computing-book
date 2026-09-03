"""Context-dependent formal gates for later regulation examples."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any

Context = Mapping[str, Any]


@dataclass(frozen=True, slots=True)
class RegulatoryGate:
    name: str
    predicate: Callable[[Context], bool]

    def evaluate(self, context: Context) -> bool:
        return bool(self.predicate(context))

