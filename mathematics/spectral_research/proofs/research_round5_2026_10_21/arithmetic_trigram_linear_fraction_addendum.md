> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/arithmetic_trigram_linear_fraction_addendum.md`. Embedded SHA256: `73c8aa1e35676526fc881799c3c02b75676cc4d43b1f188c96f3fde21e19a401`.
> [Thematic guide](../../topics/histories.md).

# A fixed positive fraction of changed trigram centers

Date: 2026-10-21.  
Status: proved strengthening of the frozen original-family coverage theorem.

Base source: arithmetic_macroscopic_trigram_coverage_barrier.md, SHA256  
828b12a6b933e2f541b2296d240555d8caceac407442f27397f050f2bf0928c7.

This addendum uses the fully proved inequalities (3.2), (4.5), and (5.1) of that source, with exactly the same hypotheses and definitions. It changes no source and no original matrix.

## 1. Explicit linear threshold

Fix $0<c\le B<\infty$, and write
$$
 \alpha=e^{-B}c^3/6,\qquad
 K=\max\{e^2,32e^B/\alpha\},\qquad
 \delta=2^{-16}\left(\frac{\alpha}{K}\right)^4.
 \tag{1.1}
$$
Then $0<\delta<1/2$, and, uniformly over $cN\le n\le BN$, for all sufficiently large $N$,
$$
 \boxed{\quad
 \sum_{\substack{x,y:\ L(x)=L(y)\\
                 \mathfrak d(x,y)>\lfloor\delta N\rfloor}}
       a(x)\overline{a(y)}
 \ge\frac{\alpha}{16}\,2^{\alpha N/2}.
 \quad}                                                     \tag{1.2}
$$
A positive subclass providing this bound lies outside the forward and reversed rotation classes, as in the base theorem.

In particular, the large coherent contribution requires changes at a fixed positive fraction of all vertex labels. This is stronger than the base statement for an arbitrary sequence $q_N=o(N)$.

## 2. Entropy bound at $q=\lfloor\delta N\rfloor$

For selected words $x\in\mathcal A_{n,N}$, the exact base bound (4.5) gives, if $q/N\to\delta$,
$$
 \limsup_{N\to\infty}
 \sup_{\substack{cN\le n\le BN\\x\in\mathcal A_{n,N}}}
 \frac1N\log\mathcal N_x(q)
 \le h_K(\delta),
 \tag{2.1}
$$
where
$$
 h_K(t)
 =t\log(e/t)+\frac{t}{(\log2)^2}\log^2(eK/t).
 \tag{2.2}
$$
Indeed, the factors $n4^{\mathcal J}(q+1)$ have logarithm $O_{B}(\log N)$, because $\mathcal J\le\log N$. The two other logarithms divided by $N$ converge to (2.2), with errors uniform in the selected word and time.

We verify explicitly that the $\delta$ in (1.1) satisfies
$$
 h_K(\delta)<\frac{\alpha\log2}{4}.                           \tag{2.3}
$$
First $0<\alpha\le1$: $c\le B$ and $e^B\ge B^3/6$. Put
$X=K/\alpha\ge e^2$, so $\delta=2^{-16}X^{-4}$ and $K\le X$.
The elementary bounds $1/2<\log2<1$, $\log X\ge2$, imply
$$
 \log(e/\delta)=1+16\log2+4\log X\le13\log X,
$$
and
$$
 \log(eK/\delta)\le1+16\log2+5\log X\le14\log X.
$$
Consequently
$$
 \begin{split}
 h_K(\delta)
 &\le\delta\left(13\log X+
       \frac{196}{(\log2)^2}\log^2X\right)\\
 &<791\,\delta\,\log^2X
 \le\frac{791}{2^{16}}X^{-3}
 \le\frac{791}{2^{16}}\alpha
 <\frac{\alpha}{8}
 <\frac{\alpha\log2}{4}.
 \end{split}                                                 \tag{2.4}
$$
Here $\log^2X\le X$ for $X\ge e^2$, since $\log^2X/X$ decreases on that interval and its value at $e^2$ is $4/e^2<1$. Also
$X^{-3}=\alpha^3/K^3\le\alpha$. All constants in (2.4) are explicit.

Taking $q=\lfloor\delta N\rfloor$, equations (2.1)–(2.3) imply, for all sufficiently large $N$,
$$
 \mathcal N_x(q)\le 2^{3\alpha N/8}
 \le2^{\alpha N/2-2}
$$
uniformly in the selected word and time. The second inequality holds once $\alpha N/8\ge2$.

The base last-exit construction gives at least $2^{\alpha N/2-1}$ distinct coherent rooted partners for each selected $x$. Removing all partners counted by $\mathcal N_x(q)$ leaves at least $2^{\alpha N/2-2}$. The base selected-word mass is at least $\alpha/4$. Multiplication proves (1.2).

## 3. Consequence for directed cuts, with its exact scope

Every directed rearrangement of $r$ arcs satisfies
$\mathfrak d(x,y)\le2r$, by the endpoint argument in the base source. Thus the positive subclass counted above cannot be generated with
$r\le\lfloor\delta N\rfloor/2$ cuts.

In particular choose any fixed integer
$$
 L_*>2B/\delta.
$$
Even the union of all directed arc rearrangements whose arcs each contain at least $L_*$ vertices misses the exponential positive subclass, once $N$ is large: its number of arcs is at most $BN/L_*<\delta N/2$. The strict inequality absorbs integer rounding.

This is an exact set-coverage statement and an obstruction to discarding the uncovered class by absolute values. It does not assert that the uncovered **signed** complement has a large net value; positive and negative contributions there can compensate. It therefore does not categorically preclude a proof using long arcs together with an additional argument for the uncovered dense configurations, and it gives no conclusion about validity or failure of $H_{\rm diag}$.

