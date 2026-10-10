from pathlib import Path
import importlib.util
import json
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna_computing_book_ch16", ROOT / "drafts/ch16/reference.py"
)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def test_committed_results_match_execution():
    assert m.results() == json.loads(
        (ROOT / "drafts/ch16/results.json").read_text()
    )


@pytest.mark.parametrize("n", range(10))
def test_recognizer_exhaustive(n):
    from itertools import product

    for w in map("".join, product("01", repeat=n)):
        accepted, trace = m.recognize(w)
        assert accepted == w.endswith("01")
        assert len(trace) == len(w) + 1
        for i, q in enumerate(trace):
            prefix = w[:i]
            expected = (
                2
                if prefix.endswith("01")
                else 1
                if prefix.endswith("0")
                else 0
            )
            assert q == expected


@pytest.mark.parametrize("width", range(7))
def test_addition_independent_integer_oracle(width):
    for x in range(2**width):
        for y in range(2**width):
            a = format(x, f"0{width}b")[::-1] if width else ""
            b = format(y, f"0{width}b")[::-1] if width else ""
            out, trace = m.add_bits(a, b)
            assert int(out[::-1], 2) == x + y
            assert len(out) == width + 1 and len(trace) == width


def test_orientation_and_overflow_negative_controls():
    out, _ = m.add_bits("1011", "1100")
    assert out == "00001"  # 13+3=16
    assert int(out[:-1][::-1], 2) != 16
    with pytest.raises(ValueError):
        m.add_bits("0", "11")
    with pytest.raises(ValueError):
        m.recognize("012")


@pytest.mark.parametrize("error", [0, 0.02, 1])
@pytest.mark.parametrize("loss", [0, 0.01, 1])
def test_probability_and_absorbing_loss(error, loss):
    for n in range(10):
        word = "01" * n
        v = m.noisy_distribution(word, error, loss)
        assert sum(v) == pytest.approx(1)
        assert v[3] == pytest.approx(1 - (1 - loss) ** len(word))
        assert all(x >= 0 for x in v)
        if error == 0 and loss == 0:
            accepted, _ = m.recognize(word)
            assert v[2] == int(accepted)


def test_probability_domain():
    for p in [-0.1, 1.1, float("nan")]:
        with pytest.raises(ValueError):
            m.noisy_distribution("01", p, 0)
