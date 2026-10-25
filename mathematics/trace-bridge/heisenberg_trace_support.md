# Corrected supporting identities for the submitted Heisenberg route

Date: 30 September 2026. Status: exact identities and conditional estimates,
with author check. These complete useful supporting arguments from
the uploaded note; they do not establish its model-specific CUE input.
The [audit](../../record/heisenberg_note_review_20260930.md) distinguishes
prior repository results from these expository completions.

## 1. A cycle formula for the finite Haar-CUE factorial benchmark

Let $D_N(m)=\sum_{j_1,\ldots,j_k\ {\rm distinct}}
e^{2\pi i\sum_a m_a\theta_{j_a}}$, with integer modes and eigenphases
in $\mathbb R/\mathbb Z$. For a cycle $C=(a_1\ldots a_\ell)$ of a
permutation $\sigma$, put $s_0=0$, $s_j=\sum_{t=1}^j m_{a_t}$ and
$R_C=\max_{0\le j<\ell}s_j-\min_{0\le j<\ell}s_j$. Then
$$
\mathbb E_{\rm CUE} D_N(m)
=\sum_{\sigma\in S_k}\operatorname{sgn}\sigma
\prod_{C\in\operatorname{Cyc}\sigma}
1_{\{\sum_{a\in C}m_a=0\}}(N-R_C)_+.                       \tag{1}
$$
This is a finite consequence of the standard CUE determinant density
already used in [the maintained reference](../../supplement/fixed_map/report-audit/cue_reference.md),
not a universality theorem for $U_N$.

Expand that density as $\sum_\sigma\operatorname{sgn}\sigma
\prod_a K_N(x_a-x_{\sigma(a)})$, with
$K_N(x)=\sum_{r=0}^{N-1}e^{2\pi irx}$, and integrate against the
specified modes. On each cycle, Fourier orthogonality requires zero
total mode. The frequency labels are then determined by one integer
label and successive partial sums. Requiring every label to lie in
$[0,N-1]$ leaves exactly $(N-R_C)_+$ choices. Distinct cycles have
independent labels, proving (1), including zero modes, resonant proper
subsets, and $k>N$ (where the determinant is zero).
If no proper nonempty subset has zero sum and the total sum is zero,
only $k$-cycles survive; a nonzero total sum makes the whole expression
zero. Omitting these resonance contributions would give a wrong all-order
benchmark.

For every finite unitary spectrum one also has
$$
D_N(m)= [t_1\cdots t_k]\det\left(I+\sum_a t_a U^{m_a}\right).
$$
The product over eigenindices proves this by selecting one distinct
index for each label. For a partition $\pi$ and $\sum_a m_a=0$, put
$R_{a,\pi}=U^{(B(a))}(U^{(B(k))})^{-1}$ on the tensor product with
one factor per block. The factors commute, and
$\operatorname{Tr}\prod_{a<k}R_{a,\pi}^{m_a}
=\prod_{B\in\pi}p_{\sum_{a\in B}m_a}$.
These identities are equivalent representations of the existing
[partition--Möbius bridge](trace_to_local_statistics_bridge.md).

## 2. Smooth-sector Fejér estimate with the necessary error budget

Let $U_N$ be unitary, $A_N$ any matrix, $c_n$ any scalar comparison
sequence with $\sum_{n\in\mathbb Z}|c_n|\le C_a$, and assume
$$
N^{-1}\operatorname{Tr}(A_N^*U_N^n A_N U_N^{-n})=c_n+e_{N,n},
\quad |n|<M.
$$
If $CM/N\le1/2$, then
$$
Q_{N,C}:=N^{-1}\sum_{d_{\mathbb T}(\theta_j-\theta_l,0)\le C/N}
|(A_N)_{jl}|^2
\le\frac{\pi^2}{4M}\left(C_a+\sum_{|n|<M}|e_{N,n}|\right). \tag{2}
$$
Indeed $F_M(t)=M^{-1}|\sum_{r=0}^{M-1}e^{2\pi irt}|^2\ge0$,
and $F_M(t)\ge4M/\pi^2$ on $d_{\mathbb T}(t,0)\le1/(2M)$.
Expanding the trace in an eigenbasis turns its Fejér-weighted sum into
$N^{-1}\sum_{jl}|(A_N)_{jl}|^2F_M(\theta_j-\theta_l)$.
Positivity permits discarding the other terms; the triangle inequality
then proves (2).

For a smooth mean-zero symbol $a$, the intended $c_n$ are classical
correlations. If they are summable and the logarithmic-time trace/Egorov
error has the quantitative bound $|e_{N,n}|\le C_aN^{-\rho}e^{\Gamma|n|}$,
then $M=\lfloor c\log N\rfloor$, $c\Gamma<\rho$, gives
$Q_{N,C}=O_a(1/\log N)+O_a(N^{-\rho+c\Gamma})$.
Uniform $e_{N,n}=o(1)$ alone gives only $O_a(1/\log N)+o(1)$.
This conditional implication repairs the submitted summation argument.
No new source-to-model Egorov or mixing theorem is claimed here.
These weights concern one fixed observable; they do not count eigenphase
pairs in the entire Hilbert--Schmidt space.

## 3. Near-unitary transfer at Heisenberg times

Let $U_N$ be unitary and $V_N$ an $N\times N$ matrix with
$\|U_N-V_N\|\le\varepsilon_N<1/2$. Then $V_N$ is invertible and
$$
\|V_N\|\le1+\varepsilon_N,\quad
\|V_N^{-1}\|\le(1-\varepsilon_N)^{-1},\quad
|\operatorname{Tr}(V_N^m-U_N^m)|
\le2N|m|\varepsilon_N e^{2|m|\varepsilon_N}                 \tag{3}
$$
for every integer $m$. The positive case is telescoping; the negative
case uses $\|V_N^{-1}-U_N^{-1}\|\le\varepsilon_N/(1-\varepsilon_N)$
and the same telescoping identity. Thus no separate unitarity of $V_N$
is needed. The powers are controlled by their closeness to a unitary.

For fixed $k\ge2$, compactly supported bounded Fourier weights,
$|m_a|\le C_kN$, $\sum_a m_a=0$, and
$\varepsilon_N=O(N^{-K})$ with $K>k$, the normalized weighted
distinct-index statistics differ by $O(N^{k-K})$.
Here the distinct-index expression for $V_N$ can be defined by the
partition--Möbius polynomial in its traces. A partition with $b$ blocks
has a product of $b$ traces. Telescoping the product using (3) bounds
the difference by $C_k N^{b+1}\varepsilon_N$; the exponential factors
are bounded since $N\varepsilon_N\to0$. There are $O(N^{k-1})$
integer mode vectors in the support. Multiplying by the normalization
$N^{-k}$ gives $O(N^b\varepsilon_N)$, at worst $O(N^{k-K})$.
Every fixed $k$ therefore transfers under a superpolynomial norm error.

For a natural quantization $\mathcal F_N$, one must actually construct
$V_N=B_N\mathcal F_N B_N^{-1}$ and prove this error for the same family
at every order. If $B_N$ is unitary, source norm estimates transfer
unchanged; a general isomorphism requires control of its condition number.
No such all-order identification is obtained from the finite-power
comparison in Faure--Tsujii's Theorem 1.69. Even a completed transfer
would leave the long-time periodic-orbit cancellation and every higher
joint-trace estimate to prove. Pair cancellation alone also does not
supply the CUE plateau or higher correlations.

## 4. Exact Weyl convention repair

For the ordinary Fourier coefficients $\widehat g(n,m)$,
$$
A_N=\sum_{n,m}\widehat g(n,m)W_N(m,n)
=\sum_{n,m}(-1)^{nm}\widehat g(n,m)T_N(m,n).
$$
Keeping $\widehat g$ while changing $W$ to raw modular $T$ omits a sign.
In the maintained raw convention,
$T(a,b)T(c,d)=e_N(2^{-1}(ad-bc))T(a+c,b+d)$ and
$M_NT(a,b)M_N^*=T(3a+4b,2a+3b)$.
These identities fix both the commutator and the metaplectic transport;
the index pair is (translation, modulation), not (q frequency, p frequency).
The corrected 32-neighbor commutator representation is exact, but its
exponential is not a scalar multiplication by the translated symbol.
