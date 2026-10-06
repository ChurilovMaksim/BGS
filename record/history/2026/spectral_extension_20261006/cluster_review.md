# Frozen audit: first ramified spectral cluster at N = 175

Date: 2026-10-06. Primary verdict: **proved as written**, for the normalized claim below, with an exact bounded computational input independently reconstructed here. This is an independent internal review of the submitted candidate, not an external referee report or a proof-assistant formalization.

## 1. Claim card and frozen source

**Normalized claim.** For the actual frozen generator A_175 defined by the raw modular Weyl quantization in `BGS/mathematics/fixed_map_resolvent_frontier.md`, all 175 complex eigenvalues are distinct. The proof uses one prime above 5 and the real-Jacobi algebraic similarity already established in `BGS/mathematics/frozen_kick_rank_boundary.md`.

Reviewed candidate: `first_ramified_cluster_split.md`, SHA-256 `811dd1b7ef91ecddf46d203e81860c813e4aca020a22697a337e5a96071b9fc7`. A byte-identical copy and the frozen supporting sources are under `source_snapshot/`. The submitted argument was explicitly a candidate pending audit; this report records the narrower audit outcome and does not modify or promote canonical repository status.

The claim is about A_175 alone. No conclusion about simplicity of U_175, uniformity in 5-adic depth, quantitative complex spectral gaps, the common commutant, or BGS is made. The general normalization discussion is used for e >= 1 only; the theorem audited here has e = 2.

## 2. Dependency graph

1. Actual raw Weyl symbol and midpoint convention -> algebraic similarity to the seven real Jacobi paths (internal exact calculation; inherited source checked).
2. Cyclotomic local field and exact cancellation -> integral normalized matrix T and its residue/jet dictionary (independently derived below).
3. Seven degree-five residue polynomials -> squarefreeness, pairwise coprimality, and nonzero offset derivatives (35 explicit finite-field Bezout certificates; reconstructed independently).
4. Actual pi^4 translation jet + simple-root lifting -> all 175 eigenvalues of the 35-block diagonal part distinct, maximum gap valuation 4 (internal local algebra).
5. Exact pi^8 interblock scale + integral eigenbasis -> 175 disjoint Schur fixed-point discs (internal contraction proof below).
6. Nonzero local discriminant -> nonzero algebraic discriminant -> complex simplicity of the actual A_175.

No load-bearing external source was imported for the new implication. The local lifting and perturbation steps are supplied explicitly below rather than inferred from a named theorem without its hypotheses.

## 3. Exact model, field, and normalization

Put q = exp(2 pi i/175), Q = q^7, h = 88. In the raw Weyl convention a Fourier mode r_k exp(2 pi i(kq+p)) contributes r_k q^{k(x+h)} in row x, column x+1. Thus the upper bond of A is exp(-i alpha_0) r(q^{x+h})/200; the lower bond is its conjugate. On each of the seven paths the diagonal change of basis with consecutive ratio exp(i alpha_0)=(-3+4i)/5 makes both bonds r(q^{x+h})/200. This is an algebraic similarity. It need not be integral at the chosen prime and the proof never assumes that it is.

Here, writing the trigonometric function as a Laurent polynomial,

r(q^x) = -(Q^x-1)^2 (q^x+1)^2 / (4 q^{8x}).

The actual diagonal of 200A_real is

200 cos(14 pi x/175) + 20 r(q^x) + 2 r(q^x) sin(2 pi x/175) - 20.

Consequently subtracting 180I removes exactly its constant part at Q=1. Set eta = Phi_7(q^h)^2 and T = (200A_real-180I)/eta. Since

eta = (Q^h-1)^2/(q^h-1)^2,

R_x := r(q^x)/eta = -([x]_Q/[h]_Q)^2 (q^h-1)^2 (q^x+1)^2/(4 q^{8x}),

where [x]_Q=(Q^x-1)/(Q-1). The exact normalized diagonal is

D_x = 100 ([x]_Q/[h]_Q)^2 (q^h-1)^2/Q^x + 20 R_x + R_x(q^x-q^{-x})/i.

This formula fixes both the centering and the odd-term sign independently of the candidate scripts.

Choose i congruent to 2 modulo 5. Put zeta=q^50, a primitive seventh root, so exactly q=zeta Q^18 (because 50+7*18=176 congruent to 1 modulo 175). The residue of zeta has minimal polynomial Phi_7: the powers of 5 modulo 7 are 5,4,6,2,3,1, so its residue degree is six. The polynomial Phi_25(1+pi) is Eisenstein over this unramified coefficient field: it has degree 20, reduction pi^20, and constant term 5. Thus pi=Q-1 is a uniformizer and v_pi(5)=20. Adjoining i at the root i=2 modulo 5 is unramified (indeed i is in Q_5), since the derivative of X^2+1 at 2 is a unit.

Both [h]_Q and q^h-1 are units: h=3 modulo 5 and h=4 modulo 7. Therefore T is integral; v_pi(eta)=2. The first two terms of D_x have valuation at least 40 and 20, respectively. Modulo pi^5 (and modulo pi^9) the remaining term is exactly 3 R_x(q^x-q^{-x}), since 1/i congruent to 3 modulo 5. These quotients have characteristic 5 because v_pi(5)=20.

## 4. Residue coefficients and both derivatives

Let z be the residue of q. Then

f_x = -3^(-2) (z^4-1)^2 (z^x+1)^2/(4 z^{8x}),

r_x = x^2 f_x,    d_x = 3 r_x(z^x-z^{-x}).

All integer coefficients here are in F_5. The residue is 35-periodic. A bond at left endpoint x has position u=x+h and vanishes precisely when 5 divides u, equivalently x=2 modulo 5. There are 35 length-five blocks with starts 3+5j modulo 175. Their seven residue types have starts 3,8,13,18,23,28,33, each occurring five times. The h=18 convention for N=35 gives the identical residue coefficients because 88-18=70 is divisible by 35.

For the auxiliary offset y, keep every z phase fixed and replace x^2 by (x+y)^2. Thus

partial_y r_x = 2x f_x,    partial_y d_x = 3 (2x f_x)(z^x-z^{-x}).

Internal bond positions use x+h in this same formula; they do not use the diagonal position x. Both derivatives of the determinant are needed: partial_X p_j ensures simple-root lifting, and partial_y p_j ensures a nonzero translation response. They were independently reconstructed using the full Leibniz determinant over dual polynomials in y, not the submitted differentiated continuant.

For each of seven types the exact certificates prove gcd(p_j,partial_X p_j)=1 and gcd(p_j,partial_y p_j)=1. All 21 gcd(p_j,p_k) are also 1. There are therefore exactly 35 distinct simple base eigenvalues, and every one has nonzero offset derivative.

The exact field used for the independent certificates is F_5[z]/(1+z+...+z^6), with low-to-high coefficients encoded in base 5. The submitted field uses t^6+t^4+3t^3+t^2+1 and qbar=t^9. The explicit map z -> t^9 was checked; all seven polynomials and offset derivatives match the submitted JSON under this map. No root convention was silently changed.

## 5. Actual next-jet identity

Modulo pi^5, use q=z(1+pi)^18 and

[x]_Q = sum_{a=0}^4 binom(x,a+1) pi^a.

For delta=35k with 0 <= k <= 4,

[delta]_Q = 2k pi^4 modulo pi^5,    q^delta=1 modulo pi^5.

The first identity follows either from binomial coefficients or from Q^{35k}=(Q^5)^{7k}; its leading coefficient is 7k=2k modulo 5. For the second, q^{35k}=Q^{5k} exactly. In particular this phase variation starts at order 5 and does not contaminate the order-4 offset.

The identity [x+delta]_Q=[x]_Q+Q^x[delta]_Q gives a change 2k pi^4 in [x]_Q modulo pi^5. The normalization [h]_Q and q^h are common to all blocks. Reducing the coefficient of this order-4 change gives precisely the auxiliary derivative above, at both diagonal and bond positions. No derivative of a q phase is missing at this order. The wraparound modulo 175 also causes no error: q^175=Q^175=1 exactly.

Writing P_{j,k}(X) for the actual normalized length-five block at start s_j+35k, the result is

P_{j,k}(X)-P_{j,0}(X) = 2k pi^4 partial_y p_j(X,0) modulo pi^5.

The independent script verifies this identity coefficient by coefficient for every one of the 35 actual block polynomials, using the cancelled exact actual coefficients, in addition to 665 individual residue/coefficient checks. This is an exact truncated jet calculation, not a floating fit or a replay of the proposed discriminator.

## 6. Lifted block eigenvalues and exact interblock scale

Pass to a finite unramified extension splitting the seven residue polynomials. For a simple residue root, coefficients of its lift are solved successively: at each step the next error is cancelled by dividing by the unit derivative. Completeness gives a unique integral root in that residue class. Each block has five roots this way and all internal eigenvalue differences are units.

The actual block eigenvalue lambda_{j,k} lifting a fixed residue root lambda obeys

lambda_{j,k}-lambda_{j,0} = -2k pi^4 (partial_y p_j(lambda)/partial_X p_j(lambda)) modulo pi^5.

Both derivatives are units at lambda. Hence differences between distinct copies k,l have valuation exactly 4, while different base eigenvalues have gap valuation 0. The block-diagonal matrix consequently has 175 distinct eigenvalues and every gap valuation is at most 4.

An integral diagonalizing matrix with integral inverse is available for every block. Indeed, its spectral projectors are products (B-lambda_l I)/(lambda_i-lambda_l), with all denominators units. They are integral and reduce to distinct rank-one eigenspace projectors. Choosing one vector in each projector image whose reduction is nonzero gives a matrix whose columns reduce to an eigenbasis, hence whose determinant is a unit. This establishes the needed GL_5(O) statement without assuming Euclidean orthogonality in the local field.

For an interblock bond u=5a, if 25 does not divide u then Q^u has order 5 and v_pi(Q^u-1)=5. All other factors in R_u are units, so v_pi(R_u)=2(5-1)=8. If 25 divides u then the bond is exactly zero. Thus there are 28 nonzero interblock bonds of exact valuation 8 and seven exact original-chain boundaries. A separate exact computation modulo pi^9 verifies those 35 valuations (the seven zeros follow exactly from Q^u=1). The integral block diagonalization preserves entrywise divisibility by pi^8.

## 7. Strict Schur-disc perturbation argument

After that change of basis, write T=D+E, D=diag(d_1,...,d_175), with v_pi(E_ab)>=8 and v_pi(d_a-d_b)<=4 for a!=b. Consider the closed disc B_j=d_j+pi^5 O; the 175 discs are pairwise disjoint.

For lambda in B_j, every diagonal difference lambda-d_l with l!=j has valuation at most 4. For the complementary matrix

R_j(lambda)=lambda I-D_rest-E_rest,

factor out lambda I-D_rest. Its inverse has entries of valuation at least -4, and the resulting Neumann-series perturbation has entries of valuation at least 8-4=4>0. Therefore R_j(lambda) is invertible throughout B_j and its inverse has entries of valuation at least -4.

The Schur equation is the fixed-point equation

lambda = d_j + E_jj + E_{j,rest} R_j(lambda)^(-1) E_{rest,j}.

Its displacement has valuation at least 8 (the off-diagonal product actually has valuation at least 8-4+8=12), so it maps B_j into itself. The resolvent identity shows that the difference of its values at lambda and mu has valuation at least

v_pi(lambda-mu) + 8-4-4+8 = v_pi(lambda-mu)+8.

This is a strict contraction in the complete disc. Successive substitution produces a unique solution in each B_j. Each solution is an eigenvalue by the Schur determinant identity; the complementary determinant is a nonzero unit times a power of pi throughout the disc. The 175 distinct solutions already exhaust a degree-175 characteristic polynomial, so every eigenvalue is simple.

Notice the strict inequalities actually used: the disc depth 5 exceeds the largest gap valuation 4, the perturbation depth 8 exceeds 5, and the inverse perturbation depth 8-4=4 is positive. Equality at one of these margins was not silently accepted.

Finally, q and i are algebraic and eta is nonzero. Local simplicity says that the characteristic discriminant, an algebraic number, is nonzero under one embedding. It is therefore nonzero in the original number field and under the complex embedding. Undoing the scalar normalization and algebraic similarity proves the stated complex simplicity of A_175.

## 8. Obligation matrix and evidence

- Actual raw-Weyl midpoint, phase and gauge: passed by direct reconstruction against the inherited exact model.
- Centering 180, eta and integrality: passed by exact Laurent identities.
- Gaussian prime i -> 2 and residue-root map: passed explicitly.
- All seven base blocks, both derivatives and every pair: passed; 35 exact Bezout identities saved.
- Actual pi^4 dictionary: passed for every coefficient of all 35 blocks.
- Interblock valuation: passed analytically and independently modulo pi^9.
- Unit eigenbasis and strict perturbation implication: passed with explicit arguments above.
- Uniform e>=3 continuation, U simplicity, BGS, commutant reproof: out of scope.
- Formal proof-assistant verification: not addressed or claimed.

Reproduction from this directory:

    python3 independent_cluster_certificate.py

The script imports no candidate implementation and uses only the Python standard library. Its actual bounded result is in `independent_cluster_certificate.json`: seven 120-permutation determinant checks; 7+7+21 gcd/Bezout checks; 35 actual block-polynomial pi^5 identities; 665 coefficient identities; seven reconstructed degree-25 residue chain polynomials; and 35 interblock pi^9 checks.

The submitted scripts were also replayed in `replay/`, with only the absolute dependency lookup redirected into that isolated directory. Both regenerated JSON files are byte-identical to the frozen source outputs. Replay is supplementary; the independent reconstruction is the substantive audit evidence.

## 9. Remaining gap and strongest safe statement

There is no remaining implication gap for this frozen N=175 claim. The strongest audited conclusion is **simple spectrum of the actual A_175**. The existing residue calculation also suffices separately for A_35, but that is not a new inference about arbitrary e. Repeated deeper clusters for e>=3 require a separate controlled analysis; this report supplies neither a uniform continuation nor a result for the propagator.

Canonical BGS files were not changed. No repository integration, commit, push, or full-project build was performed by this audit.
