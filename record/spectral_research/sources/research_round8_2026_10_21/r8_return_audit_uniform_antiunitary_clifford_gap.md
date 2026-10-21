> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round8_2026_10_21/r8_return_audit_uniform_antiunitary_clifford_gap.md`. Embedded SHA256: `0b077e2b9ac15b877fbe373977991531adbbe82747ff040cd849b9a329767c33`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/symmetry.md).

# Independent audit: uniform antiunitary Clifford reversal gap

Date: 21 October 2026. Auditor: Round 8 signed-resolvent branch.

## Source and conclusion

Audited source:
`r8_original_uniform_antiunitary_clifford_gap.md`, SHA-256
`96a22f2e1ef7b79af6fcbd3768f00adb4dac2bbadfef53545bac2199cf96d3e9`.
The source was not modified.

**Conclusion:** no defect was found in the complete load-bearing proof
in Sections 1--7. It establishes, for the original exact family and all
odd dimensions,

$$
\limsup_{N\to\infty}\sup_{\Gamma\in\mathcal C_N}
N^{-1}|\operatorname{Tr}(U_N\Gamma\overline{U_N}\Gamma^*)|
\le\sqrt{(1+144\tau)/2}<3/4.
$$

It therefore proves the claimed normalized Hilbert--Schmidt gap from
every projective antiunitary Clifford reverser. There is no exception
for scalar $\Gamma$, arbitrary characters, growing modular matrices,
prime-power dimensions, or other odd composite dimensions.

The proof's only imported quantitative quantum input is the all-entry
output-label theorem in
`research_round4_2026_10_21/root_all_entry_and_arbitrary_weyl_routes.md`,
SHA-256
`c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd`.
The present audit checked its exact scope of use. The source reproves
the fixed-symbol calculus, its required classical nonreversibility, and
the trace-localization step.

Section 8 of the source records an older, stronger classical proof chain
for provenance. None of its analytic-conjugacy or $C^1$-rigidity
assertions is a hypothesis of Sections 1--7. This audit does not purport
to replace all older independent audits of that historical chain. The
map and time conventions identified there are consistent with the new
proof's explicit definitions.

## 1. Antiunitary reduction and the exact trace being estimated

Coordinate conjugation satisfies $KW_{(k,l)}K=W_{(-k,l)}$. Thus
an antiunitary normalizer is precisely $\Theta=\Gamma K$, with
$\Gamma$ a unitary normalizer. The complete finite covariance
classification in the source is valid over every odd modulus: the label
map is a linear automorphism of the additive group, the exact commutator
makes it symplectic, and the residual scalar is a character.

In particular,

$$
U_N\Theta U_N\Theta^{-1}
=U_N\Gamma\overline{U_N}\Gamma^*.
$$

For $P=U_N\Gamma$, $Q=\Gamma U_N^T$, one has
$PQ^*=U_N\Gamma\overline{U_N}\Gamma^*$ exactly. Cyclicity gives
$\operatorname{Tr}(P^*Q)=\overline{\operatorname{Tr}(PQ^*)}$.
The subsequent estimate of $V=P^*Q$ therefore controls exactly
the requested trace magnitude. The use of transpose here, rather than
an unconjugated inverse, is correct.

## 2. Symbol, exact ordinary-half signs, and fixed Egorov

Changing to $\widetilde W_{(k,l)}=(-1)^{kl}W_{(k,l)}$ shifts the
$q$-dependent coefficient of the $l=\pm1$ terms by one half.
It leaves the $l=0$ terms fixed. Thus the source's symbol (2.1),
including $r(q+1/2)$, is exactly the original quantum Hamiltonian
in this convention.

For arbitrary integer labels, the parity of the modular-half product
cancels the prefactor introduced by the ordinary-half Weyl basis:

$$
\widetilde W_u\widetilde W_v
=e^{\pi i\omega(u,v)/N}\widetilde W_{u+v}.
$$

This is an exact identity including aliases. Its commutator multiplier,
after multiplication by $i/h$, has leading term
$-4\pi^2\omega(u,v)$. The vector field
$Z=(a_p,-a_q)$ acts on a Fourier character with precisely that
leading term. Thus the sign in (2.4) is correct.

The finite support of $a$, the estimate
$|\sin x-x|\le|x|^3/6$, and the third weighted Fourier norm of
each fixed smooth transported symbol give a finite $O_g(N^{-2})$
error. Duhamel at the fixed time $t=\tau/(2\pi)$ then establishes
the asserted kick Egorov statement and its negative-time version. The
cat action is exactly $S=S_f^T$, because its parity character
vanishes. Hence the forward map of $\operatorname{Ad}U_N$ is
$\Psi=S\Phi_t$, in the stated order.

The coefficient norm estimates were also checked. The combined even
$q$-terms have Fourier one-norm $11/10$, and the other two
terms have norm at most $1/25$ each, giving $59/50<2$.
Their support satisfies $|k|+|l|\le9$.

## 3. Transpose reverses the product in the required way

Directly from matrix entries,
$\widetilde W_{(k,l)}^T=\widetilde W_{(k,-l)}$. Therefore
$A_N^T=Q_N(a\circ R_p)$, with $R_p(q,p)=(q,-p)$.
Transpose does not conjugate the scalar $i$ in the exponential,
so $E_N^T=\exp(i\tau N A_N^T)$.

The reflection is antisymplectic. Its Hamiltonian vector field satisfies
$Z_{a\circ R_p}(x)=-R_pZ_a(R_px)$, and its flow is
$R_p\Phi_{-t}R_p$. The symmetric kernel gives $M_N^T=M_N$,
so $U_N^T=M_NE_N^T$. Composition of its Egorov maps yields

$$
\Psi_T=R_p\Phi_{-t}R_pS=R_p\Psi^{-1}R_p.
$$

The equality uses $R_p S R_p=S^{-1}$. This verifies the
transpose convention, the sign of the flow time, and the order of the
cat relative to the reflected flow.

## 4. The escaping-matrix estimate has the stated smaller constant

The transposed symbol has the same support and coefficient norm. For a
basic label $e_j$, the exact commutator satisfies
$\|[A_N^T,W_{e_j}]\|\le36\pi/N<144/N$. Unitary Duhamel gives

$$
\|E_N^TW_{e_j}(E_N^T)^*-W_{e_j}\|_{2,N}\le144\tau.
$$

Here the transpose places the small-observable estimate before the cat
in $U_N^T=M_NE_N^T$. Conjugation by the cat then preserves the
error norm. This explains why the argument legitimately uses
$144\tau$, rather than the larger constant needed in the unitary
Clifford comparison.

The two products have the exact leading labels

$$
PW_{e_j}P^*=\text{phase}\,E_NW_{S_f\sigma e_j}E_N^*,
\qquad
QW_{e_j}Q^*=\text{phase}\,W_{\sigma S_fe_j}
+O_{2,N}(144\tau).
$$

The output tail is applied to $\sigma S_fe_j$, not to the
different input $S_f\sigma e_j$. Both are nonzero because the
matrices are invertible over the residue ring.

Finally, scalar subtraction gives
$\|[V,W]\|_{2,N}\le2\sqrt{1-|\operatorname{Tr}V/N|^2}$,
while direct expansion gives
$\|[V,W]\|_{2,N}^2=2-2\operatorname{Re}\langle W,VWV^*\rangle_N$.
These yield exactly
$|\operatorname{Tr}V/N|^2\le(1+144\tau+\varepsilon)/2$ in
the escaping-output case. The estimate is uniform in the character.

## 5. Bounded matrices, affine limits, and the quantum commutator map

Bounded centered columns of $\sigma S_f$ form an integer matrix
whose determinant is both bounded by $2R^2$ and congruent to 1.
For $N>2R^2+1$, its determinant is exactly 1. Multiplication by
$S_f^{-1}$ therefore leaves a finite set of fixed integral matrices
$\Sigma$, once $R$ has been fixed.

For each such matrix, the full parity and character correction gives
exact covariance by

$$
\rho_N(x)=\Sigma^Tx+
\kappa_N/N+(\alpha\gamma/2,\beta\delta/2).
$$

This follows from the integer identity
$(\Sigma v)_1(\Sigma v)_2-v_1v_2
\equiv\alpha\gamma v_1+\beta\delta v_2\pmod2$, and retains
all aliases. A subsequence of translations converges to $t_0$ on
the compact torus. For fixed $\Sigma$, the resulting symbols
converge in every fixed derivative norm, hence in Fourier one-norm and
quantization operator norm. Fixed-symbol Egorov is sufficient along this
subsequence; no rate or growing-symbol Egorov assumption is needed.

The Egorov maps of $P=U_N\Gamma$ and $Q=\Gamma U_N^T$ are
respectively $\rho\Psi$ and $\Psi_T\rho$. Consequently the
map for $D_N=PQ^*$ is

$$
\chi=\rho^{-1}\Psi_T^{-1}\rho\Psi.
$$

If this were the identity, left multiplication by $R_p$ in
$\rho\Psi=\Psi_T\rho$ would give
$(R_p\rho)\Psi=\Psi^{-1}(R_p\rho)$. The exact affine map
excluded by the next lemma is therefore $R_p\rho$, with the
reflection in this order.

## 6. Independent audit of the new affine nonreversibility lemma

### 6.1. Flow bounds and the exact fixed set

The support and coefficient bounds give, in the maximum vector norm,
$\|Z\|<36\pi<120$ and
$\|DZ\|<648\pi^2<6500$. Integration and the variational equation
then give, for either sign of time,

$$
\|d_t\|\le120|t|,
\quad \|d_t-tZ\|\le390000t^2,
\quad \|Dd_t\|\le e^{6500|t|}-1\le6501|t|.
$$

The last inequality holds throughout the stated interval
$|t|\le10^{-12}$. The constant $390000$ is exactly one half
of $6500\cdot120$.

With $B=S-I$ and
$C=B^{-1}S=\bigl(\begin{smallmatrix}1/2&1\\1/2&1/2\end{smallmatrix}\bigr)$,
the displacement map is $B G_t$, where
$G_t(x)=x+Cd_t(x)$. The derivative norm of its perturbation is
less than $10^4|t|<1$. The source correctly proves global
invertibility by solving $x=y-Cd_t(x)$ as a contraction on
$\mathbb R^2$. The inverse respects integer translations, so this
is a torus diffeomorphism.

The integer map $B=2\bigl(\begin{smallmatrix}1&2\\1&1\end{smallmatrix}\bigr)$
has four preimages of zero, since the second matrix is unimodular.
Thus $\Psi_t$ has exactly four fixed points. The actual vector
field vanishes on the full lines $q=0$ and $q=1/2$, so those
four points are exactly the stated half grid. No additional fixed
points are presumed absent without proof.

### 6.2. Exact Hessians and simultaneous derivative equations

At the four fixed points, the Hessian has only its $qq$ entry.
Independent differentiation gives the same four values, in units of
$\pi^2/125$:

$$
-19606,\quad -19594,\quad 24306,\quad 24894.
$$

The $q$-only contributions are $-784\pi^2/5$ and
$984\pi^2/5$. The shifted $r$ has second derivative
$8\pi^2$ or $392\pi^2$, multiplied by $\mp3/500$.
The odd $q$-term has zero second derivative at these points.

Because the vector field vanishes there and its derivative is
$-hE_{21}$, the flow derivative is exactly $I-thE_{21}$,
not a first-order approximation. Hence

$$
D_h=S(I-thE_{21}),\qquad \operatorname{Tr}D_h=6-4th,
$$

with four distinct traces for every nonzero $t$ in the interval.
An affine reverser must permute fixed points and conjugate the derivative
at one to the inverse derivative at its image. Determinant one makes
inverse traces equal to the original traces. Distinctness therefore
forces every fixed point to be fixed individually, and the affine
translation is zero on the torus.

For two distinct values of $h$, the equations
$LD_h=D_h^{-1}L$ imply

$$
LS=S^{-1}L,
\qquad -LSE_{21}=E_{21}S^{-1}L.
$$

Writing $L=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$,
the first equation gives $b=-2c$, $d=-a$, and the second
gives $4a+3b=0$. Thus
$L=v\bigl(\begin{smallmatrix}3&-4\\2&-3\end{smallmatrix}\bigr)=vSR_p$.
Since $2v$ and $3v$ are integers, so is $v$. The condition
$\det L=\pm1$ forces $v=\pm1$. The lemma has genuinely
reduced all integral affine candidates to exactly two matrices.

### 6.3. Both candidates fail at the actual nonzero time

For $L=SP$, where $P=\pm R_p$, the identities
$PSP=S^{-1}$ and $SPS=P$ show that reversal of $S\Phi_t$
is equivalent to $P\Phi_tP=\Phi_{-t}$. Their natural lifts agree
at zero; equality on the torus would therefore give equality of lifts,
not an unresolved integer translation.

The flow remainder then implies

$$
\|t(PZ(Px)+Z(x))\|\le780000t^2.
$$

At $x=(1/4,0)$, the first component for $P=R_p$ is
$2a_p(x)=4\pi/125$: here $r(3/4)=1$ and
$\sin\alpha_0=4/5$. For $P=-R_p$, the second component is
$-a_q(-1/4,0)-a_q(1/4,0)=8\pi/25$. To check the latter,
all even $q$-terms cancel upon differentiation at opposite points;
the remaining term has
$(r(q)\sin(2\pi q))'|_{q=1/4}=r'(1/4)=-16\pi$.
These signs and constants match the source.

Both values contradict the last inequality because
$780000|t|<4\pi/125$ on $0<|t|\le10^{-12}$.
The contradiction works for both time signs. The lemma consequently
excludes every affine torus reverser at the exact prescribed time,
without the older $C^1$-rigidity or structural-conjugacy machinery.

## 7. Trace localization, compactness, and final uniformity

For each fixed matrix and translation limit, the map $\chi$ is
analytic and nonidentity by the new lemma. The analytic fixed set has
measure zero, using the directional-derivative, Rolle, and Fubini argument
given in the source. The smooth Weyl product and trace estimates follow
from the exact Fourier calculus with all divisible aliases retained.

The smooth square partition in the localization proof is valid. Away
from the fixed set, the product symbol of a localized term vanishes by
Egorov and disjoint support. Near the fixed set, the source bounds
$|\operatorname{Tr}(D_NQ_N(h_0)^2)|$ by
$\operatorname{Tr}Q_N(h_0)^2$, using positivity of this actual
square and unitarity. It does not assume positivity of Weyl
quantization. Shrinking the fixed-set neighborhood gives
$\operatorname{Tr}D_N/N\to0$.

Any sequence violating uniformity over characters for a fixed matrix
would have a convergent translation subsequence, to which this argument
applies. Uniformity over the finite set of bounded matrices follows.
Unlike the commuting problem, $\Sigma=I$ requires no separate
pure-Weyl theorem, since the affine nonreversibility lemma also excludes
all its reflection limits.

The radius is fixed before the dimension tends to infinity. The escaping
and bounded branches cover all normalizers, and sending $\varepsilon$
to zero gives the theorem's overlap bound. The exact unitary identity

$$
\min_{|\zeta|=1}\|A-\zeta B\|_{2,N}^2
=2-2|\operatorname{Tr}(B^*A)|/N
$$

with $A=\Theta U_N\Theta^{-1}$, $B=U_N^{-1}$, proves both
claimed distance bounds. No unmentioned asymptotic parameter or
restriction on odd $N$ appears.

## 8. Stability and spectral limitation

As with the unitary Clifford gap, the antiunitary overlap supremum is
2-Lipschitz in the underlying unitary's operator norm. Indeed,

$$
\|U\Gamma\overline U\Gamma^*
-V\Gamma\overline V\Gamma^*\|_{\rm op}
\le2\|U-V\|_{\rm op},
$$

and normalized trace and absolute value preserve this bound. Taking the
supremum over $\Gamma$ does likewise. Thus the symmetry exclusion
is compatible with the separate microscopic rounding constructions;
it cannot alone determine local statistics.

The audit certifies the uniform antiunitary Clifford theorem in its
stated scope. It neither classifies arbitrary eigenbasis-dependent
antiunitaries nor proves the missing pair and higher-order signed trace
estimates. In particular no $H_{\rm diag}$ conclusion is supplied.
