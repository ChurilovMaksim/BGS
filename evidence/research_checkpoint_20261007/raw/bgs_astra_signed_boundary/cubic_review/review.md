# Independent audit: cubic off-charge boundary witness

Date: 7 October 2026. Canonical BGS access was read-only. All audit outputs are confined to this `cubic_review` directory. No canonical edit, theorem promotion, publication, or actual-map claim was performed.

## Normalized claim and verdict

**Primary verdict: proved as written, in the explicitly restricted changed-family scope.**

Let primes p ≥ 5 tend to infinity through p ≡ 2 (mod 3), and let

    V_p(j,k) = p^(-1/2) exp(2πi j³k³/p),  j,k ∈ F_p.

This family is unitary, exactly flat, and has uniformly vanishing nonzero diagonal charge-block norms. For every nonnegative nonzero smooth w supported in a fixed band 0 < a < b < 1/4 and every fixed κ > 0, the original signed occupation-mismatched pair aggregate, still restricted to

    h(y−x) > floor(0.49m),
    s(y−x) > floor(κp/log p),

is bounded below by

    p c_w + o(p),    c_w = ∫ (1/4−t)w(t)dt > 0.

Its switch-damped aggregate at z_p = 1−A log p/p tends to zero for A > 4/a. Thus its exact signed marked-switch boundary integral has the same linear lower bound. This refutes closure from position-chain flatness, diagonal charge-block contraction and the universal exact switch/occupation transfer algebra alone.

It does **not** refute a criterion retaining every actual FM-021/FM-022 input. In particular, V_p is symmetric and its reverse kernel is exactly J_p, of norm 1. It does not preserve the fixed quantization, the prescribed smooth symbol, the fixed coupling, or the actual reverse-path bound. The proof is along the stated prime subsequence; no assertion that this is the actual operator through all odd dimensions is made.

Audited candidate SHA-256:

    180e1c45acdf9f8c6db5a8c6b0fe8ebf3dfd4ddafd5b5307ea674823298077bb

## 1. Dependency graph and source roles

1. Integer occupation expansion + Parseval + cyclic matrix differentiation + unitarity imply the universal bound B_m(U) ≤ mN.
2. Cubing permutes F_p for p ≡ 2 (mod 3). Permutation conjugacy to the Fourier matrix gives flatness, V_p² = reflection and V_p⁴ = I. Elementary quadratic differencing gives the optional odd-power trace statement.
3. Direct charge-block multiplication + injectivity of cubing + elementary quadratic/cubic differencing + the Hermitian row-sum bound give uniform charge-block norm decay.
4. The exact occupation projector identifies G(1,1) = |Tr V_p^m|²−B_m(V_p). Multiples of four, the universal occupation bound, and ordinary Riemann sums give the divergent lower bound.
5. The universal raw off-charge Hamming estimate, equation (3) of `inputs/11_fractional_hamming_cancellation.md`, annihilates the entire low-Hamming trace because P−J = 0 and m−2r > 0.
6. The universal exact block and torus identities T1–T5 and zero-run/word-count estimates T10–T12 of `inputs/13_global_switch_transfer.md` remove the disjoint high-Hamming low-switch mask. The charge-gap hypothesis needed here is proved directly in step 3 for V_p; no actual-parametrix input is imported.
7. T6–T9 give a negligible high-Hamming damped endpoint. T15 is a finite-polynomial fundamental-theorem-of-calculus identity and identifies the divergent integrated boundary term.

Every analytic/algebraic leaf in this chain is elementary or a specifically supplied project theorem whose needed universal argument was checked below. There is no external Weil, Dirichlet, actual parametrix or Haar-tail leaf. The source `13_global_switch_transfer.md` retains its original candidate/conditional-actual-map header; this audit verifies its universal transfer algebra as used for this explicit family, and makes no independent promotion of its actual-map hypothesis.

All 18 copied inputs in `source_manifest.json` match their recorded SHA-256 values. In particular:

- Hamming source: `10fd5b3e5d14d54c7d2b3ad2ace7b9d474a47f142b5a87e35fcf73b894ecaeb5`
- Switch-transfer source: `4a333b1847eb466ef66326e26562ee63770f6e09ed7f47d7b517e5fbf5e6d0be`

Repository instructions, source-of-truth and convention files, research brief, relevant ledger/registry entries, theorem index, open-obligation surface and fixed-map definitions were inspected. They retain deterministic BGS and TRACE-005 as open. The record distinguishes the universal algebra here from the actual map's additional inputs.

## 2. Independent derivation

### 2.1 Universal occupation-gradient inequality

For any unitary U on C^N, write the homogeneous degree-m polynomial

    f(x) = Tr((diag(x)U)^m) = Σ_(|n|=m) c_n x^n.

The exponents n_j are nonnegative integers, including all repeated coordinates. With normalized measure on T^N,

    B_m(U) = Σ_n |c_n|²,
    Σ_j ∫ |∂_(θ_j) f(e^(iθ))|² dθ
       = Σ_n (Σ_j n_j²)|c_n|² ≥ m B_m(U).

The last inequality follows termwise from n_j² ≥ n_j. Put W = Z_θ U. Since ∂_j W = i E_jj W, the m product-rule terms have the same trace by cyclicity:

    ∂_j Tr(W^m) = im Tr(E_jj W^m) = im (W^m)_jj.

W is unitary at every θ, so Σ_j |(W^m)_jj|² ≤ N. Integrating proves B_m(U) ≤ mN. This includes m = 1 and arbitrary m ≥ N; it does not require distinct labels, square-free monomials, or an averaging assumption on the target U. The torus is only the exact projector selecting equal occupation vectors.

### 2.2 Prime family and recurrence

There are infinitely many primes ≡ 2 (mod 3) without invoking Dirichlet: if their finite list included 2 and had product Q, the odd integer 3Q−1 is ≡ 2 (mod 3), is divisible by none of the listed primes, and has a prime factor ≡ 2 (mod 3).

Because gcd(3,p−1) = 1, j ↦ j³ is a permutation. Define the permutation operator S by (Sf)(j)=f(j³). Then V_p = S F_p S*, genuinely a similarity and not just a one-sided row permutation. Thus V_p is unitary and flat. The usual character sum gives F_p²(j,l)=1_(l=−j). Cubing commutes with negation, so also V_p²(j,l)=1_(l=−j), and V_p⁴=I.

Consequently Tr(V_p^m)=p for 4|m and Tr(V_p^m)=1 for m ≡ 2 (mod 4). For odd m, similarity reduces the assertion to the normalized quadratic Gauss sum (or its conjugate). Differencing that sum gives squared modulus 1. Hence the candidate's full trace-square formula is correct, though only the 4|m case is needed.

### 2.3 Uniform nonzero charge contraction

Fix c ≠ 0. For B_c(j,k) = V_p(j,k) conjugate(V_p(j+c,k+c)),

    (B_c B_c*)_(j,l)
       = p^(-2) Σ_k e_p(a k³ − b(k+c)³),
    a = j³−l³,    b = (j+c)³−(l+c)³.

For j ≠ l, both a and b are nonzero. If a−b ≠ 0, the phase is cubic; otherwise it is quadratic with coefficient −3bc ≠ 0. The exclusions p ≥ 5 and c ≠ 0 are essential here.

For a nondegenerate quadratic q, the identity

    |Σ_k e_p(q(k))|² = Σ_h Σ_k e_p(q(k+h)−q(k))

has h=0 contribution p and all other inner sums zero, so its modulus is sqrt(p). For a genuine cubic f, every h ≠ 0 derivative f(k+h)−f(k) has nonzero quadratic coefficient 3a_3h. The same identity and the triangle inequality give

    |Σ_k e_p(f(k))|² ≤ p+(p−1)sqrt(p) ≤ 2p^(3/2).

Thus diagonal entries of B_c B_c* are p^(-1), while off-diagonal entries have modulus at most sqrt(2)p^(-5/4). The Hermitian row-sum bound gives

    ||B_c||² ≤ p^(-1)+sqrt(2)(p−1)p^(-5/4)
              ≤ p^(-1)+sqrt(2)p^(-1/4).

Since p^(-1) ≤ p^(-1/4), this also gives exactly the candidate's weaker norm estimate sqrt(1+sqrt(2))p^(-1/8). All constants are uniform over nonzero c.

The zero-charge block is J_p; on traceless diagonal operators it is zero. Nonzero-charge blocks lie entirely perpendicular to the identity. Therefore the charge-pinched transfer on I-perp has norm exactly the maximum nonzero-block norm, tending to zero.

### 2.4 The signed aggregate and its sign

A rooted path x has amplitude A(x)=∏_j V_p(x_j,x_(j+1)). Expanding Tr((Z_θV_p)^m) and its conjugate gives exactly the occupation-difference character. The normalized torus integral retains precisely n(x)=n(y), including repetitions. Hence

    Σ_(n(x)≠n(y)) A(x)conjugate(A(y))
       = |Tr(V_p^m)|²−B_m(V_p).

For w ≥ 0,

    p^(-2)Σ_m w(m/p) G_(p,m)(1,1)
      ≥ Σ_(4|m) w(m/p) − p^(-1)Σ_m m w(m/p)
      = p[¼∫w(t)dt−∫t w(t)dt]+o(p).

The band b < 1/4 makes c_w strictly positive. There is no claim that the summands G_(p,m) are positive. Their signs are retained until the complete weighted sum is taken. Every masked aggregate used below is real because swapping x and y conjugates its amplitude and preserves occupation mismatch, h and s.

### 2.5 Low-Hamming removal

For r=floor(0.49m), m−2r > 0 for every integer m ≥ 1. The raw off-charge Hamming theorem gives

    |low-Hamming signed trace|
       ≤ 2(p²−1) [Σ_(j≤r) binom(m,j)] ||P−J||^(m−2r) = 0.

No 0^0 convention is used. This is a bound on the complete literal off-charge Hamming mask; no centered balanced range projector is substituted for it. In the source proof, the needed k=1 cyclic compressed trace estimate has at least m−2r diagonal-to-diagonal transitions, and exact torus averaging imposes occupation balance. It is therefore applicable to every unitary with P=J, including this family.

### 2.6 Low-switch removal, with the Hamming restriction retained

For an arbitrary difference word c, the occupation-twisted fiber is the cyclic trace of the blocks B_(c_j,c_(j+1)) with their unitary row phases. These phases preserve every nonzero diagonal block norm. Zero-charge row phases are trivial.

Unitarity gives B_(c,0)1=0 for c≠0 and 1*B_(0,d)=0 for d≠0. Thus in a nonconstant word, every internal zero-charge run permits replacement of its internal P factors by P−J. Here any positive number of such factors annihilates the product exactly. A zero run of length one has no internal factor and causes no difficulty.

There are precisely m−s(c) diagonal block factors. It follows uniformly in θ that

    |F_θ(c)| ≤ p ρ^(m−s(c))

whenever every nonzero diagonal charge block has norm ≤ρ and the zero centered block does also. Constant nonzero words obey the same formula; the constant zero word is entirely balanced. Subtracting the exact normalized torus integral gives

    |F_off(c)| ≤ 2p ρ^(m−s(c)).

This estimates the actual off-charge part of each complete fiber. It does not infer an arbitrary-subset estimate from a signed full-fiber bound.

There are at most binom(m,r)p^r words with r≥1 switches, plus p constant words. Hence

    Σ_(s(c)≤R) |F_off(c)|
       ≤ 2p²ρ^m + 2pρ^m Σ_(r=1)^R binom(m,r)(p/ρ)^r.

Choose γ=−logρ > 8κ/a, and use the charge decay to make this fixed ρ valid eventually. For R=floor(κp/log p), m≤bp and large p, log(bp²/ρ)≤3log p. The nonconstant sum is bounded by a polynomial prefactor times exp(−γap+3κp), and therefore by O(exp(−γap/2)) after absorbing that prefactor. This is uniform on the band.

The Hamming mask is a function of c alone. It can be imposed on this sum of absolute fiber bounds. Thus the disjoint high-Hamming low-switch contribution is exponentially small, with no checksum restriction. The full off-charge mask partitions into low Hamming, high-Hamming/low-switch, and the stated residual. The first part is exactly zero and the second is exponentially small. The linear lower bound survives unchanged.

### 2.7 Damping and the integrated boundary term

On identity-perp the transfer satisfies

    ||M(z,q,θ)|| ≤ z+(1−z)ρ,   |q|=1,  0≤z≤1.

The identity summand cancels between θ=0 and the torus integral. Extracting any Hamming set costs at most m+1, giving T8. After the original p^(-2) sum over O(p) times, this is

    O(p² exp[−(1−ρ)ap(1−z)]).

Eventually ρ≤1/2. For z_p=1−A log p/p and A>4/a, the bound is O(p^(2−Aa/2))=o(1). Subtracting high-Hamming low-switch fibers remains exponentially small uniformly in z∈[0,1], because 0≤z^s≤1 inside the fiber estimate.

Write R_(p,m)(z) for the remaining exact residual polynomial. The finite identity

    R_(p,m)(1)−R_(p,m)(z_p)
      = ∫_(z_p)^1 Σ_residual s(c)u^(s(c)−1)A(x)conjugate(A(y)) du

has no limit exchange or analytic continuation issue. Its weighted aggregate is at least p c_w+o(p), because the interior endpoint is o(1). This proves the claimed failure of the signed marked-switch boundary estimate.

## 3. Obligation matrix

| Obligation | Status | Decisive reason |
|---|---|---|
| All repeated occupation multiplicities retained | Passed | Exact nonnegative-integer monomial expansion and normalized torus Fourier projection |
| Universal gradient constant mN | Passed | Degree m, derivative im(W^m)_jj, diagonal unitary energy ≤ N |
| Infinitely many admissible dimensions | Passed | Elementary product-minus-one prime argument |
| Cubic-permuted Fourier is a similarity | Passed | S F S* with S acting by j↦j³ |
| Exact flatness and fourth power | Passed | Character sum and oddness of cubing |
| Uniform contraction for every c≠0 | Passed | Nondegenerate degree-2/3 row phases, elementary differencing and Hermitian row-sum bound |
| Original off-charge lower bound | Passed | Exact balanced subtraction bounded independently by mp |
| Original p^(-2) and rooted counting | Passed | One cyclic trace expansion, no quotient by rotations |
| Low-Hamming removal at 0.49m | Passed | Universal raw-mask theorem and positive exponent |
| κp/log p low-switch removal | Passed | Choose a fixed sufficiently small ρ using uniform decay |
| Hamming/checksum restrictions compatible | Passed | Bounds apply to each occupation-projected difference fiber; Hamming depends only on c |
| Damped residual negligible | Passed | Uniform twist contraction and correct p² aggregate prefactor |
| Integrated marked-switch term diverges | Passed | Exact finite-polynomial endpoint identity |
| Reverse-kernel decay | Failed, intentionally | Symmetry forces Q=J and ||Q||=1 |
| Literal frozen quantization / full FM-021/FM-022 package | Out of scope and not satisfied | Changed prime-dimensional family; no actual quantization preservation |
| Actual deterministic BGS conclusion | Out of scope | No actual-model signed boundary estimate is supplied |

## 4. Finite evidence and commands

The author's `check_cubic_witness.py` and `cubic_controls.json` were inspected only as supporting evidence. They do not supply any asymptotic step above.

An independently written checker, `check_independent.py`, reconstructs rooted paths and exact cyclotomic coefficient vectors directly. Arithmetic is integer arithmetic modulo the prime cyclotomic relation 1+ζ+⋯+ζ^(p−1)=0; no floating-point tolerance is used.

Executed coverage:

- Full exact V² reflection character sums and every off-diagonal charge-row phase degree for p=5,11,17,23,29.
- Exact total trace-square and balanced occupation-polynomial values for p=5,m=1..4; p=11,m=1..3; p=23,m=4.
- Literal low-Hamming off-charge cancellation in every listed case.
- Full 390625 ordered pair enumeration at p=5,m=4, retaining all occupation, Hamming and cyclic-switch masks. The disjoint mask partition agrees before cyclotomic reduction.
- All 18 input hashes and the candidate hash.
- Normal and optimized Python outputs are byte-identical. An injected failure exits unsuccessfully, so validation is not disabled by -O.

Commands (working directory is immaterial):

    python3 cubic_review/check_independent.py > cubic_review/independent_controls.json
    python3 -O cubic_review/check_independent.py > cubic_review/independent_controls_optimized.json
    cmp cubic_review/independent_controls.json cubic_review/independent_controls_optimized.json
    python3 cubic_review/check_independent.py --inject-failure

The last command is expected to fail; its traceback is saved in `injected_failure.log`. Finite cases validate definitions and implementation only. Universal and asymptotic conclusions come from Section 2.

## 5. Remaining gap, strongest safe statement and wording caution

There is no remaining mathematical gap in the candidate's stated changed-family obstruction. The actual-map signed marked-switch boundary problem remains open and is not reduced by pretending this family satisfies reverse-kernel decay.

One nonblocking clarification would improve F5's phrase “positivity at real q=1.” The transfer for q=1, real z and fixed θ is mixed-unitary (charge pinching can be written as an average of diagonal-modulation conjugates), so its total superoperator trace powers are nonnegative. The off-charge subtraction G, and the separately masked residual, need not be positive. The same witness gives exactly G_(5,2)(1,1)=1−9/5=−4/5. No false positivity assertion is needed anywhere in the proof.

The strongest safe summary is: exact flatness and vanishing charge-diagonal block norms, even with the complete universal occupation/switch transfer structure, do not force the signed high-Hamming/high-switch boundary target to vanish. Any successful actual-map closure needs further information not captured by those inputs. Reverse-kernel decay is one actual input this witness explicitly loses; this audit does not claim it alone would suffice.

The cheapest useful next check is editorial: make the referent of “positivity” explicit if that sentence is reused. No further numerical experiment is needed to justify the proved obstruction.
