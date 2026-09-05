#!/usr/bin/env python3
"""Build the companion paper from the maintained proof notes.

Requires pandoc and a LaTeX installation with amsmath, lmodern and hyperref.
The build does not certify the mathematical arguments.
"""
from pathlib import Path
import hashlib
import subprocess
import re
import json

ROOT=Path(__file__).resolve().parents[1]
SOURCES=[('I. Fixed-strength flat kicks','mathematics/pell_fixed_strength_review.md'),
         ('II. Analytic Poisson rigidity','mathematics/analytic_poisson_flatness_rigidity.md'),
         ('III. The sharp single-orbit extremum','mathematics/pell_sharp_orbit_coercivity.md'),
         ('IV. A sharp multiorbit Fourier-box inequality','mathematics/pell_four_mode_coercivity.md')]
HEADER=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,microtype,booktabs,longtable,array,calc}
\usepackage[hidelinks]{hyperref}
\setlength{\emergencystretch}{3em}
\setcounter{secnumdepth}{0}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\title{Flat Quantum Conjugacies, Analytic Rigidity,\\and Sharp Resonance Minima}
\author{WoW research programme}
\date{5 September 2026}
\begin{document}
\maketitle
\begin{abstract}
We verify a fixed-strength smooth nonlinear cat-map construction with
arbitrary inverse-power quantum conjugacy and polynomial-time spectral
control. Its arithmetic structure survives through smooth symplectic
conjugacy. We audit the existing analytic Poisson-rigidity argument and derive a
quantitative quantum lower bound. The existing Pell sharp minimum is
generalized to a single Fourier orbit of every hyperbolic integral
determinant-one matrix, at every finite support length. The
lower bound is attained through a real Fejer--Riesz spectral factor. A
separate exact sum-of-squares identity solves the complete first Fourier
box, retaining the interference terms between frequency orbits.
These are project proofs with independent finite checks, not a claim of
priority or positive BGS universality.
\end{abstract}
'''

def keep_small_tables(tex):
    # These proof notes contain only short tables; keep each on one page.
    tex=tex.replace(r"\begin{longtable}[]", r"\begin{center}\begin{tabular}")
    tex=tex.replace(r"\end{longtable}", r"\bottomrule\end{tabular}\end{center}")
    tex=re.sub(r"\\endhead\s*\\bottomrule\\noalign\{\}\s*\\endlastfoot", "", tex)
    return tex


def main():
    chunks=[HEADER]
    for number,(title,path) in enumerate(SOURCES):
        source=ROOT/path
        chunks.append('% '+path+' SHA256 '+hashlib.sha256(source.read_bytes()).hexdigest()+'\n')
        if number: chunks.append('\\clearpage\n' if number==3 else '\\bigskip\n')
        chunks.append('\\section*{'+title+'}\n')
        chunks.append(keep_small_tables(subprocess.check_output(['pandoc',str(source),'-f','markdown+tex_math_single_backslash','-t','latex','--wrap=none'],text=True)))
    data=json.loads((ROOT/'evidence/rigidity_validation.json').read_text())
    chunks.append(r"\section*{Finite operator diagnostics}")
    chunks.append(r"The same fixed classical strength $\kappa=0.02$ is used at every $N$. "
                  r"These are full-space operator norms from the exact nodal formula, "
                  r"evaluated in floating point. No fitted convergence rate or interval certificate is asserted.")
    chunks.append(r"\begin{center}\begin{tabular}{rrr}\toprule $N$ & $\|[A_N,D_N]\|$ & $\|J_N^*V_NJ_N-U_N\|$ \\ \midrule")
    for row in data['flat_operator_checks']:
        chunks.append(f"{row['N']} & {row['commutator_operator_norm']:.5g} & {row['gauge_operator_error']:.5g}"+r" \\")
    chunks.append(r"\bottomrule\end{tabular}\end{center}")
    chunks.append(r"The exact single-orbit checks comprise 726 Python/C++ comparisons plus 720 checks "
                  r"for three further matrices. The multiorbit quartic is checked coefficientwise over "
                  r"the integers, with 80 independent C++ samples and the radius-three integer witness. "
                  r"Raw reports, command exit codes and source hashes accompany the paper. "
                  r"No new Lean compilation or repository-wide green CI is claimed.")
    chunks.append('\\end{document}\n')
    output=ROOT/'manuscript/rigidity_and_sharp_resonance.tex'
    output.write_text(''.join(chunks),encoding='utf-8')
    print(output)

if __name__=='__main__':main()
