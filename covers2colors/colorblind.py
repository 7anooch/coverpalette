"""Utilities for checking color maps for color-blind friendliness.
"""

import math
from typing import Iterable, Tuple

# Transformation matrices from Vischeck for simulating color vision deficiency
# RGB values should be in the range 0-1
_CVD_MATRICES = {
    "protanopia": (
        (0.56667, 0.43333, 0.0),
        (0.55833, 0.44167, 0.0),
        (0.0, 0.24167, 0.75833),
    ),
    "deuteranopia": (
        (0.625, 0.375, 0.0),
        (0.7, 0.3, 0.0),
        (0.0, 0.3, 0.7),
    ),
    "tritanopia": (
        (0.95, 0.05, 0.0),
        (0.0, 0.43333, 0.56667),
        (0.0, 0.475, 0.525),
    ),
}


def _simulate_cvd(rgb: Tuple[float, float, float], deficiency: str) -> Tuple[float, float, float]:
    """Return ``rgb`` transformed to simulate a color vision deficiency."""

    matrix = _CVD_MATRICES.get(deficiency)
    if not matrix:
        raise ValueError(f"Unknown deficiency: {deficiency}")

    r, g, b = rgb
    r2 = r * matrix[0][0] + g * matrix[0][1] + b * matrix[0][2]
    g2 = r * matrix[1][0] + g * matrix[1][1] + b * matrix[1][2]
    b2 = r * matrix[2][0] + g * matrix[2][1] + b * matrix[2][2]
    return r2, g2, b2


def _color_distance(c1: Tuple[float, float, float], c2: Tuple[float, float, float]) -> float:
    """Euclidean distance between two RGB triples."""

    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))


def is_colorblind_friendly(colors: Iterable[Tuple[float, float, float]], deficiency: str = "deuteranopia", threshold: float = 0.1) -> bool:
    """Check if a set of colors remains distinct for a color vision deficiency.

    Parameters
    ----------
    colors:
        Iterable of RGB tuples with values between 0 and 1.
    deficiency:
        One of ``"protanopia"``, ``"deuteranopia"`` or ``"tritanopia"``.
    threshold:
        Minimum distance between colors after simulation. Smaller values flag
        colors as indistinguishable.
    Returns
    -------
    bool
        ``True`` if all simulated color pairs are farther apart than
        ``threshold``.
    """

    simulated = [_simulate_cvd(c, deficiency) for c in colors]
    for i in range(len(simulated)):
        for j in range(i + 1, len(simulated)):
            if _color_distance(simulated[i], simulated[j]) < threshold:
                return False
    return True
