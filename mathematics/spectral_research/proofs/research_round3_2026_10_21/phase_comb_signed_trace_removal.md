> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/phase_comb_signed_trace_removal.md`. Embedded SHA256: `f0d3318d9dd84035078acd143e8fbde5d943329ff27d7610a3601c967ffd4c03`.
> [Thematic guide](../../topics/arithmetic.md).

# A signed pair-trace contribution eliminated by uniform arithmetic-comb escape

Research continuation, 21 October 2026.

**Status.** This note removes one complete class of exact word histories, together with its cross-term against the rest of the trace, from the pair functional with an explicit error tending to zero. It concerns the original fixed-$\tau$ matrices and every sufficiently large odd dimension possessing the specified oldspace. It does not control histories which leave the oldspace and return, and does not prove $H_{\rm diag}$.

The dynamical input is the uniform compression gap proved in Section 6 of the companion manuscript
*arithmetic_comb_fourth_difference_gap.md*, snapshot SHA-256
c66991d1a7f73eba818911f6d5d2088232e2427de815ebc05a3e7bc220520b39.
The finite-dimensional trace argument below is independent of that proof.
The companion manuscript's independent audit is the verification gate for its compression-gap input; no further cancellation hypothesis is introduced here.

## 1. The original-family compression and its exact word contribution

Let $N=d^2m$ be odd, with

$$
r_{\rm dim}:=m\le \sqrt N .
$$

For $\varphi\in\mathbb C^m$, define the canonical oldspace embedding

$$
(J_{d,N}\varphi)(x)=
\begin{cases}
d^{-1/2}\varphi(y\bmod m),&x=dy,\\
0,&d\nmid x.
\end{cases}
$$

It is an isometry: each of its $m$ coordinates is repeated $d$ times with squared normalization $1/d$.
Set

$$
P=J_{d,N}J_{d,N}^*,\qquad Q=I-P,\qquad
D=J_{d,N}^*U_NJ_{d,N}.
$$

The companion result, including preservation of the oldspace by $M_N$, gives the uniform bound

$$
\|D\|\le \rho,\qquad
\rho=\sqrt{1-\left(\frac{\tau\sigma}{512}\right)^2}<1,
\tag{1}
$$

for all sufficiently large odd $N$, uniformly over the allowed divisors $d$. Here $\sigma=\|\widehat{\partial_q^4 a}\|_{\ell^2}>10^6$ is the fixed number defined there. Both $\tau$ and $\rho$ are independent of $N,d,m$.
The elementary bound
$\sigma\le 2(18\pi)^4<3\cdot10^7$ also gives $1/2<\rho<1$, so no issue about positivity of the square root occurs.

For integers $n\ge1$, put

$$
p_n=\operatorname{Tr}U_N^n,\qquad
c_n=\operatorname{Tr}D^n,\qquad
\widetilde p_n=p_n-c_n .
\tag{2}
$$

The term $c_n$ is an exact summand of $p_n$. Indeed, inserting $I=P+Q$ after each $U_N$ gives the finite identity

$$
p_n=
\sum_{\epsilon_1,\ldots,\epsilon_n\in\{P,Q\}}
 \operatorname{Tr}(U_N\epsilon_1\cdots U_N\epsilon_n).
\tag{3}
$$

Its all-$P$ word has trace

$$
\operatorname{Tr}(U_NP)^n
=\operatorname{Tr}D^n=c_n.
\tag{4}
$$

Thus $\widetilde p_n$ is exactly the sum of every remaining word, including all words with escape and later return. This decomposition does not depend on eigenvector bases or on a probabilistic path interpretation.

From (1),

$$
|c_n|\le r_{\rm dim}\rho^n,\qquad |p_n|\le N.
\tag{5}
$$

## 2. The entire pure-comb class and its cross-term are negligible

Let $w:[0,\infty)\to\mathbb C$ be any bounded function.
Define the correction by the termwise difference

$$
\mathcal E_{N,w}
=\frac1{N^2}\sum_{n\ge1}w(n/N)
 \left(|p_n|^2-|\widetilde p_n|^2\right).
\tag{6}
$$

The difference series in (6) is absolutely convergent for every bounded $w$. The two individual series need not converge for an arbitrary bounded nondecaying weight; whenever they do converge, (6) equals their ordinary difference. All the bounds below also hold uniformly for every finite upper cutoff.

The exact identity

$$
|p_n|^2-|p_n-c_n|^2
=2\operatorname{Re}(p_n\overline{c_n})-|c_n|^2
$$

and (5) give

$$
\begin{aligned}
|\mathcal E_{N,w}|
&\le \|w\|_\infty
 \left[
 \frac{2r_{\rm dim}}N\sum_{n\ge1}\rho^n
 +\frac{r_{\rm dim}^2}{N^2}\sum_{n\ge1}\rho^{2n}
 \right]\\
&=
\boxed{\displaystyle
 \|w\|_\infty
 \left[
 \frac{2r_{\rm dim}}N\frac{\rho}{1-\rho}
 +\frac{r_{\rm dim}^2}{N^2}\frac{\rho^2}{1-\rho^2}
 \right].}
\end{aligned}
\tag{7}
$$

In particular,

$$
\boxed{\displaystyle
\mathcal E_{N,w}=O_{\tau,a,w}(r_{\rm dim}/N)
=O_{\tau,a,w}(N^{-1/2})\longrightarrow0.}
\tag{8}
$$

The implied constants can be extremely large because $\tau=10^{-80}$, but they are fixed mathematical constants. The statement is an asymptotic estimate over the original family, without perturbation averaging or an $N$-dependent kick.

Unlike an estimate only for $\sum|c_n|^2$, (7) also controls the full signed cross-term between the all-inside-comb word and every other exact word in (3). No independence or diagonal approximation is used.

## 3. Direct application to the pair factorial functional

For an admissible $b$, write $H=\widehat b(0)$ and
$w_b(\xi)=|\widehat b(\xi)|^2$.
The verified finite Fourier identity at order two is

$$
M_{2,N}^U(b)
=\frac{H^2}{2}\left(1-\frac1N\right)
 +\frac1{N^2}\sum_{n\ge1}w_b(n/N)
     \left(|p_n|^2-N\right).
\tag{9}
$$

The sum is finite because $\widehat b$ has compact support.
Define the algebraic functional

$$
\widetilde M_{2,N}(b)
=\frac{H^2}{2}\left(1-\frac1N\right)
 +\frac1{N^2}\sum_{n\ge1}w_b(n/N)
     \left(|\widetilde p_n|^2-N\right).
\tag{10}
$$

No claim is made that (10) is the factorial moment of another unitary matrix or another point process.
Equations (7)--(9) imply the actual estimate

$$
\boxed{\displaystyle
|M_{2,N}^U(b)-\widetilde M_{2,N}(b)|
\le \|\widehat b\|_\infty^2
 \left[
 \frac{2r_{\rm dim}}N\frac{\rho}{1-\rho}
 +\frac{r_{\rm dim}^2}{N^2}\frac{\rho^2}{1-\rho^2}
 \right].}
\tag{11}
$$

The same conclusion applies to the exponential pair weight $w(\xi)=e^{-2s\xi}$, where both individual series converge. Its infinite tail presents no extra difficulty for this particular correction, owing to the factor $\rho^n$.

## 4. Combining the compression gap with logarithmic-time dispersion

The companion independent dispersion theorem
*phase_logtime_dispersion_and_missing_modes.md*, SHA-256
40dd41555520f712b99f7467ed14fd41ff0369db4b44a9b78f21c7f5a8314b4b,
gives fixed $C,A$, $A\ge2$, with

$$
|p_n|\le \min\{N,C A^n\sqrt N\}.
\tag{12}
$$

This theorem is not needed for (7)--(11). If one also uses it, the error has a strictly stronger power bound. Put

$$
\delta=-\frac{\log\rho}{2\log A}\in(0,1/2).
$$

For all sufficiently large $N$, choose

$$
L=\left\lfloor
 \frac{\log(\sqrt N/C)}{\log A}
 \right\rfloor.
$$

Since $A\rho>1$, splitting the cross-term sum at $L$ and using the two sides of (12) gives

$$
\begin{aligned}
\frac{2}{N^2}\sum_{n\ge1}|p_n|\,|c_n|
&\le
\frac{2C r_{\rm dim}}{N^{3/2}}
 \sum_{n=1}^{L}(A\rho)^n
+\frac{2r_{\rm dim}}N
 \sum_{n>L}\rho^n\\
&\le C_{A,C,\rho}\,
 \frac{r_{\rm dim}}{N^{1+\delta}}.
\end{aligned}
\tag{13}
$$

For the last step, use $A^L\le\sqrt N/C$ and
$\rho^L\le \rho^{-1}(\sqrt N/C)^{\log\rho/\log A}
=C_{A,C,\rho}N^{-\delta}$.
Adding the quadratic term from (7) proves

$$
\boxed{\displaystyle
|\mathcal E_{N,w}|
\le C_{A,C,\rho}\|w\|_\infty
 \left(\frac{r_{\rm dim}}{N^{1+\delta}}
      +\frac{r_{\rm dim}^2}{N^2}\right)
=O_{A,C,\rho,w}(N^{-1/2-\delta}).}
\tag{14}
$$

The exponent improvement is tiny for the prescribed $\tau$, but strictly positive and dimension-independent. It is a genuine combination of the two estimates for this exact signed contribution.

## 5. What remains and why this does not establish universality

The remaining trace in (2) retains every mixed word in (3). It may contain long excursions through $Q$, a return to $P$, another exit, and many later returns. Compression contractivity only bounds consecutive all-$P$ segments. It does not provide a factor $\rho^n$ for the sum of those mixed histories.

Likewise, the coordinate kernel estimate (12) controls only logarithmic times before becoming trivial. It does not estimate the sum of the mixed histories at $n\asymp N$. This note introduces no bound for that missing contribution.

Consequently the argument excludes the purely internal canonical-comb sector as a source of a nonzero limiting pair discrepancy, including its cross-term with the full complementary word sum. It does not evaluate the complementary word sum, does not address all higher factorial orders, and does not settle the required fixed-test discrepancy for the original $U_N$.

