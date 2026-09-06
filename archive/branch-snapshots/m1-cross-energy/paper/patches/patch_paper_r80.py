import io

p = 'paper/exact_wd_and_subgroup_moments.tex'
s = open(p, encoding='utf-8').read()
block = open('paper/section_r80.tex', encoding='utf-8').read()
anchor = "\\section{Numerical certification}\\label{sec:numerics}"
assert anchor in s, "anchor missing"
assert "Run 80: the generating function evaluated" not in s, "already inserted"
s = s.replace(anchor, block + "\n\n" + anchor)

old = "$\\mathcal B(k;s,s)$ exhaustive & \\texttt{pstar\\_scan.py} & table above\\\n\\bottomrule"
new = (r"""$\mathcal B(k;s,s)$ exhaustive & \texttt{pstar\_scan.py} & table above\\"""
       "\n"
       r"""Run \ref{sub:r80}: census rows $r\le8$ ($\ZZ$/full/wrap), $X^{\ZZ}$"""
       "\n"
       r""" $r\le12$, $\mathrm S_{\mathrm{win}}$ $8/8$, $\operatorname{triv}(6,17)$"""
       "\n"
       r""" & \texttt{r80\_jweight\_dp.py} & exact\\"""
       "\n"
       r"""Run \ref{sub:r80}: collision excess $r=10,12$ & \texttt{r80\_wrap\_collisions.py}"""
       "\n"
       r""" & exact (last digit)\\"""
       "\n"
       r"""Run \ref{sub:r80}: float replica $r\le12$ & \texttt{r80\_julia\_bigdp.jl} &"""
       "\n"
       r""" $\le2.2\!\cdot\!10^{-15}$\\"""
       "\n"
       r"""\bottomrule""")
assert old in s, "table anchor missing"
s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s)
print("paper patched OK")
