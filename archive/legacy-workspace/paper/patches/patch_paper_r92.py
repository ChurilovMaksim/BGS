r"""RUN 94 paper patch: insert the R92-R93 section (exact fluctuation
reduction, uniform even-k factorization, coupled energy, Katz
cancellation) AFTER the R91 section (which now sits before
\section{Numerical certification}).  Idempotent.

Insertion point: immediately before \section{Numerical certification}
if present, else before \end{document}.
"""
import io

P = "paper/exact_wd_and_subgroup_moments.tex"
s = io.open(P, encoding="utf-8").read()
block = io.open("paper/section_r92.tex", encoding="utf-8").read()

BS = chr(92)
anchor = BS + "section{Numerical certification}" + BS + "label{sec:numerics}"

if "The exact fluctuation reduction and the coupled energy" in s:
    print("already inserted; nothing to do")
    raise SystemExit(0)

if anchor in s:
    s = s.replace(anchor, block + chr(10) + chr(10) + anchor, 1)
    print("inserted before sec:numerics")
else:
    enddoc = BS + "end{document}"
    assert enddoc in s, "no anchor and no end{document}"
    s = s.replace(enddoc, block + chr(10) + chr(10) + enddoc, 1)
    print("appended before end{document}")

io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("paper updated:", P)
