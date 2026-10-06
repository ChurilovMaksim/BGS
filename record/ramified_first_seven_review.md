# Curated independent ramified first-seven review

Editorial copy only; the exact accepted original is retained in
record/history/2026/ramified_first_seven_20261006/independent_review.md. Historical commands
describe the original audit, while portable execution receipts are separate.

# Independent audit: ramified first-seven chain-trace theorem

Date: 2026-10-06. Primary verdict: **proved as written**. Repository vocabulary: **verified in stated scope**.

## Exact claim and reviewed revision

For every odd integer N>7 with 7|N and 49∤N, the common commutant over C of the prescribed, unchanged BGS matrices A_N and M_N is C I. No restriction on v_5(N) is needed. This is a common-commutant theorem for the pair, not spectral simplicity or a statement that the full complex commutant of the single propagator U_N is scalar.

Reviewed candidate: `record/history/2026/ramified_first_seven_20261006/accepted_proof.md`, SHA-256 `b9aab9a0edbf91ef2e6ab477e52f24ec3a5ff0b9cf661bcb98e613cfb8ab3d17`. All six source/data hashes in its candidate manifest were verified. The independently constructed computation is `independent_check.py`; complete finite output is `independent_results.json`.

The canonical repository was read-only throughout this audit. Its observed HEAD was `66724291b2ec77c22823f52ecc5ee56278fed096`, newer than the candidate's declared base `d4132ccee82849b644520d88c953cb9b33382a59`. A read-only git comparison found no changes between those commits in the four model/valuation/coefficient sources used below. Neither accepted higher-seven proof nor accepted unramified first-seven proof was edited or used as an unverified substitute for this argument.

## Dependency graph and obligation matrix

The proof dependency chain is:

1. Exact modular-Weyl Jacobi generator and quadratic metaplectic kernel.
2. Elementary cyclotomic 5-adic valuations and explicit diagonal gauge.
3. Rank-seven endpoint reduction and Toeplitz commutant of identical Jordan blocks.
4. Integral block-trace consequence of the actual commutator.
5. Exact normalization of the two rational chain-trace harmonics.
6. Polynomial gcd/Bézout certificate and exhaustive seven-point collision classification.
7. Elementary nonvanishing of Fourier minors of sizes at most three.
8. Partition-block scalarity and rank lifting of an augmented integral linear system.

Every listed obligation passed. The mathematical steps 1–5 and 7–8 were reconstructed independently. The finite inputs in 5–6 were recomputed independently in a different finite-field representation. There is no conditional external theorem leaf in this proof. In particular no Lindemann–Weierstrass statement, spectral-projector specialization, idempotent-lifting hypothesis, or invertibility of the full reduced Fourier matrix is required.

| Obligation | Finding |
|---|---|
| Actual model and modular half-shift | Passed; canonical formulas match the candidate |
| eta nonzero, including N=7·5^e | Passed; eta vanishes only at the excluded N=7 |
| All gauge and perturbation valuations | Passed, with explicit margins below |
| Full-rank seven-dimensional endpoint | Passed even when 5 divides N |
| Removal of higher Toeplitz coefficients | Passed by disjoint corner supports |
| Added trace equation follows from actual commutation | Passed exactly before reduction |
| Integrality after division by alpha | Passed for every stated N |
| Two-harmonic formula at residue order seven | Passed using error valuation 1−c>0 |
| gcd, Bézout, and all nine collision partitions | Passed by fresh exact computation |
| 2×2/3×3 Fourier-minor proof | Passed analytically and exhaustively |
| Scalarity, augmented-rank lifting, complex base extension | Passed |
| N=7 and higher-seven ramified exclusions | Correctly preserved |

## 1. Reconstruction from the actual model

The canonical definitions used are `BGS/mathematics/fixed_model_symmetry_theorem.md`, §1, and `frozen_seven_cut_reduction.md`, exact normalization. Write q=ζ_N, h=2^{-1} mod N, a=1−h=h mod N, N=7L, and x_(u,j)=a+u+jL. The actual matrices satisfy

- B=1000A;
- B(x,x)=1000 cos(14πx/N)+100r(x/N)+10r(x/N)sin(2πx/N)−100;
- B(x,x+1)=(-3−4i)r((x+h)/N);
- B(x+1,x)=(-3+4i)r((x+h)/N);
- G=√N M, G(x,y)=q^{-8^{-1}(3x²−2xy+3y²)}.

The Laurent identity is r(z)=−(z^7−1)^2(z+1)^2/(4z^8). The bond from depth u−1 to depth u has z=q^(u+jL). Because z^7=q^(7u), the zero bonds are exactly the seven chain endpoints; internal bonds have 1≤u<L and are nonzero. Thus these are seven length-L paths of the actual generator, without deleting any nonzero bond or changing quantization.

## 2. Uniform valuations and normalization

Choose the 5-adic place with i≡2. Then v(-3−4i)=0 and v(-3+4i)=2. The latter also follows from -3+4i=(1+2i)^2. All odd-order roots of unity have 1+z a unit in residue characteristic five.

Put t=q^h and eta=Phi_7(t)^2. The element t has order N, so eta≠0 because N>7. Write N=5^e n with 5∤n. Its reduction has exact order n.

- If n>7, then tbar^7≠1 and eta is a unit, so c=v(eta)=0.
- If n=7, then e≥1, t−1 is a unit, and t^7 is primitive of order 5^e. Consequently c=2v(t^7−1)=1/(2·5^(e−1))≤1/2.

For a nontrivial root of unity θ, positive v(1−θ) is possible only when θ has 5-power order. If that order is 5^s, v(1−θ)=1/(4·5^(s−1))≤1/4. This elementary formula follows from Phi_(5^s)(1)=5 and the equality of valuations of the primitive conjugates; the exponents prime to five give a unit geometric quotient. Therefore each nonzero internal r_u has v(r_u)≤1/2. When n=7 its underlying 5-power order is at most 5^e, giving v(r_u)≥c. In all other cases the lower bound c=0 is automatic. The valuation is independent of chain j since z^7 is independent of j and the other Laurent factors are units.

Choose σ with v(σ)=−3/4 and D_(0,j)=1, D_(u,j)=D_(u−1,j)/(σb_u(j)). Then

v(D_(u,j))−v(D_(u−1,j))=3/4−v(r_u)∈[1/4,3/4].

The common depth valuation d_u strictly increases. B'=σD^{-1}BD has upper entries exactly 1. Its lower entry has valuation 2v(σ)+v(-3−4i)+v(-3+4i)+2v(r_u)=1/2+2v(r_u)>0. The original diagonal has valuation at least 1, so the gauged diagonal has valuation at least 1/4. Hence B' is integral and reduces to I_7⊗J_L in chain-major order.

Set α=5ση, so v(α)=1/4+c. The upper perturbation is zero. After division by α the lower-entry valuation is at least 1/4+2v(r_u)−c≥1/4+c>0. On the diagonal, division gives exactly B(x,x)/(5eta). The four raw terms have respective lower valuation bounds 2−c, 1+v(r(x))−c≥1, v(r(x))−c≥0, and 1−c. At any zero r(x), the terms containing r vanish and require no finite valuation bound. Thus R=(B'−J)/α is integral and its reduction is diagonal, with entry 2r(x/N)sin(2πx/N)/eta reduced after division.

## 3. Endpoint reduction does not require full Fourier rank

Take β=D_(L−1,0). The (row depth r, column depth s) entries of G'=βD^{-1}GD have valuation d_(L−1)−d_r+d_s, since every G entry is a root of unity. This is nonnegative and is zero exactly when r=L−1 and s=0. Therefore G' is integral and G'bar=E⊗e_(L−1)e_0^T.

Expanding the actual quadratic exponent at x=a+L−1+jL and y=a+kL, the mixed chain term is q^(4^{-1}L²jk)=w^(2Ljk), w=q^L. All remaining terms separate into row and column phases. The endpoint D-ratios have valuation zero. Thus E is diagonal-unit × seventh-root Fourier matrix with multiplier 2L mod 7 × diagonal-unit. The multiplier is nonzero because 7∤L, and w retains exact order seven since 5≠7. E is invertible even if the full N×N reduced G is singular.

A commuter of J has blocks polynomial in J_L, equivalently Sbar=Σ C_d⊗J_L^d. For d≥1, J_L^d(e_(L−1)e_0^T) is supported at (L−1−d,0), while (e_(L−1)e_0^T)J_L^d is supported at (L−1,d). These supports are disjoint. Commutation with G'bar gives C_dE=0 and therefore C_d=0. At d=0 it gives [C_0,E]=0. This argument is valid already at the smallest allowed L=3.

## 4. The augmented partial-trace constraint is legitimate

Let τ take the ordinary trace of each L×L block. For arbitrary S, not merely a commuter or a Toeplitz matrix,

τ([S,J])_(j,k)=tr(S_(j,k)J_L−J_LS_(j,k))=0.

Therefore [S,B']=0 implies ατ([S,R])=0 over the characteristic-zero field, and α≠0 implies τ([S,R])=0 exactly. The coefficients of this last linear equation are integral because R is integral. This is an integral equation retained before taking the residue, not an inference that arbitrary reduced commuters lift.

For Sbar=C_0⊗I_L, reducing this equation yields [C_0,T]=0, where T_j is the sum of the reduced diagonal R-entries along chain j. There is no division by L, so 5|L presents no problem.

For rank lifting one may define the full integral linear map explicitly as

S ↦ ([S,B'], [S,G'], τ([S,R])).

Over the characteristic-zero field its third component is redundant, and its kernel is exactly the original common commutant after gauge/scalar changes. Over the residue field it is allowed, and essential, to be stronger than the naive two-commutator reduction.

## 5. Independent normalized trace computation

The reduction of B(x,x)/5 is P(z)=2r(z)sin(z), which I reconstructed directly from the model rather than importing the coefficient generator:

P(z)=3(z^7−1)^2(z+1)^2(z−z^{-1})z^{-8} over F_5.

Its positive-label coefficients at 1,2,5,6,8,9 are 3,4,2,4,1,3, the negative coefficients are their negatives, and the label-seven coefficient vanishes. This matches the maintained 4000A coefficient dictionary and the candidate data.

For positive k the chain sum is t^k(1−w^k)/(1−t^(2k)) times w^(kj). Combining the negative-frequency partner gives the exact bracket w^(kj)−w^(−k(j+1)). Grouping k=1,6,8 and k=2,5,9 gives exactly the candidate a(t) and b(t), with no missing sign or extra w factor. Every denominator is a unit since the residue order is divisible by seven but no displayed 2k is divisible by seven.

Fresh F_5 polynomial arithmetic reproduces the cancellation of Phi_7(x)^2 and the following normalized numerators:

p_a=−2x^11−x^10+x^9−x^8−x^7+2x^6−x^5−x^4+x^3−x^2−2x,

p_b=−x^14+2x^13+2x^12+x^11+x^10+2x^9+2x^7+x^6+x^5+2x^4+2x^3−x^2.

The saved denominators divide the stated products of 1−x^(2k). The exact identity u p_a+v p_b=x was independently checked, where

u=x^12−2x^11−2x^9−2x^8+x^7−2x^6+x^4+2x^3+x+2,

v=−2x^9−x^8+2x^7+x^6+x^4+x^3−2x^2−2x+1.

In particular the normalized amplitudes cannot both vanish at a nonzero residue tbar of order divisible by seven.

The order-seven residue case is genuinely covered. Coefficient reductions at i≡2 have errors of valuation at least 1, not merely a positive unspecified valuation: i−2 has valuation 1 because (i−2)(i+2)=−5 and i+2 is a unit. A polynomial identity modulo five, after clearing the unit denominators, gives an identity of the form numerator=eta·Q+5H in the valuation ring. Division by eta leaves an error of valuation at least 1−c≥1/2>0. Thus the reduced quotient is the normalized rational function even when both the unnormalized numerator and eta reduce to zero. Substitution into the unnormalized zero trace is never used.

As a separate direct control, I expanded the raw diagonal at t=t_0(1+ε), with t_0 primitive of order seven, and divided its quadratic leading term by that of Phi_7(t)^2. Writing z=t_0^(2x), the quotient is

2x²(t_0−1)²(z+2+z^{-1})(z−z^{-1}).

Fresh code sums all L terms of each chain, without the candidate's period-35 shortcut, for e=1,…,6, N=7·5^e. All six agree with the rational formula and have seven distinct trace values. These are finite corroborating checks; the preceding valuation-and-polynomial argument is the uniform proof for all e.

## 6. All collision partitions and Fourier minors

The independent field implementation uses six-tuples in F_5[w]/(1+w+⋯+w^6), different from the candidate's degree-six factor of Phi_63 and log tables. Phi_7 is irreducible because ord_7(5)=6. Its primitive roots are the six Frobenius conjugates, so this exact computation covers every primitive w; a larger residue field introduces no additional pair-collision ratios.

The seven ξ_j=w^j−w^(−j−1) are distinct. Their difference factors into w^j−w^k and 1+w^(−j−k−1), both nonzero for j≠k. For B≠0, the 21 pair ratios give exactly nine values. The complete groups, omitting singleton braces in this list, are:

- triple {0,3,6};
- triple {1,3,5};
- triple {2,3,4};
- pairs {0,1}, {5,6};
- pairs {0,2}, {4,6};
- pairs {0,4}, {2,6};
- pairs {0,5}, {1,6};
- pairs {1,2}, {4,5};
- pairs {1,4}, {2,5}.

All other coordinates are singleton groups. Hence every nonsingleton group has size at most three and there are at least as many singletons as its size. B=0 gives all singletons. Every group partition agrees with the candidate; field-basis-independent ratio coefficients are saved in the independent output.

The elementary minor proof is valid. A 2×2 Fourier determinant is a nonzero phase times 1−w^m with m nonzero modulo seven. For a normalized 3×3 minor, vanishing would make its degree-at-most-six exponent polynomial a multiple of Phi_7. Its value at 1 is zero but Phi_7(1)=7≠0 mod 5, so the multiple must be zero. The integer coefficients have absolute value at most three, so zero modulo five means zero as integers. This forces equality of the two exponent multisets. Since ac+bd cannot equal ac or bd, it must equal ad+bc; either matching of the remaining two terms forces a=b or c=d, both excluded. Thus the proof has no characteristic-five cancellation loophole.

Independent exhaustive checks found all 49 one-by-one, 441 two-by-two, and 1,225 three-by-three minors nonzero for the chosen primitive root. Frobenius transfers the result to the other five roots. All 900 allowed normalized exponent quadruples also passed the integer-multiset check.

## 7. Final scalarity and lift

The equation [C_0,T]=0 makes C_0 block diagonal on the displayed partition. At singleton coordinates it has scalars λ_j. Because every E entry is nonzero, [C_0,E]=0 between singleton coordinates forces all λ_j to equal one λ. For a group I of size m≤3, choose m singleton coordinates J. The (I,J) block equation is

(C_(0,I,I)−λI_m)E_(I,J)=0.

The required E minor is invertible by the elementary Fourier-minor result and the diagonal-unit/permutation form of E. Therefore every partition block is scalar and C_0=λI. Consequently the reduced augmented kernel has dimension one.

The identity matrix is always in the kernel, so the augmented integral linear map has residue rank exactly N²−1. A nonzero minor of that size remains nonzero over the 5-adic field, and its characteristic-zero kernel agrees with the original common commutant. Ranks of a matrix over the defining number field are unchanged by extension to the 5-adic field or C. The conclusion therefore applies to arbitrary complex-entry commuters, not just algebraic-entry matrices. Diagonal conjugations and nonzero scalar multiples do not affect common commutants.

## 8. Exceptions, scope, and remaining gap

There is **no remaining proof gap for the stated first-seven theorem**.

- N=7 is correctly excluded: eta=0 and A_7=(9/10)I; its common commutant with M_7 is non-scalar.
- If 49|N, the mixed endpoint coefficient 2L vanishes modulo seven and the endpoint block has rank one. This proof does not extend to that case.
- The separately accepted 49|N, 5∤N theorem remains separate and unchanged.
- Combining this theorem with that separate result and the separately accepted 7∤N result leaves odd multiples of 245 as the unresolved common-commutant branch, besides the genuine N=7 exception.
- No seven-divisible spectral simplicity, quantitative gap, signed Heisenberg comparison, microscopic universality, or full complex single-U commutant assertion follows here.

The strongest safe new statement is exactly the claim at the top. No additional numerical range extension is needed to validate its universal scope. Canonical promotion, broader theorem consolidation, and any formalization are separate actions not performed in this audit.

## Reproduction and trust boundary

Run:

`PYTHONDONTWRITEBYTECODE=1 python3 record/history/2026/ramified_first_seven_20261006/independent_check_original.py`

Python 3.12.14, SymPy 1.14.0; exact polynomial and finite-field arithmetic; no floating point, randomized sampling, external calls, or finite-N extrapolation. Two executions completed, approximately 56.4 seconds and 55.0 seconds. The first execution's stdout is `independent_check.log`; the complete current JSON is from the second execution. Both passed all identical mathematical checks. Code does not import or execute candidate scripts, avoiding their hard-coded output writes into the candidate directory. All audit writes are confined to this review directory.

The analytic proof is independently reviewed mathematics, not formally machine-checked. The finite program verifies the explicit small algebraic certificate; it does not, by itself, prove the infinite theorem. The preceding uniform reduction is what connects the finite certificate to every allowed N.
