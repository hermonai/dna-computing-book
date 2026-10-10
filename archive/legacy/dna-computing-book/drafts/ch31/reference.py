"""Original finite-fuel refinement and context-specific evidence teaching oracle."""

from dataclasses import dataclass
import math
import statistics


def nonnegative(values):
    if any(
        type(v) not in (int, float) or not math.isfinite(v) or v < 0 for v in values
    ):
        raise ValueError("finite nonnegative real values required")


@dataclass(frozen=True)
class Rates:
    on: float
    off: float
    cat: float

    def __post_init__(self):
        nonnegative((self.on, self.off, self.cat))


def rhs(state, rates):
    """Species order A,F,I,B,W. Concentration/time units."""
    if len(state) != 5:
        raise ValueError("five species required")
    nonnegative(state)
    a, f, i, _, _ = state
    capture, release, convert = rates.on * a * f, rates.off * i, rates.cat * i
    values = (
        -capture + release,
        -capture + release,
        capture - release - convert,
        convert,
        convert,
    )
    if not all(math.isfinite(v) for v in values):
        raise ValueError("rate overflow")
    return values


def euler_step(state, rates, dt):
    """Simultaneous stoichiometric update; no clipping of negative concentrations."""
    nonnegative((dt,))
    if dt == 0:
        raise ValueError("positive step required")
    a, f, _, _, _ = state
    if dt * max(rates.on * f, rates.on * a, rates.off + rates.cat) > 1:
        raise ValueError("step violates sufficient positivity bound")
    slope = rhs(state, rates)
    result = tuple(v + dt * d for v, d in zip(state, slope))
    nonnegative(result)
    return result


def simulate(state, rates, horizon, dt):
    nonnegative((horizon, dt))
    if dt == 0 or horizon / dt > 200000:
        raise ValueError("bounded positive step required")
    rhs(state, rates)
    elapsed = 0.0
    state = tuple(state)
    while elapsed < horizon:
        step = min(dt, horizon - elapsed)
        state = euler_step(state, rates, step)
        elapsed += step
    return state


def held_fuel(a0, u, off, cat, time):
    """Exact two-state linear transient, initially I=B=0, for fixed fuel."""
    nonnegative((a0, u, off, cat, time))
    if u == 0:
        return (a0, 0.0, 0.0)
    total = u + off + cat
    discriminant = total * total - 4 * u * cat
    if not math.isfinite(discriminant) or discriminant < 0:
        raise ValueError("unrepresentable poles")
    gap = math.sqrt(discriminant)
    if gap == 0:  # off=0, u=cat: repeated-pole limit
        a = a0 * math.exp(-u * time)
        i = a0 * u * time * math.exp(-u * time)
    else:
        fast = -(total + gap) / 2
        slow = -(2 * u * cat) / (total + gap)  # avoid subtractive cancellation
        es, ef = math.exp(slow * time), math.exp(fast * time)
        i = a0 * u * (es - ef) / gap
        a = a0 * ((-fast - u) * es + (slow + u) * ef) / gap
    return (a, i, a0 - a - i)


def error_bound(initial, forcing, lipschitz, time):
    nonnegative((initial, forcing, lipschitz, time))
    try:
        result = (
            initial + forcing * time
            if lipschitz == 0
            else initial * math.exp(lipschitz * time)
            + forcing * math.expm1(lipschitz * time) / lipschitz
        )
    except OverflowError as exc:
        raise ValueError("bound overflow") from exc
    if not math.isfinite(result):
        raise ValueError("bound overflow")
    return result


def calibrated_interval(y, offset, gain):
    """Independent interval box, nonsaturating y=offset+gain*B, B>=0."""
    for pair in (y, offset, gain):
        if (
            len(pair) != 2
            or not all(math.isfinite(v) for v in pair)
            or pair[0] > pair[1]
        ):
            raise ValueError("ordered finite intervals required")
    if gain[0] <= 0 or y[1] < offset[0]:
        raise ValueError("positive gain and feasible nonnegative signal required")
    return (max(0.0, (y[0] - offset[1]) / gain[1]), (y[1] - offset[0]) / gain[0])


@dataclass(frozen=True)
class Evidence:
    kind: str
    context: str
    protocol: str
    controls: frozenset
    observables: frozenset
    unit_ids: tuple
    source: str


@dataclass(frozen=True)
class Claim:
    kind: str
    context: str
    protocol: str
    controls: frozenset
    observables: frozenset
    minimum_units: int


def admissible(evidence, claim):
    """Metadata coverage only, not truth, effect significance or independent review."""
    ids = evidence.unit_ids
    return (
        evidence.kind == claim.kind
        and evidence.context == claim.context
        and evidence.protocol == claim.protocol
        and claim.controls <= evidence.controls
        and claim.observables <= evidence.observables
        and type(claim.minimum_units) is int
        and claim.minimum_units >= 1
        and len(ids) >= claim.minimum_units
        and len(ids) == len(set(ids))
        and all(isinstance(v, str) and bool(v) for v in ids)
        and isinstance(evidence.source, str)
        and bool(evidence.source)
    )


def summarize_units(reads):
    """Each key is one independently prepared unit; technical readings are averaged."""
    if not reads or any(not isinstance(k, str) or not k for k in reads):
        raise ValueError("named independent units required")
    means = []
    count = 0
    for values in reads.values():
        if not values or not all(math.isfinite(v) for v in values):
            raise ValueError("nonempty finite readings required")
        means.append(statistics.mean(values))
        count += len(values)
    return {
        "units": len(means),
        "technical_reads": count,
        "mean": statistics.mean(means),
        "sample_sd": statistics.stdev(means) if len(means) > 1 else None,
    }


TABLES = [
    (
        "kinetics",
        ["$t$", "$A$", "$I$", "$B$", "Reduced $B$"],
        ["t", "A", "I", "B", "reduced"],
        "rrrrr",
    ),
    (
        "fuel",
        ["$F_0$", "$B(20)$", "$F(20)$", "Pool error"],
        ["F0", "B", "F", "error"],
        "rrrr",
    ),
]
PLOTS = [("kinetic-lines", "kinetics", "t", ["B", "reduced", "I"])]
LISTINGS = [
    "euler_step",
    "held_fuel",
    "calibrated_interval",
    "admissible",
    "summarize_units",
]


def results():
    rates = Rates(0.1, 0.9, 0.1)
    kinetics = []
    for t in (0, 1, 2, 5, 10, 20, 40, 80):
        a, i, b = held_fuel(1, 0.1, 0.9, 0.1, t)
        kinetics.append(
            {"t": t, "A": a, "I": i, "B": b, "reduced": -math.expm1(-0.01 * t)}
        )
    fuel = []
    for f0 in (0.1, 1.0, 10.0):
        a, f, i, b, w = simulate((1.0, f0, 0.0, 0.0, 0.0), rates, 20, 0.002)
        fuel.append(
            {
                "F0": f0,
                "B": b,
                "F": f,
                "error": max(abs(a + i + b - 1), abs(f + i + w - f0)),
            }
        )
    return {
        "kinetics": kinetics,
        "fuel": fuel,
        "calibration": calibrated_interval((0.48, 0.52), (0.08, 0.12), (0.9, 1.1)),
        "replicates": summarize_units(
            {"unit-a": [0.4, 0.42], "unit-b": [0.1, 0.12], "unit-c": [0.38, 0.4]}
        ),
    }
