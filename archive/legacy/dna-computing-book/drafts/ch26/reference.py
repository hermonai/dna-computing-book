"""DNAD-26: append-only evidence records, not a wet-lab protocol or trust authority."""

from dataclasses import asdict, dataclass
import hashlib
import json
import math
import re

STAGES = (
    "design_frozen",
    "materials_verified",
    "run_recorded",
    "observations_frozen",
    "analysis_frozen",
    "released",
)
REQUIRED = (
    {"design", "sequences", "protocol"},
    {"materials"},
    {"execution", "controls", "randomization"},
    {"raw", "calibration", "blinding"},
    {"analysis_spec", "analysis_code", "derived"},
    {"release_metadata"},
)
ROLES = frozenset().union(*REQUIRED)
ZERO = "0" * 64


def sha(data):
    if not isinstance(data, bytes):
        raise ValueError("Artifact content must be bytes")
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    """Declared local JSON profile, not a universal cross-language canonicalizer."""
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    ).encode("ascii")


def identifier(value):
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError("Nonempty, stripped string identity required")
    return value


@dataclass(frozen=True)
class Plan:
    run_id: str
    design_id: str
    sequence_set_id: str
    material_id: str
    preparation_id: str
    protocol_version: str
    independent_unit_id: str
    control_ids: tuple
    blinding_required: bool
    blinding_exception: str = ""


@dataclass(frozen=True)
class Artifact:
    role: str
    identity: str
    digest: str
    size_bytes: int


@dataclass(frozen=True)
class Event:
    stage: str
    plan: Plan
    artifacts: tuple
    deviations: tuple
    analyst_blinded: bool
    previous_digest: str
    digest: str


def validate_plan(plan):
    if not isinstance(plan, Plan):
        raise ValueError("Typed plan required")
    for field in (
        "run_id",
        "design_id",
        "sequence_set_id",
        "material_id",
        "preparation_id",
        "protocol_version",
        "independent_unit_id",
    ):
        identifier(getattr(plan, field))
    if type(plan.control_ids) is not tuple or len(plan.control_ids) < 2:
        raise ValueError("Declared negative and positive control identities required")
    for value in plan.control_ids:
        identifier(value)
    if len(set(plan.control_ids)) != len(plan.control_ids):
        raise ValueError("Control identities must be distinct")
    if type(plan.blinding_required) is not bool:
        raise ValueError("Blinding policy must be Boolean")
    if not plan.blinding_required:
        identifier(plan.blinding_exception)
    elif plan.blinding_exception:
        raise ValueError("Required blinding cannot silently become an exception")


def bind_artifact(role, identity, data):
    if role not in ROLES:
        raise ValueError("Unknown artifact role")
    return Artifact(role, identifier(identity), sha(data), len(data))


def verify_artifacts(artifacts, store):
    if type(artifacts) is not tuple or not isinstance(store, dict):
        raise ValueError("Immutable artifact tuple and byte store required")
    seen = set()
    for item in artifacts:
        if not isinstance(item, Artifact) or item.role not in ROLES:
            raise ValueError("Unknown typed artifact")
        identifier(item.identity)
        if item.identity in seen:
            raise ValueError("Artifact identities must be unique")
        seen.add(item.identity)
        if (
            not isinstance(item.digest, str)
            or re.fullmatch("[0-9a-f]{64}", item.digest) is None
            or type(item.size_bytes) is not int
            or item.size_bytes < 0
        ):
            raise ValueError("Malformed artifact digest or size")
        data = store.get(item.identity)
        if not isinstance(data, bytes) or len(data) != item.size_bytes:
            raise ValueError("Missing artifact bytes or size mismatch")
        if sha(data) != item.digest:
            raise ValueError("Artifact byte digest mismatch")


def payload(event):
    value = asdict(event)
    del value["digest"]
    return value


def validate_event(event, store):
    if not isinstance(event, Event) or event.stage not in STAGES:
        raise ValueError("Unknown typed workflow stage")
    validate_plan(event.plan)
    verify_artifacts(event.artifacts, store)
    index = STAGES.index(event.stage)
    required = set().union(*REQUIRED[: index + 1])
    if not required <= {a.role for a in event.artifacts}:
        raise ValueError("Missing cumulative stage prerequisites")
    if type(event.deviations) is not tuple:
        raise ValueError("Immutable deviation tuple required")
    for note in event.deviations:
        identifier(note)
    if type(event.analyst_blinded) is not bool:
        raise ValueError("Blinding status must be Boolean")
    if index == 3 and event.plan.blinding_required and not event.analyst_blinded:
        raise ValueError("Observation-freeze blinding contract not satisfied")
    if re.fullmatch("[0-9a-f]{64}", event.previous_digest) is None:
        raise ValueError("Malformed predecessor digest")
    if event.digest != sha(canonical(payload(event))):
        raise ValueError("Event content digest mismatch")


def make_event(
    stage,
    plan,
    artifacts,
    store,
    previous_digest=ZERO,
    deviations=(),
    analyst_blinded=False,
):
    event = Event(
        stage, plan, artifacts, deviations, analyst_blinded, previous_digest, ""
    )
    event = Event(
        stage,
        plan,
        artifacts,
        deviations,
        analyst_blinded,
        previous_digest,
        sha(canonical(payload(event))),
    )
    validate_event(event, store)
    return event


def start(plan, artifacts, store):
    """Genesis is design_frozen, never an arbitrary label supplied by a caller."""
    return (make_event(STAGES[0], plan, artifacts, store),)


def validate_history(history, store):
    if type(history) is not tuple or not 1 <= len(history) <= len(STAGES):
        raise ValueError("Nonempty bounded immutable history required")
    prior = None
    for index, event in enumerate(history):
        validate_event(event, store)
        if event.stage != STAGES[index]:
            raise ValueError("Skipped, duplicated or reordered workflow stage")
        if event.previous_digest != (ZERO if prior is None else prior.digest):
            raise ValueError("Broken predecessor link")
        if prior is not None:
            if event.plan != prior.plan:
                raise ValueError("Frozen plan identities changed; create a new run")
            old = {a.identity: a for a in prior.artifacts}
            new = {a.identity: a for a in event.artifacts}
            if not old.items() <= new.items():
                raise ValueError("Frozen artifact removed or replaced")
            if event.deviations[: len(prior.deviations)] != prior.deviations:
                raise ValueError("Deviation history rewritten")
        prior = event
    return True


def advance(history, target, additions, store, notes=(), analyst_blinded=False):
    """Validate actual history/bytes, append one audited boundary, retain old facts."""
    validate_history(history, store)
    if len(history) == len(STAGES) or target != STAGES[len(history)]:
        raise ValueError("Must advance exactly one stage; release is terminal")
    if type(additions) is not tuple or type(notes) is not tuple:
        raise ValueError("Immutable additions and deviation notes required")
    old = history[-1]
    event = make_event(
        target,
        old.plan,
        old.artifacts + additions,
        store,
        old.digest,
        old.deviations + notes,
        analyst_blinded,
    )
    result = history + (event,)
    validate_history(result, store)
    return result


def nonnegative(value, name):
    if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
        raise ValueError(f"Finite nonnegative {name} required")
    return value


def concentration_amount(c_molar, volume_litre):
    """SI bookkeeping amount, not a measured functional molecule inventory."""
    value = nonnegative(c_molar, "concentration") * nonnegative(volume_litre, "volume")
    if not math.isfinite(value):
        raise ValueError("Amount overflow")
    return value


def amount_uncertainty(c, volume, sigma_c, sigma_volume, correlation=0.0):
    """First-order delta approximation with explicitly supplied covariance."""
    c, volume = nonnegative(c, "concentration"), nonnegative(volume, "volume")
    sc = nonnegative(sigma_c, "concentration uncertainty")
    sv = nonnegative(sigma_volume, "volume uncertainty")
    if type(correlation) not in (int, float) or not math.isfinite(correlation):
        raise ValueError("Finite correlation required")
    if not -1 <= correlation <= 1:
        raise ValueError("Correlation outside [-1,1]")
    x, y = volume * sc, c * sv
    if not math.isfinite(x) or not math.isfinite(y):
        raise ValueError("Uncertainty overflow")
    sigma = math.hypot(x + correlation * y, math.sqrt(1 - correlation**2) * y)
    if not math.isfinite(sigma):
        raise ValueError("Uncertainty overflow")
    return sigma


def cluster_mean_variance(groups):
    """Variance of an equally weighted preparation mean; at least two preparations."""
    if not isinstance(groups, (tuple, list)) or len(groups) < 2:
        raise ValueError("At least two independent preparations required")
    means = []
    for group in groups:
        if not isinstance(group, (tuple, list)) or not group:
            raise ValueError("Nonempty preparation observations required")
        for x in group:
            if type(x) not in (int, float) or not math.isfinite(x):
                raise ValueError("Finite numeric observations required")
        try:
            means.append(math.fsum(x / len(group) for x in group))
        except OverflowError as exc:
            raise ValueError("Preparation mean overflow") from exc
    mean = math.fsum(x / len(means) for x in means)
    try:
        variance = math.fsum((x - mean) ** 2 for x in means) / (
            len(means) * (len(means) - 1)
        )
    except OverflowError as exc:
        raise ValueError("Preparation variance overflow") from exc
    if not math.isfinite(mean) or not math.isfinite(variance):
        raise ValueError("Preparation statistic overflow")
    return mean, variance


def demo():
    plan = Plan(
        "run-26",
        "design-v4",
        "seqset-v4",
        "lot-7",
        "prep-11",
        "protocol-r3",
        "independent-prep-11",
        ("negative-1", "positive-1"),
        True,
    )
    store, history = {}, None
    rows = []
    for index, roles in enumerate(REQUIRED):
        additions = []
        for role in sorted(roles):
            identity = f"{role}-demo"
            data = (
                f"Assigned teaching artifact: {role}; not experimental data.".encode()
            )
            store[identity] = data
            additions.append(bind_artifact(role, identity, data))
        if index == 0:
            history = start(plan, tuple(additions), store)
        else:
            history = advance(
                history,
                STAGES[index],
                tuple(additions),
                store,
                notes=("instrument restart recorded before unblinding",)
                if index == 2
                else (),
                analyst_blinded=index >= 3,
            )
        rows.append({"stage": STAGES[index], "artifacts": len(history[-1].artifacts)})
    return history, store, rows


def results():
    history, store, rows = demo()
    validate_history(history, store)
    mean, variance = cluster_mean_variance(([0] * 100, [1] * 100, [1] * 100))
    iid_variance = 300 * mean * (1 - mean) / (300 * 299)
    return {
        "history_valid": True,
        "event_digest": history[-1].digest,
        "amount_mol": concentration_amount(2e-9, 5e-6),
        "amount_sigma_mol": amount_uncertainty(2e-9, 5e-6, 0.2e-9, 0.1e-6),
        "preparation_mean": mean,
        "preparation_mean_variance": variance,
        "naive_object_mean_variance": iid_variance,
        "stages": rows,
    }


TABLES = [("stages", ["Stage", "Bound artifacts"], ["stage", "artifacts"], "lr")]
PLOTS = []
LISTINGS = [
    "verify_artifacts",
    "validate_history",
    "advance",
    "amount_uncertainty",
    "cluster_mean_variance",
]

if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
