> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_return_singer_research_checkpoint.md`. Embedded SHA256: `4cb1e3c83c2384f66b94689460767bdaa31832be60f2036c2b2b44fd16711ae1`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Research checkpoint: a possible sharper auxiliary clock obstruction

21 October 2026. **Candidate construction only; not an audited theorem.**
This concerns an auxiliary sequence in dimensions $N=p^2$, not the original
$e^{i10^{-80}NA_N}M_N$. It is not part of the proved-results ledger and
supplies no original Heisenberg-time signed estimate.

## 1. Candidate target

The intended auxiliary sequence would combine nearly flat probabilities and
reverse-transfer norm tending to zero for all $n\le c\sqrt N$, with
$\|\mathcal B_N\mathcal B_N^*-J_N\|\le4/(N+1)+o(N^{-1})$.
After the already proved generic microscopic perturbation, it should have
simple spectrum, distinct nontrivial ordered ratios, no dark sector, and
every square minor of every nonzero power nonzero. Nevertheless its local
limit should be a randomly shifted integer lattice, with uniformly bounded
local-count moments and a fixed negative pair defect in a band below one.
Thus loss of moment uniform integrability would not explain this candidate.

## 2. A symplectic cycle over a field extension

Put $q=p^2$, $E=\mathbb F_{p^2}$, $K=\mathbb F_{p^4}$,
$L=q+1=N+1$, and $\bar u=u^q$. Choose $\zeta\in K^*$ of exact
order $L$. Then $\bar\zeta=\zeta^{-1}$. Put
$c=\zeta-\zeta^{-1}$, $t=\zeta+\zeta^{-1}$, and use
$$
 \omega(u,v)=\operatorname{Tr}_{E/\mathbb F_p}
                  \frac{u\bar v-\bar u v}{c}.
$$
This is a nondegenerate alternating form: for $u\ne0$, the numerator,
as $v$ varies, has image the anti-invariant $E$-line $cE$.
Multiplication by $\zeta$ preserves $\omega$. In coordinates
$u=x\zeta+y$, the form becomes $\operatorname{Tr}(xy'-yx')$, and
multiplication by $\zeta$ has $E$-matrix
$$
 g_0=\begin{pmatrix}t&1\\-1&0\end{pmatrix}.
$$
Choose an $\mathbb F_p$-basis for $x$ and its trace-dual basis for $y$.
Every noncentral power $g_0^n$, $0<n<L/2$, has an invertible lower-left
block, because it is multiplication by a nonzero multiple of
$(\zeta^n-\zeta^{-n})/(\zeta-\zeta^{-1})$.
Also $g_0^n+g_0^{-n}$ is not scalar over $\mathbb F_p$: otherwise
$\zeta^n$ would satisfy a quadratic over $\mathbb F_p$, hence lie in
$E$, whereas the norm-one group intersects $E$ only in $\{\pm1\}$.

## 3. Proposed simultaneous shear selection

For a symmetric $2\times2$ matrix $Z$ over $\mathbb F_p$, set
$h_Z=\left(\begin{smallmatrix}I&Z\\0&I\end{smallmatrix}\right)$.
Writing $g_0^n=\left(\begin{smallmatrix}A_n&B_n\\C_n&D_n\end{smallmatrix}\right)$,
the upper-right block of $h_Z^{-1}g_0^nh_Z$ is
$$
 B_n(Z)=A_nZ+B_n-Z(C_nZ+D_n).
$$
Its determinant is a nonzero polynomial of degree at most four: the
highest-degree term is $(\det Z)^2\det C_n$.
The scalar $B_n(Z)_{12}-B_n(Z)_{21}$ has degree at most two.

The proposed nonidentity check for the latter is that its vanishing on
all graph planes forces the alternating form
$\beta_n(u,v)=\omega(u,(g_0^n+g_0^{-n})v)$ to vanish on all such planes.
For an alternating block matrix
$\left(\begin{smallmatrix}K&A\\-A^T&M\end{smallmatrix}\right)$, restriction
to a graph is $ZKZ+ZA-A^TZ+M$. Polynomial identity zero forces, successively,
$M=0$ by $Z=0$, $K=0$ and $A=A^T$ by $Z=sI$, and then $A$
scalar by varying symmetric $Z$. This would make $\beta_n$ a multiple
of $\omega$, contradicting nonscalarity above.

One further polynomial condition makes the two $\mathbb F_p$-components
of the norm $u\bar u\in E$, restricted to $h_Z(0,\mathbb F_p^2)$,
independent quadratic forms. A determinant between the squared and mixed
coefficients has degree at most four in $Z$ and is nonzero at $Z=0$:
there the plane is $E$, the norm is $y^2$, and for the trace-dual basis
$\beta_1,\beta_2$, the relevant coefficient ratio is
$2\beta_2/\beta_1\notin\mathbb F_p$.

For $R_p=\lfloor(p-5)/12\rfloor$, the total degree in a polynomial
zero-count union bound is $6R_p+4<p$. It should supply a simultaneous
choice of $Z$, selectable lexicographically. These coordinate formulas
and the simultaneous selection still require a finished independent check.

## 4. Weyl implementation and the spectral clock

The map $T_v\mapsto T_{gv}$, $g=h_Z^{-1}g_0h_Z$, preserves the full
finite Weyl multiplication and adjoint tables. It is a star automorphism
of the full $p^2\times p^2$ matrix algebra, hence is implemented by a
unitary $V$, unique up to scalar. A direct proof with matrix units and
an algebraic selection is intended; no unverified Weil-character theorem
is to be used.

Since $g^L=I$, a scalar normalization makes $V^L=I$. In the normalized
Weyl basis, the adjoint permutes phase-space points, so the intended trace
calculation is
$$
 |\operatorname{Tr}V^n|^2=\operatorname{Tr}\operatorname{Ad}(V^n)
 =\#\{v:g^nv=v\}=1,\qquad0<n<L.
$$
If $m_a$ are the multiplicities of the $L$-th roots, finite Parseval gives
$\sum_a m_a^2=(N^2+L-1)/L=N=\sum_a m_a$. Thus the spectrum should be
the $L$-th roots with exactly one omitted.

For invertible upper-right block $B$, the proposed kernel is the standard
quadratic Weyl intertwiner with cross coefficient $B^{-T}$, up to the
chosen covariance sign. Its entries have modulus $1/p$.
The nonzero antisymmetric part $B-B^T$ in dimension two makes
$B^{-T}-B^{-1}$ invertible; finite Fourier orthogonality should give
reverse-transfer norm exactly $1/p$. Kernel signs and coordinate
orientation must be verified against the exact Weyl convention.

## 5. Intended stationary bound

Every nonzero $g_0$-orbit has length $L$ and is a nonzero fiber of
the norm $K^*\to E^*$. In the Weyl basis, compression of the stationary
adjoint projection to a diagonal plane therefore consists of blocks
$L^{-1}{\bf1}{\bf1}^T$, of sizes equal to orbit intersections with that
plane. For two independent quadratic norm components $Q_1,Q_2$,
a prescribed nonzero fiber $(a,b)$ has at most four points:
$bQ_1-aQ_2$ is a nonzero homogeneous quadratic, hence has at most two
projective roots, and each corresponding line has at most two square roots
of the prescribed nonzero norm. Thus the proposed bound is
$$
 \|\Pi E_1(\operatorname{Ad}V)\Pi-J_N\|\le4/L.
$$
The exact identification of the coordinate plane with the norm plane chosen
in Section 3 remains to be checked in one consistent construction.

## 6. Generic perturbation and candidate pair failure

Apply the already proved algebraic-basis/binary-exponent perturbation with
$\eta_N=N^{-12}$. It should preserve the short-power properties, change
the intensity Gram norm by at most $4\eta_N$, and impose the qualitative
no-dark, nonzero-minor, and ordered-ratio properties.
The eigenphase shift is $o(N^{-1})$. The smallest circular gap would
remain at least $1/(2N)$, so local counts would be uniformly bounded.
The random-origin local limit should be the shifted integer lattice.

For any fixed nonzero admissible $b$ with
$\operatorname{supp}\widehat b\subset[-B,B]$, $B<1$, the trace formula
would give
$$
 \Delta_{2,N}(b)\longrightarrow-\int_0^B u|\widehat b(u)|^2\,du<0.
$$
The previously established perturbation estimate is $O_b(\eta_NN^2)$
and should preserve the limit.

## 7. Status and relation to the original problem

The finite-field implementation, simultaneous polynomial conditions,
Weyl-kernel orientation, algebraic choice of the implementing unitary,
and norm-fiber compression must be assembled and independently audited
before the candidate can be called a theorem.

Even a successful completion would only eliminate a larger class of
possible criteria. In particular it would warn that short-power probability
mixing and an $O(N^{-1})$ stationary Gram bound do not determine local
spectral statistics. It gives no estimate for the original signed trace
sum on times of order $N$, and is not an original-family obstruction.

