> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/arithmetic_exact_sector_three_cell_bridge_audit.md`. Embedded SHA256: `b7cf3ce194cffd8dac98ac85af5b9dcf9dbfbf8aaadd4d2089b8876088b539a7`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Exact sectors and the three-cell contribution to the original double trace sum

Independent second audit and a missing explicit bridge, 20 October 2026.

## 0. Scope and immutable inputs

This note concerns the matrices in the question, with the exact fixed
parameter `tau=10^-80`, and all sufficiently large odd `N`. There is no
restriction involving the prime divisors of `N`. It proves that the signed
three-cell profile already established for the principal scalar cocycle
also describes a precisely specified subsum of the **exact** double
periodic-sector expansion of `|Tr U_N^m|^2`.

The distinction matters. A bound for the error of the whole trace does not,
by itself, justify replacing an arbitrarily selected subsum of its square.
The repair here uses a relative estimate for each sector and an independent
positive upper bound for the absolute mass of the selected family.

The following complete source texts were reread, rather than accepted on
the strength of earlier audit labels.

| Source | SHA-256 |
|---|---|
| `../research_continuation_2026_10_20/exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` |
| `../research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` |
| `../research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md` | `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b` |
| `fermionic_signed_three_cell_profile.md` | `edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5` |

The coding and positive-transfer inputs used below have hashes

* `fermionic_quantitative_pressure.md`:
  `d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2`;
* `fermionic_homoclinic_and_doubled_transfer.md`:
  `85e74eda0116dbbda1e3ba7a1028fbeb36da97072b7a92b3addc5d3004024168`;
* `fermionic_coherent_pair_mass.md`:
  `dc6ff71218f427c6d4dc0da4d7c3b833d641cd7107eb43e65d9f11da4e498816`.

The pertinent coding, branch, word-weight, and uniqueness arguments in
these inputs were checked again. The first four sections of the evolving
report `../Spectral_partial_results_2026-10-20.md` were also checked; the
report itself is not used as a proof input.

The exact formulas and estimates needed from the analytic construction
are stated below, together with the checks that justify their time
uniformity. The new bridge and its absolute-mass estimate are proved in
full in Sections 4--8. This note does not prove or refute `H_diag`.

## 1. The actual one-step operator and the analytic issue

Put

$$
 h=(2\pi N)^{-1},\qquad t=\tau/(2\pi),\qquad
 L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},\qquad
 \lambda=3+2\sqrt2.
$$

In the ordinary real Weyl convention the plane symbol is

$$
 a(q,p)=V(q)+\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha _0),
 \qquad
 V(q)=\cos(14\pi q)+\frac{r(q)}{10}
       +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}.
 \tag{1.1}
$$

The half shift in (1.1) is required: ordinary Weyl quantization of the
mode `(k,l)` descends to `(-1)^(kl) T_N(l,k)`. The resulting plane
operator `A_h` descends exactly to `A_N`. With the metaplectic kernel

$$
 \mu_L(Q,q)=C_h e^{iF_0(Q,q)/h},\qquad
 C_h=\frac{e^{i\pi/4}}{\sqrt{8\pi h}},\qquad
 F_0=-\frac{3Q^2-2Qq+3q^2}{8},
$$

the plane operator `V_h=e^(itA_h/h) mu_L` descends to
`zeta_N^(-1) U_N`, where

$$
 \zeta_N=e_8(3N-1).
 \tag{1.2}
$$

The eight-term Gauss sum in the descent computation gives this scalar
with the stated positive square-root convention. Thus no unspecified
metaplectic phase enters the orbit weights below.

The exact amplitude source proves

$$
 V_h(Q,q)=C_h e^{iF(Q,q)/h}B_h(Q,q),\qquad
 F=F_0+G,
 \tag{1.3}
$$

for the actual time `t`. Here `F` solves `F_t=a(Q,F_Q)`, generates
`Psi=phi_a^(-t) L`, and is real on the real plane. The uniform bound
`|D^2G| <= 2*10^7 |t|` is more than sufficient below. The amplitude is
holomorphic on a fixed spatial strip and has uniform first and second
real-`h` derivatives on a smaller strip. It has the expansion

$$
 B_h=B_0+ihb_1+O(h^2),\qquad
 B_0=2\sqrt{F_{Qq}}>0,
 \tag{1.4}
$$

with `B_0,b_1` real on real arguments.

The potentially dangerous analytic step in that source is valid for the
following reason. The real-`h` finite shifts preserve horizontal complex
strips, and the amplitude equation contains

$$
 \frac{f(Q+ch)-f(Q)}h
       =c\int_0^1 f_Q(Q+uch)\,du.
 \tag{1.5}
$$

For fixed real `h` it therefore loses one spatial analytic derivative,
uniformly as `h` tends to zero. It is not an evolution with a loss of two
derivatives hidden behind an asymptotic expansion. On nested strips the
source proves

$$
 \|\partial_h^j\mathcal L_h f\|_\rho
 \le 10^6\delta^{-j-1}\|f\|_{\rho+\delta},
 \qquad j=0,1,2.
$$

Dividing an available width `Delta=.001` into `n` pieces bounds the
`n`th Dyson term by `(e*10^6*|t|/Delta)^n`. For the larger auxiliary
time `|t|<=10^-12`, this ratio is below `.002719`; the differentiated
series have only fixed polynomial factors in `n`. The actual time is
much smaller. At each nonzero real `h`, the conjugated amplitude solves
a bounded analytic-strip equation whose uniqueness identifies (1.3)
with the exact exponential. This is not an asymptotic replacement of
the one-step kernel.

## 2. Exact sector decomposition and the number of sectors

The physical translations are

$$
 (T_{(u,v)}\psi)(q)=e^{iv(q-u/2)/h}\psi(q-u),\qquad
 R_n=(-1)^{n_qn_p}T_n,\quad n\in\mathbb Z^2.
$$

For odd `N`, the operators `R_n` form an honest representation of
`Z^2`, and `V_h R_n=R_{Ln}V_h`. Periodizing coherent states gives
the exact finite-dimensional frame identity. Grouping the resulting
absolutely convergent lattice sum by cosets gives

$$
 \operatorname{Tr}U_N^m
 =\zeta_N^m
   \sum_{[n]\in\mathbb Z^2/(L^m-I)\mathbb Z^2}
     \mathfrak T_h(R_{-n}V_h^m),
 \tag{2.1}
$$

where

$$
 \mathfrak T_h(B)=\frac1{2\pi h}
                \int_{\mathbb R^2}\langle z|B|z\rangle\,dz.
$$

There is no determinant prefactor in (2.1). Translation of a coherent
cell by an integer vector shifts its winding label by `(L^m-I)w`;
within each coset the translated cells tile the whole plane once.

Here the use of all times is an exact finite-iterate assertion. For
each fixed pair `(m,N)`, expand `V_h^m` into translated metaplectic
words. Their coefficients have finite total mass, including every
fixed exponential moment of their translation vectors. The coherent
diagonal of a translated metaplectic word has an integrable Gaussian
majorant; its plane integral is bounded independently of the word's
translation. These facts justify the grouping leading to (2.1).
The bounds used in this step may grow with `m,N`; no uniform error
estimate is extracted from this intermediate expansion.

Each sector also has the exact common Abel-regularized path form

$$
 \begin{split}
 \mathfrak T_h(R_{-n}V_h^m)
 ={}&(-1)^{n_qn_p}\lim_{\epsilon\downarrow0}
     \int_{\mathbb R^m}e^{-\epsilon\sum q_j^2}
     e^{-in_p(q_0+n_q/2)/h}
     \prod_{j=0}^{m-1}V_h(q_{j+1},q_j)\,d\mathbf q,\\
 &q_m=q_0+n_q.
 \end{split}
 \tag{2.2}
$$

For the quadratic words used to prove (2.2), the Hessian is

$$
 -\frac14(6I-\mathcal R-\mathcal R^{-1}),
 \tag{2.3}
$$

where `R` is the cyclic shift, with its actual multiplicities also for
`m=1,2`. Its eigenvalues lie in `[-2,-1]`. Gaussian integration with
positive damping is bounded uniformly in the word's real linear
term. Summability of the coefficients thus permits the Abel limit.
This avoids an interchange of undamped, conditionally convergent
integrals.

The nonlinear sector action is

$$
 \mathcal S_n(\mathbf q)=\sum_{j=0}^{m-1}F(q_{j+1},q_j)
                 -n_p(q_0+n_q/2).
 \tag{2.4}
$$

Its Hessian differs from (2.3) in operator norm by at most
`4 sup|D^2G|`. It is therefore strictly negative definite, uniformly
in `m`. Since `G` is bounded, the action is coercive downwards and
has exactly one critical point. Its equations are exactly
`Psi^m(q_0,p_0)=(q_0+n_q,p_0+n_p)`.
Two such points project to the same torus point precisely when their
winding labels differ by `(L^m-I)w`. Consequently (2.1) has exactly

$$
 |\det(L^m-I)|=\lambda^m+\lambda^{-m}-2<\lambda^m
 \tag{2.5}
$$

pointed periodic sectors. This proves the count needed for the
all-time error without invoking a separate structural-stability
theorem.

## 3. Uniform one-edge Gaussian reduction

Center the exact kernel (1.3) at the critical point of a sector, and
remove its constant and linear phase. The resulting centered edge
phase is denoted `Ftilde_x(z',z)`. The integer deck identity for `F`
and the corresponding identity for `B_h` make these centered kernels
a family on one fixed Hilbert space over the torus.

The Gaussian source uses the bounded complex deformation

$$
 z_s(y)=sy-i\psi(sy),\qquad s=\sqrt h,
$$

where `psi` is odd, equals its argument near zero, has derivative
between zero and one, and saturates inside the fixed analytic strip.
If `u=sy`, its exact coercive estimate is

$$
 \operatorname{Re}\frac{i\widetilde F_x(z_s(y'),z_s(y))}{s^2}
 \le -\frac{u'\psi(u')+u\psi(u)}{4s^2}.
 \tag{3.1}
$$

Near zero this is Gaussian in `y,y'`; outside the straight part it
gives genuine exponential tails. Thus the proof does not incorrectly
assert a global Gaussian bound on the saturated contour. At fixed
`m,h`, retain the damping from (2.2) during contour deformation.
The bounded imaginary displacement and Gaussian damping justify
the boundary limits; (3.1) then supplies an integrable majorant for
removing the damping. Centering makes the sum of all linear edge
terms cancel the sector boundary term exactly.

With `lambda_0=2 sqrt(pi)/sqrt(lambda)`, the transverse kernel is

$$
 K_h(x;y',y)=\lambda_0^{-1}
 B_h(Q+z_s(y'),q+z_s(y))\,
 \frac{1-i\psi'(sy)}{1-i}\,
 e^{i\widetilde F_x(z_s(y'),z_s(y))/s^2}.
$$

The outside constant on each edge is exactly
`C_h sqrt(h) (1-i) lambda_0=lambda^(-1/2)`. Consequently, if `x`
is the pointed period-`m` sector, its exact summand in (2.1) is

$$
 W_{m,N}(x)=\zeta_N^m\omega_{m,N}(x)\lambda^{-m/2}
       \operatorname{Tr}\!\left[
          K_h(\Psi^{m-1}x)\cdots K_h(x)\right],
 \quad
 \omega_{m,N}(x)=(-1)^{n_qn_p}e^{i\mathcal S_n/h}.
 \tag{3.2}
$$

The trace-class estimate is reduced to weighted kernel derivatives
using `A=1-d^2/dy^2+y^2` and
`||A^(-1)||_HS^2=pi^2/24`. Its model kernel is

$$
 K_G(y',y)=\lambda_0^{-1}
       e^{-3(y'^2+y^2)/4+y'y/2}.
$$

Its eigenvalues are `1,rho,rho^2,...`, with `rho=lambda^(-1)`.
The spatial perturbation and the saturated tails give one threshold
`h_0>0`, independent of any iterate, such that

$$
 \sup_x\|K_h(x)-K_G\|_1\le10^{-4},\qquad 0<h<h_0.
 \tag{3.3}
$$

The source's direct normalized right and left graph contractions
have Lipschitz constant below `.172`. They give

$$
 K_h(x)=\gamma_h(x)v_h(\Psi x)\ell_h(x)+\mathcal B_h(x),
 \qquad \ell_h(x)v_h(x)=1,
$$

with

$$
 |\gamma_h(x)-1|<.0002,\qquad
 \|\mathcal B_h(x)\|<.174,\qquad
 \|\mathcal B_h(x)\|_1<.209.
 \tag{3.4}
$$

The identities `B_h(x)v_h(x)=0` and
`ell_h(Psi x) B_h(x)=0` make every mixed rank-one/residual word
vanish exactly. Hence

$$
 \operatorname{Tr}\prod_{j=m-1}^{0}K_h(\Psi^j x)
       =\Gamma_h(x,m)+r_h(x,m),
 \quad \Gamma_h(x,m)=\prod_{j=0}^{m-1}\gamma_h(\Psi^j x),
 \tag{3.5}
$$

and

$$
 |r_h(x,m)|\le .209(.174)^{m-1}.
 \tag{3.6}
$$

This holds for every positive integer `m` after the single threshold
(3.3). Summing (3.6), using (2.5) and the outside factor in (3.2),
gives

$$
 |p_{m,N}-\mathcal P_{m,N}|
 \le\frac{.209}{.174}(.174\sqrt\lambda)^m
 <2(.421)^m.
 \tag{3.7}
$$

The proof of (3.7) uses no high-dimensional stationary-phase remainder.
The finite-sector equality is exact at each time, and its error estimate
comes solely from a uniform one-edge contraction.

For completeness, the modulus input used in Section 7 is also valid
uniformly in the period:

$$
 \lambda^{-m}|\Gamma_h(x,m)|^2
     =\Lambda(x,m)^{-1}e^{O(mh^2)}.
 \tag{3.8}
$$

Here `Lambda(x,m)>1` is the actual unstable multiplier. The source
derives (3.8) from a finite expansion through degree three in `s`,
with trace-norm remainder `O(s^4)`. Reflection makes `gamma_s` even;
the coefficients of the centered expansion have the form
`(1-i)^j` times real coefficients. Therefore the first `h` coefficient
of `gamma_h` is imaginary and
`log|gamma_h|^2=2log gamma_0+O(h^2)` pointwise. The exact Gaussian
determinant identity, followed by repeating a fixed orbit and taking
positive roots, gives `lambda^(-m) Gamma_0^2 Lambda(x,m)=1`.
The repetition step uses the residual contraction in (3.6). No
unproved differentiability in `h` of the full transverse operator is
needed.

## 4. The full primitive-sector weight and its relative error

Let `p` be a primitive orbit of least period `m`. Choose any one of
its points and a compatible lifted orbit. Define

$$
 \begin{split}
 u_{p,N}&=\zeta_N^m\omega_{p,N}\lambda^{-m/2}\Gamma_h(p,m),\\
 \widetilde u_{p,N}
   &=\zeta_N^m\omega_{p,N}\lambda^{-m/2}
        \operatorname{Tr}\prod_{j=m-1}^{0}K_h(\Psi^j x).
 \end{split}
 \tag{4.1}
$$

The second line, not the first, is the exact contribution of one
point of `p` to `p_{m,N}`. By (3.4),

$$
 |\Gamma_h(p,m)|\ge .9998^m>0.
$$

Equations (3.5)--(3.6) therefore prove the uniform relative bound

$$
 \boxed{
 \left|\frac{\widetilde u_{p,N}}{u_{p,N}}-1\right|
 \le C_0 q_0^m,\qquad
 C_0=\frac{.209}{.174}<1.202,\qquad
 q_0=\frac{.174}{.9998}<.175.}
 \tag{4.2}
$$

This estimate is simultaneous over all primitive orbits and all times
after the single sufficiently-large-`N` threshold.

For repeated orbits one must retain a distinction. If `C_p` is a
full transverse cycle operator, the sector associated with `r`
repetitions contains `Tr(C_p^r)`, not `(Tr C_p)^r`. Thus the full
weights in (4.1) are not asserted to be multiplicative under
repetition. Principal weights are multiplicative, since their
transverse factor is the scalar cocycle `Gamma_h`. The selected
family below has primitive period exactly `m`, so this distinction
introduces no ambiguity there.

## 5. Odd deck signs, cyclic points, and the factor `2m^2`

For `w=(b,d)` and `Lw=(a,c)`, the exact deck identity is

$$
 F(Q+a,q+b)-F(Q,q)=cQ-dq+(ca-db)/2.
 \tag{5.1}
$$

Changing the initial lift by `w` changes the winding to
`n'=n+(L^m-I)w`. Write `L^j w=(a_j,b_j)`. Direct telescoping of
(5.1), including the boundary term in (2.4), gives

$$
 2\Delta\mathcal S
 =n_q(b_m+b_0)-n_p(a_m+a_0)+b_0a_m-b_ma_0.
 \tag{5.2}
$$

Since `L=I mod 2`, the right side is even, and `n'=n mod 2`.
Thus both the exponential action and the character in (3.2) are
unchanged. The centered transverse kernels are also unchanged by
the same deck transformation.

Beginning the orbit at its next point changes the winding to `Ln`.
The new edge sum differs from the old one by

$$
 (Ln)_p q_1-n_pq_0+
       ((Ln)_p(Ln)_q-n_pn_q)/2.
$$

The boundary action changes by exactly the negative of this expression.
The character is again unchanged. Finally the transverse product is
cyclically permuted, and the trace of these trace-class products is
cyclic. Both weights in (4.1) are consequently independent of the
chosen one of the `m` starting points.

Equivalently, the odd half-winding cancellation is exactly

$$
 (-1)^{n_qn_p}e^{-in_pn_q/(2h)}=1,
$$

so the phase is the Landau holonomy
`exp[i(sum F-n_p q_0)/h]`. This agrees with the cell action convention
in the signed-profile source. The scalar `zeta_N^m` in (4.1) is
common to all period-`m` terms and cancels against its conjugate in
each double-sum term.

Since the sector identity (2.1) is a sum over pointed fixed points,
each unordered pair of distinct primitive period-`m` orbits contributes
exactly

$$
 2m^2\operatorname{Re}
        (\widetilde u_{p,N}\overline{\widetilde u_{p',N}})
 \tag{5.3}
$$

to its squared modulus: `m^2` choices of points, and the two ordered
directions. There is no additional factor coming from code rotations
or winding cosets.

## 6. The selected family is a genuine, nonduplicated set of pairs

Fix the interior loop `0` and the distinct loop `a` at its vertex
in the twelve-edge coding, as in the signed-profile source. Let
`Lambda>5` be the multiplier of the actual fixed point coded by
`0^infinity`. Fix `R_0>=0`, and set

$$
 R=\left\lceil\frac{\log N}{2\log\Lambda}\right\rceil+R_0,
 \qquad k=2R,\quad \varepsilon=\Lambda^{-2R},\quad x_N=N\varepsilon.
 \tag{6.1}
$$

For `N<=m<=3N/2`, choose integer lengths

$$
 m/8\le\ell_1\le m/6,\qquad
 m/4\le\ell_2\le m/3,\qquad
 \ell_3=m-6R-6-\ell_1-\ell_2.
 \tag{6.2}
$$

For all sufficiently large `N`, the three length bands are disjoint
and `min ell_j>=m/9`. Let `u_j` be an admissible length-`ell_j`
interior word at the specified vertex, avoiding `0^k`, and form
the cells `e_j=0^R a u_j a0^R`. The two cyclic words are
`e_1 e_2 e_3` and `e_1 e_3 e_2`.

Here is the needed coding check. The source uses the Berg partition
for `S=L^(-1)` in coordinates
`B(q,p)=(q-sqrt(2)p,q+sqrt(2)p)`. The lattice basis is
`(1,1),(-sqrt(2),sqrt(2))`, and both eigenvalues of `B S B^(-1)`
are positive. Siemaszko--Wojtkowski, *Counting Berg partitions*,
Nonlinearity **24** (2011), 2383--2403, Section 2 and Theorems
4.1--4.2, therefore give the two rectangular tiles with sides
`(sqrt(2),1)` and `(1,sqrt(2))`, after placing a spine intersection
at the origin. The incidence matrix is `S^T=[[3,2],[4,3]]`.
The theorem statements, their positive-eigenvalue case, and the
lattice convention were reopened in the primary full text
<https://arxiv.org/pdf/1007.3984>, preprint pp. 2--3 and 8--11.

The rest of the uniqueness argument is direct. Full strip crossings
give a coding by the separate edges. A centered cylinder of depth
`n` is a closed rectangle with sides bounded by
`sqrt(2) lambda^(-n)`, so it specifies one point. Generic points
have unique codes. Every fiber has at most four codes: each nested
cylinder at a point contains at least one of its four coordinate
quadrant germs; one germ persists at all depths, and distinct codes
cannot share a persistent germ because their cylinder interiors
are disjoint. The partition spines lie on stable or unstable leaves
of the origin. A periodic point on either such leaf must be the
origin, since its finite orbit cannot converge to a different orbit.
These statements transfer through the explicitly established
equivariant conjugacy to the actual map, with time orientation
reversed.

Each of the two constructed cyclic words has exactly three zero
runs of length at least `k`. All three have length exactly `k` and
are bracketed by `a`. If a word were a proper power, its repetition
number would divide three, hence would be three; its three gaps
would then have equal lengths. This contradicts (6.2). The code is
therefore primitive of length `m`. For `m>4` it cannot code the
origin, whose fiber has at most four elements. Every other periodic
point has unique itinerary. The two codes thus give primitive
geometric orbits of least period exactly `m`.

The orbits are different: starting immediately before the short
interior, one order is short--medium--long and the other is
short--long--medium. They cannot agree by a cyclic rotation.
There is also no duplicate unordered pair. In either member, the
unique long zero marker preceding the short interior fixes the
cut at its middle. The three interiors and their lengths can then
be recovered, and the member whose next gap is medium fixes the
orientation. Thus different triples of interiors or lengths cannot
produce the same unordered pair.

Denote this set of unordered pairs by `A_(m,N)`. It is precisely
the family used for the signed principal profile. Together with
all its pointed representatives in the two ordered directions,
it is a literal subset of the exact finite double sum obtained
by squaring (2.1).

## 7. Independent bound for the selected absolute mass

We prove

$$
 \boxed{\quad
 \mathscr A_{m,N}:=\sum_{\{p,p'\}\in\mathcal A_{m,N}}
                       2m^2|u_{p,N}u_{p',N}|
       \le C N,
 \quad N\le m\le3N/2.\quad}
 \tag{7.1}
$$

This bound does not use cancellation, the oscillatory profile, or
the localized comparison of the two scalar cocycles.

Use the actual positive transfer operator `T`, the zero branch `J`,
and the fixed nonzero branch `A=J_a` from the signed-profile source.
Their direct transfer and zero-branch proofs give constants,
independent of every word length, such that

$$
 \sup_{\ell\ge0}\|T^\ell\|\le C_T,
 \qquad \|J^j\|\le C_J\Lambda^{-j}.
 \tag{7.2}
$$

All operators preserve nonnegative functions. Let `G_(k,ell)` be
the sum of branches of words avoiding `0^k`. For fixed lengths
the open positive weight of all good `123` words is exactly

$$
 [J^R A G_{k,\ell_3} A J^{2R}
       A G_{k,\ell_2} A J^{2R}
       A G_{k,\ell_1} A J^R1](o),\qquad o=0^\infty.
 \tag{7.3}
$$

On nonnegative functions each `G_(k,ell)` is pointwise bounded
by `T^ell`. Replacing the three factors in (7.3) therefore
increases its value. Applying (7.2) to the unrestricted expression
gives

$$
 \text{open positive sum}\le C\Lambda^{-6R}
                               =C\varepsilon^3.
 \tag{7.4}
$$

This argument does not assume that a pointwise inequality bounds
Hölder operator norms: it first compares the final positive
quantities, and only then uses the operator norms of the
unrestricted factors.

The same bound applies to the actual periodic multiplier weights.
Indeed the one-sided geometric potential has variations at most
`C theta^j`, for fixed `theta<1`. For

$$
 w=0^R a u_1 a0^{2R}a u_2 a0^{2R}a u_3 a0^R,
$$

the two continuations `w0^infinity` and `w^infinity` agree for at
least `m+R` edges. Summing the variations along their first `m`
shifts bounds the logarithm of their weight ratio by

$$
 C\sum_{j=0}^{m-1}\theta^{m+R-j}
       \le\frac{C\theta^{R+1}}{1-\theta}.
 \tag{7.5}
$$

Periodic cohomology makes the periodic weight exactly
`Lambda_p^(-1)`. Equations (7.4)--(7.5) imply

$$
 \sum_{u_1,u_2,u_3}\Lambda_{p(123)}^{-1}
       \le C\varepsilon^3,
 \qquad
 \sum_{u_1,u_2,u_3}\Lambda_{p(132)}^{-1}
       \le C\varepsilon^3.
 \tag{7.6}
$$

For the second inequality simply interchange the positions of
the second and third transfer blocks; (7.2) is unchanged.

The modulus formula (3.8) and Cauchy--Schwarz now give, for these
fixed lengths,

$$
 \begin{split}
 \sum_{u_1,u_2,u_3}|u_{p(123),N}u_{p(132),N}|
 &\le e^{Cmh^2}
       \Big(\sum\Lambda_{p(123)}^{-1}\Big)^{1/2}
       \Big(\sum\Lambda_{p(132)}^{-1}\Big)^{1/2}\\
 &\le C\varepsilon^3.
 \end{split}
 \tag{7.7}
$$

Here `mh^2=O(N^(-1))` uniformly in the stated time range. The
number of allowed length pairs in (6.2) is
`m^2/288+O(m)`, and in particular `O(m^2)`. After the exact
pointed factor `2m^2`, (7.7) is at most `C m^4 epsilon^3`.
Since `m=O(N)` and `epsilon=O(N^(-1))`, this proves (7.1).

## 8. The bridge to the original double sum

Define separately

$$
 \begin{split}
 E^{\rm principal}_{m,N}
 &=\sum_{\{p,p'\}\in\mathcal A_{m,N}}
        2m^2\operatorname{Re}(u_{p,N}\overline{u_{p',N}}),\\
 E^{\rm original}_{m,N}
 &=\sum_{\{p,p'\}\in\mathcal A_{m,N}}
        2m^2\operatorname{Re}
                  (\widetilde u_{p,N}\overline{\widetilde u_{p',N}}).
 \end{split}
 \tag{8.1}
$$

The second line is an exact subsum of `|Tr U_N^m|^2`, by Sections
5--6. Write `tilde u_p=u_p(1+e_p)`, with `|e_p|<=C_0 q_0^m`
from (4.2). For each pair,

$$
 |(1+e_p)(1+\overline{e_{p'}})-1|
       \le 2C_0q_0^m+C_0^2q_0^{2m}.
$$

Multiplying by the absolute weights and using (7.1) proves

$$
 \boxed{\quad
 |E^{\rm original}_{m,N}-E^{\rm principal}_{m,N}|
 \le C N q_0^m=o(N),\qquad
 q_0<.175,\quad N\le m\le3N/2,
 \quad}
 \tag{8.2}
$$

uniformly along all odd `N`. In particular, for any fixed bounded
weight `w` on `[1,3/2]`,

$$
 \left|\frac1{N^2}\sum_{N\le m\le3N/2}w(m/N)
       (E^{\rm original}_{m,N}-E^{\rm principal}_{m,N})\right|
       \le C\|w\|_\infty q_0^N.
 \tag{8.3}
$$

The full signed principal profile in the frozen source may therefore
be restated for `E_original`, with the same uniform `o(N)` error.
In particular its sine-compression formulation becomes

$$
 E^{\rm original}_{m,N}
 =\frac{m^4}{144N^3}
       e^{-\kappa_{\rm esc}m\varepsilon}
       \operatorname{Tr}(S_{cN\varepsilon}^{\,3})+o(N).
 \tag{8.4}
$$

Here the actual geometric constants and the sine-compression
operator are exactly those specified in the signed-profile and
endpoint-law proofs. Equation (8.4) adds no new probabilistic
assumption or classical-to-quantum approximation. It is the same
profile, transferred to the full sector amplitudes by (8.2).

## 9. What this audit establishes, and the remaining limit

The reread found no failure of the exact-amplitude construction,
the coherent-sector identity, the bounded contour deformation,
the rank-one contraction, or the stated all-time error constant.
The essential ordering of arguments is: exact finite-iterate
identities first, one-edge uniform estimates second. Constants
that grow with the iterate in the exact word identity do not enter
the residual bound.

The previously implicit step repaired here is the transfer of a
selected principal double sum to the exact double sum. The repair
uses (4.2) and (7.1), not merely (3.7). The exact deck and cyclic
checks preserve the factor `2m^2`; primitiveness and absence of
duplicate geometric pairs are established independently of any
oscillatory estimate.

No estimate for the complementary pairs follows. A positive
order-`N` subsum can be offset by its signed complement. Thus even
for the explicit test `b_*` in the consolidated report, the full
quantity

$$
 \frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
       \bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)
$$

remains unevaluated. The bridge is an exact connection of the
proved selected profile to the original spectrum; it does not
supply the missing cancellation of all remaining orbit pairs or
any higher-order `H_diag` estimate.
