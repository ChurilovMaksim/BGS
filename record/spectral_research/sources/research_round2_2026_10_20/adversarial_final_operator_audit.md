> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_final_operator_audit.md`. Embedded SHA256: `91a78f95638a706116d8ebbef651eb9e84102a3c164ed5d07b9709f79ab30fd8`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent final audit: endpoint laws, quantum feedback, shells, and exact sectors

This certificate records new independent checks completed on 20 October 2026. Its conclusions rest on the displayed derivations and the reread source proofs, not on agreement among reviewers. It does not prove or refute the original H_diag.

## 1. Frozen inputs

| Source | SHA-256 |
|---|---|
| arithmetic_endpoint_laws_and_sine_compression.md | 8307e8bed074727caee3788adca79a44cab2fdf2627bbbfdcb2058a50863dfe1 |
| root_uniform_translation_contact.md | 257afa4511da2fae8bd9260cc33a654bf045115f80aa0861bb8eae6a4f92347e |
| fermionic_hierarchical_feedback_barrier.md | c1ff587a2ffc08d25af21fcff203a2788d2631b98c94f01fb7d888591b3f036a |
| fermionic_frequent_shell_coherence.md | 21c536cdcb9c8f5dc43aa5c7e74300865b0152f7187b8358b68832b2ae21e285 |
| arithmetic_exact_sector_three_cell_bridge_audit.md | b7cf3ce194cffd8dac98ac85af5b9dcf9dbfbf8aaadd4d2089b8876088b539a7 |

The companion new theorem proved independently in this audit branch is:

| New theorem | SHA-256 |
|---|---|
| adversarial_finite_detector_shell_coherence.md | 76aa1ece063eea6b9e673d5fc592fa23ba72c541fee5c93916314a62da85ee6f |

The consolidated report was checked in the snapshot
81321bf635e84845b334aff302912b3ca02eccfa57fdc4de2eed270848af0f28,
Sections 7–8. Its evolving wording is not a proof input.

## 2. Endpoint laws and the sine compression: fresh challenge passed

The most delicate question is whether uniform endpoint laws were obtained by assuming a differentiable conjugacy. They were not.

### 2.1. The equilibrium measure is area

For the positive one-sided transfer with geometric weight $w$, positive eigenfunction $h$, and eigenmeasure $\nu$, the normalized backward transition is
$$
p(y)=\frac{w(y)h(y)}{h(\sigma y)}.
$$
The invariant probability is $h\nu$. In the natural extension, the conditional preceding-edge distribution given the entire future is exactly $p$. Consequently its entropy is
$$
-\int\log p\,d(h\nu)=\int\log J^u\Xi\,d(h\nu).
$$
The coboundary involving $h$ integrates to zero.

The finite-fiber entropy step is valid. If every coding fiber contains at most $D$ points, the conditional entropy of an $n$-block partition over the full factor is at most $\log D$. For each fixed $n$, choose a finite factor partition approximating that conditional entropy. The entropy inequality for a join of $k$ consecutive $n$-blocks then gives an error at most $k(\log D+\eta)$. Divide by $kn$, let $k$ tend to infinity, and then let $n$ tend to infinity. This proves equality of the coding and factor entropies without requiring one finite factor partition to work at every $n$.

The actual constant-roof suspension is a smooth transitive Anosov flow preserving a smooth volume. Its whole compact phase space is the basic set. The geometric potential is Hölder, and dense periodic points follow from the established conjugacy. The precise applicable facts are Theorem 3.3, Proposition 4.4(b), Theorem 5.1, and Remark 5.2 in Bowen–Ruelle, *The ergodic theory of Axiom A flows*, Inventiones Mathematicae 29 (1975), 181–202. They identify the geometric equilibrium with volume. These parts were reopened in the author's primary PDF:
https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B42%5D.pdf .

Thus the coding equilibrium pushes to actual area. Mixing of the constant-roof suspension is neither asserted nor needed.

### 2.2. Actual differentiability is proved separately

The topological conjugacy is used only to transport leaves, brackets, and coding. Actual stable graphs depend $C^1$ on their basepoint in one fixed holomorphic norm by the independent inverse graph transform. Its contraction is $q<1/25$, whereas the base map has derivative norm below 6. The differentiated recurrence has contraction factor at most $6q<1$; its successive derivative differences are summable. The same argument applies to the inverse map.

The actual stable/unstable product chart therefore follows from the ordinary implicit function theorem. At the fixed point its two tangent columns are $(1,s_s)$ and $(1,s_u)$; its absolute area Jacobian is
$$
\chi=s_s-s_u>0.
$$
No derivative of the topological conjugacy enters this Jacobian.

Each full crossing edge strip meets the relevant plaque in one nondegenerate interval. The conjugacy preserves the nondegenerate arc topologically; the actual invariant cones make its physical coordinate monotone. The one-dimensional Koenigs derivative is given by a uniformly convergent positive product and is normalized to 1 at the fixed point. Thus the limiting scattering intervals have positive lengths.

### 2.3. Exact cylinder indexing and normalization

The central cylinder is
$$
v\,a\,0^{2R}\,a\,w,
$$
with exactly $R$ zero edges on either side of its midpoint. Its mass is
$$
\nu(J_w A J^{2R}A J_v h).
$$
The zero-branch rank-one limit gives its rescaled mass. The actual product chart gives the same rescaled area:
$$
\Lambda^{2R}\mu[v\,a\,0^{2R}\,a\,w]
\longrightarrow \chi\,|I_S(w)|\,|I_U(v)|.
$$
Comparison first with empty outer words and then with a refinement on just one side proves the two uniform interval laws and the common constant
$$
c=\chi|I_S||I_U|.
$$
There is no extra edge factor $\Lambda$, and no conditioning on a null leaf is used.

After removing the midpoint phase, the endpoint kernel is unitarily equivalent to
$$
(c x)^{-1}S_{cx}.
$$
The unitary rescaling includes the square root of its Jacobian. Checking its trace, equal to 1 on both sides, verifies the normalization independently. In the cubic profile, the factor $c^3\varepsilon^3$ cancels the three normalization factors and gives the stated coefficient $m^4/(144N^3)$.

**Verdict:** the endpoint-to-sine passage is valid in its fixed compact range of $N\varepsilon$. This audit supplies no extension to $N\varepsilon\to\infty$.

## 3. Exact quantum feedback: all norm factors checked

Use the source notation
$$
a=\sqrt{I-E},\quad b=\sqrt E,\quad D=aU,\quad
\Theta(z)=-a+\sum_{m\ge1}z^m bUD^{m-1}b.
$$
Put $c=b(I+a)^{-1}$, $W=c^2$, and $\beta=\operatorname{Tr}W$. The exact feedback formula is
$$
(I-\Theta(z))^{-1}
=\frac{I-W}{2}+c(I-zU)^{-1}c.
$$
Since $E/4\le W\le E$, it yields the stated detector bounds.

For clarity, the mean-square lower estimate can be checked directly. The constant Fourier coefficient of the right side is $(I+W)/2$, and the positive coefficients are $cU^m c$. Their squared Hilbert–Schmidt sum can be completed to a Poisson kernel in the eigenbasis of $U$. Its off-diagonal kernel values are nonnegative. Thus
$$
\int\|(I-\Theta(re^{it}))^{-1}\|_{\mathrm{HS}}^2\,\frac{dt}{2\pi}
\ge
\frac N4+\frac\beta2-\frac{\operatorname{Tr}W^2}{4}
+\frac{1+r^2}{2(1-r^2)}\sum_j W_{jj}^2.
$$
Use $\operatorname{Tr}W^2\le\beta$ and
$\sum_j W_{jj}^2\ge\beta^2/N$. This gives the exact displayed lower bound in the source, including its factor $1/32s$ at the mesoscopic detector scale.

The operator norm upper bound needed for truncation is also exact:
$$
(I-\Theta(z))^{-1}
=\frac I2+\frac12c(I+zU)(I-zU)^{-1}c,
\qquad
\|(I-\Theta(z))^{-1}\|\le\frac1{1-|z|}.
$$

If $T\le N$, $q=\|D^T\|\le N^{-6}$, the return tail is exactly
$$
z^{T+1}bUD^T(I-zD)^{-1}b.
$$
On the circle $|z|=e^{-s/N}$, its norm is $O_s(Nq)$, and the derivative norm is $O_s(N^2q)$. The inverse difference is $O_s(N^3q)$. In the differentiated feedback trace this yields $O_s(N^6q)=O_s(1)$. The open trace tail is smaller.

The final squared Abel error uses only the unconditional estimate
$$
\left\|\sum_{m\ge1}z^m\operatorname{Tr}U^m\right\|_{L^2}
=O_s(N^{3/2}),
$$
which follows from $|\operatorname{Tr}U^m|\le N$. It is therefore $O_s(N^{-1/2})$ after normalization by $N^2$. No desired $O(N^2)$ pair-energy estimate is hidden in the proof.

The geometric open-power premise remains unproved. The constant detector $E=I/\log N$ satisfies that premise on the original $U_N$, but its feedback formula retains the original eigenphases exactly. This verifies the stated limitation without introducing another family of unitaries.

**Verdict:** the hierarchical-feedback theorem and its scope are valid.

## 4. Continuum shell theorem: coefficient and tails checked

After scaling, the Gram kernel is $\sin(\pi(x-y))/(\pi(x-y))$ on a fixed-sign pair of intervals whose outer endpoints are proportional to $\beta$. For adjacent lengths $a,\rho a$,
$$
\int_0^a\int_0^{\rho a}\operatorname{sinc}^2(\pi(u+v))\,du\,dv
=\frac1{2\pi^2}\log(\rho a)+O(1)
$$
when $\rho a\ge1$. The smaller-scale sum is $O(1)$ by the area bound.

One sign and one unordered adjacent pairing contribute
$$
\frac{(\log\beta)^2}{4\pi^2\log\Lambda}+O(\log\beta).
$$
There are two signs and two ordered directions, giving exactly
$$
\frac{(\log\beta)^2}{\pi^2\log\Lambda}.
$$
Opposite pieces at the same shell index are retained by the pinching. All opposite-side terms together are only $O(\log\beta)$, so this convention does not change the leading coefficient.

Nonadjacent resolved interactions are bounded by a geometric ratio. Unresolved intervals have a summable total area, including their accumulation at zero. These bounds account for the whole infinite remainder.

For $X=G-D$, $G_u=D+uX$,
$$
\frac{d^2}{du^2}\log\det(I-tG_u)
=-t^2\|(I-tG_u)^{-1/2}X(I-tG_u)^{-1/2}\|_{\mathrm{HS}}^2.
$$
The first derivative at 0 vanishes because $X$ has zero diagonal shell blocks. Finite compressions justify that trace identity with infinitely many blocks. Integrating with weight $1-u$ gives both determinant inequalities and the correct sign. The infinite block determinant product converges absolutely in logarithm because the block traces are summable.

**Verdict:** the continuum theorem passes, including its necessary distinction between relative determinant error and absolute error. The finite-N companion proves the same leading coefficient without a continuum-to-lattice approximation assumption.

## 5. Principal selected family to the exact double sum

This is a separate check of the new bridge, not a deduction from the small whole-trace residual.

For each primitive period-$m$ sector, the exact transverse product equals its nonzero scalar part plus residual:
$$
\operatorname{Tr}\prod K_h=\Gamma_h+r_h,
\quad |\Gamma_h|\ge .9998^m,
\quad |r_h|\le .209(.174)^{m-1}.
$$
Hence its full and principal weights satisfy
$$
\widetilde u_p=u_p(1+\eta_p),\qquad
|\eta_p|\le\frac{.209}{.174}
\left(\frac{.174}{.9998}\right)^m.
$$
This is a relative estimate for each selected sector.

For each admissible triple of lengths, replace avoidance operators in the positive word sum by unrestricted positive transfers before using operator norms. The bounds
$\sup_\ell\|T^\ell\|\le C$ and $\|J^R\|\le C\Lambda^{-R}$
give a weight $O(\varepsilon^3)$. Open and periodic continuations agree for at least $m+R$ edges, so their geometric weight ratio is bounded uniformly by summable Hölder variations. Cauchy–Schwarz applied to the two cyclic orders gives the same $O(\varepsilon^3)$ upper bound for the sum of absolute pair amplitudes.

There are $O(m^2)$ length choices and exactly $2m^2$ pointed ordered representatives per unordered orbit pair. Primitivity and recovery of the uniquely shortest gap exclude all duplicate geometric pairs. Therefore the total selected absolute mass is
$$
O(m^4\varepsilon^3)=O(N),\qquad N\le m\le3N/2.
$$
Multiplying by the uniform relative error gives
$$
|E^{\mathrm{original}}_{m,N}
-E^{\mathrm{principal}}_{m,N}|
\le CNq_0^m,\qquad q_0<.175.
$$
The bridge is valid. Full transverse cycle traces under repetition are not claimed to multiply; the selected family consists of genuinely primitive period-$m$ orbits.

## 6. Consolidated report and remaining estimate

The checked snapshot of Sections 7–8 has the correct mixed Kac identity, all absolute convergence bounds, the $7/10$ open Abel lower bound, the exact feedback determinant, the truncation budget, and the finite shell coefficient and signs.

One minor formal correction was requested in the condensed finite-entry proof: the off-diagonal sine quotient is stated for $m\ne n$, while $E_{mm}=\sigma$. This does not affect the theorem or its separate complete proof.

The first unresolved original quantity remains
$$
\frac1{N^2}\sum_{m\ge1}|\widehat b(m/N)|^2
\left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)
$$
even for the explicit fixed admissible test in the report. The independent audits establish no estimate for its full complementary orbit pairs or for higher factorial moments.

## 7. Primary-source check on a possible future open-map input

A targeted search found a theorem broader than the linear cat-map statements: Lucas Vacossin, *Spectral gap for obstacle scattering in dimension 2*, Analysis & PDE 17 (2024), with author text https://arxiv.org/pdf/2201.08259 , Theorem 1 in Section 2.1. Its hypothesis includes a fixed open canonical relation, a compact hyperbolic trapped set with negative geometric pressure, and an associated microlocally unitary Fourier integral operator. Its conclusion is a spectral-radius gap; the threshold depends on symbol seminorms.

This was not imported into the proof. The exact finite torus detector has not been reduced to that operator class with controlled errors. A shrinking hole also changes the trapped geometry; the theorem's fixed open relation cannot simply be replaced by a varying one while keeping its constants. No quantitative estimate of $\|D_N^{T_N}\|$ for the geometric shrinking detector was obtained. Even such an estimate would leave the mixed feedback phases requiring a separate argument.

