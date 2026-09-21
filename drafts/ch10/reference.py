"""Synthetic measurement models; not an instrument or assay calibration."""

import math
import numpy as np


def vector(values, positive=False):
    a = np.asarray(values, dtype=float)
    if a.ndim != 1 or not np.isfinite(a).all():
        raise ValueError("finite vector required")
    if positive and np.any(a <= 0):
        raise ValueError("positive values required")
    return a


def calibrate(lengths, distances):
    """Fit x = a - b log10(L); lengths in bp, distances in mm."""
    length, x = vector(lengths, True), vector(distances)
    if len(length) != len(x) or len(x) < 2:
        raise ValueError("at least two matched ladder observations")
    u = np.log10(length)
    design = np.column_stack((np.ones(len(u)), -u))
    coef, _, rank, _ = np.linalg.lstsq(design, x, rcond=None)
    if rank != 2 or coef[1] <= 0:
        raise ValueError("nondegenerate decreasing calibration required")
    return dict(
        a=float(coef[0]),
        b=float(coef[1]),
        low=float(min(x)),
        high=float(max(x)),
        residual=(x - design @ coef).tolist(),
    )


def infer_length(distance, calibration):
    """Interpolation only; uncertainty in fitted coefficients is separate."""
    if not math.isfinite(distance):
        raise ValueError("finite distance required")
    if not calibration["low"] <= distance <= calibration["high"]:
        raise ValueError("outside calibrated migration interval")
    return 10 ** ((calibration["a"] - distance) / calibration["b"])


def band_kernel(edges, centers, widths):
    """Each column integrates a unit-area Gaussian over detector bins."""
    e, c, s = vector(edges), vector(centers), vector(widths, True)
    if len(e) < 2 or np.any(np.diff(e) <= 0) or len(c) != len(s):
        raise ValueError(
            "ordered edges and matched centers/widths required"
        )
    z = (e[:, None] - c[None, :]) / (math.sqrt(2) * s[None, :])
    erf = np.vectorize(math.erf, otypes=[float])(z)
    return np.diff(0.5 * (1 + erf), axis=0)


def response_matrix(edges, centers, widths, lengths, gain=1.0):
    """Gain is integrated signal per bp per molecule-equivalent."""
    length = vector(lengths, True)
    kernel = band_kernel(edges, centers, widths)
    if (
        len(length) != kernel.shape[1]
        or not math.isfinite(gain)
        or gain <= 0
    ):
        raise ValueError(
            "matched lengths and positive finite gain required"
        )
    return kernel * (gain * length)[None, :]


def observe(matrix, counts, background=0.0, ceiling=None):
    a, n = np.asarray(matrix, dtype=float), vector(counts)
    if (
        a.ndim != 2
        or a.shape[1] != len(n)
        or not np.isfinite(a).all()
        or np.any(a < 0)
        or np.any(n < 0)
        or not math.isfinite(background)
        or background < 0
    ):
        raise ValueError("nonnegative finite measurement model required")
    y = background + a @ n
    if ceiling is not None:
        if not math.isfinite(ceiling) or ceiling <= 0:
            raise ValueError("positive finite ceiling required")
        y = np.minimum(y, ceiling)
    return y


def unmix(matrix, signal, noise_sd):
    """Weighted least squares, known background removed, independent noise."""
    a = np.asarray(matrix, dtype=float)
    y, sd = vector(signal), vector(noise_sd, True)
    if (
        a.ndim != 2
        or a.shape[0] != len(y)
        or len(sd) != len(y)
        or min(a.shape) == 0
        or not np.isfinite(a).all()
    ):
        raise ValueError("matched finite observations/design required")
    aw, yw = a / sd[:, None], y / sd
    u, singular, vt = np.linalg.svd(aw, full_matrices=False)
    cutoff = np.finfo(float).eps * max(aw.shape) * singular[0]
    if len(singular) < a.shape[1] or np.any(singular <= cutoff):
        raise ValueError("species are not identifiable in this design")
    estimate = vt.T @ ((u.T @ yw) / singular)
    covariance = (vt.T / singular**2) @ vt
    return dict(
        estimate=estimate.tolist(),
        covariance=covariance.tolist(),
        sd=np.sqrt(np.diag(covariance)).tolist(),
        condition=float(singular[0] / singular[-1]),
        residual=(y - a @ estimate).tolist(),
    )


def roi_summary(signal_pixels, blank_pixels, pixel_variance):
    """Independent pixels with known common variance; one shared blank mean."""
    y, blank = vector(signal_pixels), vector(blank_pixels)
    if not len(y) or not len(blank):
        raise ValueError("nonempty signal and blank regions required")
    if not math.isfinite(pixel_variance) or pixel_variance < 0:
        raise ValueError("finite nonnegative variance required")
    m, k = len(y), len(blank)
    net = y.sum() - m * blank.mean()
    variance = pixel_variance * (m + m * m / k)
    return float(net), math.sqrt(variance)


def collect_window(lo, hi, centers, widths, counts, target=0):
    """Ideal collection by position; purity counts molecules, not base pairs."""
    n = vector(counts)
    if np.any(n < 0) or type(target) is not int or not 0 <= target < len(n):
        raise ValueError("nonnegative counts and valid target required")
    fraction = band_kernel([lo, hi], centers, widths)[0]
    if len(fraction) != len(n):
        raise ValueError("one count per species required")
    captured = n * fraction
    total = float(captured.sum())
    return dict(
        recovery=float(fraction[target]),
        purity=None if total == 0 else float(captured[target] / total),
        captured=captured.tolist(),
    )


def results():
    lengths = [250, 500, 1000, 2000]
    distances = [100 - 20 * math.log10(v) for v in lengths]
    cal = calibrate(lengths, distances)
    grid = np.linspace(35, 57, 111)
    centers = [46.0, 49.0]
    a = response_matrix(grid, centers, [1.2, 1.2], [500, 400], 0.002)
    profiles = [
        dict(
            x=float((grid[i] + grid[i + 1]) / 2),
            target=float(a[i, 0] * 7),
            other=float(a[i, 1] * 3),
            total=float(a[i] @ [7, 3]),
        )
        for i in range(len(grid) - 1)
    ]
    ambiguity = np.array([[1.0, 1.0], [0.2, 0.2], [0.5, 0.5]])
    extra = np.vstack((ambiguity, [1.0, 0.1]))
    return dict(
        ladder=[
            dict(length=l, distance=x) for l, x in zip(lengths, distances)
        ],
        inferred_length=infer_length(45, cal),
        profiles=profiles,
        same_signal=observe(ambiguity, [7, 3]).tolist(),
        alternative_signal=observe(ambiguity, [10, 0]).tolist(),
        resolved=unmix(extra, extra @ [7.0, 3.0], np.ones(4) * 0.1),
        uncertainty=[
            dict(
                delta=d,
                sd=unmix([[1, 1], [0, d]], [10, 3 * d], [0.1, 0.1])["sd"][
                    0
                ],
            )
            for d in [1, 0.5, 0.2, 0.1, 0.05, 0.01]
        ],
        windows=[
            dict(
                width=w,
                **collect_window(
                    46 - w, 46 + w, centers, [1.2, 1.2], [7, 3]
                ),
            )
            for w in [0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
        ],
        roi=list(roi_summary([12, 14, 13, 11], [2, 2, 2, 2], 1)),
    )
