#!/usr/bin/env python3
"""Idempotent registration and deterministic rendering of coboundary research.

No mathematical status is inferred from a render or from a successful build.
The proof and evidence remain separate files. Existing sections are not replaced.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess

ROOT=Path(__file__).resolve().parents[2]


def append_once(path: str, marker: str, addition: str) -> None:
    p=ROOT/path
    text=p.read_text(encoding='utf-8')
    if marker not in text:
        p.write_text(text.rstrip()+'\n\n'+addition.strip()+'\n',encoding='utf-8')


def integrate() -> None:
    append_once('CMakeLists.txt','add_executable(pell_coboundary_pairs ','''
add_executable(pell_coboundary_pairs computations/cpp/pell_coboundary_pairs.cpp)
target_include_directories(pell_coboundary_pairs PRIVATE ${Boost_INCLUDE_DIRS})
if(MSVC)
  target_compile_options(pell_coboundary_pairs PRIVATE /W4)
else()
  target_compile_options(pell_coboundary_pairs PRIVATE -Wall -Wextra -Wpedantic)
endif()
''')
    append_once('formalization/Bgs.lean','import Bgs.PellCoboundary','import Bgs.PellCoboundary')
    description='''
## Second-order coboundary resonance

For the different fixed Fourier kick `H=B_(1,0)-B_(3,4)`, the first-order
period average vanishes. A uniform second-order loop bound, together with
an exact two-species multiplicity-two theorem, gives a deterministic
wrapped-normal recurrence law at quantum strength
`epsilon ~ sqrt(N) K^(-1/4)`. Its classical action amplitude still tends to
zero. Bounded `|epsilon| K^(1/4)/sqrt(N)` obstructs any bounded globally
unfolded pair density tending to one at large separation; escaping this
obstruction is necessary, not sufficient, for universality.

The complete proof is [the coboundary note](mathematics/pell_coboundary_resonance.md).
The second-order residual mechanism has direct prior literature, audited in
[literature/pell_coboundary_sources.md](literature/pell_coboundary_sources.md).
No world-priority, fixed-system BGS, or complete analytic Lean claim is made.
The independent Python/C++ and finite Lean components have narrower scope.
'''
    append_once('README.md','## Second-order coboundary resonance',description)
    append_once('mathematics/results.md','## Coboundary resonance extension','''
## Coboundary resonance extension

[pell_coboundary_resonance.md](pell_coboundary_resonance.md) proves the uniform
second-order loop estimate; classifies all four-atom two-species collisions;
derives the wrapped-normal recurrence law at `epsilon ~ sqrt(N) K^(-1/4)`;
and obtains necessary escape and subcritical microscopic-collapse criteria.
This is a project proof with unestablished priority. Residual fidelity freeze
is prior art. It concerns a specified vanishing-classical-kick family, not
positive BGS universality. Exact finite pair certificates, numerical operator
checks, and Lean compilation records are distinct verification layers.
''')
    append_once('record/claim_ledger.md','## Coboundary continuation, 2026-09-05','''
## Coboundary continuation, 2026-09-05

PROJECT PROOF: `mathematics/pell_coboundary_resonance.md`, Theorems 1--2,
Lemmas 3--4 and 6, Corollary 5. The proof combines a uniform second-order
loop estimate and exact multiplicity-two arithmetic with a two-species
Gaussian limit. Its quantum critical scale is `sqrt(N) K^(-1/4)` for a
specified coboundary kick; the classical amplitude still tends to zero.
The necessary escape criterion is not a sufficient universality criterion.

FINITE EVIDENCE: `evidence/certificates/pell_coboundary_audit.json` records
independent original-coordinate Python and quadratic-ring C++ enumeration,
phase and dense-operator checks, all numerical fourth moments, and retained
first and second recurrence modes including their finite-size deviations.
Seeded RMS errors are not deterministic intervals. The Lean module covers
an integer identity and finite K=11 counts, not an analytic limit theorem;
its compilation is certified only by an actual successful build log.

PRIORITY: second-order residual perturbations and quantum fidelity freeze
are established prior work. No first-ever or prize-level claim is made.
OPEN: fixed classical perturbations, positive microscopic BGS universality,
correct full symmetry resolution, and Heisenberg-scale joint trace control.
''')
    p=ROOT/'manuscript/arithmetic_cat_map_moments.tex'
    s=p.read_text(encoding='utf-8')
    command=r'\input{pell_coboundary_section.tex}'
    anchor=r'\begin{thebibliography}'
    if command not in s:
        if s.count(anchor)!=1:
            raise RuntimeError('Expected one main-manuscript bibliography anchor')
        p.write_text(s.replace(anchor,command+'\n\n'+anchor),encoding='utf-8')


def figures() -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    data=json.loads((ROOT/'evidence/certificates/pell_coboundary_audit.json').read_text())
    dst=ROOT/'assets/figures'; dst.mkdir(exist_ok=True)
    rows=[r for r in data['fourth_checks'] if r['K']>=11]
    fig,ax=plt.subplots(figsize=(7.5,4.6))
    ax.errorbar([r['K'] for r in rows],[r['odd_fourth_center'] for r in rows],
                yerr=[r['odd_fourth_noncentral_bound'] for r in rows],fmt='o',capsize=3,
                label='Central Weyl convolution; analytic odd-tail bound')
    ax.axhline(3,linestyle='--',label='Gaussian fourth moment')
    ax.set_xscale('log');ax.set_xlabel('Odd prime period K');ax.set_ylabel('Normalized fourth moment')
    ax.set_title('Generated two-species observable');ax.legend(fontsize=8);ax.grid(alpha=.2)
    fig.tight_layout();fig.savefig(dst/'pell_coboundary_fourth.png',dpi=170);plt.close(fig)
    fig,ax=plt.subplots(figsize=(7.5,4.6))
    for m,marker in ((1,'o'),(2,'s')):
        r=[x for x in data['dense_checks'] if x['m']==m and x['tau']==1.]
        ax.plot([x['K'] for x in r],[x['actual_trace_real'] for x in r],marker=marker,
                linestyle='none',label=f'm={m}: complete dense odd spectrum')
        r=[x for x in data.get('sampled_checks',[]) if x['m']==m and x['tau']==1.]
        if r:
            ax.errorbar([x['K'] for x in r],[x['trace_real'] for x in r],
                        yerr=[x['complex_RMS_bound'] for x in r],fmt=marker,capsize=3,
                        label=f'm={m}: sparse trace estimate (RMS bars)')
        ax.axhline(np.exp(-m*m/2),linestyle='--',label=f'm={m}: limiting value')
    ax.set_xlabel('Odd prime period K');ax.set_ylabel('Real normalized recurrence trace')
    ax.set_title('Actual coboundary-kicked propagator, critical parameter t=1')
    ax.legend(fontsize=7);ax.grid(alpha=.2);fig.tight_layout()
    fig.savefig(dst/'pell_coboundary_echo.png',dpi=170);plt.close(fig)


def render() -> None:
    src=ROOT/'mathematics/pell_coboundary_resonance.md'
    body=subprocess.check_output(['pandoc',str(src),'-f','markdown','-t','latex','--wrap=none'],text=True)
    header=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,graphicx,microtype}
\usepackage[hidelinks]{hyperref}
\setlength{\emergencystretch}{3em}
\setcounter{secnumdepth}{0}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\title{A second-order resonance scale for\\coboundary kicks of a fixed cat map}
\author{WoW research programme}
\date{5 September 2026}
\begin{document}
\maketitle
'''
    footer=r'''
\clearpage
\section*{Reproducible diagnostics}
\begin{center}
\includegraphics[width=.88\linewidth]{../assets/figures/pell_coboundary_fourth.png}
\end{center}
\noindent Central fourth moments are evaluated by Weyl convolution, not
matrix diagonalization. Bars bound the noncentral odd trace analytically;
floating-point evaluation of the center is not interval-certified.
\begin{center}
\includegraphics[width=.88\linewidth]{../assets/figures/pell_coboundary_echo.png}
\end{center}
\noindent Both recurrence modes are retained, including the visible finite-size
bias of the second mode. Sampled bars are complex RMS bounds over independent
random probes, not confidence intervals or deterministic error bars.
\end{document}
'''
    out=ROOT/'manuscript/pell_coboundary_resonance.tex'
    out.write_text('% Source SHA256: '+hashlib.sha256(src.read_bytes()).hexdigest()+'\n'+header+body+footer,encoding='utf-8')


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--integrate-only',action='store_true')
    args=p.parse_args()
    integrate()
    if not args.integrate_only:
        figures();render()
    print('Coboundary registration complete; no verification status inferred.')

if __name__=='__main__':
    main()
