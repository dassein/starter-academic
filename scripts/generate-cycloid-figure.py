#!/usr/bin/env python3
"""Generate an accessible, self-contained SVG of the exact ICML 2024 cycloid.

Source: Luo and Hashemi, Unveiling the Cycloid Trajectory of EM Iterations
in Mixed Linear Regression, ICML 2024, Propositions 4.3 and 4.4, Eqs. (9)-(10).
https://arxiv.org/html/2405.18237v2#S4
Official proceedings: https://proceedings.mlr.press/v235/luo24c.html

Assumptions: symmetric two-component mixed linear regression with parameters
+theta_star and -theta_star; independent standard Gaussian covariates;
noiseless population EM (the zero-noise limiting update). Mixture weights
need not be balanced. This draws the positive-correlation, upper branch in
the plane spanned by the initial estimate and theta_star, normalized by
||theta_star||. The initial direction has varphi_0 = 0.15 radians, so it is
neither parallel nor orthogonal to theta_star. theta_0 itself is not drawn.

For phi in [0, pi], the exact cycloid branch is
    x = 1 - (phi - sin(phi))/pi,
    y = (1 - cos(phi))/pi.
With varphi_t = pi/2 - acos(rho_t), rho_t > 0, population EM obeys
    tan(varphi_t) = tan(varphi_(t-1))
                    + varphi_(t-1) * (1 + tan(varphi_(t-1))**2).
The plotted theta_t, t >= 1, uses phi_(t-1) = pi - 2*varphi_(t-1).

The smooth line is the locus of possible updates; it is not a continuous
time trajectory. Finite-sample or noisy EM is not exactly on this curve.
Coordinates have the same screen scale on both axes to preserve geometry.

Usage: python3 scripts/generate-cycloid-figure.py content/publication/em_2mlr/cycloid-explained.svg
Requires only Python's standard library. No external fonts or images.
"""

from __future__ import annotations

import html
import json
import math
from pathlib import Path
import sys


BLUE = "#1565c0"
INK = "#243447"
MUTED = "#526477"
AXIS = "#a3b2c1"
WIDTH, HEIGHT = 760, 710
LEFT, BASE, SCALE = 110.0, 515.0, 520.0
INITIAL_VARPHI = 0.15
SOURCE = "https://arxiv.org/html/2405.18237v2#S4"


def cycloid(phi: float) -> tuple[float, float]:
    return 1.0 - (phi - math.sin(phi)) / math.pi, (1.0 - math.cos(phi)) / math.pi


def screen(point: tuple[float, float]) -> tuple[float, float]:
    x, y = point
    return LEFT + SCALE * x, BASE - SCALE * y


def em_iterates(count: int = 5) -> list[dict]:
    """Return theta_1...theta_count; check against Corollary 3.3 as well."""
    varphi = INITIAL_VARPHI
    points = []
    for iteration in range(1, count + 1):
        phi = math.pi - 2.0 * varphi
        x, y = cycloid(phi)
        # Corollary 3.3, normalized, with theta/||theta||=(sin(v),cos(v)).
        direct_x = 2.0 / math.pi * (varphi + math.cos(varphi) * math.sin(varphi))
        direct_y = 2.0 / math.pi * math.cos(varphi) ** 2
        assert math.isclose(x, direct_x, abs_tol=1e-14)
        assert math.isclose(y, direct_y, abs_tol=1e-14)
        next_varphi = math.atan(math.tan(varphi) + varphi / math.cos(varphi) ** 2)
        assert math.isclose(next_varphi, math.atan2(x, y), abs_tol=1e-14)
        points.append({"iteration": iteration, "varphi_previous": varphi, "x": x, "y": y})
        varphi = next_varphi
    assert all(a["x"] < b["x"] and a["y"] > b["y"] for a, b in zip(points, points[1:]))
    return points


def text(x: float, y: float, value: str, *, size=24, fill=INK, anchor="start", extra="") -> str:
    return f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" {extra}>{html.escape(value)}</text>'


def create_svg() -> str:
    points = em_iterates()
    curve = [screen(cycloid(math.pi * (1.0 - i / 360.0))) for i in range(361)]
    curve_d = " ".join(("M" if i == 0 else "L") + f"{x:.4f},{y:.4f}" for i, (x, y) in enumerate(curve))
    top = BASE - SCALE * 2.0 / math.pi
    metadata = {
        "source": SOURCE,
        "propositions": ["4.3", "4.4"],
        "normalization": "theta / ||theta_star||",
        "initial_varphi_radians": INITIAL_VARPHI,
        "iterates": points,
        "curve_is_locus_not_continuous_time_path": True,
    }
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="cycloid-title cycloid-desc">',
        '<title id="cycloid-title">Exact cycloid geometry of population EM</title>',
        '<desc id="cycloid-desc">A blue cycloid branch with five numbered, exact population expectation-maximization estimates approaching the true parameter at coordinate (1, 0). The horizontal axis is the normalized component along the true parameter; the vertical axis is the normalized orthogonal component. The plot assumes noiseless symmetric two-component mixed linear regression with standard Gaussian covariates. The initial direction has varphi zero equal to 0.15 radians. Theta one is the first update, not the initial estimate. The curve is an exact update locus, not a continuous-time path. Equal scales are used on both axes. Source: Luo and Hashemi, ICML 2024, Propositions 4.3 and 4.4.</desc>',
        f'<metadata>{html.escape(json.dumps(metadata, ensure_ascii=False))}</metadata>',
        '<rect width="760" height="710" fill="#ffffff"/>',
        '<g font-family="Arial, Helvetica, sans-serif">',
        text(58, 54, "EM updates lie on a cycloid", size=34, extra='font-weight="700"'),
        text(58, 92, "Noiseless population EM · Gaussian covariates", size=23, fill=MUTED),
        text(58, 122, "Symmetric two-component mixed linear regression", size=23, fill=MUTED),
        f'<path d="M{LEFT:.0f},{top-23:.2f} V{BASE:.0f} H668" fill="none" stroke="{AXIS}" stroke-width="2"/>',
        f'<path d="M{LEFT:.0f},{top:.4f} H630 M370,{top:.4f} V{BASE:.0f}" fill="none" stroke="#e7edf3" stroke-width="1.5" stroke-dasharray="5 7"/>',
        f'<path d="M{LEFT-6:.0f},{top:.4f} h6 M110,515 v7 M370,515 v7 M630,515 v7" fill="none" stroke="{AXIS}" stroke-width="2"/>',
        text(91, top + 8, "2/π", size=23, fill=MUTED, anchor="end"),
        text(LEFT, BASE + 36, "0", size=23, fill=MUTED, anchor="middle"),
        text(370, BASE + 36, "0.5", size=23, fill=MUTED, anchor="middle"),
        text(630, BASE + 36, "1", size=23, fill=MUTED, anchor="middle"),
        text(370, 590, "Component along the true parameter", size=23, anchor="middle"),
        '<text transform="translate(37 361) rotate(-90)" font-size="23" fill="#243447" text-anchor="middle">Orthogonal component</text>',
        f'<path d="{curve_d}" fill="none" stroke="{BLUE}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
    ]
    # Leader lines keep the last two labels separate from the limiting solution.
    labels = [(0, -23), (0, -24), (-20, -24), (-38, -9), (-45, -22)]
    for point, (dx, dy) in zip(points, labels):
        sx, sy = screen((point["x"], point["y"]))
        t = point["iteration"]
        if t >= 4:
            parts.append(f'<path d="M{sx+dx+15:.2f},{sy+dy+4:.2f} L{sx-8:.2f},{sy-2:.2f}" fill="none" stroke="{BLUE}" stroke-width="1.5"/>')
        parts.append(f'<circle cx="{sx:.4f}" cy="{sy:.4f}" r="7.5" fill="{BLUE}" stroke="#ffffff" stroke-width="2"><title>theta {t}: ({point["x"]:.8f}, {point["y"]:.8f})</title></circle>')
        parts.append(f'<text x="{sx+dx:.2f}" y="{sy+dy:.2f}" font-size="27" fill="{BLUE}" text-anchor="middle">θ<tspan baseline-shift="sub" font-size="19">{t}</tspan></text>')
    parts.extend([
        '<circle cx="630" cy="515" r="7" fill="#243447" stroke="#ffffff" stroke-width="2"><title>True parameter, normalized coordinate (1, 0)</title></circle>',
        text(651, 526, "θ*", size=28),
        '<circle cx="113" cy="625" r="7" fill="#1565c0"/>',
        text(134, 634, "Five exact EM updates; θ₁ is the first update.", size=23),
        text(110, 666, "Coordinates normalized by ‖θ*‖; equal axis scales.", size=22, fill=MUTED),
        f'<a href="https://proceedings.mlr.press/v235/luo24c.html">{text(110, 696, "Luo &amp; Hashemi · ICML 2024 · Props. 4.3–4.4".replace("&amp;", "&"), size=21, fill=BLUE)}</a>',
        '</g>',
        '</svg>',
    ])
    return "\n".join(parts) + "\n"


if __name__ == "__main__":
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/zhankun-cycloid.svg")
    output.write_text(create_svg(), encoding="utf-8")
    print(f"Wrote {output}")
    print(json.dumps(em_iterates(), indent=2))
