> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/phase_dense_transition_attempt.md`. Embedded SHA256: `db6fe94135f7afbadfa358698c4bb671210da38c785e522348939a56bc579993`.
> [Thematic guide](../../topics/histories.md).

# Executed estimate tests for the remaining dense character histories

Research continuation, 21 October 2026.

**Status.** The sparse-history theorem has removed a complete exponentially large class of exact histories, with a signed pair error tending to zero. This note executes the next estimates on its complement. The all-block norm gap, exact unitarity identities, Hilbert--Schmidt summation, and analytic generating function do not produce an $O(1)$ pair bound or the required CUE limit for that complement. The concrete failure factors are given below. No impossibility theorem about other trace arguments is claimed.

## 1. Exact setting and the stronger all-block estimate

In the dimensions $N=d^2m$, $m\le\sqrt N$, $N\ge10^{140}$, let

$$
Q=d^2,\qquad m=N/Q,
$$

so there are $Q$ orthogonal character sectors of equal dimension $m$.
The independently checked rescaled word estimate proves

$$
\|P_\psi E_NP_\chi\|\le\rho=\sqrt{4095/4096}<1
\quad\text{for every }\chi,\psi.
\tag{1}
$$

This all-pairs extension is Section 3.1 of
*arithmetic_comb_rescaled_gap.md*, SHA-256
898528107bfc2691c0f17fe6d8a096592c46de537b045c6bbc41949d0f3bfd2f.
Its proof normalizes $R$ and $E_N^*RE_N$ by the possibly different input and output character phases; the commutator is unchanged and the same error estimate holds. Since $M_N$ permutes character spaces, (1) also gives

$$
\|P_\psi U_NP_\chi\|\le\rho
\quad\text{for every }\chi,\psi.
\tag{2}
$$

Thus no individual character transition can nearly preserve the entire norm of its input vector. This is stronger than the permitted-permutation block estimate, but it remains an upper bound on each block separately.

## 2. Complete trajectory norm summation and the surviving entropy factor

For a length-$n$ sequence
$\gamma=(\chi_0,\ldots,\chi_n)$, define

$$
A_\gamma=P_{\chi_n}U_NP_{\chi_{n-1}}\cdots
              U_NP_{\chi_0}.
$$

The exact open-history identity is

$$
\sum_{\chi_1,\ldots,\chi_n} A_\gamma^*A_\gamma
=P_{\chi_0}.
\tag{3}
$$

To verify (3), sum over $\chi_n$ first and use
$\sum_{\chi_n}P_{\chi_n}=I$ and $U_N^*U_N=I$.
The adjacent two factors of $U_N$ disappear. Repeating this calculation removes each successive intermediate sum, leaving $P_{\chi_0}$.
Consequently

$$
\boxed{\displaystyle
\sum_{\text{all open }\gamma}\|A_\gamma\|_{\rm HS}^2=N.}
\tag{4}
$$

This is a genuine exact norm cancellation identity for the original matrix.

The spectral trace closes the path, however:

$$
p_n=\operatorname{Tr}U_N^n
=\sum_{\gamma:\chi_n=\chi_0}a_\gamma,
\qquad a_\gamma=\operatorname{Tr}A_\gamma.
\tag{5}
$$

There are $Q^n$ such closed character sequences. Since a closed $A_\gamma$ acts on a space of dimension $m$,

$$
|a_\gamma|^2\le m\|A_\gamma\|_{\rm HS}^2.
$$

Restricting the nonnegative sum in (4) to closed paths gives

$$
D_n:=\sum_{\gamma\ {\rm closed}}|a_\gamma|^2
\le mN=N^2/Q.
\tag{6}
$$

Cauchy--Schwarz over the remaining path labels now yields only

$$
\boxed{\displaystyle
|p_n|^2\le Q^nD_n\le N^2Q^{n-1}.}
\tag{7}
$$

The all-block bound (2) separately gives
$|a_\gamma|\le m\rho^n$, hence

$$
|p_n|\le Q^n m\rho^n=NQ^{n-1}\rho^n.
\tag{8}
$$

For $Q\ge\sqrt N$, both (7) and (8) are weaker than the direct unitarity bound $|p_n|\le N$ already for sufficiently large $N$ and $n\ge2$.
Thus neither the exact positive identity (4) nor the per-block contraction compensates for the closed-history summation.

This remains true after the proved sparse sector is removed. If a history has at most $\epsilon n$ deviations from a fixed permutation, its initial character and the positions and values of the deviations determine it. The number of such closed histories is at most

$$
Q\sum_{j\le\epsilon n}\binom nj(Q-1)^j
\le Q\,2^nQ^{\epsilon n}.
$$

The total closed count is $Q^n$. At $n\asymp N$, the ratio of this upper bound to $Q^n$ tends to zero exponentially in $n\log Q$. Therefore the remaining dense-transition class still contains essentially $Q^n$ closed labels. A count-based Cauchy estimate does not acquire a useful smaller entropy factor.

## 3. What the exact unitary identities recover, and what they do not

Let $\mathcal P(X)=\sum_\chi P_\chi XP_\chi$, and let
$\mathcal C(X)=U_NXU_N^*$. The channel

$$
\mathcal F=\mathcal P\mathcal C
$$

has Kraus operators $P_\chi U_N$.
The general finite matrix identity
$\operatorname{Tr}_{\rm HS}(X\mapsto AXA^*)=|\operatorname{Tr}A|^2$
then gives

$$
\operatorname{Tr}_{\rm HS}\mathcal F^n=D_n,\qquad
\operatorname{Tr}_{\rm HS}\mathcal C^n=|p_n|^2.
\tag{9}
$$

The first identity follows by expanding the $n$-fold Kraus products. Their traces are exactly the $a_\gamma$ in (5), by cyclicity and the endpoint projection.
Hence the exact quantity lost by the character dephasing is

$$
|p_n|^2-D_n
=\sum_{\substack{\gamma,\gamma'\ {\rm closed}\\\gamma\ne\gamma'}}
       a_\gamma\overline{a_{\gamma'}}.
\tag{10}
$$

The unitarity contractions in (3) concern the open endpoint sums. They do not evaluate (10), whose two independent traces impose closed endpoint identifications. Replacing $\mathcal C$ by $\mathcal F$ therefore deletes precisely an unevaluated signed trace-pair contribution.

One can resum the remaining matrix words exactly, without discarding their phases. Write $S_{n,N}$ for the already bounded sparse-history operator, $\|S_{n,N}\|\le\eta^n$, and set

$$
G_{n,N}=U_N^n-S_{n,N}.
$$

Then all the apparent exponential entropy in a direct wordwise norm sum cancels down to

$$
\|G_{n,N}\|\le1+\eta^n,\qquad
\|G_{n,N}\|_{\rm HS}\le\sqrt N(1+\eta^n).
\tag{11}
$$

This is a real improvement over summing absolute norms of dense words. However its trace consequence is only

$$
|\operatorname{Tr}G_{n,N}|\le N(1+\eta^n).
$$

Summed over $O(N)$ times and divided by $N^2$, it gives $O(N)$, not $O(1)$.
The missing gain is in the coherent trace, rather than in the norm of the fully resummed unitary evolution.

## 4. Executed analytic generating-function test

Let $K_N$ retain the permitted character permutation and
$R_N=U_N-K_N$. The exact polynomial

$$
F_n(z)=\operatorname{Tr}(K_N+zR_N)^n
=\sum_{j=0}^n c_{n,j}z^j
\tag{12}
$$

has $c_{n,j}$ equal to the trace sum of all histories with exactly $j$ deviations.
The available norm estimates imply

$$
\|K_N+zR_N\|
\le\rho+|z|(1+\rho).
$$

Thus a norm contraction is proved only in the disk

$$
|z|<z_c:=\frac{1-\rho}{1+\rho}.
\tag{13}
$$

For $0<a<z_c$, Cauchy's formula gives

$$
|c_{n,j}|
\le N\big(\rho+a(1+\rho)\big)^n a^{-j}.
\tag{14}
$$

At the radius
$a=(1-\rho)/(2(1+\rho))$, the first factor equals
$Nr_*^n$, $r_*=(1+\rho)/2<1$.
For $j$ proportional to $n$, however, the coefficient cost is
$\exp(j\log(1/a))$.
The exponent in (14) is

$$
n\log r_*+j\log(1/a),
$$

which becomes positive once $j/n>-\log r_*/\log(1/a)$.
This is the quantitative boundary behind the successful sparse-sector estimate.

Evaluating at the physical value $z=1$ by these coefficient bounds gives, for example,

$$
|F_n(1)|
\le\frac{N}{1-a}(r_*/a)^n,
$$

which is exponentially worse than unitarity. The exact relation
$K_N+R_N=U_N$ reduces it to $|F_n(1)|\le N$, but does not supply an average-square trace estimate on the $n\asymp N$ scale.
No analytic continuation from (13) to $z=1$ with the required error has been proved.

## 5. The best full-pair growth bound recovered by this attempt

The existing logarithmic-time dispersion theorem does yield a growth bound for the whole pair sum. This reproduces the Fejer estimate already present in Section 4.2 of *arithmetic_seven_chain_cut_stability.md*; it is not claimed as a new universality result.

Here is a derivation using only the independently audited dispersion input.
Let $L=\lfloor\log N/(4\log A)\rfloor$, so
$|p_j|\le C\sqrt N A^j$ gives

$$
\sum_{|j|<L}(1-|j|/L)|p_j|^2
\le N^2+O(NA^{2L})=O(N^2).
\tag{15}
$$

For the nonnegative Fejer kernel
$F_L(t)=\sum_{|j|<L}(1-|j|/L)e^{2\pi ijt}$,
the shifted sum satisfies for every integer $v$

$$
\begin{aligned}
0\le\sum_j(1-|j-v|/L)_+|p_j|^2
&=\sum_{a,b}e^{2\pi iv(\theta_a-\theta_b)}
                  F_L(\theta_a-\theta_b)\\
&\le\sum_{a,b}F_L(\theta_a-\theta_b).
\end{aligned}
$$

The first expression is real and nonnegative because its coefficients are nonnegative; the last inequality follows by taking the absolute value and using $F_L\ge0$.
Thus every block of $\lfloor L/2\rfloor$ consecutive times has total squared trace $O(N^2)$.
Covering $1\le n\le BN$ gives

$$
\boxed{\displaystyle
\frac1{N^2}\sum_{1\le n\le BN}|p_n|^2
=O_B(N/\log N).}
\tag{16}
$$

For $e^{-2sn/N}$, weighting these consecutive blocks by a geometric series proves the corresponding full infinite-sum bound
$O_s(N/\log N)$.
The sparse-history removal changes either weighted expression by $o(1)$, so (16) also bounds the remaining dense-history trace functional.

This falls short even of a uniform $O(1)$ pair bound. It does not control the limiting value.

## 6. First estimate still unproved

For the concrete admissible $b_*$ in the main report, let
$w_*(\xi)=|\widehat b_*(\xi)|^2$, supported in $[-2,2]$.
The first unresolved original estimate is still

$$
\frac1{N^2}\sum_{1\le n<2N}
 w_*(n/N)\left(|\operatorname{Tr}U_N^n|^2-\min(n,N)\right)
\longrightarrow0
$$

over all odd $N$.
Even on the allowed dimensions $N=d^2m$, $m\le\sqrt N$, replacing
$\operatorname{Tr}U_N^n$ by
$\operatorname{Tr}(U_N^n-S_{n,N})$ changes this by a proved $o(1)$, but the retained weighted sum has not been evaluated.

The all-block norm gap, the exact identities (3)--(4) and (9), and the contraction disk (13) have all been used quantitatively above. None produces the needed signed cancellation among the retained dense character histories. This note records the failed completion attempt and its actual best bound, not a hidden estimate assumed for the remaining argument.

