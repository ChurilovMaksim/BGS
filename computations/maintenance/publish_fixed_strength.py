#!/usr/bin/env python3
"""Register and render fixed-strength locality; never infer a proof from a build."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]


def append_once(name: str, marker: str, text: str) -> None:
    p=ROOT/name
    old=p.read_text(encoding='utf-8')
    if marker not in old:
        p.write_text(old.rstrip()+'\n\n'+text.strip()+'\n',encoding='utf-8')


def integrate() -> None:
    # Repair a single transport-only escape at the end of equation (21).
    proof=ROOT/'mathematics/fixed_strength_locality.md'
    original=proof.read_text()
    fixed=[]
    for line in original.splitlines(keepends=True):
        body=line.rstrip('\n')
        if body.startswith(r' \|V_{\kappa,N}^t-') and body.endswith('\\|\\'):
            line=body[:-1]+'\n'
        fixed.append(line)
    normalized=''.join(fixed)
    if normalized!=original: proof.write_text(normalized)
    for target in ('pell_floquet_pair_verifier','spectral_lattice_clustering',
                   'pell_minimal_relation_verifier','fixed_strength_locality_exact'):
        if (ROOT/f'computations/cpp/{target}.cpp').exists():
            append_once('CMakeLists.txt',f'add_executable({target} ',f'''
add_executable({target} computations/cpp/{target}.cpp)
target_include_directories({target} PRIVATE ${{Boost_INCLUDE_DIRS}})
if(MSVC)
  target_compile_options({target} PRIVATE /W4)
else()
  target_compile_options({target} PRIVATE -Wall -Wextra -Wpedantic)
endif()
''')
    for module in ('PellCohomology','PellEchoWeights','LocalityKernels'):
        if (ROOT/f'formalization/Bgs/{module}.lean').exists():
            append_once('formalization/Bgs.lean',f'import Bgs.{module}',f'import Bgs.{module}')
    for dependency in ('scipy==1.17.0','mpmath==1.3.0','matplotlib==3.10.8'):
        append_once('requirements.txt',dependency.split('==')[0]+'==',dependency)
    p=ROOT/'computations/verification/pell_weighted_echo_regression.py'
    text=p.read_text()
    broken='from pell_floquet_regression import design, odd_basis, weyl, expi, hs'
    if broken in text:
        text=text.replace(broken,'''from pell_floquet_regression import design, weyl, hermitian_exponential

def odd_basis(n):
    q=np.zeros((n,(n-1)//2),dtype=complex)
    j=np.arange(1,(n+1)//2)
    q[j,j-1]=1/math.sqrt(2)
    q[n-j,j-1]=-1/math.sqrt(2)
    return q

def expi(a,t):
    return hermitian_exponential(a,t)

def hs(a):
    return float(np.linalg.norm(a,'fro')/math.sqrt(len(a)))''')
        text=text.replace('n,f,h,_=design(k)','n,f,h=design(k)')
        p.write_text(text)
    append_once('README.md','## Fixed-strength locality and long-time conjugacy','''
## Fixed-strength locality and long-time conjugacy

The [locality proof](mathematics/fixed_strength_locality.md) treats a fixed
nonzero classical kick, not the earlier shrinking-strength limit. Disjoint
smooth supports make the natural one-exponential coboundary kick conjugate
to the cat propagator modulo every inverse power of N in operator norm.
This persists through Heisenberg and all fixed polynomial times. An explicit
Gevrey-2 bump gives a conservative stretched-exponential bound.

Odd Pell spectra retain K superpolynomially narrow equal-rank clusters.
Spacing collapse, diverging close-pair counts, and an empty random-origin
local point-process limit survive any polynomially distorted unfolding.
These maps are smoothly conjugate to the arithmetic cat map: inherited
structure is essential, and no generic BGS or priority claim is made.

The independent exact C++ and numerical Python verifiers have distinct
scope. The Lean module proves algebraic support kernels only. Actual build
and execution status is recorded separately in the evidence manifests.
''')
    append_once('mathematics/results.md','## Fixed-strength disjoint-support family','''
## Fixed-strength disjoint-support family

[Complete project proof](fixed_strength_locality.md): all-orders operator-norm
conjugacy for a natural fixed-classical-strength kick; all polynomial times;
a conservative Gevrey-2 stretched-exponential estimate; microscopic clusters
and empty local process even after polynomially bounded unfolding.
The hypothesis implies exact smooth classical conjugacy to the arithmetic
model. This is a controlled exceptional family, not positive BGS universality.
''')
    append_once('record/claim_ledger.md','## Fixed-strength locality, 2026-09-05','''
## Fixed-strength locality, 2026-09-05

PROJECT PROOF: Theorems A-C in `mathematics/fixed_strength_locality.md`.
Disjoint smooth supports cancel every local Weyl-product coefficient.
The quantitative Fourier remainder and a Duhamel inequality give operator-norm
conjugacy at fixed classical strength and all polynomial times. Odd Pell
spectra form equal-rank superpolynomial clusters, with spacing collapse,
exact eventual close-pair counts, and an empty random-origin local limit.
The latter conclusions persist under polynomially bounded unfolding.

STRUCTURAL LIMIT: the classical maps are smoothly conjugate to an arithmetic
cat map. Approximate quantum commutants are inherited. This does not prove
universal BGS, eliminate hidden arithmetic structure, or establish priority.

FINITE CHECKS: Python physical-Weyl and separable Fourier constructions,
refinement and quadrature diagnostics, actual single-kick matrices; independent
integer C++ Moyal and cluster counts. Floating-point refinement is not interval
certification. `LocalityKernels.lean` covers only scaled support inequalities
and finite algebra. Its compilation status belongs to actual logs, not to the
existence of its source. No analytic theorem is claimed Lean-proved.
''')
    append_once('README.md','## Stability above the mean-spacing scale','''
## Stability above the mean-spacing scale

The [covering and robustness addendum](mathematics/locality_robustness.md)
shows that the negative local-statistics conclusions survive any unitary
perturbation of operator norm o(1/K), even if it is much larger than 1/D.
A K-arc cover of length ell gives explicit bounds for long gaps, close pairs,
and the probability that a random-origin window meets a level. A nonempty
local limit after unfolding requires a corresponding nonvanishing image
cover length; the explicit Gevrey example forces a stretched-exponential
lower bound on the unfolding's Lipschitz constant. These are stability
results for an arithmetic-conjugate family, not generic BGS universality.
''')
    append_once('mathematics/results.md','## Covering stability under larger spectral errors','''
## Covering stability under larger spectral errors

[Proof and finite estimates](locality_robustness.md): a cover by K arcs with
K/D tending to zero and total length ell tending to zero forces gap collapse,
close-pair divergence, and an empty random-origin local process. This applies
to arbitrary unitary errors o(1/K) around the locality family. Quantitative
unfolding distortion bounds and exact rational regressions are separate
from the operator estimates and their numerical diagnostics.
''')
    append_once('record/claim_ledger.md','## Locality robustness, 2026-09-05','''
## Locality robustness, 2026-09-05

PROJECT PROOF: equations R1-R10 in `mathematics/locality_robustness.md`.
The covering length, rather than individual agreement below 1/D, controls
the negative local-statistics limit. Any additional unitary norm error
eta_N with K eta_N tending to zero preserves the three collapse statements.
The same classical principal map alone does not imply that norm hypothesis.

FINITE EVIDENCE: `locality_robustness.py` performs exact rational gap,
ordered-pair and origin-union calculations, before and after an independent
piecewise-linear unfolding. Successful command logs and hashes, not source
existence, establish execution. No general BGS or new-priority claim is made.
''')
    p=ROOT/'manuscript/arithmetic_cat_map_moments.tex'
    text=p.read_text()
    marker='fixed_strength_section.tex'
    anchor=r'\begin{thebibliography}'
    if marker not in text:
        if text.count(anchor)!=1:
            raise RuntimeError('Unexpected main bibliography; no automatic rewrite')
        inc=(r'\IfFileExists{manuscript/fixed_strength_section.tex}'
             r'{\input{manuscript/fixed_strength_section.tex}}'
             r'{\input{fixed_strength_section.tex}}')
        p.write_text(text.replace(anchor,inc+'\n\n'+anchor))


def render() -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    sys.path.insert(0,str(ROOT/'computations/verification'))
    from fixed_strength_locality import symbol
    data=json.loads((ROOT/'evidence/certificates/fixed_strength_locality.json').read_text())
    dst=ROOT/'assets/figures';dst.mkdir(parents=True,exist_ok=True)
    q,p=np.meshgrid(np.linspace(0,1,601),np.linspace(0,1,601))
    g=symbol(q,p);d=symbol(3*q+4*p,2*q+3*p)
    fig,ax=plt.subplots(figsize=(7.2,5.2))
    c1=ax.contour(q,p,g,levels=[.001,.2,.6],linestyles='solid')
    c2=ax.contour(q,p,d,levels=[.001,.2,.6],linestyles='dashed')
    ax.clabel(c1,inline=True,fontsize=6);ax.clabel(c2,inline=True,fontsize=6)
    ax.set(xlabel='q',ylabel='p',title='Separated symbols: g (solid), g composed with M (dashed)')
    ax.set_aspect('equal');fig.tight_layout();fig.savefig(dst/'fixed_strength_support.png',dpi=170);plt.close(fig)
    rows=data['matrix_checks']
    fig,ax=plt.subplots(figsize=(7.2,4.6))
    ax.loglog([r['N'] for r in rows],[r['odd_kick_conjugacy_operator_error'] for r in rows],
              'o-',label='Actual single-kick conjugacy error')
    ax.loglog([r['N'] for r in rows],[r['trotter_upper_bound'] for r in rows],
              's--',label='Finite commutator-based upper bound')
    ax.set(xlabel='Odd dimension N',ylabel='Operator norm',title='Fixed classical parameter kappa = 1/8')
    ax.legend(fontsize=8);ax.grid(alpha=.2);fig.tight_layout()
    fig.savefig(dst/'fixed_strength_conjugacy.png',dpi=170);plt.close(fig)
    src=ROOT/'mathematics/fixed_strength_locality.md'
    body=subprocess.check_output(['pandoc',str(src),'-f','markdown','-t','latex','--wrap=none'],text=True)
    addendum=ROOT/'mathematics/locality_robustness.md'
    body+='\n\\bigskip\n\\section*{Addendum: stability above the mean-spacing scale}\n'+subprocess.check_output(
        ['pandoc',str(addendum),'-f','markdown','-t','latex','--wrap=none'],text=True)
    header=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,graphicx,microtype}
\usepackage[hidelinks]{hyperref}
\setlength{\emergencystretch}{3em}
\setcounter{secnumdepth}{0}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\title{Fixed-strength coboundary kicks:\\locality, long-time conjugacy, and microscopic clustering}
\author{WoW research programme}
\date{5 September 2026}
\begin{document}
\maketitle
'''
    footer=r'''
\clearpage
\section*{Finite diagnostics, not asymptotic evidence}
\begin{center}
\includegraphics[width=.83\linewidth]{../assets/figures/fixed_strength_support.png}
\end{center}
The solid and dashed contours are computed from the explicit fixed smooth
symbols. The rigorous separation is the rational inequality (13), not a
visual inference from a finite grid.
\begin{center}
\includegraphics[width=.83\linewidth]{../assets/figures/fixed_strength_conjugacy.png}
\end{center}
The plotted error is computed from the actual one-exponential kick. Finite
errors need not decrease monotonically. No asymptotic exponent is fitted;
Fourier refinement and floating-point rounding remain separate error sources.
\end{document}
'''
    (ROOT/'manuscript/fixed_strength_locality.tex').write_text(
        '% Source SHA256: '+hashlib.sha256(src.read_bytes()).hexdigest()+'\n'
        +'% Addendum SHA256: '+hashlib.sha256(addendum.read_bytes()).hexdigest()+'\n'+header+body+footer)


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--integrate-only',action='store_true')
    args=parser.parse_args()
    integrate()
    if not args.integrate_only: render()
    print('Locality integration complete; verification status is not inferred.')

if __name__=='__main__': main()
