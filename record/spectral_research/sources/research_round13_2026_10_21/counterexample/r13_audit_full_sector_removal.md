> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round13_2026_10_21/counterexample/r13_audit_full_sector_removal.md`. Embedded SHA256: `00d11197cc07012920d6bee18ae0cb1a7db2c1c49b1937bc44af6245d7e560cc`.
> [Thematic guide](../../../../../mathematics/spectral_research/topics/arithmetic.md).

# Independent audit: exact protected-sector removal

Date: 21 October 2026. Reviewer: `/root/r13_original_counterexample`.

## 1. Normalized claim and verdict

**Verdict: proved as written, with two immaterial punctuation corrections
noted below.** The original `H_diag` remains unproved and is not a conclusion
of this review.

The complete reviewed source is
`../root/exact_protected_sector_removal.md`, SHA-256
`e1535a9b624aadeaaf0097089e6aef3bdebd1613caaab67d680b2a233e4161cd`.
The reviewer independently reconstructed the critical implications from the
raw supporting proofs, rather than accepting their earlier verdicts.

For the exact original `U_N`, decompose each power trace into its exact
coherent/Abel sector integrals, one for each torus fixed point of the
classical iterate. Let `Q_(m,N)` be the sum of the sector integrals indexed
by the at most sixteen points of the protected set that are fixed by that
iterate. Then, for all sufficiently large odd `N` and **all** `m>=1`,

$$
|Q_{m,N}|\le20q_0^m,\qquad q_0=83/200.
$$

The same dimension threshold works for every `m`. For an arbitrary array
of weights of modulus at most `W`, the sum of the absolute values of the
termwise pair differences is bounded by

$$
\frac1{N^2}\sum_{m\ge1}|w_{m,N}|
\left|\,|p_{m,N}|^2-|p_{m,N}-Q_{m,N}|^2\right|
\le W\left(
\frac{40q_0}{N(1-q_0)}+
\frac{400q_0^2}{N^2(1-q_0^2)}\right).
$$

These are full exact sector terms, including their transverse corrections.
They are not contributions of quantum invariant subspaces. No convergence
of either separate unweighted infinite squared-trace series is needed or
claimed.

## 2. Raw dependencies read and checked

| Source | Exact SHA-256 | Read scope |
|---|---|---|
| `research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` | Scope and Sections 1--4.4 |
| `research_continuation_2026_10_20/exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` | Sections 1--8 |
| `research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md` | `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b` | Sections 2--8 |
| `research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md` | `355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c` | Sections 1--2 |
| `research_round13_2026_10_21/orbit_correlations/protected_actions_and_one_step_trace.md` | `b1dc645d52f16f7ca653f113796fb5d0b41764e7036f76a35b86328894ae714d` | Sections 1--2 |

The required dependency graph is:

`exact modular comb descent + coherent frame + wordwise Gaussian bounds`
implies `exact finite sector decomposition`; independently,
`exact convergent amplitude + small analytic phase`
implies `bounded-contour trace-class sector product`; then a uniform
one-edge norm bound implies the all-time sector bound; unitarity of the
original finite matrix controls all pair cross terms.

The higher-order modulus expansion and the repeated-orbit normalization
elsewhere in the Gaussian source are not dependencies here.

## 3. Exact sector and amplitude obligations: passed

The integer operators `R_n=(-1)^(n_q n_p) T_n` form an honest representation
when `N` is odd. In the raw comb calculation the metaplectic quotient is
exactly `zeta_N^(-1) M_N`, with `|zeta_N|=1`. The ordinary Fourier mode
has quotient `(-1)^(kl) T_N(l,k)`, so the half-period shift of the mixed
term in the ordinary symbol is necessary and present. The physical
time satisfies `t_*/h=tau N`; no change of the prescribed parameter occurs.

The coherent frame has the exact factor `N`. The coset regrouping uses

$$
g_{n_0}(z+w)=g_{n_0-(L^m-I)w}(z).
$$

It tiles the entire plane once per coset and introduces no extra
determinant multiplier. Absolute convergence is provided separately for
each finite `m,N` by expanding the exact operator into translated
metaplectic words. A word's coherent diagonal has a Gaussian modulus whose
whole-plane integral is independent of its real translation. The word
coefficient sum is finite. These two facts justify the regrouping.

The passage to the `m`-variable Abel integral is also justified wordwise.
Its unperturbed cyclic Hessian is

$$
H_m=-\tfrac14(6I-R-R^{-1}),
$$

with spectrum in `[-2,-1]`. For `m=1`, it equals `-1`; for `m=2`, its
eigenvalues are `-1,-2`, since the two coincident neighboring edges are
both retained. The modulus of a damped Gaussian word integral is bounded
by a determinant prefactor independent of the linear phase. This permits
the common Abel limit and the word sum to be interchanged.

For the exact amplitude, the raw proof removes all `1/h` singularities
by the real-shift integral formulas before estimating operators on analytic
strips. The analytic-scale Dyson bound is geometric for the actual tiny
time and uniform in real `h`; fixed spatial derivative bounds follow on a
smaller strip. For each nonzero fixed `h`, bounded-operator uniqueness
identifies this amplitude with the exact plane propagator kernel. Thus
its use in the Abel integral is an exact equality, rather than a truncated
semiclassical expansion. Its `h=0` value is `2 sqrt(F_(Qq))`.

The small Hessian perturbation preserves strict concavity of the cyclic
action uniformly in `m`. Coercivity of its quadratic part gives a critical
point, and strict concavity gives uniqueness. The critical equations and
the lift change by `(L^m-I)w` therefore identify the exact sectors with the
torus fixed points.

## 4. Contour and uniform trace-norm obligations: passed

For `U=(u',u)` and `V=(psi(u'),psi(u))`, monotonicity gives

$$
u'\psi(u)+u\psi(u')\le
D:=u'\psi(u')+u\psi(u).
$$

Hence the real part of the unperturbed imaginary quadratic phase is at
most `-D/2`. The centered perturbation satisfies

$$
|\operatorname{Im} g(U-iV)|
\le\eta(|U|_1+|V|_1)|V|_1\le4\eta D.
$$

The last inequality follows from oddness and monotonicity of `psi` on
nonnegative arguments, with `|psi(u)|<=|u|`. Thus the displayed bound
`Re(i Ftilde)/h <= -D/(4h)` is valid uniformly in the base point. It yields
Gaussian decay where the contour is straight and exponential decay in
the absolute real coordinate in the saturated tails.

For fixed positive regularization, finite-box side faces are controlled
by the Gaussian regulator even during separate coordinate deformations.
After deformation the entire regulator has modulus at most one. The
preceding coercive bound permits dominated removal of the regulator for
each finite `m`. No uniform-in-`m` estimate of that deformation error is
required because the resulting identity is exact for each `m`.

The weighted kernel criterion follows by setting
`A=1-d_y^2+y^2` and writing `K=A^(-1) S A^(-1)`. Since
`||A^(-1)||_HS^2=pi^2/24` and `||S||_op<=||S||_HS`,

$$
\|K\|_1\le\frac{\pi^2}{24}
\|A_{y'}A_y k\|_{L^2}.
$$

The local Taylor limit holds uniformly in base point and in each fixed
bounded set of rescaled variables. On the entire straight portion, the
coercive estimate gives a Gaussian times a fixed polynomial majorant for
the necessary derivatives. Outside that portion, its tail integral is
bounded by a fixed polynomial in `h^(-1)` times `exp(-c/h)`. These facts
justify uniform convergence in the displayed weighted norm, and hence in
trace norm. They do not use a globally Gaussian bound on a saturated
contour.

### Independent check of the reference Gaussian norms

For

$$
k_G(x,y)=\lambda_0^{-1}
e^{-3(x^2+y^2)/4+xy/2},
\qquad \lambda_0=2\sqrt\pi/\sqrt\lambda,
$$

Gaussian integration shows that the positive function
`e_0(y)=(sqrt(2)/pi)^(1/4) exp(-y^2/sqrt(2))` satisfies `K_G e_0=e_0`.
The weighted Schur test can be proved here directly: Cauchy--Schwarz with
weight `e_0(y)`, followed by symmetry of `k_G`, gives
`||K_G f||_2^2 <= ||f||_2^2`. Thus `||K_G||=1`.

Positivity of the operator follows by expanding `exp(xy/2)` into its
series of positive rank-one kernels. The sum of their traces is the
finite diagonal integral. Consequently

$$
\|K_G\|_1=\operatorname{Tr}K_G
=\lambda_0^{-1}\int e^{-y^2}\,dy
=\frac{\sqrt\lambda}{2}=\frac{1+\sqrt2}{2}.
$$

This independently verifies the two norms needed in the argument without
using the complete Hermite eigenvalue list.

The numerical perturbation constant has ample room. For `|H_ij|<=1`
and a monomial `p` of degree at most two, each differentiation of
`p exp(Y^T H Y)` changes the coefficient-sum bound by at most `d+4`
when the current polynomial degree is `d`. Up to four derivatives this
gives at most `6*7*8*9=3024`. Expanding the two oscillator operators
costs at most `4+84+84+3024=3196`, below the source's `8*10^5`.
The polynomial degree is at most six. Also

$$
\|(1+|Y|)^6e^{-|Y|^2/4}\|_2^2
\le2\pi\,2^{11}(1+2^6\cdot6!)<(25000)^2.
$$

Together with the finite Hessian and amplitude changes this is more than
sufficient for `||K_(0,x)-K_G||_1 <= 10^12 eta < 10^(-60)`.

## 5. All times and the absolutely convergent difference series: passed

Uniform one-edge convergence gives a single `h_0` with

$$
\|K_h(x)\|\le a_0=1.0001,\qquad
\|K_h(x)\|_1<b_0=1.208
$$

for all base points and all `0<h<h_0`. This threshold is selected before
any iterate length. The trace ideal inequality then gives, for every
finite positive `m`,

$$
|I_{m,N}(x)|\le\lambda^{-m/2}b_0a_0^{m-1}.
$$

The exact sector identity already holds separately for every such `m`.
There is no interchange of an asymptotic expansion with an unbounded
product length in this step.

There are at most sixteen selected points. Since `sqrt(lambda)=1+sqrt(2)`,
the strict inequalities

$$
a_0/\sqrt\lambda<83/200,
\qquad16b_0/a_0<20
$$

give the required geometric bound. The first also follows from
`sqrt(2)>141/100`, exactly as in the source. The same proof would bound
any selection of at most sixteen sectors; the protected set provides
the selection relevant to the proposed counterexample mechanism.

Finally, writing `p=p_(m,N)` and `Q=Q_(m,N)`,

$$
|\,|p|^2-|p-Q|^2|
=|2\operatorname{Re}(p\bar Q)-|Q|^2|
\le2N|Q|+|Q|^2.
$$

Multiplying by the bounded weights and summing the geometric series
from `m=1` gives the stated constants `40` and `400`. This directly
proves absolute convergence of the series of termwise differences.
It does not subtract two independently convergent infinite sums, so
there is no invalid infinity-minus-infinity step. The finite Fourier
weights of the actual pair test are included as a special case, with
an `O(N^(-1))` change after removing these sectors.

## 6. Corrections and boundary of the verdict

In the reviewed hash, the displays (0.3) and in Section 5 contain the
typographical string `left|,|p...`; the comma should be removed or replaced
by a spacing command. The intended absolute-value expression is explicit
in the prose and the proof and is the one audited above. This correction
has no effect on the argument or constants.

No original pair limit, no all-order factorial moment limit, and no
negative `H_diag` result follows. The estimate removes these finitely many
exact sectors, including their interference with the full original trace.
It leaves the exponentially large complementary family of sectors
unestimated. The precise original signed-sum obligation remains unchanged.

This is an independent mathematical review supported by the calculations
recorded here. Agreement between agents is not a formal proof certificate.
