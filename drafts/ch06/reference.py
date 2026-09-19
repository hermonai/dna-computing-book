"""Restricted duplex equilibrium, not a general oligonucleotide design tool."""

from collections import Counter
import math
import json

R = 1.98720425864083  # cal mol^-1 K^-1
STANDARD_M = 1.0
# SantaLucia 1998 Table 2: kcal/mol, cal/(mol K), at 1 M NaCl.
NN = {
    "AA": (-7.9, -22.2),
    "AT": (-7.2, -20.4),
    "TA": (-7.2, -21.3),
    "CA": (-8.5, -22.7),
    "GT": (-8.4, -22.4),
    "CT": (-7.8, -21.0),
    "GA": (-8.2, -22.2),
    "CG": (-10.6, -27.2),
    "GC": (-9.8, -24.4),
    "GG": (-8.0, -19.9),
}


def finite(value, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("finite numerical quantity required")
    if not math.isfinite(value) or (value <= 0 if positive else value < 0):
        raise ValueError("quantity outside physical domain")
    return value


def reverse_complement(sequence):
    if not isinstance(sequence, str) or set(sequence) - set("ACGT"):
        raise ValueError("canonical uppercase DNA required")
    return sequence.translate(str.maketrans("ACGT", "TGCA"))[::-1]


def nn_parameters(sequence, sodium_m=1.0):
    rc = reverse_complement(sequence)
    if len(sequence) < 2 or sequence == rc:
        raise ValueError("at least two bases; distinct partner required")
    if sodium_m != 1.0:
        raise ValueError("this implementation supports only 1 M NaCl")
    dh, ds = 0.0, 0.0
    counts = Counter()
    for i in range(len(sequence) - 1):
        step = sequence[i : i + 2]
        key = step if step in NN else reverse_complement(step)
        h, s = NN[key]
        dh += h
        ds += s
        counts[key] += 1
    for end in (sequence[0], sequence[-1]):
        h, s = (2.3, 4.1) if end in "AT" else (0.1, -2.8)
        dh += h
        ds += s
    return {
        "dh_kcal": dh,
        "ds_cal": ds,
        "steps": dict(sorted(counts.items())),
    }


def kd_from_thermo(dh_kcal, ds_cal, kelvin):
    finite(kelvin, positive=True)
    if not all(math.isfinite(v) for v in (dh_kcal, ds_cal)):
        raise ValueError("finite thermodynamic parameters required")
    log_kd = (1000 * dh_kcal - kelvin * ds_cal) / (R * kelvin)
    if not -700 < log_kd < 700:
        raise ValueError("equilibrium constant outside numerical budget")
    return STANDARD_M * math.exp(log_kd)


def duplex_molar(a_total, b_total, kd):
    """Physical root of (a-x)(b-x)=Kd*x, using scaled stable arithmetic."""
    for v in (a_total, b_total, kd):
        finite(v)
    if min(a_total, b_total) == 0:
        return 0.0
    scale = max(a_total, b_total, kd)
    a, b, k = (v / scale for v in (a_total, b_total, kd))
    discriminant = (a - b) ** 2 + k * (2 * (a + b) + k)
    return scale * (2 * a * b) / (a + b + k + math.sqrt(discriminant))


def melting_kelvin(dh_kcal, ds_cal, each_strand_m):
    finite(each_strand_m, positive=True)
    denominator = ds_cal + R * math.log(each_strand_m / (2 * STANDARD_M))
    if denominator == 0:
        raise ValueError("no finite melting point in this model")
    temperature = 1000 * dh_kcal / denominator
    finite(temperature, positive=True)
    return temperature


def results():
    rows = []
    for sequence in ("ACGTCAGT", "AGCTACGT"):
        p = nn_parameters(sequence)
        kd = kd_from_thermo(p["dh_kcal"], p["ds_cal"], 310.15)
        rows.append(
            {
                "sequence": sequence,
                **p,
                "kd_37_m": kd,
                "tm_100nm_c": melting_kelvin(
                    p["dh_kcal"], p["ds_cal"], 1e-7
                )
                - 273.15,
            }
        )
    p = nn_parameters("ACGTCAGT")
    return {
        "scope": "ideal two-species duplex equilibrium; Table 2 parameters, 1 M NaCl",
        "exact_example": {
            "a_nm": 100,
            "b_nm": 100,
            "kd_nm": 5,
            "duplex_nm": duplex_molar(100e-9, 100e-9, 5e-9) * 1e9,
            "free_each_nm": 20,
        },
        "nn_table": NN,
        "sequence_comparison": rows,
        "concentration_curve": [
            {
                "b_nm": b,
                "exact_fraction": duplex_molar(100e-9, b * 1e-9, 5e-9)
                / 100e-9,
                "excess_approximation": b / (b + 5),
            }
            for b in (1, 5, 10, 20, 50, 100, 200, 500, 1000)
        ],
        "melting_curve": [
            {
                "celsius": t,
                **{
                    str(c): duplex_molar(
                        c * 1e-9,
                        c * 1e-9,
                        kd_from_thermo(
                            p["dh_kcal"], p["ds_cal"], t + 273.15
                        ),
                    )
                    / (c * 1e-9)
                    for c in (10, 100, 1000)
                },
            }
            for t in range(0, 81, 2)
        ],
        "melting_points": [
            {
                "each_nm": c,
                "celsius": melting_kelvin(
                    p["dh_kcal"], p["ds_cal"], c * 1e-9
                )
                - 273.15,
            }
            for c in (10, 100, 1000)
        ],
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
