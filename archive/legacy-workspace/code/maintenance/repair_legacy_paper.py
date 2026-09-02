"""One-off repair of archive/papers/resonance_laws_catmaps.tex against the 2026-08-28 audit.

Line-oriented and newline-agnostic.  Each edit asserts that it found its target,
so the script is safe to re-run (it reports NOOP for edits already applied).
"""
import os
import re
import sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "paper",
                 "resonance_laws_catmaps.tex")
raw = open(P, "rb").read()
crlf = b"\r\n" in raw
text = raw.decode("utf-8", errors="surrogateescape")
lines = text.split("\r\n") if crlf else text.split("\n")
print(f"file has {len(lines)} lines, CRLF={crlf}")
print(f"begin(remark)={sum(1 for l in lines if l.startswith(r'\begin{remark}'))}  "
      f"end(remark)={sum(1 for l in lines if l.strip() == r'\end{remark}')}")

report = []


def find(pred, what):
    hits = [i for i, l in enumerate(lines) if pred(l)]
    if not hits:
        report.append(f"NOOP  {what}")
        return None
    return hits


# ---- E1: close rem:rev, which is left open (nested remark follows)
h = find(lambda l: l.startswith(r"\begin{remark}[Degenerate chart"), "E1 locate")
if h:
    i = h[0]
    # walk back to the last non-blank line before it
    j = i - 1
    while j >= 0 and lines[j].strip() == "":
        j -= 1
    if lines[j].strip() != r"\end{remark}":
        lines.insert(j + 1, r"\end{remark}")
        report.append("E1    inserted \\end{remark} closing rem:rev")
    else:
        report.append("E1    NOOP (already closed)")

# ---- E2: retracted max/median figure
h = find(lambda l: "max/median" in l, "E2 max/median")
if h:
    i = h[0]
    lines[i] = (r"(eigenvalue excess kurtosis $5.9$ and $9.3$, "
                r"$\mathrm{ev}_{\max}/\sigma = 3.8$ and $5.0$; artifact")
    lines.insert(i + 1, r"\texttt{taskA\_entry\_gaussianity.json}).")
    lines.insert(i + 2, r"% RETRACTED 2026-08-28: the figure ``max/median approx 15--40''")
    lines.insert(i + 3, r"% stood here; LEDGER R61 retracted it as a fabrication.")
    report.append("E2    replaced retracted max/median figure")

# ---- E3: U4 bound wrongly attributed to the red team
h = find(lambda l: r"\mathrm{EXTRAS}\le k^3p^{-2\delta}$ under" in l, "E3 U4")
if h:
    i = h[0]
    assert "Bourgain--Garaev input" in lines[i + 1]
    lines[i:i + 4] = [
        r"the red team's actual bound is",
        r"$\mathrm{EXTRAS}\le k^4p^{-2\delta}$ under the Bourgain--Garaev",
        r"input $\sup|S|\le kp^{-\delta}$, whose threshold",
        r"$k\lesssim p^{\delta}$ is vacuous at every published $\delta$;",
        r"the sharper $k^3p^{-2\delta}$ of earlier drafts was \emph{not}",
        r"the red team's correction and is withdrawn (audit 2026-08-28)\\",
    ]
    report.append("E3    U4 bound restated as the red team's actual correction")

# ---- E4: smooth law downgraded from PROVEN to heuristic
h = find(lambda l: "smooth law $N_3" in l and "PROVEN" in l, "E4 smooth law")
if h:
    i = h[0]
    lines[i:i + 1] = [
        r"smooth law $N_3 \le k^2/p + C\sqrt{k}\,(\log p)^{O(1)}$ for",
        r"$k \ge p^{3/7+\varepsilon}$: HEURISTIC, not proven. The only",
        r"derivation on disk, \texttt{drafts/tail\_bound\_attempt.md},",
        r"labels itself heuristic and shows its completion step invalid",
        r"for proper subgroups; the constant is not $1$)\\",
    ]
    report.append("E4    smooth law downgraded to HEURISTIC")

# ---- E5: cor:domination second clause
h = find(lambda l: "also under OSV-conditional smooth law" in l, "E5 domination")
if h:
    i = h[0]
    lines[i:i + 1] = [
        r"PROVEN under Conj.~\ref{conj:tight}. The second clause, via the",
        r"smooth law for $k \ge p^{3/7+\varepsilon}$, is withdrawn: that law",
        r"is heuristic, see the row above\\",
    ]
    report.append("E5    cor:domination second clause withdrawn")

# ---- E6: Hecke-centred decorrelation row retracted
h = find(lambda l: "Hecke-symmetrised entry decorrelation" in l, "E6 hecke row")
if h:
    i = h[0]
    assert "raw kurt" in lines[i + 1]
    lines[i:i + 2] = [
        r"Hecke-centred entry decorrelation & RETRACTED 2026-08-28: the",
        r"centring is a Haar average, whose expectation is a multiple of the",
        r"identity and cannot change an off-diagonal entry; the observed",
        r"``collapse'' is finite-sample noise from an unnormalised accumulator,",
        r"and the multiplet basis used was a set of columns of the propagator,",
        r"not eigenvectors. See",
        r"\texttt{artifacts/r71/hecke\_centring\_refutation.json}\\",
    ]
    report.append("E6    Hecke-centred row retracted")

out = ("\r\n" if crlf else "\n").join(lines)
open(P, "wb").write(out.encode("utf-8", errors="surrogateescape"))
print("\n".join(report))
print(f"begin(remark)={sum(1 for l in lines if l.startswith(chr(92)+'begin{remark}'))}  "
      f"end(remark)={sum(1 for l in lines if l.strip() == chr(92)+'end{remark}')}")
