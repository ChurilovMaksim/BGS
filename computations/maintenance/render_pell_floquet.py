#!/usr/bin/env python3
"""Generate the companion TeX from its authoritative Markdown proof."""
from pathlib import Path
import hashlib
import subprocess

ROOT=Path(__file__).resolve().parents[2]

def main() -> None:
    src=ROOT/'mathematics/pell_floquet_normal_form.md'
    body=subprocess.check_output(['pandoc',str(src),'-f','markdown','-t','latex','--wrap=none'],text=True)
    body=body.replace(r'\section{Related primary records}',r'\section{Related primary records}'+chr(10)+r'\small')
    digest=hashlib.sha256(src.read_bytes()).hexdigest()
    header=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,graphicx,microtype}
\usepackage[hidelinks]{hyperref}
\setlength{\emergencystretch}{3em}
\setcounter{secnumdepth}{0}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\title{A resonance-scale spectral law for a\\deterministically kicked Pell cat map}
\author{WoW research programme}
\date{5 September 2026}
\begin{document}
\maketitle
'''
    footer=r'''
\normalsize
\clearpage
\section*{Reproducible numerical diagnostics}
\begin{center}
\includegraphics[width=\linewidth]{../assets/figures/pell_floquet_echo.png}
\end{center}
\noindent These are actual propagator traces, not fitted observable densities.
Both Fourier modes are retained. Bars for the sampled traces represent
an RMS bound over the random probes, not deterministic error bounds or
confidence intervals. The visible finite-size bias is not removed.
\begin{center}
\includegraphics[width=\linewidth]{../assets/figures/pell_floquet_commutators.png}
\end{center}
\noindent The constant bounds are analytic; the points are independent
finite evaluations. Exact pair-key checks use both diagonal coordinates
(Python) and original integral map coordinates (C++20).
\end{document}
'''
    dst=ROOT/'manuscript/pell_floquet_normal_form.tex'
    dst.write_text('% Generated from mathematics/pell_floquet_normal_form.md\n% Source SHA256: '+digest+'\n'+header+body+footer)
    print('Generated',dst.relative_to(ROOT),'from',digest)

if __name__=='__main__':
    main()
