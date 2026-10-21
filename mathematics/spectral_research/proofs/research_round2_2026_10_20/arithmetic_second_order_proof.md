> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_second_order_proof.md`. Embedded SHA256: `7d6a0a28d67ab43efa4e444c26ccd25d9d981925c9af80604f3bf608e17c7770`.
> [Thematic guide](../../topics/arithmetic.md).

# Exact second-order splitting at N=49 and N=147

Research continuation, 20 October 2026. This report concerns the exact family in
the question, with no numerical replacement of the fixed rational parameter.
It proves a finite-dimensional structural result; it does not prove H_diag.

## 1. Result and provenance

**Theorem.** In dimensions N=49 and N=147, the matrix

$$
U_N(z)=\exp(izNA_N)M_N
$$

has simple spectrum for every nonzero algebraic complex number z. In
particular, both actual matrices at z=10^(-80) have simple spectrum.

The earlier first-order certificates were inconclusive in these two
dimensions. The new calculation resolves only their remaining two-dimensional
sectors, using a second-order Schur complement. It is not an additional sweep
over the 97 previously successful dimensions.

Input files, all read without modification:

| File | SHA-256 |
|---|---|
| `../research_continuation_2026_10_20/verify_spectral_simplicity.py` | `add99347a674298335226dccb58b87c35a7343a33c97053bd2310f69c07bd6cf` |
| `../research_continuation_2026_10_20/spectral_simplicity_certificates.json` | `9b35dbce426538d275574c484be5519d14f69399dbad3c14eaaeb5e44390024b` |
| `../research_continuation_2026_10_20/exact_spectral_simplicity.md` | `4aef0bf28965da0c359c01dff6e3bd330dd0cafdeb79118a5e84bd359d1ac2eb` |

The new verifier is `arithmetic_second_order.py`, and its full exact output is
`arithmetic_second_order_results.json`. The verifier checks both the input code
and initial-certificate hashes before use. Its arithmetic is over the indicated finite prime fields, with
an explicit bound excluding overflow of each integer matrix product.

## 2. Algebraic exponential-polynomial transfer

For any algebraic Hermitian matrix A, its distinct eigenvalues a_j and its
spectral projectors E_j are algebraic. Indeed,

$$
E_j=\prod_{h\ne j}\frac{A-a_h I}{a_j-a_h}.
$$

Consequently every polynomial in the entries of exp(tA) and in fixed
algebraic matrices is a finite sum of exponentials with algebraic coefficients
and algebraic frequencies. After collecting equal frequencies, any such
function can be written

$$
F(t)=\sum_{\beta\in B}c_\beta e^{\beta t},\qquad
B\subset\overline{\mathbb Q}\text{ finite},\quad
c_\beta\in\overline{\mathbb Q}.
$$

If F is not identically zero, at least one collected coefficient is nonzero.
For nonzero algebraic t, the numbers beta*t are distinct algebraic numbers.
The Lindemann-Weierstrass linear-independence theorem therefore gives
F(t) != 0. The precise theorem used is Theorem 3.2 of S. A. Popescu,
*A Simple and Self-contained Proof for the Lindemann-Weierstrass Theorem*,
published chapter DOI
[10.1007/978-3-031-51959-8_16](https://link.springer.com/chapter/10.1007/978-3-031-51959-8_16);
the theorem and its proof are also in the author's
[arXiv manuscript, Theorem 3.2](https://arxiv.org/pdf/2306.14352).
The statement applies to complex algebraic exponents, not only real ones.

Apply this to

$$
D(t)=\operatorname{disc}_X\det(XI-e^{tA_N}M_N).
$$

It remains to certify D is not identically zero. Once this is done, t=iNz
is a nonzero algebraic number whenever z is, and the theorem follows. This
step supplies no quantitative lower bound on eigenvalue gaps.

## 3. The second coefficient

The following calculation is valid over any field of characteristic other
than 2, as long as M is semisimple. Let lambda be one of its nonzero
eigenvalues, P its spectral projector, and Q=I-P. Define

$$
R_\lambda=Q(M-\lambda I)^{-1}Q
          =(M-\lambda I+P)^{-1}-P.
\tag{3.1}
$$

The first inverse on the right of the first expression is only taken on
Ran(Q). The second expression is a full matrix inverse and is what the code
uses. It also explicitly verifies PR=RP=0 and (M-lambda I)R=Q.

Let V(t)=e^{tA}M, or any matrix power series with this same second jet. Put
C=PAP restricted to Ran(P). Suppose C=aI in the current field. In the
spectral equation V(t)-X, set X=lambda*(1+a*t+b*t^2). The Schur complement
with respect to Ran(Q), divided by lambda, is

$$
t(C-aI)+t^2(H_\lambda-bI)+O(t^3),
$$

where

$$
\boxed{H_\lambda=\tfrac12 PA^2P-PAMR_\lambda AP
                    \quad\hbox{on Ran}(P).}
\tag{3.2}
$$

To check the sign and the factor lambda, the two off-diagonal blocks of V-X
start as t*PAQ*M_Q and t*lambda*QAP. Their product through the inverse of
M_Q-lambda contributes
lambda*t^2*PA*M_Q*(M_Q-lambda)^(-1)*AP, which is subtracted from the
diagonal block. Dependence of the complementary inverse on a first enters
at order t^3. This proves (3.2).

If C has distinct eigenvalues, the eigenvalues belonging to this sector
separate at first order. If C=aI and H_lambda has distinct eigenvalues,
they separate at second order in the current field. These statements can be
proved entirely formally: factor the characteristic polynomial into its
distinct lambda-clusters by polynomial Hensel lifting; then substitute
X=lambda*(1+tY), or X=lambda*(1+a*t+t^2Y), respectively. The reduced
polynomial in Y has simple roots, so the elementary simple-root Hensel
recursion gives formal roots over the algebraic closure. No division by a
formal-series degree is involved in this recursion; only nonzero root
derivatives are inverted.

## 4. Finite-jet lifting: the precise scope of a good reduction

Suppose in a finite field F_p every sector of dimension d_s is either
first-order simple, or has scalar first coefficient and simple second
coefficient. A one-dimensional sector needs neither test. Define

$$
\nu=\sum_s d_s(d_s-1)
       +\sum_{s\text{ resolved at order 2}}d_s(d_s-1).
\tag{4.1}
$$

Within a first-order sector, differences of formal roots have order 1;
within a second-order sector, order 2; between different sectors, order 0.
Since the discriminant is the product of squared root differences, its
valuation over F_p is precisely nu. Its leading coefficient is

$$
c_\nu=
\prod_{s<t}(\lambda_t-\lambda_s)^{2d_sd_t}
\prod_s\lambda_s^{d_s(d_s-1)}\operatorname{disc}(G_s),
\tag{4.2}
$$

where G_s is the characteristic polynomial of C_s for order 1, that of
H_s for order 2, and contributes 1 for dimension 1. Every factor is nonzero.
The verifier computes (4.2), using a Sylvester determinant for the small
polynomial discriminants, in addition to the squarefree-gcd checks.

One must not speak of an unrestricted exponential power series in
characteristic p. Instead, because the computed nu satisfies nu<p, use the
polynomial matrix

$$
V_{[\nu]}(t)=\left(\sum_{j=0}^{\nu}\frac{t^jA^j}{j!}\right)M.
\tag{4.3}
$$

All of its factorial denominators are invertible at p. The formal root
argument just given applies to this polynomial matrix: the first two jets
suffice to determine its discriminant valuation and the coefficient (4.2).

The characteristic-zero coefficient [t^nu]D(t) depends only on the entries
of (4.3), since the discriminant is a polynomial in matrix entries.
Therefore its reduction is the nonzero number (4.2), and [t^nu]D(t) is
nonzero in characteristic zero. This proves D is not identically zero.

**What does not follow:** the first coefficient C need not be scalar in
characteristic zero, and nu need not be the characteristic-zero order of
vanishing. Earlier coefficients might be nonzero but divisible by the
chosen prime. The proof uses only the one certified nonzero coefficient.

For completeness, the algebraic specialization is legitimate here. The
entries lie in Q(zeta_N,i,sqrt(N)), with denominators supported at 2,5 and
prime divisors of N. Both chosen primes are 1 modulo 4N and do not divide
10N. A primitive 4N-th root in F_p specifies the reduction of zeta_N and i.
Extending that prime to the field containing sqrt(N) sends sqrt(N) to one
of its two roots in F_p. If the code chose the opposite root, the whole
matrix M is multiplied by -1. The discriminant is unchanged by this
common sign because N(N-1) is even. Thus the nonzero coefficient remains
a valid characteristic-zero certificate. No assertion about a
characteristic-zero lift of the individual finite-field projectors is
needed.

## 5. Exact certificate values

| N | p | order of S mod N | reduced valuation nu | reduced leading coefficient |
|---:|---:|---:|---:|---:|
| 49 | 3529 | 21 | 92 | 1657 |
| 147 | 37633 | 84 | 246 | 32647 |

The code verifies M^r is scalar, constructs all root-of-unity projectors,
checks P_s^2=P_s and MP_s=lambda_s P_s, and checks that their dimensions
sum to N. For all other sectors the first characteristic polynomial is
squarefree. Every previously unresolved sector has dimension 2 and scalar
first compression. Their second characteristic polynomials and
discriminants are:

| N | sector k | first scalar | second polynomial X^2+c1 X+c0 | discriminant mod p |
|---:|---:|---:|---|---:|
| 49 | 2 | 2035 | X^2+2846X+3081 | 2453 |
| 49 | 6 | 2186 | X^2+1342X+1235 | 3292 |
| 49 | 9 | 2035 | X^2+2872X+2593 | 1326 |
| 49 | 13 | 2186 | X^2+2123X+2326 | 1879 |
| 49 | 16 | 2035 | X^2+1922X+25 | 2650 |
| 49 | 20 | 2186 | X^2+2556X+2088 | 3192 |
| 147 | 5 | 870 | X^2+32914X+21070 | 18844 |
| 147 | 33 | 870 | X^2+10897X+33351 | 29622 |
| 147 | 61 | 870 | X^2+13021X+36179 | 15592 |

All numbers in this table are field residues, not characteristic-zero
eigenvalues or approximations to tau. The JSON records the full matrices,
projector pivot rows/columns, all first-order checks, and the chosen field
embeddings. Running

```
python arithmetic_second_order.py --dimensions 49 147
```

reconstructs both certificates from the original definitions.

## 6. Consequences and limits

The two persistent failures of the earlier first-order test were not
evidence for persistent spectral degeneracy. A nonzero second-jet
discriminant certificate closes those two finite cases at the actual
algebraic parameter, without relying on a small-tau approximation.

Together with the previously proved finite certificates, all odd
dimensions from 3 through 201 except 7 are now certified simple at every
nonzero algebraic parameter. That statement combines old and new results;
only 49 and 147 were computed in this pass. The genuine exception at N=7
is a single finite dimension and is not an asymptotic counterexample.

There is still no proof of simplicity for all remaining odd N, no uniform
lower bound on spectral gaps, and no proof or counterexample to H_diag.
The companion report `arithmetic_oldspace_escape.md` treats the distinct
infinite-dimensional mechanism of inherited canonical old subspaces.
