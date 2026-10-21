> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_original_pointwise_interference.md`. Embedded SHA256: `cfc9f714eb19b28fedae80d1137d473bc6be59616e0b7829b83634e6760a48d3`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: persistent physical-kernel interference

Round 5, 21 October 2026. Auditor: /root/audit_uniform_word_r4.

## 1. Frozen source and verdict

I read the entire source dual_original_pointwise_interference.md and
independently verified its SHA-256:

650d508cae0e6e19576497f03404d2beb1a5ab196081d177b402f8b221147408.

Its sole analytic input is dual_physical_four_branch_kernel.md, SHA-256

0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c,

already independently checked in audit_four_branch_physical_kernel.md
(SHA-256 f2ae8cb525af0d957cfd59656bf4dce020404be80604d390c6800ca185b8e381).
No source was modified.

**Verdict.** Both conclusions (1.1) and (1.2) are proved as stated for the
original matrices. The progression is used to disprove an auxiliary uniform
pointwise-flatness assertion, and this does not constitute an $H_{\rm diag}$
countersequence. I found no missing estimate in this discriminator.

## 2. The four exact actions and the unique frequency

At $q=1/3,r=0$, the corrected symbol has

$$
p_m^0=(m-1)/4,\qquad R(1/3)=r(5/6)=3/4.
$$

Using the exact trigonometric values

$$
\cos\alpha_0=-3/5,\qquad \sin\alpha_0=4/5,
$$

the four momentum-cosine values are respectively

$$
-4/5,\quad-3/5,\quad4/5,\quad3/5.
$$

Multiplication by $3/400$ yields exactly the displayed offsets

$$
-3/500,\quad-9/2000,\quad3/500,\quad9/2000.
$$

Their strict order is $0,1,3,2$; the least positive separation is $3/2000$.
The source uses the exact phases $s_m=S_m(t,1/3,0)$, not their first-order
truncations. Since the error of each such truncation is at most $35000t^2$,

$$
70000t^2<(3/2000)t
$$

preserves every strict ordering at the fixed original
$t=10^{-80}/(2\pi)>0$.

Thus $\delta=s_2-s_0$ is the unique largest ordered difference among all
$s_m-s_n$. The bound $|s_m|\le2t$ gives $0<24\delta\le96t<1$. Every
relative frequency $24(s_m-s_n-\delta)$ has absolute value at most
$192t<1$. Therefore an integer relative frequency must be zero, and only
the pair $(m,n)=(2,0)$ has this property. This argument requires neither
irrationality of an action nor independence of their differences.

## 3. Modular coefficients on the exact progression

For $N_k=24k+3$, one has $\nu_N=5$. Hence

$$
z=e^{-15\pi i/4}=e^{\pi i/4},\qquad
(g_0,g_1,g_2,g_3)=\tfrac12(z,1,-z,1).
$$

At $y=0$ the remaining chirp scalar is one. The relative initial phase at
$x=N_k/3$ is exactly

$$
e^{2\pi iN_k m/12}=e^{2\pi i(2km+m/4)}=i^m.
$$

After removing a common unit-modulus phase, the four coefficients are

$$
(c_0,c_1,c_2,c_3)=\tfrac12(z,i,z,-i),
\qquad c_2\overline{c_0}=1/4.
$$

The kernel's column error gives an entry error $O(N_k^{-1})$; multiplication
by $\sqrt{N_k}$ makes it $O(N_k^{-1/2})$. The four-term amplitude stays
bounded. Squaring the absolute value therefore gives the exact observation

$$
F_k=\left|\sum_m c_m b_m e^{2\pi i(24k+3)s_m}\right|^2-1
+O(N_k^{-1/2}),
$$

where $b_m>0$ and every $s_m,b_m,c_m$ is independent of $k$. No matrix
entry of a changed kick or continuous replacement has been substituted here.

## 4. Cesaro coefficient and lower density

For a fixed real $\beta\notin\mathbb Z$, the geometric-series identity gives

$$
\left|\frac1K\sum_{k=0}^{K-1}e^{2\pi ik\beta}\right|
\le\frac2{K|1-e^{2\pi i\beta}|}\longrightarrow0.
$$

There are only sixteen differences in the squared amplitude, so no
uniformity in tiny nonzero frequencies is needed. Multiplication by
$e^{-2\pi i24k\delta}$ isolates exactly the $(2,0)$ coefficient. The
constant and subtracted one have noninteger frequency $-24\delta$, and the
error has Cesaro mean zero. Thus the claimed limiting coefficient is exactly

$$
\lim_{K\to\infty}\frac1K\sum_{k<K}F_k e^{-2\pi i24k\delta}
=\frac{b_2b_0}{4}e^{2\pi i3\delta}.
$$

Positivity of the amplitudes and their squared-amplitude bounds imply

$$
\frac{b_2b_0}{4}\ge\frac{1-40000t}{4}>\frac15.
$$

The triangle inequality therefore gives

$$
\liminf_K\frac1K\sum_{k<K}|F_k|>1/5,
$$

which implies the strict limsup claim.

For the density estimate, the squared main amplitude is at most
$4(1+40000t)$. After subtracting one, its maximum positive deviation is
$3+160000t<4$, and its negative deviation is no larger than one. The
vanishing remainder therefore gives $|F_k|\le4$ for all sufficiently large
$k$. Finitely many initial values contribute $o(1)$ to an average. With

$$
p_K=K^{-1}\#\{0\le k<K:|F_k|\ge1/10\},
$$

one obtains

$$
\frac1K\sum_{k<K}|F_k|\le\frac1{10}+\frac{39}{10}p_K+o(1).
$$

Rearranging before taking the lower limit gives

$$
\liminf_K p_K\ge\frac{1/5-1/10}{4-1/10}=\frac1{39}.
$$

In fact the exact amplitude lower bound yields a slightly larger constant;
the target deliberately states the simpler one.

## 5. Scope boundary

The oscillation takes place at the original fixed kick as the dimension
grows. It disproves

$$
\sup_{x,y}|N|U_N(x,y)|^2-1|\longrightarrow0,
$$

because a single selected entry already violates that assertion on a positive
lower-density subset of the chosen arithmetic progression. It does not
contradict the operator-norm estimate for the physical transition matrix:
an entry deviation of order $N^{-1}$ need not produce a nonvanishing
operator norm. No factorial spectral moment or bounded point-process
observable has been estimated by this discriminator, so neither direction
of the original spectral-statistics question follows from it.
