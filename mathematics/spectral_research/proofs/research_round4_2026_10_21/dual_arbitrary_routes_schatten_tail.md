> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/dual_arbitrary_routes_schatten_tail.md`. Embedded SHA256: `3fab0cb9a2940969201f727a30888913b00838f80ef21ff65362e86874893e84`.
> [Thematic guide](../../topics/dephasing.md).

# Arbitrary prescribed Weyl routes: uniform trace norm after a fixed time cutoff

21 October 2026. This is an exact consequence of the fixed-family all-entry
theorem in `root_all_entry_and_arbitrary_weyl_routes.md`, SHA-256
`c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd`.
That theorem is independently audited in
`dual_audit_all_entry_arbitrary_routes.md`, SHA-256
`e0f6e0785d8a052ab20464a5efaaec7a41f608010c9e4398dbe1c7fd143ecc6e`.

The result retains the same fixed positive deviation density and the same
arbitrary, possibly time-dependent permutation choices. It improves the
normalized all-time correction to O(N^(-2)) after leaving finitely many early
times unchanged. There is no assertion of H_diag or of a bound on all possible
route lists taken together.

## 1. Exact assumptions already proved for the prescribed family

Use the source's notation M=N^2-1, C=Ad_(U_N) restricted to the traceless
Weyl space, D_j the selected permutation entry in each column, and R_j=C-D_j.
For all sufficiently large odd N, uniformly in every permutation choice,

$$
|C_{w,v}|\le C_*(1+|Sv|_N)^{-1/17}+C_*/N,
\quad \|D_j\|\le\rho=1-g,
\quad\|R_j\|\le2-g,
$$

where C_*,rho,g are fixed, 0<g<=1/2, and rho>=1/2. The source chooses
fixed delta in (0,1/2) and eta in (0,1) with

$$
\sum_{r\le\lfloor\delta n\rfloor}\binom nr
\rho^{n-r}(2-g)^r\le\eta^n,
\qquad \eta=\sqrt{1-g/2}.
\tag{1.1}
$$

Let B_(n,N) be exactly the same sum of length-n words having at most
floor(delta n) complementary factors. Define

$$
p=35,\qquad
n_0=\left\lceil\frac{35}{1-\delta}\right\rceil\le70,
\qquad A=145\,2^{34}C_*^{35}.
\tag{1.2}
$$

The cutoff n0 depends only on the fixed constants, not on N or the routes.

**Theorem.** For every permitted N and route list,

$$
\boxed{\|B_{n,N}\|_{S_1}\le A\rho^{-35}\eta^n
\quad(n\ge n_0).}
\tag{1.3}
$$

Consequently,

$$
\boxed{\sum_{n\ge n_0}\|B_{n,N}\|_{S_1}
\le\frac{A\rho^{-35}}{1-\eta},\qquad
\frac1{N^2}\sum_{n\ge n_0}|\operatorname{Tr}B_{n,N}|
\le\frac{A\rho^{-35}}{(1-\eta)N^2}.}
\tag{1.4}
$$

Here S1 is the ordinary, unnormalized trace norm of the M by M coefficient
matrix. The first inequality is stronger than an absolute-trace bound.

## 2. A uniform Schatten-35 bound for every selected matrix

Each D_j is a weighted permutation, so its singular values are its selected
coefficient magnitudes. Reindexing by the invertible map S and using convexity,

$$
\|D_j\|_{S_{35}}^{35}
\le2^{34}C_*^{35}\left[
\sum_{v\ne0}(1+|v|_N)^{-35/17}+M/N^{35}\right].
$$

The centered shell of infinity norm r has 8r points. Therefore

$$
\sum_{v\ne0}(1+|v|_N)^{-35/17}
\le8\sum_{r\ge1}r^{-18/17}
\le8\left(1+\int_1^\infty x^{-18/17}\,dx\right)=144.
$$

Since M/N^35<=1,

$$
\boxed{\|D_j\|_{S_{35}}^{35}\le A}
\tag{2.1}
$$

uniformly in j,N, and all permutations. This is an unnormalized bound; its
constant has no dimension factor.

## 3. Trace norm Holder and the word estimate

The finite-dimensional proof in Section 2 of
`dual_sparse_cat_schatten_trace_sharpening.md`, SHA-256
`784f41271c57c3655215239153fafcd66dc9ecebdcab5eb462d6f25b451bc92d`,
actually establishes the stronger inequality

$$
\|X_1\cdots X_p\|_{S_1}
\le\prod_{j=1}^p\|X_j\|_{S_p}.
\tag{3.1}
$$

Specifically, its exterior-power argument gives prefix log-majorization of
the product's singular values by the products of the individual singular
values; the exponential-integral argument then bounds the sum of the former
by the sum of the latter. Scalar Holder gives (3.1). That proof does not
need to pass through the possibly smaller absolute trace. Its ideal
inequality also permits arbitrary intervening operator-norm factors.

For n>=n0 and r<=floor(delta n), the number of selected factors is
n-r>=(1-delta)n>=35. Choose 35 of them. Group the remaining factors
between them in their original order, assigning any factors before the first
chosen one to that first block. Apply (3.1), the left and right Schatten
ideal inequalities, and (2.1). This yields

$$
\|\mathrm{word}\|_{S_1}
\le A\rho^{n-r-35}(2-g)^r.
\tag{3.2}
$$

This argument works for different D_j at every step. It uses no cyclic
rotation of a trace norm, which would be invalid in general. All factors
remain in their original linear order when grouped into the 35 blocks.

Sum (3.2) over the selected placements and use the trace-norm triangle
inequality and (1.1). This proves (1.3). Summing the geometric bound gives
(1.4); the starting factor eta^(n0) was dropped only to enlarge the bound.

## 4. Exact correction and the early-time convention

Define an explicitly modified deletion by deleting nothing at 1<=n<n0 and
deleting B_(n,N) for n>=n0. Then its complete signed pair-trace correction,
with any weights satisfying sup|w_(n,N)|<=W, has magnitude at most

$$
\frac{WA\rho^{-35}}{(1-\eta)N^2}.
$$

The first n0-1 original pair terms are retained exactly. No assertion that
an arbitrary route has a vanishing or uniformly bounded unnormalized trace
at these early times is needed. The scalar-mode identity
Tr C^n=|Tr U_N^n|^2-1 makes this an exact correction to the original complete
squared-trace statistic. Its error is uniform in all bounded finite Fourier
windows and all infinite Abel windows.

The result is also uniform if an independent deterministic route list is
chosen for each n. It still refers to one specified list at each n. The
unproved quantity remains the complete signed contribution of the retained
dense histories (together with the finitely many untouched early terms),
and no all-order factorial-moment conclusion is supplied here.
