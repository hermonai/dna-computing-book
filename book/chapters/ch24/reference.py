"""DNAD-24 resource models, not laboratory protocols or fitted chemistry."""

from math import exp, expm1, log, log1p, isfinite, fsum, lgamma
import json
import random

AVOGADRO = 6.02214076e23  # exact SI mol^-1
BOLTZMANN = 1.380649e-23  # exact SI J/K


def integer(value, minimum=0):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError("integer outside the declared domain")


def scalar(value, minimum=0, strictly=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("real finite quantity required")
    if not isfinite(value) or value < minimum or (strictly and value == minimum):
        raise ValueError("quantity outside the declared domain")


def probability(value):
    scalar(value)
    if value > 1:
        raise ValueError("probability must not exceed one")


def candidates(bits):
    integer(bits)
    return 1 << bits


def molecule_expectation(concentration_molar, volume_litre):
    scalar(concentration_molar)
    scalar(volume_litre)
    return concentration_molar * volume_litre * AVOGADRO


def poisson_complete(species, mean_copies):
    """Independent Poisson counts for each species; all must be nonzero."""
    integer(species, 1)
    scalar(mean_copies)
    if mean_copies == 0:
        return 0.0
    # expm1 prevents 1-exp(-mu) cancellation when mu is tiny.
    nonempty_log = (
        log(-expm1(-mean_copies)) if mean_copies < 1 else log1p(-exp(-mean_copies))
    )
    return exp(species * nonempty_log)


def coverage_copies(species, failure):
    """Exact independent-Poisson requirement for P(all present) >= 1-failure."""
    integer(species, 1)
    probability(failure)
    if not 0 < failure < 1:
        raise ValueError("a finite, nonzero failure tolerance in (0,1) required")
    return -log(-expm1(log1p(-failure) / species))


def coverage_union_copies(species, failure):
    integer(species, 1)
    probability(failure)
    if not 0 < failure < 1:
        raise ValueError("failure tolerance in (0,1) required")
    return log(species) - log(failure)


def coverage_volume(species, failure, concentration_molar):
    scalar(concentration_molar, strictly=True)
    return (
        species * coverage_copies(species, failure) / (AVOGADRO * concentration_molar)
    )


def dilution_volume(c_stock, c_final, v_final):
    """Incoming r01 bookkeeping retained; consistent units, simple dilution only."""
    for value in (c_stock, c_final, v_final):
        scalar(value, strictly=True)
    if c_final > c_stock:
        raise ValueError("simple dilution cannot up-concentrate")
    return c_final * v_final / c_stock


def species_wait(species, total_concentration_molar, association_per_molar_second):
    """Pseudo-first-order target association, equal species concentrations."""
    integer(species, 1)
    scalar(total_concentration_molar, strictly=True)
    scalar(association_per_molar_second, strictly=True)
    return species / (association_per_molar_second * total_concentration_molar)


def serial_mean(depth, rate_per_second):
    integer(depth)
    scalar(rate_per_second, strictly=True)
    return depth / rate_per_second


def erlang_complete(depth, rate_per_second, time_second):
    """CDF of depth independent equal-rate exponential stages; depth <= 256."""
    integer(depth)
    if depth > 256:
        raise ValueError("reference is limited to 256 serial stages")
    scalar(rate_per_second, strictly=True)
    scalar(time_second)
    if depth == 0:
        return 1.0
    x = rate_per_second * time_second
    if not isfinite(x):
        raise ValueError("rate times time must be finite")
    if x == 0:
        return 0.0
    if x >= depth:
        lower = fsum(exp(-x + k * log(x) - lgamma(k + 1)) for k in range(depth))
        return max(0.0, 1 - lower)
    term = exp(-x + depth * log(x) - lgamma(depth + 1))
    terms = [term]
    for k in range(depth + 1, 10000):
        term *= x / k
        terms.append(term)
        if term <= 1e-16 * fsum(terms):
            break
    return min(1.0, fsum(terms))


def parallel_complete(depth, rate_per_second, time_second, jobs):
    """Independent jobs; chemistry coupling/depletion excluded."""
    integer(jobs)
    if jobs == 0:
        return 1.0
    per_job = erlang_complete(depth, rate_per_second, time_second)
    return per_job**jobs


def diffusion_time(length_metre, diffusion_metre2_per_second, dimensions=3):
    """Time whose free Brownian RMS displacement equals length, not mixing time."""
    scalar(length_metre)
    scalar(diffusion_metre2_per_second, strictly=True)
    integer(dimensions, 1)
    if dimensions > 3:
        raise ValueError("physical spatial dimension is one, two or three")
    return length_metre**2 / (2 * dimensions * diffusion_metre2_per_second)


def detection_probability(copies, efficiency):
    """Poisson count and independent thinning; at least one detectable molecule."""
    scalar(copies)
    probability(efficiency)
    return -expm1(-copies * efficiency)


def required_detectable_copies(failure, efficiency):
    probability(failure)
    probability(efficiency)
    if not 0 < failure < 1 or efficiency == 0:
        raise ValueError("positive efficiency and tolerance in (0,1) required")
    return -log(failure) / efficiency


def readout_time(bits, bits_per_second):
    integer(bits)
    scalar(bits_per_second, strictly=True)
    return bits / bits_per_second


def erasure_lower_bound(bits, kelvin):
    """Ideal unbiased-bit quasistatic erasure bound, not DNA reaction expenditure."""
    integer(bits)
    scalar(kelvin, strictly=True)
    return bits * BOLTZMANN * kelvin * log(2)


def fixed_draw_complete(species, draws):
    """Exact small coupon-collector DP oracle: fixed count, NOT Poissonized."""
    integer(species, 1)
    integer(draws)
    if species > 128 or draws > 4096:
        raise ValueError("small exact-DP oracle budget exceeded")
    p = [1.0] + [0.0] * species
    for _ in range(draws):
        q = [0.0] * (species + 1)
        for seen, value in enumerate(p):
            q[seen] += value * seen / species
            if seen < species:
                q[seen + 1] += value * (species - seen) / species
        p = q
    return p[-1]


def poisson_coverage_monte_carlo(species, mean_copies, trials=4000, seed=24):
    """Sample total Poisson arrivals with exponential clock; allocate uniformly."""
    integer(species, 1)
    scalar(mean_copies, strictly=True)
    integer(trials, 1)
    if species * mean_copies > 10000:
        raise ValueError("Monte Carlo oracle budget exceeded")
    rng = random.Random(seed)
    success = 0
    horizon = species * mean_copies
    for _ in range(trials):
        time = 0.0
        seen = set()
        while True:
            time += rng.expovariate(1)
            if time > horizon:
                break
            seen.add(rng.randrange(species))
        success += len(seen) == species
    return success / trials


def results():
    scaling = []
    for bits in (10, 20, 30, 40, 50, 60):
        species = candidates(bits)
        copies = coverage_copies(species, 0.05)
        scaling.append(
            {
                "bits": bits,
                "species": species,
                "copies_per_species": copies,
                "total_copies": species * copies,
                "volume_litre_at_1uM": coverage_volume(species, 0.05, 1e-6),
                "nominal_wait_second": species_wait(species, 1e-6, 1e6),
            }
        )
    curves = [
        {
            "time": t,
            "single": erlang_complete(4, 0.1, t),
            "ten": parallel_complete(4, 0.1, t, 10),
            "hundred": parallel_complete(4, 0.1, t, 100),
        }
        for t in range(0, 201, 5)
    ]
    observation = [
        {"efficiency": e, "copies": required_detectable_copies(0.05, e)}
        for e in (1, 0.1, 0.01)
    ]
    return {
        "assumptions": "All numbers are teaching models, not measurements or a feasible device design.",
        "scaling": scaling,
        "curves": curves,
        "detection": observation,
        "poisson_oracle": {
            "species": 8,
            "copies": 3,
            "trials": 4000,
            "seed": 24,
            "exact": poisson_complete(8, 3),
            "sampled": poisson_coverage_monte_carlo(8, 3),
            "fixed_24_draws": fixed_draw_complete(8, 24),
        },
        "transport": [
            {"length_metre": length, "rms_time_second": diffusion_time(length, 1e-10)}
            for length in (1e-6, 1e-4, 1e-3)
        ],
        "readout_1Mbit_at_100kbit_second": readout_time(1_000_000, 100_000),
        "ideal_1bit_erasure_300K_joule": erasure_lower_bound(1, 300),
    }


TABLES = [
    (
        "scaling",
        ["Input bits", "Species", "Copies/species", "Volume (L)"],
        ["bits", "species", "copies_per_species", "volume_litre_at_1uM"],
        "rrrr",
    ),
    (
        "detection",
        ["Efficiency", "Required mean copies"],
        ["efficiency", "copies"],
        "rr",
    ),
    (
        "transport",
        ["Length (m)", "RMS timescale (s)"],
        ["length_metre", "rms_time_second"],
        "rr",
    ),
]
PLOTS = [("latency-plot", "curves", "time", ["single", "ten", "hundred"])]
LISTINGS = [
    "coverage_copies",
    "coverage_volume",
    "erlang_complete",
    "detection_probability",
    "fixed_draw_complete",
]

if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
