> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_iterated_all_oldspaces.md`. Embedded SHA256: `853aeae71f699d0af37aa071202112603eb518a0e8614a65ca1f91246d2bd5b8`.
> [Thematic guide](../../topics/arithmetic.md).

# Collective arithmetic oldspaces along every odd dimension

## Scope and inputs

This note proves quantitative statements for the original fixed
`tau=10^-80`, along **all odd dimensions**, concerning all canonical
oldspaces at once. The conclusions concern eigenvector mass and do not
evaluate the spectral statistics in `H_diag`.

The frozen input `arithmetic_iterated_effective_horizon.md` has SHA-256
`9739e62cc9a4282d39b379c50835f05fd3d46d664663cf6032b3337857751768`.
Its full proof and published-theorem application have been independently
audited. The earlier exact oldspace identities are in the frozen
`arithmetic_oldspace_escape.md`, SHA-256
`596d44605310cc898fa75e23df4aa811189a1764fed21ce8b9f5d07ae734813a`.

Use the effective input's notation

$$
\Lambda_N=\log\log N,\quad
T_N=\left\lfloor\frac{\log(\Lambda_N/32000)}{\log256}\right\rfloor,
\quad R_N=T_N+1,
$$

and

$$
\varepsilon_N=
\sqrt{16\pi e^5}e^{-\sqrt{\log N}/768}
+C_*(\log\log N)^{11}N^{-7/8}.
$$

The notation `R_N` here denotes an integer cutoff, not the remainder
`mathcal R_N` of the input note; that remainder is denoted `epsilon_N` here.
All assertions below hold for sufficiently large odd `N`, with the explicit
universal condition `Lambda_N>=8192000` sufficient for their applications
of the input theorem.

## 1. The exact lattice of oldspaces

For each odd `d>=3` such that `d^2` divides `N`, let `P_{d,N}` be the
orthogonal projector onto

$$
\mathcal H_{d,N}=
\{\psi:\psi(x)=0\text{ if }d\nmid x,
\quad\psi(x+N/d)=\psi(x)\}.
$$

It has rank `N/d^2` and is the canonical oldspace in the input notes.
If `d^2,e^2` divide `N`, then

$$
\boxed{P_{d,N}P_{e,N}=P_{\operatorname{lcm}(d,e),N}.}     \tag{1.1}
$$

To verify this, first note that the two finite Weyl groups defining the
projectors commute. Their symplectic products are multiples of
`N^2/(de)`, which is divisible by `N`, since `de` divides `N`.
Thus the product of their projectors is the orthogonal projector onto
the intersection. In that intersection the support is contained in the
multiples of `lcm(d,e)`, and the two shift invariances generate the shift
by `gcd(N/d,N/e)=N/lcm(d,e)`. These are exactly the defining conditions
for the oldspace on the right side of (1.1).

Let

$$
\mathcal H_{{\rm old},N}
=\sum_{d\ge3,\ d^2\mid N}\mathcal H_{d,N},
\qquad P_{{\rm old},N}\text{ its orthogonal projector}.
$$

Every composite-index oldspace is contained in the oldspace of each of
its prime divisors. Hence (1.1) gives the exact finite formulas

$$
P_{{\rm old},N}=I-\prod_{p^2\mid N}(I-P_{p,N}),
\qquad
c_N:=\frac{\operatorname{rank}P_{{\rm old},N}}N
=1-\prod_{p^2\mid N}(1-p^{-2}).                         \tag{1.2}
$$

Here and below all primes are odd because `N` is odd. The empty product
is one, so the old projection is zero for square-free `N`.
The rank identity follows by expanding the finite product and using
`rank P_d=N/d^2`. In particular

$$
0\le c_N\le\sum_{p\ge3}p^{-2}
\le\sum_{n\ge1}(2n+1)^{-2}<\frac14.                    \tag{1.3}
$$

For the last inequality, use
`(2n+1)^2>4n(n+1)` and the telescoping sum
`sum 1/(n(n+1))=1`.

## 2. Uniform validity for the divisors used below

The effective trace theorem has divisor-dependent conditions

$$
\Lambda_N\ge4\log D_d,\qquad
\log N\ge192\log(\sqrt2/m_d),
$$

where `m_d=tau/(1000d)` and
`D_d=2(ceil(log(4/m_d))+2)`.
These conditions hold uniformly not only for `d<=R_N`, but also for

$$
d\le R_N^{R_N}.                                        \tag{2.1}
$$

Indeed

$$
\log(4/m_d)<193+\log d,\quad
D_d\le392+2\log d.
$$

For `Lambda_N>=8192000`, the definition of `R_N` implies
`R_N<=sqrt(Lambda_N)` and `log R_N<=sqrt(Lambda_N)/2`.
One direct check is
`R_N<=1+log(Lambda_N)/log256`, followed by the monotonic comparison
with `sqrt(Lambda_N)` on this range. Therefore

$$
\log d\le R_N\log R_N\le\Lambda_N/2,
\qquad D_d\le392+\Lambda_N\le2\Lambda_N.
$$

The elementary inequality `4 log(2 Lambda_N)<=Lambda_N` proves the
first divisor condition. The second follows from

$$
192\log(\sqrt2/m_d)
<192(192+\log d)
\le192(192+\Lambda_N/2)<e^{\Lambda_N}=\log N.
$$

All inequalities in this paragraph hold on the displayed universal range;
for example the last one already follows there from
`e^x>=x^2/2`. Thus no fixed-divisor limit is used when the divisor below
depends on `N`.

## 3. Quantum ergodicity of the entire old projection

Let `E_{U_N}` be the full commutant projection. Then

$$
\boxed{\frac1N
\|\mathcal E_{U_N}(P_{{\rm old},N})-c_NI\|_{\rm HS}^2
\le\frac{5}{2R_N}+2\,4^{R_N}\varepsilon_N.}             \tag{3.1}
$$

This is `O(1/log log log N)` along every odd `N`, with no fixed-divisor
restriction. It is valid in the presence of repeated eigenvalues.

To prove it, let `Q_N` be the version of (1.2) using only primes
`p<=R_N`, and put `q_N=rank Q_N/N`. If there are no such primes then
`Q_N=0`. Otherwise let `d_0` be their product. The divisor `d_0` satisfies
`d_0^2|N` and `d_0<=R_N^{R_N}`, so Section 2 applies to its finite Weyl
group.

Expand `Q_N` by inclusion--exclusion. If there are `s` relevant primes,
it is a signed sum of `2^s-1` canonical projectors. Each such projector
is an average of a subgroup of the Weyl group for `d_0`, with coefficient
one-norm equal to one. Thus the coefficient one-norm of `Q_N` in that
group is at most `2^s-1`. Its identity coefficient equals `q_N`, because
all nonidentity group elements have trace zero. Consequently
`B_N=Q_N-q_NI` has zero identity coefficient and coefficient one-norm
less than `2^s<=2^{R_N}`.

The uniform trace bound in the effective theorem, applied to every pair
of these Weyl elements, gives

$$
\left|N^{-1}\operatorname{Tr}(B_NU_N^{-r}B_NU_N^r)\right|
\le4^{R_N}\varepsilon_N,
\qquad 1\le|r|\le T_N.
$$

The zero-lag value is `q_N-q_N^2<=1/4`. Averaging over `R_N=T_N+1`
times and projecting onto the commutant as in the effective theorem
therefore proves

$$
\frac1N\|\mathcal E_{U_N}(Q_N)-q_NI\|_{\rm HS}^2
\le\frac1{4R_N}+4^{R_N}\varepsilon_N.                  \tag{3.2}
$$

Now `D_N=P_old,N-Q_N` is an orthogonal projector, by (1.1). Its rank
fraction `delta_N=c_N-q_N` is bounded by

$$
\delta_N\le\sum_{p>R_N,\ p^2\mid N}p^{-2}
\le\sum_{n>R_N}n^{-2}\le1/R_N.
$$

Commutant projection is an orthogonal contraction, so

$$
N^{-1}\|\mathcal E_{U_N}(D_N)-\delta_NI\|_{\rm HS}^2
\le\delta_N-\delta_N^2\le1/R_N.
$$

Combine this with (3.2) using `||A+B||^2<=2||A||^2+2||B||^2`.
This gives (3.1). Finally,

$$
4^{R_N}=4\,(256^{T_N})^{1/4}
\le(\Lambda_N/125)^{1/4},
$$

so the remainder in (3.1) tends to zero faster than `1/R_N`.

For every orthonormal eigenbasis, even one chosen differently inside
degenerate eigenspaces, (3.1) implies

$$
\frac1N\sum_j
\left|\|P_{{\rm old},N}\psi_{j,N}\|^2-c_N\right|^2
\le\frac{5}{2R_N}+2\,4^{R_N}\varepsilon_N.               \tag{3.3}
$$

In particular, for any fixed `eta>1/4`, the proportion of eigenvectors
whose mass in the entire old subspace is at least `eta` tends to zero
with this rate, divided by `(eta-1/4)^2`.

## 4. A sharper threshold for concentration in any individual oldspace

For any fixed `eta>1/9`, uniformly over all orthonormal eigenbases,

$$
\boxed{\frac1N\#\{j:\exists d\ge3,\ d^2\mid N,
\ \|P_{d,N}\psi_{j,N}\|^2\ge\eta\}
\le\frac{\frac1{2(\eta-1/9)^2}+\frac1\eta}{R_N}
+\frac{R_N\varepsilon_N}{(\eta-1/9)^2}.}                \tag{4.1}
$$

For `d<=R_N`, apply the effective variance theorem, justified uniformly
by Section 2. The centered mean is `d^(-2)<=1/9`, so Chebyshev's inequality
bounds the fraction for this `d` by

$$
\frac{d^{-2}/R_N+\varepsilon_N}{(\eta-1/9)^2}.
$$

Sum these bounds, using `sum_{d>=3}d^(-2)<=1/2` and at most `R_N`
eligible small divisors. For `d>R_N` use only the exact trace identity

$$
\sum_j\|P_{d,N}\psi_{j,N}\|^2=N/d^2.
$$

The fraction with mass at least `eta` for any such divisor is at most
`eta^(-1)sum_{d>R_N}d^(-2)<=1/(eta R_N)`. Adding the two union bounds
proves (4.1).

No independence of different oldspaces or eigenvectors is used in either
(3.1) or (4.1). Their overlaps are handled by the exact projector lattice
or by a union bound, respectively.

## 5. Limitation

These are actual asymptotic results for the stated family at every odd
dimension. They exclude concentration of a positive fraction of its
eigenvectors in the old decomposition inherited from the unperturbed cat
matrices. They do not exclude arbitrary arithmetic correlations of the
eigenphases, do not bound every principal angle, and do not prove the
order-`N` trace cancellations required by `H_diag`.
