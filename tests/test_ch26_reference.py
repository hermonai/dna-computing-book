import importlib.util
from dataclasses import FrozenInstanceError, replace
import hashlib
import itertools
import json
from pathlib import Path
import sys

import pytest

path = Path(__file__).parents[1] / "book/chapters/ch26/reference.py"
spec = importlib.util.spec_from_file_location("dna26", path)
r = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = r
spec.loader.exec_module(r)


def demo():
    history, store, _ = r.demo()
    return history, dict(store)


def rehash(event):
    # Deliberately independent JSON construction: no r.payload/canonical/sha.
    from dataclasses import asdict

    body = asdict(event)
    body.pop("digest")
    digest = hashlib.sha256(
        json.dumps(
            body,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        ).encode("ascii")
    ).hexdigest()
    return replace(event, digest=digest)


def test_complete_history_and_hash_oracle():
    history, store = demo()
    assert r.validate_history(history, store)
    assert len(history) == 6
    for event in history:
        assert rehash(event).digest == event.digest


def test_frozen_nested_records():
    history, _ = demo()
    with pytest.raises(FrozenInstanceError):
        history[0].plan.run_id = "changed"
    with pytest.raises(FrozenInstanceError):
        history[0].artifacts[0].identity = "changed"


def test_every_prefix_is_valid_not_released():
    history, store = demo()
    for k in range(1, 7):
        assert r.validate_history(history[:k], store)
        assert history[k - 1].stage == r.STAGES[k - 1]


def test_all_illegal_stage_orders():
    history, store = demo()
    for order in itertools.permutations(range(3)):
        if order == (0, 1, 2):
            continue
        with pytest.raises(ValueError):
            r.validate_history(tuple(history[k] for k in order), store)


def test_released_label_is_not_a_history():
    history, store = demo()
    with pytest.raises(ValueError, match="stage"):
        r.validate_history(
            (rehash(replace(history[-1], previous_digest=r.ZERO)),), store
        )


def test_skip_and_terminal_transition():
    history, store = demo()
    with pytest.raises(ValueError):
        r.advance(history[:1], "released", (), store)
    with pytest.raises(ValueError):
        r.advance(history, "released", (), store)


def test_missing_stage_roles_despite_recomputed_digest():
    history, store = demo()
    for index, event in enumerate(history):
        for role in set().union(*r.REQUIRED[: index + 1]):
            bad = rehash(
                replace(
                    event, artifacts=tuple(a for a in event.artifacts if a.role != role)
                )
            )
            with pytest.raises(ValueError, match="prerequisites"):
                r.validate_event(bad, store)


def test_actual_bytes_mutation_detected():
    history, store = demo()
    identity = history[-1].artifacts[0].identity
    data = store[identity]
    store[identity] = bytes([data[0] ^ 1]) + data[1:]
    with pytest.raises(ValueError, match="digest"):
        r.validate_history(history, store)


def test_missing_bytes_and_length_change():
    history, store = demo()
    identity = history[-1].artifacts[0].identity
    for data in (None, store[identity] + b"x"):
        other = dict(store)
        other[identity] = data
        with pytest.raises(ValueError):
            r.validate_history(history, other)


def test_event_mutation_requires_digest():
    history, store = demo()
    with pytest.raises(ValueError, match="content digest"):
        r.validate_event(replace(history[-1], deviations=("concealed",)), store)


def test_rehashed_plan_change_fails_history():
    history, store = demo()
    event = rehash(
        replace(history[1], plan=replace(history[1].plan, sequence_set_id="other"))
    )
    with pytest.raises(ValueError, match="identities"):
        r.validate_history((history[0], event), store)


def test_rehashed_old_artifact_removal():
    history, store = demo()
    # Keep required roles by a new artifact ID; stage prerequisites still pass.
    old = history[1]
    item = old.artifacts[0]
    substitute = replace(item, identity="renamed")
    store["renamed"] = store[item.identity]
    bad = rehash(replace(old, artifacts=(substitute,) + old.artifacts[1:]))
    r.validate_event(bad, store)
    with pytest.raises(ValueError, match="removed"):
        r.validate_history((history[0], bad), store)


def test_predecessor_link_rejects_rehashed_event():
    history, store = demo()
    bad = rehash(replace(history[1], previous_digest="a" * 64))
    with pytest.raises(ValueError, match="predecessor"):
        r.validate_history((history[0], bad), store)


def test_deviation_prefix_cannot_be_removed():
    history, store = demo()
    assert history[2].deviations
    bad = rehash(replace(history[3], deviations=()))
    with pytest.raises(ValueError, match="Deviation"):
        r.validate_history(history[:3] + (bad,), store)


def test_conflicting_duplicate_artifact_id():
    history, store = demo()
    with pytest.raises(ValueError, match="unique"):
        r.verify_artifacts(history[0].artifacts + (history[0].artifacts[0],), store)


@pytest.mark.parametrize("digest", ["x", "g" * 64, "A" * 64, "", "0" * 63])
def test_malformed_digest(digest):
    history, store = demo()
    bad = replace(history[0].artifacts[0], digest=digest)
    with pytest.raises(ValueError):
        r.verify_artifacts((bad,), store)


def test_role_size_and_policy_types():
    history, store = demo()
    item = history[0].artifacts[0]
    for bad in (
        replace(item, role="unknown"),
        replace(item, size_bytes=True),
        replace(item, size_bytes=-1),
    ):
        with pytest.raises(ValueError):
            r.verify_artifacts((bad,), store)
    for plan in (
        replace(history[0].plan, control_ids=("same", "same")),
        replace(history[0].plan, run_id=" "),
        replace(history[0].plan, blinding_required=1),
    ):
        with pytest.raises(ValueError):
            r.validate_plan(plan)


def test_declared_blinding_exception_not_silent_waiver():
    history, store = demo()
    bad = rehash(replace(history[3], analyst_blinded=False))
    with pytest.raises(ValueError, match="blinding"):
        r.validate_event(bad, store)
    plan = replace(
        history[0].plan,
        blinding_required=False,
        blinding_exception="Instrument displays coded group; explicit limitation",
    )
    r.validate_plan(plan)
    with pytest.raises(ValueError):
        r.validate_plan(replace(plan, blinding_exception=""))


def test_units_zero_and_reference():
    assert r.concentration_amount(0, 2) == 0
    assert r.concentration_amount(2e-9, 5e-6) == pytest.approx(1e-14)
    assert r.amount_uncertainty(2e-9, 5e-6, 0.2e-9, 0.1e-6) == pytest.approx(
        1.019803902718557e-15
    )


@pytest.mark.parametrize("value", [-1, float("nan"), float("inf"), True, "2"])
def test_invalid_quantity(value):
    with pytest.raises(ValueError):
        r.concentration_amount(value, 1)


def test_covariance_term():
    # Independent hand Jacobian for c=2,V=3, sigma_c=.1,sigma_V=.2.
    for rho in (-1, 0, 1):
        expected = (9 * 0.01 + 4 * 0.04 + 2 * 2 * 3 * rho * 0.1 * 0.2) ** 0.5
        assert r.amount_uncertainty(2, 3, 0.1, 0.2, rho) == pytest.approx(expected)
    with pytest.raises(ValueError):
        r.amount_uncertainty(2, 3, 0.1, 0.2, 1.01)


def test_preparation_oracle_not_object_count():
    means = (0, 1, 1)
    expected = sum((x - 2 / 3) ** 2 for x in means) / 6
    assert r.cluster_mean_variance(([0] * 100, [1] * 100, [1] * 100)) == pytest.approx(
        (2 / 3, expected)
    )
    assert r.cluster_mean_variance(([0], [1] * 999))[0] == 0.5


def test_invalid_preparation_groups():
    for groups in ([], [[1]], [[1], []], [[True], [0]], [[float("nan")], [0]]):
        with pytest.raises(ValueError):
            r.cluster_mean_variance(groups)


def test_unblinding_after_observation_freeze_is_allowed():
    history, store = demo()
    event = rehash(replace(history[4], analyst_blinded=False))
    assert r.validate_history(history[:4] + (event,), store)


def test_numeric_overflow_is_a_domain_error():
    with pytest.raises(ValueError):
        r.amount_uncertainty(1e308, 1e308, 1e308, 1e308)
    with pytest.raises(ValueError):
        r.cluster_mean_variance(([1e308], [-1e308]))


def test_coherent_rebuilt_chain_is_not_authentication():
    history, store = demo()
    identity = history[0].artifacts[0].identity
    store[identity] = b"Coherent replacement; no authenticated external anchor"
    rebuilt = []
    for event in history:
        artifacts = tuple(
            r.bind_artifact(a.role, a.identity, store[a.identity])
            for a in event.artifacts
        )
        rebuilt.append(
            rehash(
                replace(
                    event,
                    artifacts=artifacts,
                    previous_digest=r.ZERO if not rebuilt else rebuilt[-1].digest,
                )
            )
        )
    assert r.validate_history(tuple(rebuilt), store)
    assert rebuilt[-1].digest != history[-1].digest
