> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/counter_audit_root_all_entry.md`. Embedded SHA256: `0061de6da1f97e4bbe57f3b2373b83e3df58eb37abcc9416240a48f1caefeeae`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Frozen comparison audit: all entries and arbitrary Weyl routes

21 October 2026. Audited source: root_all_entry_and_arbitrary_weyl_routes.md, SHA-256 c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd.

The entire raw source was read and compared with the independent derivation counter_all_entry_validation.md, SHA-256 5ebdc6987ebaf1d35d9902dfd03a569604a5aeb45c1d7b46bdf865fa0ce06acd. This is a mathematical comparison and an additional check of the all-time extension. It does not rely on a previous verdict for the new statement.

## 1. All-entry bounds and strict loss

The independent derivation reconstructs every substantive new step in Sections 2--7 of the root source:

- the $C^{18}$ maximum norm of the exact center-phase error, including the rational margin $127903052333056/3378810882568359375<1/4000$;
- the modified extractors with derivative orders $2,\ldots,17$, and the unchanged coefficient budgets $27$ and $3$;
- uniform one-dimensional oscillation after an arbitrary linear modulation, since the relevant derivative order is at least two;
- the alias formula with $k_m=v-w-Nm$ and $z_m\equiv-J(v-k_m/2)/N$;
- the centered-lattice inequality in the regime $|k_m|\le|v|_N$, and the periodic integration by parts in the complementary regime;
- the negative-kick argument giving the row bound;
- the low-label Egorov limit with flow sign $+J\nabla a$;
- the nonconstant displacement coefficient excluding equality in the triangle inequality;
- the finite-low-label and high-label combination producing one fixed entry gap.

The root's exact scalar in its formula (4.1) was also checked directly on a Fourier mode. The Weyl product gives
$$
\widetilde W_{-w}\widetilde W_u\widetilde W_v
=e^{\pi i[\omega(u,v+w)+\omega(v,w)]/N}
\widetilde W_{u+v-w}.
$$
This is precisely the multiplier of the shifted symbol in (4.1), with the stated scalar $e^{\pi i\omega(v,w)/N}$. In the alias pairing, shifting by $H_m=(s/2,r/2)$ contributes $e^{-2\pi i k_m\cdot H_m}$, so the displayed $\gamma_m$ is also correct.

The root proves its fixed-mode Egorov estimate in operator norm, whereas the independent source uses only normalized HS norm. The stronger root estimate is justified in this nonoscillating fixed-mode application: the difference of sine and linear Fourier multipliers is bounded by $C h^2|\omega|^3$, and the exact quantization operator norm is at most the coefficient absolute sum. Finite support in the Hamiltonian index and a fixed $C^6$ bound in the other index make that weighted sum finite. This does not introduce an operator-norm claim about the rapidly oscillating WKB approximation.

In the original modular basis the label map is $S(k,l)=(3k+2l,4k+3l)$, as follows by exchanging the coordinate order in the exact action on $(a,b)$. Its determinant is one. Thus replacing the input label by $Sv$ preserves both the supremum and the summed HS estimate.

## 2. All-time estimates, including the second HS gain

Let $M=N^2-1$, let $\|D_j\|\le\rho=1-g$ with $0<g\le1/2$, and let
$\|D_j\|_{\rm HS}/\sqrt M\le\sigma_N$. The complementary factor has norm at most $2-g$. The numbers $\delta,z_g,\eta$ in the source satisfy
$$
0<\delta<1/2,\qquad
z_g^{-\delta}(\rho+z_g(2-g))=\eta<1.
$$
The first inequality follows immediately from
$-\log(1-g/2)<\log(2(2-g)/g)$, valid throughout $0<g\le1/2$.

A word with $r\le\lfloor\delta n\rfloor$ complementary factors contains a selected factor. Using that factor in HS norm proves
$$
|\operatorname{Tr}(\mathrm{word})|/M
\le\sigma_N\rho^{n-r-1}(2-g)^r.
$$
The exact binomial majorant in the source then gives
$$
|\operatorname{Tr}B_{n,N}|/M
\le(\sigma_N/\rho)\eta^n.
$$
Summing and using $M/N^2<1$, $\rho^{-1}\le2$, and $(1-\eta)^{-1}\le4/g$ proves the stated $8\sigma_N/g$ bound.

For every $n\ge2$, the condition $\delta<1/2$ ensures at least two selected factors in each retained word. Split its cyclic trace at those two factors:
$$
|\operatorname{Tr}(A D_a B D_b)|
\le\|A D_a\|_{\rm HS}\|B D_b\|_{\rm HS}.
$$
Absorbing every remaining factor into the operator norms of $A,B$ gives
$$
|\operatorname{Tr}(\mathrm{word})|/M
\le\sigma_N^2\rho^{n-r-2}(2-g)^r.
$$
The same binomial sum and $\rho^{-2}\le4$ prove
$$
\frac1{N^2}\sum_{n\ge2}|\operatorname{Tr}B_{n,N}|
\le16\sigma_N^2/g.
$$
This validates both rates in the root's statement. The time-one term is correctly treated separately.

## 3. Scope and verdict

The trace of quantum conjugation is exactly $|\operatorname{Tr}U_N^n|^2$; removing its scalar line subtracts one. Therefore the root's correction is directly a correction of the full squared-trace functional, including all coherent cross-terms. It is not a squared trace of a claimed new unitary. Absolute summability is asserted for the correction only.

The frozen Section 9 specifies the support of its particular test $b_*$, and explicitly uses all positive indices for an arbitrary admissible test. It does not impose a Fourier-band restriction on the theorem.

**Verdict.** The new all-entry bounds, fixed entry gap, arbitrary prescribed permutation-route theorem, both all-time rates, and their stated scope are proved as written, under the exact WKB and finite-quantization inputs identified in the source. No $H_{\rm diag}$ conclusion is justified by these estimates alone.
