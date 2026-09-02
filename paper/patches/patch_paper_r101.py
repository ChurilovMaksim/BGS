r"""RUN 101 paper patch: insert the R101 section (the Mobius-fiber theorem:
delta = o(1), the k=4 layer of the fluctuation hypothesis as a THEOREM).
Idempotent.  Inserted before \section{Numerical certification}.
"""
import io

P = "paper/exact_wd_and_subgroup_moments.tex"
s = io.open(P, encoding="utf-8").read()
block = io.open("paper/section_r101.tex", encoding="utf-8").read()

BS = chr(92)
anchor = BS + "section{Numerical certification}" + BS + "label{sec:numerics}"

if "The M" + chr(246) + "bius--fiber theorem" in s:
    print("already inserted; nothing to do")
    raise SystemExit(0)

if anchor in s:
    s = s.replace(anchor, block + chr(10) + chr(10) + anchor, 1)
    print("inserted before sec:numerics")
else:
    enddoc = BS + "end{document}"
    s = s.replace(enddoc, block + chr(10) + chr(10) + enddoc, 1)
    print("appended before end{document}")

io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("paper updated:", P)
