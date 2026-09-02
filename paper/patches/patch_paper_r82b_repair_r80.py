"""RUN 82 repair of the R80 paper-integration claim.

R80.7 states "Paper integration: new subsection 'Run 80' ... both papers
recompile clean".  In fact only the certification-table ROWS were inserted;
`paper/section_r80.tex` was never spliced in, so `\\ref{sub:r80}` was dangling
on page 18 of the shipped PDF.  This script inserts the missing subsection
(before the Run-82 one, preserving chronology) and appends the Run-82
certification rows.  Idempotent.
"""
import io

BS = chr(92)
P = "paper/exact_wd_and_subgroup_moments.tex"
s = io.open(P, encoding="utf-8").read()

# --- 1. splice in the missing Run-80 subsection -------------------------
if "Run 80: the generating function evaluated" in s:
    print("Run-80 subsection already present")
else:
    r80 = io.open("paper/section_r80.tex", encoding="utf-8").read()
    anchor = BS + "subsection{Run 82: the observable family is a one-parameter"
    assert anchor in s, "Run-82 anchor missing"
    s = s.replace(anchor, r80 + chr(10) + chr(10) + anchor, 1)
    print("Run-80 subsection inserted (repairs the dangling ref:sub:r80)")

# --- 2. Run-82 certification rows --------------------------------------
old = (r"""Run \ref{sub:r80}: float replica $r\le12$ & \texttt{r80\_julia\_bigdp.jl} &"""
       + chr(10) + r""" $\le2.2\!\cdot\!10^{-15}$\\""" + chr(10) + r"""\bottomrule""")
new = (r"""Run \ref{sub:r80}: float replica $r\le12$ & \texttt{r80\_julia\_bigdp.jl} &"""
       + chr(10) + r""" $\le2.2\!\cdot\!10^{-15}$\\""" + chr(10)
       + r"""Run \ref{sub:r82}: Thm \ref{thm:torus}, certificates C1--C5,"""
       + chr(10) + r""" 3 designs & \texttt{r82\_torus\_rigidity.py} & $15/15$;"""
       + chr(10) + r""" spectra $\le2\!\cdot\!10^{-13}$\\""" + chr(10)
       + r"""Run \ref{sub:r82}: $\mu_4$ via the exact $N\times N$ projector"""
       + chr(10) + r""" & \texttt{r82\_orbit\_invariant.py} & $1.3\!\cdot\!10^{-14}$\\"""
       + chr(10) + r"""Run \ref{sub:r82}: relation-count DP, glue check to $R=150$"""
       + chr(10) + r""" & \texttt{r82b\_dp\_push.jl} & exact\\""" + chr(10)
       + r"""\bottomrule""")
if new.replace(chr(10), "") in s.replace(chr(10), ""):
    print("Run-82 rows already present")
elif old in s:
    s = s.replace(old, new, 1)
    print("Run-82 certification rows added")
else:
    print("WARNING: certification-table anchor not found; rows not added")

io.open(P, "w", encoding="utf-8").write(s)
print("written:", len(s), "chars")
