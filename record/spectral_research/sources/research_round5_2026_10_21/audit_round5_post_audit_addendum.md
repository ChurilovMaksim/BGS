> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_round5_post_audit_addendum.md`. Embedded SHA256: `93fbb42a78f4b04f2f350879e68ddd62ed40f37cd541bfbf77b8d61026037702`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent validation of the post-audit Russian addendum

21 October 2026. Auditor: /root/audit_uniform_word_r4.

## Exact reviewed version

Reviewed round5_post_audit_addendum.md in full.

**Final reviewed SHA256:** 3c2c02e81a3bb4c8d91c2fe0824581f95f07f39b26d587c6925ff45e56d5b8f5

The separately audited main report is unchanged:

- round5_main_report.md, SHA256 8a4629d270c1b70e2478ce98cc2ed66b8e4a6c836cc27c35fbaf1555587420c2.
- Its existing audit: audit_round5_main_report.md, SHA256 eb1cb385cdcfca1e378de8420ea23656ee9560bf2d12f806539c65cf98910d2d.

**Verdict:** the addendum accurately states the finite identities, the localized relative compensation, the marked positive-moment theorem, and their unresolved implications. No substantive gap remains in this exposition after the finite-hypothesis correction recorded below. This verdict does not establish $H_{\rm diag}$, the pair limit, or a countersequence.

The two raw mathematical sources checked against the exposition are:

1. arithmetic_occupation_resummation_obstruction.md, SHA256 1aeefa2931e83e4368ecdc4b5b0aa3b31c81beef8eb6fbb69ea825e08e5b0556.
2. dual_collision_moment_phase_cancellation.md, SHA256 8528fb6bf6f633c3bb799261da69638ef0c9e55a30e062eb5e94dcab6440493a.

The first source was reconstructed in audit_occupation_resummation_obstruction.md, SHA256 680841fae8341687da7949090b2c2daf3db84ce89ec7885a1120c7af79e1eee6. The collision proof was read in full and its estimates were independently reconstructed during the present validation. The sibling audit arithmetic_audit_collision_moment_phase_cancellation.md, SHA256 447a1d559969c424551eef1e1234725c2c5fabe5851f85dff9bfe3f12f512fcd, is a separate check; its verdict was not used as proof.

All cited raw source hashes were rechecked. None of those sources was modified.

## 1. Occupation identities and relative error

Sections Д.1--Д.3 preserve the original rooted-word convention. The trace expansion and formal integration give exactly
$$
 A_{n,d}=n[z^d]\{-\log\det(I-ZU)\}.
$$
Neither periodicity nor repeated edges introduce an extra divisor. The principal-minor polynomial and normalized row-phase Parseval identity are stated with the correct signs and measures.

The relative compensation formula (Д.4) follows from a direct inequality, not from cancellation of error terms. Namely, the occupation source proves
$$
 0\le\mathcal O_n=\mathcal F_n+\mathcal R_n^{\rm occ}\le N^2.
$$
The already audited original-family exponential theorem gives, for $s=n/N\in[c,B]$,
$$
 \mathcal F_n\ge \exp\{\kappa(s)N-C_{c,B}\},
 \qquad \kappa(s)=\frac{\log2}{6}e^{-s}s^3>0.
$$
Hence
$$
 0\le
 \frac{\mathcal R_n^{\rm occ}}{\mathcal F_n}+1
 =\frac{\mathcal O_n}{\mathcal F_n}
 \le e^{C_{c,B}}N^2e^{-\kappa(s)N}.
$$
This proves both the uniform error in (Д.4) and its stated nonnegativity. The conclusion retains absolute uncertainty up to $N^2$. The text correctly does not treat this as the required $N$-scale form-factor asymptotic.

The notation $\mathcal R_n^{\rm occ}$ is explicitly separated from the earlier reversed-path sum $R_n$. The indexing sets are not confused.

The equality
$$
 |\operatorname{Tr}U^n|^2=\mathcal O_n+\Omega_n
$$
is exact, and both aggregate sums are real. The uncomputed quantity is not merely a remainder from a finite number of arc reconnections: it also includes the relative phases between different occupation vectors.

The row-phase identities for $P,Q$ and the extreme Fourier coefficient are faithfully reproduced. The qualitative Lindemann--Weierstrass application has the hypotheses established in the raw source and its independent audit: algebraic spectral projectors, at least one nonzero coefficient because their sum is a nonzero entry of $M_N$, and distinct algebraic exponents $iN\tau\lambda$. No assumption of simple eigenvalues is used.

The addendum correctly distinguishes nonconstant dependence on auxiliary row phases from the value at the original phase. It neither asserts $\Omega_n(U_N)\ne0$ nor obtains a quantitative discrepancy from the nonzero extreme coefficient.

## 2. Independent check of the collision estimates

The notation in (Д.6) agrees with the raw marked observable. The partner-root factor is $n$, including repeated labelled roots of periodic words. The admissible permutations satisfy the literal mismatch condition; no regularity or distinct-word quotient is inserted into the moment definition.

For completeness, the essential numerical and combinatorial checks were reconstructed as follows.

1. In the nonempty range, $n\ge3(2K+3)$, hence $K<n/2$. The $K$ constraint edges $u\to u+d$ for $0\le u<K$ cannot contain a complete translation orbit: such an orbit has representative span $n-\gcd(n,d)\ge n/2$. The graph is a forest of $K$ edges, including the possible order-two displacement case. Therefore a repeated block has rank exactly $K$. Reordering arcs merely permutes formal positions.
2. A length-$K$ block meets at most two arcs, because every intervening full arc has at least $2K+3$ vertices. Thus $j$ collision events touch at most $4j$ arcs. Their combined rank is at least the rank $K$ of the first event, even if events repeat.
3. For each untouched arc, its endpoint remains unconstrained. Column orthogonality kills its $J$-term at fixed allowed starts before any modulus is taken. The remaining contraction is at most $\delta_i/N$, with $\delta_i=(C-1)2^{-(\ell_i-2)}\le\delta$.
4. On $s$ affected paths, a rank-$h$ quotient has $t\le s$ components. Bounding the nonforest edges and the $s$ connector pairs, then summing the forest, gives $C^t(C/N)^h\le C^s(C/N)^h$. The untouched free starts cancel their factors $N^{-1}$. This step preserves the earlier signed cancellations.
5. Under $N\ge C\ge1$, $h\ge K$, $s\le4j$, and $\delta<1$, the result is bounded by
   $$
   C^{4j}(C/N)^K\delta^{\max(r-4j,0)}.
   $$
   There are at most $2\binom n2\le n^2$ collision events in the two words, so the ordered expansion of the $j$-th power has at most $n^{2j}$ terms.
6. The exact cyclic index factor remains $n^2/r$: the collision count is rotation invariant, and the full sums over ordered lengths and permissible cycles are invariant under cyclic relabelling of arcs. Periodic words are deliberately counted with labelled partner roots. The estimates $n^{r-1}/(r-1)!$ for length tuples and $(r-1)!$ for Hamiltonian orders cancel their factorials. They yield exactly the sum displayed before (Д.7).
7. For $r<4j$, use $n^{r+2j+1}\le n^{6j+1}$ and at most $4j$ terms. For $r\ge4j$, write $r=4j+h$ and sum $(n\delta)^h$. This gives
   $$
   |\mathcal H_j|\le
   C^{4j}n^{6j+1}(C/N)^K
   \left(4j+\frac1{1-n\delta}\right).
   $$
   Infeasible orders are zero, so the bound is uniform in $M$. When $C=1$, the convention for empty products at exponent zero gives the same conclusion directly.

The initially read addendum, SHA256 bf36c9b002b77771d6aedfed477374bf8a6ae01deb6c895b476a570f9d3fa0c8, omitted $N\ge C$ in the hypotheses immediately before (Д.7). This condition is required for $(C/N)^h\le(C/N)^K$. The author added precisely $N\ge C\ge1$. The final reviewed hash listed above contains this correction. The underlying frozen collision source already included the condition and was not changed.

## 3. Uniform range and the indicator obstruction

Put $u=\log_2N$, $B_+=\max(B,1)$, $K=\lceil4u\rceil$, and $1\le j\le\lfloor u/3\rfloor$. For fixed $B,C$, eventually $n\delta<1/2$ uniformly for $n\le BN$. The finite bound implies
$$
 |\mathcal H_j|
 \le C B_+(4u/3+2)\,
 N^{-2u+1+(16/3)\log_2C+2\log_2B_+}.
$$
Here the two powers of $C$ contribute respectively $(4/3)\log_2C$ and $4\log_2C$. The power of $N$ from $n^{6j+1}N^{-K}$ is at most $-2u+1$. Consequently (Д.8) is superpolynomial for every fixed $A,B,C$, uniformly in the stated $n,j,M$ ranges.

The allowed arc count is bounded by $\lfloor n/(2K+3)\rfloor$, of order $N/\log N$ when $n\asymp N$. The addendum explicitly confines this enlarged range to **marked positive-order moments**. It does not transfer the range to the earlier theorem about distinct regular pairs.

There is no accidental inclusion of moment order zero in (Д.8). With the displayed logarithmic cutoff, the source's separate uniform order-zero bound is only $O(N^{-20})$. The addendum does not claim it to be superpolynomial.

The finite-difference example is correct: for
$$
 \mu_H=\sum_{q=0}^H(-1)^q\binom Hq\delta_q,
$$
all polynomial moments of degree below $H$, including total mass, vanish, whereas $\mu_H(\{0\})=1$. Thus small signed moments do not by themselves control the zero-collision indicator. The text explicitly does not claim that this auxiliary measure is realized by $U_N$.

## 4. Remaining target and document checks

Formula (Д.9) substitutes the exact occupation decomposition into the existing pair identity. The normalization $N^{-2}$, the finite range $1\le n<2N$, and the CUE term $\min(n,N)$ agree with the fixed test in the main report. The addendum leaves the joint signed estimate unproved and does not assume separate smallness of $\mathcal O_n-\min(n,N)$ and $\Omega_n$. It correctly retains all higher orders of $H_{\rm diag}$ as additional requirements.

For the final reviewed addendum:

- UTF-8 decoding succeeds; no ASCII control character other than line feeds is present.
- There are 92 paired inline and 27 paired display math delimiters, for 119 math blocks.
- All checked mathematical brace counts are balanced.
- The finite assumptions before (Д.7) now explicitly contain $N\ge C\ge1$.
- The main-report hash remains the separately audited hash stated above.

This audit covers the addendum's mathematical exposition and these byte-level checks. It does not validate any later cumulative assembly, its embedded historical copies, or its original/rendered hash ledger. Those require checking the assembled artifact itself.
