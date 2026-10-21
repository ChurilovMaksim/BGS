> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round10_2026_10_21/r10_arithmetic_stationary_rational_test.md`. Embedded SHA256: `7dc028a0d85f388c1b68873ffc6cfc7c7b6e5f0435399ae039ad565e4e86f4f0`.
> [Thematic guide](../../topics/dephasing.md).

# Round 10: the arithmetic countersequence attempt and its surviving gap

21 October 2026. Agent `/root/r10_arithmetic`.

**Target retained:** a fixed admissible test `b`, fixed `k`, positive `epsilon`, and infinitely many original odd dimensions with `|Delta_(k,N)(b)| >= epsilon`, or a proof of the complete original criterion. The value `tau=10^(-80)` has not been varied. No such countersequence or proof is obtained in this note.

This is a route record and a self-contained auxiliary calculation. The calculation classifies rational orbits on which the kick is exactly inactive; it does not produce quantum eigenvectors, a spectral cluster, or a local statistical limit. In particular, it must not be counted as a gain on the unresolved pair discrepancy.

## 1. An explicit remaining arithmetic test

Let

$$
\omega=(-3+4i)/5=e^{i\alpha _0},\qquad
r(q)=(1-\cos 14\pi q)(1+\cos2\pi q).
$$

The ordinary midpoint Weyl convention is

$$
W_N(k,l)=(-1)^{kl}T_N(l,k).
$$

Indeed the modular half in `T_N` differs from the real half by the factor `(-1)^(kl)` when `N` is odd. The symbol of the exact matrix `A_N` in this convention is

$$
a(q,p)=\cos14\pi q+\frac{r(q)}{10}
 +\frac{r(q)\sin2\pi q}{100}-\frac1{10}
 +\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha _0).
\tag{1.1}
$$

To verify the last shift directly, the `l=+1` and `l=-1` terms both multiply their `k`th Fourier coefficient by `(-1)^k`; this is precisely translation of `r` by `1/2`. The `l=0` terms do not change. Thus (1.1) is not the unshifted classical function mistakenly substituted for the specified quantization.

Write

$$
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},\quad
t=-\frac{\tau}{2\pi},\quad
\Psi=\phi_a^t\circ L,
\tag{1.2}
$$

where `phi_a` is the Hamiltonian flow of (1.1). This notation is used only to inspect an exact classical arithmetic mechanism. No theorem transferring its periodic points to microscopic eigenphase clusters is assumed.

An apparently dangerous possibility is that the perturbation vanishes on an infinite family of rational cat orbits, so that the bare arithmetic phases survive there. The following computation identifies the completely untouched rational set exactly.

## 2. Rational fixed points of the kick

**Proposition 2.1.** At the fixed time `t` in (1.2), a rational point `(q,p)` of the torus is fixed by `phi_a^t` if and only if `q=0` or `q=1/2` modulo one.

### 2.1. At this time a fixed point of the flow is stationary

The Fourier support of `a` is contained in `|k|<=9, |l|<=1`. The sum of absolute values of its Fourier coefficients is at most

$$
1+\frac4{10}+\frac4{100}+\frac4{100}+\frac1{10}
=\frac{79}{50}.
\tag{2.1}
$$

Here each factor `1 +/- cos` has Fourier coefficient sum two, and `sin` and `cos` each have sum one. Consequently, for the Euclidean norm,

$$
\|X_a\|_\infty\le2\pi\sqrt{82}\,\frac{79}{50}<100,
\qquad
\|DX_a\|_\infty\le4\pi^2\,82\,\frac{79}{50}<6000.
\tag{2.2}
$$

Suppose a flow point returns to itself after `T=|t|`. Its lifted displacement has norm less than `100T<1/2`; if its displacement is an integer vector it is therefore zero. The lifted orbit is closed. If it is nonconstant, write its velocity as `v(s)`, let `M=max_[0,T] |v(s)|>0`, and choose the time origin at a maximum. Put `C=6000`. Then

$$
\left|\frac{dv}{ds}\right|\le CM,
\qquad
\int_0^T v(s)\,ds=0.
$$

It follows that

$$
M=\left|\frac1T\int_0^T(v(0)-v(s))\,ds\right|
\le\frac1T\int_0^T CMs\,ds=\frac{CMT}{2}.
\tag{2.3}
$$

Thus `CT>=2`, whereas our fixed `T` satisfies `CT<6000*10^(-80)<2`. This contradiction proves that the flow's fixed points at this time are exactly the zeros of `X_a`. Negative time gives the same fixed-point set as positive time.

### 2.2. Rational stationary points

The number `omega` is not a root of unity: otherwise `omega+omega^(-1)=-6/5` would be a rational algebraic integer, hence an integer. For rational `p`, the equation

$$
\sin(2\pi p-\alpha _0)=0
$$

would imply `e^(2 pi i p)=+/-omega`, contradicting that observation. Therefore, at a rational stationary point,

$$
0=\partial_pa
=-\frac{2\pi}{100}r(q+1/2)\sin(2\pi p-\alpha _0)
\quad\Longrightarrow\quad r(q+1/2)=0.
\tag{2.4}
$$

Using

$$
r(q+1/2)=(1+\cos14\pi q)(1-\cos2\pi q),
$$

its zero set is

$$
q=0\quad\hbox{or}\quad q=\frac{2j+1}{14},\qquad j=0,\ldots,6.
\tag{2.5}
$$

At `q=0` both `r(q)` and `r(q+1/2)`, together with their first derivatives, vanish. The first derivatives of `a` vanish for every `p`.

At `q=(2j+1)/14` put `theta=2 pi q`, `c=cos theta`, and `s=sin theta`. Then

$$
\cos14\pi q=-1,\quad \sin14\pi q=0,\quad
r(q)=2(1+c),\quad r'(q)=-4\pi s.
$$

Both `r(q+1/2)` and its first derivative vanish. Direct differentiation of (1.1) now gives

$$
\frac{\partial_qa}{2\pi}
=-\frac{s}{5}+
  \frac{-2s^2+2c(1+c)}{100}
=\frac{2c^2+c-1-10s}{50}.
\tag{2.6}
$$

For `c` in `[-1,1]`, the quadratic `2c^2+c-1` lies in `[-9/8,2]`. If `theta` is one of the indicated odd multiples of `pi/7` other than `pi`, then

$$
|s|\ge\sin(\pi/7)\ge\frac27,\qquad
10|s|\ge\frac{20}{7}>2.
\tag{2.7}
$$

The elementary sine lower bound follows from concavity on `[0,pi/2]`. Thus (2.6) cannot vanish at these six points. At `theta=pi`, equivalently `q=1/2`, it does vanish. Here again the full first derivative of `a` vanishes for every `p`. This proves Proposition 2.1.

The rationality of `p` is essential in this argument. It is not a classification of all real critical points of `a`.

## 3. Maximal completely untouched rational cat set

**Proposition 3.1.** The rational points whose entire `L` orbit lies in the fixed-point set of `phi_a^t` form exactly

$$
\mathcal G=\left\{(a/2,b/8):a\in\mathbb Z/2\mathbb Z,
                              b\in\mathbb Z/8\mathbb Z\right\}.
\tag{3.1}
$$

This set has four fixed points and six orbits of period two. On it, `Psi=L` exactly. For every odd `N`,

$$
\mathcal G\cap (N^{-1}\mathbb Z/\mathbb Z)^2=\{(0,0)\}.
\tag{3.2}
$$

**Proof.** Proposition 2.1 makes `q` and the next `q` coordinate both half-integers. Since

$$
q'=3q-4p,
$$

this requires `8p` to be an integer. Hence the point belongs to (3.1). Conversely, for the pair of residue indices `(a,b)`, the exact map is

$$
(a,b)\longmapsto(a-b\pmod2,\ 3b\pmod8).
\tag{3.3}
$$

It preserves (3.1), and its square is the identity. Its fixed points have `b=0` or `b=4`, with either value of `a`; thus there are four fixed points and `(16-4)/2=6` two-cycles. The intervening kicks are stationary, so `Psi=L` at every step. Finally, multiplication by the odd integer `N` is invertible on a finite group of order 16. Thus the only `N`-torsion point of `G` is zero, proving (3.2).

In particular, a nontrivial odd-order rational translation orbit cannot be contained in `G`: subtracting two such points would give nonzero odd torsion in a group of exponent eight. This rules out the direct construction of an untouched full odd Weyl comb from these classical points. It does not rule out other quantum states, approximate revivals, or coherent sums of many moving combs.

## 4. Why this test has not produced the required countersequence

The propositions give finitely many exact classical orbits. They do not give eigenvalues of `U_N`, let alone a number of eigenphases growing with `N`. Listing the orbits cannot replace this missing step.

For example, a cluster-based route to a fixed factorial defect would need a statement of the following kind about the **original** matrix: an arc `I_N` of length at most `C/N` contains at least `g_N` eigenphases. Choose one fixed admissible `b` that is at least `beta>0` on `[-C-1,C+1]`. Such a test is obtained by suitably widening a nonnegative band-limited Schwartz function positive near zero. For centers `alpha` in a suitable arc of length `1/N`, all the cluster labels then have `b_N(theta_j-alpha)>=beta`. Therefore

$$
M^U_{k,N}(b)\ge\frac{\beta^k}{k!N}(g_N)_k.
\tag{4.1}
$$

Here `(g)_k=g(g-1)...(g-k+1)`. If `g_N^k/N` tends to infinity, (4.1) and the exact bounded CUE benchmark would disprove the original criterion. If this ratio is merely bounded below, a comparison of constants or other contributions is still needed. A finite collection of classical points supplies neither hypothesis. No eigencluster bound of this kind has been proved here.

Equation (4.1) describes this particular attempted route; it is not a claim that every possible counterexample must contain a large individual cluster.

## 5. Previously resolved arithmetic routes checked before this attempt

The following statements are old results, not new claims of Round 10. Raw proof passages were inspected instead of inferring validity from theorem labels.

1. **Seven Jacobi components.** `arithmetic_seven_chain_cut_stability.md`, Sections 1–8, constructs seven exact path blocks at every sufficiently large odd dimension by cutting six extra edges when necessary. The perturbation has trace norm `O(N^(-2))` at the `A_N` level. At the original fixed `tau`, the complete admissible pair statistic and complete Abel statistic change by `O(tau/log N)`, unconditionally. The full criterion holds for the original family if and only if it holds for the cut family; this higher-order transfer explicitly uses the source criterion to obtain moment integrability. Thus the mere existence of exactly seven path blocks when `7|N` is not a remaining special-subsequence mechanism. The dense metaplectic factor still connects every pair of path blocks.

2. **Single oldform sectors.** The old growing-order commutator calculation covers, among others, divisors with `log d >= C(log N)^(2/3)` and proves a one-step escape of size `N^(-o(1))` from every prescribed input/output character pair. The formerly tempting `N=7^(4r), d=7^r` tower is within earlier excluded regimes. It was not re-proposed here.

3. **Coherent unions of character routes.** The exact full-route identities in `counter_growing_routing_families.md`, Section 4, were checked. For `q=d^2` character labels and time `n`, trace closure leaves exactly `q^n/F_n` potentially closed routes, while Parseval bounds the sum of their squared traces by `N^2 F_n/q`. Applying Cauchy–Schwarz to the complete coherent sum therefore loses

   $$
   \sqrt{(q^n/F_n)(F_n/q)}=d^{n-1}.
   \tag{5.1}
   $$

   The exact Fourier example in its Section 6 has perfectly flat relative-character masses and arbitrarily small block compressions, yet an exact full trace revival. It is explicitly an auxiliary model, not the original kick. It disproves a general closure implication from those estimates, not `H_diag` for the specified matrices. The small-divisor coherent-superposition proposal reaches this same unresolved full-sum step; it has not yielded an additional original-family estimate in this round.

4. **Qualitative arithmetic nonvanishing.** The all-odd obstruction to projectively algebraic eigenvectors and the Round 9 Galois spectral inequivalence do not provide polynomial-scale spectral gaps or local moment asymptotics. No new version of those qualitative statements was used as a substitute for the requested conclusion.

## 6. Published arithmetic symmetry comparison, with its hypotheses checked

M. Degli Esposti and B. Winn, *The quantum perturbed cat map and symmetry*, J. Phys. A **38** (2005), 5895–5912, DOI [10.1088/0305-4470/38/26/005](https://doi.org/10.1088/0305-4470/38/26/005), [author-hosted text](https://www.dm.unibo.it/fismat/pub/a5_26_005.pdf), Theorems 1–2 on pp. 5901–5902.

Their first construction requires dimensions divisible by four and a particular symmetry of one-coordinate shear Hamiltonians. Their second, for even `A_12`, requires `s>1` with `2s | gcd(A_12,A_22-1)`. Here the dimensions are odd, `|L_12|=4`, and `gcd(4,3-1)=2`, so the second divisibility condition has no such `s`. The symbol (1.1) also depends on both coordinates. These exact hypotheses do not furnish a spectral splitting for this problem. The paper's numerical random-matrix interpretations are not used as a universality theorem.

## 7. First still-unproved target estimate

Let

$$
\varphi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\quad
u=\mathcal F^{-1}\varphi,\quad
b_*(x)=\frac{|u(x)|^2}{2(\int\varphi)^2},\quad
w=|\widehat b_*|^2.
$$

For this one fixed admissible test alone, the first unresolved original pair comparison remains

$$
\boxed{\quad
\frac1{N^2}\sum_{1\le m<2N}w(m/N)
\left(\left|\operatorname{Tr}\big[(e^{i\tau N A_N}M_N)^m\big]\right|^2-\min(m,N)\right)
\stackrel{?}{\longrightarrow}0
\quad}
\tag{7.1}
$$

through all odd `N`. The trace in (7.1) means `Tr[(e^(i tau N A_N) M_N)^m]`. Neither its convergence nor a fixed nonzero defect along an infinite original subsequence has been proved by this arithmetic branch. The complete higher-order and all-band requirements remain beyond (7.1).

## 8. Input provenance and verification record

The frozen complete master entering Round 10 has SHA-256 `e338400f1f360b680ea74c739283b296c9c67eb4e598c2067b136f9f29773777`. The companion machine-readable manifest records hashes of the actual local input files and exact residue computations for (3.3). Hashing a complete file is provenance, not a claim that every line was reread in this branch. Proposition 2.1 and Proposition 3.1 are proved above directly from (1.1); they do not depend on the correctness of the old asymptotic proof packages.

The finite computation enumerates (3.3) exactly over the 16 residue pairs. It verifies the stated cycle bookkeeping only. It does not calculate the original large-`N` eigenphases, and is not offered as evidence for a spectral limit.
