# Independent audit of the stationary-label cyclic residual

6 October 2026. Separate supporting-note review, after the frozen combined S1–S9 interface verdict. No candidate or canonical edits.

## Claim and verdict

**Primary verdict: correct only after a stated restriction.** Formulas R1–R6 and the plateau boundary reconstruct correctly. The sentence asserting that “The N-torsion sectors ... remain inside this signed residual” must be restricted to the **unremoved portions** of those sectors. Removing the cyclic pair family removes both diagonal torsion and some nonzero-torsion pairs. This correction does not change any displayed formula, estimate, normalization or residual definition.

Frozen candidate `/workspace/shared/bgs_paired_box_cancellation/stationary_cyclic_remainder.md`, SHA-256:
`7c54200d10568200c3f77e42f796c099c7f939c1f6421137aec7c985cf24047e`.

The statement is a stationary-label ramp and once-counted residual for fixed-J V_(N,J). It correctly credits the prior FM-021 position-path ramp, without claiming an identification of the two pair families. The combined selected-family theorem was positively interface-reviewed before this supporting note; the opening “awaits interface review” describes an earlier checkpoint and may be updated editorially with the exact review provenance.

## 1. Positive cyclic family and short periods

Put beta(z)=e(NQ_m(z))alpha(z). Then T(z,z')=D_m^(-1)beta(z')conjugate(beta(z)). Exact cyclic invariance gives beta(Sz)=beta(z). For each fixed z, precisely p_m(z) distinct points z' occur in its orbit, regardless of the number of j in 0,...,m-1 that realize them. Therefore the once-counted sum is

sum_(C_m)T=D_m^(-1)sum_z p_m(z)|alpha(z)|^2.

The integer p_m(z) divides m. This retains short orbits correctly and yields a nonnegative real cyclic sum even for global complex Fresnel coefficients.

For exact boxes, w_0^2=D_m rho_m and P_z^2|Z_z|^2=1+O_J(N^(-1/2)). The latter follows from imaginary ell_1 and the accepted relative first-loop error; it does not assume Z itself tends to one. Multiplying by p_m<=m gives R2 with error at most C_J m N^(-1/2) Z_m^cl.

For a proper-period point, p_m(z)<=m/2. Taking a union over proper divisors bounds its total count by

sum_(ell|m,ell<m)#Fix S^ell <= C m lambda^(m/2).

The actual entrywise derivative lower bound is enough for the individual weight estimate, and can be checked directly without importing unrelated claims from its source. The fixed tiny perturbation gives DF(x)>=B entrywise, where

B=[[5/2,7/2],[3/2,5/2]], det B=1,
lambda_-=(5+sqrt(21))/2.

All entries are positive, so products preserve this order and tr DF^m>=tr B^m=lambda_-^m+lambda_-^(-m). Area preservation gives

|det(I-DF^m)|=tr DF^m-2
 >=lambda_-^m(1-lambda_-^(-m))^2
 >=(1-lambda_-^(-1))^2 lambda_-^m.

Thus rho_m<=C lambda_-^(-m), uniformly including small m. Since lambda_->sqrt(lambda), the short-period defect is bounded by

m times [C m lambda^(m/2)] times [C lambda_-^(-m)],

which is R3. EQ gives m Z_m^cl=m+O(m e^(-c m)); this is absorbed into the displayed m^2 exponential error.

For global coefficients the previously proved normalized l2 bound compares |alpha_global|^2 and |alpha_box|^2 with multiplier p_m. Its operator norm is at most m. Cauchy–Schwarz therefore costs C_J m sqrt(N)e^(-4N/5), exactly as in R4. The band m<=2N and fixed J remain essential. No new contour extension is inferred.

## 2. Exact disjointness

k0=(1/2,0) satisfies Sk0=k0 modulo Z^2, hence belongs to every G_m. The perfect pairing b_m is S-invariant. For every cyclic displacement d=(S^j-I)z,

b_m(k0,d)=b_m((S^(-j)-I)k0,z)=0 modulo one.

For every selected homoclinic displacement d=+/-S^j d_m,

b_m(k0,d)=+/-b_m(k0,d_m)=+/-1/2=1/2 modulo one.

Thus no ordered pair can be simultaneously cyclic and selected homoclinic. This is an exact character obstruction at every m; it does not require full least period, generic nonintersection, or an asymptotic estimate. Because O_m is a set and the initial point is retained, the pairs in H_m are also counted exactly once.

## 3. Residual normalization and U transfer

The total ordered-pair sum splits exactly into C_m, H_m and their complement. R4 gives a cyclic contribution m plus its stated errors; S9 bounds the selected H_m sum at the original time normalization.

For a smooth weight supported in a fixed positive subinterval of (0,1/2),

N^(-2)sum_m |w(m/N)| m N^(-1/2)=O_w(N^(-1/2)).

The exponentially small m^2 and m sqrt(N) terms remain exponentially small after the O(N) time sum and its polynomial factors. The separate fixed-J>=2 aggregate U/V estimate also costs O(N^(-1/2)). These statements prove R6. There is no additional division by m, by D_m or by |O_m|.

R is exactly the complement of two explicitly disjoint ordered-pair sets for V. It is not an intrinsic decomposition of U. Above m/N=1, the CUE benchmark is min(m,N)=N while the cyclic family still contributes m, so the signed complement must supply N-m. The note preserves this negative plateau correction and makes no claim to bound the residual or higher factorial hierarchy.

## 4. Decisive counterexample to the overly broad torsion sentence

At m=3,

S^3-I=[[98,140],[70,98]].

Take N=7 and z=(1/7,0), so (S^3-I)z=(14,10) is integral and z belongs to G_3. Its cyclic successor is

z'=Sz=(3/7,2/7),
d=z'-z=(2/7,2/7).

The displacement is nonzero and 7d is integral. Hence d belongs to the nonzero N-torsion sector ker 7, but (z,z') belongs to C_3 and is removed before R is defined. Also every diagonal pair belongs to C_m, removing the d=0 sector entirely.

Required boundary edit in Section 3:

“The unremoved portions of the N-torsion sectors and nearly all noncyclic stationary pairs remain inside this signed residual.”

One may instead state simply that no estimate of the remaining torsion contribution is supplied. The exact complement definition and R6 already use the correct once-counting. No displayed equation needs to change.

## Obligation matrix and source controls

| Obligation | Status |
|---|---|
| R1 once-counted positive cyclic sum | Passed |
| Box norm from imaginary first loop | Passed |
| Proper-period count and weighted suppression | Passed, explicit derivative lower bound reconstructed |
| Global norm comparison with multiplier p_m | Passed for m<=2N |
| C_m disjoint H_m | Passed by exact order-two character |
| R6 original normalization and J>=2 aggregate transfer | Passed |
| Prior FM-021 ownership and coordinate distinction | Passed |
| Entire torsion sectors remaining after removal | Failed literally; explicit nonzero-torsion counterexample above |
| Plateau and full signed residual estimate | Explicitly open |

The entrywise lower bound was read at `BGS/mathematics/frozen_seven_cut_reduction.md`, lines 220–229, SHA-256 `af615f74c88d475267207b2404d6b0674e6aa7f5b9cc32346bf412d2de3feb39`. Only the stated local derivative inequality and its elementary matrix consequence are used. FM-021's maintained source `position_chain_mixing.md`, especially Section 4, was read to verify prior ownership and the differing families.

New exact checker:

`python3 /workspace/shared/bgs_physical_quantum_homoclinic_review/check_stationary_residual.py`

It exhaustively checked 273,280 distinct cyclic ordered pairs for m=1,...,6, every label and all selected homoclinic directions in those dimensions, including short periods and overlaps within each family. Every C/H intersection was empty. It also verified the stated nonzero 7-torsion counterexample exactly. This is finite algebraic evidence only; it does not establish the analytic ramp or asymptotic residual estimate.

The strongest safe result is R1–R6 with the torsion sentence narrowed as above. No new mathematical gap was found in those formulas or their dependency interfaces.
