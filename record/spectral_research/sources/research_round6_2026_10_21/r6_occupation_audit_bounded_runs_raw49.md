> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/r6_occupation_audit_bounded_runs_raw49.md`. Embedded SHA256: `251ad2ac4e4bcc96a6b79b30cd3a1c56f222f4390f5aaca2d94522fba55db7a1`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: the complete bounded-run raw class

21 October 2026. Auditor: occupation/cross-phase branch.

## 1. Frozen source and verdict

The source examined in full is:

- research_round6_2026_10_21/r6_dense_bounded_runs_raw49.md
- SHA256: 631663c9639c286510125df4806b833d4cfb8344a7a9d0fc36d6c647e83bc9e8

The source hash was checked immediately before this audit was written.

**Verdict:** the all-time exponentially weighted bound is justified for exactly the stated raw class. Its finite transfer includes each actual rooted pair once. The logarithmic determinant introduces the correct factor $n/m$, and the treatment of one-factor traces removes a potential dimension loss. All displayed numerical constants have been independently reconstructed.

The theorem applies to pairs with at least one agreement, at least one disagreement, and every cyclic disagreement run of length at most 48. Pairs with no agreement are excluded even when their length is at most 48. Equal and unequal occupations are both included. No claim about the unequal-occupation subset follows from this result.

The physical input is the independently audited fixed-power theorem:

- r6_original_fixed_powers_49.md, SHA256 3f51c6d7de5b559c28271c72ae62c2f2d331f9c606b24a84cdab80751339d019;
- r6_occupation_audit_fixed_powers_49.md, SHA256 0953ee6eb3c665fe667fabcb094651eb7284f6250ebfa2c6d535bd98f7da9b61.

The renewal source hash also matches its frozen value:

- r6_dense_renewal_long_return_obstruction.md, SHA256 95ea7e37c46b840854853c934eebecbd51ac1cb305d0200a283e68b9f7c3d0b2.

The finite encoding needed for the present theorem is additionally reconstructed directly below.

## 2. Exact class identity and rooted multiplicities

Use the row-to-column convention for path weights, so that a product of matrix entries along a cycle has precisely the weight
$$
 a(x)\overline{a(y)}
 =\prod_i W_{(x_i,y_i),(x_{i+1},y_{i+1})},
 \qquad W=U\otimes\overline U.
$$

The age transfer has diagonal-pair state block 0 and off-diagonal pair blocks with ages $1,\ldots,R-1$. Its nonzero blocks are
$$
 A_{00}=P,\quad A_{0,1}=B,\quad A_{j,0}=C,\quad
 A_{j,j+1}=S.
$$
Thus a disagreement run starts at age 1, advances by exactly one at each successive disagreement, and terminates by a transition to block 0. Runs longer than $R-1$ are impossible.

Every allowed cyclic physical pair has a unique lift: the age at a disagreement is the number of consecutive disagreements since its most recent cyclic agreement. The existence of an agreement makes this definition unique. If all positions disagree, no closed age walk is possible, since age would have to increase strictly around a cycle.

This lift is unique for each rooted pair, including words with repeated labels or shorter physical period. There is no chosen agreement or chosen run, and no additional multiplicity from rotations. Consequently
$$
 \operatorname{Tr}A^n
 =\sum_{\substack{\text{at least one agreement}\\
                  \text{all disagreement runs}\le R-1}}
    a(x)\overline{a(y)}.
$$
The all-agreement pairs contribute exactly $\operatorname{Tr}P^n$. This proves the precise raw-class identity
$$
 T_n^{[R-1]}=\operatorname{Tr}A^n-\operatorname{Tr}P^n.
$$

Eliminating the age blocks is legitimate because their internal transfer is strictly upper triangular. Its determinant contribution is one, and its Schur complement is
$$
 I-sP-\sum_{j=0}^{R-2}s^{j+2}BS^jC
 =I-\sum_{r=1}^R s^rF_r.
$$
This proves the determinant identity without invoking an orbit quotient.

For example, $n=1$ gives no nonempty raw class. At $n=2$, the two possible singleton disagreement positions give $2\operatorname{Tr}F_2$, consistent with both the transfer trace and the later logarithmic coefficient. These small cases do not require exceptions to the identity.

## 3. First-return recurrence and matrix bounds

For the unrestricted returns $R_j=MW^jM$, the Schur-complement generating function, or direct first-return decomposition, gives
$$
 R_j=\sum_{r=1}^jF_rR_{j-r},\qquad R_0=I.
$$
Both left and right renewal versions are valid. Since all $R_j$ are doubly stochastic, induction gives
$$
 F_rJ=JF_r=0\quad(r\ge2).
$$
Equivalently, these equalities follow from the fixed diagonal-pair vector of $W$.

With $E_j=R_j-J$, $G_1=E_1$, and $G_r=F_r$ for $r\ge2$, the recurrence is exactly
$$
 G_r=E_r-\sum_{j=1}^{r-1}G_jE_{r-j}.
 \tag{A1}
$$
For the $j=1$ term one uses $P E_{r-1}=E_1E_{r-1}$, because $J E_{r-1}=0$. Thus no omitted constant-mode term remains.

If $\|E_j\|\le q$, induction in (A1) yields
$$
 \|G_r\|\le q(1+q)^{r-1}.
$$
For Hilbert--Schmidt estimates, every $F_r=BS^{r-2}C$ is a contraction, and $E_1$ is the restriction of the contraction $P$ to the orthogonal complement of constants. Therefore all $\|G_j\|\le1$ can be used in (A1).

The entry bound on each physical power gives
$$
 \|E_j\|_{\rm HS}^2
 =\sum_{a,b}|(U^j)_{ab}|^4-1\le C_j-1.
$$
Consequently
$$
 \|G_r\|_{\rm HS}
 \le\sum_{j=1}^r\sqrt{C_j-1}=h_r.
$$
The sum has no dimension factor.

The separate trace estimate is essential. Since diagonal entries of $R_r$ lie between zero and $C_r/N$,
$$
 0\le\operatorname{Tr}R_r\le C_r,\qquad
 |\operatorname{Tr}E_r|\le\max(1,C_r-1).
$$
Taking traces in (A1) and using Hilbert--Schmidt Cauchy--Schwarz for each product gives
$$
 |\operatorname{Tr}G_r|
 \le\max(1,C_r-1)
      +\sum_{j=1}^{r-1}h_j\sqrt{C_{r-j}-1}=t_r.
$$
This bounds a single return trace directly. Replacing it by $N\|G_r\|$ would lose the dimension-independent conclusion; the source does not make that replacement.

## 4. The logarithmic coefficient and absolute summability

All $G_r$ annihilate constants on both sides. Thus the common constant direction contributes the factor $1-s$ both to the age determinant and to $\det(I-sP)$. On its orthogonal complement the determinant ratio is built from
$$
 G(s)=\sum_{r=1}^R s^rG_r.
$$

The finite-dimensional determinant identity gives, as a formal power series,
$$
 \sum_{n\ge1}\frac{s^n}{n}T_n^{[R-1]}
 =\sum_{m\ge1}\frac1m
   \left[\operatorname{Tr}G(s)^m
         -\operatorname{Tr}(sG_1)^m\right].
 \tag{A2}
$$
The sign is correct: the left side is
$-\log\det(I-sA)+\log\det(I-sP)$. Every coefficient has finitely many contributing words, so (A2) requires no convergence assumption.

At $m=1$, the $G_1$ term cancels. A term $\operatorname{Tr}G_r$, $r\ge2$, has degree $n=r$. Multiplying the logarithmic coefficient by $n$ therefore gives exactly the weighted contribution
$$
 \sum_{r=2}^R r\rho^{-r}|\operatorname{Tr}G_r|
 \le T_\rho.
$$
This is the correct one-return rooted multiplicity.

For $m\ge2$, an ordered return-length word $(r_1,\ldots,r_m)$ has degree $n=\sum r_i$. The coefficient factor is $n/m$, and
$$
 n/m\le R.
$$
The all-1 word cancels exactly. No additional rotation factor should be introduced; it is already encoded by (A2), including periodic words.

For every remaining ordered word, the unnormalized Hilbert--Schmidt ideal inequality gives
$$
 |\operatorname{Tr}(G_{r_1}\cdots G_{r_m})|
 \le h_{r_1}h_{r_2}\prod_{j=3}^m\|G_{r_j}\|.
$$
This remains valid for complex, nonnormal factors. It follows by grouping the first factor against the rest in the Hilbert--Schmidt trace inequality and then applying the ideal inequality to the second factor.

The weight $\rho^{-n}$ factors over the word. Allowing the previously cancelled all-1 word back into a nonnegative upper bound and summing over all ordered words yields
$$
 R H_\rho^2 a_\rho^{m-2}.
$$
If $a_\rho<1$, summing over $m\ge2$ is geometric. Tonelli applies to this nonnegative majorant and proves
$$
 \sum_{n\ge1}\rho^{-n}|T_n^{[R-1]}|
 \le T_\rho+\frac{RH_\rho^2}{1-a_\rho}.
$$
Thus the weighted coefficient series is absolutely summable. The source does not use a conditionally convergent trace rearrangement.

All $F_r$ still contain their full complex sums over internal disagreement paths before these moduli are taken. This is where the original deterministic cancellation is retained.

## 5. Original-family hypotheses and exact constants

The independently audited physical theorem supplies, simultaneously for $1\le j\le49$ and all sufficiently large odd $N$,
$$
 \|E_j\|\le1/100,\qquad
 \max_{a,b}|(U_N^j)_{ab}|^2\le4b_j/N.
$$
Accordingly choose
$$
 R=49,\quad q=1/100,\quad C_j=4b_j,\quad
 \rho=99/100,\quad C=4b_{49}.
$$

The geometric sum is exactly
$$
 a_\rho=\frac12\left[(101/99)^{49}-1\right].
$$
The elementary bounds
$$
 (101/99)^{49}<e^{98/99}<e<87/32
$$
imply $a_\rho<55/64$, hence
$(1-a_\rho)^{-1}<64/9$.

The bound $e<87/32$ is correct: its terms through degree three sum to $8/3$, and
$$
 \sum_{j\ge0}\frac1{(4+j)!}
 \le\frac1{24}\sum_{j\ge0}5^{-j}=\frac5{96},
$$
with strict inequality for some terms. Moreover
$87/32<25/9$, so $\sqrt e<5/3$. Thus
$$
 \rho^{-49}<e^{49/99}<\sqrt e<5/3.
$$

Since $b_j$ increases and $C_j\ge16$,
$$
 h_r\le r\sqrt{C-1},\qquad
 t_r\le(C-1)\left(1+\frac{r(r-1)}2\right).
$$
The exact sums are
$$
 \sum_{r=1}^{49}r=1225,
$$
$$
 \sum_{r=2}^{49}r\left(1+\frac{r(r-1)}2\right)=731324.
$$
The latter can be checked from
$\sum_{r=1}^{49}r^3=1225^2$,
$\sum_{r=1}^{49}r^2=40425$, and subtracting the $r=1$ term.

Substitution gives the exact bound
$$
 \begin{split}
 T_\rho+\frac{49H_\rho^2}{1-a_\rho}
 &\le(C-1)\left[
 \frac53\,731324+
 49\frac{64}{9}\frac{25}{9}\,1225^2\right]\\
 &=\frac{117747728740}{81}(C-1)\\
 &<1500000000(C-1).
 \end{split}
$$
The numerator and comparison with $1.5\cdot10^9$ are correct.

For $\rho=1$,
$$
 a_1=(101/100)^{49}-1<2/3,
$$
so the same argument gives
$$
 [731324+3\cdot49\cdot1225^2](C-1)
 =221323199(C-1).
$$
This verifies both stated constants without a floating-point estimate.

The pointwise and tail consequences follow directly from positivity of the weighted majorant. For $n>M$,
$\rho^n\le\rho^{M+1}$, so
$$
 \sum_{n>M}|T_n|
 \le\rho^{M+1}\sum_{n>M}\rho^{-n}|T_n|
 \le K_{49}\rho^{M+1}.
$$
All positive times are included. The threshold in $N$ is the finite common threshold from the physical theorem; no further time-dependent threshold is introduced.

## 6. Scope that must survive assembly

The exact raw class is larger than the isolated-single-disagreement class, but it is still a specific class. It requires at least one agreement and excludes runs longer than 48.

Its decomposition by occupations is
$$
 T_n^{[48]}=H_n^{[48]}+\Omega_n^{[48]}.
$$
The theorem controls the left side. It does not bound either summand separately. In particular the full nonnegative same-occupation form factor does not dominate the signed restricted sum $H_n^{[48]}$, and the concentration estimate proved for isolated disagreements does not automatically extend to 48-step runs.

The result permits every number of runs and every positive time. This should not be confused with control of every factorial correlation order in $H_{\rm diag}$. The source's explicit distinction is mathematically necessary and correct.

Subject to keeping these scope statements, the theorem can be added to the main report without altering its stated first unresolved $H_{\rm diag}$ estimate.

