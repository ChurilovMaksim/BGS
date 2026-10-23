# Curated first-seven review

This is an editorial copy of the accepted independent review. The original
bytes are retained at `record/history/2026/first_seven_20261006/independent_review.md`.
Commands and filenames below describe the historical independent execution;
portable replays are recorded separately and do not impersonate those runs.

# Independent audit: first unramified seven-primary actual commutant

## Claim and verdict

**Verdict: proved as written**, as a computer-assisted project theorem.

For every odd integer `N > 7` satisfying `7 | N`, `49 ∤ N`, and `5 ∤ N`, the complex joint commutant of the unchanged prescribed matrices `A_N,M_N` is exactly `C I`.

This audit independently reconstructs the mathematical reduction and the finite polynomial certificate. It is not formal verification or external peer review. It does not prove spectral simplicity, a quantitative gap, a Heisenberg trace estimate, or BGS. It gives no theorem at `5 | N`.

The audited proof is `record/history/2026/first_seven_20261006/accepted_proof.md`, SHA-256 `f154f26b67cf15ae537b99616b8f3b777e39afb9c046334a9773307129648727`. All 29 entries of `first_seven_candidate_manifest.json` were hash-checked. No candidate or canonical file was edited. All review writes are confined to `the original independent-review workspace`.

The checkout HEAD during this audit was `300d99270d11c87d0aa84e9d8f624491788629ba`, and the checkout had pre-existing integration changes. The candidate names the earlier base `d4132ccee82849b644520d88c953cb9b33382a59`. The authoritative actual-model definition `mathematics/fixed_model_symmetry_theorem.md` and the prior `frozen_algebraic_spectral_simplicity.md` are byte-identical between that base and the files audited here. Their hashes and the authority/status snapshots are recorded in `authority_snapshot.json`.

The previously accepted higher-seven-primary theorem was read for its actual-model dictionary and scope only. Its proof and bytes were not changed; its accepted status is not being reopened or replaced by this audit.

## Dependency graph and obligations

The logical chain is:

1. The raw modular Weyl definition gives the displayed Jacobi generator and quadratic metaplectic kernel.
2. Integral reduction at characteristic five gives seven unit-weight upper chains when `5 ∤ N`.
3. Simultaneous diagonal conjugation gives `J_L ⊗ I_7` and the actual gauged kernel.
4. Four exact boundary block equations give necessary endpoint-free constraints on the leading Toeplitz coefficient.
5. An explicit Fourier/bond dictionary turns those constraints into `M_l(q)`.
6. Exact determinant identities and exact root-exclusion identities give rank 48 for every nonzero odd-order `q` over the algebraic closure of `F_5`.
7. The leading coefficient is scalar; invertibility of the corner block kills every Toeplitz tail.
8. A nonzero commutator-rank minor lifts from characteristic five to characteristic zero.

Obligation status:

- Actual model and raw midpoint convention: passed.
- Characteristic-five integral reduction and unit bonds: passed under `5 ∤ N`.
- Four boundary equations, including signs: passed by fresh block multiplication.
- Cross-ratio and nontriviality of its scalar: passed by fresh Fourier calculation.
- Removal of the arbitrary long endpoint diagonal: passed, as necessary conditions only.
- Six-class Fourier exponent and the relative scalar `w²`: passed algebraically and by independent finite controls.
- Polynomial degree bounds and 937-node identity argument: passed.
- Field encoding and field arithmetic: passed independently.
- All 18 determinant polynomials, exact gcds, three-term Bezout identities and quotient identities: passed independently.
- Excluded factors, degree-6/34 decomposition, coprimality, field containment and odd-order exclusion: passed independently.
- Primitive seventh-root conjugacy: passed.
- Smallest depth and tail elimination: passed; no depth-21 hypothesis is needed.
- Characteristic-zero lift: passed.
- Ramified `5 | N` extension, spectral simplicity, quantitative estimates and BGS: out of scope.

There is no unverified external theorem leaf in the new common-commutant argument. Its general ingredients are elementary matrix algebra, polynomial interpolation, finite-field root orders, and a nonzero-minor specialization argument. The independent C++ finite computation is a load-bearing exact certificate check, not merely a finite-dimensional experiment.

## Fresh derivation of the actual reduction

Let `h=2^{-1} mod N`, `L=N/7`, and `a=1-h`. Use positions `x_(t,j)=a+t+jL`, with `0 ≤ t < L` and `0 ≤ j < 7`. The actual entries are

`1000 A_N(x,x+1)=(-3-4i) r((x+h)/N)`,
`1000 A_N(x+1,x)=(-3+4i) r((x+h)/N)`,

and `G(x,y)=q^{-8^{-1}(3x²-2xy+3y²)}`, where `G=sqrt(N) M_N`.

The exact Laurent identity is

`r(z)=-(z^7-1)^2(z+1)^2/(4z^8)`.

At the Gaussian prime with `i ↦ 2` in characteristic five, the upper coefficient is 4, the lower coefficient is 0, and every diagonal term of `1000 A_N` vanishes. For an internal bond `u=1,...,L-1`, the root is `z=q^u w^j`, with `w=q^L`. Then `z^7=q^{7u} ≠ 1`, and `z ≠ -1` since its order is odd. Thus every internal bond is a unit. The omitted bonds have `z^7=1`, giving exactly seven length-`L` chains.

Set `D_0=I` and `D_(t+1,j)=D_(t,j)/b_(t+1,j)`. Then `D^{-1} B D=J_L⊗I_7`; the same conjugation must be applied to `G`. This is the actual characteristic-five specialization, not a characteristic-zero upper-truncation surrogate.

## Four boundary equations

A commuter with `J_L⊗I_7` has blocks `X_(t,s)=C_(s-t)` for `s≥t`, zero otherwise. Write the gauged corner blocks as

`E0=Gtilde_(L-1,0)`, `E1=Gtilde_(L-1,1)`,
`F0=Gtilde_(L-2,0)`, `F1=Gtilde_(L-2,1)`.

Directly computing `X Gtilde - Gtilde X` at these four positions gives

`[C0,E0]=0`,
`[C0,E1]=E0 C1`,
`[C0,F0]=-C1 E0`,
`[C0,F1]=F0 C1-C1 E1`.

These formulas use no discarded higher coefficient: at the last row only `C0` appears on the left, and at the penultimate row only `C0,C1` appear. They are valid already at `L=3`, the smallest admissible odd depth.

If `A,B,C,T` are the four raw blocks in the same order, `R=D_(L-1)^{-1}`, `D1=diag(b_1^{-1})`, and `Dl=diag(b_(L-1)^{-1})`, the simultaneous gauging gives exactly

`E0=R A`, `E1=R B D1`, `F0=R Dl C`, `F1=R Dl T D1`.

## Cross-ratio, freshly computed

Let `Z=diag(w^j)`, `U=Z²`, `l=L mod 7`, and `rho=2l`. Put `x0=L-h`, `y0=1-h`. The raw kernel ratios give

`B=beta U A Z`,
`C=gamma Z^6 A Z^5`,
`T=beta gamma delta Z^6 U A Z^6`,

where

`beta=q^{(2x0-6y0-3)/8}`,
`gamma=q^{(6x0-2y0-3)/8}`,
`delta=q^{-1/4}`.

All fractions here use inverses modulo `N`. After invertible diagonal factors, `A` is the Fourier matrix `w^{rho jk}`, so it is invertible because `rho ≠ 0 mod 7`.

The matrix `A Z^5 A^{-1}` is a diagonally weighted shift with row `j` supported at column `j-L^{-1}`. Consequently

`(A Z^5 A^{-1}) U = eta U (A Z^5 A^{-1})`,
`eta=w^{-2L^{-1}}`.

It follows that `T=theta C A^{-1} B` with `theta=delta/eta`; the gauged identity is `F1=theta F0 E0^{-1} E1`. If `theta=1`, then `q^{-1}=delta^4=eta^4` belongs to the seventh roots, forcing `q` to have order dividing 7. This contradicts `N>7`. Thus `theta-1` is nonzero in the actual residue field.

## Endpoint-free constraints

Define `J=E0^{-1}F0=A^{-1} Dl C` and `K=E0^{-1}E1=A^{-1} B D1`. The four equations imply

`C1=[C0,K]`,
`[C0,J]=-E0^{-1} C1 E0`.

Substituting the cross-ratio into the fourth equation gives

`(theta-1)(F0 C1-C1 E1)=0`.

Hence `[C0,JK]=E0^{-1}(F0 C1-C1 E1)=0`.

The first equation also gives `R^{-1} C0 R=A C0 A^{-1}`. Since `R` is invertible diagonal, its conjugation preserves each diagonal entry. Therefore

`diag(C0-A C0 A^{-1})=0`.

Similarly `A[C0,J]A^{-1}=-R^{-1} C1 R`, so

`diag([C0,K]+A[C0,J]A^{-1})=0`.

These are necessary conditions; no converse is asserted or needed. They remove every long endpoint-product entry without treating it as an arbitrary favorable gauge. In particular they do not invoke a false scalar q-commutation or disjoint-spectrum assertion.

## Fourier and polynomial dictionary

Expanding the raw exponent at `x=x0+jL`, `y=y0+kL` shows, up to its nonzero constant `(0,0)` entry,

`A_l(j,k)=w^{-3l(j²+k²)+2l jk+(l+4)j+(2l+3)k}`.

Here `h=4 mod 7`, so the linear coefficients are forced by the raw modular convention. No ordinary-midpoint replacement is involved.

In characteristic five the first and last inverse-bond scalars are

`b_1(j)^{-1}=kappa_1 z_j (1+q z_j)^{-2}`,
`kappa_1=-q^8/(q^7-1)^2`,

`b_(L-1)(j)^{-1}=kappa_l z_j (1+w q^{-1}z_j)^{-2}`,
`kappa_l=-w q^6/(q^7-1)^2`.

Since `beta/gamma=q^{-(x0+y0)/2}=w^3`, one obtains

`J=nu A_l^{-1}(1+w q^{-1} Z)^{-2} A_l U^{-1}`,
`K=nu w² q² A_l^{-1} U A_l U(1+q Z)^{-2}`,

with `nu=kappa_l gamma ≠ 0`.

The exact geometric-series identities are

`S_c(q,z)=(q^7+1)/(q+wz)`,
`S_q(q,z)=(1+q^7)/(1+qz)`

on `z^7=w^7=1`. Therefore

`J=lambda Jbar`, `K=lambda w² Kbar`,
`lambda=nu q²/(1+q^7)^2`.

Both denominators and the individual bond factors are units: `q ≠ 0`, `q^7 ≠ 1` for primitive `N>7`, and `q^7 ≠ -1` for odd-order `q`.

Substitution gives precisely the candidate's 63 equations. The independent implementation builds `S_c,S_q` as their seven-term sums, forms `Jbar,Kbar` by direct matrix multiplication, and constructs each equation coefficient by the action on the elementary matrix `E_uv`. It does not import the candidate's polynomial coefficient arrays or NumPy Kronecker construction.

Independent split-prime raw-model tests verified all six residue classes at:

- `N=21, L mod 7=3, p=337`;
- `N=63, L mod 7=2, p=757`;
- `N=77, L mod 7=4, p=617`;
- `N=91, L mod 7=6, p=1093`;
- `N=133, L mod 7=5, p=1597`;
- `N=203, L mod 7=1, p=2437`.

They checked the Fourier dictionary, raw and gauged cross-ratios, and common-scalar normalization. These six checks are corroboration of the algebra above, not the universal proof.

## Independent exact certificate verification

### Field

`review.cpp` implements `F_5[t]/(t^6+t^4+3t^3+t²+1)` with ascending base-five coefficient codes. It independently implements polynomial multiplication and reduction, addition, negation, log/antilog arithmetic, matrix inversion, Gaussian determinants, polynomial arithmetic, Euclidean gcds, and binary modular exponentiation.

Direct multiplication by `t+4` enumerated every one of the 15,624 nonzero coefficient tuples exactly once and returned to 1. Thus every nonzero element of this quotient ring is a unit; this independently establishes that the quotient is a field and its modulus irreducible. The logarithm table is thereby certified, rather than assumed. An additional 156,250 products were compared directly with polynomial convolution/reduction. The class `t` has order 63; `w=t^9`, code 1208, has order 7. Order 63 also proves that the modulus divides `Phi_63` in characteristic five.

### Polynomial identities, not dimensional sampling

For each of six classes, all three recorded row selections were checked to have 48 distinct rows: six degree-0 rows, six degree-12 rows, and 36 degree-24 rows. The determinant degree is therefore at most 936. Every recorded polynomial has degree at most 936. The 937 encoded nodes are pairwise distinct field elements, even though the base characteristic is five: they are coefficient codes, not residues of ordinary integers modulo five.

For each of the 18 minors the fresh implementation checked:

- all 937 determinant values against both the recorded values and the recorded polynomial;
- ten additional nodes, 12000 through 12009.

This totals 17,046 independently rebuilt determinant evaluations, of which 16,866 establish the polynomial identities. The degree bound and 937 distinct equality points imply exact identities over the coefficient field and every extension. The ten extra points are only additional controls.

The same implementation recomputed each monic three-polynomial gcd by the Euclidean algorithm. It also verified all supplied three-term Bezout identities and all three quotient identities, and rebuilt the gcd from its removed factors and remaining components. The exact minor degrees and gcd degrees match the proof.

All removed linear roots were separately checked to be zero or to satisfy `q^7=-1`. Each remaining degree-40 polynomial was reconstructed as the product of its degree-6 and degree-34 components; their gcd was checked to be 1.

### Odd-root exclusion

For the two components, the implementation verified by separately written binary powering

`B_6 | q^(5^18)-q`, `B_34 | q^(5^102)-q`,

then recomputed the remainders of the odd powers and independently verified both gcds equal 1 and their explicit Bezout identities. In both cases `v_2(5^m-1)=3`; this was also calculated from exact binary integer representations.

Every root of either component is therefore in the indicated finite field. If such a root had odd order, its order would divide the full odd part `(5^m-1)/8`, contradicting the corresponding gcd. Neither residual component has an odd-order root. The discarded `q^7=-1` factors likewise have no odd-order roots in characteristic five.

Consequently the three minors cannot vanish simultaneously at any nonzero odd-order `q` in the algebraic closure. This establishes rank 48 uniformly. The argument does not infer universal rank merely from generic rank or successful sample dimensions.

Since `ord_7(5)=6`, the six primitive seventh roots are exactly the Frobenius conjugates of the chosen `w`. Applying a field automorphism to both coefficients and `q` preserves rank and odd multiplicative order. Thus the fixed-`w` certificate covers the actual root `w=q^L` in every case.

## Small depths, tails, and lifting

Once `C0` is scalar, the first boundary equation for column depth 1 gives `E0 C1=0`, hence `C1=0`. At every later depth `s`, the last-row equation is

`0=sum_(d=1)^s E_(s-d) C_d`.

Induction makes every earlier `C_d` zero, leaving `E0 C_s=0`. Invertibility of `E0` therefore kills all tails. There is no Casoratian or seven-column depth threshold in this argument.

`actual_small.cpp` constructs the actual characteristic-five raw quadratic kernel and all actual internal bonds directly, gauges the entire pair, and forms all commuting equations on the complete block-Toeplitz centralizer of the reduced generator. It finds:

- `N=21, L=3`: rank 146 on 146 scalar-quotiented unknowns; common commutant dimension 1.
- `N=63, L=9`: rank 440 on 440 scalar-quotiented unknowns; common commutant dimension 1.
- `N=7, L=1`: rank 32 on 48 scalar-quotiented unknowns; residue common commutant dimension 17.

The last check is a control, not a claim that characteristic-zero nullity follows from reduction. The genuine characteristic-zero exception follows directly: at `N=7`, `r` vanishes at every relevant root, and `A_7=(9/10) I`; the commutant of `M_7` alone is non-scalar. Thus the exclusion is necessary.

Finally work over the cyclotomic Gaussian ring with 2 inverted. Since `5 ∤ N`, reduction can retain a primitive `N`th root. The entries of `1000 A_N` and `G` are integral there. A nonzero `(N²-1)`-minor of their reduced joint-commutator map is the reduction of the corresponding characteristic-zero minor, which therefore cannot vanish. The characteristic-zero kernel has dimension at most one and contains `I`, hence is exactly scalar; scalar extension to `C` preserves this rank. Neither a lifted idempotent nor reduction of an arbitrary complex commuter is needed.

At `5 | N` these unit and primitive-root arguments fail. Nothing in the certificate repairs that failure.

## Commands, execution, and durable evidence

From this review directory:

```
python3 serialize_inputs.py
g++ -std=c++17 -O3 -o review review.cpp
./review independent_inputs.txt
python3 dictionary.py
g++ -std=c++17 -O3 -o actual_small actual_small.cpp
./actual_small
```

`serialize_inputs.py` performs only JSON-to-plain-text serialization and checks field metadata; it imports no candidate code. `review.cpp`, `dictionary.py`, and `actual_small.cpp` were written independently in this audit. `actual_small.cpp` reuses this audit's own field/matrix utilities, not the author's implementation. Runtime receipts and logs distinguish independent verification from author replay.

Evidence files:

- `verified_input_hashes.json`: all 29 candidate artifact hashes;
- `authority_snapshot.json`: authority/model hashes, HEAD and software versions;
- `independent_check.log`, `independent_check_receipt.json`: full determinant and polynomial certificate verification;
- `dictionary_results.json`, `dictionary.log`: six-class raw-model dictionary controls;
- `actual_small.log`, `actual_small_receipt.json`: exact actual residue checks at 7, 21 and 63;
- `review_artifact_manifest.json`: review artifact hashes and final input-integrity recheck.

An initial build attempt found no Boost multiprecision headers. The final verifier instead implements the required integer exponents as exact binary digit vectors and needs only the C++ standard library. An attempted `/usr/bin/time` wrapper was unavailable; no mathematical check ran in that wrapper. The successful runs were timed with Python's monotonic clock and `resource` module. These environment failures did not change the inputs or mathematical scope.

## Remaining gap and strongest safe conclusion

There is no remaining gap in this theorem's stated scope, subject to the ordinary trust in exact computation and the reviewed algebra. The new certificate supports the universal first-seven-primary theorem, not merely the listed sample dimensions.

Combining it with the separately accepted `49 | N, 5 ∤ N` theorem and the prior `7 ∤ N` result gives scalar actual common commutant for all odd `N ≥ 3` with `35 ∤ N`, except `N=7`. This combination preserves each prior theorem's own review boundary. The family of odd multiples of 35 remains unresolved here. No further dimensional sampling is needed for this certificate; the next useful work is integration of this precisely bounded theorem and its independently verified certificate, followed by a separate ramified analysis if desired.
