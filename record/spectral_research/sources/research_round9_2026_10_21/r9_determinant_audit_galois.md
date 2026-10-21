> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round9_2026_10_21/r9_determinant_audit_galois.md`. Embedded SHA256: `e32125fba85ef0f9a47d46a60ec4c05b58160e2ad2a1003c190c0a1946ff5ab0`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/algebra.md).

# Independent audit of the cyclotomic spectral-transfer obstruction

21 October 2026. Auditor: `/root/r9_spectral_determinant`.

## 1. Verdict and exact frozen targets

**PASS for Theorems 1 and 2, with the stated dimension restrictions.**

The quantitative cubic Hamiltonian gap holds for every odd $N\ge75$.
The projective non-isospectrality conclusion holds for every odd
$N\ge75$ with $7\nmid N$, at every nonzero algebraic complex
parameter $z$. In particular it applies at the fixed prescribed
$\tau=10^{-80}$.

No mathematical correction to the author's new theorems is required.
The theorem does not establish either a microscopic spectral distance
lower bound or any discrepancy estimate in $H_{\rm diag}$.

The following hashes were computed from the actual bytes before this
audit. None of the author's targets or old inputs was modified.

| Frozen target/input | Bytes | SHA-256 |
|---|---:|---|
| `research_round9_2026_10_21/r9_arithmetic_galois_obstruction.md` | 18,885 | `19fc46287b04ee3dd88cfc16826b2e07e19f397b23d6e85a148844e12929ca27` |
| `research_round9_2026_10_21/r9_arithmetic_galois_check.py` | 3,841 | `3a0e2612c2a0644355a125a26e449751268565a06437726a24713372968d96fd` |
| `research_round9_2026_10_21/r9_arithmetic_galois_check.json` | 2,115 | `dc6ef9115edcd13ce217a0b8c1c8457bc270df6ff839f1ec3ae3ea0ebab5a4b0` |
| `research_round2_2026_10_20/arithmetic_padic_jacobi_simplicity.md` | 17,689 | `f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df` |

The ten hashes recorded in the author's JSON, including the base
master hash `b1dc28374e62fb77c59d7da04f638916e43e0ac5809c68ea02c501fb92436a20`,
were individually recomputed and all agreed. Reading the load-bearing
Jacobi source was not replaced by that hash check: its full raw proof
was read and reconstructed as detailed in Section 5 below.

The historical arithmetic-route survey in the author's Section 7 is
not needed to prove either new theorem. This audit does not re-prove
every historical result mentioned in that survey.

## 2. Independent exact verification of the cubic moment

The Weyl multiplication convention was checked directly. With
$W_{(k,l)}=T_N(l,k)$, multiplying the two actions on a coordinate
vector gives
$$
 W_uW_v=e_N(\overline2\,[l_uk_v-k_ul_v])W_{u+v}.
$$
The opposite convention for the alternating form would change the
individual signed area labels; the table is even, but the displayed
convention itself is correct. The trace of a nonidentity Weyl label is
zero by the additive-character sum.

For the coefficient support, $|k|\le9$ and $|l|\le1$. If a triple
sums to zero modulo $N\ge29$, both integer sums are zero. For the
companion labels, multiplication of the first Fourier coordinate by
two is invertible modulo odd $N$, so the same zero-sum test applies.
There is no need to impose a new cutoff $N>54$ on account of the
displayed doubled frequencies. In either case the final triple-product
phase is the phase of $W_uW_v$, because $u+v=-w$ makes the last
alternating product zero.

Two exact computations were performed:

1. The arithmetic part of the author's checker was executed from its
   parsed AST, stopping before the suffix that writes its JSON. Its
   computed table, count, and rational bound agree with the frozen JSON.
2. An independent reconstruction formed Laurent polynomials by
   multiplying $(1-\cos7t)(1+\cos t)$, then formed every prescribed
   summand of $f-1/10$ by Laurent multiplication. It enumerated all
   ordered triples directly, rather than completing the third label
   from the first two.

Both computations use exact pairs of rational numbers for Gaussian
rational coefficients. Both give 32 nonzero Fourier coefficients and
414 ordered zero-sum triple contributions. The resulting table is
$$
 d_0=-\frac{273}{20000},\quad
 d_{\pm1}=\frac9{800000},\quad
 d_{\pm6}=d_{\pm8}=\frac3{800000},\quad
 d_{\pm7}=-\frac{81}{800000},
$$
with no other nonzero entries. Thus the table is an exact finite
certificate, not an asymptotic fit or a floating-point experiment.

For odd $N$, $\overline2=(N+1)/2$, whence
$e_N(\overline2j)=(-1)^je^{\pi ij/N}$. Multiplication of the area
by two in the companion instead gives $e_N(j)$. This verifies every
sign and argument in the author's formulas (2.6) and (2.7).

For $N\ge75$, the two cosine differences in (3.1) are nonnegative,
and the final negative term is at least $-18$. The bound
$\cos t\ge1-t^2/2$ follows, for positive $t$, by first
integrating $\cos u\le1$ to obtain $\sin u\le u$, and then
integrating once more; evenness covers negative $t$.
One elementary verification of the strict $\pi^2<10$ used there is
$$
 \frac{22}{7}-\pi
 =\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx>0,
 \qquad (22/7)^2<10.
$$
Polynomial division and $\int_0^1(1+x^2)^{-1}dx=\pi/4$
verify the integral identity. Thus the stated numerator lower bound
is strictly larger than
$$
 81\left(2-\frac{1225}{75^2}\right)-18
 =\frac{3159}{25}>120.
$$
This proves the strict cubic gap $3/10000$ with no numerical
rounding.

Both Hamiltonians have norm at most $69/50<2$ by the author's
Fourier coefficient triangle bound. The noncommutative telescoping
identity
$A^3-B^3=A^2(A-B)+A(A-B)B+(A-B)B^2$ is correct. Normalized
Hilbert--Schmidt Cauchy--Schwarz bounds its normalized trace by
strictly less than $12\|A-B\|_{2,N}$. This gives the constant
$1/40000$. The operator-norm and Wasserstein statements follow
exactly as claimed; neither requires the conjugating matrix to have
algebraic entries.

## 3. The Galois automorphism and the positive square root

For odd $N$, the Chinese remainder theorem gives an integer
$a\equiv2\pmod N$, $a\equiv1\pmod4$. It is prime to $4N$.
Thus $\zeta_{4N}\mapsto\zeta_{4N}^a$ is an automorphism of the
cyclotomic field and sends $\zeta_N$ to $\zeta_N^2$ while fixing
$i$.

All Fourier coefficients $c_{k,l}$ are in $\mathbb Q(i)$, so they
are fixed. Applying the automorphism to the original Weyl matrix
entries therefore gives precisely
$$
 \sigma(A_N)=\sum_{k,l}c_{k,l}T_N(l,2k)=A_N^{[2]}.
$$
No change of the modular inverse $\overline2$, which is a residue
represented by an integer, occurs in this step.

Extend this automorphism to a common algebraic closure containing the
eigenvalues and projectors. An algebraic embedding extends successively
by choosing roots of the transported minimal polynomials; the standard
maximal-extension argument supplies the required extension. Its image
of the chosen $\sqrt N$ is necessarily one of the two roots of
$X^2-N$, namely $\pm\sqrt N$. Consequently
$$
 \sigma(M_N)=\epsilon M_N^{[2]},\qquad \epsilon\in\{1,-1\}.
$$
The target handles this sign correctly. It would not be justified to
assume that the positive real normalization is automatically fixed.

Hermiticity of $A_N^{[2]}$ may be checked directly from the
conjugate Fourier pairs and $T_N(l,2k)^*=T_N(-l,-2k)$. Equivalently,
the original cyclotomic automorphism commutes with complex conjugation
on the base cyclotomic field. No commutation with complex conjugation
on the entire algebraic closure is required or used.

The proof concerns the explicitly defined companion exponential
$e^{izNA_N^{[2]}}$. It does not apply an unverified field automorphism
to the transcendental entries of $e^{izNA_N}$.

## 4. Spectral projectors and principal compression determinants

The characteristic polynomial of $A_N^{[2]}$ is the image of that of
$A_N$. Once simplicity of $A_N$ is established, its nonzero
discriminant remains nonzero under $\sigma$. Its transformed roots
are precisely the distinct eigenvalues of $A_N^{[2]}$. They are
real because the latter is Hermitian, not because an arbitrary
algebraic-closure automorphism preserves the real axis.

For each distinct eigenvalue, the Lagrange interpolation polynomial
$$
 P_\lambda=\prod_{\mu\ne\lambda}
           \frac{A_N-\mu I}{\lambda-\mu}
$$
is its spectral projector. Applying $\sigma$ produces the same
interpolation polynomial for the transformed Hermitian matrix and
transformed eigenvalues. Hence $\sigma(P_\lambda)$ is its genuine
orthogonal spectral projector. The argument still makes no assertion
about $\sigma(Q^*)$ for an eigenvector matrix $Q$.

Let $I$ contain $k$ eigenvalues and $P_I=\sum_{\lambda\in I}P_\lambda$.
The operator $\wedge^kP_I$ is the rank-one projection onto the
exterior product of their orthonormal eigenvectors. Therefore
$$
 b_I=\operatorname{Tr}\bigl((\wedge^kP_I)(\wedge^kM_N)\bigr)
$$
is exactly the determinant of the principal compression of $M_N$
to that eigenspace. This is algebraic in the original matrix entries:
exterior-power entries are minors, and the trace is a finite sum.
Thus
$$
 \sigma(b_I)=\epsilon^k
 \operatorname{Tr}\bigl((\wedge^k\sigma(P_I))
                       (\wedge^kM_N^{[2]})\bigr).
$$
If $b_I\ne0$, the transformed principal minor is nonzero. Every
companion subset is the image of some original subset. The use of
all subsets in the old input, rather than just one ordered initial
flag, is crucial here because Galois action need not preserve order.

## 5. Audit of the actual old principal-minor proof

The full raw source
`research_round2_2026_10_20/arithmetic_padic_jacobi_simplicity.md`
was read, including its ramified valuation argument. Only its first
theorem is load-bearing here: simplicity of $A_N$ and nonvanishing
of the overlap minors. The old assertions about simplicity of
$U_N(z)$ and its algebraic commutant are not needed for the present
Galois proof.

### 5.1 The exact path and the valuation bounds

The source's coordinate ordering is $x_j=(N+1)/2+j\pmod N$.
The hopping edge in this order is $r((j+1)/N)$. On an odd grid,
the factor $1+\cos(2\pi y/N)$ never vanishes. When $7\nmid N$,
the first factor vanishes only at $y=0\pmod N$; there is exactly
one zero seam edge and all internal edges are positive.
The gauge $D_{jj}=\omega^j$, $\omega=(-3+4i)/5$, removes each
internal phase exactly, including the wrap in original coordinates.
Thus $200D^{-1}P^*A_NPD$ is a real symmetric Jacobi path.

At the valuation over $1+2i$, normalized by $v(5)=1$,
$v(\omega)=1$. The exact factorization
$$
 r(y/N)=-\frac{(\eta^7-1)^2(\eta+1)^2}{4\eta^8},
 \qquad \eta=e^{2\pi iy/N},
$$
and the odd order of $\eta$ make $1+\eta$ a valuation unit.
For a primitive $5^a$-root, the identity
$\Phi_{5^a}(1)=5$ gives
$v(1-\eta)=1/(4\cdot5^{a-1})$, since the ratios of its primitive
conjugate factors are units. Roots whose order is not a power of
five have unit difference from one. Hence every nonzero edge obeys
$0\le v(b_j)\le1/2$. The scaled diagonal is integral at this
valuation because its only remaining denominators are units
$2$ and $i$. These arguments include arbitrary $5$-power
divisibility in $N$.

The nonzero-edge recurrence proves that an eigenvector is determined
by its first coordinate and that a zero first coordinate forces the
whole vector to vanish. Hermiticity then proves simplicity. The
eigenvalues of the scaled path are valuation-integral because they
satisfy a monic integral characteristic polynomial.

### 5.2 Both endpoint eigenvector-minor estimates

The endpoint-normalized coordinates have the exact form
$p_j(\mu)/(b_0\cdots b_{j-1})$, where $p_j$ is monic of degree
$j$ with integral coefficients. An alternant in any chosen
eigenvalues is divisible by their Vandermonde with integral quotient;
this follows by expanding into monomial alternants with integer
Schur quotients. For the first $k$ indices the quotient is one.
Using $v(b_j)\le1/2$ yields the source's bound relative to that
first endpoint set. Applying the same recurrence from the other
endpoint yields the corresponding bound relative to the last
$k$ indices. Nonzero endpoint normalization factors cancel in
these ratios, so no assumption that they are valuation units is made.

### 5.3 The Fourier minors when $5\mid N$

After roots of unity multiplying rows and columns are removed,
the cat overlap in path coordinates has entries
$N^{-1/2}\zeta_N^{cij}$, with $c=\overline4$ a unit.
For $N=5^en$, $(n,5)=1$, the valuation of the Vandermonde
in a row set $I$ is exactly
$$
 \frac{C_n(I)}{4\cdot5^{e-1}}+
 \sum_{t=1}^{e-1}5^{t-e}C_{n5^t}(I),
 \quad C_d(I)=\sum_{r\bmod d}\binom{m_r(I)}2.
$$
The coefficients follow by taking successive increments of
$1/(4\cdot5^{e-t-1})$. For each modulus, convexity of the
occupancy sum minimizes it at balanced occupancies. Consecutive row
indices realize these minima simultaneously for every divisor used.
Arbitrary column exponents add an integral Schur factor, of
nonnegative valuation. This proves that the designated last-row,
first-column Fourier minor has minimal valuation. Its common
normalization $N^{-k/2}$ cancels in every ratio even when ramified.

### 5.4 The strictly unique term

For a $k$-minor of the eigenbasis cat matrix, double
Cauchy--Binet expands over coordinate row and column subsets.
The pair consisting of the last $k$ row indices and first $k$
column indices has nonzero eigenvector minors and a nonzero Fourier
Vandermonde minor. It uniquely minimizes the index difference in
the factor $\omega^{\sum J-\sum I}$.
If a different pair has positive integer defect
$g=(\sum I_0-\sum I)+(\sum J-\sum J_0)$, the two endpoint
eigenvector estimates cost at most $g/2$, while the gauge gains
$g$ and the Fourier minor costs nothing. Its relative valuation
is therefore at least $g/2>0$.

The complete sum is the nonzero extreme term times a valuation
unit of the form one plus elements of positive valuation. It cannot
vanish. Normalizing the eigenvectors multiplies rows and columns by
nonzero algebraic factors and preserves this conclusion.
This proves the principal-minor input needed in Section 4 of this
audit. No step extends it to the seven-component case $7\mid N$.

## 6. Continuation from one algebraic parameter and the projective scalar

For $N\ge75$, neither original nor transformed nonzero Fourier
labels are zero modulo $N$, so both Hamiltonian traces vanish.
It follows that $\det U_N(z)=\det M_N$ and
$\det U_N^{[2]}(z)=\det M_N^{[2]}$ for all complex $z$.
Both determinants are nonzero algebraic numbers.

If the companion spectrum equals $\eta$ times the original
spectrum at a given $z_0$, taking determinants makes $\eta^N$
nonzero algebraic. Hence $\eta$ is itself algebraic by algebraic
transitivity. This is valid even though no algebraicity was assumed
for a hypothetical conjugating matrix. It is the necessary step
before applying Lindemann--Weierstrass to the projective relation.

Spectral projector expansion of the two Hermitian generators makes
every characteristic coefficient an exponential polynomial with
algebraic coefficients and algebraic frequencies. Their difference
after multiplication by $\eta^k$ retains this property.
For $z_0\ne0$ algebraic, combine equal frequencies and remove zero
coefficients. The retained exponents multiplied by $z_0$ remain
distinct algebraic numbers. Theorem 1.1 of Cheng-Chao Huang,
*Explicit Bounds for Linear Forms in the Exponentials of Algebraic
Numbers*, ISSAC 2022,
[DOI 10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170),
then shows that a zero value forces the entire exponential polynomial
to be identically zero. Its precise theorem statement and publication
metadata were independently checked in the original
[author version 2, page 1](https://arxiv.org/abs/2112.05004v2).

Thus every elementary coefficient identity continues to all complex
$z$. Coincident subset sums cause no problem: they are combined
before applying the theorem. No rational independence of Hamiltonian
eigenvalues is assumed.

## 7. Highest subset sums and the contradiction

At $z=-it/N$, $t>0$, the matrices are $e^{tA_N}M_N$ and
$e^{tA_N^{[2]}}M_N^{[2]}$. In each Hamiltonian eigenbasis, the
$k$-th elementary coefficient is the finite sum of principal
overlap minors weighted by $e^{t\sum_{j\in I}a_j}$.

Strictly order the real Hamiltonian eigenvalues in decreasing order.
The first $k$ of them uniquely maximize a $k$-subset sum: any
other subset omits a larger selected eigenvalue in favor of a smaller
one. Its coefficient is nonzero by Sections 4 and 5. Therefore the
coefficient equals its unique leading nonzero exponential times
$1+O(e^{-\gamma_kt})$, with $\gamma_k>0$ for $k<N$.
For $k=N$, there is only one term.

The logarithm of its modulus divided by $t$ converges to that
largest subset sum. This remains true if the sum is negative, and
the factor is eventually nonzero. In the entire projective
coefficient identity, the constants $\eta^k$ and the leading
minors disappear after this division. All largest subset sums of
the two Hamiltonians are therefore equal. Taking successive
differences makes their ordered spectra identical, contradicting
the proved strict cubic moment gap.

This last limiting argument fixes $N$ and sends $t$ to infinity;
it is used only to contradict an entire identity. It does not make
a uniform-in-$N$ asymptotic claim or vary the parameter of the
original problem.

## 8. Final scope of acceptance

The algebraic projective scalar, the square-root sign, the failure
of a global conjugation-commuting extension, the arbitrary-subset
minor requirement, and possible repeated subset sums are all
handled correctly. The new theorems are accepted in their precise
stated scope.

They rule out identification of the exact original spectrum with
this exact companion spectrum. They do not rule out the same
limiting local statistics for the two families and do not imply
either direction of the original $H_{\rm diag}$.
