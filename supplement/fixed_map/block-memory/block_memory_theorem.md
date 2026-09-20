# Rapid block mixing and persistent coherent memory

Research continuation, 19 September 2026. Base revision:
`e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7`. Parent:
`../algebraic-return/checkpoint.json`.

This note proves a limitation of replacing the prescribed quantum map
by a Markov chain on the spectral blocks of its cat factor. Every pair
of distinct blocks has a uniformly positive one-step transition rate.
Nevertheless, the unmeasured map retains almost all of an initial
block population for **every** time in the small quantum kick regime.
The distinction persists in Heisenberg windows. There is also an exact
finite certificate at the original coupling tau=10^-80.

The full fixed-coupling BGS problem remains open. No priority claim,
external refereeing, or proof-assistant certification is made. These
results and their programs remain research intermediates; no git commit
or push is authorized before the main barrier is closed.

## 1. Model and precise claims

Let K be an odd prime, K>=13, and define odd integers N,F by

\[
 N+F\sqrt2=(1+\sqrt2)^K,\qquad N^2-2F^2=-1.
\]

Use the raw modular Weyl convention on C^N:

\[
 (T(a,b)\psi)(x)=e_N\bigl(b(x+a/2)\bigr)\psi(x+a),
 \quad
 M_{xy}=N^{-1/2}e_N[-8^{-1}(3x^2-2xy+3y^2)].
\]

Fractions inside e_N mean modular inverses. With
S=((3,4),(2,3)) one has M T(v) M*=T(Sv). Multiplication of M by a scalar
will be used to arrange M^K=I. It changes no block transition.

The actual symbol is

\[
\begin{split}
 f(q,p)&=\cos(14\pi q)+r(q)/10
       +r(q)\sin(2\pi q)/100
       +r(q)\cos(2\pi p-\alpha_0)/100,\\
 r(q)&=(1-\cos(14\pi q))(1+\cos(2\pi q)),\qquad
 e^{i\alpha_0}=(-3+4i)/5.
\end{split}
\]

Quantize e(kq+lp) as T(l,k), and center A=Op_N(f)-(1/10)I.
Put D=exp(i epsilon A), U=DM, and omega=exp(2 pi i/K). Let P_s be
the spectral projection of M for omega^s, d_s=Tr P_s, pi_s=d_s/N.
For integers m>=0 define column-stochastic matrices

\[
 T_{rs}^{\rm cl}=\frac{\operatorname{Tr}(P_rDP_sD^*)}{d_s},
 \qquad
 C_{rs}(m)=\frac{\operatorname{Tr}(P_rU^mP_sU^{-m})}{d_s}.
\tag{1}
\]

The superscript cl distinguishes the Markov transition from Weyl T(v).
They obey C(1)=T^cl. In general C(m) is not (T^cl)^m. Iteration of
T^cl represents measuring the cat block **and resetting the state to
P_s/d_s** after each outcome s. Block measurement alone need not make
the populations Markovian: the state inside the block also matters.

Write TV(p,q)=(1/2) sum_r |p_r-q_r| and set

\[
 F_0=593/500,\qquad a_0=43/125.
\]

**Theorem.** If 0<|epsilon|<=1/10, then

\[
 T_{rs}^{\rm cl}\ge\frac{\epsilon^2}{300}\pi_r
 \quad\hbox{for all }r,s,
 \qquad
 \operatorname{TV}((T^{\rm cl})^m e_s,\pi)
 \le e^{-m\epsilon^2/300}.
\tag{2}
\]

If also K |epsilon| F_0<=1/4, then for every integer m

\[
 C_{ss}(m)\ge1-4K^2\epsilon^2F_0^2.
\tag{3}
\]

Consequently, for m>=0,

\[
 \operatorname{TV}\bigl(C_{\cdot s}(m),(T^{\rm cl})^m e_s\bigr)
 \ge 1-4K^2\epsilon^2F_0^2-\pi_s-e^{-m\epsilon^2/300}.
\tag{4}
\]

The same statements hold for the ordinary-midpoint convention when
the signs (-1)^(ab) are applied to the original integer Fourier labels
before modular reduction. The proof uses coefficient magnitudes and
the two unchanged dominant coefficients, not equality of the spectra
of the two conventions. The raw convention is used in the finite
diagnostics below.

## 2. Arithmetic and traces, including composite N

Pell arithmetic gives

\[
 S^K=\begin{pmatrix}N^2+2F^2&4NF\\2NF&N^2+2F^2\end{pmatrix}
 \equiv I\pmod N.
\]

Since det(S-I)=-4 is a unit modulo odd N, S has no nonzero fixed
label. For 0<j<K, if S^j v=v, then Bezout applied to j and K, using
the invertibility of S, gives Sv=v. Thus S^j-I has trivial kernel
on the finite module (Z/NZ)^2 and is invertible. This argument does
not assume N is prime. Every nonzero Weyl label has orbit length K.

The Weyl operators form an orthonormal basis for the normalized
Hilbert--Schmidt product <X,Y>=Tr(X*Y)/N. Exact covariance and S^K=I
imply that M^K commutes with every Weyl operator and hence is scalar.

For any label v and 0<j<K,

\[
 |\operatorname{Tr}(T(v)M^j)|=1.
\tag{5}
\]

Indeed, the trace of Ad(T(v)M^j) as an operator on matrices is
|Tr(T(v)M^j)|^2. On the Weyl basis it permutes labels by S^j, with
unit phases. Its only fixed label is zero, whose phase is one.

Now P_s=K^-1 sum_j omega^(-sj) M^j. Equation (5) implies

\[
 |d_s-N/K|\le(K-1)/K<1,
 \quad d_s\le2N/K,\quad \pi_s\le2/K.
\tag{6}
\]

All the blocks exist. We will also need N>=144K^2. At K=13,
N=47321>144*169. For odd k, N_(k+2)=3N_k+4F_k>5N_k, whereas
((k+2)/k)^2<2 for k>=13. Induction proves the asserted inequality
for all odd k>=13, including the prime subsequence.

**Necessary scope control.** For composite K=9, N=1393=7*199,
S^3-I has 49 fixed labels. Consequently |Tr M^3|=7, not 1. The
prime-period restriction cannot simply be removed from (5).

## 3. A lower bound in every nonzero temporal charge

For the unique finite Weyl expansion X=sum_v x_v T(v), put
||X||_W=sum_v |x_v|. It is submultiplicative, since Weyl products
have unit-modulus structure constants. Also ||X||_op<=||X||_W.
For k in Z/KZ put

\[
 \Pi_k X=\frac1K\sum_{j=0}^{K-1}\omega^{-kj}M^jXM^{-j}.
\]

For k!=0 the scalar Weyl term is killed. Every other Weyl term
has an orbit of K orthogonal labels, giving

\[
 \|\Pi_k X\|_2\le\|X\|_W/\sqrt K.
\tag{7}
\]

The exact centered symbol has 32 nonzero coefficients, each Gaussian
rational with denominator dividing 4000. Its dominant terms are
(9/20)T(0,7)+(9/20)T(0,-7). The sum of |Re a_v|+|Im a_v| over all
other terms is 143/500. Thus ||A||_W<=F_0. No modular aliases occur
here: all integer labels have |a|+|b|<=9, and N>=47321.

The two dominant labels have disjoint S-orbits. Otherwise S^j v=-v
for v=(0,7), so S^(2j)v=v; odd prime K then forces j=0 mod K,
contradicting 2v!=0. Their charge projections are orthogonal. By (7)
and the triangle inequality, for every k!=0,

\[
 \|\Pi_k A\|_2
 \ge\frac{9\sqrt2/20-143/500}{\sqrt K}
 \ge\frac{43/125}{\sqrt K}=\frac{a_0}{\sqrt K},
\tag{8}
\]

where sqrt(2)>=7/5 suffices for the last rational bound.

Let B=D-I. The Banach algebra exponential and F_0<6/5 give, for
|epsilon|<=1/10,

\[
 \|B\|_W\le\frac{F_0|\epsilon|}{1-F_0|\epsilon|}
 \le\frac{15}{11}|\epsilon|,\qquad
 \|B\|_W^2\le2\epsilon^2.
\tag{9}
\]

Using 1/n!<=1/2 for n>=2 similarly gives

\[
 \|B-i\epsilon A\|_W
 \le\frac{F_0^2\epsilon^2}{2(1-F_0|\epsilon|)}
 \le\frac9{11}\epsilon^2.
\]

Since 9/110<a_0/2, equations (7)--(8) imply

\[
 \|\Pi_k B\|_2\ge\frac{a_0|\epsilon|}{2\sqrt K}
 \quad(k\ne0).
\tag{10}
\]

## 4. Exact one-step expansion and Doeblin bound

For r!=s, P_rDP_s=P_rBP_s. Expanding the projectors gives

\[
 \operatorname{Tr}(P_rBP_sB^*)
 =\frac1{K^2}\sum_{u,v=0}^{K-1}
 \omega^{-ru-sv}\operatorname{Tr}(M^u B M^v B^*).
\]

The terms with v=-u mod K sum exactly to
N ||Pi_(r-s) B||_2^2/K. In every other term, commute M^u across
each Weyl component of B; multiplying by a component of B* reduces
the trace, up to a unit phase, to Tr(T(w) M^(u+v)). Its modulus is
one by (5). The total coefficient weight is at most ||B||_W^2,
and the prefactor times the number of such pairs is (K-1)/K<=1.
Therefore the **unscaled trace** satisfies

\[
 \operatorname{Tr}(P_rBP_sB^*)
 =\frac NK\|\Pi_{r-s}B\|_2^2+E_{rs},
 \qquad |E_{rs}|\le\|B\|_W^2.
\tag{11}
\]

There is no missing factor of N in this error bound. Equations
(9)--(10) imply

\[
 \operatorname{Tr}(P_rDP_sD^*)
 \ge\frac{Na_0^2\epsilon^2}{4K^2}-2\epsilon^2
 \ge\frac{Na_0^2\epsilon^2}{8K^2},
\]

since N>=144K^2>(16/a_0^2)K^2. Divide by d_s<=2N/K and use
pi_r<=2/K to obtain

\[
 T_{rs}^{\rm cl}\ge\frac{a_0^2\epsilon^2}{16K}
 \ge\frac{a_0^2\epsilon^2}{32}\pi_r
 \ge\frac{\epsilon^2}{300}\pi_r.
\]

For the diagonal, leakage out of block s is at most
||D-I||_op^2<=epsilon^2||A||_op^2<=epsilon^2 F_0^2. Hence
T_ss^cl>=1-epsilon^2 F_0^2, which also exceeds (epsilon^2/300)pi_s.

Unitarity of D gives column stochasticity and T^cl pi=pi. With
eta=epsilon^2/300, the matrix
R=(T^cl-eta pi 1^T)/(1-eta) is column stochastic with stationary pi.
It follows that TV((T^cl)^m e_s,pi)<= (1-eta)^m<=exp(-m eta).
This proves (2), including its meaning as a measured and reset process.

## 5. All-time memory for the unmeasured unitary

Set delta=||U-M||_op<=|epsilon|F_0. The cat eigenvalues have minimum
chordal separation 2 sin(pi/K)>=g=4/K. Take a circle of radius g/2
around omega^s. The resolvent of M on the circle has norm at most
2/g. If delta<g/2, the Neumann resolvent estimate for U gives
||R_U||<=1/(g/2-delta). The Riesz projections satisfy

\[
 \|Q_s-P_s\|\le\frac{\delta}{g/2-\delta}
 \le\frac{4\delta}{g}\le K|\epsilon|F_0,
\tag{12}
\]

where delta<=g/4 suffices for the middle inequality. Our hypothesis
K|epsilon|F_0<=1/4 is stronger. Along exp(i t epsilon A)M for
0<=t<=1 the contour remains in the resolvent set, so Q_s has rank
d_s. Since U is normal, Q_s is an orthogonal spectral projection;
in particular it commutes with U^m for every integer m.

Split P_s=Q_s+(P_s-Q_s). The two resulting terms give

\[
 \|(I-P_s)U^mP_s\|_{\rm op}
 \le 2\|Q_s-P_s\|\le2K|\epsilon|F_0.
\tag{13}
\]

The normalized squared Hilbert--Schmidt leakage is bounded by the
square of (13), proving (3). The same leakage estimate applies to
each pure unit vector initially in ran(P_s), not only the maximally
mixed state. No expansion growing with m was used.

For any two probability columns their TV distance is at least the
difference of their entries at s. Combine (2) and (3), using
((T^cl)^m)ss<=pi_s+exp(-m eta), to prove (4).

## 6. Heisenberg windows and the original fixed coupling

First consider epsilon_N=N^-a for any fixed 0<a<1/2 along the prime
Pell subsequence. Since K=O(log N), one has K epsilon_N -> 0,
N epsilon_N^2 -> infinity, and max_s pi_s -> 0. For any fixed c>0,
equation (4) proves

\[
 \inf_{m\ge cN}\inf_s
 \operatorname{TV}(C_{\cdot s}(m),(T^{\rm cl})^m e_s)\longrightarrow1.
\tag{14}
\]

This asymptotic uses classical coupling tau_N=epsilon_N/N, which
tends to zero. It is **not** a fixed nonzero tau result. For any
nonnegative normalized time-window weights supported at m>=cN,
the two window-averaged columns also have TV distance tending to
one: the same positive discrepancy at entry s survives averaging.
This last assertion uses the coordinate lower bound, not an invalid
lower bound from convexity of TV.

There is a separate exact finite instance at the prescribed, fixed
tau=10^-80. Set K=199 and

\[
 N=7435863118750905263055986496384859433567398577182017960020667655210005041519,
 \qquad\epsilon=N/10^{80}.
\]

The following are decimal displays of rational bounds computed by
`verify.py`; their decisive comparisons use integer fractions:

| Quantity | Value or bound |
|---|---:|
| epsilon | 0.00007435863118750905263055986496385 |
| K epsilon F_0 | 0.01754967798108876154754895596958 |
| C_ss(m), every integer m | >= 0.99876803521104035316194333330876 |
| N epsilon^2/300 | > 1.37048 * 10^65 |
| Markov TV error, m>=N | < 7.29672 * 10^-66 |
| TV(C column, Markov column), m>=N | > 0.9937 |

For the Markov bound it is enough to use exp(-x)<=1/(1+x), avoiding
evaluation of a giant exponential. More precisely, the exact lower
bound used is

\[
 1-4K^2\epsilon^2F_0^2
 -\left(\frac1K+\frac1N\right)
 -\frac1{1+N\epsilon^2/300}
 >\frac{9937}{10000}.
\tag{15}
\]

Thus after time N a hypothetical repeatedly reset model is essentially
stationary, while the true unitary retains at least 99.8768 percent
of each initial block. This is a finite certificate at the actual
coupling, not a numerical simulation in dimension N or a fixed-tau
asymptotic counterexample. As N tends to infinity at fixed tau,
epsilon=tau N eventually violates the smallness assumptions above.

## 7. What this establishes for the research program

The one-step rates are uniformly positive for the actual frozen
Fourier symbol, and their Markov chain mixes long before time N in
(14)--(15). Even these strong inputs do not justify replacing closed
coherent evolution by that chain at Heisenberg times. Small errors
per step cannot be accumulated here without controlling the memory.
The almost invariant projections Q_s show where that memory resides.

These statements concern cat-block populations. They do not by
themselves give a lower bound on a CUE-subtracted trace statistic,
prove failure of fixed-tau BGS, or solve the all-k correlation target.
The earlier finite spectral-clustering obstruction at K=199 is in
`../design-return/frozen_sharp_return.json`; it is not counted again
as a new result here. Qualitative exclusion of exact returns from
`../algebraic-return/` is consistent with the approximate retention
proved above.

For comparison, Gnutzmann--Altland, *Universal spectral statistics
in quantum graphs*, [arXiv:nlin/0402029v2](https://arxiv.org/pdf/nlin/0402029v2),
explicitly replace spectral averaging by independent bond-phase
averaging using rationally independent bond lengths, equation (2).
Their use of a classical transition operator belongs to that averaged
graph construction. It supplies no identity C(m)=(T^cl)^m for this
single fixed unitary. This is a source-scope comparison, not a new
claim about the validity of their theorem.

The still missing estimate is quantitative control of the **coherent**
CUE-subtracted trace products in a Heisenberg window for epsilon=tau N
at fixed nonzero tau, without imposing independent phases, resetting,
or averaging over the coupling. The new result rules out one proposed
replacement for that estimate; it does not provide the estimate itself.

### Qualitative continuation beyond small epsilon

For these same prime Pell dimensions, every entry of T^cl is strictly
positive at **every nonzero real algebraic epsilon**, with no smallness
restriction. Thus the actual fixed algebraic tau family has a primitive
block transition matrix at every dimension of this subsequence. There
is no uniform lower bound on its gap from this assertion.

To prove this, apply (11) to B=A and (8), obtaining for r!=s

\[
 \operatorname{Tr}(P_rAP_sA)
 \ge\frac{Na_0^2}{K^2}-F_0^2>0,
\]

since N>=144K^2 and 144a_0^2>F_0^2. Every P_rAP_s is nonzero.
The entries of M, its scalar-normalized version, P_r and A are
algebraic. Each entry of P_r exp(i z A) P_s is a finite linear
combination of exponentials exp(i z a_j), where the distinct real
eigenvalues a_j of A and all coefficients are algebraic. By the
Lindemann--Weierstrass specialization lemma proved and sourced in
`../algebraic-return/exact_return_theorem.md`, vanishing at a nonzero
algebraic epsilon forces such an entry to vanish identically in z.
If the whole offdiagonal block vanished, its derivative at zero,
i P_rAP_s, would vanish, a contradiction. A diagonal block cannot
vanish either, since its value at zero is P_s!=0. Squared block
Hilbert--Schmidt norms give the asserted strict positivity.

The external theorem is the linear independence of exponentials of
distinct algebraic numbers over the algebraic numbers; see Evertse,
*Transcendence results*, Theorem 4.8, printed p.48,
[lecture notes](https://pub.math.leidenuniv.nl/~evertsejh/dio15-4.pdf).
This is an application of the prior specialization argument, not a new
transcendence result. Neither strict positivity nor finite-dimensional
primitivity specifies a mixing time uniform in N, and neither restores
the equality between repeated resetting and coherent evolution.

## 8. Reproduction and review

Run from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 python build/block-memory/verify.py
```

`exact_certificate.json` records the rational certificate (15),
constant checks, exact Pell/coprimality checks through K=199, and
the K=9 negative control. The proof covers infinitely many prime K;
finite arithmetic checks alone do not establish that range.

`dense_diagnostics.json` independently assembles dense Weyl and cat
matrices at (K,N)=(5,41),(7,239), epsilon=0.03. It checks covariance,
twisted traces, charge and edge formulas, stochasticity and stationarity,
C(1)=T^cl, and all-time retention at the sampled times up to 500000.
Schur diagonalization is checked before powering. These small dimensions
do **not** satisfy N>=144K^2, so the diagnostics are not instances of
the full conservative Doeblin theorem. They are also not at tau=10^-80.
Their epsilon does satisfy the separate retention condition.
`block_memory.png` and `.svg` show this finite diagnostic honestly.

A separate internal mathematical audit checked the dependency chain,
normalizations, constants, projector argument and exact K=199 comparison.
It reported no gap under the stated hypotheses. This does not replace
external review or formal verification. No Lean execution is claimed.
