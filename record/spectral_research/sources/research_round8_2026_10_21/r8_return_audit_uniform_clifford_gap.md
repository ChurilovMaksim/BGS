> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round8_2026_10_21/r8_return_audit_uniform_clifford_gap.md`. Embedded SHA256: `64c08f2b11e395954ec52abb556ee6c6d74f92e5e8d3b6dd7a48aa9979ac18cd`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/symmetry.md).

# Independent audit: the full Clifford-normalizer gap

Date: 21 October 2026. Auditor: Round 8 signed-resolvent branch.

## Audited version and verdict

The complete audited source is
`r8_original_uniform_clifford_symmetry_gap.md`, SHA-256
`0e4e58867f3f8745f9e3b1724fe8b269fc34cafd4dbea015e3a031495bf9d375`.
The source was not modified. The audit checked the extension independently,
including the cases absent from the centralizer theorem.

**Verdict:** no mathematical defect was found. For the exact original
family and its prescribed fixed $\tau$, the argument establishes

$$
\limsup_{\substack{N\to\infty\\N\text{ odd}}}
\sup_{\Gamma\in\mathcal C_N\setminus\mathbb CI}
\frac1N|\operatorname{Tr}(U_N\Gamma U_N^*\Gamma^*)|
\le\sqrt{(1+600\tau)/2}<3/4.
$$

Here $\mathcal C_N$ is the entire unitary normalizer of the original
finite Weyl system. Both the symplectic matrix and its character may
depend arbitrarily on $N$. The normalized Hilbert--Schmidt distance
conclusions in the source follow with the stated constants.

The proof reuses the following proved quantum inputs, with their exact
scope rather than an assumption of spectral universality:

- all-entry output-label decay from
  `research_round4_2026_10_21/root_all_entry_and_arbitrary_weyl_routes.md`,
  SHA-256
  `c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd`;
- the original-family pure-Weyl self-overlap theorem and elementary flow
  bounds in `r8_original_uniform_weyl_self_overlap.md`, SHA-256
  `7ad8afb5fa2f9098111166b70398aad2fc95bf10de508f47ae661ec25080755d`;
- the elementary implementer argument, and the trace-localization
  argument which the extension repeats, in the separately audited
  metaplectic file, SHA-256
  `bd607591e7d31980d828762bf4ab01fd7e84b418a8c81cb48bc8e896f86bdc78`.

No restriction to prime or squarefree dimensions enters any step below.

## 1. The normalizer classification is complete

If conjugation takes each $W_v$ to a scalar Weyl operator, its label
map is an additive automorphism of $(\mathbb Z/N\mathbb Z)^2$.
Additive automorphisms of this group are automatically linear over
$\mathbb Z/N\mathbb Z$. Preservation of the exact scalar
commutator makes the alternating form invariant. In dimension two this
is exactly $\det\sigma=1$, also over composite moduli.

Since $N$ is odd, the original cocycle uses an inverse of 2. Once
$\sigma$ preserves the alternating form, preservation of the exact
product law gives a multiplicative scalar function on the label group.
It is a character, necessarily $e_N(\kappa\cdot v)$. Conversely,
the determinant-one label action defines a unital $*$-automorphism
of the full matrix algebra, and the matrix-unit proof makes it unitarily
inner. Nondegeneracy of the alternating pairing ensures that multiplication
by a Weyl operator realizes every possible character.

Thus no unitary normalizers are omitted by the source's formula (1.1).
When $\sigma=I$, uniqueness of covariance up to a scalar implies
that the implementer is a scalar Weyl operator. It is nonscalar exactly
when that Weyl label is nonzero. The separate pure-Weyl theorem applies
uniformly to all these labels, even when their associated classical
translations tend to zero.

## 2. The quantum comparison uses the correct output label

Set $A=U\Gamma$, $B=\Gamma U$, $V=A^*B$. By cyclicity,
$\operatorname{Tr}(A^*B)$ is the complex conjugate of
$\operatorname{Tr}(U\Gamma U^*\Gamma^*)$. Their absolute values
are equal.

For a basic label $e_j$, exact covariance yields

$$
AW_{e_j}A^*=\text{phase}\,E W_{S_f\sigma e_j}E^*.
$$

For the other product one obtains

$$
BW_{e_j}B^*=\Gamma E W_{S_fe_j}E^*\Gamma^*
=\text{phase}\,W_{\sigma S_fe_j}+\mathcal E_j.
$$

The order $S_f\sigma e_j$ in the input and
$\sigma S_fe_j$ in the output is correct. They must not be
identified outside the centralizer.

The Fourier support of the actual ordinary-half symbol has
$|k|+|l|\le9$ and coefficient one-norm below 2. For
$S_fe_1=(3,4)$ or $S_fe_2=(2,3)$, the alternating pairing has
modulus at most 36 on this support. Therefore

$$
\|[A_N,W_{S_fe_j}]\|\le144\pi/N,
\quad
\|\mathcal E_j\|_{2,N}\le144\pi\tau<600\tau.
$$

This is the exact unitary Duhamel bound; aliases can only combine terms
which were already bounded in the full Fourier sum. It does not require
the kick to be close to the identity.

Conjugating the inner product by $A$ gives exactly

$$
|\langle W_{e_j},VW_{e_j}V^*\rangle_N|
=|\langle AW_{e_j}A^*,BW_{e_j}B^*\rangle_N|
\le |C^E_{\sigma S_fe_j,S_f\sigma e_j}|+600\tau.
$$

Both labels are nonzero modulo $N$, since all participating matrices
are invertible. The proved output-label tail is consequently applicable
when $|\sigma S_fe_j|_N$ escapes a fixed radius, whatever the input
does.

For $c=N^{-1}\operatorname{Tr}V$, the elementary bounds

$$
\|[V,W]\|_{2,N}\le2\sqrt{1-|c|^2},
\qquad
\|[V,W]\|_{2,N}^2=2-2\operatorname{Re}\langle W,VWV^*\rangle_N
$$

then give $|c|^2\le(1+600\tau+\varepsilon)/2$, with the
constant stated in the source. Scalar character phases disappear only
after taking absolute values, which is legitimate in this estimate.

## 3. Bounded output columns give a finite integral set

If both centered columns of $\sigma S_f$ have norm at most $R$,
their integer matrix $P$ satisfies $|\det P|\le2R^2$ and
$\det P\equiv1\pmod N$. For $N>2R^2+1$, this forces
$\det P=1$. Hence $\Sigma=PS_f^{-1}$ is an integral
determinant-one matrix, and there are only finitely many possibilities
when $R$ is fixed.

This step requires no centralizer congruence. If $\Sigma=I$, the
pure-Weyl case is already controlled. Each of the finitely many remaining
fixed $\Sigma$ is treated by fixed-symbol Egorov and compactness of
translations, with no growing-matrix estimate.

## 4. Exact affine covariance, varying translations, and echo order

For a fixed integral matrix
$\Sigma=\bigl(\begin{smallmatrix}\alpha&\beta\\\gamma&\delta\end{smallmatrix}\bigr)$,
conversion to the full ordinary-half Weyl labels gives

$$
\Gamma\widetilde W_v\Gamma^*
=e^{2\pi i v\cdot t_N}\widetilde W_{\Sigma v},
\qquad
t_N=\kappa_N/N+(\alpha\gamma/2,\beta\delta/2)\pmod{\mathbb Z^2}.
$$

The parity identity follows from
$\alpha\delta+\beta\gamma-1=2\beta\gamma$. It holds for
full integer labels and so retains signs at aliases. This proves exact
pullback covariance by $\rho_N(x)=\Sigma^Tx+t_N$.

After passing to a subsequence, $t_N\to t_0$ on the compact torus.
Since $\Sigma$ is fixed, composition with $\rho_N$ and its
inverse converges in every fixed derivative norm on smooth symbols. Such
convergence implies convergence of Fourier coefficient one-norms and
therefore operator-norm convergence of the corresponding quantizations.
The fixed-symbol Egorov estimate can thus be applied to the limiting
symbols, with the variable-symbol errors controlled separately by
unitarity. This justifies the compactness argument without imposing any
rate on $t_N-t_0$.

For the prescribed ordinary-half convention,

$$
\Psi=S_c\circ\Phi_t,\qquad t=\tau/(2\pi),
$$

is the forward map for $\operatorname{Ad}U_N$. In particular the
cat and flow are in the order shown. Applying the four conjugations in
$D_N=U_N\Gamma U_N^*\Gamma^*$ gives the limiting map

$$
\chi=\rho^{-1}\circ\Psi^{-1}\circ\rho\circ\Psi.
$$

The source's order is correct. Identity of this map is equivalent to
commutation of $\rho$ and $\Psi$.

## 5. Noncentralizers and hyperbolic affine centralizers

If $\rho\Psi=\Psi\rho$, the induced integer actions on the
torus fundamental group satisfy $LS_c=S_cL$, with $L=\Sigma^T$.
This immediately excludes every noncentralizer. For a centralizer, the
distinct real eigendirections of the cat diagonalize $L$. With
determinant one, its only possibilities are $I$, $-I$, or a
hyperbolic matrix. The identity case has already been removed.

Writing the lifted flow as $\Phi_t(x)=x+d_t(x)$, the lifted
commutation equation is

$$
(S_c-I)t_0+S_c\bigl(d_t(Lx+t_0)-Ld_t(x)\bigr)=m
$$

for a fixed integer vector $m$. This sign and order follow by
subtracting $\rho\Psi$ from $\Psi\rho$. If $L$ is
hyperbolic, subtraction at two points and iteration in both directions
force $d_t(x)-d_t(y)=0$ for all $x,y$, because the displacement
is bounded and periodic.

The actual symbol has $\nabla a(0,0)=0$, so its lift fixes zero and
a constant displacement would vanish. However,
$a_{1,0}=1/20-i/200$,
$|\widehat Z_2(1,0)|\ge\pi/10$, and
$\|d_t-tZ\|_\infty\le78000t^2$ make the flow nonidentity at
the prescribed time. No restriction on $\|L\|t$ or extra
ergodicity assumption is used.

## 6. Exact zero mean and all shifted reflections

The mean displacement identity used in the extension is exact in the
chosen flow lift. Since $\operatorname{div}(J\nabla a)=0$, the
flow preserves Lebesgue measure. Periodicity gives $\int J\nabla a=0$,
and therefore

$$
\int d_t(x)\,dx
=\int_0^t\int Z(\Phi_s(x))\,dx\,ds=0.
$$

For $L=-I$, integrating the lifted commutation equation consequently
forces $(S_c-I)t_0=m\in\mathbb Z^2$. As

$$
S_c-I=2\begin{pmatrix}1&2\\1&1\end{pmatrix}
$$

and the second matrix is unimodular, $2t_0\in\mathbb Z^2$.
Subtraction of this constant part leaves the exact shifted oddness
condition $d_t(-x+t_0)=-d_t(x)$. This reduction accounts for every
possible translation; it is not an assumption that the shift is small.

The coefficient of the actual Hamiltonian at $(0,1)$ is

$$
a_{0,1}=e^{-i\alpha_0}/200=(-3-4i)/1000,
$$

because $r(q+1/2)$ has mean 1. Thus the position component of the
displacement has coefficient

$$
c:=\widehat{d_{t,q}}(0,1)
=\tau(4-3i)/1000+\mathcal R,
\qquad |\mathcal R|\le2200\tau^2.
$$

The factor $t=\tau/(2\pi)$, the derivative factor $2\pi i$,
and the sign of $e^{-i\alpha_0}$ have all been checked. The remainder
bound follows from
$78000/(4\pi^2)<2200$.

For a real function, the coefficient of its composition with
$x\mapsto-x+t_0$, at a label $v$, is
$e^{-2\pi i v\cdot t_0}\overline{\widehat f(v)}$.
Consequently shifted oddness would require

$$
c+e^{-2\pi i(t_0)_p}\overline c=0.
$$

The phase is $+1$ or $-1$, by the half-period condition. The
two leading terms are respectively $8\tau/1000$ and
$-6i\tau/1000$; the remainder has modulus at most
$4400\tau^2$. Both alternatives are impossible. The $q$-shift
does not appear in this label, so the argument simultaneously excludes
all four possible half-period translations.

## 7. Trace localization and uniformity over characters

The analytic vector field is a finite trigonometric polynomial. Its
fixed sufficiently small time flow is analytic in space, which also
follows directly by complexifying the vector field on a fixed narrow
strip and applying convergent Picard iteration there. Thus the limiting
commutator $\chi$ is analytic. Having proved that it is nonidentity,
the source's directional-derivative and Fubini argument makes its fixed
set measure zero.

The repeated trace-localization proof is valid. Approximate multiplication
and the normalized trace limit are obtained from the exact Fourier Weyl
product and all its aliases. A real smooth square partition places one
term near the measure-zero fixed set and all other terms in supports
disjoint from their inverse images under $\chi$. Egorov kills
the latter localized terms. For the former, the source correctly uses
the positive matrix $Q_N(h_0)^2$, not positivity of Weyl quantization:

$$
|\operatorname{Tr}(D_NQ_N(h_0)^2)|
\le\operatorname{Tr}Q_N(h_0)^2.
$$

The normalized limit is bounded by the measure of the chosen
neighborhood. It follows that $N^{-1}\operatorname{Tr}D_N\to0$
on every convergent-character subsequence for a fixed nonidentity
$\Sigma$.

If convergence were not uniform over characters, a violating sequence
would have a convergent translation subsequence by compactness, producing
exactly the contradiction just proved. Uniformity over the fixed finite
set of matrices then follows. This is a valid compactness argument, not
an unproved uniform remainder bound.

## 8. Completion, stability check, and exact limitation

The three classes in the source cover the full projective normalizer:
an escaping output column, a member of the bounded finite integral set
with nonidentity matrix, or a nontrivial pure Weyl translation. Their
respective limiting bounds are
$\sqrt{(1+600\tau+\varepsilon)/2}$, 0, and a number below
$11\tau$. Fixing the radius before the dimension limit, and then
sending $\varepsilon$ to zero, proves the claimed constant.

The distance conversion is the exact identity

$$
\min_{|\zeta|=1}\|U\Gamma U^*-\zeta\Gamma\|_{2,N}^2
=2-2N^{-1}|\operatorname{Tr}(U\Gamma U^*\Gamma^*)|.
$$

Since the limiting overlap bound is strictly less than $3/4$, the
eventual separation $1/\sqrt2$ holds uniformly. No effective
dimension threshold is claimed or established.

As a further check on the scope, this property is stable under arbitrary
$o(1)$ operator-norm perturbations. Indeed, for any unitaries $U,V$
and any unitary $\Gamma$,

$$
\left|N^{-1}|\operatorname{Tr}(U\Gamma U^*\Gamma^*)|
-N^{-1}|\operatorname{Tr}(V\Gamma V^*\Gamma^*)|\right|
\le2\|U-V\|_{\rm op}.
$$

This follows by a two-term telescoping expansion and
$|\operatorname{Tr}X|/N\le\|X\|_{\rm op}$. Taking the
supremum over the normalizer preserves the bound. In particular the
theorem cannot by itself force microscopic spectral statistics: the
separate microscopic rounding constructions preserve this gap while
altering those statistics. This consistency check does not affect the
proved original-family theorem and supplies no counterexample for the
original $U_N$.

The audit approves the theorem in its stated full-Clifford scope. It
does not upgrade it to the missing signed trace estimates or to
$H_{\rm diag}$.
