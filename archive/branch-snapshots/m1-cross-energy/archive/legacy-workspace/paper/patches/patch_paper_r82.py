"""RUN 82 paper patch: insert the Theorem-I subsection and its bibliography
entries, and add certification rows.  Written as a file (heredocs mangle
backslashes on this box).  Idempotent: refuses to insert twice."""
import io

P = "paper/exact_wd_and_subgroup_moments.tex"
s = io.open(P, encoding="utf-8").read()
block = io.open("paper/section_r82.tex", encoding="utf-8").read()

BS = chr(92)
anchor = BS + "section{Numerical certification}" + BS + "label{sec:numerics}"
assert anchor in s, "anchor missing"
if "Run 82: the observable family is a one-parameter" in s:
    print("already inserted; nothing to do")
    raise SystemExit(0)
s = s.replace(anchor, block + chr(10) + chr(10) + anchor, 1)

# bibliography entries (thebibliography or \bibitem list)
bib_marker = BS + "begin{thebibliography}"
kr = (BS + "bibitem{KR2000} P. Kurlberg and Z. Rudnick, "
      "\\emph{Hecke theory and equidistribution for the quantization of "
      "linear maps of the torus}, Duke Math. J. \\textbf{103} (2000), "
      "47--77; arXiv:chao-dyn/9901031." + chr(10) +
      BS + "bibitem{KR2003} P. Kurlberg and Z. Rudnick, "
      "\\emph{On the distribution of matrix elements for the quantum cat "
      "map}, Ann. of Math. \\textbf{161} (2005), 489--507; "
      "arXiv:math/0302277." + chr(10))
if bib_marker in s:
    i = s.index(bib_marker)
    j = s.index(chr(10), i) + 1
    s = s[:j] + kr + s[j:]
    print("bibliography entries inserted")
else:
    print("WARNING: no thebibliography environment found; citations left dangling")

io.open(P, "w", encoding="utf-8").write(s)
print("paper patched:", len(s), "chars")
