> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_nonlattice_audit.md`. Embedded SHA256: `419838b92148a29f21a32c450dff633089f437462011593efcb0f8391f772847`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: exact fixed multipliers and their multiplicative independence

Research continuation, 20 October 2026. **Verdict: the stated fixed-point
and nonlattice theorems pass.** This verdict concerns their exact stated
scope, not a high-frequency estimate for quantum actions.

## Frozen inputs

| Input | SHA-256 |
|---|---|
| `root_fixed_point_multipliers.md` | `42e52ff202f56182f1ac8314fcca9d668d207c59217738a06eb2f162e9d6824a` |
| `root_fixed_multiplier_nonlattice.md` | `256352cb8b82452d7346345ab0345fd46b795e04935ecf9389940ac920c25e62` |

Both complete files were read. The exact symbol was also checked against
the ordinary-Weyl convention in the independently audited all-time and
sector reports. No earlier verdict was used as a proof of the new
number-theoretic assertion.

## 1. Direct recomputation of the fixed-point data

The actual ordinary symbol is

$$
a(q,p)=V(q)+\frac1{100}r(q+1/2)\cos(2\pi p-\alpha_0).
$$

At q=0 and q=1/2, both r terms and their first derivatives vanish.
The cosine and sine derivatives in V also give zero first derivative.
Thus these vertical lines consist of exact equilibria of the kick.
The four points with q,p in `{0,1/2}` are fixed by L modulo the lattice.

Differentiating the two products in r gives

$$
r''(0)=392\pi^2,\quad r''(1/2)=8\pi^2,
\quad V''(0)=-\frac{784}{5}\pi^2,
\quad V''(1/2)=\frac{984}{5}\pi^2.
$$

For the term `r sin(2 pi q)`, every second-derivative summand vanishes at
the indicated q because it contains r, r', or the sine. The mixed and
p-p derivatives of a vanish there. With `cos alpha_0=-3/5`, multiplying
the q-q derivatives by `125/pi^2` gives, in the stated order,

$$
-19600-6=-19606,\quad -19600+6=-19594,
\quad 24600-294=24306,\quad24600+294=24894.
$$

These calculations use the necessary shift `q+1/2`; omitting it would
change the four coefficients.

For the physical forward convention `Psi=phi_(-a)^(tau/(2 pi)) L`, the
linearized Hamiltonian vector field at any of these equilibria is

$$
\begin{pmatrix}0&0\\a_{qq}&0\end{pmatrix}.
$$

Its square is zero. The variational equation has this constant matrix
because the orbit is an equilibrium, so its time-t derivative is exactly
`I+t DX`, at all t. Multiplication by
`L=((3,-4),(-2,3))` gives

$$
\operatorname{Tr}D\Psi=6-4\frac{\tau}{2\pi}a_{qq}
 =6-2c_i\frac{\pi\tau}{125}.
$$

Thus there is no discarded term of order tau squared. The coefficients
are distinct and nonzero; the positive trace remains above two at the
specified tau. Each expanding multiplier is the positive larger root
of `z^2-T_i z+1`, and is larger than one.

The C1 nonconjugacy consequences follow by differentiating a putative
diffeomorphism conjugacy at a fixed point. The four different derivative
traces cannot all be similar to one constant derivative matrix. This
does not assert a classification of arbitrary nonlinear centralizers.

## 2. The transcendental field substitution is legitimate

Let `t_0=pi tau/125`. Lindemann's theorem implies that t_0 is
transcendental, since `tau/125` is a nonzero rational. Therefore no
nonzero rational polynomial, including a denominator, vanishes at t_0.
Evaluation is an isomorphism from `Q(t)` onto the actual real subfield
`Q(t_0)`. It preserves all field statements about squares. The argument
does not use a generic algebraic specialization.

The invoked primary theorem was checked directly: Popescu,
*A Simple and Self-contained Proof for the Lindemann-Weierstrass
Theorem*, author manuscript arXiv:2306.14352v2, Theorem 2.1, explicitly
states the transcendence of pi. Its proof begins on printed page 9.
The published chapter is in *New Frontiers in Number Theory and
Applications* (2024), DOI `10.1007/978-3-031-51959-8_16`.
The author manuscript and published metadata were opened in this audit.
Only this elementary consequence of that theorem is needed here.

## 3. Private simple zeros give the required four square classes

Over `Q(t)` let

$$
d_i(t)=(c_i t-2)(c_i t-4).
$$

Every possible coincidence among the eight zeros would require a ratio
`c_i/c_j` equal to 1, 2, or 1/2. Opposite signs rule this out immediately.
Within the negative group the absolute values are 19594 and 19606;
within the positive group they are 24306 and 24894. They are different,
and their ratios lie strictly between 1/2 and 2. All eight zeros are
therefore distinct.

Any nonempty product of the d_i has a simple zero at a point belonging
to one selected factor. A rational square has even valuation at every
finite point. Hence no nonempty selected product is a square in Q(t),
and the same holds in Q(t_0) by Section 2. Leading scalar factors do
not affect this argument; a private zero already obstructs a square.

## 4. The multiquadratic lemma needs no hidden algebraic closure claim

The induction in the source is valid. If `d_s` acquired a square root y
in a preceding multiquadratic field, every existing sign automorphism
would send y to plus or minus y. The monomial basis in the preceding
square roots has distinct simultaneous characters. Expanding y in that
basis consequently leaves only one monomial. Squaring gives a forbidden
dependence of square classes. The degree therefore doubles at every step.

After the degree is known to be `2^s`, arbitrary sign changes preserve
products of the monomial basis and define mutually independent field
automorphisms. Taking the four actual positive roots in R poses no
problem: they generate a real field of degree sixteen. Its field
automorphisms need not preserve the ordering or fix all real numbers;
only the base field `Q(t_0)` is fixed.

This last distinction matters. Changing an expanding multiplier to its
contracting reciprocal is a legitimate automorphism of this real
subfield, even though it would not be an order-preserving automorphism
of the entire real line.

## 5. Multiplicative and affine nonlattice conclusions

The exact two roots are

$$
\Lambda_i=3-c_i t_0+\sqrt{d_i(t_0)},\qquad
\Lambda_i^{-1}=3-c_i t_0-\sqrt{d_i(t_0)}.
$$

Their product is one because `(3-c_i t_0)^2-d_i(t_0)=1`. In a relation
`product Lambda_i^(n_i)=1`, changing only the sign of the i-th square
root and dividing by the original relation gives
`Lambda_i^(-2n_i)=1`. The chosen real value is above one, so `n_i=0`.
This proves all four exponents vanish. The identical argument proves
the slightly stronger assertion that such a monomial lies in the base
field only when every exponent is zero.

Clearing denominators and taking the real exponential proves rational
linear independence of the four real logarithms. No statement about
arbitrary complex logarithm branches is needed.

If `omega log Lambda_i=theta+2 pi k_i` held for a nonzero real omega,
distinct multipliers would give distinct integers k_i. Eliminating omega
and theta from the first three equations yields

$$
(k_3-k_1)(\log\Lambda_2-\log\Lambda_1)
 -(k_2-k_1)(\log\Lambda_3-\log\Lambda_1)=0.
$$

At least one coefficient is nonzero. This contradicts the just-proved
rational independence. The argument excludes an affine lattice, not
only the case theta=0.

Evaluating a nowhere-zero multiplicative coboundary at these four fixed
points gives the same forbidden equations. This implication is valid
for an equation holding at every point; the source correctly does not
apply it to a merely almost-everywhere equation without periodic-point
values.

## 6. Exact boundary of the audited result

The proof gives multiplicative independence and absence of an exact
affine lattice for the four actual fixed-point multipliers. It supplies
no quantitative lower bound for nearly vanishing integer combinations
with growing coefficients. In particular the proof is not an
application of a linear-forms-in-logarithms theorem for algebraic
numbers: these multipliers belong to an algebraic extension of the
transcendental field `Q(pi)`, not to the algebraic numbers over Q.

The potential `log J^u` is also different from the periodic-action phase
in the all-time quantum trace formula. Nonlattice behavior of the former
does not establish cancellation of the latter at frequency N. The
source explicitly preserves both distinctions. No correction to the
frozen proofs is required.

