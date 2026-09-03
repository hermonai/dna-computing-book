from minidna.expression import ExpressionNode, express
from minidna.regulation import RegulatoryGate


def test_expression_returns_outputs_and_gate_trace() -> None:
    nodes = [
        ExpressionNode(
            "copy",
            RegulatoryGate("has_input", lambda ctx: "input" in ctx),
            lambda ctx: ctx["input"],
        ),
        ExpressionNode(
            "suppressed",
            RegulatoryGate("never", lambda _ctx: False),
            lambda _ctx: "unreachable",
        ),
    ]
    outputs, trace = express(nodes, {"input": "ACGT"})
    assert outputs == {"copy": "ACGT"}
    assert trace == [("copy", True), ("suppressed", False)]

