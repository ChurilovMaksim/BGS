> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round8_2026_10_21/r8_return_audit_uniform_metaplectic_gap.md`. Embedded SHA256: `9b10fa20685716aeaf308e3a892df58fbf949c68bc24372fe367ae663a18595b`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit: uniform metaplectic-centralizer gap

Date: 21 October 2026. Auditor: Round 8 signed-resolvent branch.

## Audited version and conclusion

The complete source audited here is
`r8_original_uniform_metaplectic_symmetry_gap.md`, SHA-256
`bd607591e7d31980d828762bf4ab01fd7e84b418a8c81cb48bc8e896f86bdc78`.
The source was not edited during this audit.

**Conclusion:** no mathematical defect was found. The proof establishes,
for the prescribed fixed $\tau=10^{-80}$ and all odd dimensions,

$$
\limsup_{N\to\infty}\sup_{\substack{\sigma S_f=S_f\sigma\\\sigma\ne I}}
\frac1N\left|\operatorname{Tr}(U_N\Gamma_{N,\sigma}U_N^*
\Gamma_{N,\sigma}^*)\right|
\le \sqrt{(1+144\tau)/2}<3/4,
$$

where $\Gamma W_v\Gamma^*=W_{\sigma v}$ is exact covariance. It
therefore proves the claimed uniform normalized Hilbert--Schmidt
separation from every individual nonidentity centralizing metaplectic
element. It does not prove $H_{\rm diag}$, does not estimate a
Heisenberg-time spectral trace sum, and does not exclude arbitrary linear
combinations of the metaplectic elements.

The two substantive previously established inputs used by this proof are:

- the all-entry Weyl tail theorem in
  `research_round4_2026_10_21/root_all_entry_and_arbitrary_weyl_routes.md`,
  SHA-256
  `c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd`;
- the displayed symbol and elementary flow bounds in
  `r8_original_uniform_weyl_self_overlap.md`, SHA-256
  `7ad8afb5fa2f9098111166b70398aad2fc95bf10de508f47ae661ec25080755d`.

These are dependencies with proofs, not assumptions of random-matrix
universality. The audit checked the precise tail form and the hypotheses
needed in the present use. It did not replace the existing proof and
independent audit of the entire Round 4 oscillatory construction.

## 1. Exact algebra over every odd modulus

The Weyl operators form an orthogonal basis of the full matrix algebra
also for composite odd $N$. The exact product uses the modular inverse
of 2, and a determinant-one matrix preserves its alternating bilinear
form. Consequently $W_v\mapsto W_{\sigma v}$ defines a unital
$*$-automorphism, with no primality or squarefree hypothesis. The
matrix-unit argument supplied in the source proves existence of a unitary
implementer and its uniqueness up to a scalar.

The exact covariance of $M_N$ is with
$S_f=\bigl(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\bigr)$.
If $\sigma$ commutes with $S_f$, then
$M_N\Gamma M_N^*$ and $\Gamma$ have identical conjugation actions
on the full Weyl basis. Thus they differ by a scalar phase. This gives
the source's reduction

$$
G=\Gamma E\Gamma^*,\quad V=E^*G,\quad c=N^{-1}\operatorname{Tr}V,
\qquad r_N(\sigma)=|c|.
$$

The trace conjugation in this reduction has the correct order:
$\operatorname{Tr}(EG^*)=\overline{\operatorname{Tr}(E^*G)}$, by
cyclicity. Only absolute values are identified.

## 2. The scalar-subtracted inequality and its constant

For normalized Hilbert--Schmidt norm,

$$
\|V-cI\|_{2,N}^2=1-|c|^2,
\qquad
\|[V,W]\|_{2,N}\le 2\sqrt{1-|c|^2}.
$$

The identity

$$
\|[V,W]\|_{2,N}^2
=2-2\operatorname{Re}\langle W,VWV^*\rangle_N
$$

was checked by expansion. Therefore, if the absolute value of the final
inner product is at most $\eta+\varepsilon$, then

$$
2-2(\eta+\varepsilon)\le 4(1-|c|^2),
\quad\text{hence}\quad
|c|^2\le (1+\eta+\varepsilon)/2.
$$

This preserves the scalar component exactly. No implication from a
generator commutator to a lower bound for a commutator of exponentials
is being used.

## 3. The low-label kick estimate and the escaping-label split

For the actual ordinary-half symbol, the Fourier one-norm is below 2
and each frequency satisfies $|k|+|l|\le9$. For a basic Weyl label
$e_j$, the exact commutator therefore gives

$$
\|[A_N,W_{e_j}]\|\le 36\pi/N<144/N.
$$

The estimate remains valid when Fourier modes alias: it bounds the full
integer Fourier sum before any grouping of residues. Exact unitary
Duhamel then proves
$\|EW_{e_j}E^*-W_{e_j}\|_{2,N}\le144\tau$.
It does not assert $\|E-I\|=o(1)$.

For $u=\sigma^{-1}e_j$, exact conjugation gives

$$
|\langle W_{e_j},GW_{e_j}G^*\rangle_N|
=|\langle W_u,EW_uE^*\rangle_N|.
$$

The Round 4 all-entry theorem applies to this diagonal coefficient and
gives $C_*(1+|u|_N)^{-1/17}+C_*/N$, uniformly at every odd modulus.
Both labels are nonzero because $\sigma$ is invertible. The choice
of a fixed radius, followed by a dimension threshold, therefore controls
every escaping column simultaneously. Conjugating one side of the
inner product by $E$ changes it by at most $144\tau$, giving
exactly the estimate required in Section 2 above.

## 4. Bounded modular matrices really reduce to a finite integer set

If both centered columns of $\sigma^{-1}$ have norm at most $R$,
let $P$ be their integer matrix. Then $|\det P|\le2R^2$. The
congruence $\det P\equiv1\pmod N$, with $N>2R^2+1$, forces
$\det P=1$. Each entry of $PS_f-S_fP$ has modulus at most
$14R$, so for $N>14R$ its congruence to zero is an integer
equality. Thus only finitely many integral centralizers arise for fixed
$R$. Their inverses are integral and form another finite set.

No uniform semiclassical assertion for an unbounded integer matrix is
needed. The order of quantifiers is essential and is respected: first
fix $\varepsilon$, then $R$, then treat this finite set as
$N\to\infty$.

## 5. The modular-half parity correction and Egorov order

For $\widetilde W_v=(-1)^{v_1v_2}W_v$ and fixed integral
$\sigma=\bigl(\begin{smallmatrix}\alpha&\beta\\\gamma&\delta\end{smallmatrix}\bigr)$,
the exact parity difference is

$$
(\sigma v)_1(\sigma v)_2-v_1v_2
\equiv\alpha\gamma v_1+\beta\delta v_2\pmod2.
$$

The cross coefficient is even because
$\alpha\delta+\beta\gamma-1=2\beta\gamma$. The resulting
covariance is exactly pullback by

$$
\rho(x)=\sigma^Tx+(\alpha\gamma/2,\beta\delta/2).
$$

This full-integer-label calculation also handles aliases. For the
integral centralizers at issue,
$\sigma=\bigl(\begin{smallmatrix}a&b\\2b&a\end{smallmatrix}\bigr)$,
$a^2-2b^2=1$. Reduction modulo 4 implies that $b$ is even and
$a$ is odd. The displayed translation is then integral.

With $t=\tau/(2\pi)$ and $Z=J\nabla a$, the kick Egorov map
is $\Phi_t$. Applying the four conjugations in
$V=E^*\Gamma E\Gamma^*$ in their actual order gives pullback by

$$
\rho^{-1}\circ\Phi_t\circ\rho\circ\Phi_t^{-1}.
$$

The source has this order correctly. The fixed smooth-symbol commutator
error follows from the exact sine-minus-linear multiplier and a finite
weighted Fourier norm. Negative time introduces no new hypothesis.

## 6. Nonidentity of every needed classical commutator

Every real determinant-one matrix commuting with the cat is diagonal in
the cat's two real eigendirections. Hence it is $I$, $-I$, or
hyperbolic. There is no unaccounted unipotent case.

If a hyperbolic affine $\rho(x)=Lx+\xi$ commuted with the flow on
the torus, its lifted displacement would satisfy

$$
d_t(Lx+\xi)-Ld_t(x)=m
$$

for one integer vector $m$. Subtracting at two points removes this
integer, and iterating in both directions gives a two-sided bounded
orbit under $L$ for $d_t(x)-d_t(y)$. Hyperbolicity forces this
difference to vanish. The flow displacement is therefore constant. The
actual symbol satisfies $\nabla a(0,0)=0$, so its lift fixes zero
and that constant must be zero.

The fixed flow is not the identity: the exact coefficient
$a_{1,0}=1/20-i/200$ gives
$|\widehat Z_2(1,0)|\ge\pi/10$, while
$\|d_t-tZ\|_\infty\le78000t^2$. At the prescribed positive
$t$, its corresponding displacement coefficient is nonzero. This
argument needs neither a mean-flux hypothesis nor a bound for
$\|L\|t$.

For $L=-I$, the affine correction is zero. There is a small lift
detail implicit in the source which is valid and can be made explicit:
torus commutation first gives $d_t(-x)+d_t(x)\in\mathbb Z^2$
constant; evaluating at zero, where $d_t(0)=0$, makes that constant
zero. Thus commutation would imply exact oddness of the displacement.
But

$$
\widehat Z_2(1,0)=-\pi/100-i\pi/10,
\qquad
\widehat Z_2(1,0)+\widehat Z_2(-1,0)=-\pi/50.
$$

The even displacement coefficient has modulus at least
$\pi t/50-156000t^2>0$. Both signs and the factor 2 in the error
were checked. This excludes the last nonidentity centralizer.

## 7. The trace-vanishing lemma requires no trace formula

The finite smooth quantization has approximate multiplication, exact
adjoints, and normalized trace converging to symbol mean. Their proofs
use full Fourier sums and keep all modes divisible by $N$. For the
analytic nonidentity classical commutator, the fixed set has measure
zero. The supplied directional-derivative, Rolle, Fubini, and countable
cover proof of this analytic fact is valid on the connected torus.

The smooth square partition in the proof can be constructed from an
ordinary subordinate partition and normalization by the square root of
the sum of squares. Outside a small neighborhood of the fixed set, the
supports are disjoint from their inverse images under the map. Egorov
then makes the corresponding localized trace terms vanish.

For the remaining term the source uses positivity of
$Q_N(h_0)^2$, not an unproved positivity-preserving property of Weyl
quantization. Since $h_0$ is real, $Q_N(h_0)$ is self-adjoint,
and

$$
|\operatorname{Tr}(V_NQ_N(h_0)^2)|
\le\operatorname{Tr}Q_N(h_0)^2.
$$

Its normalized limit is $\int h_0^2$, bounded by the measure of
the chosen neighborhood. This establishes trace vanishing for each
fixed nonidentity matrix and uniformly for the already fixed finite set.

## 8. Final quantifiers, distance conversion, and scope

The escaping case and finite bounded case cover every nonidentity modular
centralizer. The limit superior, then $\varepsilon\downarrow0$,
yield the stated constant. The elementary exact identity

$$
\min_{|\zeta|=1}\|U\Gamma U^*-\zeta\Gamma\|_{2,N}^2
=2-\frac2N|\operatorname{Tr}(U\Gamma U^*\Gamma^*)|
$$

gives both distance conclusions. Because the limiting overlap bound is
strictly below $3/4$, the eventual lower bound $1/\sqrt2$
follows uniformly. The source correctly makes no effective claim about
the dimension threshold.

This audit approves the theorem in its stated scope. It supplies no
additional implication from that theorem to pair statistics or the
all-order signed hierarchy.
