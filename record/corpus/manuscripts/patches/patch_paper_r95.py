r"""RUN 96 paper patch: insert the R95-R96 section (twist identity,
flatness lemma, delta envelope, H3 closure at k=4).  Idempotent.
Insertion: after the R92 section, i.e. immediately before
\section{Numerical certification} (both R91 and R92 sections sit there).
"""
import io

P = "paper/exact_wd_and_subgroup_moments.tex"
s = io.open(P, encoding="utf-8").read()
block = io.open("paper/section_r95.tex", encoding="utf-8").read()

BS = chr(92)
anchor = BS + "section{Numerical certification}" + BS + "label{sec:numerics}"

if "The closure of the" in s and "fluctuation layer" in s:
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
