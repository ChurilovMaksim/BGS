# Figure index

Created 20 October 2026 (repository audit, finding Ж-1 / В-2). This index
records, for every figure in `assets/`, its generator where one is known,
and its canonical format. For figures that exist as a PNG+SVG pair, the
**SVG is canonical** and the PNG is a derived preview. Figures with no
recorded generator are maintained manual SVG; their captions live with
the surfaces that use them and must be checked against the SVG by hand.

| Figure | Generator (`computations/analysis/`) | Canonical format | Notes |
|---|---|---|---|
| `figures/bgs_frontier.svg` | none recorded — manual SVG | SVG | Key scheme; no scripted regeneration |
| `figures/trace_ramp_plateau.svg` | none recorded — manual SVG | SVG | Key scheme; no scripted regeneration |
| `figures/scientific_evidence_layers.svg` | none recorded — manual SVG | SVG | No scripted regeneration |
| `research_pipeline.svg` | none recorded — manual SVG | SVG | No scripted regeneration |
| `verification_stack.svg` | none recorded — manual SVG | SVG | No scripted regeneration |
| `figures/cayley_trace_gaussian.svg` | `cayley_trace_limit_figure.py` | SVG | |
| `figures/correlation_bandwidth.svg` | `correlation_bandwidth_figure.py` | SVG | |
| `figures/microscopic_pair_reference.svg` | `microscopic_pair_reference.py` | SVG | Analytic benchmark curves, not measured data |
| `figures/pell_harmonic_returns.svg` | `pell_harmonic_returns_figure.py` | SVG | |
| `figures/pell_harmonic_transition.svg` | `pell_harmonic_transition_figure.py` | SVG | |
| `figures/return_obstruction.svg` | `return_obstruction_figure.py` | SVG | |
| `magnetic_quotient_global.svg` / `.png` | `magnetic_spectrum_figure.py` | SVG (PNG derived) | Pair with identical stem |
| `figures/pell_floquet_commutators.svg` / `.png` | `pell_floquet_figure.py` | SVG (PNG derived) | Pair with identical stem |
| `figures/pell_floquet_echo.svg` / `.png` | `pell_floquet_figure.py` | SVG (PNG derived) | Pair with identical stem |
| `figures/pell_coboundary_echo.png` | none recorded | PNG only | **Requires regeneration**: no vector source; a generator script must be added or recovered before this figure can be maintained as SVG |
| `figures/pell_coboundary_fourth.png` | none recorded | PNG only | **Requires regeneration**: no vector source; see above |
| `figures/pell_fourth_moment.png` | none recorded | PNG only | **Requires regeneration**: no vector source; see above |

## Manuscript use (blocked conversion)

The consolidated manuscript (`manuscript/BGS_unified.tex`) currently
includes no figures. The three key schemes — `bgs_frontier`,
`trace_ramp_plateau` and `microscopic_pair_reference` — exist **only as
SVG**, and no PNG or PDF rendering of them exists anywhere in the
repository (checked against the full file inventory on 20 October 2026).
LaTeX cannot include the SVG files directly, so no `\includegraphics`
was added for them: a reviewed SVG→PDF/PNG conversion step, with the
renderings committed alongside the sources, is required first. When the
figures are included, their captions must carry the same qualifications
as the README surfaces (for example, the pair-reference figure depicts
analytic benchmark curves, **not measured data**).
