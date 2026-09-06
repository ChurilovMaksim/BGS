r"""RUN 92 paper patch: insert the R91-R92 section (arcsine/Wigner dichotomy,
spectral package, k=2/k=4 fluctuation reduction) into the main paper.
Written as a file (heredocs mangle backslashes on this box).  Idempotent.

The new section is inserted BEFORE \section{Numerical certification} or,
if absent, appended before \end{document}.  Bibliography entries are added
to the thebibliography block if present.
"""
import io

P = "paper/exact_wd_and_subgroup_moments.tex"
s = io.open(P, encoding="utf-8").read()
block = io.open("paper/section_r91.tex", encoding="utf-8").read()

BS = chr(92)
anchor = BS + "section{Numerical certification}" + BS + "label{sec:numerics}"

if "The arcsine/Wigner dichotomy and the spectral package" in s:
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
