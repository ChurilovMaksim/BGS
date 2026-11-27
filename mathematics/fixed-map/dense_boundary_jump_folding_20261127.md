# A common jump cutoff for dense signed boundary sums

Use the [signed affine convention](boundary_prefix_audit_20261127.md), \(A=S^T\), \(W=I-A^n\), \(G=\operatorname{Fix}(S^n)\), \(K=G[N]\) and \(H=G/K\). Let \(X(d)\) be the squared physical trace, expressed as the endomorphism-space trace of the product of pointwise unitary matrices \(C(d),C(Sd),\ldots,C(S^{n-1}d)\). In the physical Fourier expansion write \(C_J\) for the cutoff to \(\|u\|_\infty\le J\). Denote the affine coefficient with this incremental jump restriction by \(a_J(h)\). For every \(d\in H\),
\[
 X_J(d):=\operatorname{Tr}_{\mathrm{End}}\prod_{i=0}^{n-1} C_J(S^id)
   =\sum_{h\in\widehat H}a_J(h)\overline{\chi_h(d)}.
\]
In Fourier propagation order a jump word has winding \(\nu=\sum_{j=0}^{n-1}A^{n-1-j}u_j\). The exact Weyl conservation law sends \(w\) to \(Aw+u_j\bmod N\). A returning diagonal entry therefore has \(Ww_0=\nu\bmod N\), so \([\nu]\in N\widehat G\), the annihilator of \(K\). It selects the unique character with \([m'(h)]=-[\nu]\). The affine equation \(W\ell_0=\nu+m'(h)\) then has a unique integer solution, whose relative deck is \(c_j=\ell_j-w_j\bmod N\). The affine recurrence reconstructs the whole word; the periodic Green bound places the retained frequencies inside any common aperture equal to one on \(\|\ell\|_\infty\le2(J+4)\). This is a bijection preserving the matrix entries and all modular aliases. The character gives \(e(\nu\cdot d)\), with \(e(t)=e^{2\pi it}\).

If a Fourier tail has uniform pointwise bound \(\delta_J\), the ordinary matrix telescope gives
\[
 \|X-X_J\|_\infty\le N^2 n\delta_J(1+\delta_J)^{n-1}.
\]
Consequently a mask \(v\) on \(\widehat H\) costs only \(\|v\|_A\), the sum of the absolute values of its normalized Fourier coefficients. Indeed the masked difference is normalized convolution of \(X-X_J\) with the inverse Fourier transform of \(v\). In particular the bound is independent of \(|H|\) for the complete sum, or for any coset of a subgroup of labels. The scalar contribution is unchanged. For the literal finite symbol the strip bound is \(\delta_J\le C e^{40|\tau|N-J/20}\); equivalently, this conclusion can be used with any pointwise Fourier-tail estimate in the preceding telescope.

## Sharp wrap cylinders

Suppose the signed displacement coordinates form the product of two centered grids, of orders \(M_1,M_2\) with ratio 1 or 2, and write \(M=\max M_i\). This holds on the odd and even embedded grids of Day 112. One prescribed wrap is the intersection of two row events \((Av)_i+b_i\in I_i\) with \(I_i\) the defining half-open coordinate interval. Each row \((Av)_i\) has denominator dividing \(M\) and belongs to \([-7/2,7/2]\). Clip its allowed interval to this range. Evaluating its exact indicator on \(M(Av)_i\bmod16M\) preserves the real membership, including the chosen endpoint convention. The cyclic interval has Wiener norm \(O(\log(2M))\) by the finite geometric sum. Each of its characters pulls back to a product of two fractional characters on the centered grids. If a grid has order \(m\), the coefficient of the character at integer index \(k\bmod m\) is bounded by
\[
 \min\bigl(1,[2\,\operatorname{dist}(\beta-k,m\mathbb Z)]^{-1}\bigr)
\]
for real frequency \(\beta\), with the bound 1 at zero distance. Summing over unit shells gives \(O(\log(2m))\), uniformly in \(\beta\). Each row costs \(O(\log^3(2M))\) and each wrap \(O(\log^6(2M))\); a complement adds at most one. Pullback by \(A\) preserves the norm and multiplication is submultiplicative. Since \(\log(2M)=O(1+n)\), a cylinder of \(k\) specified predicates costs at most \([C(1+n)^6]^k\).

On a fixed band \(aN\le n\le bN\) and at fixed \(\tau\ne0\), choose \(J=\lceil1600|\tau|N+20(D+4)\log(2N)\rceil\). The full error is \(O_{b,D}(N^{-D}e^{-40|\tau|N})\). For \(k\le c_0|\tau|N/\log(2N)\) with sufficiently small absolute \(c_0\), the masked error is \(O_{b,D}(N^{-D}e^{-20|\tau|N})\). All estimates compare common jump truncations, including at the distinguished boundary. They provide no estimate of the remaining signed trace. In fact, on the traceless sector \(C_J(0)\) is within \(\delta_J\) of unitary and \(\sigma_{\min}(C_J(0)^n)\ge(1-\delta_J)^n\). Thus the completely folded matrix has no ordinary operator-norm loss at this cutoff.

## Exact cancellation of entrance and exit

For a length-\(r\) clean run let \(q_r(h)\) be the indicator of zero centered wraps for its first \(r\) steps. At the distinguished phase the mask \(q_r(Ah)-q_r(h)\) cancels exactly, including when multiplied by any orbit-invariant predicate. Indeed \(X(Sd)=X(d)\) and \(X_J(Sd)=X_J(d)\) by cyclicity, so their signed coefficients are constant on the corresponding \(A\)-orbits. On each orbit the mask sums to zero.

The clean-run mask has Wiener norm \(O((1+n)^6)\) for \(r\le n\). An unwrapped path with endpoints \(v,A^rv\) inside the centered square stays there. The intermediate \(A^jv\) is the positive combination of those endpoints with weights \(\sinh((r-j)\log\lambda)/\sinh(r\log\lambda)\) and \(\sinh(j\log\lambda)/\sinh(r\log\lambda)\), adding the origin with the unused weight. This preserves the half-open convention. Encode the two row tests for \(A^rv\) in an auxiliary cycle of order \(4M(2+\|A^r\|_\infty)\) and apply the same fractional character bounds. Each row costs \(O((1+n)^3)\); the entrance and exit masks separately cost \(O((1+n)^{12})\). An additional orbit-invariant predicate preserves exact difference cancellation independently of its Wiener norm.
