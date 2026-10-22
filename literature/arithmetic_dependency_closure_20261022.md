# Arithmetic dependencies: exact scope and project use

**Reviewed:** 22 October 2026. **Claims:** BGS-CAYLEY-006 and BGS-CAYLEY-007.
This is a source-to-proof check by the editing agent, not independent refereeing
or a priority determination. The five registered inputs below were missing
from the dependency metadata; their use was already present in the proofs.

## Prime cotangents and the Gaussian limit

Kai Wang, [*On a theorem of S. Chowla*](https://doi.org/10.1016/0022-314X(82)90078-6),
J. Number Theory **15** (1982), 1–4, **Theorem A, p. 1**, states rational
independence of the cotangents at the first half of the nonzero residues for
prime order. This supplies precisely the prime-order independence needed in
[CAYLEY-006](../mathematics/cayley_trace_gaussian_limit.md) to classify its
rational relations as balanced. Composite orders and Wang's derivative
extension are not used. Registry ID: `EXT-WANG-1982`.

The indexed primary PDF text was inspected through the web retrieval service;
publisher metadata agrees. Direct PDF download returned HTTP 403, so this
review supplies neither a local byte hash nor visual page authentication for
this source. This limitation is preserved in the metadata receipt.

## Averaging primes in residue classes

Étienne Fouvry and Henryk Iwaniec,
[*On a theorem of Bombieri–Vinogradov type*](https://people.math.ethz.ch/~kowalski/fouvry-iwaniec-on-a-theorem.pdf),
Mathematika **27** (1980), 135–152, **§1, equation (1), p. 135**, restate the
classical Bombieri–Vinogradov estimate with main term
$\pi(x)/\varphi(q)$, any fixed logarithmic saving, and moduli below
$x^{1/2-\varepsilon}$. We use that restatement, not their enlarged-range
result. In the density theorem, $Q=X^{o(1)}$ eventually lies in this range
with $\varepsilon=1/4$, at both endpoints $X$ and $X/2$. Restricting the
nonnegative modulus sum to prime $K$ and taking the dyadic difference gives
the required average error. Registry ID: `EXT-FI-1980`.

Accordingly equation (21) of the Markdown and TeX proofs now retains the
exact factor $\pi(X)-\pi(X/2)$. This avoids requiring a quantitative prime
number theorem merely to replace that factor with logarithmic integrals.
The asymptotic denominator and all conclusions are unchanged.

Don Zagier, [*Newman's Short Proof of the Prime Number Theorem*](https://doi.org/10.2307/2975232),
Amer. Math. Monthly **104** (1997), 705–708, **p. 705 and the deduction from
(VI), p. 707**, supplies the qualitative prime number theorem. Partial
summation then gives the prime reciprocal sum over $(Q/2,Q]$; the same
theorem gives $\pi(X)-\pi(X/2)\sim X/(2\log X)$. No specified logarithmic
remainder is inferred. Registry ID: `EXT-ZAGIER-1997`.

## Characteristic functions to distribution functions

Bence Borda,
[*Berry–Esseen smoothing inequality for the Wasserstein metric on compact Lie groups*](https://arxiv.org/abs/2005.04925v2),
**v2, 23 June 2020, Theorem A, p. 2**, restates the classical real-line
Kolmogorov smoothing inequality. The empirical law may be discrete; the
target Gaussian distribution function is Lipschitz. These are the hypotheses
needed by CAYLEY-006. The paper's compact Lie group extensions are not used.
Registry ID: `EXT-BORDA-2020`.

## Polynomial subresultants

W. S. Brown and J. F. Traub,
[*On Euclid's Algorithm and the Theory of Subresultants*](https://doi.org/10.1145/321662.321665),
J. ACM **18** (1971), 505–514, **§5, pp. 507–508 and the Fundamental Theorem,
equations (26)–(29), p. 511**, give the polynomial subresultant criterion.
In [CAYLEY-007](../mathematics/cayley_product_row_real_trace_ideal.md), unit
leading coefficients keep both degrees fixed after reduction to each residue
field. Vanishing of the first three polynomial subresultants is therefore
equivalent to gcd degree at least three. The defining ideal uses every
coefficient of these polynomials, not just principal coefficients. The
argument is used for $K\ge7$; the stated conventions at $K=3,5$ remain
separate. Registry ID: `EXT-BT-1971`.

## Evidence and limits

The Fouvry–Iwaniec, Borda and Brown–Traub theorem pages were inspected as
rendered PDF pages. Zagier's primary PDF text was inspected. The four
downloaded PDFs have byte hashes in the
[new metadata snapshot](../evidence/source_metadata/registry_metadata_20261022_recheck.json).
The papers themselves are not redistributed. Earlier source observations
are carried forward with their original dates; this review does not refresh
the other 52 references or certify the full project bibliography.
