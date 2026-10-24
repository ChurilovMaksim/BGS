# One-step squared-trace transcendence in every odd dimension except seven

Date: 6 October 2026. Status: **exact computer-assisted project proof with independent internal audit**.

## Claim, dependencies, and prior ownership

Keep the actual raw modular quantization in
`mathematics/fixed-map/fixed_model_symmetry_theorem.md`, without changing its symbol,
midpoint convention, coupling, dimension sequence, or normalization. For
every odd integer N≥3, let

\[
 U_N(t)=e^{itA_N}M_N,\qquad
 H_N=\operatorname{Tr}(M_N)\operatorname{Tr}(A_N^2M_N)
       -\operatorname{Tr}(A_NM_N)^2.
\]

The bounded certificate and argument below establish the following statements

\[
 H_N\ne0\quad(N\ne7),                                      \tag{1}
\]

and, for every nonzero real algebraic t,

\[
 |\operatorname{Tr}U_N(t)|^2\text{ is transcendental}
       \quad(N\ne7).                                      \tag{2}
\]

At N=7, A₇=(9/10)I, H₇=0, and |Tr U₇(t)|²=1 for every real t.
In particular (2) applies at the prescribed t=10⁻⁸⁰N.

Prior FM-008 already proves (2), and its stronger all-nonzero-power
analogue, when 7∤N. Prior FM-010 already proves nonvanishing of all positive
power traces on the entire odd sequence; it does **not** assert squared-trace
transcendence at 7|N. Thus the new scope of (2) is the **one-step** trace in
odd dimensions N>7 divisible by seven, including arbitrary five-adic
ramification. The H_N certificate is a sufficient nonconstancy witness;
the trace-square implication is a reused Lindemann–Weierstrass argument.

Dependencies are the unchanged actual matrices/raw Fourier dictionary,
elementary finite Weyl and cyclotomic algebra, the displayed exhaustive
integer certificate, and the existing external dependency
EXT-POPESCU-2023: Popescu, arXiv:2306.14352v2, Theorem 3.2, exponential
linear independence over algebraic coefficients. The exact external
locator and hypothesis mapping are inherited from the maintained registry;
this work does not present a new primary-source audit.

No common-commutant theorem, simplicity of A_N, or simplicity of U_N is
required. No conclusion for powers |m|≥2 at 7|N is established here. There
is no quantitative trace estimate, eigenphase-gap estimate, Heisenberg-scale
comparison, formalization, priority claim, or BGS progress claim.

The prior-source search covered the maintained FM-008, FM-010 and FM-009
proofs, theorem/status surfaces, and searches for squared-trace,
transcendence, and nonconstant-trace statements. It is a repository
ownership check, not an exhaustive external novelty search.

## 1. Raw Weyl character for one M

Write e_N(x)=exp(2πix/N), with every inverse below taken modulo the odd N.
The actual definitions are

\[
 (T_N(a,b)\psi)(x)=e_N\bigl(b(x+a/2)\bigr)\psi(x+a),
\qquad
 (M_N)_{xy}=N^{-1/2}e_N\bigl(-(3x^2-2xy+3y^2)/8\bigr).
\]

For v=(a,b), w=(c,d), direct multiplication gives

\[
 T_N(v)T_N(w)=e_N\bigl(\omega(v,w)/2\bigr)T_N(v+w),
 \qquad \omega(v,w)=ad-bc.                                  \tag{3}
\]

Let Q(a,b)=2b²−a². Directly taking the trace of T_N(a,b)M_N gives
the exponent

\[
 -x^2/2+(b-a/2)x+ab/2-3a^2/8
 =-(x-b+a/2)^2/2+(2b^2-a^2)/4.
\]

Translation by b−a/2 is a permutation of Z/N, so for **every odd N**,

\[
 \operatorname{Tr}(T_N(v)M_N)
   =\operatorname{Tr}(M_N)e_N(Q(v)/4).                       \tag{4}
\]

The normalizing trace is nonzero. Indeed, if
G_N=Σ_x e_N(−x²/2), then

\[
 |G_N|^2=\sum_{x,y} e_N(-(x-y)(x+y)/2)=N.
\]

Here (x,y)↦(x−y,x+y) is bijective because 2 is invertible, and the
inner additive character sum vanishes unless its coefficient is zero.
Thus |Tr M_N|²=1. This is also the m=1 case of prior FM-010's Gauss trace
formula. All statements are valid with raw modular aliases; there is no
large-N or distinct-support requirement.

## 2. A single bounded integer Laurent polynomial

Write A_N=Σ_v c_vT_N(v), retaining the actual 32 raw integer modes before
modular reduction. The unchanged FM-009 coefficient source gives
d_v=4000c_v∈Z[i], and d_{−v}=conjugate(d_v). The full coefficient
array is `evidence/spectral_extension_20261006/trace_inputs/raw_coefficients.json`. The verifier additionally
expands the original trigonometric symbol with exact rational arithmetic
and checks that it gives the identical dictionary; this is an author-level
cross-check, not a separate independent audit.

Define the Laurent polynomial

\[
 P(z)=\sum_{v,w}d_vd_w
 \left(z^{Q(v+w)+2\omega(v,w)}-z^{Q(v)+Q(w)}\right).        \tag{5}
\]

The sum is over all 32² ordered pairs. Pairing (v,w) with (−v,−w)
keeps each exponent unchanged and conjugates its coefficient. Therefore
P∈Z[z,z⁻¹]. Equations (3)–(4) yield the exact identity

\[
 \boxed{\frac{4000^2H_N}{\operatorname{Tr}(M_N)^2}
       =P(e_N(4^{-1})).}                                    \tag{6}
\]

This uses the square of Tr M_N, not its absolute square. Since every
raw mode is retained and only evaluated modulo N at the end, (6) includes
all midpoint and small-dimension aliases.

Exact enumeration has the following reproducible output:

- 143 nonzero integer Laurent coefficients, support −36 through 648;
- endpoint coefficients P_{−36}=−14 and P₆₄₈=−50;
- integer content 2 and coefficient absolute sum 40,256,624;
- R(z)=z³⁶P(z)/2∈Z[z], degree 684, constant coefficient −7 and
  leading coefficient −25;
- R(z)=(z⁷−1)²V(z), with V∈Z[z] of degree 670 and
  V(1)=2,067,702,784.

The sparse Laurent array, full ascending coefficient arrays of R and V,
and exact division witnesses are included in `evidence/spectral_extension_20261006/`.

## 3. Exhaustive odd-order cyclotomic test

Suppose P vanishes at a primitive odd-order root of unity of order n.
The irreducible monic cyclotomic polynomial Φ_n divides R over Z, so
φ(n)≤684 and Φ_n mod 2 divides R mod 2. The latter polynomial is
nonzero, with unchanged degree 684.

For odd n, φ(n)²≥n: apply
p^(a−2)(p−1)²≥1 to each prime power pᵃ∥n, p≥3, and multiply.
Hence n≤684²=467,856. The product of the first seven odd primes is
4,849,845, so n has at most six distinct prime factors. Since p/(p−1)
decreases with p,

\[
 \frac n{\varphi(n)}\le
 \prod_{p\in\{3,5,7,11,13,17\}}\frac p{p-1}
 =\frac{17017}{6144},
 \qquad n\le\left\lfloor684\frac{17017}{6144}\right\rfloor
 =1894.                                                     \tag{7}
\]

The inherited `root_of_unity_screen` performs the necessary mod-2 test
for every odd n≤1894 with φ(n)≤684. There are exactly 446 such orders:
373 with 7∤n and 73 with 7|n. The only zero remainders occur at n=1,7.
Every order, totient and bit-encoded F₂ remainder is recorded in
`evidence/spectral_extension_20261006/trace_inputs/all_odd_order_F2_remainders.json`.

For reproducibility, the cyclotomic recursion takes n=pm, p prime:
Φ_n(X)=Φ_m(Xᵖ) if p|m, and Φ_m(Xᵖ)/Φ_m(X) otherwise; Φ₁=X−1.
The exact division in F₂[X] is checked, and the resulting degree is
checked against φ(n). Each odd eligible order is then divided directly.
The order bound (7), not a finite-dimension extrapolation, makes this
bounded calculation exhaustive for all odd roots of unity.

Exact monic division over Z confirms that Φ₁ and Φ₇ each divide R
with multiplicity exactly two. After division by Φ₁², the next
remainder is 101,317,436,416. After division by Φ₇², the next
remainder, in ascending powers of z, is

\[
 [-15043392,\ 2469131168,\ -5071846528,\ 1851639440,
    1156209488,\ -612458448],
\]

which is nonzero. Full quotient arrays are retained, with reconstructed
product identities checked. Thus the only odd-order roots of unity
annihilating P have orders 1 and 7. The root e_N(4⁻¹) has exact order
N because gcd(4,N)=1. Equation (6) and |Tr M_N|²=1 prove (1).

## 4. Nonconstant trace square and algebraic times

For fixed N, let the index a run over the distinct real eigenvalues of
the Hermitian algebraic-entry matrix A_N. They are algebraic. Its
spectral projectors are algebraic even when eigenvalues repeat, since

\[
 P_a=\prod_{b\ne a}\frac{A_N-bI}{a-b}.
\]

Put c_a=Tr(P_aM_N), an algebraic number. Then

\[
 F(t)=\operatorname{Tr}(e^{itA_N}M_N)=\sum_a c_ae^{ita},
\qquad
 H_N=\left(\sum_a c_a\right)\left(\sum_a a^2c_a\right)
                 -\left(\sum_a ac_a\right)^2.              \tag{8}
\]

If at most one c_a were nonzero, the last expression would vanish.
For N≠7, (1) therefore gives at least two active distinct frequencies.
Let a₊ and a₋ be the largest and smallest active frequencies. In

\[
 J(t)=\sum_{a,b}c_a\overline{c_b}e^{it(a-b)},                \tag{9}
\]

the largest frequency a₊−a₋>0 occurs uniquely at (a₊,a₋), with
nonzero coefficient c_{a₊} conjugate(c_{a₋}). Thus J is a nonconstant
finite exponential polynomial with algebraic coefficients and real
algebraic frequencies. For real t, J(t)=|F(t)|².

For any algebraic number L, collect equal frequencies in J(t)−L.
Its nonzero highest-frequency coefficient survives. At any nonzero
real algebraic t, its distinct exponents it(a−b) are algebraic and
remain distinct after collection. The registered Lindemann–Weierstrass
theorem makes a nontrivial algebraic-coefficient linear relation among
their exponentials impossible. Consequently J(t)≠L for every
algebraic L, proving (2). This argument does not assume simple spectrum
of A_N or U_N and does not imply either simplicity assertion.

## 5. The exact exception

At N=7, sum the Gaussian-integer coefficients d_v over raw residue
classes v mod 7. The only surviving class is (0,0), with coefficient
3600. Thus 4000A₇=3600I, so H₇=0 and

\[
 U_7(t)=e^{9it/10}M_7,\qquad
 |\operatorname{Tr}U_7(t)|^2=|\operatorname{Tr}M_7|^2=1
 \quad(t\in\mathbb R).
\]

This exact aggregation is checked directly in Gaussian integers, not
inferred from a numerical near-zero or from reduction at one prime.

## 6. Executed certificate and audit boundary

Run `python computations/verification/spectral_extensions.py --mode trace`.
The maintained independent reconstruction uses standard-library integer and
rational arithmetic with explicit checks active under optimization. Its
cyclotomics use a divisor-product recursion, independent of the original
prime-step screen. The 15 characteristic-zero matrix controls use direct
Jacobi entries in Q(zeta_(4N)), independently of the raw-mode dictionary.
They check bounded implementation identities; the degree and root-order
argument proves the uniform theorem.

The original author proof, checker and source provenance remain historical.
Its finite-field controls and assertion-only execution policy are not
relabeled as the maintained independent characteristic-zero replay.
All exact non-timing outputs of that independent replay are compared with
the accepted source-bound outputs. No higher-power trace result, spectral
simplicity, quantitative estimate or BGS conclusion follows here.

## Independent replay and external scope

The portable replay reconstructs 32 raw coefficients, 143 Laurent coefficients,
all 446 eligible odd-order cyclotomic remainders and 15 characteristic-zero
matrix controls. The root-order bound, not the matrix sample, proves uniformity.
The independent source audit freshly checked the registered Popescu v2 Theorem
3.2 and its collected-frequency mapping; that theorem remains an external input.
See [the scoped review](../record/trace_variance_review.md).
