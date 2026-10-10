"""Tiny deterministic expression network for pedagogical examples."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any

from .regulation import RegulatoryGate


@dataclass(frozen=True, slots=True)
class ExpressionNode:
    name: str
    gate: RegulatoryGate
    operation: Callable[[Mapping[str, Any]], Any]


def express(
    nodes: list[ExpressionNode], context: Mapping[str, Any]
) -> tuple[dict[str, Any], list[tuple[str, bool]]]:
    """Evaluate gates once, execute enabled nodes, and return an explicit trace."""

    outputs: dict[str, Any] = {}
    trace: list[tuple[str, bool]] = []
    scope: dict[str, Any] = dict(context)
    for node in nodes:
        enabled = node.gate.evaluate(scope)
        trace.append((node.name, enabled))
        if enabled:
            value = node.operation(scope)
            outputs[node.name] = value
            scope[node.name] = value
    return outputs, trace

