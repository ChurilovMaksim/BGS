# Gaussian limits for Cayley sums and the full twisted-Jacobi trace

**Status: EXACT + EXTERNAL-THEOREM.** The external arithmetic inputs are
Chowla's cotangent independence and, for the density statement only, the
classical Bombieri--Vinogradov theorem and PNT. This extends the repository's
fourth-moment results to a distribution theorem in explicitly sparse regimes.
Priority for this specialization is not established. It is not a microscopic
BGS theorem, and the trace parameters below are not powers of one matrix.

## 1. Statements and quantifiers

Let $K$ be an odd prime, $p\equiv1\pmod K$ a prime, $H\leq\mathbb F_p^*$
the subgroup of order $K$, and
$$
 n=K-1,\qquad d=n/2,\qquad
 A=\{(h+1)/(h-1):h\in H\setminus\{1\}\}.
$$
For every $q\in\mathbb F_p$ put
$$
 X_{K,p}(q)=\frac1{\sqrt n}\sum_{a\in A}e^{2\pi iqa/p}.
 \tag{1}
$$
Thus $X_{K,p}(0)=\sqrt n$. This is real because $A=-A$.
Probability within a design means uniform
sampling of $q\in\mathbb F_p^*$, not sampling eigenvalues of a matrix.

**Theorem 1 (pointwise sparse limit).** Along every sequence of these split
prime designs with $K\to\infty$ and $K=o(\log p)$, the law of (1) tends
weakly to $N(0,1)$. More generally, for any fixed distinct positive integers
$m_1,\ldots,m_L$,
$$
 (X_{K,p}(m_1q),\ldots,X_{K,p}(m_Lq))
 \ \Longrightarrow\ N(0,I_L).
 \tag{2}
$$
The multipliers are fixed before taking the limit. In particular they are
nonzero and distinct modulo $p$ for all sufficiently large $p$.

**Theorem 2 (density limit beyond logarithmic size).** Let $Q=Q(X)\to\infty$
with $\log Q=o(\log X)$, and define
$$
 \mathcal D(X)=\{(K,p):K,p\text{ prime},\ Q/2<K\le Q,
 \ X/2<p\le X, p\equiv1\pmod K\}.
 \tag{3}
$$
Write $\mu_{K,p}^{\boldsymbol m}$ for the empirical probability law in (2).
For every $\varepsilon>0$,
$$
 \frac{\#\{(K,p)\in\mathcal D(X):
 d_{\rm BL}(\mu_{K,p}^{\boldsymbol m},N(0,I_L))>\varepsilon\}}
 {|\mathcal D(X)|}\longrightarrow0.
 \tag{4}
$$
Here $d_{\rm BL}$ is the bounded-Lipschitz metric, with tests bounded by one
and Lipschitz constant at most one. This is convergence of the conditional
empirical laws in probability over designs. It does not say that every design
is good. For example $Q=\exp(\sqrt{\log X})$ is allowed. A fixed polynomial
scale $Q=X^\theta$, $\theta>0$, is not covered by (4).

Under the normalization of `cayley_jacobi_trace_average.md`, the exact identity
$$
 X_{K,p}(mq)=\frac K{\sqrt{K-1}}\operatorname{Tr}M_{H^\perp}(2mq)
 \tag{5}
$$
transfers both theorems to the ordinary trace of the full annihilator
twisted-Jacobi matrix. Equation (5) does not identify this quantity with
$\operatorname{Tr}(M_{H^\perp}(q)^m)$. No desymmetrized local spectral law
follows from it.

## 2. Every fixed moment: characteristic-zero classification

Fix a nonempty ordered word $\boldsymbol w=(w_1,\ldots,w_r)$ of positive
integers. Set $W=\sum_i w_i$. An exponent tuple
$\boldsymbol a\in(\mathbb F_K^*)^r$ is **balanced for this word** if
$$
 \sum_{i:a_i=b}w_i=\sum_{i:a_i=-b}w_i
 \quad(1\le b\le d).
 \tag{6}
$$
Let $B_{K,\boldsymbol w}$ count these tuples and let
$$
 Z_{K,\boldsymbol w}(p)=
 \#\{\boldsymbol a:\sum_i w_i c(h^{a_i})=0\text{ in }\mathbb F_p\},
 \qquad \Delta_{K,\boldsymbol w}(p)=Z_{K,\boldsymbol w}(p)-B_{K,\boldsymbol w},
 \tag{7}
$$
where $h$ is any generator of $H$. Counts do not depend on its choice.

For a primitive complex $K$-th root $\zeta$,
$c(\zeta^a)=-i\cot(\pi a/K)$. Chowla's theorem says that the $d$
cotangents with $1\le a\le d$ are linearly independent over $\mathbb Q$.
Consequently a characteristic-zero relation
$\sum_iw_ic(\zeta^{a_i})=0$ holds if and only if (6) holds.
Every balanced relation remains valid after reduction, so
$\Delta_{K,\boldsymbol w}(p)\ge0$ counts exactly the nonbalanced tuples
which become relations in characteristic $p$.

For the scalar word $\boldsymbol1_r$, abbreviate $B_{K,r}$. Direct counting
of the equal positive and negative multiplicities gives
$$
 B_{K,2s}=(2s)![t^s]
 \left(\sum_{j\ge0}\frac{t^j}{(j!)^2}\right)^d,
 \qquad B_{K,2s+1}=0. \tag{8}
$$
In particular $B_{K,2}=n$, $B_{K,4}=3n(n-1)$, and
$$
 B_{K,6}=15n^3-45n^2+40n. \tag{9}
$$
The term with $s$ different antipodal coordinates gives
$(2s)!\binom ds$; all remaining terms are $O_s(d^{s-1})$. Thus
$$
 B_{K,2s}/n^s=(2s-1)!!+O_s(n^{-1}). \tag{10}
$$
We use $r\ge1$ throughout the resultant argument. Zeroth moments equal one
and require no resultant.

## 3. A weighted resultant budget for all orders

Choose integer representatives $1\le a_i\le K-1$, and define
$$
 F_{\boldsymbol a,\boldsymbol w}(T)
 =\sum_{i=1}^r w_i(T^{a_i}+1)\prod_{j\ne i}(T^{a_j}-1).
 \tag{11}
$$
Repeated exponents are allowed. There is no division in (11), and
$$
 \|F\|_1\le W2^r,\qquad (T-1)^{r-1}\mid F.
 \tag{12}
$$
For a nonbalanced tuple,
$$
 R_{\boldsymbol a,\boldsymbol w}=\operatorname{Res}(\Phi_K,F)\ne0,
 \quad |R|\le(W2^r)^n,
 \quad K^{r-1}\mid R. \tag{13}
$$
Indeed $F(\zeta)$ is the nonzero Cayley sum times its nonzero denominators.
All $n$ conjugates have modulus at most $\|F\|_1$, proving the bound.
Writing $F=(T-1)^{r-1}G$ and using
$\operatorname{Res}(\Phi_K,T-1)=K$ proves divisibility. A balanced tuple
has zero resultant and is excluded from every logarithmic budget.

The simultaneous scaling action
$u\boldsymbol a=(ua_1,\ldots,ua_r)$, $u\in\mathbb F_K^*$, is free:
its first coordinate already forces $u=1$ in a stabilizer. It preserves
balance. There are exactly
$$
 \frac{n^r-B_{K,\boldsymbol w}}n \tag{14}
$$
nonbalanced orbits. For each orbit choose the representative with $a_1=1$.
Its single resultant counts all orbit members, not just this representative.

To see this, fix a split prime $p$. The simple roots of $\Phi_K$ lift from
$h^u$, $u\in\mathbb F_K^*$, to $\mathbb Z_p$. Each orbit member
that is a relation modulo $p$ makes one factor $F(\zeta_p^u)$ divisible
by $p$. All factors are nonzero and integral. Therefore
$$
 \#\{u:u\boldsymbol a\text{ contributes to }\Delta_{K,\boldsymbol w}(p)\}
 \le v_p(R_{\boldsymbol a,\boldsymbol w}). \tag{15}
$$
Although individual integer representatives change under scaling, evaluation
at $K$-th roots is unchanged; the conjugate identification in (15) is exact.

**Proposition 3 (global budget).** For every such word and odd prime $K$,
$$
 \sum_{\substack{p\text{ prime}\\p\equiv1\ ({\rm mod}\ K)}}
 \Delta_{K,\boldsymbol w}(p)\log p
 \le \frac{n^r-B_{K,\boldsymbol w}}n
 \big[n\log(W2^r)-(r-1)\log K\big]. \tag{16}
$$
In particular the right side is $O_{\boldsymbol w}(K^r)$.

**Proof.** Sum (15) over split primes and over the orbits (14). A split prime
is never $K$, so the forced factor $K^{r-1}$ in (13) can be removed.
Each orbit contributes at most
$\log(|R|/K^{r-1})$, bounded by the bracket in (16). This proves (16).
For fixed $K,\boldsymbol w$, the sum has finite support. $\square$

A pointwise corollary needed below is
$$
 p>(W2^r)^n\quad\Longrightarrow\quad
 \Delta_{K,\boldsymbol w}(p)=0. \tag{17}
$$
For $r=4,\boldsymbol w=\boldsymbol1$, (16) is weaker in constant than the
specialized fourth-order budget with coefficient 12 already in the repository.
Its gain is validity for every order and weighted word, not a better
fourth-order exponent.

## 4. Moment identity and independent-phase comparison

Additive orthogonality, including the omitted zero frequency, gives exactly
$$
 \frac1{p-1}\sum_{q\ne0}\prod_{i=1}^rX_{K,p}(w_iq)
 =\frac{p(B_{K,\boldsymbol w}+\Delta_{K,\boldsymbol w}(p))-n^r}
 {(p-1)n^{r/2}}. \tag{18}
$$
The subtraction $n^r$ is essential. For example the mean is
$-\sqrt n/(p-1)$, not identically zero; the second moment is
$(p-n)/(p-1)$.

Let $\Theta_1,\ldots,\Theta_d$ be independent uniform variables on
$[0,2\pi]$, and define
$$
 Y_{K,j}=\frac1{\sqrt n}\sum_{b=1}^d2\cos(m_j\Theta_b).
 \tag{19}
$$
Expanding products and integrating each phase shows that the mixed moment
for the word $\boldsymbol w$ is exactly
$B_{K,\boldsymbol w}/n^{r/2}$: an exponent survives precisely when (6)
holds. This is an equality of moments, not an assertion that the finite-field
phases are independent.

For each $b$, the vector
$(\sqrt2\cos(m_j\Theta_b))_{j=1}^L$ is bounded, has mean zero and
covariance $I_L$, by cosine orthogonality and distinct positive $m_j$.
The vectors for different $b$ are independent. Expanding a fixed mixed
moment of their normalized sum, partitions containing a singleton vanish.
Only pair partitions have $r/2$ distinct indices and order-one contribution;
their contribution is Wick's formula with covariance $I_L$. Every other
partition is $O_{r,L,\boldsymbol m}(d^{-1/2})$, or smaller. Thus all mixed
moments in (19) tend to those of $N(0,I_L)$.

Integer relations between the multipliers do not invalidate this argument.
For instance the word $(1,1,2)$ has $B_{K,(1,1,2)}=n$, so its normalized
mixed third moment is $n^{-1/2}$, which vanishes. Multipliers $m,-m$
would give identical components, explaining the distinct-positive hypothesis.

For each fixed word, (18) differs from the reference moment by at most
$$
 \frac p{p-1}\frac{\Delta_{K,\boldsymbol w}(p)}{n^{r/2}}
 +\frac{2n^{r/2}}{p-1}. \tag{20}
$$
If $K=o(\log p)$, (17) eventually removes the excess for every fixed word,
and the second term vanishes. The Gaussian is moment-determinate; alternatively
apply the scalar moment argument to every real linear combination of the
components and use the Gaussian exponential moments. This proves Theorem 1.

## 5. Averaging the obstruction, rather than each trace function

In the family (3), Bombieri--Vinogradov at the endpoints $X,X/2$ gives
$$
 |\mathcal D(X)|=
 (\operatorname{Li}(X)-\operatorname{Li}(X/2))
 \sum_{\substack{Q/2<K\le Q\\K\text{ prime}}}\frac1{K-1}
 +O_A(X/(\log X)^A). \tag{21}
$$
For each fixed $A$, the modulus bound holds eventually since $Q=X^{o(1)}$.
PNT and partial summation, requiring only $Q\to\infty$, give
$$
 \sum_{\substack{Q/2<K\le Q\\K\text{ prime}}}\frac1{K-1}
 =\frac{\log2+o(1)}{\log Q},\qquad
 |\mathcal D(X)|\sim\frac{\log2}{2}
 \frac X{\log X\log Q}. \tag{22}
$$
For example $A=3$ makes the error relative to this main term
$O(\log Q/(\log X)^2)=o(1)$, even if $Q$ grows arbitrarily slowly.
No prime-number theorem for one individually varying modulus is assumed.

Since $\log p\ge\log(X/2)$, (16) implies
$$
 \sum_{(K,p)\in\mathcal D(X)}
 \frac{\Delta_{K,\boldsymbol w}(p)}{(K-1)^{r/2}}
 \ll_{\boldsymbol w}\frac1{\log X}
 \sum_{\substack{Q/2<K\le Q\\K\text{ prime}}}K^{r/2}
 \ll_{\boldsymbol w}\frac{Q^{r/2+1}}{\log X\log Q}. \tag{23}
$$
Dividing by (22) yields the main quantitative estimate
$$
 \frac1{|\mathcal D(X)|}\sum_{(K,p)\in\mathcal D(X)}
 \frac{\Delta_{K,\boldsymbol w}(p)}{(K-1)^{r/2}}
 \ll_{\boldsymbol w}\frac{Q^{r/2+1}}X=o(1). \tag{24}
$$
Markov's inequality, (20), and the independent-phase comparison now give
convergence in probability of every fixed mixed moment to its Gaussian value.

To justify the law-level quantifier, take any sequence $X_j\to\infty$.
If (4) failed, take a subsequence with probability bounded below of a fixed
positive distance from the Gaussian. From moment convergence in probability,
extract a further subsequence on which all the countably many mixed moments
converge almost surely: at step $j$, make the probability of an error in the
first $j$ moments at most $2^{-j}$, and use Borel--Cantelli on a product
coupling of the design selections. The second moments ensure tightness;
higher even moments ensure uniform integrability of each lower polynomial.
Every weak subsequential limit therefore has the Gaussian mixed moments.
Gaussian moment determinacy (or scalar determinacy for rational projections)
identifies the limit as $N(0,I_L)$. Thus the bounded-Lipschitz distance tends
to zero almost surely on this further subsequence, contradicting the
probability lower bound. This proves Theorem 2.

For a fixed $Q=X^\theta$, (23)--(24) still prove the order-$r$ moment
conclusion when $0<\theta<\min(1/2,2/(r+2))$. For $r=4$ this recovers
the earlier $\theta<1/3$ threshold. The thresholds tend to zero as
$r\to\infty$; they cannot be exchanged for a fixed positive $\theta$ in a CLT.

## 6. Falsification controls and remaining frontier

For $(K,p)=(11,199)$, exact integer convolution gives
$$
 (Z_3,B_3)=(6,0),\quad (Z_4,B_4)=(270,270),\quad
 (Z_6,B_6)=(12250,10900). \tag{25}
$$
Thus an exact fourth-order baseline does not imply the higher-order
classification. At $(13,521)$, likewise $Z_4=B_4=396$ but
$Z_6-B_6=2730$. These examples do not contradict either limit theorem.

`computations/verification/cayley_higher_moments.py` tests the actual weighted
tuple domains, characteristic-zero polynomial criterion, resultant valuations,
and finite-field convolution independently on its stated finite designs.
`computations/analysis/cayley_trace_limit_figure.py` gives a floating-point
illustration of the empirical law, explicitly separate from the proof.
The new analytic limit theorem is not Lean-formalized.

Three routes were examined in this pass:

1. Shifted-subgroup transfer: the existing exact orbit decomposition still
   sums to $O(K^3)$. The inspected 2026 multiplicative irreducibility theorem
   does not supply a bound for the moving distinguished product classes.
   The sparse uniform $8/3$ exponent remains unimproved.
2. Falsification by higher moments: (25) rules out promoting the earlier
   fourth-order identity directly to a Gaussian law.
3. All-order cyclotomic budgets: (16)--(24) establish the sparse trace limits.
   At fixed polynomial size the first uncontrolled moments have
   $Q^{r/2+1}/X\not\to0$. This route alone has no fixed-power CLT.

The main BGS frontier remains control of joint traces of powers of the
correct desymmetrized quantum propagator at Heisenberg times. The Gaussian
family in (5) varies an additive parameter in a full Jacobi matrix. Converting
one into the other would be an additional mathematical theorem; none is
asserted here.

## Sources and review boundary

- K. Wang, *On a theorem of S. Chowla*, J. Number Theory 15 (1982), 1--4,
  [DOI](https://doi.org/10.1016/0022-314X(82)90078-6), Theorem A, p. 1;
  [author-posted copy](https://www.researchgate.net/profile/Kai-Wang-227/publication/256257948_On_a_theorem_of_S_Chowla/links/5c423968a6fdccd6b5b7dd15/On-a-theorem-of-S-Chowla.pdf).
  The prime-order statement was checked in the article text in this pass.
- Bombieri--Vinogradov and PNT: the exact forms and references already listed
  in `cayley_jacobi_trace_average.md`, Section 4, and `literature/bibliography.md`.
  A published restatement of the needed average prime-distribution estimate
  appears in Fouvry--Iwaniec, *On a theorem of Bombieri--Vinogradov type*, p. 135,
  [article](https://people.math.ethz.ch/~kowalski/fouvry-iwaniec-on-a-theorem.pdf).
- Kim--Yip--Yoo, *Multiplicative irreducibility of shifted multiplicative
  subgroups*, [arXiv:2602.20919v2](https://arxiv.org/abs/2602.20919v2), was
  screened as a possible energy input; it is not used in the proof.
- T. Untrau, *Equidistribution of exponential sums indexed by a subgroup of
  fixed cardinality*, Math. Proc. Cambridge Philos. Soc. 176 (2024), 65--94,
  [DOI](https://doi.org/10.1017/S0305004123000361), Section 1.3 and Theorem A,
  studies fixed subgroup order and torus pushforwards for Laurent-polynomial
  phases. This is relevant prior context for the independent-phase mechanism.
  The present statements use a rational Cayley phase and growing subgroup
  order; those changes require the explicit uniform budget above. This
  comparison does not establish priority.

An independent read-only review checked the statement, orbit valuation
argument, growing-modulus denominator, and moment-to-law quantifiers.
Finite tests are implementation checks, not substitutes for those proofs.
Neither the source screening nor the review establishes global novelty.
