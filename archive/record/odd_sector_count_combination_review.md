# Independent check of the odd-sector combination

Verdict: proved as written relative to the named accepted component theorems.
The combination was derived afresh from the displayed embeddings and complete
cat-group statements. This is an internal mathematical review of disjointness,
thresholds, counting, and transfer. It is not a fresh audit of the underlying
residual-125 or odd-newest kernel proofs and is not an external referee report.

## Exact reviewed statement

For N=7*5^e and every nonzero real algebraic t, the lower bounds are 24N/25
for odd e>=3, 24N/25+35 for odd e>=5, and 24N/25+875 for odd e>=7. The last
875 is exactly 120*7+(7+7+7+4+5+5). It does not mean 875+35.

## Source and review bindings

All originals below are indexed by role and hash in
`evidence/odd_newest_20261007/original_index.json`, with lossless base64 bytes.

- Odd newest source: a75bd91a452d5285ec447d9ca1be623e8eda3218835ce2ed9af71f741e8872c0.
- Odd newest independent review: 43d7e05efefb0905742b28f82b93c29e3de3eccc40e1189b1894e32912889dd9; final review manifest: 6810fbf4bcd9625d29b48f8b1b33b6dab9c5966da8bc2fc0fb4549de8120f87b.
- Residual-125 source: 9efdd0257feae0d20c583e8ee94c0d8e1cee36c45d275cd4a5347a269c6b095a.
- Residual-125 independent review: 2adfb22893df719fa8e650c34a70bd0e277148e10ae7bdc8df2d3ad37446172e; final review manifest: 421550655307c0361f35b50c73daf029dceac1874a8e5a076fe88d4a7ff0df7d.
- Accepted oldform tower, maintained snapshot: 506064db5360f204360f54cb8598e61d5db50d9fa3d0589dc8fc289271a6eeb1. Original tower proof: d359482763667a6707ed9a060a3874e951f95336561a4ac645df453022b085ae. The exact displayed embedding and complete-eigenspace argument agree.
- Deepest odd-core source: 38b1e1b442f942a81a3ea7f89c9bd6a91f4a6ed39f12beb644d0c44064d0b46e. Its historical candidate header is superseded by the acceptance bound in the accepted rank review, which names odd-core report 2b8f451ebca20251be2dec5864e8d8a6497eabeb4259cc5edcbc28da33ede101.
- Accepted algebraic-time rank-transfer source: 2890bddc3a6a67814233014f070313fa9b0a7e24acbc3f68a403a2d2f416090a.
- Accepted cat/jet/rank review: 2f291fdfb43f081066479847d1cda550653ecd91880d2fa15edd2c16f50ce7bb. Its complete-group and odd-core sections explicitly supply six groups of sizes 7,7,7,4,5,5 for odd e>=5. Its external-source section binds the existing Popescu arXiv:2306.14352v2, Theorem 3.2, application. No external theorem is added or newly verified here.

## Obligations checked

1. Ambient modulus: the residual theorem uses n=125*5^(2j), so its j>=2
   hypothesis is exactly odd e=2j+3>=7. It is not applied at e=5.
2. Containment: direct substitution in J_j gives J_j=J_1 J_(j-1);
   hence the residual-125 space lies inside W_1. The deepest core is the
   nested W_(j+1), whose index is (e-1)/2.
3. Completeness: the tower theorem gives full ambient product-cat eigenspaces,
   not invariant proper pieces. Its cubic-orbit isolation prevents overlap
   of the initial eigenvalue labels inside and outside each W_k.
4. Residual count: 120 new groups times seven is 840; the six old groups sum
   to 35, exhausting 7*125=875. The old groups are inherited, not added twice.
5. Local addition: finite initial group separation permits one common small
   real punctured interval for all selected branches, even though the new
   sector splits at first order and the residual groups at second order.
6. Transfer: rank chi_t'(U_N(t)) counts simple eigenvalues exactly at real t.
   The inherited coefficient-separation theorem transfers the lower bound;
   no target-time invariant-subspace assumption enters.

At the thresholds, the bounds are 840 of 875 dimensions (e=3), 21035 of
21875 (e=5), and 525875 of 546875 (e=7). These arithmetic evaluations are
consistency checks, not a substitute for the uniform embedding argument.

No gap was found in this combination. Its exact stopping boundary is a lower
bound on the count of simple eigenvalues. Full simplicity, quantitative gaps,
BGS, and the first-old follow-on remain outside its conclusions.
