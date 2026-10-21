> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/phase_sparse_character_histories.md`. Embedded SHA256: `8bc8ecddf8b5b684eeff3b31ab9e8f99a864a50413bcbe8b3edd1791f04200bd`.
> [Thematic guide](../../topics/arithmetic.md).

# A signed estimate for histories with a small positive density of arithmetic character changes

Research continuation, 21 October 2026.

**Status.** For the original matrices, in the odd dimensions $N=d^2m$ with $m\le\sqrt N$, this note removes an exponentially large class of mixed character histories from the entire pair-trace functional, including its cross-term against the remaining trace. The class permits up to $\epsilon n$ deviations from the unperturbed character permutation at time $n$, where $\epsilon>0$ is fixed. The resulting correction is $o(1)$; with the explicit exponential dispersion budget, it is $O(N^{-\beta})$ for a fixed $\beta>0$. Neither a random-phase assumption nor a replacement spectral ensemble is used.

The remaining histories have a positive density of those deviations. Their coherent trace sum is not evaluated, so the original pair discrepancy and $H_{\rm diag}$ remain unresolved.

## 1. Verified inputs and their status

Use the complete character decomposition $I=\sum_\chi P_\chi$ and the character permutation $\mathsf S\chi=\chi\circ L$, with

$$
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},
$$

as defined and checked in *phase_all_character_signed_trace_removal.md*.

The analytic input is the uniform arithmetic escape estimate

$$
\|P_\chi E_NP_\chi\|\le\rho<1,
\qquad E_N=e^{i\tau NA_N},
\qquad
\rho=\sqrt{4095/4096},
\tag{1}
$$

for all characters and all allowed $N,d$ with $N\ge10^{140}$.
This stronger numerical gap is proved in
*arithmetic_comb_rescaled_gap.md*, Sections 1--3, snapshot SHA-256
898528107bfc2691c0f17fe6d8a096592c46de537b045c6bbc41949d0f3bfd2f.
It changes an auxiliary translation step in the proof and leaves the original $\tau=10^{-80}$ unchanged. That manuscript records its exact-operator input and independent audit source.

The quantitative estimate also uses the exponential kernel budget in
*phase_logtime_dispersion_and_missing_modes.md*, SHA-256
40dd41555520f712b99f7467ed14fd41ff0369db4b44a9b78f21c7f5a8314b4b.
Section 4 below verifies explicitly its uniform extension to the translated, time-dependent kicks needed here.
The independent audit gates of those analytic manuscripts remain attached to these inputs. The word estimate, exact group average, and summation argument below introduce no further unproved cancellation claim.

## 2. Allowed and forbidden character transitions

Define

$$
K_N=\sum_\chi P_{\mathsf S\chi}U_NP_\chi
=\left(\sum_\chi P_\chi E_NP_\chi\right)M_N,
\qquad R_N=U_N-K_N.
\tag{2}
$$

The exact Egorov identity for $M_N$ proves the equality in (2).
The orthogonality of the character decomposition and (1) give

$$
\|K_N\|\le\rho,\qquad
\|R_N\|\le1+\rho.
\tag{3}
$$

For each integer $n\ge1$, expand

$$
U_N^n=(K_N+R_N)^n
\tag{4}
$$

as its finite sum of noncommuting words. In any such word, $K_N$ has only blocks $\chi\to\mathsf S\chi$, whereas $R_N$ has exactly the complementary blocks. Hence, after inserting the character projections, a word containing $j$ occurrences of $R_N$ sums precisely the character histories with $j$ transitions that fail to follow $\mathsf S$. This is a disjoint finite partition of the trace histories; no probability law is associated with the words.

Set the fixed constants

$$
z=\frac{1-\rho}{2(1+\rho)},\qquad
r_*=\frac{1+\rho}{2},\qquad
\epsilon=\frac{-\log r_*}{2\log(1/z)},\qquad
\eta=\sqrt{r_*}.
\tag{5}
$$

Here $0<z<1$, $0<\epsilon<1$, and $\eta<1$.
Define the concrete finite operator sum

$$
S_{n,N}
=\sum_{\substack{\text{words of length }n\text{ in }K_N,R_N\\
                  \#R_N\le\lfloor\epsilon n\rfloor}}
       \text{word}.
\tag{6}
$$

It includes pure permutation histories and all mixed histories with at most the indicated positive density of deviations, including histories that leave a character-permutation orbit and later return.

Using (3), and then $z^j\ge z^{\epsilon n}$ for $j\le\epsilon n$, gives

$$
\begin{aligned}
\|S_{n,N}\|
&\le \sum_{j\le\lfloor\epsilon n\rfloor}
 \binom nj \rho^{n-j}(1+\rho)^j\\
&\le z^{-\epsilon n}
   \sum_{j=0}^n\binom nj \rho^{n-j}
        \big(z(1+\rho)\big)^j\\
&=\left[z^{-\epsilon}\big(\rho+z(1+\rho)\big)\right]^n\\
&=\eta^n.
\end{aligned}
\tag{7}
$$

The last equality uses
$\rho+z(1+\rho)=r_*$ and
$z^{-\epsilon}r_*=\sqrt{r_*}$.
Thus

$$
\boxed{\displaystyle
|s_{n,N}|:=|\operatorname{Tr}S_{n,N}|\le N\eta^n.}
\tag{8}
$$

Unlike a bound for one selected word, (7) has already summed all placements and all numbers of deviations up to $\epsilon n$.

## 3. The exact group average is only an identity inside the proof

Let $G=(\mathbb Z/d\mathbb Z)^2$, and let $T_G(g)$ be the commuting Weyl representation used to define $P_\chi$.
Finite character orthogonality proves

$$
\sum_\chi P_\chi E_NP_\chi
=\frac1{|G|}\sum_{g\in G}T_G(g)E_NT_G(g)^*.
\tag{9}
$$

Indeed, on a block $P_\chi E_NP_\psi$, the right-hand side multiplies by
$|G|^{-1}\sum_g\chi(g)\overline{\psi(g)}
=\mathbf1_{\chi=\psi}$.

Put

$$
U_{g,N}=T_G(g)E_NT_G(g)^*M_N.
$$

Then

$$
K_N=\frac1{|G|}\sum_g U_{g,N},
\qquad U_N=U_{0,N},
\qquad R_N=U_{0,N}-\frac1{|G|}\sum_gU_{g,N}.
\tag{10}
$$

Equation (10) does not average the spectral statistic in the original task. It is an exact algebraic representation of operators that already occur in the deterministic partition (4).

For any fixed placement of $j$ letters $R_N$, expansion using (10) is a signed linear combination of products
$U_{g_n,N}\cdots U_{g_1,N}$, with total absolute coefficient at most $2^j$.
Consequently the entire $S_{n,N}$ is such a linear combination with total absolute coefficient at most

$$
\sum_{j\le\lfloor\epsilon n\rfloor}\binom nj2^j\le3^n.
\tag{11}
$$

The bound is independent of $|G|$: each exact finite group average has total absolute coefficient one.

## 4. Uniform dispersion for the translated products

Write $T_G(g)=T_N(a_g,b_g)$.
The exact Weyl multiplication law gives

$$
T_N(a_g,b_g)T_N(l,k)T_N(a_g,b_g)^*
=e_N(a_gk-b_gl)T_N(l,k).
\tag{12}
$$

Thus $T_G(g)A_NT_G(g)^*$, in the ordinary-half quantization of the dispersion proof, has the symbol

$$
a_g(q,p)=a(q+a_g/N,p-b_g/N).
\tag{13}
$$

It is real and has the same finite Fourier support
$|k|\le9,\ |l|\le1$, the same coefficient absolute values, and the same coefficient sum bound $<2$.
All analytic derivative bounds of the dispersion proof are therefore uniform in $g$.

The proof in that manuscript applies step by step to the product
$U_{g_n,N}\cdots U_{g_1,N}$, even when the translations change at every step:

1. The initial application of $M_N$ to a coordinate vector is the same exact finite quadratic-phase decomposition.
2. Every translated kick has the same complex field bounds $|Y_q|<3$, $|Y_p|<30$ on the fixed complex tube. It therefore preserves the same analytic graph class after the linear step restores the strip.
3. The amplitude transport and finite-shift Taylor remainders depend only on these fixed Fourier and graph bounds, so their constants do not depend on the selected translations.
4. The linear step, its finite Poisson set, and the amplitude branch budget are unchanged.
5. Every factor is exactly unitary; old error vectors therefore propagate without norm growth, just as in the original recurrence.

Hence there are fixed finite $C_*,A_*$, $A_*\ge2$, independent of $N,n$ and of the full translation sequence, such that

$$
\boxed{\displaystyle
\max_{x,y}
 |(U_{g_n,N}\cdots U_{g_1,N})_{xy}|
\le C_* A_*^n N^{-1/2}.}
\tag{14}
$$

This is an application of the explicit uniform one-step bounds and recurrence, not a formal extension of an unquantified fixed-time theorem.
Taking a trace and then using the exact coefficient bound (11) gives, with $B=3A_*>1$,

$$
\boxed{\displaystyle
|s_{n,N}|\le C_*\sqrt N\,B^n.}
\tag{15}
$$

Only the fixed-$n$ consequence $s_{n,N}/N\to0$ is needed for the qualitative result below. The exponential dependence in (15) yields its explicit power rate.

## 5. Complete signed summation, with no cutoff

Set

$$
p_{n,N}=\operatorname{Tr}U_N^n,\qquad
q_{n,N}=p_{n,N}-s_{n,N}.
$$

The second expression is exactly the sum of all trace histories with more than $\lfloor\epsilon n\rfloor$ deviations.

For any bounded $w:[0,\infty)\to\mathbb C$, define

$$
\mathcal E_{N,w}
=\frac1{N^2}\sum_{n\ge1}w(n/N)
 \left(|p_{n,N}|^2-|q_{n,N}|^2\right).
\tag{16}
$$

As in the pure-character result, the difference series is absolutely convergent for every bounded weight. For compactly supported or exponentially decaying weights it equals the difference of the two individual series. No assertion of individual convergence is made for bounded nondecaying weights.

From (8), (15), and $|p_{n,N}|\le N$, put

$$
a_{n,N}=\min\{C_*N^{-1/2}B^n,\eta^n\}\le1.
$$

The exact square difference then satisfies

$$
\frac1{N^2}
 \left||p_{n,N}|^2-|p_{n,N}-s_{n,N}|^2\right|
\le 2a_{n,N}+a_{n,N}^2\le3a_{n,N}.
\tag{17}
$$

For each fixed $n$, $a_{n,N}\to0$, and
$\sum_n\eta^n<\infty$.
Thus dominated convergence already proves

$$
\mathcal E_{N,w}=o(1),
\tag{18}
$$

uniformly over bounded weights with a common supremum bound. It also proves the same statement if (14) is only used at each fixed time with a finite uniform-in-translation constant $C_n$; no growing-time claim is needed for this qualitative conclusion.

For the quantitative bound define

$$
\beta=\frac{-\log\eta}{2\log(B/\eta)}>0,\qquad
L_N=\left\lfloor
 \frac{\log(\sqrt N/C_*)}{\log(B/\eta)}
\right\rfloor.
$$

For all sufficiently large $N$, $L_N\ge0$, and

$$
\begin{aligned}
\sum_{n\ge1}a_{n,N}
&\le C_*N^{-1/2}\sum_{n=1}^{L_N}B^n
       +\sum_{n>L_N}\eta^n\\
&\le \eta^{L_N}
 \left[\frac B{B-1}+\frac\eta{1-\eta}\right]\\
&\le \eta^{-1}C_*^{2\beta}N^{-\beta}
 \left[\frac B{B-1}+\frac\eta{1-\eta}\right].
\end{aligned}
$$

Together with (17), this gives the explicit signed estimate

$$
\boxed{\displaystyle
|\mathcal E_{N,w}|
\le
3\|w\|_\infty\,\eta^{-1}C_*^{2\beta}
 \left[\frac B{B-1}+\frac\eta{1-\eta}\right]N^{-\beta}.}
\tag{19}
$$

The exponent and constants are independent of dimension and divisor and depend on the fixed dispersion budget. No sharpness of this rate is claimed. The value of $A_*$ was proved finite rather than numerically optimized, so no numerical value of $\beta$ is asserted.

## 6. Application and exact boundary

For $w(\xi)=|\widehat b(\xi)|^2$, substitute $q_{n,N}$ for $p_{n,N}$ in the exact pair factorial formula, leaving the $n=0$ term and the subtraction of $N$ unchanged. Equation (19) bounds the change by $O_b(N^{-\beta})$.
The same estimate covers the exponential weight $e^{-2s\xi}$, including its infinite tail.

The resulting expression is an algebraic functional of the remaining exact trace histories. It is not claimed to be a point-process moment of a new unitary matrix.
The estimate includes the full cross-term between the discarded histories and their complement.

At times $n\asymp N$, every remaining history has at least a fixed positive fraction $\epsilon$ of transitions away from $\chi\mapsto\mathsf S\chi$. This conclusion is stronger than excluding only the pure permutation paths or a fixed finite number of deviations. It still does not estimate the phase cancellation within the remaining dense-transition class, compare it to CUE, or control any higher factorial order. That coherent sum is the outstanding obstruction.

