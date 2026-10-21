> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_trigram_linear_fraction_addendum.md`. Embedded SHA256: `8e3f68f6c838d213863c987e8f39ffd0b3233f4331616cd5bb1f4651aeb01d4e`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: a fixed positive fraction of trigram centers

Date: 21 October 2026. Auditor: /root/audit_uniform_word_r4.

Frozen target:
arithmetic_trigram_linear_fraction_addendum.md.

Target SHA256:
73c8aa1e35676526fc881799c3c02b75676cc4d43b1f188c96f3fde21e19a401.

The hash was independently recomputed. The target was read in full
and not modified. Its base inequalities were independently proved
in audit_macroscopic_trigram_coverage_barrier.md, SHA256
21d592609bd5a222b00028fa531ad0a9724e3e808216a982b864a87076eb39f4.
In particular, the present argument uses the explicit finite
partner-count estimate, not an invalid application of the base
$q_N=o(N)$ theorem to a linear sequence.

## Verdict

The strengthening is proved with the stated explicit
$$
\delta=2^{-16}(\alpha/K)^4,\qquad
\alpha=e^{-B}c^3/6,\qquad
K=\max\{e^2,32e^B/\alpha\}.
$$
For all sufficiently large $N$, uniformly over $cN\le n\le BN$,
the same exponential lower bound holds for coherent pairs with
more than $\lfloor\delta N\rfloor$ changed trigram centers.
No gap or constant correction was found.

## Entropy and constants

The base finite count bound for a selected word is
$$
\mathcal N_x(q)\le
n4^{\mathcal J(x)}(q+1)(eN/q)^q
\exp\left\{\frac{q}{(\log2)^2}
\log^2(eKN/q)\right\}.
$$
Its prefactor has logarithm $O_B(\log N)$, since
$\mathcal J(x)\le\log N$. For $q/N\to\delta\in(0,1/2)$,
continuity of the two remaining expressions therefore gives
the uniform rate bound
$$
\limsup_N\sup_{n,x}\frac1N\log\mathcal N_x(q)
\le h_K(\delta)
=\delta\log(e/\delta)
+\frac{\delta}{(\log2)^2}\log^2(eK/\delta).
$$

The explicit constant check is valid. Since $c\le B$ and
$e^B\ge B^3/6$, one has $0<\alpha\le1$.
Put $X=K/\alpha\ge e^2$. Then $K\le X$ and
$\delta=2^{-16}X^{-4}\in(0,1/2)$. The inequalities
$1/2<\log2<1$ and $\log X\ge2$ yield
$$
\log(e/\delta)\le13\log X,\qquad
\log(eK/\delta)\le14\log X.
$$
Consequently
$$
h_K(\delta)
<791\,\delta\log^2X.
$$
To check the number $791$, the first term contributes at
most $6.5\log^2X$, while
$196/(\log2)^2<784$. Their sum is strictly less than
$790.5$, hence less than $791$.

On $X\ge e^2$, the function $\log^2X/X$ decreases and
has value $4/e^2<1$ at the left endpoint. Also
$X^{-3}=\alpha^3/K^3\le\alpha$. Thus
$$
h_K(\delta)
<\frac{791}{2^{16}}X^{-3}
\le\frac{791}{2^{16}}\alpha
<\frac\alpha8
<\frac{\alpha\log2}{4}.
$$
All inequalities used in the target's entropy margin are
therefore justified. In particular $791<2^{13}=8192$
gives the penultimate strict inequality.

For $q=\lfloor\delta N\rfloor$, the finite count bound is
applicable for large $N$, since then $1\le q\le N/2$.
The strict entropy margin implies
$$
\mathcal N_x(q)\le2^{3\alpha N/8}
\le2^{\alpha N/2-2}
$$
uniformly in the selected words and times, the second
inequality holding once $N\ge16/\alpha$.

## Lower count, roots and coverage

The base last-exit construction supplies at least
$2^{\alpha N/2-1}$ distinct coherent rooted partners
for each selected word. Removing the partners counted
above leaves at least $2^{\alpha N/2-2}$. The selected
words have weight at least $\alpha/4$. Multiplication
therefore gives
$$
\sum_{\substack{L(x)=L(y)\\
\mathfrak d(x,y)>\lfloor\delta N\rfloor}}
a(x)\overline{a(y)}
\ge\frac{\alpha}{16}\,2^{\alpha N/2}.
$$
The phases agree exactly on every pair used in this lower
bound. The same selected words have a good vertex, so the
base argument excluding reversed rotations applies.
Forward rotations have zero trigram distance and are
also excluded. There is no extra root multiplicity.

A directed rearrangement of $r$ arcs changes trigram
arrays at at most $2r$ vertex labels. Thus this positive
subclass cannot arise when $2r\le\lfloor\delta N\rfloor$.
If $L_*>2B/\delta$ is a fixed integer and every arc
contains at least $L_*$ vertices, then
$$
2r\le2BN/L_*=(\delta-\varepsilon)N
$$
for a fixed $\varepsilon>0$. For $N\ge1/\varepsilon$
this is at most $\lfloor\delta N\rfloor$, which checks
the rounding issue explicitly.

The theorem therefore excludes coverage of the stated
positive class even by the union of all directed
rearrangements having this sufficiently large fixed
minimum length. It does not assert a positive net
signed value of the uncovered complement. Other
edge-count arrays may cancel its positive mass, and
neither the validity nor the failure of
$H_{\rm diag}$ follows.
