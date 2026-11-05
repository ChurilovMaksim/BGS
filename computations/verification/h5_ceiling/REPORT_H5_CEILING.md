# H5 structural ceiling: elementary arithmetic of h_p (BGS-TRACE-348..351)

*5 November 2026. Source material: the research pass `research1105` (`AUDIT_H5A.md` §1.3, `BYPASS.md` §1.1–1.2), re-derived
and re-checked independently for this integration. Registry ids BGS-TRACE-348..351 (next free after BGS-TRACE-347 on
origin/main `3995d691`; open PR branches #83, #84, #85 register nothing above BGS-TRACE-336).*

**Tags.** [P] paper proof given here · [CA] exact integer computation · [N] floating-point evidence · [H] heuristic.

## 0. Convention (checked)

ε = 1 + √2, ε̄ = 1 − √2 = −ε⁻¹, λ = ε² = 3 + 2√2, O = Z[√2]. Write εⁿ = a_n + b_n√2 (a_0 = 1, b_0 = 0,
a_{n+1} = a_n + 2b_n, b_{n+1} = a_n + b_n). Then

    h_n := (εⁿ + ε̄ⁿ)/2 = a_n,   a_{n+2} = 2a_{n+1} + a_n,   a_0 = a_1 = 1,

which is exactly the convention of BGS-TRACE-342 and `Bgs.H6LemmaW` (`hpair`: h_0 = h_1 = 1, h_{n+2} = 2h_{n+1} + h_n;
h_3 = 7, h_5 = 41, h_7 = 239, h_11 = 8119 = 23·353, h_13 = 47321 = 79·599). For odd p, h_p = u_{(p−1)/2} with u_0 = 1,
u_1 = 7, u_{n+1} = 6u_n − u_{n−1} (the convention of BGS-TRACE-265/344). The first identity is proved in Lean
(`Bgs.H5CeilingArith.a_eq_h6`, every n); both are checked in `code/h5_arith.py` (every odd prime p ≤ 1500).

Two facts are used throughout:
- **(N)** a_n² − 2b_n² = N(εⁿ) = (−1)ⁿ; for odd n, a_n² − 2b_n² = −1.
- **(O)** a_n is odd (a_{n+1} ≡ a_n mod 2), so every prime q | h_n is odd.

Let q be an odd prime and s ∈ F_q with s² = 2 (when one exists). The ring map Z[√2] → F_q, √2 ↦ s, sends ε to
e := 1 + s, and eⁿ = a_n + b_n s. Also e(1 − s) = 1 − s² = −1, so e ≠ 0.

## 1. BGS-TRACE-348 — Lemma W sharpened [P]

**Claim.** Let p be an odd prime and q a prime with q | h_p. Then q ≡ 1 (mod 2p) and q ≡ ±1 (mod 8).
The mod-8 part holds for every odd index n in place of p.

*Proof.* By (O), q is odd. By (N) with a_p ≡ 0 (mod q), 2b_p² ≡ 1 (mod q). So s := 2b_p satisfies
s² = 4b_p² = 2·(2b_p²) ≡ 2: 2 is a quadratic residue mod q, hence q ≡ ±1 (mod 8) (second supplementary law). This used
only that p is odd.

Let s be any square root of 2 in F_q, e = 1 + s. Then e^p = a_p + b_p s = b_p s, so e^{2p} = b_p²s² = 2b_p² = 1, i.e.
(e²)^p = 1. Also e² − 1 = 2s + s² = 2(1 + s) = 2e ≠ 0, because q is odd and e ≠ 0. Since p is prime, e² has order
exactly p in F_q^×, so p | q − 1. q is odd and p is odd, hence 2p | q − 1. ∎

*Relation to BGS-TRACE-342* (unchanged). TRACE-342 states q ≡ ±1 (mod 2p); its proof treats a split case (p | q − 1)
and an inert case (p | q + 1). The first step above shows that 2 is always a square mod q, so q always splits and the
inert branch never occurs: the "−1" class is empty. TRACE-342 remains true as stated; this claim is strictly sharper.

**Checks.** [CA] `code/h5_arith.py` (A): every prime q < 10⁷ (664,579 primes, **no residue-class presieve**) and every
odd prime p ≤ 1500; 207 hits q | h_p (each re-confirmed with the exact big integer), 0 violations of q ≡ 1 (mod 2p),
0 violations of q ≡ ±1 (mod 8). Complete factorisations of h_p for all odd primes p ≤ 61 (sympy; factors above 2⁶⁴
are BPSW probable primes): every factor satisfies both congruences, all squarefree. Lean: `prime_dvd_mod2p`,
`prime_dvd_mod8`, `orderOf_lambda` (general proofs for every p, q).

## 2. BGS-TRACE-349 — pairwise coprimality [P]

**Claim.** For distinct odd primes p ≠ p′, gcd(h_p, h_{p′}) = 1. Equivalently, every prime q divides h_p for at most
one odd prime p, namely p = ord(λ mod 𝔮).

*Proof.* Suppose a prime q divides both. By §1, 2 is a square mod q; fix one square root s. The proof of §1 shows
that ord((1 + s)²) = p and, with the same s, = p′. So p = p′. ∎

**Checks.** [CA] (B): exact big-integer gcd(h_p, h_{p′}) = 1 for all 28,203 pairs of odd primes p < p′ ≤ 1500; no prime
q < 10⁷ is hit by two different p in (A). Lean: `coprime_h` (general).

## 3. BGS-TRACE-350 — the Sophie Germain family [P]

**Claim.** (i) If n ≡ 3 (mod 4) and q = 2n + 1 is prime, then q | h_n (n need not be prime).
(ii) If n is odd, q = 2n + 1 is prime and q | h_n, then n ≡ 3 (mod 4).
(iii) For a prime p ≡ 3 (mod 4) with 2p + 1 prime, the least prime factor of h_p is exactly 2p + 1, and h_p is
composite for p ≥ 5.

*Proof.* (i) q ≡ 7 (mod 8), so 2 is a square mod q; take s, e = 1 + s ≠ 0. By Fermat, e^{2n} = e^{q−1} = 1. With
A = a_n, B = b_n, eⁿ = A + Bs and (N) 2B² = A² + 1, so
e^{2n} − 1 = A² + 2B² + 2ABs − 1 = 2A² + 2ABs = 2A·eⁿ (the F_q image of λⁿ − 1 = 2h_nεⁿ). Hence 2A·eⁿ = 0;
2 ≠ 0 and eⁿ ≠ 0, so A ≡ 0, i.e. q | h_n.
(ii) By the mod-8 part of §1, q ≡ ±1 (mod 8); for odd n, n ≡ 1 (mod 4) gives q ≡ 3 (mod 8). So n ≡ 3 (mod 4).
(iii) By (i), 2p + 1 | h_p; by §1 every prime factor of h_p is ≡ 1 (mod 2p), hence ≥ 2p + 1. So the least prime
factor is 2p + 1. For p ≥ 5, h_p ≥ 2^{p−1} > 2p + 1, so h_p is composite. ∎

So these p are never "good" (h_p prime or with all prime factors large) for any positive exponent. Whether the family
is infinite is the Sophie Germain problem, which is open; **no density statement follows from this claim.**

**Checks.** [CA] (C): for every odd prime p ≤ 1500, (2p+1) | h_p ⟺ (p ≡ 3 mod 4 and 2p+1 prime), with no mismatch;
trial division of h_p by **all** primes ≤ 2p + 1 shows that the only one that can divide is 2p + 1; the p with
least prime factor 2p + 1 are exactly this family. For 5 ≤ p ≤ 1500 there are **25** such p:
11, 23, 83, 131, 179, 191, 239, 251, 359, 419, 431, 443, 491, 659, 683, 719, 743, 911, 1019, 1031, 1103, 1223, 1439,
1451, 1499 (see `logs/h5_arith.json`). Lean: `sg_dvd`, `sg_iff`, `sg_minFac` (general).

## 4. BGS-TRACE-351 — product formula [P]

**Claim.** For every odd n ≥ 1, h_n = ∏_{k=1}^{(n−1)/2} (6 − 2cos(2πk/n)).

*Proof.* With ζ = e^{2πi/n}, (xⁿ − 1)/(x − 1) = ∏_{k=1}^{n−1}(x − ζ^k). At x = λ: λⁿ − 1 = εⁿ(εⁿ − ε⁻ⁿ) and, n odd,
ε⁻ⁿ = (−ε̄)ⁿ = −ε̄ⁿ, so λⁿ − 1 = 2h_nεⁿ; λ − 1 = 2ε. The left side is h_nε^{n−1} = h_nλ^{(n−1)/2}. Pairing k with n − k,
(λ − ζ^k)(λ − ζ^{−k}) = λ² − 2λcos(2πk/n) + 1 = λ(6 − 2cos(2πk/n)), since λ + λ⁻¹ = 6. Cancel λ^{(n−1)/2}. ∎

**Checks.** [N] (D): mpmath at 80 digits, every odd n with 3 ≤ n ≤ 301: maximal relative error 3.3·10⁻⁸⁰.
Not formalized in Lean.

## 5. Scope and non-claims

- These are elementary arithmetic facts about the integers h_p. They do not bound any class sum, do not touch H5(a)
  (BGS-TRACE-303, open), H6 (BGS-TRACE-304), H7* (BGS-TRACE-305) or Theorem R♯-mod v5 (BGS-TRACE-325, conditional), and
  say nothing about the frozen R′ (BGS-TRACE-206, open).
- TRACE-342 is not edited. Squarefreeness of h_p is not proved.
- The structural-ceiling discussion that uses these facts is the research note
  `evidence/research/20261105_h5_ceiling/NOTE.md`; it is not registered.

## 6. Reproduction

    export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
    python computations/verification/h5_ceiling/code/h5_arith.py      # TRACE-348..351 checks  -> logs/h5_arith.json
    python computations/verification/h5_ceiling/code/h5_density.py    # research note [CA+N]   -> logs/h5_density.json
    python computations/verification/h5_ceiling/code/thmL_sanity.py   # research note [N]      -> logs/thmL_sanity.json
    (cd formalization && lake build Bgs.H5CeilingArith)

Run with Python 3.13.5, numpy 2.5.4, sympy 1.14.0, mpmath 1.3.0 (venv `/workspace/venv_audit`), 1 thread.
