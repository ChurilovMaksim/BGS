> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_pseudoorbit_cutoff.md`. Embedded SHA256: `34aa4bff0c8b67e5f09fbf6b923b3c18259278c9f5c109f7b82077e6de0b6021`.
> [Thematic guide](../../topics/histories.md).


# Fermionic pseudo-orbit cancellation at the dimension threshold

## Scope and status

This is a continuation for the exact matrices in the question, with the fixed
parameter `tau=10^-80` and all sufficiently large odd dimensions. No average in
dimension, kick strength, or orbit phases is taken. The results below concern
coefficients of the exact dynamical determinant and their geometrically defined
diagonal contributions. They do **not** prove `H_diag` or its negation.

The new calculations are:

1. exact multiplicativity of the full lattice/action phase under orbit
   repetition, including its odd-dimensional character;
2. a quantitative cancellation bound for the complete pseudo-orbit coefficient
   at degree `N+s`, valid for `s>=N^(1/50)`;
3. the full positive diagonal of that coefficient, at degrees of order `N`, with
   an explicit constant within relative logarithmic error `10^-51` of
   `7 sqrt(2)/16`;
4. consequently, a complete signed different-pseudo-orbit cancellation of that
   positive constant beyond the dimension threshold;
5. the corresponding diagonal calculation for reciprocal coefficients, followed
   by an explicit account of the step at which a mixed determinant-ratio
   argument fails.

The threshold cancellation is an actual estimate of a full alternating sum of
products of orbit amplitudes. It is not a distinguishing criterion for CUE: a
unitary clock countermodel can have an even sharper cutoff. The original
power-trace pair estimate remains unproved. No claim of priority over the general
pseudo-orbit literature is made.

## Input provenance

The directory of the checked inputs is
`/workspace/scratch/e111873eea6c/research_continuation_2026_10_20/`.

| Input | SHA-256 |
|---|---|
| `manifest.json` | `0e09ed285ffff620b2e1e5de83a148cae01de354f1deed7f5c81216aa2a61550` |
| `exact_dynamical_determinant.md` | `e75d4e7477246e189ba56f0b6bbbda4d806ad1e8bb114e1f4b7d07613b8f0035` |
| `gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` |
| `odd_trace_and_algebraic_rigidity.md` | `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b` |
| `exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` |
| `classical_trace_and_pair_diagonal.md` | `355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c` |
| `selfinverse_countermechanism.md` | `5eaa20f8d1c3621ac69c526db33ba41eed761cbbbd637a8ed77a12bcdedeaf42` |

We use the actual proved statements in those inputs: the exact action/deck law,
the all-time trace identity, the scalar cocycle modulus estimate, and the
explicit trace-class classical operator. In particular, no universality theorem
is imported.

Write

$$
\lambda=3+2\sqrt2,\quad \rho=\lambda^{-1},\quad
h=(2\pi N)^{-1},\quad q_*=0.421,\quad
a=\sqrt\lambda\,1.0002.
$$

The inputs establish, at one sufficiently large odd-dimensional threshold and
for every positive integer `m`,

$$
p_{m,N}=\mathcal P_{m,N}+E_{m,N},\quad
|E_{m,N}|\le2q_*^m,\quad |\mathcal P_{m,N}|\le a^m,
\tag{1}
$$

$$
\mathcal Z_N(z)=\exp\left(-\sum_{m\ge1}\frac{\mathcal P_{m,N}}m z^m\right)
=D_N(z)e^{G_N(z)},\quad D_N(z)=\det(I-zU_N),
\tag{2}
$$

where `G_N(z)=sum E_{m,N}z^m/m` is holomorphic in `|z|<q_*^-1` and

$$
|e^{G_N(z)}|\le(1-q_*|z|)^{-2}.
\tag{3}
$$

The classical map is the fixed map

$$
\Psi=\phi_a^{-\tau/(2\pi)}\circ L,\qquad
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix}.
$$

Here the use of `a` for the numerical growth constant in (1) is separate from
the classical symbol denoted `a(q,p)` in the input files; no symbol is changed.

For a periodic point let `Lambda_m` denote its positive unstable multiplier. The
classical inputs give

$$
\#\operatorname{Fix}\Psi^m=\lambda^m+\lambda^{-m}-2<\lambda^m,
\qquad \Lambda_m\ge5^m,
\tag{4}
$$

$$
Q_m:=\sum_{\operatorname{Fix}\Psi^m}
\frac{\Lambda_m^{-1}}{(1-\Lambda_m^{-1})^2}
=1+O(\vartheta^m),\quad \vartheta=1-1/8000.
\tag{5}
$$

## 1. Repetition of the full phase

Let a primitive closed torus orbit have period `d`. Choose a lifted initial
point `z_0`, with `Psi^d z_0=z_0+n`, `n=(n_q,n_p)` integral. Its exact phase is

$$
\omega_d=(-1)^{n_qn_p}\exp(2\pi iN\mathcal S_n),
\tag{6}
$$

where, writing the lifted positions as `q_j`,

$$
\mathcal S_n=\sum_{j=0}^{d-1}F(q_{j+1},q_j)
-n_p(q_0+n_q/2).
$$

The deck law is

$$
F(Q+a',q+b')-F(Q,q)=c'Q-d'q+(c'a'-d'b')/2,
\quad L(b',d')=(a',c').
\tag{7}
$$

We verify the repetition sign explicitly. Suppose the first `r` blocks have
winding `w`, and put `v=L^d w`. The next shifted block has total new winding
`n+v`. Telescoping (7) along this block, followed by subtracting its new boundary
term, gives

$$
\mathcal S_{r+1}=\mathcal S_r+\mathcal S_1+
\frac{n_qv_p-n_pv_q}{2}.
\tag{8}
$$

For clarity, if `w=(b,c)` and `v=(b',c')`, the change in the uncorrected edge sum
is `c' q_d-c q_0+(c'b'-cb)/2`. Inserting `q_d=q_0+n_q` and the three boundary
terms yields exactly (8).

Let `chi(u)=(-1)^(u_q u_p)` and `sigma(u,v)=u_qv_p-u_pv_q`. For integral vectors,

$$
\chi(n+v)=\chi(n)\chi(v)(-1)^{\sigma(n,v)}.
$$

Since `L=I mod 2`, `chi(v)=chi(w)`. The action correction in (8) contributes
`(-1)^(N sigma(n,v))`. Because `N` is odd, these two signs cancel. Consequently

$$
\omega_{rd}=\omega_d^r.
\tag{9}
$$

The scalar `zeta_N^m`, with `zeta_N=e_8(3N-1)`, plainly obeys the same
multiplication rule. The product of the scalar cocycle over a repeated cycle is
the corresponding power. The full primitive weight is therefore

$$
u_{p,N}:=\zeta_N^{d_p}\omega_{d_p,N}(p)\lambda^{-d_p/2}
\prod_{j=0}^{d_p-1}\gamma_h(\Psi^j p).
\tag{10}
$$

The input cyclic-invariance proof makes (10) independent of the chosen point on
the primitive orbit. Equation (9) gives the exact identity

$$
\mathcal P_{m,N}=
\sum_{p:\,d_p\mid m}d_p\,u_{p,N}^{m/d_p}.
\tag{11}
$$

All sums at a fixed length are finite by (4). Substituting (11) in (2) proves,
first in the common absolute-convergence disk and hence coefficientwise,

$$
\boxed{\quad \mathcal Z_N(z)=\prod_{p\ {
m primitive}}
(1-u_{p,N}z^{d_p}).\quad}
\tag{12}
$$

No arbitrary independent phase variables have been introduced in (12).

## 2. Complete pseudo-orbit coefficients and their cutoff

Write `c_{n,N}=[z^n]Z_N(z)`. A finite set `S` of distinct primitive orbits has
length `ell(S)=sum_(p in S)d_p` and weight

$$
U_N(S)=(-1)^{|S|}\prod_{p\in S}u_{p,N}.
$$

Thus

$$
c_{n,N}=\sum_{S:\,\ell(S)=n}U_N(S).
\tag{13}
$$

This is a finite alternating sum, with no unresolved convergence of the product.

### 2.1 A radial estimate using the actual all-time trace bound

Unitarity and (1) give

$$
|p_{m,N}|\le3\min(N,a^m).
\tag{14}
$$

Fix `1<R<q_*^-1`; in this entire interval `R<a`. Put

$$
\kappa_R=1-\frac{\log R}{\log a}>0.
$$

We claim

$$
S_N(R):=\sum_{m\ge1}\frac{|p_{m,N}|}{mR^m}
\le C_R\frac{N^{\kappa_R}}{\log N}
\tag{15}
$$

for all sufficiently large `N`. Let `J=floor(log N/log a)`. The part `m>J` is
at most

$$
\frac{3NR^{-J}}{(R-1)(J+1)}.
$$

For `m<=J`, write `beta=a/R>1`. Splitting at `J/2` shows

$$
\sum_{m\le J}\frac{\beta^m}{m}
\le C_\beta\frac{\beta^J}{J}.
$$

Indeed, the upper half is bounded by a geometric sum times `2/J`; the lower
half is bounded by `beta^(J/2+1)/(beta-1)`, and
`J beta^(-J/2)` is bounded. Finally `beta^J<=N^kappa_R` and
`N R^-J<=R N^kappa_R`. This proves (15).

All zeros of `D_N` have modulus one. Its exterior product expansion gives

$$
\log |D_N(Re^{it})|=N\log R-
\operatorname{Re}\sum_{m\ge1}\frac{\overline{p_{m,N}}e^{-imt}}{mR^m},
$$

up to replacing `t` by its negative, which does not affect the bound. In
particular

$$
R^N e^{-S_N(R)}\le |D_N(Re^{it})|\le R^N e^{S_N(R)}.
\tag{16}
$$

The upper bound in (16), (3), and Cauchy's coefficient formula yield

$$
\boxed{
|c_{N+s,N}|\le(1-q_*R)^{-2}R^{-s}
\exp\left(C_R\frac{N^{\kappa_R}}{\log N}\right),\qquad s\ge0.
}
\tag{17}
$$

This is considerably stronger than using `|D_N(z)|<=(1+|z|)^N` in the
determinant convolution. It uses the actual exponential orbit bound in (1).

Choose `R=19/8`. Then `q_*R=7999/8000<1` and `kappa_R<1/50`. The latter strict
inequality can be checked without floating-point logarithms: `a<483/200` and

$$
(19/8)^{50}>(483/200)^{49}.
\tag{18}
$$

The rational inequality (18) is equivalently the exact integer comparison
`19^50 200^49 > 483^49 8^50`. Also `a<483/200` follows from
`sqrt(2)<1.4143`. Thus there are constants `c>0,N_0` such that

$$
\boxed{\quad |c_{N+s,N}|\le e^{-cs},
\qquad s\ge N^{1/50},\quad N\ge N_0\text{ odd}.\quad}
\tag{19}
$$

One can take any `c<log(19/8)` after increasing `N_0`; `c=log(19/8)/2`
suffices. The result holds for every integer `s` in this range, without an
upper bound on `s`.

### 2.2 A separate sharper comparison of squared traces

For every uniformly bounded weight `w_m`, (1) and (14) imply

$$
\left|N^{-2}\sum_{m\ge1}w_m
\bigl(|p_{m,N}|^2-|\mathcal P_{m,N}|^2\bigr)\right|
\le C\sup_m|w_m|\,N^{-2+\kappa_*},
\tag{20}
$$

where `kappa_*=1+log q_*/log a<1/50`. Indeed the absolute difference of the
squares is at most `4q_*^m |p_m|+4q_*^(2m)`. Split
`sum q_*^m min(N,a^m)` at `floor(log_a N)`: the two geometric sums are both
`O(N^kappa_*)`. The rational check

$$
(483/200)^{49}(421/1000)^{50}<1
$$

proves `kappa_*<1/50`. This improves the earlier `O(N^-1)` replacement bound,
but does not estimate the different-orbit contribution itself.

## 3. Full geometric diagonal of the fermionic coefficients

Define the positive diagonal

$$
F_{n,N}:=\sum_{S:\,\ell(S)=n}|U_N(S)|^2
=[t^n]\prod_p(1+|u_{p,N}|^2t^{d_p}).
\tag{21}
$$

This includes **all** finite subsets of primitive orbits of total length `n`.
It is not merely the single-period diagonal in `|p_m|^2`.

For the primitive multiplier `Lambda_p`, the input scalar-cocycle estimate is

$$
|u_{p,N}|^2=\Lambda_p^{-1}e^{\xi_{p,N}},
\qquad |\xi_{p,N}|\le C d_p h^2.
\tag{22}
$$

Introduce the two fixed-map sums

$$
A_m:=\sum_{\operatorname{Fix}\Psi^m}\Lambda_m^{-1},\qquad
B_m:=\sum_{\operatorname{Fix}\Psi^m}\Lambda_m^{-2}.
\tag{23}
$$

From (4)-(5),

$$
A_m=1+O(\vartheta^m),\qquad 0\le B_m\le5^{-m}A_m=O(5^{-m}).
\tag{24}
$$

To check the first statement, put `x=Lambda_m^-1<=5^-m`. For `0<=x<=1/5`,
`0<=x/(1-x)^2-x<=C 5^-m x/(1-x)^2`; summing proves
`0<=Q_m-A_m<=C5^-m Q_m`.

Let the zero-`h` positive coefficient series be

$$
F_0(t)=\prod_p(1+\Lambda_p^{-1}t^{d_p}).
$$

Initially for `|t|<1`, repeated-orbit counting gives the exact identity

$$
\log F_0(t)=\sum_{m\ge1}\frac{A_m}{m}t^m
-\sum_{m\ge1}\frac{B_m}{m}t^{2m}.
\tag{25}
$$

For example, (25) also follows by applying
`1+x=(1-x^2)/(1-x)` to every primitive factor. The factors `d_p` in (23)
exactly cancel the `m=r d_p` denominators; no repeated-orbit multiplicity is
omitted.

Set

$$
H_F(t)=\sum_{m\ge1}\frac{A_m-1}{m}t^m
-\sum_{m\ge1}\frac{B_m}{m}t^{2m}.
$$

By (24), `H_F` is holomorphic in

$$
|t|<R_{\rm cl}:=\min(\vartheta^{-1},\sqrt5)>1.
\tag{26}
$$

Therefore

$$
F_0(t)=\frac{e^{H_F(t)}}{1-t},\qquad
C_F(\Psi):=e^{H_F(1)}
=\exp\sum_{m\ge1}\frac{A_m-1-B_m}{m}>0.
\tag{27}
$$

For every fixed `1<R_1<R_cl`, Cauchy estimates for the coefficients of
`e^{H_F}` give

$$
[t^n]F_0(t)=C_F(\Psi)+O_{R_1}(R_1^{-n}).
\tag{28}
$$

Indeed `[t^n]F_0` is the partial sum of those analytic coefficients; subtract
their absolutely convergent sum at `t=1` and bound the remaining geometric tail.

For every subset `S` in (21), the total error exponent in (22) has absolute
value at most `C n h^2`. Since the coefficients in (21) are nonnegative,

$$
e^{-Cnh^2}[t^n]F_0(t)\le F_{n,N}
\le e^{Cnh^2}[t^n]F_0(t).
\tag{29}
$$

The fixed coefficients in (28) are uniformly bounded. Consequently, for every
fixed finite `B`, uniformly for `0<=n<=BN`,

$$
\boxed{\quad
F_{n,N}=C_F(\Psi)+O_B(n/N^2)+O_{R_1}(R_1^{-n}).\quad}
\tag{30}
$$

This estimate covers the full Heisenberg-scale degree range. Only the second
error in (30) needs `n` to tend to infinity to obtain a limit.

## 4. The constant for this specified perturbation

For the unperturbed cat map, `Lambda_m=lambda^m` and the fixed-point count (4)
give

$$
A_m^{(0)}=1-2\rho^m+\rho^{2m},\qquad
B_m^{(0)}=\rho^m-2\rho^{2m}+\rho^{3m}.
$$

Using `sum x^m/m=-log(1-x)` in the absolutely convergent series (27),

$$
C_F(L)=\frac{(1-\rho)^3(1-\rho^3)}{(1-\rho^2)^3}
=\frac{1-\rho^3}{(1+\rho)^3}
=\frac{7\sqrt2}{16}.
\tag{31}
$$

For the last equality, put `v=sqrt(2)-1`, so `rho=v^2`. Dividing numerator and
denominator of the middle expression by `v^3` gives
`(v^-3-v^3)/(v^-1+v)^3=14/(16 sqrt(2))`.

The existing quantitative classical proof is strong enough to control the
change in this constant; no differentiation of an unproved pressure function
is needed.

### 4.1 Quantitative trace part

Let `R_perp` and `R_0,perp` be the trace-class operators on the complement of
constants constructed in the classical input. That proof establishes

$$
\|R_\perp\|,\|R_{0,\perp}\|\le\vartheta,
\qquad \|R_\perp-R_{0,\perp}\|_1<\eta:=10^{-56}.
$$

The linear operator is a weighted permutation of nonzero Fourier indices; no
index is fixed by a positive power of `L^T`. Its trace at every positive power
is therefore zero. The finite telescoping identity for powers and the
trace-norm ideal inequality give

$$
|Q_m-1|\le m\eta\vartheta^{m-1},\qquad
\sum_{m\ge1}\frac{|Q_m-1|}{m}<8000\eta.
\tag{32}
$$

### 4.2 Quantitative multiplier part

In the fixed eigenbasis of `L`, the derivative matrices have the form

$$
D\Psi(x)=\begin{pmatrix}\lambda&0\\0&\rho\end{pmatrix}+E(x),
\qquad |E_{ij}(x)|<\delta:=10^{-70}
$$

by the classical input. The slope cone `|s/u|<=delta` is invariant: its new
slope has absolute value at most
`(delta+(rho+delta)delta)/(lambda-delta-delta^2)<delta`.
The invariant unstable line thus has a slope in this cone. Its expanding first
coordinate factor belongs to `[lambda-2delta,lambda+2delta]`. On a periodic
orbit, multiplication of these coordinate factors gives its unstable
eigenvalue exactly. Since `lambda>5`,

$$
|\log\Lambda_m-m\log\lambda|\le\delta m.
\tag{33}
$$

No regularity of the invariant line beyond this invariant-cone construction is
used.

Define

$$
c(x)=\frac{x}{(1-x)^2}-x+x^2.
$$

For `0<=x<=1/5`, direct differentiation gives `0<=c'(x)<=10x`. Moreover

$$
A_m-1-B_m=Q_m-1-\sum_{\operatorname{Fix}\Psi^m}c(\Lambda_m^{-1}).
\tag{34}
$$

The fixed-point counts for `Psi` and `L` agree exactly. By (33), for each
multiplier `x=Lambda_m^-1` and `x_0=lambda^-m`,

$$
|x-x_0|\le\delta m\lambda^{-m}e^{\delta m},\qquad
\max(x,x_0)\le\lambda^{-m}e^{\delta m}.
$$

Using (4) to sum the mean-value bound for `c`,

$$
\left|\sum_{\operatorname{Fix}\Psi^m}c(\Lambda_m^{-1})
-(\lambda^m+\lambda^{-m}-2)c(\lambda^{-m})\right|
\le10\delta m\lambda^{-m}e^{2\delta m}.
\tag{35}
$$

The sum of (35) divided by `m` is below `3delta` because
`lambda^-1 e^(2delta)<0.18`. Combining (27), (31)-(35) proves

$$
\boxed{\quad
\left|\log\frac{C_F(\Psi)}{7\sqrt2/16}\right|
<8000\,10^{-56}+3\,10^{-70}<10^{-51}.
\quad}
\tag{36}
$$

This number concerns a positive geometric diagonal, not the spectral-statistic
discrepancy.

## 5. A complete signed cancellation beyond degree N

Define the different-subset contribution by the finite sum

$$
X_{n,N}:=\sum_{\substack{S\ne T\\\ell(S)=\ell(T)=n}}
U_N(S)\overline{U_N(T)}.
\tag{37}
$$

No modulus is taken before completing this sum. By its definition,

$$
|c_{n,N}|^2=F_{n,N}+X_{n,N}.
\tag{38}
$$

Combining (19), (30), and (38), for every fixed `B>1`, uniformly throughout

$$
N+N^{1/50}\le n\le BN,
$$

one has

$$
\boxed{
X_{n,N}=-C_F(\Psi)+O_B(N^{-1})+
O_{R_1}(R_1^{-n})+O(e^{-2cN^{1/50}}).
}
\tag{39}
$$

Thus a positive diagonal close to `0.618718433538229` is canceled by the entire
different-pseudo-orbit sum at these lengths. This holds for the original fixed
map and all sufficiently large odd `N`.

It is essential to distinguish (39) from the unresolved expression
`N^-2 sum_m w(m/N) O_{m,N}` in the original problem. In (39), the objects being
paired are subsets of primitive orbits of total length `n`, with fermionic
signs. In the original pair statistic they are periodic orbits contributing to
a **power trace**. Passing from one to the other requires division by the
determinant and controls mixed products not present in (39).

## 6. Direct attempt at the reciprocal and mixed ratio

To go beyond the numerator cutoff, write

$$
\mathcal Z_N(z)^{-1}=\sum_{n\ge0}b_{n,N}z^n.
$$

Its formal Euler expansion consists of multisets of primitive orbits. Pairing
only identical multisets gives the positive coefficients

$$
B_{n,N}^{\rm diag}=[t^n]\prod_p(1-|u_{p,N}|^2t^{d_p})^{-1}.
\tag{40}
$$

At zero `h` the corresponding series is

$$
B_0(t)=\exp\sum_{m\ge1}\frac{A_m}{m}t^m
=\frac{e^{H_B(t)}}{1-t},\quad
H_B(t)=\sum_{m\ge1}\frac{A_m-1}{m}t^m.
\tag{41}
$$

The same coefficient proof and the same weight comparison as (28)-(30) imply

$$
B_{n,N}^{\rm diag}=C_B(\Psi)+O_B(n/N^2)+O(R_1^{-n}),\quad n\le BN,
\tag{42}
$$

where

$$
C_B(\Psi)=\exp\sum_{m\ge1}\frac{A_m-1}{m}>0.
$$

The elementary calculation for the cat map gives

$$
C_B(L)=\frac{(1-\rho)^2}{1-\rho^2}=
\frac{1-\rho}{1+\rho}=\frac1{\sqrt2}.
$$

Replacing `c(x)` in (34)-(35) by `x/(1-x)^2-x`, whose derivative also is
bounded by `10x` on `[0,1/5]`, proves

$$
\left|\log\frac{C_B(\Psi)}{1/\sqrt2}\right|<10^{-51}.
\tag{43}
$$

There is also a rigorous control of the **whole diagonal** at a microscopic
radius. For fixed `s>0`, put `r_N=e^{-s/N}`. The bounds in (29) remain valid
for the multiset coefficients at every `n`; the fixed coefficients of (41) are
bounded. Hence the tail after `BN` of
`N^-1 sum r_N^(2n) B_{n,N}^{diag}` is uniformly bounded by
`C_s exp(-sB)` once `N` is large. Applying (42) on the finite interval and then
letting `B` increase gives

$$
\boxed{\quad
\frac1N\sum_{n\ge0}e^{-2sn/N}B_{n,N}^{\rm diag}
\longrightarrow\frac{C_B(\Psi)}{2s}.
\quad}
\tag{44}
$$

This is the full positive diagonal calculation for the reciprocal, not an
assumption that its phase cross terms vanish.

For the actual reciprocal Parseval gives

$$
\int_0^{2\pi}|\mathcal Z_N(r_Ne^{it})|^{-2}\frac{dt}{2\pi}
=\sum_{n\ge0}r_N^{2n}|b_{n,N}|^2.
\tag{45}
$$

Equations (40)-(44) do not bound (45): their omitted different-multiset terms
can have either sign. The cutoff (19) supplies no bound on those reciprocal
coefficients. In fact, (2) implies that the reciprocal has exactly the spectral
poles on the unit circle. Any use of Cauchy's estimate for it at the exterior
radius `19/8` is invalid.

The direct universal estimate from the eigenvalue product at `r_N` is only

$$
|D_N(r_Ne^{it})|^{-1}\le(1-r_N)^{-N},
\tag{46}
$$

of size `exp(N log N+O_s(N))`. The analytic factor in (2) changes this by at
most a fixed multiplicative constant, and cannot repair it. Using (46) in a
mixed determinant ratio loses the entire cancellation estimate.

The first unsuccessful step of this route is therefore a **direct** bound or
evaluation of mixed numerator/reciprocal orbit sums at radius `e^{-s/N}`. Neither
the controlled positive diagonals (30), (42), nor the full alternating
numerator cancellation (39) supplies such a bound. It is not being installed as
a hidden hypothesis.

## 7. Exact finite-rank location of the ramp and plateau

There is a useful exact way to locate what a successful fermionic argument
would still have to establish, without declaring that step proved.

Let `e_j` be the elementary symmetric functions of the eigenvalues of the
original `U_N`, and `h_j` the complete symmetric functions, so

$$
D_N(z)=\sum_{j=0}^N(-1)^je_jz^j,\qquad
D_N(z)^{-1}=\sum_{j\ge0}h_jz^j.
$$

For `m>=1,0<=r<m`, define the explicit hook combination

$$
\chi_{m,r}:=\sum_{j=0}^r(-1)^j e_{r-j}h_{m-r+j}.
\tag{47}
$$

No representation-theoretic theorem is needed for the following identity:

$$
\boxed{\quad p_{m,N}=\sum_{r=0}^{\min(m,N)-1}(-1)^r\chi_{m,r}.\quad}
\tag{48}
$$

To prove it, sum (47) over `r=0,...,m-1` with the outside sign. The term
`e_t h_(m-t)` occurs `m-t` times, so the result is
`sum_(t=0)^(m-1) (m-t)(-1)^t e_t h_(m-t)`. The identity `D_N D_N^-1=1`
reduces this to
`sum_(t=1)^m (-1)^(t+1)t e_t h_(m-t)`, exactly the coefficient of
`-zD_N'/D_N`, namely `p_m`. If `r>=N`, (47) equals
`(-1)^r sum_(t=0)^N (-1)^t e_t h_(m-t)=0`, because `m>r>=N`. This proves
the finite-rank endpoint in (48).

There are exactly `min(m,N)` surviving terms. Counting them would give the CUE
ramp and plateau only after the relevant weighted signed cross products of the
`chi_(m,r)` were evaluated. At the fixed matrix, a scalar angular shift
multiplies every term in (48) by the same phase of degree `m`; it does not
orthogonalize them.

The exterior-power norm `||wedge^r U_N||=1` and positivity of its squared
coefficients do not change this fact. Formula (47) contains the reciprocal
coefficients, and the step from the exact alternating decomposition (48) to
the weighted covariance `min(m,N)` is precisely the uncontrolled mixed sum
identified in Section 6. The geometrically computed diagonals above do not
estimate that mixed sum.

## 8. Remaining original estimate

With the fixed bump test `b_*` in the input manifest, the first original
statistical estimate remains

$$
\frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
\bigl(|p_{m,N}|^2-\min(m,N)\bigr)\longrightarrow0
$$

along all odd dimensions. No value or sign of this limit is proved here.

The new cancellation (39) is kept as a distinct proved fact; it must not be
substituted for this estimate. All-order `H_diag` and the point-process limit
therefore remain open in this continuation.


---

