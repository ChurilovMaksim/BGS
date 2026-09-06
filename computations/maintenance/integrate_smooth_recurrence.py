#!/usr/bin/env python3
"""Idempotent source integration and rendering for the smooth continuation.

Run --integrate-only before verification. Full rendering consumes an existing
PASS certificate; it does not infer mathematical proof or compilation status.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PROOF = 'mathematics/smooth_recurrence_and_compensation.md'
VERIFIER = 'computations/verification/smooth_recurrence_and_compensation.py'
CERTIFICATE = 'evidence/certificates/smooth_recurrence_and_compensation.json'


def append_once(name: str, marker: str, text: str) -> None:
    p = ROOT/name
    old = p.read_text(encoding='utf-8')
    if marker not in old:
        p.write_text(old.rstrip()+'\n\n'+text.strip()+'\n', encoding='utf-8')


def integrate() -> None:
    # Preserve the historical run identity and source/log hashes. This fixes
    # an omitted producer field, not a claim that a new execution took place.
    p = ROOT/'evidence/certificates/pell_coboundary_validation.json'
    if p.exists():
        d = json.loads(p.read_text())
        if 'producer' not in d:
            d['producer'] = '.github/workflows/coboundary-validation.yml'
            d['provenance_annotation'] = 'Missing producer field restored; original run, input commit and recorded hashes unchanged.'
            p.write_text(json.dumps(d, indent=2)+'\n')
    p = ROOT/'.github/workflows/coboundary-validation.yml'
    if p.exists():
        text = p.read_text()
        if "data={'input_commit':" in text:
            text = text.replace("data={'input_commit':", "data={'producer':'.github/workflows/coboundary-validation.yml','input_commit':", 1)
            p.write_text(text)
    p = ROOT/'computations/verification/pell_coboundary_fourth_moment.py'
    if p.exists():
        text = p.read_text().replace("'producer': str(Path(__file__).name)", "'producer': 'computations/verification/pell_coboundary_fourth_moment.py'")
        p.write_text(text)
    # The imported module exports hermitian_exponential and Weyl matrices,
    # not odd_basis/expi/hs. Keep independent local basis/norm definitions.
    p = ROOT/'computations/verification/pell_weighted_echo_regression.py'
    if p.exists():
        text = p.read_text()
        pattern = r'^from pell_floquet_regression import ([^\n]+)$'
        match = re.search(pattern, text, flags=re.M)
        if match and any(x in match.group(1).split(', ') for x in ('odd_basis', 'hs', 'expi')):
            allowed = {'design', 'weyl', 'odd_basis', 'hs', 'expi'}
            names = {x.strip() for x in match.group(1).split(',')}
            if not names <= allowed:
                raise RuntimeError('Unexpected echo imports; refusing a speculative rewrite')
            replacement = '''from pell_floquet_regression import design, weyl, hermitian_exponential as expi


def odd_basis(n: int) -> np.ndarray:
    if n < 3 or n % 2 == 0:
        raise ValueError("odd N>=3 required")
    d=(n-1)//2
    q=np.zeros((n,d),dtype=complex)
    for j in range(1,d+1):
        q[j,j-1]=1/np.sqrt(2)
        q[n-j,j-1]=-1/np.sqrt(2)
    return q


def hs(a: np.ndarray) -> float:
    return float(np.linalg.norm(a,"fro")/np.sqrt(a.shape[0]))
'''
            text = re.sub(pattern, lambda _: replacement, text, count=1, flags=re.M)
        text = re.sub(r'(\b\w+\s*,\s*\w+\s*,\s*\w+)\s*,\s*_\s*=\s*design\(', r'\1 = design(', text)
        p.write_text(text)
    append_once('formalization/Bgs.lean', 'import Bgs.PellFourierKernel', 'import Bgs.PellFourierKernel')
    append_once('README.md', '## Smooth Green--Kubo recurrence and compensation', '''
## Smooth Green--Kubo recurrence and compensation

The [complete smooth continuation](mathematics/smooth_recurrence_and_compensation.md)
extends the quantum Pell recurrence law to all fixed real mean-zero C6
observables. The full-space theorem uses the classical Green--Kubo variance;
odd-space statements require inversion-even symbols. A C7 residual generator
admits a covariance-bearing mixed law and an explicitly compensated family
with uniform operator error `C_g |epsilon|^3/N^2 + D_g epsilon^2/N^3`.

The compensated pinning range is `epsilon=o(N^(2/3) K^(-1/3))`. Compensation
changes the family. The classical action amplitude still tends to zero, and
times remain fixed multiples of the arithmetic period. No positive BGS,
world-priority, or full analytic Lean formalization is claimed.

The [independent finite verifier](computations/verification/smooth_recurrence_and_compensation.py)
separates exact rational Fourier-tail checks from floating-point operator
falsifiers and retains nonzero mixed third moments. The Lean addition covers
integer telescoping, reconstruction and coordinate parity only. Actual logs
and source-hashed manifests determine execution status.
''')
    append_once('mathematics/results.md', '## Smooth Green--Kubo continuation', '''
## Smooth Green--Kubo continuation

[Complete proof](smooth_recurrence_and_compensation.md): support-dependent
finite Fourier normal forms; all fixed C6 observable recurrence limits;
general C7 residual/covariant crossover; and an explicitly compensated
microscopic-pinning regime. Classical variance and residual commutator
mechanisms are attributed to prior work. Positive fixed-system BGS and
Heisenberg-scale trace comparison are not proved.
''')
    append_once('record/claim_ledger.md', '## Smooth Green--Kubo continuation, 2026-09-05', '''
## Smooth Green--Kubo continuation, 2026-09-05

PROJECT PROOF: `mathematics/smooth_recurrence_and_compensation.md`, Theorems
1--3. All C6 fixed real mean-zero symbols are covered on the full space;
inversion-even symbols also admit the entire odd-space statement. The
residual generator is C7 and the mixed Green--Kubo covariance is retained.
The wider pinning range belongs to an explicitly compensated family, not
the unchanged residual kick.

SCOPE: odd prime K and its possibly composite Pell modulus; fixed recurrence
orders; vanishing classical action amplitude. No priority certification,
fixed-strength positive BGS, or analytic Lean proof is asserted.

FINITE VERIFICATION: exact Fraction Fourier-tail and integer pair tests;
nonzero mixed third moments; direct finite matrices including physical Weyl
signs and non-vacuous small-exponent controls. Floating-point checks are not
interval certificates. `Bgs.PellFourierKernel` proves only integer kernels;
compilation status requires an actual build log. Historical producer-field
repair does not change the historical execution identity or source hashes.
''')
    section = r'''\section{Smooth observables and compensated residual kicks}
For each fixed real mean-zero $C^6$ observable $f$, the Pell quantization
satisfies the project theorem
\[
 \frac1N\operatorname{Tr}(e^{i\tau A_N(f)/\sqrt K}U_0)^{mK}
      \longrightarrow e^{-m^2\tau^2\sigma_f^2/2}.
\]
Here $m,\tau$ are fixed and $\sigma_f^2$ is the classical Green--Kubo
variance. The odd-space version requires inversion-even $f$. A growing
Fourier cutoff is controlled by a support-dependent normal form and an exact
second-moment tail identity, rather than an unjustified interchange of limits.
For a real $C^7$ symbol $g$, put $d=g\circ T^{\mathsf T}$,
$r_g=\{g,d\}/(4\pi)$, $A=A_N(g)$, $D=A_N(d)$ and $R=A_N(r_g)$.
The mixed kick $e^{i[\varepsilon(A-D)+\eta A_N(f)]}U_0$ has recurrence
variance $\sigma_{a f+t r_g}^2$ when $\sqrt K\eta\to a$ and
$\sqrt K\varepsilon^2/N\to t$. Its mixed covariance need not vanish.
The explicitly compensated, different family obeys
\[
 \left\|e^{-i\varepsilon A}
   (e^{i[\varepsilon(A-D)-\varepsilon^2R/N]}U_0)e^{i\varepsilon A}-U_0\right\|
 \leq C_g\frac{|\varepsilon|^3}{N^2}+D_g\frac{\varepsilon^2}{N^3}.
\]
For $\varepsilon=o(N^{2/3}K^{-1/3})$ its globally unfolded spacings collapse
and close-pair counts diverge. Its classical action still vanishes. The full
proof, finite constants and prior-art boundary are in the smooth companion
article. These are project proofs, not positive BGS or full analytic Lean
formalization. Cohen--Conze and Prosen--Znidaric provide the directly relevant
classical variance and residual-perturbation precedents.
'''
    (ROOT/'manuscript/smooth_recurrence_section.tex').write_text(section)
    p = ROOT/'manuscript/arithmetic_cat_map_moments.tex'
    text = p.read_text()
    marker = r'\input{smooth_recurrence_section.tex}'
    anchor = r'\begin{thebibliography}'
    if marker not in text:
        if text.count(anchor) != 1:
            raise RuntimeError('Unexpected bibliography structure')
        p.write_text(text.replace(anchor, marker+'\n\n'+anchor))


def render() -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    data = json.loads((ROOT/CERTIFICATE).read_text())
    if data.get('status') != 'PASS':
        raise RuntimeError('No successful finite source certificate')
    if data['source_sha256'] != hashlib.sha256((ROOT/VERIFIER).read_bytes()).hexdigest():
        raise RuntimeError('Source certificate is stale')
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    for group in data['matrix_checks']:
        rows = sorted((r for r in group['operator_checks'] if r['is_compensated'] and r['epsilon'] > 0), key=lambda r:r['epsilon'])
        ax.loglog([r['epsilon'] for r in rows], [r['operator_error'] for r in rows], marker='o', label=f"K={group['K']}: operator error")
        ax.loglog([r['epsilon'] for r in rows], [r['analytic_bound'] for r in rows], linestyle='--', label=f"K={group['K']}: analytic bound")
    ax.set_xlabel('Quantum exponent epsilon')
    ax.set_ylabel('Operator norm distance after compensation')
    ax.set_title('Finite smooth-symbol controls; no Gaussian fitting')
    ax.legend(fontsize=7); ax.grid(alpha=.2); fig.tight_layout()
    destination = ROOT/'assets/figures/smooth_recurrence_compensation.png'
    destination.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destination, dpi=180); plt.close(fig)
    body = subprocess.check_output(['pandoc', str(ROOT/PROOF), '-f', 'markdown', '-t', 'latex', '--wrap=none'], text=True)
    header = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,graphicx,microtype}
\usepackage[hidelinks]{hyperref}
\setlength{\emergencystretch}{3em}
\setcounter{secnumdepth}{0}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\title{Smooth Green--Kubo recurrence\\and compensated residual kicks}
\author{WoW research programme}
\date{5 September 2026}
\begin{document}
\maketitle
'''
    footer = r'''
\clearpage
\section*{Finite diagnostic}
\begin{center}
\includegraphics[width=.95\linewidth]{../assets/figures/smooth_recurrence_compensation.png}
\end{center}
The finite trigonometric symbol includes an odd coordinate-product frequency
and tests the physical Weyl sign. Points are direct matrix exponentials.
Dashed curves are analytic operator bounds; floating-point rounding is not
interval-certified. The all-smooth theorem is proved by Fourier approximation,
not extrapolation of these matrices. The source certificate retains both
compensated and uncompensated controls, including finite-size deviations.
\end{document}
'''
    digest = hashlib.sha256((ROOT/PROOF).read_bytes()).hexdigest()
    (ROOT/'manuscript/smooth_recurrence_and_compensation.tex').write_text('% Proof SHA256: '+digest+'\n'+header+body+footer)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--integrate-only', action='store_true')
    args = parser.parse_args()
    integrate()
    if not args.integrate_only:
        render()
    print('Sources integrated; no analytic proof or execution status inferred.')


if __name__ == '__main__':
    main()
