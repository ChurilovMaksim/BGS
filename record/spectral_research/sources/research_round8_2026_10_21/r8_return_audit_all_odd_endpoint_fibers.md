> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round8_2026_10_21/r8_return_audit_all_odd_endpoint_fibers.md`. Embedded SHA256: `8a69e39f2f4d672a4c76d5ec7067656b0e5cc6b094b13c8f8a313076c4a3cb0d`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit: all-odd, all-time endpoint fibers

Date: 21 October 2026. Auditor: Round 8 signed-resolvent branch.

## Source and verdict

Audited source:
`r8_weyl_all_odd_endpoint_fiber_identity.md`, SHA-256
`ec36b997ef3a38dd464d468833f78a3934b45bdc57dbc36f54987aa42a649b70`.
The source was not modified. Its companion full-weight calculation,
SHA-256
`038d6c03710c38829fba3d96367d271f5c33cdeacf94889d32cc3d7a22070109`,
was independently audited separately.

**Verdict:** no defect was found. The addendum removes the invertibility
restriction from the exact endpoint-sector classification. It holds at
every positive integer time and every odd modulus, including singular
$S^m-I$, with the original modular-half phases. Its positive
representation of the equal-endpoint sector is also correct.

The result remains an exact decomposition of the adjoint trace. It does
not estimate the remaining coherent powers at times of order $N$.

## 1. The terminal cross identity and its signs

Let $R=S^m$. For matrices $A,B$, the trace on full matrix space
of $X\mapsto AXB$ is $\operatorname{Tr}A\operatorname{Tr}B$,
as follows directly in the matrix-unit basis. Apply this to

$$
X\mapsto W(\lambda)M_N^m X M_N^{-m}W(-\lambda-\Gamma).
$$

Its trace is
$g_m(\lambda)\overline{g_m(\lambda+\Gamma)}$, by cyclicity
in the second factor. On a Weyl basis element the label becomes
$Rv-\Gamma$. It is diagonal in that basis exactly when
$(R-I)v=\Gamma$.

On this fiber, $Rv=v+\Gamma$, and the phase simplifies to

$$
\begin{aligned}
&\overline2\bigl[\omega(\lambda,Rv)
-\omega(\lambda+Rv,\lambda+\Gamma)\bigr]\\
&\qquad=\omega(\lambda,v+\overline2\Gamma)
+\overline2\omega(\Gamma,v).
\end{aligned}
$$

This verifies independently both the fiber equation and the sign of its
constant phase. Summing diagonal coefficients proves exactly (2.1).
If the fiber is empty, the terminal product is identically zero. No
Gauss-sum evaluation, primality assumption, or modular inverse of
$R-I$ occurs.

At $\Gamma=0$, the formula gives the previously proved terminal
magnitude. When $R-I$ is invertible, its unique fiber point
$(R-I)^{-1}\Gamma$ recovers the companion Cayley phase, with the
same signs.

## 2. Full-weight factorization for each relative path

The companion area identity is

$$
\mathcal A(\eta+\delta)-\mathcal A(\eta)
=\mathcal A(\delta)
+\sum_j\omega(2A_{<j}+a_j-\Gamma,x_j).
$$

Fix one fiber point $v_0$ with $(R-I)v_0=\Gamma$.
Combining the terminal phase just checked with this area difference
leaves the background-independent phase

$$
-\overline2\mathcal A(\delta)
+\overline2\omega(\Gamma,v_0),
$$

and the linear phase at site $j$

$$
\omega(x_j,A_{<j}+v_0+\overline2a_j).
$$

The background sum therefore factorizes with
$w_j=S^{-j}(A_{<j}+v_0)$. The exact local identity is

$$
F_d(\delta_j,w_j+\overline2\delta_j)
=e_N(\overline2\omega(w_j,\delta_j))
C^E_{w_j,w_j+\delta_j}.
$$

Its order and phase were independently derived and audited in the
companion calculation. The new endpoint variables obey
$w_j+\delta_j=S w_{j+1}$, and the fiber equation gives
$w_m=R^{-1}(v_0+\Gamma)=v_0=w_0$.

The total phase from the local identities is determined by

$$
\sum_j\omega(w_j,\delta_j)
=\mathcal A(\delta)+\omega(v_0,\Gamma).
$$

Its contribution cancels the background-independent phase exactly.
This verifies the full relative-path formula

$$
\mathcal T_m(\delta)
=\sum_{v_0:\,(R-I)v_0=\Gamma}
\prod_j C^E_{w_j,S w_{j+1}}.
$$

The source correctly limits the identity-label cancellation in a singular
case to the fiber element $v_0=0$. A nonzero closed relative path
forces a transition out of that identity label and hence a zero local
coefficient. Other elements of $\ker(R-I)$ need not give zero,
and the addendum does not discard them.

## 3. The complete fiber sum is a bijective change of variables

For each fixed fiber point, a closed path $w_m=w_0=v_0$ determines
the relative path uniquely by
$\delta_j=S w_{j+1}-w_j$. Conversely the displayed formula for
$w_j$ recovers this closed path. The endpoint condition follows by
telescoping:

$$
\sum_j S^j\delta_j=(S^m-I)v_0=\Gamma.
$$

This is a bijection for each fiber point. As
$C^U_{u,v}=C^E_{u,Sv}$, summing the closed products gives exactly

$$
\mathcal S_m(\Gamma)
=\sum_{v:\,(S^m-I)v=\Gamma}((C^U)^m)_{v,v}.
$$

Every nonempty fiber is a coset of the kernel, hence has cardinality
$|K|$, including over composite residue rings. Unitarity of
$C^U$ gives the stated bound $|\mathcal S_m(\Gamma)|\le|K|$.
Summing all fibers accounts for every diagonal entry once and recovers
$\operatorname{Tr}((C^U)^m)=|\operatorname{Tr}U_N^m|^2$.
No positivity of these individual nonzero sectors is asserted.

## 4. Equal-endpoint positivity and the Weyl projection

Writing the unitary full-kick product as
$L_m=\sum_\lambda v_m(\lambda)W(\lambda)$, the equal-endpoint
sector is exactly

$$
\mathcal S_m(0)=\sum_\lambda |v_m(\lambda)|^2|g_m(\lambda)|^2.
$$

The terminal magnitude is the finite character sum over $K$.
For each $\lambda$, this sum is $|K|$ when the character is
trivial on $K$ and zero otherwise. The elementary translation
argument supplied in the source proves that orthogonality for every
finite subgroup; no free-module assumption is needed. Consequently

$$
\mathcal S_m(0)=|K|\sum_{\lambda\in K^{\perp_\omega}}
|v_m(\lambda)|^2\ge0.
$$

Conjugation satisfies
$W(v)^*W(\lambda)W(v)=e_N(\omega(\lambda,v))W(\lambda)$.
Thus the average $\mathsf P_K$ in the source acts diagonally on
the normalized Weyl basis, with coefficient 1 on
$K^{\perp_\omega}$ and 0 elsewhere. It is exactly the indicated
orthogonal projection, and

$$
\mathcal S_m(0)=|K|\|\mathsf P_K(L_m)\|_{2,N}^2.
$$

Since $L_m$ is unitary, its normalized Hilbert--Schmidt norm is 1.
This proves the bound $0\le\mathcal S_m(0)\le|K|$. It does
not imply equality with $|K|$.

The extreme case $R=I$ is also consistent: all nonzero fibers are
empty, the kernel is the whole label group, and the entire trace square
lies in the equal-endpoint sector. In that case $M_N^m$ is scalar
by exact Weyl covariance, so the projection formula gives the same
value directly. The nondegenerate value 1 has not been extended to
recurrence times.

## 5. An additional bound, not needed for the source theorem

For clarity about the scale of these results, set
$a_\lambda=v_m(\lambda)g_m(\lambda)$. Grouping the original
trace square by endpoint difference gives

$$
\mathcal S_m(\Gamma)
=\sum_\lambda a_\lambda\overline{a_{\lambda+\Gamma}}.
$$

Cauchy--Schwarz and translation of the finite label set imply
$|\mathcal S_m(\Gamma)|\le\mathcal S_m(0)\le|K|$.
This slightly refines the size bound when the equal-endpoint projection
has small norm. It still contains no proved Heisenberg-time decay for
the original family, and is not used to infer one.

## 6. Direct finite check of an intermediate degeneracy

As a supplementary check on the new terminal formula, the auditor
constructed the original quadratic $M_N$ directly at $N=9$,
$m=4$. Here $S^m-I$ is singular but nonzero, with a kernel
of size 9 and nine nonempty fibers. Every terminal cross product for
all 81 choices of $\lambda$ and 81 choices of $\Gamma$ was
compared to (2.1). The largest floating-point discrepancy was less than
$9.7\times10^{-15}$.

This is solely a finite verification of the sign and fiber indexing.
The exact algebra above supplies the proof. It is not an asymptotic
spectral experiment and does not concern the universality of the
original kicked family.

## 7. Status after the audit

The all-odd, all-time sector decomposition, its complete treatment of
singular fibers, and its positive equal-endpoint formula are approved.
The remaining quantities are diagonal entries of the coherent quantum
propagator $(\operatorname{Ad}U_N)^m$. Neither the decomposition
nor the bounds proved here supply the normalized weighted trace estimate
at $m\asymp N$, and no $H_{\rm diag}$ conclusion follows.
