# Review of the all-order Cayley trace limit

Base revision: `d6086cfa9ce9be37aa3d936875e8ec1da3edf811`.
Date: 9 September 2026.

## Mathematical outcome

The new note `mathematics/cayley_trace_gaussian_limit.md` and Section 13 of
the unified manuscript prove:

- a weighted length-`r` cyclotomic collision budget `O_w(K^r)`;
- a Gaussian limit for the full normalized Cayley--Jacobi trace when
  prime `K->infinity`, `p=1 mod K` is prime, and `K=o(log p)`;
- independent joint Gaussian limits at finitely many distinct positive
  fixed integer multiples of the additive parameter;
- convergence of these conditional empirical laws in probability over
  dyadic split designs with `Q->infinity` and `log Q=o(log X)`.

The inputs are Chowla independence and, for the density version,
Bombieri--Vinogradov/PNT. The norm argument controls each entire Galois orbit
through one resultant, avoiding an extra factor of `K`.
The normalization and omitted zero frequency are treated exactly.

## Review findings and corrections

An independent review first examined the complete mathematical proposal,
then its weighted extension, and finally the actual Markdown and TeX files.
It checked the balance criterion, free action, valuation multiplicities,
ramified factor, Gaussian covariance, varying-modulus denominator, and the
passage from moments in probability to laws in probability.

The final file review found a domain defect: the exact weighted identity
could evaluate `X(0)` when a prime divides a weight, although `X` had initially
been defined only at nonzero arguments. Both definitions now cover all of
`F_p` with `X(0)=sqrt(K-1)`; empirical sampling still excludes zero.
The added exact case `K=3, w=(7), p=7` exercises this boundary.
No other proof gap was identified in the reviewed statements. This is a
scoped internal review, not external journal certification.

The final review examined pre-correction SHA256 values
`2ea66a57b8be417f53589f9ebacbd3c0e9ed70c5f23315a98032768657230203`
(mathematical note) and
`00a8deabac2a5282c7173f00cc54a908408182439b4d2e1d0e8aefb6df5ab982`
(TeX section). The only subsequent change to those proof files is the
domain correction just described; final hashes are in the associated
verification certificate.

## Evidence

| Check | Result and scope |
|---|---|
| All-order exact verifier | 32 word/order designs; 6,440 ordered tuples represented by 1,242 complete scaling orbits; 1,183 nonzero resultants; 13,293 orbit-valuation comparisons |
| Independent arithmetic reconstruction | Integer convolution agrees with the orbit reconstruction at every split prime through 257 for each listed word/order design |
| Negative controls | `(11,199)` and `(13,521)` have the exact fourth-order baseline but additional third- and sixth-order relations |
| Domain control | Nonsplit pair `(11,521)` is rejected; a split prime dividing a fixed weight is included |
| Existing Jacobi identity regression | Pass at its maintained designs; complex floating-point comparison, not an exact proof |
| Figure | All nonzero frequencies at `(11,199)`, `(31,100069)`, `(101,1000507)`; double-precision FFT; explicitly numerical |
| Repository structural audit | Pass; new verifier is automatically included by the existing verification runner |
| Manuscript | Three-pass build with the existing overflow/reference/hash gate; 157 pages; new section and contents inspected visually |
| Lean | No new Lean claim; the analytical limit theorem is not formalized |

The exact and numerical certificates are respectively
`evidence/certificates/cayley_higher_moments_20260909.json` and
`evidence/certificates/cayley_trace_illustration_20260909.json`.
The full Python/C++/Lean corpus was not rerun in this scoped pass.
The 106-check / 16-module result recorded on September 8 remains dated
evidence, not a claim about fresh execution here.

## Prior work and closed routes

Wang's Theorem A was checked in the article text. Fouvry--Iwaniec's published
restatement supplies a source locator for the classical average
prime-distribution input. Untrau's fixed-cardinality subgroup-sum
equidistribution is related prior work on torus pushforward laws. The present
source screening does not establish novelty of the growing-order Cayley
specialization or of its method.

The shifted-subgroup route did not improve the uniform sparse `8/3`
exponent: a per-orbit shifted energy bound still loses information when
summed globally. Multiplicative irreducibility by itself does not fill that
gap. The exact fourth-baseline counterexamples reject a shortcut from the
previous fourth-moment theorem to a CLT.

The all-order route succeeds only in its stated regimes. For
`Q=X^theta` the normalized order-`r` error contains `Q^(r/2+1)/X`, and
the admissible positive threshold in `theta` tends to zero with `r`.
The next distributional target is a fixed-polynomial-scale CLT; the first
missing ingredient is an all-order estimate without this growing exponent
loss, or an alternative control of characteristic functions.

The BGS target remains separate: prove desymmetrized joint traces of powers
of one quantum propagator at Heisenberg times. Parameter multiples of a full
Jacobi matrix are not those powers. Neither full BGS, a sparse pointwise
quadratic energy theorem, nor a world-priority discovery is claimed.
