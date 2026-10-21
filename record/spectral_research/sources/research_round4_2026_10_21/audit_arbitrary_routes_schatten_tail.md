> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_arbitrary_routes_schatten_tail.md`. Embedded SHA256: `e0a083f9b6a4654444a97f8fa74b386c70422067f62a5075c0cf41cd60ff63d4`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: arbitrary Weyl routes and the Schatten-35 tail

21 October 2026. Auditor: /root/audit_uniform_word_r4.

## Source identity and verdict

Target: root_arbitrary_routes_schatten_tail.md.

SHA-256: d05c0bc44decafe181e28b06a603b2309567ae8808bb8dd5dc7a81aa14457e3e.

Upstream source: root_all_entry_and_arbitrary_weyl_routes.md.

SHA-256: c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd.

Both hashes were recomputed. Neither source was modified.

**Verdict:** the stated uniform bound for the sum of absolute traces is
proved. The convention setting the removed contribution equal to zero for
times 1 through 34 is essential to this particular arbitrary-route
statement. The proof is uniform over all prescribed time-dependent
permutations and all sufficiently large odd dimensions.

The result controls a specified exact coherent correction. It neither
evaluates its complement nor proves or refutes the original spectral
criterion.

## 1. Exact hypotheses used from the upstream theorem

On the traceless Weyl coefficient space of dimension $M=N^2-1$, the
selected matrix at each time is a weighted permutation:

$$
 D_j e_v=C_{\pi_j(v),v}e_{\pi_j(v)}.
$$

Consequently its singular values are exactly the moduli of the selected
entries. The upstream theorem supplies, for one fixed $C_*$, a fixed
$g\in(0,1/2]$, and every sufficiently large odd $N$,

$$
 |C_{\pi_j(v),v}|
 \le C_*(1+|Sv|_N)^{-1/17}+C_*/N,\qquad
 \|D_j\|\le\rho:=1-g,\qquad
 \|R_j\|\le 2-g.
 \tag{1.1}
$$

Here $R_j=C-D_j$ and $C$ is unitary. The last inequality also follows
immediately from $\|C\|=1$ and the preceding operator bound. No claim
about independent entries is involved.

The upstream proof was independently reconstructed in this audit session:
its two estimates come from the exact finite Weyl alias formula, uniform
oscillation using derivatives of orders 2 through 17, and a separate
strictness argument for the finitely many low labels. In particular, the
row estimate is obtained by applying the construction to the negative
kick, and the fixed positive gap follows from fixed-label limits and
high-label decay together. It does not follow merely from a normalized
Hilbert--Schmidt bound. The exponent in (1.1) is $1/17$, so using
Schatten order 33 here would be insufficient in dimension two. Order 35
correctly exceeds 34.

## 2. The unnormalized Schatten estimate

For $a,b\ge0$, convexity gives
$(a+b)^{35}\le2^{34}(a^{35}+b^{35})$. Since $S$ permutes nonzero
labels modulo every odd $N$, (1.1) gives

$$
 \|D_j\|_{S_{35}}^{35}
 \le2^{34}C_*^{35}
 \left(
 \sum_{v\in\Lambda_N}(1+|v|_N)^{-35/17}
 +(N^2-1)N^{-35}
 \right).
 \tag{2.1}
$$

The source defines the centered norm as Euclidean. On the square shell
$\max(|v_1|,|v_2|)=r$, there are $8r$ integer points, and their
Euclidean norms are at least $r$. Thus the square-shell count used in
the target is valid for that norm:

$$
 \sum_{v\in\mathbb Z^2\setminus\{0\}}(1+|v|)^{-35/17}
 \le8\sum_{r\ge1}r^{-18/17}
 \le8\left(1+\int_1^\infty x^{-18/17}\,dx\right)=144.
 \tag{2.2}
$$

Also $(N^2-1)N^{-35}\le1$. Therefore

$$
 \|D_j\|_{S_{35}}^{35}\le
 A:=145\,2^{34}C_*^{35}.
 \tag{2.3}
$$

This is an unnormalized Schatten bound, with no hidden factor $M$.
It is uniform in the permutation and in time.

## 3. Trace Hölder and the number of charged factors

The trace Hölder and ideal inequalities used here are

$$
 |\operatorname{Tr}(X_1\cdots X_{35})|
 \le\prod_{j=1}^{35}\|X_j\|_{S_{35}},
 \qquad
 \|AXB\|_{S_{35}}\le\|A\|\|X\|_{S_{35}}\|B\|.
 \tag{3.1}
$$

Their self-contained finite-dimensional proof was checked independently
in the source dual_sparse_cat_schatten_trace_sharpening.md, SHA-256
784f41271c57c3655215239153fafcd66dc9ecebdcab5eb462d6f25b451bc92d.
Specifically: exterior powers give the prefix inequalities for logarithms
of singular values of an invertible product; the determinant gives equality
of total sums. The positive-part representation of the exponential
converts these inequalities to the aligned singular-value product bound;
scalar Hölder finishes the trace inequality. Singular matrices follow by
continuity. The ideal bound follows from
$(XY)(XY)^*\le\|Y\|^2XX^*$ and the min--max characterization. There is
no assumption of commutativity or normality of the blocks.

Put

$$
 \delta_*=\min\left\{
 \frac{-\log(1-g/2)}{2\log(2(2-g)/g)},\frac1{70}\right\}.
$$

If $n\ge35$ and a word has $r\le\lfloor\delta_*n\rfloor$ letters
$R_j$, its number of selected letters is the integer

$$
 n-r\ge(69/70)n\ge34.5,
$$

and hence is at least 35. Choose exactly 35 of those occurrences, once for
that word. Cut the cyclic product into 35 blocks, one chosen occurrence
per block, and charge every other occurrence in operator norm. There is
no sum over the choices of 35 occurrences and therefore no missing
combinatorial factor. Equations (2.3) and (3.1) give exactly

$$
 |\operatorname{Tr}(\text{word})|
 \le A\rho^{\,n-r-35}(2-g)^r.
 \tag{3.2}
$$

Different selected matrices at different times do not change this proof.
All empty intervening products have operator norm one.

## 4. Binomial estimate and complete time sum

For clarity, the binomial estimate can be verified directly. Set

$$
 z=\frac{g}{2(2-g)}\in(0,1),\qquad
 \eta=\sqrt{1-g/2}.
$$

For $r\le\delta_*n$, $z^{-r}\le z^{-\delta_*n}$. Thus

$$
 \begin{aligned}
 \sum_{r\le\lfloor\delta_*n\rfloor}
 \binom nr\rho^{n-r}(2-g)^r
 &\le z^{-\delta_*n}
       \bigl(\rho+(2-g)z\bigr)^n\\
 &=\left[z^{-\delta_*}(1-g/2)\right]^n\\
 &\le\eta^n .
 \end{aligned}
 \tag{4.1}
$$

The final step uses
$\delta_*\le-\log(1-g/2)/(2\log(1/z))$. This verification includes
the floor and does not require any asymptotic entropy approximation.

Summing (3.2) over the exact selected words now gives, for $n\ge35$,

$$
 |\operatorname{Tr}B_{n,N}^*|
 \le A\rho^{-35}\eta^n.
$$

By definition $B_{n,N}^*=0$ for $1\le n<35$. Hence

$$
 \sum_{n\ge1}|\operatorname{Tr}B_{n,N}^*|
 \le \frac{A\rho^{-35}}{1-\eta}=:K.
 \tag{4.2}
$$

All constants are fixed independently of $N$, time, and the chosen
permutations. Even independently chosen route lists for different values
of $n$ obey the same bound. For any complex weights with
$\sup_{n,N}|w_{n,N}|\le W$,

$$
 \frac1{N^2}\sum_{n\ge1}|w_{n,N}|\,
           |\operatorname{Tr}B_{n,N}^*|
 \le WK\,N^{-2}.
 \tag{4.3}
$$

## 5. Scope and first unresolved step

The assertion is a bound for an explicitly removed trace contribution;
the first 34 original times are retained unchanged in this comparison.
It should not be described as a bound on the whole original Abel tail
or as an evaluation of the retained trace.

In particular, the result supplies no estimate evaluating
$\operatorname{Tr}(C^n-B_{n,N}^*)$ against the CUE centering on times of
order $N$. That signed, weighted evaluation is still needed already
for a fixed $k=2$ test. The higher-order criterion remains additional
work. No mathematical erratum in the audited target was found.
