> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round9_2026_10_21/r9_determinant_main_report_audit.md`. Embedded SHA256: `c63fe295fa11fb7d9f61a046c1a06600042d65121e721a509a2774e0f5eaec71`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/closure.md).

# Audit of the assembled Round 9 report: determinants, Galois transfer, and scope

21 October 2026. Reviewer: `/root/r9_spectral_determinant`.

## 1. Verdict and frozen version

**PASS for Sections 6–8 and their stated implications and limitations in
Sections 0, 5, 9–11.** The assembled report accurately summarizes the
proved determinant obstruction and the arithmetic result. It does not
claim that either proves or disproves the original `H_diag`.

This review concerns the assembled exposition against its complete
proof sources. The reviewer authored the determinant branch and
independently audited the arithmetic branch. It is not an additional
independent proof of the determinant branch, external peer review, or
a formal verification of the whole report. The analytic and spectral
arguments in Sections 1–4 have their own separate audits.

The exact accepted report is:

- Path: `research_round9_2026_10_21/round9_main_report.md`.
- Size: **46,937 bytes**.
- SHA-256: `abd50d2f334eba5d57142e2f80eb133ed01c83a160f4e79485a07ff7ed4ff93a`.

An initial review used report hash
`678be5fb5a90ee6794f369257c4b143da4925a8eeb9701fd3b5be650abcb994e`.
The report author then implemented the following precision corrections,
all reread at hash
`76ca6ed957c288c40118a4d5a13a66a1e2f699d48f31f0dc141f0a28a47fcafb`:

1. The inverse-determinant identities have the explicit domain
   $0<r<1$; their scaling limit has fixed $s>0$.
2. The perturbed auxiliary lattice preserves the pair limit and the
   inverse-determinant asymptotics, not the exact rational identities
   of the unperturbed lattice.
3. The det–det approximation and its fixed derivatives are stated on
   $|z|,|w|\le e^{C/N}$ for each fixed $C\ge0$.
4. The Galois image of the normalization is explicitly
   $\mathfrak g(\sqrt N)=\varepsilon_N\sqrt N$,
   $\mathfrak g(M_N)=\varepsilon_NM_N^{[2]}$,
   $\varepsilon_N\in\{1,-1\}$. The restriction $N\ge75$
   is explicit also in the projective conclusion.
5. The determinant-ratio logarithm is the unique holomorphic branch
   on $|z|<1$ that vanishes at $z=0$.

The final accepted version additionally renames the Haar matrix in
(10.3) to $C_N$, explicitly separating it from the normalized
deterministic $V_N$. That final notation correction was read and
verified; it does not change Sections 6–8 or the first missing estimate.

No author's proof source or report was modified by this reviewer.

## 2. Exact proof inputs

The following input hashes were checked against the actual files.

| Input in `research_round9_2026_10_21/` | Bytes | SHA-256 |
|---|---:|---|
| `r9_determinant_exact_cue_detdet_counterexample.md` | 13,496 | `4fd909b04e8ccc1a000930e46e6efe23b520e8d41400d8f923e3aa7911623b7f` |
| `r9_determinant_nonzero_minors_addendum.md` | 6,648 | `69233cc4b5d5772bafbf7d95aceb792f7e4a2f5f579500120984c4bf1693cc79` |
| `r9_determinant_braun_haake_and_contraction_audit.md` | 10,295 | `979cdac97772c3a10d6b186c13f066677d8d4bcf2f0bc05f4a300609f5af67f9` |
| `r9_arithmetic_galois_obstruction.md` | 18,885 | `19fc46287b04ee3dd88cfc16826b2e07e19f397b23d6e85a148844e12929ca27` |
| `r9_determinant_audit_galois.md` | 17,732 | `e32125fba85ef0f9a47d46a60ec4c05b58160e2ad2a1003c190c0a1946ff5ab0` |

The last input contains the independent exact coefficient reconstruction,
checks of the arithmetic checker and JSON, and a full audit of the raw
principal-minor source
`research_round2_2026_10_20/arithmetic_padic_jacobi_simplicity.md`,
SHA-256
`f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df`.
That source was actually read, including its ramified case $5\mid N$;
its theorem was not accepted merely by name.

## 3. Section 6: exact determinant comparison and a fixed pair defect

The report's auxiliary matrix $Z_N$ is denoted $V_N$ in the
full determinant note. This is a harmless renaming. Its characteristic
determinant is
$$
 D_N(z)=\frac{1-z^{N+1}}{1-z}=\sum_{j=0}^{N}z^j.
$$
Angular orthogonality yields the full det–det correlation
$\sum_{j=0}^N(z\bar w)^j$ at every pair of complex arguments.
The CUE equality is justified in the source by the normalized
Vandermonde density and the orthogonality of the elementary-symmetric
alternants. It is an exact finite-dimensional calculation.

The fixed bump $\phi_0$ in (6.5) has support $[-1/4,1/4]$.
Consequently its autocorrelation $\widehat b$ is smooth, supported
in $[-1/2,1/2]$, and strictly positive in the interior. Since
$|g(x)|\le\int\phi_0$, the chosen $b$ is nonnegative Schwartz
and satisfies $\sup b\le1/2<1$. Its support and normalization
are therefore exactly those required for an admissible fixed test.

Within this Fourier band, every contributing positive integer obeys
$m<N/2<N+1$, so $\operatorname{Tr}Z_N^m=-1$ and
$\min(m,N)=m$. The positive and negative Fourier frequencies in
the ordered factorial pair formula cancel its factor $1/2$.
This gives precisely
$$
 \Delta^Z_{2,N}(b)=N^{-2}\sum_{1\le m<N/2}
 |\widehat b(m/N)|^2(1-m)
 \longrightarrow-\int_0^{1/2}u|\widehat b(u)|^2\,du<0.
$$
No frequency tail or varying test is hidden here.

The full clock has unfolded spacing $N/(N+1)$, with a uniform
shift. The deleted periodic point set has intensity $1/N$, so it
meets a fixed compact interval with probability at most its length
divided by $N$. The shifted-unit-lattice limit follows. For the
smooth compact test functions used throughout the report, a support
of diameter less than one gives lattice Laplace functional $1-H_F$.
The Sine process has positive probability of two points in an interval
where $h_F\ge c>0$, by its positive second factorial density.
The product excess over $1-\sum h_F$ is at least $c^2$ on that
event and is nonnegative everywhere. Thus the bounded-observable
separation is valid and does not assume convergence of unbounded
moments.

For $0<r<1$, the reciprocal polynomial has two disjoint arithmetic
progressions of coefficients. Parseval gives
$(1+r^2)/(1-r^{2(N+1)})$. Complete-symmetric alternant orthogonality
gives the CUE value $1/(1-r^2)$. Their stated distinct asymptotics
at $r=e^{-s/N}$ are correct.

The addendum constructs an explicit auxiliary $W_N$ with
$\delta_N=2^{-N^3}$. Its highest-degree term in each physical minor
of each nonzero power has consecutive Fourier columns and a nonzero
Vandermonde coefficient. Lindemann–Weierstrass then proves the minor
is nonzero, including composite $N$. The source also proves the
all-power simplicity and nonzero trace statements. The exact bounds
on secular coefficients and reciprocal determinant ratios establish
the stated superpolynomial det–det approximation, pair limit, and
inverse-moment asymptotics. The accepted report preserves the correct
domain and distinguishes these asymptotics from the original exact
rational identity.

These matrices do not satisfy the prescribed original construction;
the report explicitly treats them as a test of an inference mechanism.

## 4. Section 7: dimensions, Galois normalization, and spectral inference

The cubic table and both cosine formulas agree exactly with the
independent rational reconstruction in the arithmetic audit. The
zero-sum triples have no modular aliasing in the stated range. The
modular half introduces the factor $(-1)^j$, whereas the doubled
area has phase $e_N(j)$. These signs are the source of the cubic
gap and must not be replaced by ordinary real halves.

The strict lower bound $3/10000$ applies to every odd $N\ge75$,
including multiples of seven. Norms smaller than two and the cubic
telescoping identity give the normalized Hilbert–Schmidt bound
$1/40000$; the operator norm is at least the normalized
Hilbert–Schmidt norm. The conjugating unitary is arbitrary.

The projective spectral conclusion additionally requires $7\nmid N$
and a nonzero algebraic complex parameter $z$. These are stated
explicitly. The proof covers the original fixed algebraic
$\tau=10^{-80}$ without claiming a uniform numerical spectral gap.

The decisive proof transitions were checked in the independent
arithmetic audit and are accurately summarized here:

- A cyclotomic automorphism with $\zeta_N\mapsto\zeta_N^2$ and
  $i\mapsto i$ exists by the Chinese remainder theorem. It fixes
  the coefficients in $\mathbb Q(i)$. Its extension sends
  $\sqrt N$ to $\pm\sqrt N$, not necessarily to the positive
  choice.
- Polynomial spectral projectors transfer to the genuine projectors
  of the transformed Hermitian matrix. The invariant expression
  $\operatorname{Tr}[(\wedge^kP_I)(\wedge^kM_N)]$ transfers each
  principal compression determinant with the harmless factor
  $\varepsilon_N^k$. No commutation of an arbitrary extension with
  complex conjugation is assumed.
- The old theorem supplies nonzero minors for every eigenvalue
  subset, not only an ordered flag. This matters because the
  automorphism need not preserve eigenvalue order. Its proof includes
  all odd dimensions with $7\nmid N$, including $5\mid N$.
- A proposed projective equality forces $\eta$ algebraic through
  the determinant identity and the exactly zero traces of both
  generators. Characteristic coefficients are finite exponential
  polynomials with algebraic frequencies and coefficients. At a
  nonzero algebraic $z$, collecting equal frequencies before
  applying Lindemann–Weierstrass gives the asserted entire identities.
- On $z=-it/N$, the largest subset sum of each fixed size is unique
  because the generator spectrum is simple. Its principal-minor
  coefficient is nonzero. Taking logarithmic growth of the modulus
  identifies all top subset sums, hence all generator eigenvalues,
  contradicting the cubic gap. No independence of all subset sums is
  assumed.

The report correctly stops at exclusion of exact projective
isospectrality. It does not infer microscopic separation or a local
spectral statistic from a Hamiltonian norm gap.

## 5. Section 8: literature applicability and direct determinant bound

The Braun–Haake statements match the completed primary-text check
recorded in `r9_determinant_braun_haake_and_contraction_audit.md`:
arXiv:1206.4222v1, Sections 3, 4.2, 4.3, and 6; published as
Journal of Physics A 45 (2012), 425101,
[DOI 10.1088/1751-8113/45/42/425101](https://doi.org/10.1088/1751-8113/45/42/425101).
The evaluated diagonal model is not a uniform error estimate for the
original deterministic Heisenberg-time sum. Equation (8.1) follows by
integrating one character and imposes total degree equality only.
The example $p_1^2\overline{p_2}$ correctly exhibits this distinction.

The exact Fourier triangle bound $\|A_N\|\le117/100$ is valid
for all odd $N$, including aliasing. With real kick parameter $t$,
unitarity gives
$$
 \partial_t\log\det(I-ze^{itNA_N}M_N)
 =-iNz\operatorname{Tr}[(I-zU_N(t))^{-1}A_NU_N(t)].
$$
The resolvent norm is at most $(1-|z|)^{-1}$. Integration from
zero to $\tau$ proves (8.2) for the stated analytic logarithm.
The result controls the direct ratio and its reciprocal, but at
$|z|=e^{-s/N}$ its bound has size $O_s(\tau N^3)$.
The report correctly says that this failure to obtain decay is not
a lower bound on the true error.

The exact version of Lindemann–Weierstrass was previously read in
the primary author text, Cheng-Chao Huang, *Explicit Bounds for Linear
Forms in the Exponentials of Algebraic Numbers*, ISSAC 2022,
Theorem 1.1, [DOI 10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170).
Only its qualitative nonvanishing statement is used, with its
hypotheses explicitly checked. The Kaplan attribution agrees with
the primary-source record in the earlier stability proof; no new
external theorem is imported through that attribution. The present
audit does not rerun or certify exhaustiveness of the broader
literature search, and the report itself makes no such claim.

## 6. Final scope check

The auxiliary test in Section 6 has Fourier support
$[-1/2,1/2]$. It is distinct from the original-family test $b_*$
in Section 10, whose support is $[-2,2]$. The report does not
transfer the former's defect to the prescribed matrices.

For the original family, the report's first still-unproved estimate is
exactly
$$
 \frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
 \bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)\longrightarrow0.
$$
It also correctly states that no allowed countersequence for this
fixed test has been proved, and that settling this one test would
still leave other bands and every fixed order $k>2$.

The norm and phase-control results are not substituted for the missing
full signed trace sum. The equivalence of the complete `H_diag` under
the new normalization is not asserted as an unconditional transfer of
every individual unbounded factorial moment. No result in Sections
6–8 changes the unresolved status stated at the start of the report.

