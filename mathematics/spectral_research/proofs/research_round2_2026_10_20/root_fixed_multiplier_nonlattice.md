> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/root_fixed_multiplier_nonlattice.md`. Embedded SHA256: `256352cb8b82452d7346345ab0345fd46b795e04935ecf9389940ac920c25e62`.
> [Thematic guide](../../topics/classical_trace.md).

# Exact multiplicative independence of the four fixed-point multipliers

Research continuation, 20 October 2026. This is a statement about the
classical map associated with the **specified** quantum family at the exact
parameter `tau=10^-80`. It is not a statistical assertion about another
model and does not prove `H_diag`.

## 1. Exact input and theorem

Use the physical forward convention

$$
\Psi=\phi_{-a}^{\tau/(2\pi)}\circ
\begin{pmatrix}3&-4\\-2&3\end{pmatrix},
$$

where the actual ordinary-Weyl symbol is

$$
a(q,p)=\cos(14\pi q)+\frac{r(q)}{10}
 +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}
 +\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha_0).
$$

At the four fixed points `(0,0),(0,1/2),(1/2,0),(1/2,1/2)`, respectively,
the exactly computed derivative traces and unstable multipliers are

$$
T_i=6-2c_i t_0,\qquad t_0=\frac{\pi\tau}{125},
\qquad(c_1,c_2,c_3,c_4)=(-19606,-19594,24306,24894),
\tag{1}
$$

$$
\Lambda_i=\frac{T_i+\sqrt{T_i^2-4}}2>1.
\tag{2}
$$

The square roots in (2) are positive real roots. Formula (1) has no
discarded higher-order remainder. A derivation from the exact symbol is
given in `root_fixed_point_multipliers.md`; the essential calculation is
also reproduced in Section 2 below.

**Theorem.** The four positive real numbers `Lambda_i` are multiplicatively
independent:

$$
\boxed{\prod_{i=1}^4\Lambda_i^{n_i}=1,\quad n_i\in\mathbb Z
       \quad\Longrightarrow\quad n_1=n_2=n_3=n_4=0.}
\tag{3}
$$

Equivalently, the four real numbers `log Lambda_i` are linearly independent
over `Q`. In particular there are no real `omega!=0`, `theta` such that

$$
\omega\log\Lambda_i-\theta\in2\pi\mathbb Z
\quad\hbox{for all four }i.
\tag{4}
$$

This is an exact nonlattice statement, with no generic-parameter exception.

## 2. Verification of the trace input

At each of `q=0,1/2`, both `r(q)` and `r(q+1/2)` have value and first
derivative zero. The gradient of `a` therefore vanishes on both vertical
lines for every `p`. All four indicated points are fixed by both factors
of `Psi`. The required derivatives are

$$
r''(0)=392\pi^2,\quad r''(1/2)=8\pi^2,
\quad V''(0)=-784\pi^2/5,
\quad V''(1/2)=984\pi^2/5,
$$

where `V` is the part of `a` independent of `p`. Since
`cos alpha_0=-3/5`, at those four points

$$
D^2a(z_i)=\frac{\pi^2}{125}
\begin{pmatrix}c_i&0\\0&0\end{pmatrix}.
$$

The derivative of the Hamiltonian vector field of `-a` is the nilpotent
matrix `[[0,0],[a_qq,0]]`. Thus its time `tau/(2 pi)` flow derivative is
exactly `[[1,0],[tau a_qq/(2 pi),1]]`. Multiplication by the displayed
linear map and taking the trace gives (1). Also `|c_i|<25000` and
`0<t_0<4*10^-80/125`, so all four `T_i` are strictly larger than two.

## 3. Why the transcendental evaluation does not collapse a field relation

The only external number-theoretic input is Lindemann's theorem that
`pi` is transcendental. A published source is F. Lindemann, *Ueber die
Zahl pi*, Mathematische Annalen **20** (1882), 213--225,
DOI [10.1007/BF01446522](https://doi.org/10.1007/BF01446522).
An accessible full proof is Theorem 2.1 in S. A. Popescu,
*A Simple and Self-contained Proof for the Lindemann-Weierstrass Theorem*,
in *New Frontiers in Number Theory and Applications*, 349--366 (2024),
DOI [10.1007/978-3-031-51959-8_16](https://doi.org/10.1007/978-3-031-51959-8_16),
author manuscript [arXiv:2306.14352v2](https://arxiv.org/pdf/2306.14352).

Here `tau/125` is a nonzero rational number. Consequently `t_0` is
transcendental, and substitution `t -> t_0` is a field isomorphism
from `Q(t)` onto `Q(t_0)`. Indeed every nonzero rational polynomial has
nonzero value at `t_0`, so every denominator is legitimate and the
substitution is injective. This is different from a specialization at
an algebraic number, which can collapse a square class or a polynomial
relation.

Let `K=Q(t_0)` and put

$$
d_i=(c_i t_0-2)(c_i t_0-4),\qquad
T_i^2-4=4d_i.
\tag{5}
$$

We can check square classes over `K` by doing so over `Q(t)` before
this injective substitution.

## 4. The four square classes are independent

The eight rational numbers

$$
\frac{2}{c_1},\frac{4}{c_1},\ldots,
\frac{2}{c_4},\frac{4}{c_4}
\tag{6}
$$

are pairwise distinct. Within each pair this follows from `c_i!=0`.
Between different pairs, equality would require `c_i/c_j` to be one of
`1,2,1/2`. The four integers are distinct, the two opposite-sign groups
cannot yield these positive ratios, and within each sign group the ratio
of absolute values lies strictly between `1/2` and `2` and is not one.
Their two positive absolute values are `24306,24894`, and their two
negative absolute values are `19594,19606`.

Any nonempty product of different polynomials
`(c_i t-2)(c_i t-4)` therefore has a zero of odd order at a rational point
belonging to exactly one factor. A square in `Q(t)` has an even order at
each finite zero or pole, since the order of a quotient squared is twice
the difference of the orders of its numerator and denominator.
No such nonempty product can be a square. After substitution this proves
the independence of the four classes of `d_i` in `K^*/K^{*2}`.

## 5. Elementary proof of the multiquadratic field lemma used here

For completeness let `K` be any characteristic-zero field and let
`d_1,...,d_s` have independent square classes. We prove that

$$
E=K(\sqrt{d_1},\ldots,\sqrt{d_s})
$$

has degree `2^s`, with independent automorphisms that change the sign of
any chosen square root and fix the others.

Proceed by induction. For one square root, the assertion is just the
irreducibility of `x^2-d_1`. Suppose it holds for `s-1`. If `d_s` had a
square root `y` in the preceding field, then for every existing sign
automorphism `sigma`, `(sigma y)^2=y^2`, so `sigma y=+y` or `-y`.
The preceding induction basis consists of the products
`e_I=product_(i in I) sqrt(d_i)`. Under all sign changes, these basis
vectors have different simultaneous sign characters. Expanding `y` in
that basis shows that only one coefficient can be nonzero. Hence
`y=a e_I`, with `a in K`, implying
`d_s=a^2 product_(i in I) d_i`, contrary to square-class independence.
Therefore adjoining `sqrt(d_s)` doubles the degree.

The resulting product basis has `2^s` vectors. Assigning arbitrary signs
to its square-root generators respects the defining relations and
products, and is its own inverse; it defines the claimed field
automorphism. This proves the lemma without an unverified genericity
or specialization assertion.

In our case `d_i>0`. Adjoin their four positive real square roots to
the actual subfield `K` of `R`. The lemma applies directly to this real
field and gives degree sixteen; there is no need to assume a particular
complex branch during analytic continuation.

## 6. Proof of multiplicative independence

By (2) and (5),

$$
\Lambda_i=3-c_i t_0+\sqrt{d_i},\qquad
\Lambda_i^{-1}=3-c_i t_0-\sqrt{d_i}.
\tag{7}
$$

The second identity follows by multiplying the two expressions and
using `(3-c_i t_0)^2-d_i=1`.

Let `sigma_i` be the field automorphism that changes the sign of
`sqrt(d_i)` alone. It fixes `Lambda_j` for `j!=i` and sends `Lambda_i`
to its reciprocal. Apply it to a proposed relation in (3), then divide
by the original relation. This gives `Lambda_i^(-2n_i)=1`. Since the
actual real `Lambda_i` is strictly larger than one, `n_i=0`. Doing this
for each `i` proves (3). A rational linear relation among the four
real logarithms becomes (3) after clearing denominators and taking
the real exponential, so the logarithms are rationally independent.

In fact the same proof shows that a monomial
`product Lambda_i^(n_i)` belongs to `Q(t_0)^*` only when all `n_i=0`.
This stronger field statement is not needed for the nonlattice result.

## 7. Excluding an affine lattice, not merely a common integer period

Suppose (4) held. Write
`omega log Lambda_i=theta+2 pi k_i`, with `k_i` integers.
Distinctness of the multipliers and `omega!=0` force any two `k_i`
to be distinct. In particular, the first three equations yield

$$
(k_3-k_1)(\log\Lambda_2-\log\Lambda_1)
-(k_2-k_1)(\log\Lambda_3-\log\Lambda_1)=0.
$$

This is a nontrivial integer linear relation among the first three
logarithms, contradicting (3). This proves (4).

One direct dynamical consequence can be stated without invoking a
transfer-operator theorem. Let `J^u(x)>0` denote any unstable Jacobian
whose value at a fixed point is the expanding multiplier, as happens
with the Jacobian defined using any norm on the unstable line. There
are no `omega!=0`, real `theta`, and nowhere-zero function `v` satisfying

$$
v(\Psi x)=\exp\bigl(i\omega\log J^u(x)-i\theta\bigr)v(x)
\quad\hbox{for every }x.
\tag{8}
$$

Indeed, evaluation at the four fixed points cancels the nonzero values
of `v` and gives exactly the forbidden equations (4). No regularity of
`v` is needed for this implication. In particular a continuous
circle-valued coboundary of this form is impossible. This assertion does
not concern an equation holding only almost everywhere with uncontrolled
values at periodic points.

## 8. What this distinguishes, and what it does not estimate

All four fixed-point multipliers of a differentiable conjugate of the
bare cat map coincide with `3+2 sqrt(2)`. Here they are not only distinct:
their logarithms obey no nonzero rational relation, and there is no
common affine lattice of fixed-point logarithmic Jacobians. This rules
out a precise classical arithmetic mechanism for the actual map.

The theorem concerns the unstable-Jacobian potential. The oscillatory
phases in the required quantum traces involve the periodic actions,
the winding character and the quantum amplitude phase. They are not
the potential `log J^u`. Thus (8) is not a bound on those quantum
phases. Even for twists by `log J^u` itself, ruling out an exact
circle-valued coboundary is not a quantitative bound uniform as the
twist frequency tends to infinity. No such bound is being assumed.

In particular this theorem neither bounds nor computes the unresolved
quantity

$$
\frac1{N^2}\sum_{1\le m<2N}w(m/N)
\left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)
$$

for the fixed admissible test in the research record. The full
`H_diag` and the stated Sine_2 limit remain unproved and unrefuted.
