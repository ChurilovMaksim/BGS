# Independent audit: even-depth newest-sector first-order splitting

Date: 6 October 2026. Canonical BGS was read-only; review workspace: `/workspace/shared/bgs_even_new_sector_review`.

## Normalized claim and primary verdict

**Verdict: proved as written.** For every integer l≥1 and N=7·5^(2l), each complete eigenspace of the actual raw cat M_N contained in the orthogonal complement of H_7⊗J_1H_(5^(2l−2)) has dimension 7, and the actual Hermitian compression P A_N P on it is simple. These spaces have total dimension 24N/25. Consequently the seven eigenvalue branches emanating from each such cat eigenvalue split to first order in exp(itA_N)M_N near t=0.

The uniform conclusion uses the exact coherent-packet reduction proved below, together with the independently reconstructed 48 finite matrices. It is not an extrapolation from small dimensions or a generic-unitarity argument. No counterexample or missing uniform implication remains in the stated theorem. Integrality in the proof is integrality **in the chosen valuation ring above 5**; the seven-factor eigenbasis must have unit determinant there. Section 5 supplies that justification explicitly. A claim that 4000L clears every possible global algebraic denominator is unnecessary and is not asserted by this review.

This does not prove old-sector splitting, a common nonzero neighborhood uniform in N, simplicity of the full or literal-coupling propagator, a full complex commutant statement, or BGS. At nonzero t the phrase “new sector” describes branches starting from that cat spectral subspace, not an asserted invariant subspace of A_N or U_N(t).

## Exact source binding and inherited inputs

Audited source: `inputs/even_new_sector_first_jet.md`, copied from `/workspace/shared/bgs_seven_adic_resume/cat_splitting/even_new_sector_first_jet.md`.

SHA-256: `7e043149e73445cdd0f413f8ce9460b4c1de9690355c83d992e88ad3fbb2ad39`.

All five file hashes in the frozen `new_sector_candidate_manifest.json` were checked and matched. Dependencies:

- `uniform_cat_multiplicity_v2.md`, SHA-256 `b6e219832f094136f0ca80201ae61f80a9d2435bebc59dd2f18163e3444c8e1e`, with its accepted `V2_BINDING.md`: simple prime-power cat spectrum for all primitive-root variants, order lifting, and seven-factor eigenvalue multiplicities 3,2,2.
- `oldform_tower_compression.md`, SHA-256 `d359482763667a6707ed9a060a3874e951f95336561a4ac645df453022b085ae`; accepted independent report SHA-256 `f3d142204ed6d10015e70595633c714acaf097fa1b0e6f19fdf6a51d4e663be5`: the isometric oldform embedding, exact intertwining, and complete-product-eigenspace isolation, including m=1.
- Canonical `mathematics/fixed_model_symmetry_theorem.md`, Section 1, copied into `inputs/`, fixes the actual raw quadratic kernel, modular midpoint convention, centered symbol, and S action.

The author's finite code and JSON were read. No author verifier, field implementation, determinant implementation, or Fourier-assembly code is imported by either independent checker. The author's JSON is used only for a final exact coefficient comparison. The candidate's manifest does not pin all transitive Python imports (its field implementation and auxiliary polynomial routines); this is an author-run provenance limitation, not a gap in the independently pinned replay here.

The accepted dependencies are inherited inputs, not newly proved universal results of this audit. Their relevant mathematical mechanisms were inspected. Kelmer's coherent/norm-circle mechanism is acknowledged as prior context; no external source is used as a new load-bearing leaf or novelty premise.

The observed canonical HEAD at the initial check was `801de3ab760cab4349e68b9843dcd67955314e62`, with empty porcelain status. No canonical `.mathbox` ledger was found. This report makes no claim about other actors' later concurrent work.

## Claim card and dependency graph

For an odd modulus d, use its induced primitive root q_d and the prescribed raw matrices

    M_d(x,y)=d^(−1/2) q_d^(−8^(−1)(3x²−2xy+3y²)),
    (T_d(a,b)f)(x)=q_d^(b(x+2^(−1)a)) f(x+a).

All inverses are modular; square-root normalizations are positive real. Write h=5^l, n=h² and L=6·5^(l−1). The exact CRT permutation identifies M_N=M_7⊗M_n and T_N(v)=T_7(v)⊗T_n(v), with their respective induced primitive roots. Define W_new=(H_7⊗J_1H_(n/25))^⊥. The assertion concerns PAP for every complete M_N eigenprojection P whose range lies in W_new.

Dependency graph:

1. Raw model → exact CRT phases and actual 32-mode coefficients.
2. Raw coherent states + exact cat covariance → monomial cycles on labels modulo h.
3. Oldform intertwining + anisotropic norm form + order lifting → primitive norm circles exhaust the newest layer.
4. Accepted prime-power simplicity + cubic closure of each cycle → all three prime-power factors for a complete product eigenvalue occupy one circle; block size 7.
5. Exact cycle eigenvectors and duals → denominator L and explicit weighted intersection formula.
6. Actual coefficients at i→2 + exact quadratic intersection counts → only 48 residue types, uniformly in l.
7. Independent polynomial determinant/gcd certificates + local integral seven-basis lift → nonzero characteristic-zero discriminant → Hermitian compression simple.
8. Standard finite-dimensional degenerate perturbation at a fixed N → distinct first-order eigenphase slopes.

## Independent uniform derivation

### 1. Coherent basis, representative phases, and the old/new dictionary

Let ψ(x)=h^(−1/2) when h divides x, and 0 otherwise. In M_nψ the sum over y=ht is a geometric sum with t-coefficient h·4^(−1)x. It vanishes unless h divides x. On that support the remaining quadratic exponent vanishes modulo h² and the sum is h. Therefore M_nψ=ψ exactly for every primitive q_n.

Directly,

    ⟨ψ,T_n(a,b)ψ⟩ = 1 if h|a and h|b, and 0 otherwise.

When both divisibilities hold, the midpoint exponent is a multiple of h²; there is no residual sign. Thus φ_v=T_n(v)ψ, for v=(a,b) modulo h, is an orthonormal basis of H_n. This uses the raw midpoint, not the ordinary midpoint convention.

For representatives r modulo h and d∈Z², direct substitution on the support x≡−r_a (mod h) gives

    φ_(r+hd)=q_n^(2_n^(−1) h ω(d,r)) φ_r,
    ω((a,b),(c,d))=ad−bc.                                      (A)

Together with T(u)T(v)=q_n^(2_n^(−1)ω(u,v))T(u+v), this gives every translation edge phase explicitly. Cat covariance gives M_nφ_v=φ_(Sv), with S=[[3,4],[2,3]], and (A) gives its reduced-label edge phase. All such phases have 5-power order and reduce to 1 at every prime above 5. This is an exact statement, not an approximation as h grows.

Apply the accepted J_1 intertwining to the smaller coherent vector: J_1ψ_(h/5)=ψ_h, and T_n(5u)J_1=J_1T_(n/25)(u). Hence the first oldform layer is exactly the span of φ_v with both coordinates divisible by 5. Its orthogonal complement consists of the primitive labels. It has dimension h²−(h/5)². This argument includes l=1 and the one-dimensional m=1 endpoint.

### 2. The primitive norm circles are exactly the cycles

Put Q(a,b)=2b²−a². Since 2 is nonsquare modulo 5, Q(v) is a unit precisely when v is primitive. The matrix S preserves Q.

An explicit ring interpretation removes any transitivity assumption: identify v with a+b√2 in R=(Z/h)[√2]. Its ring norm is −Q(v), a unit. Two vectors of equal unit Q differ by a unique norm-one multiplier. Such a multiplier acts freely. Over F_5 there are six points of each nonzero norm. The gradient (−2a,4b) is nonzero modulo 5, so each norm-circle point has five lifts at every further level. Each circle consequently has 6·5^(l−1)=L points, and so does the norm-one group.

Multiplication by 3+2√2 is exactly S. Its order is L by the accepted elementary order-lifting identity S^(6j)−I=5^(1+v_5(j))B_j, with B_j invertible modulo 5. Thus it generates the whole norm-one group. Every primitive circle O_c is one free S-cycle of length L. There are 4·5^(l−1) such circles; their total size is 24·5^(2l−2), exactly h²−(h/5)². No primitive labels are omitted or counted twice.

### 3. Actual eigenvectors, cubic partners, and denominator L

Number one circle v_k=S^k v_0, 0≤k<L. Write Mφ_(v_k)=θ_kφ_(v_(k+1)), with θ_k of 5-power order, and α_0=1, α_k=∏_(r<k)θ_r. For each λ satisfying λ^L=α_L, an unnormalized eigenvector is

    e_λ = Σ_(k=0)^(L−1) α_k λ^(−k) φ_(v_k).

All its coefficients are roots of unity; its squared Hermitian norm is L. Its dual on this cycle is therefore L^(−1) times the coefficientwise inverse. This supplies the exact denominator L even when 5 divides L. No reduction of a ramified spectral projector is used.

The set of eigenvalues of this cycle is closed under multiplication by cube roots, since 3|L. Accepted global simplicity of M_n ensures two different cycles share no eigenvalue. It follows that whenever λ, λ/ω, λ/ω² are the prime-power eigenvalues participating in one product-cat eigenvalue, they all belong to this same circle. The seven-factor multiplicities are 3,2,2, so the complete block has size 7. Together with the accepted oldform completeness result, this proves the exact full-eigenspace, rather than invariant-fragment, claim.

For T_n(u), only source labels y with y,y+u∈O_c contribute. With k_y and k_(y+u) their indices, the corresponding term of

    L ⟨e_(λ_i)/√L, T_n(u) e_(λ_j)/√L⟩

is a product of roots of unity; explicitly its residue is

    γ_i^(k_(y+u)) γ_j^(−k_y),                       (B)

where γ_i is the residue of λ_i. Because λ_i^L has 5-power order, γ_i^6=1. If the common product eigenvalue divided by Tr(M_7) has residue ξ^t, and H_7=M_7/Tr(M_7) has eigenvalues z_i∈{1,ω,ω²}, then γ_i=ξ^t/z_i exactly. The factors α and every raw Weyl edge phase reduce to 1, which proves (B), including its signs and source/target order.

An orbit base can be chosen to reduce to the base used in the six-point F_5 circle. Alternatively, changing it conjugates the residue matrix by a diagonal matrix with entries powers of γ_i, leaving the characteristic polynomial unchanged. The primitive seventh-root choices are all Frobenius-conjugate because ord_7(5)=6; ξ^t ranges through all six tame choices and i→2 is fixed by that Frobenius.

### 4. Exact actual-symbol and two-regime intersection reduction

The unchanged centered physical symbol independently expands to 32 Gaussian-rational coefficients d_v/4000. At the Gaussian prime i→2, all diagonal coefficients reduce to zero. The lower coefficient −3+4i=−(2−i)² has valuation 2; its scalar multipliers are units. The upper coefficient −3−4i is a unit. Thus only a=1 survives, with b=0,±1,±6,±7,±8. Their individually retained d-values are

    b=0: (−12,−16);
    b=±1: (−6,−8);
    b=±6: (3,4);
    b=±7: (6,8);
    b=±8: (3,4).

Here each pair is (real part, coefficient of i). No aliases such as b=1 and b=−6 are merged before the exact seven-factor and five-factor Weyl phases are evaluated. Every surviving u=(1,b) has unit Q(u) modulo 5.

For Q(y)=Q(y+u)=c, subtraction gives the linear equation B(y,u)=−Q(u)/2, where B is the polar bilinear form. Since Q(u) is a unit, every solution of this linear equation is uniquely

    y=−u/2+sJu,  J=[[0,2],[1,0]].

The identities B(u,Ju)=0 and Q(Ju)=−2Q(u) give

    s²=(1−4c/Q(u))/8 mod h.                        (C)

For a nonzero square right side modulo 5 there are exactly two roots, each with unique lift; a nonsquare has none. If the right side is zero modulo 5, every root is 0 modulo 5. More explicitly, at level l≥2 a nonzero right side of valuation 2r<l has 2·5^r roots (r≥1), and odd valuation has none; a zero right side modulo 5^l has 5^floor(l/2) roots. Thus every nonzero root count in this degenerate class is divisible by 5. At l=1 there is instead exactly one root.

All degenerate roots determine the same source and target label modulo 5. Since S acts freely on the six-point circle, their orbit indices agree modulo 6. Therefore every summand (B) has the same residue weight, and their sum vanishes for l≥2. For generic roots, the two lifted roots give exactly the two mod-5 weights. This proves, uniformly in l and in every unit c, exactly the source's two regimes: retain the degenerate point for l=1; omit the entire degenerate mode for l≥2. It is not a claim that the characteristic-zero degenerate contribution vanishes.

### 5. Seven-factor integral basis and discriminant lift

Fix a number field containing the relevant roots and a prime above 5 with i→2; use its valuation ring O. The raw seven-factor matrix G_7 has integral entries, and Tr(G_7) is a unit in O: its nonzero residue is checked in the seven-factor construction (equivalently its Gauss norm is supported at 7). Hence H_7=G_7/Tr(G_7) is O-integral. Its three eigenvalue differences and 3 are units at 5.

The exact spectral projectors are

    E_z=(I+z^(−1)H_7+z^(−2)H_7²)/3.

Their reductions have ranks 3,2,2. Select independent columns in each reduced E_z and lift the same columns from the characteristic-zero projectors. The resulting eigenvector matrix V_7 reduces to an invertible matrix, so det(V_7) is a unit and both V_7 and V_7^(−1) are O-integral. Consequently every B_7(u)=V_7^(−1)T_7(u)V_7 is O-integral. A mere “integral eigenbasis” without the determinant condition would not suffice; this construction supplies the condition and can lift the author's chosen residue eigenbasis as well.

Use unnormalized e_λ coordinates in the prime-power factor. Their dual denominator is exactly L, by Section 3. Therefore 4000L times the actual seven-dimensional compression has O-integral entries. In the explicit product basis its residue is one of the 48 matrices, or a similar matrix after orbit-base/eigenbasis changes. The Hermitian compression's characteristic polynomial is invariant under these algebraic basis choices.

A squarefree residue characteristic polynomial has nonzero discriminant. The characteristic-zero discriminant of the scaled matrix therefore cannot vanish; dividing by the nonzero scalar 4000L preserves simplicity. Since the original compression is Hermitian, its seven slopes are real and distinct. The derivative of exp(itA)M on a cat eigenspace of eigenvalue λ is iλ PAP, giving the stated local first-order splitting at each fixed N.

## Obligation matrix

| Obligation | Result |
|---|---|
| Raw modular midpoint and covariance orientation | Passed; exact exponents (A), direct kernel controls |
| ψ normalization, stabilizer, and full coherent basis | Passed |
| Primitive labels equal first-oldform complement, including l=1 | Passed |
| Norm-circle transitivity, size, and exhaustive coverage | Passed by norm ring, smooth lifting and exact S order |
| Same circle for all cubic partners | Passed using simple M_n and 3|L |
| Complete full-M blocks of dimension 7 | Passed with accepted completeness input |
| Integral coordinates and exact L denominator | Passed; explicit cycle eigenvectors and unit-determinant seven basis |
| Actual Gaussian coefficients and raw aliases | Passed by independent Fourier assembly |
| γ source/target signs and tame character coverage | Passed |
| Generic and degenerate intersection counts | Passed, with separate l=1 endpoint |
| 48 matrices constructed from actual compression | Passed, uniformly justified before finite verification |
| Squarefreeness of all 48 | Passed independently by polynomial determinants and gcds |
| Lift to characteristic zero | Passed in the valuation ring above 5 |
| Old-sector, full/literal U, full commutant, BGS | Out of scope |

## Independent replay and exact tested ranges

Run from this review workspace:

    python3 run_audit.py

The wrapper runs `replay.py` and `check_packets.py`, with a 60-second wall timeout per process, 30-second CPU limit, 512 MiB address-space limit, and one-CPU affinity. It records before/after input hashes, declared results, subprocess output, software, runtime, and actual exit codes in `computation_manifest.json`. The supplied computation-audit validator accepted the completed version-2 manifest with its input/output hash checks. All scripts use explicit runtime checks rather than removable assertions. No random sampling or floating-point arithmetic is used in either mathematical checker.

`replay.py` uses F_5[w]/(1+w+w²+…+w⁶), with w a primitive seventh root. It constructs and exhaustively verifies a multiplicative generator covering every nonzero residue, establishing that the implemented quotient is a field. This differs from the author's order-63-root representation. The selected generator is integer encoding 7; ξ has encoding 1314. It obtains eigenvectors by spectral-projector columns, rather than author nullspaces. It computes det(XI−C) directly as a polynomial using subset expansion, rather than eight determinant evaluations and interpolation. Every degree-seven characteristic polynomial has derivative gcd degree 0.

An explicit isomorphism sends this w to the author's w=t⁹; it sends the independent ξ to the inverse of the author's ξ. All 48 polynomials exactly match the author JSON after the corresponding tame-index permutation t↦5t modulo 6. `finite_results.json` contains every independent coefficient list and the actual Gaussian symbol.

`check_packets.py` tests h=5,25,125 (l=1,2,3), with **all 124 primitive circles at those levels and all nine upper modes**. It checks exact actual cat phases on the coherent support, exact Weyl phases, actual cycle eigenvector recurrences, actual cyclotomic packet-entry exponents and their residues, quadratic intersection parametrization and counts, dimension completeness, and all six tame characters and nine ordered pairs of cube-root eigenvalue labels. Specifically:

- 1,968,875 exact raw cat/coherent phase entries, all coherent labels and every support coordinate at all three levels.
- 540,000 exact raw Weyl/coherent phase entries for all 32 modes: all labels at h≤25, and the nine explicitly recorded labels at h=125; all support coordinates for each tested label.
- 391,250 coherent Gram support/geometric-sum pair controls, exhaustive at h=5 and 25.
- 108,144 exact cycle eigenvector recurrence controls; all cycle eigenvalues at h≤25, six recorded representatives at h=125.
- 123,930 exact cyclotomic packet-entry exponent/residue controls with the same eigenvalue scope.
- 1,116 exact quadratic-versus-circle intersection instances.
- 60,264 residue mode/packet comparisons, exhausting all circles, upper modes, six tame characters, and ordered cube-root label pairs at the three levels.

Every assertion passed. `packet_results.json` records the exact scopes, circle monodromy exponents, counts and software. These finite checks supplement the uniform proof; h=125 was included to enter the next degenerate-root-count pattern, not to extrapolate a theorem from additional successes.

## Remaining gap, exposition repair, and strongest safe conclusion

There is no remaining mathematical gap in the stated newest-sector theorem. The advisable exposition repair is to replace unqualified “integral” by “integral in the valuation ring at the chosen prime over 5” and include the unit-determinant projector-column construction from Section 5. This clarifies the correct coefficient domain without changing the theorem or any certified matrix.

The strongest safe conclusion is the full uniform local first-order splitting statement at the top of this report, on exactly 24/25 of the even-depth cat spectral dimension. The untouched old-sector problem and any literal-coupling global collision question require additional arguments. No canonical source or status was edited. At the final repository check the HEAD and clean porcelain status were unchanged, and the live candidate source still matched the frozen SHA-256 above.
