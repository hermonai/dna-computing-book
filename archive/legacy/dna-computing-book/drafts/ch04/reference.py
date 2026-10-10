"""Dimensioned teaching models, not calibrated laboratory predictions."""

from decimal import Decimal, localcontext, ROUND_CEILING
from fractions import Fraction
from math import comb, factorial, log
import json

AVOGADRO = Decimal("6.02214076e23")  # specified entities per mole, exact SI


def probability(value):
    p = Decimal(str(value))
    if not p.is_finite() or not 0 <= p <= 1:
        raise ValueError("probability must be finite and in [0,1]")
    return p


def integer(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError("integer outside domain")
    return value


def miss(copies, p):
    integer(copies)
    p = probability(p)
    if copies == 0:
        return 1.0
    if p == 1:
        return 0.0
    if 0 < p < Decimal("1e-50"):
        raise ValueError(
            "probability is below this diagnostic's precision contract"
        )
    with localcontext() as ctx:
        ctx.prec = 80
        return float((Decimal(copies) * (1 - p).ln()).exp())


def required_copies(p, delta):
    """Smallest integer budget in the declared 80-digit log calculation."""
    p, delta = probability(p), probability(delta)
    if not 0 < delta < 1:
        raise ValueError("delta must be strictly between zero and one")
    if p == 0:
        raise ValueError("no finite budget for a zero-probability witness")
    if p == 1:
        return 1
    with localcontext() as ctx:
        ctx.prec = 80
        if p < Decimal("1e-50"):
            raise ValueError(
                "probability is below this diagnostic's precision contract"
            )
        return int(
            (delta.ln() / (1 - p).ln()).to_integral_value(
                rounding=ROUND_CEILING
            )
        )


def expected_distinct(copies, species):
    integer(copies)
    integer(species, 1)
    if copies == 0:
        return 0.0
    if species > 10**50:
        raise ValueError(
            "species count exceeds this diagnostic's precision contract"
        )
    with localcontext() as ctx:
        ctx.prec = 80
        q = Decimal(1) / species
        return float(Decimal(species) * (1 - (1 - q) ** copies))


def all_species_bound(copies, species):
    integer(species, 1)
    with localcontext() as ctx:
        ctx.prec = 80
        return min(1.0, species * miss(copies, Decimal(1) / species))


def finite_pool_miss(population, witnesses, sample):
    for v in (population, witnesses, sample):
        integer(v)
    if witnesses > population or sample > population:
        raise ValueError("sample and witness count must fit population")
    if sample > population - witnesses:
        return Fraction(0)
    return Fraction(
        comb(population - witnesses, sample), comb(population, sample)
    )


def shared_failure(copies, p, failure):
    rho = float(probability(failure))
    return rho + (1 - rho) * miss(copies, p)


def inventory(copies, molarity, length_nt=100, grams_per_mol_nt=330):
    integer(copies)
    integer(length_nt, 1)
    c, mass_unit = Decimal(str(molarity)), Decimal(str(grams_per_mol_nt))
    if (
        not c.is_finite()
        or c <= 0
        or not mass_unit.is_finite()
        or mass_unit <= 0
    ):
        raise ValueError(
            "positive finite concentration and mass approximation required"
        )
    with localcontext() as ctx:
        ctx.prec = 80
        amount = Decimal(copies) / AVOGADRO
        return {
            "moles": float(amount),
            "litres": float(amount / c),
            "grams_ssdna_approx": float(amount * length_nt * mass_unit),
        }


def half_time(k_per_molar_second, excess_molarity):
    k, b = float(k_per_molar_second), float(excess_molarity)
    from math import isfinite

    if not isfinite(k) or not isfinite(b) or k <= 0 or b <= 0:
        raise ValueError("positive finite kinetic inputs required")
    return log(2) / (k * b)


def positive_predictive_value(prior, sensitivity, false_positive):
    pi, s, f = map(
        float, map(probability, (prior, sensitivity, false_positive))
    )
    denominator = pi * s + (1 - pi) * f
    if denominator == 0:
        raise ValueError("positive observation has zero probability")
    return pi * s / denominator


def results():
    with localcontext() as ctx:
        ctx.prec = 80
        rows = []
        for vertices in (10, 15, 20, 25):
            candidates = factorial(vertices - 2)
            p = Decimal(1) / candidates
            copies = required_copies(p, ".01")
            rows.append(
                {
                    "vertices": vertices,
                    "candidate_orders": candidates,
                    "copies_99pct_one_witness": copies,
                    **inventory(copies, "1e-9"),
                }
            )
        one = required_copies(".04", ".01")
        all_four = required_copies(Decimal(1) / 4, Decimal(".01") / 4)
        return {
            "scope": "synthetic independent sampling; quantities are not measurements",
            "single_witness": {
                "q": 0.04,
                "budget": one,
                "miss": miss(one, 0.04),
                "previous_miss": miss(one - 1, 0.04),
            },
            "coverage": {
                "expected_distinct_four_draws": expected_distinct(4, 4),
                "all_four_union_budget": all_four,
                "bound": all_species_bound(all_four, 4),
            },
            "finite_pool": {
                "population": 10,
                "witnesses": 2,
                "sample": 3,
                "miss": float(finite_pool_miss(10, 2, 3)),
                "replacement_miss": miss(3, 0.2),
            },
            "resource_table": rows,
            "miss_curves": [
                {
                    "copies": m,
                    "independent": miss(m, 0.04),
                    "shared_failure_10pct": shared_failure(m, 0.04, 0.1),
                }
                for m in (0, 10, 25, 50, 100, 150, 200)
            ],
            "half_times_seconds": {
                "one_nM": half_time(1e6, 1e-9),
                "ten_nM": half_time(1e6, 1e-8),
            },
            "aliquot": {
                "fraction": 0.01,
                "copies": 100,
                "miss": miss(100, 0.01),
            },
            "readout": {
                "prior": 0.01,
                "sensitivity": 0.9,
                "false_positive": 0.05,
                "positive_predictive_value": positive_predictive_value(
                    0.01, 0.9, 0.05
                ),
            },
        }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
