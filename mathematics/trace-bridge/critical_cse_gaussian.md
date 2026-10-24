# CSE critical trace: all cumulants, a Gaussian boundary layer and phase transfer

**Stable claim:** BGS-TRACE-069. **State:** PROVED.
**Boundary:** Growing n/N->1, d=o(N), logarithmic critical variance, every fixed cumulant and mixed moment, conditional Gaussian law. Second/fourth cumulants are prior HSW formulas; no independent-block interpretation or external novelty certificate.
**Integration and review:** [11 October disposition](../../archive/record/chat_integration_20261011.md).
**Original input:** [dated source](../../archive/evidence/executions/20261011/chat-research/original/jack_phase_2026_10_11/critical_cse_gaussian.md).


## Statement and conventions

Let Q_N be a CSE matrix of size 2N, and count its N Kramers pairs once:
p_n(Q)=Tr(Q^n)/2. Let n_N be any positive integer sequence with
n_N/N→1, and set m_N=E_CSE|p_{n_N}|² using the exact finite mean.
Then

\[
\boxed{\frac{p_{n_N}(Q_N)}{\sqrt{m_N}}\ \Longrightarrow\ Z,\qquad
\mathbb P(Z\in dz)=\pi^{-1}e^{-|z|^2}\,d^2z.}
\tag{1}
\]

For independent uniform phases, repeated on each Kramers pair,

\[
\boxed{\operatorname{Law}_D\left(
\frac{p_{n_N}(DQ_N)}{\sqrt{m_N}}\right)
\ \Longrightarrow\operatorname{Law}(Z)
\quad\text{in probability over the frozen }Q_N.}
\tag{2}
\]

This includes every boundary layer |n_N−N|=o(N), including ones approaching
the critical ratio arbitrarily slowly. Normalization by √N alone would
be wrong in this regime. Precisely, with d_N=|n_N−N|,

\[
m_N\sim\frac N4\log\frac{N}{d_N+1},\qquad m_N/N\longrightarrow\infty.
\tag{3}
\]

At exactly n=N there is also a quantitative statement for characteristic
functions. Write

\[
\chi_{N,Q}(t)=\mathbb E_D
\exp\left(i\operatorname{Re}\frac{\overline t\,p_N(DQ)}{\sqrt{m_N}}\right).
\]

For every fixed T, uniformly on |t|≤T,

\[
\boxed{\mathbb E_Q|\chi_{N,Q}(t)-e^{-|t|^2/4}|^2
\le\frac1{N+1/2}+O_T((\log N)^{-4}).}
\tag{4}
\]

The big-O constant is deterministic and may depend on T. This is a
characteristic-function estimate, not a claimed rate in total variation
or a simultaneous maximum over infinitely many t.

Every fixed conditional moment also converges in L² over Q. More precisely,
if L_N=log[N/(|n_N−N|+1)], W_N=p_{n_N}/√m_N and r is fixed, then

\[
\mathbb E_Q\left|\mathbb E_D|W_N(DQ)|^{2r}-r!\right|^2
=O_r(N^{-1}+L_N^{-4}).
\tag{4a}
\]

Every unbalanced conditional moment is exactly zero, for each Q, by the
uniform global phase. For r=1 the annealed bias in (4a) is exactly zero.

The ensemble Gaussian behavior and its low cumulants were discussed by
Haake–Sommers–Weber (1999). The proof here supplies an all-order bound and
the conditional phase statement. Priority of either formulation has not
been established by the bounded literature search; neither is presented
as a first discovery.

## 1. An all-order finite bound

For integers a,b≥0, a+b≥1, let κ_{a,b} be the mixed cumulant with a copies
of p_n and b copies of its conjugate. Global rotation makes every
unbalanced cumulant vanish: κ_{a,b}=0 if a≠b.

For every fixed integer r≥2 we prove

\[
\boxed{|\kappa_{r,r}(p_n)|\le C_r(N+n^r),\qquad N\ge2, n\ge1.}
\tag{5}
\]

There is no restriction r≤N. Use the already proved finite Pfaffian identity

\[
\log Z(u,v)=\frac12\operatorname{Tr}\log\left(
I+\sum_{a+b\ge1}\frac{u^av^b}{a!b!}B_{(a-b)n}\right),
\qquad
(B_s)_{kl}=\frac{2k-s}{2k}\mathbf1_{l=k-s\in H_N}.
\tag{6}
\]

The coefficient of u^rv^r is a finite sum of words of length at most 2r.
Each shift is an integer multiple of n, has absolute size at most rn,
and a nonzero trace requires total shift zero. Delete zero shifts since
B₀=I. An empty word has trace 2N. In a nonempty closed word, consecutive
coordinates, including the last and first, are different.

One coordinate can consequently be a denominator at most r times: its
occurrences form an independent set on a cyclic word of length at most
2r. Distinct coordinates are separated by at least n.

For starting coordinate k put d(k)=min_j|k+t_j n|≥1/2, where t_j are the
integer offsets visited by the word. Choose one coordinate attaining this
minimum. All other distinct denominator coordinates have absolute value
at least n/2. Their factors have magnitude at most r+1. The chosen
coordinate has multiplicity at most r. Therefore

\[
|\text{word at }k|\le(r+1)^{2r}
\left(1+\frac{rn}{2d(k)}\right)^r.
\]

There are at most 2r distinct offsets. By translation of the half-integer
lattice,

\[
\sum_{k\in H_N}d(k)^{-r}
\le2r\sum_{q\in\mathbb Z+1/2}|q|^{-r}
=4r(2^r-1)\zeta(r)<8r\,2^r.
\tag{7}
\]

Here r≥2 is essential for summability. Using
(1+x)^r≤2^{r−1}(1+x^r) gives the explicit word bound

\[
|\operatorname{Tr}(\text{word})|
\le(r+1)^{2r}2^{r-1}[2N+8r\,r^r n^r].
\tag{8}
\]

The sum of absolute scalar coefficient weights in (6) is the finite number

\[
A_r=\sum_{\ell=1}^{2r}\frac1{2\ell}
[u^rv^r](e^{u+v}-1)^\ell.
\]

Thus (5) holds, for example, with
C_r=(r!)² A_r (r+1)^{2r}2^{r−1}(2+8r r^r).
The bound is deliberately coarse but uniform in N and n. All arguments
use a fixed formal coefficient of finite matrices; no interchange of an
infinite cumulant series with an asymptotic limit is made.

## 2. The critical boundary layer

Eventually 1≤n_N≤2N. The exact mean gives

\[
m_N=\frac{n_N}2+\frac{n_N}4
\sum_{j=d_N}^{N-1}(j+1/2)^{-1}.
\]

Uniformly for 0≤d<N,

\[
\sum_{j=d}^{N-1}(j+1/2)^{-1}
=\log\frac{N}{d+1}+O(1).
\]

This follows by integral comparison for d≥1, and by separating j=0
when d=0. Since d_N=o(N), the logarithm diverges and (3) follows.
Combining (3) and (5), for every fixed r≥2,

\[
\frac{\kappa_{r,r}}{m_N^r}\longrightarrow0.
\]

The normalized κ₁₁ is exactly one, and every unbalanced cumulant is zero.
The finite moment–cumulant identity therefore gives

\[
\mathbb E(p_{n_N}/\sqrt{m_N})^a
(\overline{p_{n_N}}/\sqrt{m_N})^b
\longrightarrow\mathbf1_{a=b}\,a!.
\tag{9}
\]

Second moments give tightness. The higher moment bounds give uniform
integrability of every fixed moment along this sequence. Every limit is
rotation invariant; its squared radius has moments r!, which uniquely
determine the exponential distribution (Carleman's criterion).
That radius and a uniform angle give precisely the complex Gaussian in
(1). This establishes convergence in distribution, beyond checking only
a fourth moment.

## 3. Conditional law under phases

For any bounded continuous g on C, apply the sharp contraction to the
spectral function g(p_{n_N}/√m_N). Its conditional expectation differs
from the CSE expectation in L² by at most
Var_CSE(g)/(N+1/2). Equation (1) identifies the limiting expectation.

Conditional tightness can also be checked quantitatively. Define
V_{N,Q}=E_D|p_{n_N}(DQ)|²/m_N. Then E_Q V_{N,Q}=1 and

\[
\operatorname{Var}_Q V_{N,Q}
\le\frac{1+\kappa_{2,2}/m_N^2}{N+1/2}\longrightarrow0.
\]

With probability tending to one these conditional second moments are at
most two; on that event Markov's inequality uniformly controls tails.
A countable convergence-determining set of bounded continuous tests,
together with this tightness, proves the weak-law statement (2).
One must retain the probability over Q: (2) is not an assertion for every
specified deterministic self-dual matrix.

For fixed r the moment–cumulant formula and (5) give the quantitative
annealed bias E|W_N|²ʳ−r!=O_r(L_N⁻²): the smallest non-Gaussian block is
κ₂₂/m_N²=O(L_N⁻²), and every higher balanced block is O_r(L_N⁻ʳ).
The normalized 4r-th moment stays bounded. Applying the same contraction
to the unbounded but square-integrable spectral test |W_N|²ʳ gives
Var_Q E_D|W_N|²ʳ≤C_r/(N+1/2). Adding the squared bias proves (4a).

## 4. Exact blocks at n=N and a quantitative characteristic function

At n=N all nonzero shifts except ±N vanish: B_s=0 for |s|≥2N−1.
Put q=uv and introduce the entire series

\[
A(q)=\sum_{a\ge0}\frac{q^a}{(a!)^2},\qquad
C(q)=\sum_{a\ge0}\frac{q^a}{a!(a+1)!}.
\]

The matrix in (6) becomes A(q)I+uC(q)B_N+vC(q)B_{−N}.
It splits into N blocks on (k,k−N), k=1/2,3/2,…,N−1/2. If

\[
c_k=\frac{(2k-N)^2}{4k(N-k)}\ge0,
\]

each block determinant equals A(q)²+c_k q C(q)². With its germ
normalized at q=0,

\[
\boxed{\log Z(u,v)=\frac12\sum_{k=1/2}^{N-1/2}
\log\bigl(A(q)^2+c_k q C(q)^2\bigr).}
\tag{10}
\]

This algebraic block factorization is not a factorization into probability
laws of independent random variables.

Direct sums give

\[
\frac12\sum_k(2+c_k)=m_N,\quad
1+c_k=\frac{N^2}{4k(N-k)}\le N,\quad
\sum_k(1+c_k)^2=\frac N4H_1(N)+\frac{N^2}8H_2(N)=O(N^2).
\tag{11}
\]

For |q|(1+c) sufficiently small, uniformly for all c≥0, the series and
the logarithm around one give

\[
\log(A(q)^2+cqC(q)^2)=(2+c)q
+O((1+c)^2|q|^2).
\tag{12}
\]

For example, first bound the remainder in A(q)=1+q+O(q²) and
C(q)=1+O(q) for |q|≤1/4; then use log(1+x)=x+O(x²) for |x|≤1/2.
This proves (12) with an absolute remainder constant.

For the characteristic function of p_N/√m_N, set
u=i\overline t/(2√m_N), v=it/(2√m_N), so q=−|t|²/(4m_N).
Equations (3) and (11) ensure the smallness condition uniformly for
|t|≤T. Equations (10)–(12) now yield

\[
\log\chi_N(t)=-|t|^2/4+O_T((\log N)^{-2}),
\qquad
\chi_N(t)=e^{-|t|^2/4}+O_T((\log N)^{-2}).
\tag{13}
\]

The phase contraction applied to the modulus-one characteristic test has
variance at most 1/(N+1/2). Orthogonality of the centered error and its
deterministic bias gives (4).

## Limits of the conclusion

This is a CSE result at a growing trace order. It supplies neither a joint
limit for an arbitrary number of critical traces, nor a deterministic
quantum-chaos theorem. At a fixed macroscopic ratio different from one,
(5) alone need not make normalized higher cumulants vanish. No such
extension is used here. The same frozen-background restriction applies
to this Gaussian law and to the full local Sine₄ law.
