> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/counter_shrinking_gap_signed_removal.md`. Embedded SHA256: `afde78e7a2e14403792eca9e0d5b92ec4831544fd1e8a79fe4b3fb7a5bdfb9c5`.
> [Thematic guide](../../topics/closure.md).

# All-time signed removal with a shrinking arithmetic compression gap

Date: 21 October 2026. Exact family: `U_N=exp(i tau N A_N) M_N`, with the original fixed `tau=10^(-80)` and every odd dimension satisfying the explicitly stated divisor condition.

## 0. Status and provenance

This manuscript proves a new all-time extension of the arithmetic trace-history exclusion. Its constants remain explicit when the compression gap tends to zero. The resulting application reaches subpolynomial square divisors and removes a class allowing a growing number of character changes. It does not evaluate the remaining trace histories, prove `H_diag`, or construct a counterexample to `H_diag`.

The following frozen sources are used and are not edited:

1. `counter_subpolynomial_comb_quantitative.md`, SHA-256 `3b59bd021e393489cd709073e683a2dec137333e0e657849b0636a9f85f90def`. Its growing-order escape theorem has been independently audited in `audit_growing_order_comb_quantitative.md`, SHA-256 `30a2039b988d49f12960ffb1d27fc72dedc6eefcb38d005d75ebee06c5de17cb`, with verdict proved as written. The older status sentence inside the frozen source is preserved; the separate audit supplies the later status.
2. `../research_round3_2026_10_21/phase_logtime_dispersion_and_missing_modes.md`, SHA-256 `40dd41555520f712b99f7467ed14fd41ff0369db4b44a9b78f21c7f5a8314b4b`, especially its Sections 3--7, containing the fixed analytic graph class and explicit one-step amplitude/error recurrences.
3. `../research_round3_2026_10_21/phase_sparse_character_histories.md`, SHA-256 `8bc8ecddf8b5b684eeff3b31ab9e8f99a864a50413bcbe8b3edd1791f04200bd`, Sections 2--4. The elementary group-average and word estimates are proved again below, and the parameter independence of its translated-product dispersion is checked in Section 4.

The original-family analytic inputs retain the audit gates recorded in those source manuscripts. No missing Heisenberg-time cancellation estimate is introduced as an assumption. The new parameter-dependent summations and their application are fully proved here; this manuscript itself is a new audit candidate.

## 1. Exact decomposition and its parameter-dependent gap

Let `N=d^2 m` be odd, `d>=3`, and define the finite abelian Weyl subgroup

$$
H_d(s,u)=T_N(sN/d,uN/d),\qquad (s,u)\in G_d=(\mathbb Z/d\mathbb Z)^2.
$$

Its Weyl cocycle is trivial, because the symplectic product of two labels is a multiple of `(N/d)^2=Nm`. Its character projections

$$
P_\chi=d^{-2}\sum_{g\in G_d}\overline{\chi(g)}H_d(g)
$$

are orthogonal, sum to the identity, and have rank `m`: all nonidentity Weyl operators have zero trace.

The exact kernel identity

$$
T_N(a,b)M_N=M_NT_N(3a-4b,-2a+3b)
$$

gives `M_N P_chi=P_(S chi) M_N`, where

$$
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},\qquad
\mathsf S\chi=\chi\circ L.
$$

Write `E_N=exp(i tau N A_N)` and define

$$
K=\left(\sum_\chi P_\chi E_NP_\chi\right)M_N,
\qquad R=U_N-K.
\tag{1.1}
$$

For the general estimates in Sections 2--5 suppose that a particular bound

$$
\max_\chi\|P_\chi E_NP_\chi\|\le\rho=1-g,
\qquad 0<g\le\tfrac12
\tag{1.2}
$$

has been proved. Both `g` and `rho` may depend on `N,d`. Orthogonality gives

$$
\|K\|\le\rho,\qquad \|R\|\le1+\rho=2-g.
\tag{1.3}
$$

Section 6 proves (1.2) for an explicit choice `g_N=(log N)^(-1/2)` in the claimed subpolynomial divisor range, using the independently audited growing-order theorem. Thus (1.2) is not left as an unproved hypothesis in that application.

## 2. Pure character histories: complete summation

Put `c_n=Tr K^n` and `p_n=Tr U_N^n`. The only diagonal blocks of `K^n` correspond to characters fixed by `S^n`. Each such block has dimension `m` and norm at most `rho^n`.

For any rationally invertible integer matrix `B`, the kernel of `B` modulo `d` injects into `Z^2/B Z^2`: for an integer representative `x` with `Bx=d y`, map `x` to `y mod B Z^2`. Changing the representative by `d z` changes `y` by `Bz`, and equality of two image classes gives `B(x-x'-dz)=0`, hence equality modulo `d`. Therefore the number of elements in this kernel is at most `|det B|`.

Apply this with `B=(L^T)^n-I`. The eigenvalues of `L` are `lambda=3+2 sqrt(2)` and `lambda^(-1)`, and

$$
|\det(L^n-I)|=\lambda^n+\lambda^{-n}-2\le\lambda^n.
$$

Since there are only `d^2` characters in total,

$$
\frac{|c_n|}{N}\le\rho^n\min\{1,\lambda^n/d^2\}.
\tag{2.1}
$$

Let `x=2 log d/log lambda` and `j=floor(x)`. Since `lambda rho>1`, splitting the sum at `j` gives

$$
\begin{aligned}
\sum_{n\ge1}\rho^n\min\{1,\lambda^n/d^2\}
&\le d^{-2}\frac{(\lambda\rho)^{j+1}}{\lambda\rho-1}
       +\frac{\rho^{j+1}}{g}\\
&\le\left(\frac{\lambda\rho}{\lambda\rho-1}+\frac1g\right)
       \rho^{2\log d/\log\lambda}\\
&\le\frac2g\exp\!\left[-\frac{2}{\log\lambda}g\log d\right].
\end{aligned}
\tag{2.2}
$$

The last numerical bound is uniform for `rho>=1/2`: the first fraction is at most `lambda/(lambda-2)<2`, while `g<=1/2`, and `log(1-g)<=-g`.

For arbitrary complex weights `w_(n,N)` with supremum at most `W`, define each difference before summing. Since `|p_n|<=N` and the right side of (2.1) is at most one,

$$
\begin{aligned}
\frac1{N^2}\left|
\sum_{n\ge1}w_{n,N}\big(|p_n|^2-|p_n-c_n|^2\big)
\right|
&\le3W\sum_{n\ge1}\rho^n\min\{1,\lambda^n/d^2\}\\
&\le\frac{6W}{g}
\exp\!\left[-c_\lambda g\log d\right],
\qquad c_\lambda=\frac2{\log\lambda}.
\end{aligned}
\tag{2.3}
$$

The difference series is absolutely convergent. For nondecaying bounded weights this does not assert that the two individual series converge separately.

An exact sufficient asymptotic criterion is

$$
c_\lambda g_N\log d_N-\log(1/g_N)\longrightarrow+\infty.
\tag{2.4}
$$

In particular, `g_N log d_N / log(1/g_N) -> infinity` suffices when `g_N -> 0`.

## 3. A growing set of histories with character changes

The letters `K` and `R` partition all character transitions: `K` follows `chi -> S chi`, whereas `R` has precisely the complementary blocks. Define

$$
z=\frac{g}{2(2-g)},\qquad r_*=1-\frac g2,\qquad
\delta(g)=\frac{-\log(1-g/2)}{2\log\big(2(2-g)/g\big)},
\qquad \eta=\sqrt{1-g/2}.
\tag{3.1}
$$

Here `0<z<1` and `0<delta(g)<1`. Let `S_n` be the finite sum of all noncommutative words of length `n` in `K,R` containing at most `floor(delta(g)n)` letters `R`, and write `s_n=Tr S_n`.

Using (1.3), `z^j>=z^(delta(g)n)` for the retained values of `j`, and `rho+z(2-g)=r_*`,

$$
\begin{aligned}
\|S_n\|
&\le\sum_{j\le\lfloor\delta(g)n\rfloor}
\binom nj\rho^{n-j}(2-g)^j\\
&\le z^{-\delta(g)n}\big(\rho+z(2-g)\big)^n
=\eta^n.
\end{aligned}
\tag{3.2}
$$

Thus `|s_n|<=N eta^n`. This has already summed all placements of the allowed changes, including histories that later return to a previously visited character. It is not an estimate on one selected word.

## 4. The short-time constants are independent of the shrinking gap

Finite character orthogonality proves the exact identity

$$
\sum_\chi P_\chi E_NP_\chi
=d^{-2}\sum_{g_0\in G_d}H_d(g_0)E_NH_d(g_0)^*.
\tag{4.1}
$$

The symbol `g_0` here denotes a group element and is unrelated to the real gap `g`. Put

$$
U_{g_0,N}=H_d(g_0)E_NH_d(g_0)^*M_N.
$$

Then `K` is the exact average of these matrices and `R=U_(0,N)-K`. A word with `j` occurrences of `R` is therefore a signed linear combination of products of translated unitaries, with total absolute coefficient at most `2^j`. Consequently the total absolute coefficient for `S_n` is at most

$$
\sum_{j\le\lfloor\delta(g)n\rfloor}\binom nj2^j\le3^n.
\tag{4.2}
$$

This bound is independent of `delta(g),g,r,d,N` and of the group cardinality. No averaging of the spectral statistic or of the original kick is performed.

To check the analytic constants used with (4.2), write `H_d(g_0)=T_N(a_0,b_0)`. The exact Weyl conjugation law multiplies the `(k,l)` Fourier coefficient of `A_N` by `e_N(a_0 k-b_0 l)`. In the ordinary-half quantization of the dispersion source, the symbol becomes

$$
a_{g_0}(q,p)=a(q+a_0/N,p-b_0/N).
\tag{4.3}
$$

The real translations leave the Fourier support `|k|<=9, |l|<=1`, all coefficient absolute values, and all strip derivative bounds unchanged. In particular, on the fixed complex tube in that proof, the Hamiltonian field satisfies the same bounds `|Y_q|<3`, `|Y_p|<30`. The linear metaplectic step is exactly the same for each factor.

Here is why arbitrary changes of the translation at each step do not alter the iteration constant. The dispersion proof constructs, after a step, leading amplitudes in a fixed analytic graph class; the linear step restores its strip before every translated kick. The one-step maps satisfy

$$
\mathcal A_{n+1}\le A_0\mathcal A_n,\qquad
\|\text{new error at step }n+1\|_2\le C_0 h\mathcal A_n,
\qquad h=(2\pi N)^{-1},
\tag{4.4}
$$

where `mathcal A_n` is the sum of the leading amplitude `C^4` norms. The suprema defining `A_0,C_0` depend only on the fixed graph class, support, derivative bounds, chart cutoffs, and the fixed finite Poisson set. By (4.3) all of these bounds are unchanged for every translated kick. The first step is the same exact application of `M_N` followed by a kick in this class. Old errors propagate by exact unitary matrices, including when the sequence of translations changes. Hence (4.4) holds with the same constants for every sequence. Choosing any fixed `A_*>max(2,A_0)` and summing the geometric error recurrence proves

$$
\max_{x,y}|(U_{g_n,N}\cdots U_{g_1,N})_{xy}|
\le C_*A_*^n N^{-1/2}.
\tag{4.5}
$$

The constants `C_*,A_*` depend only on the original symbol and `tau`, not on `r,rho,g,d,N,n` or the translation sequence. The right side may exceed one for large `n`, which does not invalidate the bound. Taking the trace and using (4.2), with the fixed number `B=3A_*>1`, gives

$$
\frac{|s_n|}{N}\le C_*N^{-1/2}B^n.
\tag{4.6}
$$

Thus the dependence on the arithmetic escape order appears only through `g,delta(g),eta`, and does not enter `B` or `C_*`.

## 5. Uniform all-time signed estimate

Put `q_n=p_n-s_n`. Combining (3.2) and (4.6),

$$
\frac{|s_n|}{N}\le a_n:=\min\{C_*N^{-1/2}B^n,\eta^n\}\le1.
$$

The elementary square identity gives the pointwise bound

$$
N^{-2}\big||p_n|^2-|q_n|^2\big|\le2a_n+a_n^2\le3a_n.
\tag{5.1}
$$

This controls the full cross-term against the retained trace `q_n` without estimating `q_n` separately. Let `L_N=log N` and `n_0=floor(L_N/(4 log B))`. A direct summation, with no fixed-gap dominated convergence, gives

$$
\begin{aligned}
\sum_{n\ge1}a_n
&\le C_*N^{-1/2}\sum_{n=1}^{n_0}B^n
       +\frac{\eta^{n_0+1}}{1-\eta}\\
&\le\frac{C_*B}{B-1}N^{-1/4}
       +\frac4g\exp\!\left[-\frac{g\log N}{16\log B}\right].
\end{aligned}
\tag{5.2}
$$

For the second term, `log eta=(1/2)log(1-g/2)<=-g/4`, `n_0+1>L_N/(4 log B)`, and `1-eta=(g/2)/(1+eta)>=g/4`.

Therefore, uniformly for all complex weight arrays with supremum at most `W`,

$$
\boxed{
\frac1{N^2}\left|
\sum_{n\ge1}w_{n,N}\big(|p_n|^2-|p_n-s_n|^2\big)
\right|
\le3W\left[
C_BN^{-1/4}+\frac4g e^{-c_Bg\log N}
\right],
}
\tag{5.3}
$$

where `C_B=C_*B/(B-1)` and `c_B=1/(16 log B)` are fixed independently of the arithmetic parameters. As in Section 2, the difference series converges absolutely at every dimension, even for bounded nondecaying weights.

The exact sufficient asymptotic criterion delivered by this bound is

$$
c_Bg_N\log N-\log(1/g_N)\longrightarrow+\infty.
\tag{5.4}
$$

When `g_N->0`, the stronger scale condition `g_N log N / log(1/g_N)->infinity` is convenient and independent of the numerical value of `B`. One must not omit `c_B` in (5.4): the statement `g_N log N-log(1/g_N)->infinity` alone need not imply this particular sufficient condition.

For the exact pair factorial expression, choose `w_(n,N)=|bhat(n/N)|^2`; the negative-index term is its complex conjugate and the prefactor `1/2` cancels the two signs. Thus (5.3) is exactly the change in the pair functional when `p_n` is replaced by `p_n-s_n` for positive and negative `n`, keeping the zero-index term and the subtraction of `N` unchanged. The same bound applies to the complete infinite Abel weight `exp(-2sn/N)`, for every fixed `s>0`.

These modified traces are explicit sums of retained histories; no claim is made that they are the traces of a new unitary spectrum.

## 6. An explicit subpolynomial divisor range for the original family

The independently audited growing-order theorem supplies fixed `C_0,C_1>0`, with `C_1>=1` after harmless enlargement, such that if

$$
\log N\ge C_0r^3,\qquad d\ge N^{1/r},
$$

then

$$
\|P_\psi E_NP_\chi\|
\le\sqrt{1-\exp[-2C_1r\log(r+1)]}
\tag{6.1}
$$

for every pair of characters. Only the diagonal case is needed here.

Write

$$
L=\log N,\qquad \ell=\log L,\qquad \ell_2=\log\ell,
\qquad c=\frac1{16C_1},\qquad
r_N=\left\lfloor c\frac{\ell}{\ell_2}\right\rfloor.
\tag{6.2}
$$

All subsequent assertions are for sufficiently large `N`, so that `ell_2>0` and `r_N>=2`. Then

$$
r_N\ge\frac c2\frac\ell{\ell_2},\qquad
r_N\log(r_N+1)\le2c\ell,
\qquad C_0r_N^3\le L.
\tag{6.3}
$$

The first inequality follows from the floor once its argument is at least two. The second follows from `r_N<=c ell/ell_2` and `log(r_N+1)<=2 ell_2` for large `N`. The last follows from `r_N^3=O(ell^3)` and `L=exp(ell)`.

Set `D=2/c=32C_1`. For every allowed odd dimension and square divisor with

$$
\boxed{
\log d\ge D\frac{\log N\,\log\log\log N}{\log\log N},
}
\tag{6.4}
$$

we have `log d>=L/r_N`. Thus all hypotheses of (6.1) hold. Its squared escape lower bound is at least

$$
\exp[-2C_1r_N\log(r_N+1)]\ge L^{-1/4}.
$$

Using `1-sqrt(1-x)>=x/2` and increasing the fixed threshold so that `L>=16`, the resulting compression gap is at least

$$
\frac12L^{-1/4}\ge L^{-1/2}.
\tag{6.5}
$$

We may therefore use the explicit weaker gap and norm bound

$$
g_N=L^{-1/2},\qquad \rho_N=1-L^{-1/2}
\tag{6.6}
$$

throughout Sections 2--5. This is an upper bound on the compression norm of the original kick, and does not change that kick or `tau`.

The two all-time signed error bounds become

$$
\begin{aligned}
\text{pure histories: }&
6W L^{1/2}\exp\!\left[-c_\lambda D L^{1/2}\frac{\ell_2}{\ell}\right]
\longrightarrow0,\\
\text{histories in }S_n\text{: }&
3WC_BN^{-1/4}
 +12W L^{1/2}\exp[-c_B L^{1/2}]
\longrightarrow0.
\end{aligned}
\tag{6.7}
$$

All constants and thresholds are independent of the choice of divisor satisfying (6.4). Both limits follow by comparing their negative exponents with `(1/2)log L=(1/2)ell`.

The allowed density of deviations is explicitly `delta_N=delta(g_N)`. As `N->infinity`,

$$
\delta_N\sim\frac{g_N}{4\log(4/g_N)}
\sim\frac1{2\sqrt{\log N}\,\log\log N}.
\tag{6.8}
$$

Thus at times `n` comparable to `N`, the removed class allows approximately `n/(2 sqrt(log N) loglog N)` changes. This number tends to infinity, while its fraction of `n` tends to zero. No fixed positive deviation density is claimed in this subpolynomial range.

Condition (6.4) is subpolynomial because its lower bound for `log d/log N` tends to zero. It includes actual infinite sequences. For example take `N_k=7^(2k)` and

$$
d_k=7^{\lceil A k\log\log k/\log k\rceil}
$$

with any sufficiently large fixed `A>2D`. For large `k` the exponent is at most `k`, so `d_k^2` divides `N_k`; moreover (6.4) holds because `loglog N_k~log k` and `logloglog N_k~loglog k`. Here `d_k=N_k^{o(1)}`.

## 7. What the larger subpolynomial range gives, and what it does not

The growing-order escape theorem also reaches `log d>=C(log N)^(2/3)`, with a guaranteed norm gap of order

$$
g_N=\exp[-O((\log N)^{1/3}\log\log N)]=N^{-o(1)}.
\tag{7.1}
$$

The gap one inserts from that bound may satisfy `g_N log N->0`. In this situation the complete majorants in Sections 2 and 5 do not tend to zero. This is a failure of these majorants, not a spectral counterexample.

There is nevertheless a valid late-time conclusion. For any fixed `a>0`, using only `|s_n|/N<=eta_N^n` gives

$$
\frac1{N^2}\left|
\sum_{n>\lfloor N^a\rfloor}w_{n,N}
\big(|p_n|^2-|p_n-s_n|^2\big)\right|
\le\frac{12W}{g_N}\exp[-g_NN^a/4]
\longrightarrow0
\tag{7.2}
$$

whenever `g_N=N^{-o(1)}`. Indeed `g_NN^a=N^{a-o(1)}` dominates `log(1/g_N)=o(log N)`. The analogous pure-history tail is at most `3W g_N^(-1)exp[-g_N N^a]`.

It would be incorrect to promote (7.2) to an all-time conclusion. More precisely, if `g_N->0` and `g_N log d_N->0`, the pure majorant has the lower bound

$$
\sum_{n\ge1}\rho_N^n\min\{1,\lambda^n/d_N^2\}
\ge\frac{\rho_N^{\lfloor2\log d_N/\log\lambda\rfloor+1}}{g_N}
\sim\frac1{g_N}.
\tag{7.3}
$$

Likewise, if `g_N log N->0`, let

$$
J_N=\left\lceil
\frac{\log(\sqrt N/C_*)}{\log(B/\eta_N)}
\right\rceil.
$$

For every `n>=J_N`, the minimum in Section 5 equals `eta_N^n`. Since `J_N=O(log N)`,

$$
\sum_{n\ge1}\min\{C_*N^{-1/2}B^n,\eta_N^n\}
\ge\frac{\eta_N^{J_N}}{1-\eta_N}
\sim\frac4{g_N}.
\tag{7.4}
$$

These exact lower bounds explain why splitting at `N^a` alone does not remove the unestimated early interval. In the actual pair normalization, the worst cross-term is bounded by `|s_n|/N`, not by `|s_n|/N^2`; there is no extra factor `1/N` remaining after using `|p_n|<=N`.

## 8. Boundary of the new result

The original family admits the all-time exclusions (6.7) under the genuine subpolynomial divisor condition (6.4), with the explicit growing allowance (6.8). The broader range (7.1) yields the late-time exclusion (7.2) and microquasimode exclusion from the preceding audited theorem, but not the complete signed correction by this argument.

Even in (6.4), the retained traces contain all histories with more than the shrinking fraction `delta_N` of character changes. Their weighted products are not compared to CUE here. The first outstanding estimate in the pair problem remains the CUE comparison for that retained coherent sum; all higher fixed factorial orders required by `H_diag` remain outstanding as well.

