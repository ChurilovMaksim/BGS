> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/arithmetic_comb_fourth_difference_gap.md`. Embedded SHA256: `0b7bd5a0c21b79f1dd45d6b6377e58cd9f9afcdb8ed017199c874ace8e2fcc66`.
> [Thematic guide](../../topics/arithmetic.md).

# A fourth quantum difference gives uniform escape from square-root comb spaces

Date: 21 October 2026. Original fixed `tau=10^(-80)`.

## 0. Claim and scope

Let `N=d^4`, with odd `d` tending to infinity, and let `J_d:C^(d^2)->C^N`
be the canonical oldspace embedding

$$
(J_d\phi)(x)=
\begin{cases}
d^{-1/2}\phi(y\bmod d^2),&x=dy,\\
0,&d\nmid x.
\end{cases}
\tag{0.1}
$$

Write `P_d=J_dJ_d^*`, `E_N=exp(i tau N A_N)`, and
`C_d=J_d^*E_NJ_d`. The range of `P_d` has rank `d^2=sqrt(N)`.

The result proved below is a fixed positive norm gap:

$$
\boxed{
\|C_d\|\le\sqrt{1-\tau^2\sigma^2/1024}<1
\quad\text{for all sufficiently large odd }d,
}
\tag{0.2}
$$

where the explicit, fixed positive number `sigma` is

$$
\sigma^2=\sum_{k,l}|\widehat{\partial_q^4a}(k,l)|^2,
\qquad
\sigma\ge\frac{9}{10\sqrt2}(14\pi)^4>10^6.
\tag{0.3}
$$

The physical symbol `a` is defined in Section 1. The constant is small but
does not decrease with dimension. In particular the sequence `d=7^r` is
included. No averaging in `d`, `N`, or `tau` is used.

This rules out a common-phase quasimode construction inside these arithmetic
comb spaces: every unit vector in the comb loses at least `tau sigma/32` in
norm under one kick, and under the full `U_N`. It does not rule out spectral
microclusters whose eigenvectors are not concentrated in these spaces.
It is not a proof or refutation of `H_diag`.

The delicate estimate is the exact finite-word norm bound in Section 4.
Its proof is given using logarithmic generators and scaled commutators;
no Egorov estimate at Fourier frequency `N^(3/4)` is invoked. An independent
operator audit has independently reconstructed this estimate and its
odd-lattice conventions; its frozen source and the precise checks are
recorded in Section 7.

## 1. Quantization and the exact low-frequency symbol

Put

$$
h=(2\pi N)^{-1},\quad t=\tau/(2\pi),\quad
W_N(k,l)=(-1)^{kl}T_N(l,k),\quad
Q_N(b)=\sum_{k,l}\widehat b(k,l)W_N(k,l).
\tag{1.1}
$$

The real-half Weyl mode on the grid is `W_N(k,l)`: its extra phase relative
to the modular half is `(-1)^(kl)`. Thus the exact original Hamiltonian is
`A_N=Q_N(a)`, where

$$
\begin{aligned}
a(q,p)={}&\cos14\pi q+\frac{r(q)}{10}
 +\frac{r(q)\sin2\pi q}{100}-\frac1{10}\\
&+\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.
\end{aligned}
\tag{1.2}
$$

The half-period change in the mixed term multiplies its `l=+/-1` Fourier
coefficients by the required `(-1)^k`. Consequently this is the given
Hamiltonian, not a modification of its quantization.

The Fourier support satisfies `|k|+|l|<=9`, and the coefficient one-norm is
at most two. Indeed the three nonconstant building-block one-norms are
`||cos||_1=||sin||_1=1` and `||r||_1<=4`, so the coarser bound
`1+4/10+4/100+4/100+1/10<2` suffices.

Let `g=partial_q^4 a`. Its support lies in `|k|<=9, |l|<=1`. In the
`l=0,k=+/-7` coefficients the cosine contribution is exactly
`(9/20)(14 pi)^4` at each sign. The `r sin(2pi q)` term has cancelling
`sin(14pi q)` contributions; in any case an imaginary sine contribution
could not decrease this real part. The mixed term has `l=+/-1`.
This proves (0.3).

## 2. Exact compression of a finite Fourier polynomial

For arbitrary odd `N=d^2m`, the embedding in (0.1), with `m` replacing `d^2`,
satisfies

$$
J^*T_N(a,b)J=0\quad\text{unless }d\mid a\text{ and }d\mid b.
\tag{2.1}
$$

If `d` does not divide `a`, the shifted support is disjoint. If `d|a` but
`d` does not divide `b`, summing the `d` periodic repetitions gives the
zero character sum `sum_(s=0)^(d-1) e_d(bs)`. This proves (2.1) directly,
including its modular phases. At `a=da',b=db'`, the surviving compression is
the appropriate `m`-dimensional Weyl operator; only the zero/nonzero
criterion is needed here.

Since any two frequencies in the support of `g` differ by at most eighteen
in `k` and two in `l`, (2.1) gives, for every `d>18`,

$$
\boxed{P_d Q_N(g)^*Q_N(g)P_d=\sigma^2P_d.}
\tag{2.2}
$$

For equal frequencies `W_N(k,l)^*W_N(k,l)=I` exactly. For unequal frequencies
their Weyl product has a nonzero frequency difference with at least one
component not divisible by `d`, so its compression is zero. Thus (2.2) has
no remainder and no positivity estimate imported from a classical model.

Equivalently, (2.2) can be obtained by averaging the conjugates of
`Q_N(g)^*Q_N(g)` over the finite group of oldspace translations. That is an
exact algebraic projection for a fixed matrix, not an extra randomization
of the spectral problem.

## 3. A smooth quantum generator with uniform bounds

This section supplies the bounded scaled commutators used in Section 4.
The same calculation is valid on the plane and on every torus character
fiber. Write `P=-ih partial_q` on the plane and use ordinary Weyl
quantization `Op_h`; the periodic modes descend to (1.1).

Let

$$
\mathcal E(s)=e^{is\operatorname{Op}_h(a)/h}.
$$

The exact commutator with `P` gives

$$
\mathcal E(t)^*P\mathcal E(t)
=P+\operatorname{Op}_h(v_h),
\qquad
v_h=\int_0^t e^{s\mathcal L_h}a_q\,ds,
\quad
\mathcal L_h b=-\frac{i}{h}(a\star_hb-b\star_ha).
\tag{3.1}
$$

The following direct series proves that this is the actual operator and
provides estimates uniform in `h`. The multiplier of a scaled Weyl
commutator of modes `nu,mu` has absolute value at most
`4pi^2 |nu wedge mu|`. Since `a` has coefficient one-norm at most two and
support radius nine, induction gives

$$
\|\mathcal L_h^n a_q\|_{\ell^1}
\le120\,7000^n n!,\qquad
\operatorname{supp}(\mathcal L_h^n a_q)
\subset\{|k|+|l|\le9(n+1)\}.
\tag{3.2}
$$

For the induction, the next multiplier costs at most
`40*9*9(n+1)*2=6480(n+1)<7000(n+1)`. The initial derivative costs less
than `2*18pi<120`. A derivative of total order `K` costs at most the further
factor `60^K(n+1)^K`.

Thus, at the stated fixed `t`, the series

$$
v_h=\sum_{n\ge0}\frac{t^{n+1}}{(n+1)!}\mathcal L_h^n a_q
\tag{3.3}
$$

converges in every fixed weighted Fourier one-norm, uniformly in real `h`.
It also converges in a fixed analytic Fourier norm: multiplication of its
`n`-th term by `exp(rho*9(n+1))` still leaves a geometric series for, say,
`rho=1`. Its quantization solves the actual bounded-operator Heisenberg
equation. Uniqueness of that equation, followed by the integral identity
`E^*PE-P=int E(s)^* Op(a_q) E(s) ds`, proves (3.1). The commutator with `P`
is bounded, so this last identity holds first on its domain and extends as
a bounded difference. It is not a formal expansion in `h`.

Set

$$
H_0=-P,\qquad H_1=-\mathcal E(t)^*P\mathcal E(t)
=-P-\operatorname{Op}_h(v_h).
\tag{3.4}
$$

The difference of these two Hamiltonians is bounded and has uniformly
bounded analytic symbol seminorms `O(tau)`. A scaled commutator with `H_0`
is exactly minus a `q` derivative. A scaled commutator with the periodic
part is bounded in weighted Fourier norms by

$$
\|h^{-1}[\operatorname{Op}_h(b),\operatorname{Op}_h(c)]\|_K
\le40\|b\|_{K+1}\|c\|_{K+1}.
\tag{3.5}
$$

Here the weighted Fourier coefficient norm is, explicitly,
`||b||_K=sum_(k,l)|bhat(k,l)|(1+|k|+|l|)^K`; it does not include a
factor `2pi` per derivative. The left side means the same coefficient norm
of the commutator symbol. Derivatives separately cost their factors `2pi`
as in (3.2). Formula
(3.5) follows term by term from the same sine multiplier. In particular
every mixed scaled commutator of positive depth at most four formed from
`H_0,H_1` is a bounded periodic operator with uniform norm `O(tau)`.
After the first nonzero bracket it contains the periodic difference;
further brackets either differentiate it or bracket it with another
uniformly controlled periodic symbol.

Here is an explicit constant sufficient for the argument. From (3.2),
for `0<=K<=4` and `|t|<=10^(-12)`,

$$
\|v_h\|_K\le240\,10^K|t|.
\tag{3.6}
$$

Each scaled commutator with `H_0` or `H_1` applied to a periodic symbol
costs at most `7||b||_(K+1)` for `K<=3`. Indeed its linear part costs
`2pi`, while its periodic part costs at most
`40*240*10^4|t|<0.001`. The first nonzero bracket of `H_0,H_1`
contains one derivative of `v_h`. Hence every mixed scaled commutator
of depth four has operator norm at most
`7^3*2pi*240*10^4|t|<10^12|t|`.
In Section 4 the Taylor expansions are ordered so that these original
mixed commutators suffice: already formed remainders are transported
only by unitary conjugation, which preserves operator norm. No estimate
of a high-frequency Egorov remainder or of analytically conjugated
brackets is required.

For the final leading term we use explicit smaller constants. With
`q_*=7000t<1/16`, (3.2) gives

$$
\|\partial_q^3(v_h-t a_q)\|_{\ell^1}
\le120\,60^3t\sum_{n\ge1}(n+1)^2q_*^n
\le2\cdot10^{12}t^2,
\tag{3.7}
$$

and

$$
\|\partial_q^3v_h\|_{\ell^1}\le240\,60^3t.
\tag{3.8}
$$

The inequality used in (3.7) is
`sum_(n>=1)(n+1)^2q^n<8q` on `0<=q<=1/16`.

## 4. Exact finite-word norm estimate at `N delta^4=1`

For a real `s`, let

$$
R(s)=e^{isH_0/h},\quad B(s)=e^{isH_1/h}
=\mathcal E(t)^*R(s)\mathcal E(t),
$$

and recursively define

$$
C_0(s)=B(s),\qquad
C_{j+1}(s)=R(s)C_j(s)R(s)^*C_j(s)^*,\quad j=0,1,2.
\tag{4.1}
$$

The word `C_3` contains fourteen occurrences of `R` or its inverse and eight
of `B` or its inverse. In particular it has a fixed length, independent
of the dimension.

### 4.1 Logarithmic-generator proof

Let

$$
\mathcal A(s)=\frac h i C_3'(s)C_3(s)^*.
$$

Differentiating the twenty-two factors expresses `A(s)` as a sum of signed
Hamiltonians conjugated by prefixes of at most twenty-one factors. The
common unbounded linear part cancels. For each single conjugation use
Duhamel's Taylor expansion

$$
\operatorname{Ad}_{e^{\pm isH/h}}F
=\sum_{r=0}^{L-1}\frac{(\pm s)^r}{r!}
 \left(\frac{i}{h}\operatorname{ad}_H\right)^rF
+\mathcal R_L,
\qquad
\|\mathcal R_L\|\le |s|^L M_L/L!.
\tag{4.1a}
$$

For `F=H_j` this is first an identity on the common invariant Schwartz
core; its first commutator is bounded, and the difference extends as a
bounded operator. Expand each prefix from right to left, retaining total
degree at most three. A term already of degree `r` is expanded to order
`4-r`; every resulting remainder therefore contains a mixed original
scaled commutator of total depth exactly four. Subsequent prefix factors
conjugate that remainder unitarily, without increasing its norm.
There are fewer than `22*21*binomial(24,3)<10^8` possible remainder
terms. By (3.6) their sum is bounded by
`10^20|t||s|^4`, uniformly in `h` and `|s|<=1`.

The coefficients through degree three can be identified by finite Lie
algebra, independently of an operator-norm Taylor series for the unbounded
Hamiltonians. For formal symbols `X,Y`, repeated use of

`[exp(sX), I+s^r Z+O(s^(r+1))]
 =I+s^(r+1)[X,Z]+O(s^(r+2))`

shows that the first term of the threefold commutator word is
`s^4[X,[X,[X,Y]]]`. Hence its logarithmic generator has no terms of degrees
zero, one, or two, and its degree-three term is four times that bracket.
Applying this finite algebra to the preceding bounded-commutator expansion
gives

$$
\mathcal A(s)=4s^3K_h+\mathcal R_h(s),\qquad
\|\mathcal R_h(s)\|\le10^{20}|t|\,|s|^4,
\quad
K_h=\left(\frac i h\right)^3
 [H_0,[H_0,[H_0,H_1]]]
=\operatorname{Op}_h(\partial_q^3v_h).
\tag{4.2}
$$

The last identity is exact, since the three commutators with `-P` are exact
derivatives. The fixed numerical bound comes entirely from (3.6) and the
finite prefix expansion just described.

Comparison with the unitary solution
`V(s)=exp(i s^4 K_h/h)`, whose logarithmic generator is exactly
`4s^3K_h`, now uses ordinary Duhamel integration:

$$
\|C_3(s)-e^{is^4K_h/h}\|
\le\frac1h\int_0^{|s|}\|\mathcal R_h(u)\|\,du
\le\frac{10^{20}|t|\,|s|^5}{5h}.
\tag{4.3}
$$

There is no factor `exp(C/h)` in this comparison: both propagators are
unitary. In particular the physically small parameter in the generator
expansion is `s`, even though `s/h` is large.

### 4.2 Descent to the exact odd torus fiber

The line bound cannot simply be restricted to distributional combs. We
prove its finite-dimensional consequence with the explicit Zak transform

$$
(Z\psi)(\alpha,\beta)_j
=N^{-1/2}\sum_{n\in\mathbb Z}e^{-2\pi in\alpha}
\psi((j+\beta)/N+n),
\quad 0\le j<N,\quad \alpha,\beta\in[0,1).
\tag{4.4}
$$

Parseval in `n`, followed by the partition of the real line into the
intervals `[(j+Nn)/N,(j+Nn+1)/N)`, proves
`integral sum_j |Zpsi|^2 dalpha dbeta=||psi||_2^2`. Inverse Fourier
series in `alpha` reconstruct the sampled values, so `Z` is unitary
onto the direct integral with fibers `C^N`.

For an integer Weyl frequency `(k,l)`, write `j+l=r+Nm`, `0<=r<N`.
Direct substitution gives the fiber matrix

$$
(W_h(k,l)_{\alpha,\beta}u)_j
=e^{2\pi ik(j+\beta+l/2)/N}e^{2\pi im\alpha}u_r.
\tag{4.4a}
$$

These unitary matrices are continuous in the fiber variables. At
`alpha=beta=0` they equal exactly `W_N(k,l)` in (1.1). Absolutely
convergent Fourier series and bounded exponentials preserve this
continuity, so it holds for `Op_h(v_h)`, `K_h`, `Op_h(g)`, and `E(t)`.

At the endpoint `s=delta`, `Ndelta` is an integer. Hence
`R(delta)=W_h(0,-Ndelta)` and the whole endpoint word `C_3(delta)`
also has continuous finite fiber matrices. The norm of a decomposable
operator is the essential supremum of its fiber norms. The line estimate
(4.3) therefore holds at almost every fiber; continuity extends it to
every fiber, including `(0,0)`. Its constants are unchanged.
Throughout the line differentiation `h` and `t` are held fixed; the
relation `delta^4/h=2pi` is substituted only at the endpoint. No
intermediate real step needs to preserve the selected finite fiber.

As an alternative exact description of the same finite family, put
`E_s=exp(i tau N Q_N(a(q-s,p)))`. With `delta=1/d`, the first commutator
on the trivial fiber is

$$
C_1=E_\delta^*E_{2\delta}E_\delta^*E_0.
\tag{4.5}
$$

The next two are obtained by taking its shifted word at `q-delta` and
multiplying by its inverse, twice. These are finite matrices for every
real shift parameter and agree with (4.1) at the permitted Weyl step.
This also verifies that the estimate concerns the specified exponential,
not a substituted random or diagonal kick.

At `s=delta=1/d`, `N=d^4`, one has

$$
R(\delta)=T_N(-N/d,0),\qquad
\delta^4/h=2\pi.
$$

Thus (4.3), restricted as above, becomes

$$
\|C_3-e^{i2\pi Q_N(\partial_q^3v_h)}\|
\le10^{21}\tau/d.
\tag{4.6}
$$

### 4.3 The uniform first-order term in the fixed kick

Equations (3.7)–(3.8), followed by the elementary unitary exponential
remainder bound `||exp(iX)-I-iX||<=||X||^2/2` for Hermitian `X`, give

$$
\boxed{
C_3=I+i\tau Q_N(g)+\mathcal R_N,
\qquad
\|\mathcal R_N\|\le10^{18}\tau^2+10^{21}\tau/d,
\quad g=\partial_q^4a.
}
\tag{4.7}
$$

For the numerical margin, `2pi||partial_q^3v_h||<=51,840,000 tau`, so the
quadratic exponential error is less than `1.4*10^15 tau^2`. The linear
error from (3.7) is less than `10^12 tau^2`. The displayed `10^18` therefore
has room to spare. Only the term `10^21 tau/d` awaits a large dimension;
the comparison with the fixed `tau` is explicit.

As a separate sign check, differentiating the exact finite word at
`tau=0` gives

$$
C_3'(0)=iN(\operatorname{Ad}_{R(\delta)}-I)^4A_N.
\tag{4.8}
$$

Its symbol is `iN(a(q-4delta)-4a(q-3delta)+6a(q-2delta)
-4a(q-delta)+a(q))`, tending to `i a_qqqq` since `N delta^4=1`.
It agrees with the sign and normalization in (4.7).

## 5. A norm gap from the exact finite Fourier identity

Let `v` be a unit vector in the oldspace and put

$$
\epsilon=\|(I-P_d)E_Nv\|.
$$

The translation `R=T_N(-N/d,0)` fixes the oldspace pointwise. Therefore

$$
\|(B-I)v\|=\|(R-I)E_Nv\|\le2\epsilon,
\qquad
\|(B^{-1}-I)v\|\le2\epsilon.
\tag{5.1}
$$

Telescoping the fixed word, using that every factor is unitary and that
`R` and `R^(-1)` fix `v`, gives

$$
\|(C_3-I)v\|\le16\epsilon.
\tag{5.2}
$$

On the other hand (2.2) says exactly `||Q_N(g)v||=sigma`. From (4.7),

$$
\|(C_3-I)v\|\ge\tau\sigma-10^{18}\tau^2-10^{21}\tau/d.
\tag{5.3}
$$

Since `tau=10^(-80)` and `sigma>10^6`, the middle error is less than
`tau sigma/4`. For example `d>=10^24` makes the last error less than
`tau sigma/4` as well. Combining (5.2)–(5.3) proves

$$
\boxed{\|(I-P_d)E_Nv\|\ge\tau\sigma/32.}
\tag{5.4}
$$

Unitarity now gives (0.2). This proves uniform escape for every vector,
including vectors whose coefficients vary with dimension in an arbitrary
way. No lower bound for a transcendental exponential polynomial was used.

The exact canonical identity `M_NJ_d=J_dM_(d^2)` can also be checked from
the kernel: summing its `d` input repetitions vanishes unless the output
is divisible by `d`; after writing that output as `dy`, the remaining
quadratic phase is precisely the `d^2` kernel, with the factor
`d N^(-1/2)=1/d` matching the embedding normalization. Modular inverses of
eight reduce to the corresponding inverse in the smaller odd modulus.
Consequently `M_N` preserves the oldspace unitarily. Applying (5.4) to
`M_Nv` proves the same lower escape bound for the full original `U_N`.

## 6. Extension to every canonical oldspace of rank at most `sqrt(N)`

The proof also has the following consequence at no new derivative order.
Let `N=d^2m` be any odd dimension with `d>=N^(1/4)`, equivalently
`m<=sqrt(N)`. Choose

$$
b=\lfloor dN^{-1/4}\rfloor\ge1,\quad
\delta=b/d,\quad\beta=N\delta^4.
$$

Then `delta<=N^(-1/4)`, `1/16<=beta<=1`, and the translation at step
`delta` still fixes the oldspace. Formula (4.7) becomes

$$
C_3=I+i\beta\tau Q_N(g)+\mathcal R_N,
\qquad
\|\mathcal R_N\|\le10^{18}\tau^2+10^{21}\tau N^{-1/4}.
\tag{6.1}
$$

Indeed `delta^4/h=2pi beta` and `delta^5/h=2pi beta delta`; the bounded
factor `beta` can only decrease the quadratic exponential error. The
same Fourier compression identity applies once `d>18`. It follows,
uniformly over every such divisor for sufficiently large odd `N`, that

$$
\boxed{
\|(I-P_{d,N})E_Nv\|\ge\tau\sigma/512,
\qquad
\|J^*E_NJ\|\le\sqrt{1-\tau^2\sigma^2/262144}.
}
\tag{6.2}
$$

The fixed threshold can be chosen independently of `d` in this range,
because the error in (6.1) depends on `N^(-1/4)` and all compression
supports are fixed. Thus the fourth-difference argument excludes
nearly invariant canonical comb packets of any rank up to `sqrt(N)`,
not only the exact fourth-power subsequence.

### 6.1 All character combs and the complete arithmetic itinerary

The same estimate holds on every character translate of the canonical
space, uniformly over all characters. To make this precise, put

$$
H_d(s,u)=T_N(sN/d,uN/d),\qquad(s,u)\in(\mathbb Z/d\mathbb Z)^2.
\tag{6.3}
$$

This is an exact representation of the abelian group: every symplectic
product in the Weyl multiplication law is divisible by `N`, since
`(N/d)^2=Nm`. For each character `chi` let

$$
P_\chi=d^{-2}\sum_{s,u}\overline{\chi(s,u)}H_d(s,u).
\tag{6.4}
$$

These are mutually orthogonal projections summing to the identity.
Every nonidentity `H_d(s,u)` has trace zero, by its nonzero shift or
the zero character sum on its diagonal. Therefore every `P_chi` has
rank `N/d^2=m`. The canonical oldspace is the trivial-character case.

A Weyl mode of frequency `(k,l)` changes the two group characters by
the phases `e_d(k)` and `e_d(-l)`. Its compression to any fixed
`P_chi` thus vanishes unless `d|k,l`. Consequently the exact identity

$$
P_\chi Q_N(g)^*Q_N(g)P_\chi=\sigma^2P_\chi
\tag{6.5}
$$

holds for every character once `d>18`.

On this space `R=T_N(-bN/d,0)` acts as a scalar `r_chi` of modulus one.
For unit `v` in the space and
`epsilon=||(I-P_chi)E_Nv||`, set `B=E_N^*RE_N`. Then

$$
\|(B/r_\chi-I)v\|
=\|(R-r_\chi)E_Nv\|\le2\epsilon.
\tag{6.6}
$$

The inverse has the same bound. Replacing `R,B` by
`R/r_chi,B/r_chi` leaves the nested group word unchanged, because
scalar phases cancel in every group commutator. Its fourteen normalized
`R` factors fix `v`; its eight normalized `B` factors have the bound
(6.6). The same telescoping proof and (6.5) therefore give

$$
\boxed{
\sup_\chi\|P_\chi E_NP_\chi\|\le\rho,
\qquad
\rho=\sqrt{1-\tau^2\sigma^2/262144}<1,
}
\tag{6.7}
$$

for all sufficiently large odd `N=d^2m` with `m<=sqrt(N)`.
For `N=d^4` one may use the sharper denominator `1024` in place of
`262144`.

The unperturbed matrix permutes these spaces exactly. Direct substitution
in its given quadratic kernel proves

$$
T_N(a,b)M_N=M_NT_N(3a-4b,-2a+3b).
\tag{6.8}
$$

For clarity, the coefficient of `x` on the left is `b-3a/4`, the
coefficient of `y` is `a/4`, and its constant is `-3a^2/8+ab/2`.
Substituting `c=3a-4b,e=-2a+3b` in the right kernel gives
`-c/4`, `3c/4+e`, and `-3c^2/8-ec/2`, respectively, which coincide.
All fractions in this check are modular inverses in the odd ring.

Let `L(s,u)=(3s-4u,-2s+3u)` modulo `d`. It is invertible because
its determinant is one. Equation (6.8) implies
`M_N P_chi M_N^*=P_(chi composed with L)`. Define the part of the full
step that follows this arithmetic itinerary by

$$
\mathcal K_{N,d}
=\sum_\chi P_{\chi\circ L}U_NP_\chi
=\left(\sum_\chi P_\chi E_NP_\chi\right)M_N.
\tag{6.9}
$$

The sum in parentheses is an orthogonal direct sum of the compressed
kick blocks, so (6.7) proves

$$
\boxed{\|\mathcal K_{N,d}\|\le\rho<1.}
\tag{6.10}
$$

This covers the entire orthogonal character decomposition, rather than
only the canonical sector. The original `U_N` also contains transitions
to other characters. Bound (6.10) does not estimate histories containing
such transitions or their interference with the displayed itinerary.

### 6.2 Its contribution to the full pair sum tends to zero

The block permutation gives more than its norm bound alone. Set

$$
c_n=\operatorname{Tr}(\mathcal K_{N,d}^{\,n}),\qquad
\lambda=3+2\sqrt2.
$$

Since `K^n` maps `P_chi` into `P_(chi composed with L^n)`, only characters
fixed by `L^n` contribute to its trace. Each contributing block has rank
`m=N/d^2` and norm at most `rho^n`. If `F_d(n)` is the number of those
characters, then

$$
\frac{|c_n|}{N}
\le\rho^n\min\left(1,\frac{F_d(n)}{d^2}\right)
\le\rho^n\min\left(1,\frac{\lambda^n}{d^2}\right).
\tag{6.11}
$$

Here is a direct proof of the last estimate valid at every composite
`d`. Characters are labeled by `(Z/dZ)^2`, and the fixed-character
condition is the kernel of `(L^T)^n-I` modulo `d`. For any integral
matrix `B` invertible over the rationals, the map

`x mod d -> Bx/d mod B Z^2`

embeds its kernel modulo `d` into `Z^2/BZ^2`. It is well-defined
because `Bx` is divisible by `d`, and injective because
`Bx/d=By` implies `x=dy`. The latter quotient has cardinality
`|det B|`: integer row and column operations of determinant plus or
minus one preserve its cardinality and, by the Euclidean algorithm,
reduce the calculation to a diagonal matrix. Thus

$$
F_d(n)\le|\det(L^n-I)|
=\lambda^n+\lambda^{-n}-2\le\lambda^n.
\tag{6.12}
$$

No prime-modulus assumption or averaging has entered this estimate.

Define the exact complementary trace

$$
r_n=\operatorname{Tr}(U_N^n-\mathcal K_{N,d}^{\,n}),
\qquad p_n=r_n+c_n.
\tag{6.13}
$$

It includes every operator word in which at least one step leaves the
unperturbed character itinerary. For any bounded weights `w_n`,
including weights depending on `N`,

$$
\begin{aligned}
\frac1{N^2}\left|
\sum_{n\ge1}w_n\bigl(|p_n|^2-|r_n|^2\bigr)\right|
&\le3\|w\|_\infty
 \sum_{n\ge1}\rho^n\min\left(1,\frac{\lambda^n}{d^2}\right)\\
&=O_\tau(\|w\|_\infty d^{-\kappa}),
\qquad
\kappa=-\frac{2\log\rho}{\log\lambda}>0.
\end{aligned}
\tag{6.14}
$$

The inequality uses only `|p_n|<=N`, `|r_n|<=N+|c_n|`, and
`||p_n|^2-|r_n|^2|<=|c_n|(|p_n|+|r_n|)`.
The difference series is absolutely summable by (6.11), even for
nondecaying bounded weights. To verify the displayed power bound, split
the series at `L_d=floor(2log d/log lambda)`. Its initial portion is
bounded by `d^(-2) sum_(n<=L_d)(rho lambda)^n`, and its tail by
`rho^(L_d+1)/(1-rho)`. Here `rho lambda>1` for the stated exact `tau`
and explicit `sigma`. The first sum is at most a fixed multiple of
`rho^(L_d)`, and both portions are `O_tau(d^(-kappa))`.

In particular (6.14) applies to the full compactly weighted pair sum
with `w_n=|bhat(n/N)|^2` and to the infinite Abel sum with
`w_n=exp(-2sn/N)`. It controls the removed contribution and its signed
cross term with all remaining histories, with no cutoff or discarded
tail. The limit for the remaining exact traces `r_n` has not been
established; (6.14) does not supply the CUE comparison for those traces.

## 7. Boundary of the result

The failed candidate was a near-invariant arithmetic sector of order
`sqrt(N)` whose phases might form a microscopic cluster. The uniform
escape estimate rules out that sector construction in the canonical
oldspaces covered above, even along all powers of seven.

It does not establish a form factor, a spacing distribution, or any
signed cancellation sum at times proportional to `N`. Eigenvectors of
`U_N` outside these comb spaces can still have unknown correlations.
The first unresolved estimate in the original problem remains the full
weighted pair discrepancy, followed by all higher fixed orders required
by `H_diag`.

Proof provenance: new derivation from the exact Weyl definition, exact
Heisenberg Fourier series, and a fixed nested unitary commutator. The
pre-existing divisor budget `d<=N^(1/4096)` is not used. Source files from
earlier rounds are not invoked as unproved universality input.

The independent exact-operator reconstruction is
`research_round3_2026_10_21/audit_quartic_commutator_word.md`, frozen SHA-256
`ac9afae71b2c9ad15bc00b4a2b98da25473131bcff15072432c605060b4118c6`.
Its Sections 2–6 independently verify the actual Heisenberg series,
uniform depth-four commutators, right-to-left prefix remainders, and
continuous Zak fiber descent. Its same-direction convention is the
one used throughout the present manuscript. The auditor additionally
checked the rank-at-most-square-root extension in Section 6.

An exact rational Fourier check, independent of asymptotic estimates, is
`research_round3_2026_10_21/arithmetic_comb_fourier_check.py`, SHA-256
`4b27d43ecb57c38765dafeb1aaeac7011e454e761cfa8210db229f06093576d1`.
It checks the support, conjugate symmetry, coefficients `a_(+/-7,0)=9/20`,
and the exact value
`sigma^2/(2pi)^8=377350620897/160000`.
