import importlib.util
import json
import math
from pathlib import Path
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna10", ROOT / "drafts/ch10/reference.py"
)
ref = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ref)


def test_ladder_interpolation_and_boundary():
    lengths = [100, 1000, 10000]
    c = ref.calibrate(lengths, [60, 40, 20])
    assert c["a"] == pytest.approx(100)
    assert c["b"] == pytest.approx(20)
    assert ref.infer_length(50, c) == pytest.approx(math.sqrt(100 * 1000))
    with pytest.raises(ValueError):
        ref.infer_length(65, c)


@pytest.mark.parametrize(
    "lengths,x",
    [([1, 1], [2, 3]), ([0, 1], [3, 2]), ([1, 2], [2, 3]), ([1], [2])],
)
def test_bad_ladders(lengths, x):
    with pytest.raises(ValueError):
        ref.calibrate(lengths, x)


def test_kernel_area_symmetry_and_finite_window():
    k = ref.band_kernel([-10, 0, 10], [0], [1])
    assert k[:, 0] == pytest.approx([0.5, 0.5])
    assert ref.band_kernel([-1, 1], [0], [1])[0, 0] == pytest.approx(
        0.6826894921
    )
    assert ref.band_kernel([0, 1], [0], [1]).sum() < 0.5


def test_mass_is_not_count_and_no_window_renormalization():
    a = ref.response_matrix([-10, 10], [0, 0], [1, 1], [500, 1000], 0.002)
    assert ref.observe(a, [2, 1])[0] == pytest.approx(4)
    partial = ref.response_matrix([0, 1], [0], [1], [500], 0.002)
    assert partial[0, 0] < 0.5


def test_exact_ambiguity_is_rejected_then_extra_channel_resolves():
    a = np.array([[1, 1], [0.2, 0.2], [0.5, 0.5]])
    assert np.allclose(ref.observe(a, [7, 3]), ref.observe(a, [10, 0]))
    with pytest.raises(ValueError, match="identifiable"):
        ref.unmix(a, a @ [7, 3], [0.1] * 3)
    b = np.vstack((a, [1, 0.1]))
    assert ref.unmix(b, b @ [7, 3], [0.1] * 4)["estimate"] == pytest.approx(
        [7, 3]
    )


@pytest.mark.parametrize("delta", [1.0, 0.1, 0.01])
def test_uncertainty_has_independent_analytic_oracle(delta):
    r = ref.unmix([[1, 1], [0, delta]], [10, 3 * delta], [0.1, 0.1])
    assert r["estimate"] == pytest.approx([7, 3])
    assert r["sd"][0] == pytest.approx(0.1 * math.sqrt(1 + 1 / delta**2))
    assert r["sd"][1] == pytest.approx(0.1 / delta)


def test_background_is_shared_error_not_independent_subtraction():
    net, sd = ref.roi_summary([12, 14, 13, 11], [2, 2, 2, 2], 1)
    assert net == 42 and sd == pytest.approx(math.sqrt(8))
    # More blank pixels reduce only the background-estimation contribution.
    assert ref.roi_summary([12, 14, 13, 11], [2] * 16, 1)[
        1
    ] == pytest.approx(math.sqrt(5))


def test_saturation_destroys_injectivity():
    assert np.array_equal(
        ref.observe([[1]], [20], ceiling=12),
        ref.observe([[1]], [30], ceiling=12),
    )
    assert ref.observe([[0.1]], [20], ceiling=12)[0] == 2


def test_collection_purity_recovery_and_empty():
    narrow = ref.collect_window(-0.5, 0.5, [0, 3], [1, 1], [7, 3])
    wide = ref.collect_window(-10, 10, [0, 3], [1, 1], [7, 3])
    assert narrow["purity"] > wide["purity"]
    assert narrow["recovery"] < wide["recovery"]
    assert wide["purity"] == pytest.approx(0.7)
    assert ref.collect_window(-1, 1, [0], [1], [0])["purity"] is None


def test_inverse_does_not_silently_clip_negative_estimates():
    assert ref.unmix([[1, 0], [0, 1]], [-1, 2], [1, 1])["estimate"] == [
        -1,
        2,
    ]


@pytest.mark.parametrize(
    "edges,widths",
    [([0, 0], [1]), ([1, 0], [1]), ([0, 1], [0]), ([0, 1], [float("nan")])],
)
def test_invalid_kernel(edges, widths):
    with pytest.raises(ValueError):
        ref.band_kernel(edges, [0], widths)


def test_results_are_reproducible():
    assert ref.results() == json.loads(
        (ROOT / "drafts/ch10/results.json").read_text()
    )


def test_full_profile_inverse_recovers_assigned_mixture():
    edges = np.linspace(35, 57, 111)
    a = ref.response_matrix(edges, [46, 49], [1.2, 1.2], [500, 400], 0.002)
    result = ref.unmix(a, ref.observe(a, [7, 3]), np.full(110, 0.01))
    assert result["estimate"] == pytest.approx([7, 3])


def test_empty_inverse_observations_are_rejected():
    with pytest.raises(ValueError):
        ref.unmix(np.empty((0, 2)), [], [])
