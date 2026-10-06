# Independent review of BGS-FM-008

Date: 2026-10-06 UTC. Scope: an independent internal mathematical audit, not an external referee report, a formal proof, or a status promotion. All artifacts were written outside the canonical repository.

## Claim card and verdict

**Primary verdict: proved as written.** This verdict applies to the theorem statement, with the two local exposition corrections identified below. No new restriction is required.

Let N>=3 be odd, 7 not divide N, and let A_N and M_N be the unchanged raw modular Weyl matrices specified by FM-001. Then A_N has simple spectrum, and every square minor of M_N represented in any A_N eigenbasis is nonzero. At every nonzero real algebraic t, U_N(t)=exp(it A_N)M_N and all its nonzero integer powers have simple spectra; ratios between different eigenvalues of U_N(t) are transcendental; every coefficient of det(I-zU_N(t)) is nonzero; and |Tr U_N(t)^m|^2 is transcendental for every nonzero integer m. The literal t=10^(-80)N is included.

The authoritative target reviewed was frozen at SHA-256:

- mathematics/frozen_algebraic_spectral_simplicity.md: d003b2abcb72d8f4922105a25892c43c8fdcd12f19a6d67ba8b51b2a3a9e2af2
- mathematics/fixed_model_symmetry_theorem.md: 32b2302c2567eebb75ff2231345e3336495ba8719517be6b5ce8734b416920c2
- mathematics/frozen_kick_rank_boundary.md: fcbc96473a964bd5272dab7676a2da5dcffd4f3afe1e8df5768b8e2356770e17

Observed repository HEAD at acquisition was 801de3ab760cab4349e68b9843dcd67955314e62. The verdict is bound to the file hashes, not to all material at that commit. The working tree had an unrelated modification to .github/workflows/ci.yml; this audit did not create or modify it. Copies and the final manifest are supplied with this report.

No assertion extends to 7-divisible N. No uniform minor lower bound, microscopic phase gap, Heisenberg trace estimate, CUE/BGS conclusion, or full complex scalar commutant of the single propagator is established.

## Dependency graph and obligation matrix

The mathematical chain is:

raw Weyl formula -> one nonzero-bond Jacobi path -> simple A

raw coefficients + local 5-adic root valuations -> integral Jordan degeneration

root-order valuations + convex balanced-residue counting -> Fourier minor lower bound

strict diagonal weights + sharp consecutive Fourier minor -> unique exterior corner

right and left recurrence alternants + that corner -> all A-eigenbasis minors

leading principal minors -> separated imaginary-time eigenvalue scales

algebraic exponential-polynomial algebra + registered Lindemann-Weierstrass -> all fixed-algebraic-time spectral consequences.

Obligations independently checked:

| Obligation | Result | Evidence class |
|---|---|---|
| Actual raw quantization, centering and path cut | Passed | Direct derivation; exact finite reconstruction |
| Simple generator for every admitted N | Passed | Hermitian eigenvector recurrence |
| Valuations, including 5-divisible N | Passed | Root-order argument and exact rational controls |
| Balanced-residue Fourier bound for all ranks | Passed | Convex counting proof, no finite extrapolation |
| Sharp, unique extremal exterior entry | Passed | Strict subset-weight inequalities |
| Integral normalized right alternants | Passed | Polynomial divisibility and reduction |
| Integral normalized left alternants and orientation | Passed | Reversed recurrence; explicit sign |
| Contraction is an arbitrary eigenbasis minor | Passed | Dual-basis normalization and Cauchy-Binet |
| Leading-minor eigenvalue asymptotics | Passed | Explicit rescaled polynomial; root count |
| Discriminants, resultants and negative powers | Passed | Collected algebraic exponential polynomials |
| Squared-trace analytic witness | Passed | Trace/inverse-trace product and unique extreme scales |
| Popescu exact version/theorem/application | Passed | Fresh primary PDF, exact hypothesis and page check |
| Quantitative spectral statistics or 7-divisible extension | Out of scope | Not inferred |

No circular dependency was found. In particular, total eigenbasis nonvanishing is not assumed from the position-basis Fourier matrix, whose minors can vanish at composite N.

## 1. Reconstruction of the actual model and simple path

Write h=2^(-1) modulo N and e_N(x)=exp(2 pi i x/N). Applying the raw quantization rule to the p-modes of the symbol gives

A(x,x+1)=(-3-4i) r((x+h)/N)/1000,

A(x+1,x)=(-3+4i) r((x+h)/N)/1000,

A(x,x)=cos(14 pi x/N)+r(x/N)/10+r(x/N)sin(2 pi x/N)/100-1/10.

This uses the raw Weyl midpoint modulo N; no ordinary-midpoint substitution is made. There are no other off-diagonal entries for N>=3. With z=e_N(y), direct Laurent expansion gives

r(y/N)=-(z^7-1)^2(z+1)^2/(4z^8).

For odd N, z cannot be -1, so a bond vanishes precisely when 7(x+h)=0 modulo N. If 7 does not divide N there is exactly one such bond, at x=-h. Ordering x_j=1-h+j modulo N, 0<=j<N, opens the cycle into a single tridiagonal path. Its internal bonds correspond to y=j+1 and are nonzero.

The matrix is Hermitian. For any eigenvector, the first component determines each successive component through the upper-bond recurrence. If the first component were zero, every component would be zero. Every eigenspace therefore has dimension at most one; Hermitian diagonalizability turns this into algebraic simplicity. This proves the only FM-005 assertion used here without importing its unrelated rank or variance arguments.

All entries and eigenvalues are algebraic. An eigenbasis with algebraic entries exists by Gaussian elimination over a finite splitting field. Since the eigenvalues are simple, every other complex eigenbasis differs by permutation and nonzero column scalings. Those transformations preserve nonvanishing of every minor.

## 2. The local valuation calculation, with ramification retained

Choose a valuation at the Gaussian prime pi=1+2i, normalized by v(5)=1, and extend it to a finite number field containing all entries, eigenvalues, and auxiliary scalings below. Since 5=(1+2i)(1-2i), the conjugate prime factor is a unit. Thus

v(-3+4i)=v(pi^2)=2,

v(-3-4i)=0.

For an odd-order root z, z+1 is a unit. One elementary reason: if z reduced to -1, its odd order would force -1 to have odd order in the residue field of characteristic 5, a contradiction. The root z and the rational factor 4 are units as well.

If a root of unity u has order with a nontrivial prime-to-5 factor, then 1-u is a unit. Indeed the prime-to-5 component reduces to a root of the same order: if a prime-to-5 root reduced to 1, the quotient (u^m-1)/(u-1) would reduce to the nonzero integer m and could not vanish. If u has exact order 5^b, b>=1, then

v(1-u)=1/phi(5^b)=1/(4*5^(b-1)).

To see the normalization directly, primitive conjugates 1-u^k have the same valuation for 5 not divide k, because their quotient by 1-u is a sum reducing to k; their product is Phi_(5^b)(1)=5.

On the present nonzero bonds, z^7 is not 1 and has the same order as z because gcd(N,7)=1. It follows that rho_j=v(r_j) satisfies 0<=rho_j<=1/2, including at 5|N. The upper endpoint occurs for order-5 roots; it is not an unramified-only argument.

Put B=1000A. The diagonal is

1000 cos(14 pi x/N)+100 r(x/N)+10 r(x/N)sin(2 pi x/N)-100.

The trigonometric root expressions have denominators that are 5-adic units. Every displayed coefficient is divisible by 5, so v(B_jj)>=1. This explicitly supplies the diagonal assertion compressed in the target.

Choose sigma algebraic with v(sigma)=-3/4. Define D_0=1 and D_(j+1)=D_j/(sigma b_j), where b_j=(-3-4i)r_j. Then

d_(j+1)-d_j=3/4-rho_j belongs to [1/4,3/4].

In B'=sigma D^(-1)BD, the upper entries are exactly 1, the diagonal entries have valuation at least 1/4, and the lower entries are sigma^2 b_j c_j, of valuation

-3/2+(rho_j)+(2+rho_j)=1/2+2rho_j>0.

Thus B' is integral and reduces to the single upper Jordan block J. Its characteristic polynomial reduces to X^N. Every root beta_i is integral (a negative-valuation root would make the monic highest term uniquely lowest), and then beta_i reduces to 0. This establishes the eigenvalue reduction without presuming an integral eigenbasis.

## 3. Fourier minor bound from residue occupancy

For N=5^a M with gcd(M,5)=1 and d not zero modulo N, the order computation just made gives zero valuation unless M divides d. In the latter case, put h=v_5(d)<a. The valuation is 1/(4*5^(a-h-1)). The target's positive indicator expansion is exactly this value, because

1/(4*5^(a-1)) + sum_(k=1)^h 5^(k-a) = 1/(4*5^(a-h-1)).

For a=0, every nonzero root difference is a unit.

Fix a rank r and distinct columns j_1,...,j_r represented in {0,...,N-1}. The alternating polynomial det(X_alpha^(j_beta)) is divisible by the Vandermonde product in Z[X_1,...,X_r]. Divisibility may be obtained by successive monic division by variable differences; no nonunit denominator enters. Evaluating at X_alpha=zeta^(i_alpha) leaves an integral quotient. Consequently a Fourier minor has valuation at least the sum of pairwise row-root valuations, with the convention v(0)=infinity.

For any modulus q dividing N and a chosen row set of size r, let n_0,...,n_(q-1) be its residue counts. The number of pairs congruent modulo q is sum binom(n_b,2). If n_b>=n_c+2, moving one count from b to c lowers the sum by n_b-n_c-1>0. Its minimum is therefore attained exactly by balanced counts, differing by at most one. If r=uq+v, 0<=v<q, the minimum is

(q-v)u(u-1)/2 + v(u+1)u/2.

A consecutive interval of r integer positions has balanced counts for every q simultaneously. Since the root-difference valuation is a positive linear combination of pair-coincidence counts for q=M5^h, consecutive rows minimize the valuation sum simultaneously at every level. Their value is

c_(N,r)=sum_(d=1)^(r-1) (r-d)v(1-zeta^d).

For consecutive columns 0,...,r-1, the determinant is exactly the Vandermonde; shifting that consecutive block contributes a unit monomial. Consecutive rows and columns therefore attain c_(N,r). This is valid for a>0 with arbitrarily high 5-adic ramification. Rank r=N and the empty minor r=0 cause no exception.

Crucial distinction: the claim is a lower bound for arbitrary Fourier position minors, not their universal nonvanishing. For example F_9 with rows (0,3) and columns (0,3) has an exactly zero determinant. The independent controls include this negative test.

## 4. Exact unique exterior corner

The physical metaplectic kernel is

M(x,y)=N^(-1/2)e_N(-8^(-1)(3x^2-2xy+3y^2)).

Substitute x=x_0+j and y=x_0+k with x_0=1-h. The constant, row-only and column-only terms can be absorbed in roots u_j and w_k. The bilinear coefficient is 2*8^(-1)=4^(-1) modulo N, a unit. Thus the Fourier factorization in path order is exact with primitive zeta=e_N(4^(-1)). No arbitrary path permutation has been substituted for this cyclic shift.

Let H=D^(-1)MD, and let H^(r)=wedge^r H. For row set I and column set K,

v(H^(r)_(I,K)) >= -r v(N)/2 + c_(N,r) - sum_(i in I)d_i + sum_(k in K)d_k.

At I_+={N-r,...,N-1}, I_-={0,...,r-1}, equality holds because the Fourier minor is consecutive/consecutive. Since d_0<...<d_(N-1), the top r indices uniquely maximize the row-weight sum, and the bottom r uniquely minimize the column-weight sum. Hence every other entry has strictly larger valuation than the nonzero corner alpha_r=H^(r)_(I_+,I_-).

Consequently alpha_r^(-1)H^(r) is integral and has reduction E_(I_+,I_-). The common factor N^(-r/2), which is not a unit when 5|N, is retained in the displayed bound and cancels in the comparison. Omitting it from a comparison is harmless, but assuming it is a unit would be wrong.

## 5. Both eigenvector alternants and the actual minor contraction

Write the diagonal and lower entries of B' as q_j and ell_j, all in the maximal ideal. A right eigenvector of eigenvalue beta can be normalized by its first component 1 and has entries phi_j(beta), where

phi_0=1,
phi_1=X-q_0,
phi_(j+1)=(X-q_j)phi_j-ell_(j-1)phi_(j-1).

Thus phi_j is monic of degree j over the valuation ring and reduces to X^j. The last row is satisfied when beta is an eigenvalue.

For a left row eigenvector, normalize the last component to 1 and recurse backward:

psi_(N-1)=1,
psi_(j-1)=(X-q_j)psi_j-ell_j psi_(j+1).

Here psi_j is monic of degree N-1-j and reduces to X^(N-1-j). The left recurrence uses the upper entries equal to 1; it does not incorrectly assume the lower entries are units. This distinction is essential.

For r distinct eigenvalues beta_(i_1),...,beta_(i_r), divide the exterior product of right eigenvectors by Delta=product_(a<b)(beta_(i_b)-beta_(i_a)). Each coordinate is an alternating polynomial divided by its Vandermonde and is integral before specialization. Reduction modulo the maximal ideal commutes with this polynomial identity; it is not division by a unit after specialization.

For increasing coordinate set J=(j_1,...,j_r), the reduced quotient is the ordinary monomial alternant quotient. It is homogeneous of degree sum j_a-r(r-1)/2. Since j_a>=a-1, this degree is zero only for J=I_-. For J=I_- the quotient is 1; for all other J it vanishes at the reduced tuple beta=0. Therefore the normalized right exterior vector reduces to e_(I_-).

Apply the same argument to the left recurrence with reversed coordinate order. Its normalized exterior covector reduces to (-1)^(r(r-1)/2)e_(I_+)^T. There is no assumption that the right and left vectors coincide.

Let R be the matrix of these right eigenvectors and L the matrix of the corresponding left rows. Distinct eigenvalues give L_i R_j=0 for i!=j. Each kappa_i=L_i R_i is nonzero: otherwise the nonzero row L_i would vanish on every column of the invertible R. Hence LR=diag(kappa_i), and the representation of M in this eigenbasis is

R^(-1) H R = diag(kappa_i^(-1)) L H R.

For arbitrary eigenvalue row set S and column set T of size r, Cauchy-Binet/exterior multiplication expresses its minor as

(product_(i in S) kappa_i^(-1)) Delta_S Delta_T alpha_r
  times [normalized left wedge for S] [alpha_r^(-1)H^(r)] [normalized right wedge for T].

The last contraction reduces to (-1)^(r(r-1)/2), a unit. All prefactors are nonzero, so the chosen minor is nonzero. This closes the passage from position Fourier valuations to arbitrary A-eigenbasis minors. Since S and T were arbitrary, every order and every row/column selection are covered.

## 6. Leading minors and imaginary-time eigenvalue scales

Take an algebraic A-eigenbasis with real eigenvalues a_1>...>a_N. Define S_r=sum_(j=1)^r a_j and b_r as the leading principal minor of M, with S_0=0 and b_0=1. Every b_r is nonzero by Section 5.

For W_s=exp(sA)M, its r-th characteristic coefficient is the sum over size-r principal subsets I of det(M_(I,I)) exp(s sum_(i in I)a_i). The top subset {1,...,r} uniquely maximizes that sum. Thus e_r(s)=b_r exp(s S_r)(1+o(1)). Other subset sums can coincide; that does not affect the unique maximum.

Write Q_s(z)=sum_(r=0)^N (-1)^r e_r(s)z^(N-r). Substitute z=exp(s a_j)w and divide by exp(s[S_(j-1)+(N-j+1)a_j]). The coefficient exponent for r differs from the normalizing exponent by

- sum_(k=r+1)^(j-1)(a_k-a_j) < 0, if r<j-1,

0, if r=j-1 or r=j,

sum_(k=j+1)^r(a_k-a_j) < 0, if r>j.

The normalized polynomial therefore converges uniformly on compact w-sets to

(-1)^(j-1)b_(j-1) w^(N-j)(w-b_j/b_(j-1)).

The nonzero root c_j=b_j/b_(j-1) is simple. A small circle around it excluding zero, followed by the elementary Rouché root count, supplies precisely one root counted with multiplicity there for sufficiently large s. It is therefore simple, and shrinking the circle gives

Lambda_j(s)=c_j exp(s a_j)(1+o(1)).

These N root regions are pairwise disjoint for large s because their modulus scales are distinct. This proves the required witness, including j=1 and j=N, without a claim about the physical small t.

## 7. Algebraic exponential polynomials and every spectral conclusion

The spectral projectors are algebraic; for example P_j=product_(k!=j)(A-a_k I)/(a_j-a_k). Thus exp(itA)M is a finite sum of algebraic matrices times exp(it a_j). Finite polynomial expressions in its entries and characteristic coefficients are finite exponential polynomials with algebraic coefficients and real algebraic frequencies. Equal frequencies must be collected before invoking transcendence.

For distinct frequencies omega_j and nonzero algebraic t_0, the exponents it_0 omega_j are distinct algebraic complex numbers. The checked Lindemann-Weierstrass input implies that a collected finite exponential polynomial vanishes at t_0 if and only if all its coefficients vanish, equivalently if and only if it is identically zero.

- **Simple U:** The discriminant is such a polynomial and is nonzero at sufficiently large imaginary time t=-is by Section 6. It cannot vanish at t_0.
- **Nonzero characteristic coefficients:** Each coefficient has the nonzero leading imaginary-time term b_r exp(sS_r). The same transfer applies. The constant coefficient in det(I-zU) is 1; its top coefficient is also covered.
- **Transcendental ratios:** For every fixed algebraic eta!=0,1, form Res_z(chi_t(z),eta^N chi_t(z/eta)). If j!=k, Lambda_j(s)/Lambda_k(s) tends to 0 or infinity in modulus, so it eventually differs from eta. The ratio of an eigenvalue to itself is 1, also excluded. Hence the resultant is not identically zero, and is nonzero at t_0. Ratios 0 are impossible because U is invertible; ratio 1 between distinct eigenvalues is already excluded by simplicity. Every possible algebraic ratio is ruled out.
- **All positive and negative powers:** A collision in U^m, m!=0, would give an eigenvalue ratio that is a root of unity. That contradicts the preceding conclusion. Invertibility permits negative powers.
- **Squared traces:** For k>0 define the entire function P_k(t)=Tr(U(t)^k) Tr(U(t)^(-k)). The inverse identity is U(t)^(-k)=(M^(-1)exp(-itA))^k. Therefore P_k is a finite exponential polynomial of the required kind. For real t, U(t) is unitary and P_k(t)=|Tr U(t)^k|^2. Unitarity follows directly from A Hermitian and the normalized Fourier factorization of M. For complex t, P_k is the analytic continuation of the real-axis squared trace; it is not a literal absolute square there.

The witness from Section 6 gives

P_k(-is)=(c_1/c_N)^k exp(k s(a_1-a_N))(1+o(1)).

Its coefficient is nonzero and its growth exponent is positive. Thus P_k is nonconstant. For each algebraic number c, P_k-c is a nonzero exponential polynomial; the source theorem gives P_k(t_0)!=c. Hence the squared trace is transcendental. Replacing k by -k leaves the product unchanged, covering every nonzero integer m.

## 8. Exact primary-source verification and inherited leaves

External source: Sever Angel Popescu, *A simple and self-contained proof for the Lindemann-Weierstrass theorem*, arXiv:2306.14352v2, 17 September 2023.

Stable primary PDF: https://arxiv.org/pdf/2306.14352v2

Freshly acquired PDF SHA-256: 0c158636ef68a2ac4586f0fff09b7429780f815d513799f1e794e9c554bae0f1.

This matches the earlier source-bound metadata check in /workspace/shared/bgs_bibliography_audit/EXT-POPESCU-2023.json. Its old text excerpt did not actually include the target theorem statement; this audit therefore did not accept that excerpt alone. It fetched the pinned primary PDF, extracted its text with pdftotext -layout, and visually inspected printed page 14 to verify the overline on Q, which extraction can lose.

Theorem 3.2 is on printed page 14, with its proof on pages 15–16. Its content is precisely independence over algebraic coefficients for exponentials with distinct complex algebraic exponents. No real-exponent restriction applies. The mapping in Section 7 satisfies every required hypothesis after collecting equal frequencies. Corollary 3.1's weaker real-exponent irrationality is not used. This audit verifies source identity, exact theorem contract, presence of its proof, and the project's application; it does not independently reprove the full classical Lindemann-Weierstrass theorem or claim a new result.

Inherited leaves after this review:

1. The raw FM-001 matrix definition is the model input, rederived at the needed coefficient level here. No FM-001 classical centralizer theorem is imported.
2. The needed FM-005 one-path simplicity is rederived here. Its rank/variance statements are not dependencies.
3. The only specialized external theorem for the spectral-time conclusions is the checked EXT-POPESCU-2023 Theorem 3.2 above.
4. Basic finite-dimensional Hermitian spectral theory, determinant/exterior algebra, finite-extension valuations, and elementary complex polynomial root counting are used as standard mathematical tools, explicitly enough to locate their use.
5. No author's computation is a proof leaf. The new finite program is independent support for the written universal derivation.

For the later all-odd pair-common-commutant theorem, the inherited 7-not-dividing-N leaf is strictly smaller: simple A plus the rank-one case of eigenbasis nonvanishing. A complex joint commuter is diagonal in the A-eigenbasis; writing its diagonal entries x_i, commutation with M says (x_i-x_j)M_ij=0. Since every M_ij is nonzero, all x_i agree. This implication is now independently checked for every N in this family and uses no Lindemann-Weierstrass input. The seven-divisible families and N=7 exception were not re-audited here.

## 9. Independent finite controls and exact scope

Fresh program: check_independent.py. It imports no project verifier or author's implementation. Arithmetic is Python Fraction plus exact SymPy QQ(i) polynomial arithmetic, with explicit finite limits. Environment: Python 3.12.14, SymPy 1.14.0, Linux x86_64. Command:

python3 /workspace/shared/bgs_fm008_independent_review/check_independent.py

The result in independent_results.json and its execution log is PASS:

- 250 odd dimensions 3<=N<=501: 62,750 root-difference indicator-formula cases; all exact zero-bond counts; 53,714 admitted single-path internal bonds and their valuation bounds. The attained extremes were rho=1/2 and D-increment=1/4.
- 497,728 row-subset balance checks: all ranks at N=3,5,9,15; ranks 0..5 at N=25; ranks 0..3 at N=75,125. Convex occupancy minima and consecutive-row equality were separately checked.
- Exact raw Fourier/Jacobi matrix equality in Q(i)[z]/Phi_N(z) at N=3,5,9,15,25,35,49, including low-N aliases and seven-cut negative-scope dimensions. All 4,591 matrix-entry identities passed. The Laurent r factorization and shifted-path metaplectic phase factorization were checked separately.
- 180 divided-alternant identities for both left and right recurrences, N=2..6, ranks 1..min(N,3), with a synthetic integral Jordan degeneration. This finite test checks polynomial reduction and orientation, not actual-model eigenvalue nonvanishing.
- 416,774 exact actual-path subset-weight tests certify the predicted unique bottom/top sets within the declared finite ranks. No pair enumeration is disguised as all-rank coverage.
- The Fourier F_9 position-minor negative control is exactly zero, confirming that the test infrastructure does not equate position-basis total nonvanishing with the proved eigenbasis statement.

These checks are regression evidence only. Universal quantifiers are justified by Sections 1–7, not by the enumeration counts. The author's checker was read to understand its advertised scope but was neither imported nor used to establish the verdict.

## 10. Local corrections, remaining gap, and next action

There is no remaining mathematical gap in the stated FM-008 theorem under its existing hypotheses.

Two local corrections are recommended for future integration:

1. Target line 186 currently displays U_N(t)^(-m)=M_N^(-1)exp(-itA_N). For general positive m it should display U_N(t)^(-m)=(M_N^(-1)exp(-itA_N))^m, or state the m=1 identity and then take powers. This is a false literal display for m!=1, but the intended finite-product argument is valid and fully supplied above. It does not require restricting the theorem.
2. Target line 155 says “the finitely many distinct exponent sums.” General subset sums need not be distinct. The correct sufficient assertion is that the leading r-subset sum is uniquely maximal; equal lower frequencies are collected. The later source paragraph already calls for collected frequencies. This is an exposition precision issue, not a missing nonresonance hypothesis.

The strongest safe statement is the full theorem card at the start, together with its complex scalar pair-commutant corollary for 7 not dividing N. The cheapest next action is a separately authorized editorial integration of these two corrections and a scoped review citation. This review itself does not change canonical text, claim state, or any downstream ledger status.
