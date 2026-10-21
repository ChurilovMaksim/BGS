> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/arithmetic_audit_collision_moment_phase_cancellation.md`. Embedded SHA256: `447a1d559969c424551eef1e1234725c2c5fabe5851f85dff9bfe3f12f512fcd`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of collision-moment phase cancellation

Date: 21 October 2026. Auditor: /root/arithmetic_countersequence_20261021_r4.

Frozen target:
dual_collision_moment_phase_cancellation.md

Target SHA256:
8528fb6bf6f633c3bb799261da69638ef0c9e55a30e062eb5e94dcab6440493a

Frozen companion:
dual_collision_moment_exact_checks.py

Companion SHA256:
958e95892d1191c45846ccdae66708fe79d7bb4887ead4dd9fcabc0e6bb780e1

Both hashes were independently recomputed. The final source, including its corrected order-zero paragraph and its finite-check section, was read completely. The frozen files were not changed.

## Verdict

The finite constraint estimate (7), the positive collision-moment estimate (10), and the uniform logarithmic-moment consequence (12)--(13) are proved on the stated hypotheses. No constant correction or missing factor was found.

The result is for the marked observables (4), with their labelled-root and repeated-presentation multiplicities. It does not remove the zero-collision indicator, does not extend the actual unmarked pair theorem to order $N/\log N$, and does not establish $H_{\rm diag}$.

The detailed reconstruction below does not rely on previous audit verdicts or on the finite tests. In particular it checks that imposing collision events leaves the other endpoint orthogonality identities available before any absolute value.

## 1. Source and hypothesis matching

The finite theorem assumes a unitary $N\times N$ matrix with
$$
P_{ab}=|U_{ab}|^2,\qquad J_{ab}=N^{-1},\qquad
\max P_{ab}\le C/N,\quad \|P-J\|_{\rm op}\le1/2,
\quad N\ge C\ge1.
\tag{A1}
$$
Its proof is purely finite dimensional.

The two original-family input files were located, their hashes recomputed, and their relevant statements checked:

- dual_physical_four_branch_kernel.md, SHA256
  0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c,
  gives $|U_{xy}|\le3/\sqrt N$ eventually through all odd $N$.
- root_oscillatory_matrix_cancellation.md, SHA256
  ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d,
  gives $\|P-J\|\le1/2$ eventually through all odd $N$.

Thus the application uses exactly $C=9$, fixed $\tau=10^{-80}$, and the original matrices. This audit concerns the new finite argument, not a new independent audit of those two analytic input proofs.

The earlier arc source
dual_directed_encounter_growing_order_cancellation.md, SHA256
f0ffa2acc3e4b66b75620ee116a20cf8793c4d7efc40d5db67ded4259436c4e4,
was read for the exact partition and marked-root convention. An arc with $\ell_i$ internal edges has $\ell_i+1$ formal vertices. The arcs partition the $n$ formal positions, so
$$
\sum_i(\ell_i+1)=n.
\tag{A2}
$$
The partner reorders entire forward arc words and is therefore a permutation of those $n$ formal positions, including when actual vertex labels repeat.

## 2. Exact rank of a single repeated substring

Translate the first starting position to zero. A length-$K$ match with displacement $d\not\equiv0\pmod n$ imposes the $K$ formal identifications
$$
u\sim u+d\pmod n,\qquad 0\le u<K.
\tag{A3}
$$
The rank here is the number of formal variables removed by the equivalence relation. It is not an assumption of probabilistic independence of the actual labels.

The directed constraint multigraph has indegree and outdegree at most one and no loops. An undirected cycle would force indegree and outdegree one at each of its vertices and hence a complete directed translation orbit. The same argument includes two opposite edges forming an undirected parallel-edge cycle.

Put $g=\gcd(n,d)$. A translation orbit is exactly one residue class modulo $g$. In ordinary representatives it has span $n-g$. Since $g$ is a proper divisor of $n$, $g\le n/2$ and
$$
n-g\ge n/2.
$$
But every tail of a constraint edge lies in $[0,K-1]$, of span $K-1<n/2$. No complete orbit can be contained there. The graph is therefore a forest with exactly $K$ edges, and its identification rank is exactly $K$.

The nonempty marked range has
$$
n\ge3(L+1)=3(2K+3),
$$
which implies $K<n/2$. The same forest conclusion applies to a collision in the partner word: pull the constraints back by its permutation of the formal positions. This relabelling preserves rank.

For a conjunction of $j\ge1$ collision events, repeated events are allowed. Its total rank $h$ is at least $K$, since adjoining identifications cannot decrease the rank of the first event.

## 3. Clean endpoint contractions survive the imposed event

Fix lengths, a permitted successor cycle $\sigma$, and a conjunction $E$ of formal equality constraints. Let $S$ contain exactly those arc indices having at least one formal position occurring in a constraint, and put $s=|S|$.

Fix an allowed tuple of arc-start labels $b$. For $i\notin S$, neither the internal variables of arc $i$ nor its endpoint $a_i$ occur in $E$. Its start $b_i$, as a formal position, also does not occur in $E$. The allowed-start domain depends only on $b$, so it does not constrain the free $a_i$-sum. Thus the entire untouched arc contracts to
$$
F_i(b)=\sum_a(P^{\ell_i})_{b_i a}
       U_{a,b_{\gamma(i)}}\overline{U_{a,b_{\sigma(i)}}}.
\tag{A4}
$$
The literal inequality $b_{\gamma(i)}\ne b_{\sigma(i)}$ implies
$$
\sum_aN^{-1}U_{a,b_{\gamma(i)}}
                   \overline{U_{a,b_{\sigma(i)}}}=0
$$
by column orthogonality. Therefore every such factor can be replaced exactly by $P^{\ell_i}-J$ before any modulus is taken. If the event contradicts an allowed-start inequality, its contribution is zero; this does not invalidate the contraction on the allowed domain.

For completeness, let $A=P-J$. Double stochasticity gives $AJ=JA=0$, and
$$
\sum_a|A_{ba}|^2,\ \sum_b|A_{ba}|^2\le(C-1)/N.
$$
Sandwiching $A^{\ell_i-2}$ between a row and a column yields
$$
|(P^{\ell_i}-J)_{ba}|
 \le\frac{C-1}{N}2^{-(\ell_i-2)}.
$$
Cauchy--Schwarz for the two unit-norm columns of $U$ consequently gives
$$
|F_i(b)|\le\delta_i/N,\qquad
\delta_i=(C-1)2^{-(\ell_i-2)}.
\tag{A5}
$$
This step applies to nonnormal $P$ and to repeated start labels satisfying the literal mismatches.

## 4. The affected-arc forest and its exact powers of $N$

Only after (A4)--(A5) have been used, take the modulus. Bound the two connector amplitudes belonging to each affected arc by $C/N$ in product. These $s$ bounds also remove any dependence of affected connectors on untouched starts.

Before imposing $E$, the remaining affected internal graph is a disjoint union of $s$ paths, with $v$ formal vertices and $v-s$ internal $P$-factors. Rank $h$ leaves $v-h$ quotient vertices. Its number $t$ of connected components satisfies $t\le s$, because identifying vertices can merge components but cannot split them.

A spanning forest of the quotient has $v-h-t$ edges. Thus exactly
$$
(v-s)-(v-h-t)=h+t-s
\tag{A6}
$$
internal factors remain outside it. This number is nonnegative. Loops and duplicate edges after quotienting are simply among the factors discarded by the pointwise bound.

Bound the factors in (A6) by $C/N$. The sum of the forest product over its vertex labels is $N^t$: delete leaves successively, using a row sum or a column sum equal to one according to the orientation of the leaf edge, and sum the final label in each component. Including the $s$ affected connector bounds gives
$$
N^t(C/N)^{h+t-s}(C/N)^s
=C^t(C/N)^h
\le C^s(C/N)^h.
\tag{A7}
$$

At this stage the start domain may be enlarged, because the bound is nonnegative. The $r-s$ untouched starts are free and contribute $N^{r-s}$, cancelling exactly the factors $N^{-(r-s)}$ in (A5). Therefore
$$
|\mathcal A_{\boldsymbol\ell,\sigma}(E)|
\le C^s(C/N)^h\prod_{i\notin S}\delta_i.
\tag{A8}
$$
This is exactly the target's (7). The constraint event never prevented an untouched orthogonality identity, and no complex weight was used as a probability.

## 5. Collision count, roots, and orders

A length-$K$ substring meets at most two arc words: meeting three would require traversing an entire intervening arc of at least $2K+3$ vertices. This applies both to $x$ and to its partner. One collision event therefore touches at most four arcs, and $j$ events touch at most $4j$ arcs.

Because $N\ge C$, $h\ge K$, $\delta_i\le\delta$, and $n\delta<1$,
$$
|\mathcal A(E)|
\le C^{4j}(C/N)^K
        \delta^{\max(r-4j,0)}.
\tag{A9}
$$
The decrease of $(C/N)^h$ with $h$ uses the stated hypothesis $N\ge C$. The direction of the error-power inequality uses $0\le\delta<1$. For $C=1$, factors with a positive error exponent vanish exactly; an empty product is one, as specified in the source.

There are at most $2\binom n2\le n^2$ collision events in the two words. Expanding the positive integer power of their sum produces at most $n^{2j}$ ordered event tuples. This expansion is finite and valid even if the same formal event occurs repeatedly.

The root/mark prefactor is exactly $n^2/r$. Distinguishing a first marked position counts each unordered $r$-marking exactly $r$ times. The distinguished position has $n$ possible locations in the original rooted word; the definition supplies another $n$ labelled partner roots. Both amplitudes and the collision counts are rotation invariant. The relabelling-invariant family of partner cycles is summed before division by $r$. This derivation counts positions, so a periodic word does not change the factor.

For fixed $r$, the number of length tuples is
$$
\binom{n-rL-1}{r-1}
\le n^{r-1}/(r-1)!
$$
when feasible, and zero otherwise. There are at most $(r-1)!$ single-cycle partner orders. The literal-mismatch requirement can be imposed as the separate $b$-domain for each index permutation; this is equivalent to the definition.

Combining these counts with (A9) gives exactly
$$
|\mathcal H_j|
\le C^{4j}(C/N)^K
 \sum_{r=3}^M\frac{n^{r+2j+1}}r
        \delta^{\max(r-4j,0)}.
\tag{A10}
$$
The exponent is $2+(r-1)+2j=r+2j+1$; there is no missing root or factorial.

For $3\le r<4j$, bound each term by $n^{6j+1}$, with at most $4j$ terms. For $r\ge4j$, put $q=r-4j$; the remaining series is at most
$$
n^{6j+1}\sum_{q\ge0}(n\delta)^q.
$$
This proves (10), uniformly in $M$. It also explains why a bound on all feasible orders can coexist with only $4j$ affected arcs.

## 6. Exact verification of exponent (12)

Put $u=\log_2N$, $K=\lceil4u\rceil$, and
$1\le j\le\lfloor u/3\rfloor$. For fixed $B$, $n\le BN$ gives
$n\delta\le B(C-1)N^{-7}<1/2$ eventually. Write $B_+=\max(B,1)$. Each factor of (10) is bounded as follows:
$$
C^{4j+K}\le C^{1+16u/3}
   =C\,N^{(16/3)\log_2C},
$$
$$
n^{6j+1}\le(B_+N)^{2u+1}
   =B_+N^{2u+1+2\log_2B_+},
$$
$$
N^{-K}\le N^{-4u},\qquad
4j+(1-n\delta)^{-1}\le4u/3+2.
$$
Their product is precisely
$$
C B_+(4u/3+2)
N^{-2u+1+(16/3)\log_2C+2\log_2B_+}.
\tag{A11}
$$
This verifies every coefficient in (12). The logarithm of (A11) is
$$
-\frac{2}{\log2}(\log N)^2+O_{B,C}(\log N)+O(\log\log N),
$$
so (13) follows for every fixed polynomial rate, uniformly in all three suprema.

The length constraint permits at most
$\lfloor n/(L+1)\rfloor$ arcs, of order $N/\log N$ on $cN\le n\le BN$. The positive-order moment result includes every such feasible order.

The final source correctly distinguishes order zero. With the fixed cutoff above, its separate bound is
$$
\frac{n(n\delta)^3}{3(1-n\delta)}
=O_{B,C}(N^{-20})
$$
uniformly for $1\le n\le BN$, since $n^4=O_B(N^4)$ and
$\delta^3=O_C(N^{-24})$. It is not claimed to decay faster than every power with that fixed cutoff.

## 7. The indicator obstruction and the scope boundary

The signed-binomial example is correct:
$$
\mu_H=\sum_{q=0}^H(-1)^q\binom Hq\delta_q.
$$
The polynomial identity
$$
\sum_{q=0}^H(-1)^q\binom Hq t^q=(1-t)^H
$$
shows, by applying $(t\,d/dt)^m$ and setting $t=1$, that
$\int q^m\,d\mu_H(q)=0$ for every $m<H$. Its zero atom is one, and its total variation is $2^H$.

Choosing $H=\lfloor(\log_2N)/3\rfloor+1$ therefore satisfies stronger moment cancellation than the displayed hypotheses while retaining a nonzero zero-collision mass. The example is correctly labelled an obstruction to an inference from moments alone, not a model for the original path weights.

Consequently the estimate for the factor $(R_K(x)+R_K(y))^j$ cannot be substituted for an estimate with
$\mathbf1_{\{R_K(x)+R_K(y)=0\}}$. Removing marking multiplicities for $r\asymp N/\log N$ requires an additional signed estimate. The previously established actual unmarked theorem remains at its stated square-root-order scope.

## 8. Independent finite checks

The companion was read and run independently. It passed:

- 34,655 exact constraint-rank checks with $3\le n\le60$, $K<n/2$;
- 128 exact constrained endpoint terms for a nonflat rational orthogonal matrix, with a nonzero full contraction equal to the version centering every untouched arc;
- 465 exact vanishing signed moments, with zero atom one and total variation $2^H$.

The nonzero contraction computed by the script is
$$
-\frac{16201305951663587328}{9094947017729282379150390625},
$$
and its checked upper bound in (7) is
$$
\frac{50176}{9765625}.
$$
The tests corroborate the identities without replacing the forest, root-count, or uniform asymptotic proofs above.

## Final assessment

All sections of the final frozen target are correct in their stated marked-observable scope. The new estimate preserves the original phases on every untouched arc and reaches all feasible long-arc orders, but its collision moments do not resolve the signed zero-collision indicator or the full spectral-statistics limit.
