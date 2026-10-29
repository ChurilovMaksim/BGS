# Random-phase cat map: exact encounter classification and the τ² coefficient (Line C)

*Canonical note for `mathematics/fixed-map/`. Prepared 2026-10-29 (Europe/Berlin) from the Line C report v2, after an independent referee audit. The packet numbered these statements BGS-TRACE-138 through BGS-TRACE-143. Main already registers BGS-TRACE-140 through BGS-TRACE-142, so the statements are registered here as BGS-TRACE-143 through BGS-TRACE-148.*

**Ensemble.** U_θ = D_θ·M_p, where M_p is the repository kernel of S = [[3,4],[2,3]] (odd N, here mostly N = p prime) and D_θ = diag(e^{iθ_x}) is a Haar (i.i.d. uniform) diagonal on all N positions. This is the *maximal* phase ensemble. It is not the 16-mode phase ensemble of BGS-TRACE-126, not a band-limited kick and **not the fixed kick**.

| ID | statement | status |
|---|---|---|
| BGS-TRACE-143 | Theorem 1 + Remark 1′: reduction to the random-phase DFT star graph; square-class dependence | proved |
| BGS-TRACE-144 | Proposition 2 + Corollary 2′: exact Gauss-sum / partition-lattice formula; rationality | proved |
| BGS-TRACE-145 | Lemmas 3–5: complete classification of the order-1/p pairs (dihedral, 2-opt, swap, figure-eight) | proved (Lean: finite instances m = 6) |
| BGS-TRACE-146 | Theorem 6 + Corollary 6′: exact coefficient identity, a₂ = −2m² for m ≥ 5, p > 4^m | proved (Lean: integer coefficient identity only) |
| BGS-TRACE-147 | Theorem 7: exact expansions for m ≤ 12; c₂ ≠ 2m³ at m = 5, 6, 8, 9, 12; p^{−5/2} and character terms; small-p exactness ranges | verification-pending (computer-assisted; independent replay deposited 2026-10-29; status review pending, as for BGS-RES-022) |
| BGS-TRACE-148 | Conjecture 8: arithmetic terms vanish in the τ-scaling limit; c₂ = 2m³ + O(m²) | open |

**File references.** In this note, `code/X` means `computations/verification/lineC/X`. `logs/X` means `evidence/executions/20261029/lineC-random-phase/X` when that file is deposited there, and `computations/verification/lineC/data/X` for the engine and symbolic logs read by the verifiers. The independent referee engine is `computations/verification/lineC/independent_replay/`; its logs are `evidence/executions/20261029/lineC-random-phase/independent_replay/`.

**Non-claims.** This note does **not** prove BGS-TRACE-005 or BGS-BGS-001. It says nothing about the fixed kick, about band-limited (≤ 32-mode) phase ensembles, or about the fixed-τ (Heisenberg-scale) limit. Every statement is at fixed m. Theorem 1 is for odd N only.

---

## 1. Setting

* N is odd, and e_N(t) = e^{2πit/N}.
* M_N(x,y) = N^{−1/2} e_N(−8^{−1}(3x² − 2xy + 3y²)). This is the repository kernel (`computations/verification/lineC/model.py`); it is symmetric (time reversal).
* U_θ = D_θM_N, with D_θ = diag(e^{iθ_x}) and θ ∈ 𝕋^N Haar-distributed. Equivalently the θ_x are independent and uniform.
* K(x) = ∏_{j∈ℤ/m} M_N(x_j, x_{j+1}) for closed paths x ∈ (ℤ/N)^m. Then Tr U^m = Σ_x K(x) e^{iΣ_jθ_{x_j}}.
* COE reference (Haake; `code/coe.py`, checked by Monte Carlo in `logs/coe_check.log`): for 1 ≤ n ≤ N,

  E_COE|Tr U^n|² = 2n − n Σ_{k=1}^n 1/(k + (N−1)/2).

  This equals 2n − 2n²/N + 2n³/N² − (2/3)n²(4n²−1)/N³ + …, i.e. K(τ) = 2τ − τlog(1+2τ) = 2τ − 2τ² + 2τ³ − … .

**Dictionary with Theorem A.** The Theorem A closure vectors a ∈ Λ_m live in the Fourier picture of D; its phase β(a) = ½Σ_{i<j}ω(a_iv_i, a_jv_j) is the shoelace (signed-area) of the closed polygon with edges a_jS^je₂, i.e. a discrete action. In the position picture used here the paths are automatically closed, and the role of β is played by the quadratic action c·P_x, with P_x = Σ_j x_jx_{j+1} and c = 4^{−1}.
* In a full phase ensemble the phase average pairs paths with **equal occupation multisets**: positions in the position basis.
* In a band-limited ensemble it pairs **equal mode content**: Fourier labels.

Only the first case is solved here.

## 2. Theorem 1: the cat map drops out of the phase ensemble [THEOREM]

**Theorem 1.** Let N be odd, and let Δ = diag e_N(−3·8^{−1}x²), F_c(x,y) = N^{−1/2}e_N(cxy) and F = F_1 (the DFT). Let (Pf)(x) = f(2x) be the permutation operator. Then:
1. M_N = ΔF_{1/4}Δ and PF_{1/4}P^{−1} = F.
2. For every θ, D_θM_N = Δ^{−1}(ΔD_θΔ F_{1/4})Δ, and P(ΔD_θΔ)P^{−1} = D_{θ'}, with θ'_x = θ_{2x} − 2π·6·8^{−1}(2x)²/N. Hence D_θM_N is unitarily conjugate to D_{θ'}F, and θ ↦ θ' is a measure-preserving bijection of 𝕋^N.
3. Consequently, the joint law of the eigenvalues of U_θ under Haar θ equals that of the random-phase DFT ensemble D_θF.

More generally, for a metaplectic kernel N^{−1/2}γe_N(αx² + βxy + δy²) with β a unit, the law depends only on the class of β in (ℤ/N)^×/((ℤ/N)^×)². Here β = 4^{−1} is a square, which gives the plain DFT.

**Remark 1′ (the square class does matter; N = p prime).** Replacing β by νβ with ν a non-square multiplies every rank-r Gauss sum of Proposition 2 by (ν/p)^r = (−1)^r.
* Hence every half-integer power p^{−k−1/2} of E_θ|Tr U^m|² (odd r) changes sign, and every integer-order coefficient (even r) is unchanged.
* For p ≡ 3 (mod 4) the half-integer terms vanish anyway (Corollary 2′); the law is just complex-conjugated, and E|Tr U^m|² is unchanged.
* For p ≡ 1 (mod 4) the form factor does change. Example (`logs/fixes_check.log`, F3; brute force with F_c): at p = 13, m = 4, E = 14033/2197 + 8√13/2197 for the square class and 14033/2197 − 8√13/2197 for a non-square class. At p = 7 and 11 the two values coincide.
* So Theorem 6, c₂ and every integer-order coefficient are S-independent, while the p^{−5/2} coefficients of Theorem 7 (8, −72, 128(2/p), 200) are those of the square class. That is the class relevant here, because 4^{−1} is a square.
* Theorem 1 is stated for odd N only. Tanner's ensemble is defined for every N.

*Proof.*
* (1): expand 3x² − 2xy + 3y². The cross term is e_N(2·8^{−1}xy) = e_N(4^{−1}xy); the diagonal parts are Δ. Then (PF_{1/4}P^{−1})(x,y) = F_{1/4}(2x,2y) = N^{−1/2}e_N(xy).
* (2): diagonal matrices commute, so D_θΔF_{1/4}Δ = Δ^{−1}(ΔD_θΔ)F_{1/4}Δ. Conjugating a diagonal matrix by a permutation permutes its entries. The map θ ↦ θ' is a coordinate permutation followed by a translation, so it preserves Haar measure.
* (3) is immediate. The general case uses x ↦ ux to rescale β by u². ∎

*Check:* `code/verify_thm1.py`, `logs/verify_thm1.log`. For N = 5, 7, 9, 11, 13, 15, 21, 101 and 103, the matrix identities hold to ≤ 5.4e-16 and the eigenphases of D_θM_N and D_{θ'}F agree to ≤ 4.1e-15. E|Tr U⁴|² agrees for M_N and F (brute force).

*Consequence for Line C.* In the maximal phase ensemble, nothing about S survives except the square class of b (which affects only the half-integer, p ≡ 1 (mod 4) terms; Remark 1′). So no ℤ[√2]-arithmetic can appear in the encounter classification. The arithmetic that does appear is that of quadratic Gauss sums over 𝔽_p (Legendre symbols, p mod 4).

## 3. Proposition 2: exact Gauss-sum formula [PROPOSITION]

**Notation.**
* Π_m is the lattice of set partitions of the time steps ℤ/m.
* For ρ ∈ Π_m with n = |ρ| blocks, write ρ(j) for the block of j.
* For σ ∈ S_m let Q_{ρ,σ}(z) = Σ_j z_{ρ(j)}z_{ρ(j+1)} − Σ_j z_{ρ(σj)}z_{ρ(σ(j+1))}, for z ∈ (ℤ/N)^n. This is the difference of the actions of the closed walks x = ρ-pattern and y = xσ.
* Write Q = ½zᵀBz, where B is the integer symmetric "signed multigraph" matrix: +1 for each edge of x, −1 for each edge of y, and 2 on the diagonal per loop.

**Proposition 2.** For odd N, with c = 4^{−1} mod N,

  E_θ|Tr U^m|² = N^{−m} Σ_{ρ∈Π_m} W(ρ) Σ_{σ∈S_m} G_N(ρ,σ),  G_N(ρ,σ) = Σ_{z∈(ℤ/N)^{|ρ|}} e_N(c·Q_{ρ,σ}(z)),

where W(ρ) = ∏_{blocks B} w(|B|) and Σ_{n≥1} w(n)tⁿ/n! = log Σ_{n≥0} tⁿ/(n!)². The first values are w(1) = 1, w(2) = −1/2 and w(3) = 2/3.

*Proof.*
1. E_θ e^{i(Σθ_{x_j} − Σθ_{y_j})} = 1 if x and y have the same occupation multiset, and 0 otherwise. So E|Tr U^m|² = Σ_x Σ_{y∈Mult(x)} K(x)K̄(y).
2. By Theorem 1 we may take M = F_c. The diagonal Gaussians cancel because x and y have the same multiset. Hence K(x)K̄(y) = N^{−m}e_N(c(P_x − P_y)).
3. {xσ : σ ∈ S_m} = Mult(x), and each y is hit |Stab(x)| = ∏_{B∈π(x)}|B|! times, where π(x) is the coincidence partition of x. Therefore E = Σ_x |Stab x|^{−1} Σ_σ K(x)K̄(xσ).
4. Group the x by their exact coincidence partition π. Möbius inversion on Π_m gives Σ_{x:π(x)=π} g = Σ_{ρ≥π} μ(π,ρ) Σ_{x: π(x) ≥ ρ} g, and the inner sum is an unrestricted sum over z ∈ (ℤ/N)^{|ρ|}. Hence W(ρ) = Σ_{π≤ρ} μ(π,ρ)/s(π), with s(π) = ∏|B|!.
5. This factorises over the blocks of ρ, with μ(π,1̂) = (−1)^{k−1}(k−1)!. The exponential formula then gives the generating function: a block of size n carries weight 1/n!, and Σ_k (−1)^{k−1}(k−1)!u^k/k! = log(1+u). ∎

**Gauss sums (p prime).** Let r = rank of B over 𝔽_p and δ = the product of the nonzero diagonal entries after congruence-diagonalising cB/2. Then G_p = p^{n−r/2} ε_p^r (δ/p), with ε_p = 1 if p ≡ 1 (mod 4) and ε_p = i if p ≡ 3 (mod 4).

All minors of B are bounded by Hadamard's inequality: the row of block B has ℓ¹-norm ≤ 4|B| (two edge incidences per time step in x and two in y), so every minor has |det| ≤ ∏_B 4|B| ≤ ∏_B 4^{|B|} = 4^m, because 4k ≤ 4^k for k ≥ 1. (v1 stated the weaker 8^m.) Hence for p > 4^m:
* the rank and the discriminant class over 𝔽_p equal those over ℚ;
* E is the exact "symbolic" expression Σ coeff·p^{n−r/2−m} ε_p^r (D/p), with integers D, valid for all such p.

**Corollary 2′ [PROPOSITION].**
* For p ≡ 3 (mod 4), E_θ|Tr U^m|² ∈ ℚ: odd-rank terms are purely imaginary and E is real.
* For p ≡ 1 (mod 4), E ∈ ℚ(√p).
* There is no p^{−1/2} term: a symmetric zero-diagonal matrix of rank 1 over a field of characteristic ≠ 2 is zero, and deficit-0 forms have zero diagonal.

*Checks* (`code/brute.py`, `code/gauss_exact.py`, `code/verify_exact.py`, `logs/verify_exact.log`).
* **V1.** Brute force over all N^m paths with the literal M_N, against Proposition 2 evaluated both by direct z-sums (any odd N) and by mod-p diagonalisation (primes). 19 cases with N ∈ {5,7,9,11,13,15,17,19,21,23,29} and m ≤ 7, composite N included. Maximum difference 1.0e-13; |Im| ≤ 1.7e-15.
* **V2.** The symbolic large-p expansion against per-prime exact evaluation, for m = 3–7 and p ∈ {101, 103, 1009, 1013, 10007, 10009}. Maximum difference 1.8e-15.
* Exact small values (`logs/audit_fractions.log`, brute force agreement ≤ 3.6e-15): 235/49 (N=7, m=3), 631/121 (N=11, m=3), 1829/343 (N=7, m=4) and 901/169 (N=13, m=3). All are rational, as Corollary 2′ requires for p ≡ 3 mod 4 (the N = 13, m = 3 value is rational because m = 3 has no odd-rank terms).

## 4. Classification of the first non-diagonal pairs [LEMMAS]

Write H_σ for the undirected Hamiltonian cycle {σ(j)σ(j+1)} on ℤ/m and C for the standard cycle. At deficit 0 (ρ = finest, n = m), B = A_C − A_{H_σ} is the signed adjacency matrix of Γ = (C∖H) ∪ (H∖C), with signs ±. For a term (ρ,σ) of deficit d = m − |ρ| and rank r, |N^{−m}G| = p^{−d−r/2}. So the orders p⁰ and p^{−1} come only from (d,r) = (0,0), (0,2) and (1,0).

**Lemma 3 (diagonal; m ≥ 3).** (d,r) = (0,0) ⇔ H_σ = C ⇔ σ ∈ D_m, the dihedral group of order 2m. The resulting contribution is 2m. For m = 1, 2 the diagonal count is 1 and 2. (For m = 2 the figure-eight term ρ = {0,1}, deficit 1, also contributes −1/p, so E|Tr U²|² = 2 − 1/p exactly; see §8.)

**Lemma 4 (rank-2 classification at deficit 0) [LEMMA].** Let m ≥ 4, H ≠ C a Hamiltonian cycle, and suppose rank_ℚ(A_C − A_H) = 2. Then exactly one of the following holds:
* (i) H is a **2-opt** of C: remove two non-adjacent edges a₁b₁, a₂b₂ and add a₁b₂, a₂b₁ (the unique Hamiltonian reconnection, after labelling). This is segment reversal, the discrete loop reversal of Sieber–Richter / Berkolaiko–Schanz–Whitney. Then Q = (z_{a₁} − z_{a₂})(z_{b₁} − z_{b₂}).
* (ii) H is a **swap**: C with two vertices a₁, a₂ at cyclic distance ≥ 3 interchanged. Then Q = ±(z_{a₁} − z_{a₂})(z_{b₁} + z_{b₂} − z_{b₃} − z_{b₄}), where b₁, b₂ and b₃, b₄ are the C-neighbours of a₁ and a₂.

Conversely, every 2-opt and every swap has rank 2. There are m(m−3)/2 2-opt cycles and max(0, m(m−5)/2) swap cycles, all distinct. Each form is a product of two independent linear forms, so for every odd N, Σ_z e_N(cQ) = N^{n−2}Σ_{u,v}e_N(cuv) = N^{n−1}.

*Proof.*
1. **Balance.** Each vertex has deg_{C∖H} = deg_{H∖C} ∈ {0,1,2}, because both cycles are 2-regular.
2. **Forbidden induced subgraphs.** Rank is at least the rank of any principal submatrix. Signed P₄ and signed 2K₂ have det = (product of the matching edge signs)² = 1, so rank 4. A signed triangle has det = 2abc ≠ 0, so rank 3. Hence Γ has no induced P₄, no induced 2K₂ and no triangle.
3. **Structure.** No induced 2K₂ means at most one component Γ′ has edges. Γ′ is a connected P₄-free graph (a cograph), so its complement is disconnected (Seinsche). Hence V(Γ′) = V₁ ⊔ V₂ with all V₁–V₂ edges present. Triangle-freeness forces V₁ and V₂ to be independent, so Γ′ = K_{s,t}. By step 1 every vertex of Γ′ has degree 2 or 4, so s,t ∈ {2,4}.
4. **Signs.** B|_{Γ′} = [[0,X],[Xᵀ,0]] with X ∈ {±1}^{s×t}, and rank = 2 rank X, so X = uvᵀ with u, v ∈ {±1}^·. Balance gives Σu = Σv = 0.
5. **Cases.**
   * (2,2) gives (i).
   * (2,4): a₁'s C-neighbours are a₂'s H-neighbours and vice versa, and all four b's are distinct. That is (ii), and distinct b's mean cyclic distance ≥ 3.
   * (4,4): all 8 vertices of Γ′ have Γ-degree 4, so by step 1 both of their C-edges lie in C∖H ⊂ E(Γ). Hence V(Γ′) is closed under C-adjacency. Since C is a single cycle, V(Γ′) is all of ℤ/m, so m = 8 and C∖H = C. But C∖H = {a_ib_j : u_iv_j = +1} is K_{2,2} ⊔ K_{2,2}, two disjoint 4-cycles, whereas C is an 8-cycle. That is a contradiction.
6. **Counts.** Pairs of non-adjacent edges number m(m−3)/2, and each admits exactly one Hamiltonian reconnection. Pairs of vertices at cyclic distance ≥ 3 number C(m,2) − 2m = m(m−5)/2 for m ≥ 5. A 2-opt has |C∖H| = 2 and a swap |C∖H| = 4, and each is determined by Γ. ∎

*Checks.*
* `code/rank_dist.py`, `logs/rank_dist.log`: exhaustive over all Hamiltonian cycles for m = 4…9 (up to 20160 cycles). The rank-2 cycles are exactly 2-opt (|C∖H| = 2) and swap (|C∖H| = 4) cycles, with counts m(m−3)/2 and m(m−5)/2. All have discriminant class −1 (hyperbolic). Rank 1 and rank 3 never occur at deficit 0 for m ≤ 9. The referee's independent exhaustive check (`evidence/executions/20261029/lineC-random-phase/independent_replay/classify.log`) extends both statements to m ≤ 10. The absence of rank 3 is still not a general lemma; see (O1).
* Lean: `rank2_class6` and `rank2_counts6` (m = 6, all 60 cycles, all 3×3 minors).

**Lemma 5 (figure-eight; deficit 1, rank 0) [LEMMA].** Let ρ merge one pair of time steps i, k at cyclic gap g (g ∈ [1, m−1]), so W(ρ) = −1/2. The words y with Q_{ρ,σ} ≡ 0 are exactly the sequences y whose closed walk has the same edge multiset. That multiset is a figure eight: two loops through the repeated label v, with g and m−g edges. The number of such y is m·d(g)·d(m−g), where d(ℓ) = 2 if ℓ ≥ 3 and 1 otherwise. The number of σ is twice that.

*Proof.*
* For N > 2m, Q ≡ 0 (mod N) ⇔ B = 0 ⇔ equal edge multisets, because the entries of B are bounded by 2m.
* Each non-v label has degree 2, so an Eulerian circuit traverses one loop and then the other.
* As cyclic sequences there are d(g)d(m−g) of them, one per choice of loop orientations. A loop with ℓ ≤ 2 edges reads the same in both directions.
* Each cyclic sequence has exactly m rotations, because a non-trivial rotation would force every label to repeat, while the m−2 singleton labels do not.

That proves the count. ∎ (Lean `fig8_6`: m = 6, k = 1, 2, 3.)

**Interpretation.** Lemmas 3–5 are the complete list of "encounter pairs" at the first non-diagonal order.
* (a) Rank-2 Gauss pairs with no coincidence: 2-opt, i.e. one loop reversed relative to the rest, and swaps. Their phases are not equal pointwise; they cancel to +1/p only after summing over paths. This is a discrete analogue of the SR action difference ΔS = (s·u) summed over the encounter stable/unstable coordinates: here the factor is c·(z_{a₁} − z_{a₂})(z_{b₁} − z_{b₂}), and Σ_{u,v}e(cuv) = p is the exact analogue of the Fresnel integral ∫e^{isu/ℏ}dsdu = 2πℏ.
* (b) Exact-degeneracy pairs at a repeated position: figure eights. Their partition weight −1/2 is the "overcounting" correction of the diagonal approximation.

The arithmetic of these pairs is that of hyperbolic planes over 𝔽_p. Since all discriminants at this order are −1 (split), no Legendre symbol survives at p^{−1}.

## 5. Theorem 6: the τ² coefficient is exactly the COE value [THEOREM]

**Theorem 6 (exact coefficient identity).** Fix m ≥ 3 and let p > 4^m be prime. Then, exactly,

  E_θ|Tr(D_θM_p)^m|² = Σ_{k=0}^{2m−1} a_{m,k}(p) p^{−k/2},

where each a_{m,k}(p) is a finite ℚ-linear combination of the functions p ↦ ε_p^r (D/p), with r ≡ k (mod 2) and D a nonzero integer. So a_{m,k} depends on p only through p mod 4 and finitely many Legendre symbols, and a_{m,k} = 0 for k odd and p ≡ 3 (mod 4). The first three coefficients do not depend on p:

  a_{m,0} = 2m,  a_{m,1} = 0,  a_{m,2} = c₁(m) = 2m[m(m−3)/2 + max(0, m(m−5)/2)] − (m²/2)Σ_{g=1}^{m−1}d(g)d(m−g),

which gives c₁(3) = −9, c₁(4) = −24, and **c₁(m) = −2m² for all m ≥ 5**.

**Corollary 6′ (remainder).** For p > 4^m, E_θ|Tr(D_θM_p)^m|² = 2m + c₁(m)/p + R_m(p), with |R_m(p)| ≤ C_m p^{−3/2} and C_m = m!·Σ_{ρ∈Π_m}|W(ρ)|. In particular E = 2m − 2m²/p + O_m(p^{−3/2}) for m ≥ 5.
* **Caveat (the explicit bound is weak).** C_m grows super-exponentially (`logs/fixes_check.log`, F1): C_5 = 3651, C_6 = 90921, C_7 ≈ 3.1·10⁶, C_8 ≈ 1.4·10⁸, C_10 ≈ 5.3·10¹¹ and C_12 ≈ 4.4·10¹⁵. The explicit bound C_m p^{−3/2} is smaller than the main correction 2m²/p only for p > (C_m/2m²)². That is ≈ 5.3·10³ (m = 5), 1.6·10⁶ (m = 6), 9.9·10⁸ (m = 7), 1.1·10¹² (m = 8) and 2.3·10²⁶ (m = 12), far above the threshold 4^m for every m ≥ 5. For m = 3, 4 the threshold is (C_m/|c₁|)² ≈ 4.5 and 77, below 4^m. The content of Theorem 6 is therefore the **exact coefficient identity**, not the numerical size of the explicit remainder. For m ≤ 12 the true remainder coefficients are known exactly (Theorem 7).
* **Exactness at small p [COMPUTATIONAL].** p > 4^m is what the Hadamard argument gives. A direct exact comparison, prime by prime, in ℚ(ε_p√p) between the per-prime value of Proposition 2 (mod-p diagonalisation, valid for every odd prime) and the large-p expansion shows that the expansion is already exact much earlier (`code/threshold_check.py`, `logs/threshold_m*.log`):
  * m = 2, 3, 4: every prime 3 ≤ p ≤ 257;
  * m = 5: every prime 3 ≤ p ≤ 257 except p = 5, hence every prime 7 ≤ p ≤ 257;
  * m = 6: every prime 7 ≤ p ≤ 257 (it fails at p = 3, 5);
  * m = 7: every prime 7 ≤ p ≤ 257 (it fails at p = 3, 5). The referee's range p ≥ 11 excluded p = 7 a priori because 7 divides some discriminants; the direct comparison shows that p = 7 is also exact, and the brute force with the literal M_N agrees there (799247/117649; F5).
  * m = 8: every prime 19 ≤ p ≤ 257, and also p = 11. It fails at p = 3, 5, 7, 13 and 17; at 13 and 17 only the √p part differs. This is the C++ expansion `logs/engine_m8.log` against the Python per-prime value (`logs/threshold_m8.log`, about 65 s per prime).

  These are finite checks, not a proof for the primes between the checked range and 4^m.

So the form factor K(τ) = E|Tr U^m|²/p, at τ = m/p, satisfies K = 2τ − 2τ² + O_m(p^{−5/2}) for each fixed m ≥ 5. This is exactly the COE Taylor coefficient −2τ², and the fixed-m, exact-in-p counterpart of the diagrammatic n, B → ∞ result of Gnutzmann–Seif (2004) for the same ensemble.

*Proof.*
0. *Exact form.* By Proposition 2, E = p^{−m}Σ_ρW(ρ)Σ_σG_p(ρ,σ), and G_p = p^{n−r/2}ε_p^r(δ/p) with r = rank_p B. For p > 4^m, rank_p = rank_ℚ and δ may be taken to be 2^r det B_II·(square), for a nonsingular principal block B_II over ℚ with |det B_II| ≤ 4^m < p (§3). So each term equals W(ρ)·ε_p^r(D/p)·p^{−(2d+r)/2} with D a fixed nonzero integer, and grouping by k = 2d + r ≤ 2m − 1 gives the identity. (k ≤ 2m − n ≤ 2m − 1, since r ≤ n.) Odd k means odd r; these terms are purely imaginary for p ≡ 3 (mod 4) and cancel (Corollary 2′). Steps 1–4 identify a_{m,0}, a_{m,1}, a_{m,2}; at k = 2 every discriminant is −1 (§4), so no character survives.
1. By Proposition 2 and the Gauss-sum evaluation, every term with 2d + r ≥ 3 is bounded by |W(ρ)|p^{−3/2}. The number of σ is m!, which gives C_m (Corollary 6′). Rank 1 at d = 0 is impossible (Corollary 2′), so a_{m,1} = 0.
2. Order p⁰ = (0,0) = 2m (Lemma 3).
3. Order p^{−1} = (0,2) + (1,0).
   * By Lemma 4, (0,2) = (1/p)·2m·[m(m−3)/2 + m(m−5)/2] = 2m²(m−4)/p for m ≥ 5. Each undirected cycle corresponds to 2m permutations σ, and each hyperbolic sum gives exactly p^{n−1}.
   * By Lemma 5, (1,0) = −(1/2)·Σ_{pairs}2·m·d(g)d(m−g)/p. There are m unordered pairs for each value of g, with g ~ m−g, so this equals −(m²/2)Σ_{g=1}^{m−1}d(g)d(m−g)/p.
   * For m ≥ 5, the sum Σ d(g)d(m−g) = 2+2+4(m−5)+2+2 = 4m − 12. So (1,0) = (−2m³ + 6m²)/p.
   * Total: 2m³ − 8m² − 2m³ + 6m² = −2m².
4. Small m: m = 3 gives 0 − (9/2)·2 = −9, and m = 4 gives 16 − 8·5 = −24. ∎

*Checks.*
* Exact symbolic computation (§6) gives p^{−1} coefficients −9, −24, −50, −72, −98, −128, −162, −200, −242, −288 for m = 3…12.
* The (d,r) decomposition matches term by term: (0,2) = 2m²(m−4) and (1,0) = −2m³+6m² for m = 5…12 (`logs/decompose_5_7.log`, `logs/engine_m*.log`). Of the (0,2) part, the 2-opt pairs give m²(m−3) and the swaps m²(m−5). Without the swaps the coefficient would be −m³ + 3m², not −2m².
* Lean: `coeff_identity` checks the polynomial identity for 5 ≤ m ≤ 300.

**Remark (what the theorem says about "beyond Ehrenfest").**
* The classical Markov chain of the ensemble, |F(x,y)|² = 1/p, mixes in one step. Its Lyapunov exponent is effectively log p per step and its Ehrenfest-type time is O(1). So the pairs above are "post-Ehrenfest" encounters of the ensemble, at every m ≥ 5.
* The cat map's own Ehrenfest time 2log_λp is invisible in this ensemble (Theorem 1).
* The theorem is not uniform in m: C_m grows superexponentially, and the threshold 4^m grows exponentially. So it says nothing about τ = m/p fixed; see §8 for numerics there.

## 6. Exact expansion beyond τ² [THEOREM, computer-assisted; CONJECTURES]

**Algorithm** (`code/engine.cpp`, `code/run_engine.py`):
1. Enumerate the set partitions ρ up to dihedral symmetry, with exact rational weights W.
2. For each ρ, enumerate all distinct words y (multiset permutations), reduced exactly by rotation: Σ_y f = (m/s₀)Σ_{y₀=0} f.
3. Compute the rank of B mod P = 2^61 − 1. This is exact, because the Hadamard bounds are < 2^60 and the code asserts it.
4. Compute the square class of the nondegenerate part as the exact integer determinant (Bareiss) of the unimodularly transformed pivot block.
5. Combine with exact fractions.

The C++ engine reproduces the independent Python implementation exactly for m = 6, 7, 8 (`logs/symbolic_m8.log` vs `logs/engine_m8.log`). The rotation reduction reproduces the unreduced runs exactly for m = 8, 9. By §3, the expansions are valid for all primes p > 4^m. Empirically, for m ≤ 8 the only primes < 200 at which the rank or square class of some form changes are ≤ 17 (`logs/symbolic_m1_7.log`, `logs/symbolic_m8.log`). The direct exact comparison of §5 ("Exactness at small p") shows where the expansion actually holds; that is [COMPUTATIONAL]. The referee engine deposited at `computations/verification/lineC/independent_replay/` reproduces the m = 11 and m = 12 expansions through order p^{−5/2} (`evidence/executions/20261029/lineC-random-phase/independent_replay/compare_theirs.log`).

**Theorem 7 (computer-assisted).** For m ≤ 10 the complete expansions are in `logs/symbolic_m1_7.log`, `logs/engine_m8.log`, `engine_m9.log` and `engine_m10.log`. For m = 11 and 12 the expansions are exact through order p^{−5/2}: partitions of deficit ≤ 2 contribute all terms of order ≥ p^{−5/2} (`logs/engine_m11_def2.log`, `engine_m12_def2.log`). Coefficients through p^{−3} (`logs/coeff_table.md`; "n/c" = not computed):

| m | p^0 | p^-1 | p^-3/2 | p^-2 | p^-5/2 (p≡1 mod 4; 0 for p≡3) | p^-3 | COE p^-1, p^-2, p^-3 |
|---|---|---|---|---|---|---|---|
| 3 | 6 | -9 | 0 | 4 | 0 | 0 | -18, 54, -210 |
| 4 | 8 | -24 | 0 | 42 | 8 | -33 | -32, 128, -672 |
| 5 | 10 | -50 | 0 | 175 + 10·(5/p) | 0 | -400 | -50, 250, -1650 |
| 6 | 12 | -72 | 0 | 390 | -72 | -1938 + -72·(5/p) | -72, 432, -3432 |
| 7 | 14 | -98 | 0 | 686 | 0 | -5047 + -98·(5/p) + 28·(-7/p) | -98, 686, -6370 |
| 8 | 16 | -128 | 0 | 1008 | 128·(2/p) | -9600 + 64·(2/p) | -128, 1024, -10880 |
| 9 | 18 | -162 | 0 | 1512 | 0 | -17658 + 36·(-3/p) + 162·(5/p) | -162, 1458, -17442 |
| 10 | 20 | -200 | 0 | 2000 | 200 | -26000 | -200, 2000, -26600 |
| 11 | 22 | -242 | 0 | 2662 | 0 | n/c | -242, 2662, -38962 |
| 12 | 24 | -288 | 0 | 3480 | 0 | n/c | -288, 3456, -55200 |


**Observations** (all exact):
* **(O1)** No p^{−3/2} term for any m ≤ 12. It is a theorem for each such m; for general m it is an open lemma. The rank-3 forms at deficit 0 do not occur for m ≤ 9 (`rank_dist.log`).
* **(O2) τ³ term.** The p^{−2} coefficient equals the COE value 2m³ (K ∋ +2τ³, as in Berkolaiko–Schanz–Whitney 2003 for the Fourier graph) at m = 7, 10 and 11. It deviates at m = 5 (175 + 10(5/p) vs 250), m = 6 (390 vs 432), m = 8 (1008 vs 1024), m = 9 (1512 vs 1458) and m = 12 (3480 vs 3456). The deviations c₂(m) − 2m³ are −75 (+10(5/p)), −42, 0, −16, +54, 0, 0, +24 for m = 5..12.
  * They show no sign pattern. In size they are ≤ 3.4m² for m ≥ 5 (the extreme case is m = 5 with (5/p) = −1, −85; v1 said "≤ 3m²", which is wrong for that case), ≤ 0.7m² for m ≥ 8 and ≤ 2m for m ≥ 10. The ratios c₂/m³ are 1.40 ± 0.08, 1.81, 2, 1.97, 2.07, 2, 2, 2.01 for m = 5..12 (`logs/fixes_check.log`, F4).
  * **Precise sense of the deviation.** It is a statement at *fixed m*: the exact p^{−2} coefficient differs from the fixed-m COE coefficient 2m³ of E_COE|Tr U^m|² = 2m − 2m²/N + 2m³/N² − … . It is not a deviation from Gnutzmann–Seif (2004), whose result stops at O(τ³). It is not a deviation from the fixed-τ predictions either (BSW 2003; Gnutzmann–Altland 2005; Pluhař–Weidenmüller 2014). In K = E/p at τ = m/p, the deviation contributes [(c₂ − 2m³)/m²]·τ²/p, which tends to 0 at fixed τ if |c₂ − 2m³| = O(m²) for all m. So the data are **consistent with the COE in the τ-scaling limit**. That is not proved: the O(m²) size is observed only for m ≤ 12, and the expansion is not known to be uniform in m.
* **(O3) Half-integer, non-universal term.** The p^{−5/2} term is present only for p ≡ 1 (mod 4); that it vanishes for p ≡ 3 (mod 4) follows in general from the rationality corollary. The values below are for the **square class** of the cross coefficient, which holds here (4^{−1} is a square). A non-square class would flip their sign (Remark 1′). Among 3 ≤ m ≤ 12 it is nonzero **only for m = 4, 6, 8, 10**:
  * m = 4: 8; m = 6: −72; m = 8: 128·(2/p); m = 10: 200; m = 12: **0** (3024 − 6336 + 3312 = 0 in the (d,r) decomposition, `logs/engine_m12_def2.log`). So the vanishing is not governed by parity alone;
  * it vanishes exactly for m = 5, 7, 9, 11 (in the (d,r) decomposition, the three classes (0,5), (1,3), (2,1) cancel, e.g. 2178 − 4598 + 2420 = 0 at m = 11).

  Its magnitude is ≈ 2m², against 2m³ for the universal p^{−2} term. In the scaling variable τ it is therefore of relative size p^{−1/2}/m.
* **(O4) Character terms.** Legendre characters appear first at p^{−2} for m = 5, as 10·(5/p): the pentagon/pentagram pair, a sporadic small-m configuration. At p^{−3} they appear as (5/p), (2/p), (−3/p), (−7/p), with coefficients O(m²) against the universal ≈ −(8/3)m⁴. These are arithmetic in exactly the Kurlberg–Rudnick sense: they depend on the splitting of p in ℚ(√5), ℚ(√−3), ℚ(√−7), ℚ(√2) and on p mod 4.
* **(O5) τ⁴ term.** The p^{−3} coefficient does **not** equal the COE value at m ≤ 10 (e.g. −26000 vs −26600 at m = 10). Whether its leading m⁴ coefficient is −8/3 cannot be decided from m ≤ 10.

**Conjecture 8.**
* (a) c₂(m) = 2m³ + O(m²) (for m ≤ 12, |c₂ − 2m³| ≤ 3.4m²). The stronger guess c₂(m) = 2m³ for all m ≥ 10, which held through m = 11, is **refuted** by m = 12 (3480 ≠ 3456).
* (b) For each k, the trivial-character coefficient of p^{−k} is (COE leading term)·(1 + O(1/m)).
* (c) All half-integer and character terms of order p^{−k−1/2} or p^{−k} have size O(m^{k}) or smaller, hence vanish in the τ-scaling limit. In other words, the arithmetic anomalies of this ensemble are finite-N, not finite-τ.

The status is: (a) is consistent with m ≤ 12; (b) and (c) are consistent with m ≤ 12 (p^{−3}: m ≤ 10) but weakly tested.

## 7. Formalisation (summary)


**Files.**
* Source: `formalization/Bgs/LineCEncounter.lean`, namespace `Bgs.LineCEncounter`, imported by `formalization/Bgs.lean`. The finite certificates support BGS-TRACE-144, BGS-TRACE-145 and BGS-TRACE-146 only. The module uses only Lean core (no imports): computable definitions on `List`, `Nat`, `Int`, with every theorem closed `by decide`.
* **v2 rebuild.** The only change to the source is the parenthesisation `theorem hyp_counts : (hypOK 5 && hypOK 7 && hypOK 11 && hypOK 13) = true` (the v1 form parsed as `… && decide (hypOK 13 = true)`; that was harmless but misleading). The private copy `/workspace/bgs-lineC/build` had been deleted by another process, so it was re-created with `cp -a /workspace/bgs-build/formalization`. Then `lake exe cache get` ran (8689 cached files decompressed, "No files to download", `logs/fix_cache_get.log`), followed by `lake build Bgs.LineCEncounter`: "Build completed successfully", 254 s (`logs/fix_lake_build_LineC.log`). Axioms were re-checked (`logs/fix_lean_axioms_LineC.log`), with the same sets as below. The seven controls were re-run and are all rejected (`logs/fix_lean_controls.log`). Lake prints the warning "mathlib: repository … has local changes" for the copied package tree; Mathlib was not rebuilt and the module imports nothing from it.
* Build copy (v1): the source was built as module `Bgs.LineCEncounter` inside a private copy of the project, `/workspace/bgs-lineC/build`, made with `cp -a /workspace/bgs-build/formalization`.
  * `lake exe cache get` was run first: "No files to download", `logs/own_cache_get.log`. Mathlib was not rebuilt; the module imports nothing from it anyway.
  * Build command: `lake build Bgs.LineCEncounter`. Result: **success**, "Build completed successfully", 226 s (`logs/own_lake_build_LineC.log`). The axioms were re-checked in this copy (`logs/own_lean_axioms_LineC.log`).
  * An earlier identical build inside the shared tree also succeeded (399 s, `logs/lake_build_LineC.log`). That import and the module file were then removed again in the packet workspace. In this repository the module stays imported from `formalization/Bgs.lean`.
* No `sorry`, no `native_decide` (checked by grep). `set_option Elab.async false` is used to keep peak memory down; an asynchronous elaboration was OOM-killed (exit 137) on the loaded box.
* `#print axioms` (`logs/lean_axioms_LineC.log`) shows only `propext` for aut5, aut6, rank2_class6, rank2_counts6, fig8_6, exact_7_3, exact_11_3 and exact_13_3, and no axioms for ham6, msPerms_count, coeff_identity and hyp_counts.

**Theorems (all `by decide`).**

| theorem | statement (finite core) | supports |
|---|---|---|
| `aut5`, `aut6` | the number of σ ∈ S_m with H_σ = C is 2m (m = 5, 6) | Lemma 3 |
| `ham6` | there are 60 undirected Hamiltonian cycles on ℤ/6 | Lemma 4 setup |
| `rank2_class6` | for all 60 cycles at m = 6: all 3×3 minors of A_C − A_H vanish (rank ≤ 2) ⇔ H = C, or \|C∖H\| = 2 (2-opt), or H is a swap | Lemma 4 (m = 6) |
| `rank2_counts6` | among those, the counts by \|C∖H\| are 1 (C), 9 (2-opt), 3 (swap) | Lemma 4 counts |
| `msPerms_count` | the multiset-permutation enumerator gives 6!/2 = 360 words for one merged pair | Lemma 5 setup |
| `fig8_6` | the words with the same edge multiset number m·d(k)·d(m−k) for m = 6, k = 1, 2, 3 | Lemma 5 (m = 6) |
| `coeff_identity` | 2m(m(m−3)/2 + m(m−5)/2) − (m²/2)(4m−12) = −2m² for 5 ≤ m ≤ 300 | Theorem 6 arithmetic |
| `hyp_counts` | #{uv = k} in 𝔽_p² is 2p−1 (k = 0) and p−1 (k ≠ 0), for p = 5, 7, 11, 13 | hyperbolic Gauss sum = p |
| `exact_7_3`, `exact_11_3`, `exact_13_3` | the aggregated quadratic-form value counts of Prop. 2 at m = 3 certify E\|Tr U³\|² = 235/49, 631/121, 901/169 | Prop. 2 instances |

**Controls.** Seven false variants were each appended to the definitions and **rejected** by `decide` (`logs/lean_controls.log`, `lean/controls/`): aut5 = 11, ham6 = 61, coefficient −2m² + 1, hypCount 7 0 = 14, the exact_7_3 value 236·6·7, fig8Words 6 3 off by one, and countRank2 6 4 = 4.

**Scope (what Lean does *not* check).** Lean checks finite instances only. Not formalised:
* the probabilistic reduction (Theorem 1, Proposition 2);
* Gauss-sum evaluation and the Hadamard bound;
* the general-m proofs of Lemmas 4 and 5 (Lean checks m = 6);
* the C++/Python expansions of Theorem 7.

The `exact_*` theorems certify only the finite counting step, with the reduction of Proposition 2 taken on paper.

## 8. Comparison with the literature

These items were re-checked against the primary texts (the arXiv full texts are in `bgs-lineC/lit/`, and the notes with line references are in `logs/lit_check.md`) unless marked *abstract only*.

* **Tanner 2001** (J. Phys. A 34 8485, nlin/0104014). **This is our ensemble.** Tanner's unitary-stochastic ensemble is U = D₁ŨD₂ with uniform phases, and spectral functions depend only on D·Ũ with N phases. His "uniformly connected star graph" takes Ũ to be the symmetric Fourier matrix. By Theorem 1, the maximal phase ensemble of the cat map is exactly this ensemble (up to the measure-preserving relabelling of θ). Tanner observes COE statistics **numerically** (his Fig. 2). The τ-averaged standard deviation from RMT is σ(N) ≈ **(3/4)N^{−4/3}**, "the same exponent but a slightly smaller prefactor" than for binary graphs (σ ≈ N^{−4/3}); see the page crop `logs/tanner2001_p10_sigma_3over4.png`. v1 wrote (4/3), a misreading of the stacked fraction in the text extraction. He attributes the off-diagonal terms to "phase correlations imposed by unitarity" but does not compute them. Theorem 1 covers odd N only.
* **Gnutzmann–Seif 2004** (PRE 69, 056219 and 056220; arXiv nlin/0309049 and nlin/0309050; full texts in `bgs-lineC/lit/gs2004_*.txt`). **This is the same ensemble, and the τ² coefficient was derived there.**
  * Their class-AI star graph has central scattering matrix S_C = S_DFT, the symmetric B × B DFT (I, eq. (73)), peripheral S_P = diag(e^{iβ_k}) with i.i.d. uniform β_k (I, eq. (74)), and equal bond lengths. That is exactly D·DFT.
  * In II §III B they "find all diagrams that contribute to the diagonal approximation and one order beyond" and obtain **K₂(τ) = 2τ − 2τ² + O(τ³)**, "in accordance with the GOE prediction" (II, eq. (25) and the text after eq. (34)).
  * Their derivation is physics-level: B ≫ n ≫ 1, a time average over [n, n+Δn], then n, B → ∞, with an overcounting bookkeeping of sub-diagrams. They make no claim at order τ³ or at fixed n.
  * Their diagrams for the first order beyond the diagonal fall into **three families**: two obtained by joining scattering regions of the diagonal diagrams, whose net contribution vanishes by overcounting, and the Sieber–Richter family. There is no family corresponding to the **swap** pairs of Lemma 4. A swap gives an additive constraint z_{b₁} + z_{b₂} = z_{b₃} + z_{b₄}, not an index coincidence of the kind forced by their eq. (24), yet in our exact count it contributes m²(m−5)/p, the same order as the 2-opt pairs. I could not determine how, or whether, it is absorbed in their bookkeeping; I make no claim that their final result is affected.
* **Berkolaiko–Keating 1999** (J. Phys. A 32, 7827; full text in `bgs-lineC/lit/bk1999_jpa32_7827.txt`). Neumann star graphs (central matrix 2/v − δ) with incommensurate bond lengths, so effectively random bond phases on a D·Σ structure. Orbits of equal length must "traverse the same set of edges … in a different order", which is equal-multiset pairing. They evaluate the diagonal and off-diagonal contributions combinatorially, in the limit of many edges, and find a non-universal K(τ). This is prior art for the *method* (exact all-pairs combinatorics in random-phase star graphs).
* **Berkolaiko–Schanz–Whitney 2002** (PRL 88 104101). Their ensemble is a different one: the B × B bond-scattering matrix with **independent bond phases** (B = N² for the complete DFT graph, and φ_ml = φ_lm under TR). They evaluate **only** pairs differing by the orientation of one loop, and obtain −2τ² in the limit B → ∞ at fixed τ under a mixing condition. They state explicitly that they have not shown that no other correlated pairs contribute at the same order.
* **Berkolaiko–Schanz–Whitney 2003** (J. Phys. A 36 8373). Same bond-phase ensemble. They include diagrams with ≤ 2 self-intersections and ≤ 4 arcs and *argue* that the others are higher order. They obtain +2τ³ for uniformly hyperbolic TR graphs; for the fully connected Fourier graph this gives GOE agreement to O(τ³) as B → ∞.
  * **Difference to ours.** With phases on the N states (vertices) instead of the N² bonds, the average pairs only *position multisets*, not bond multisets. This lets in the extra **swap** class of Lemma 4: exchanging two time steps at distance ≥ 3 changes the bonds, so it is invisible in BSW's ensemble. Swaps are needed for the exact cancellation to −2m². Our statements are also exact at finite p for fixed m, with *all* pairs included, rather than limits at fixed τ.
  * **Fixed-m comparison of the τ³ coefficient.** c₂(m) = 2m³ holds exactly only at m = 7, 10, 11 among m ≤ 12. This does not contradict BSW, whose statement is about B → ∞ at fixed τ, in another ensemble.
* **Berkolaiko 2004** (Waves Random Media 14 S7; *abstract only*): an algorithmic treatment of TR orbit pairs to third order on general graphs.
* **Gnutzmann–Altland 2004 / 2005** (PRL 93 194101; PRE 72, 056215, arXiv nlin/0508009, full text in `bgs-lineC/lit/ga2005_nlin0508009.txt`). The bond-phase average is mapped to a supersymmetric σ-model, which gives Wigner–Dyson statistics as B → ∞ under a gap condition on the classical Perron–Frobenius operator. They list "complete DFT graphs" as meeting it, and state that star graphs with a generic central scattering matrix display universal statistics, with the Neumann star graph as a counterexample. The DFT central vertex has T = 1/B, the maximal gap.
* **Pluhař–Weidenmüller 2014** (PRL 112, 144102; arXiv:1312.2349): all GOE correlation functions, as B → ∞, for mixing, time-reversal-invariant graphs with incommensurate bond lengths. Their massive-mode step rests on a gap assumption.
* So both works predict the *full* COE form factor at fixed τ for this kind of ensemble, but not rigorously in the sense of this report. That is directly relevant to Conjecture 8 and to §8. Our results are complementary: rigorous and exact in p, but at fixed m, through the first off-diagonal order (Theorem 6) and, computer-assisted, through p^{−5/2} for m ≤ 12 (Theorem 7).
* **Project claims (BGS record).** BGS-TRACE-127 proves E|Tr U|² = 1, E|Tr U²|² = (2N−1)/N and E|Tr U³|² = (6N²−9N+4)/N² for this ensemble at every odd N. BGS-TRACE-128 and BGS-TRACE-132 prove |E|Tr U^m|² − 2mP(N,m)/N^m| ≤ m!(1+m(m−1))/N, so the fixed-m limit is 2m. BGS-TRACE-131 covers the kernel for every hyperbolic S. Theorem 6 refines BGS-TRACE-128 at prime N by giving the exact 1/p coefficient. Theorem 1's reduction to the DFT is consistent with BGS-TRACE-131's kernel κ(δx² − 2xy + αy²), κ = −(2β)^{−1}.
* **Sieber–Richter 2001; Sieber 2002.** −2τ² from loop-reversed encounter pairs in uniformly hyperbolic systems, derived semiclassically. Here the analogues are explicit:
  * the 2-opt partners play the role of the loop reversals;
  * the hyperbolic form c·uv, with Σe(cuv) = p, replaces ∫e^{isu/ℏ}du ds = 2πℏ;
  * the figure-eight degeneracies supply the overcounting correction (the BSW "exceptional orbits");
  * the swaps are the ensemble-specific extra class.
* **Müller–Heusler–Braun–Haake–Altland 2004–05.** All orders in τ from encounter combinatorics, semiclassically, at fixed τ. Our fixed-m data give c₂(m) = 2m³ + O(m²) for m ≤ 12, and exactly 2m³ at m = 7, 10, 11. They also exhibit half-integer and character terms of relative size o(1) in the τ-scaling, which a fixed-τ semiclassical expansion does not see.
* **Keating 1991.** |Tr M^m|² = #ker(S^m − I): the unperturbed cat map is non-generic. Theorem 1 shows that full phase randomisation erases it completely; nothing intermediate is proved here.
* **Kurlberg–Rudnick 2000.** Hecke symmetries make the cat map non-universal through the arithmetic of the splitting of primes. Our (O3)–(O4) terms are arithmetic of the same type (p mod 4, (5/p), (2/p), (−3/p), (−7/p)), but at fixed m they are subleading. So there is **no Kurlberg–Rudnick-type anomaly at order τ²**.
  * The p^{−5/2} coefficients are exact computer-assisted values for each m ≤ 12, nonzero only for m = 4, 6, 8, 10.
  * Their vanishing for p ≡ 3 mod 4 is proved in general.
* **Gutkin–Osipov 2013** (Nonlinearity 26 177; J. Stat. Phys. 2013, arXiv:1305.0059; **unverified beyond abstracts and an ar5iv excerpt**; the referee could not confirm the description either). They study clusters of periodic orbits of the baker map / de Bruijn graphs: pairs of orbits sharing all length-p subwords, with cluster-size statistics expressed through a truncated-unitary form factor with random diagonal phases. This is the closest combinatorial analogue of "pairs with equal occupation multisets", but for symbolic dynamics with an ultrametric closeness. It contains neither the DFT/cat-map ensemble nor Gauss sums, and has no counterpart of Lemma 4.

## 9. What is new (to the best of a limited literature search; not a guarantee)

1. **Theorem 1.** The maximal phase ensemble of the quantized cat map (odd N) is exactly Tanner's DFT star-graph unitary-stochastic ensemble, i.e. the Gnutzmann–Seif class-AI star graph. All S-dependence disappears except the square class of b, which affects only the half-integer terms for p ≡ 1 (mod 4) (Remark 1′). The identification itself is elementary; its novelty is only that it connects the cat-map project to this ensemble.
2. **Proposition 2.** An exact finite Gauss-sum/partition-lattice formula for E|Tr U^m|² in this ensemble, with weight series log Σtⁿ/(n!)². Corollary: the value is rational for p ≡ 3 mod 4 and lies in ℚ(√p) otherwise.
3. **Lemma 4.** The rank-2 classification of differences of two closed-walk forms: 2-opt and swaps only. The swap class is specific to vertex-phase (as opposed to bond-phase) averaging, and it is not among the diagram families of Gnutzmann–Seif (2004).
4. **Theorem 6.** For the random-phase DFT (Tanner / Gnutzmann–Seif star-graph) ensemble, this is the first rigorous derivation of the first off-diagonal coefficient. It is an exact coefficient identity, exact in p for each fixed m ≥ 5 (p > 4^m), with a complete classification of the contributing pairs (2-opt, swap, figure-eight), including the swap class absent from the Gnutzmann–Seif diagram scheme.
   * It confirms the COE value −2m², previously obtained diagrammatically in the limit n, B → ∞ by Gnutzmann–Seif (2004) for this very ensemble, and predicted by the σ-model (Gnutzmann–Altland 2005; Pluhař–Weidenmüller 2014).
   * The τ² coefficient itself is therefore **not** new. What is new is the rigour, the exactness in p at fixed m, and the completeness of the classification. The equal-multiset pairing goes back to Berkolaiko–Keating (1999).
5. **Theorem 7 and (O1)–(O5).** Exact expansions:
   * to all orders for m ≤ 10, and through p^{−5/2} for m = 11, 12;
   * c₂(m) = 2m³ only at m = 7, 10, 11;
   * a half-integer p^{−5/2} term for p ≡ 1 mod 4 at m = 4, 6, 8, 10;
   * quadratic-character terms at p^{−2} (m = 5) and p^{−3}.

   These are explicit arithmetic, non-universal finite-N corrections. In particular the p^{−2} (order-τ³) coefficient deviates from the fixed-m COE value 2m³ at m = 5, 6, 8, 9 and 12 (e.g. c₂(12) = 3480 vs 3456). This is a fixed-m statement, consistent with the COE in the τ-scaling limit as far as the data go (§6 (O2)). The p^{−5/2} values are for the square class (Remark 1′).
6. Kernel-checked finite certificates (Lean 4, `decide`, no sorry and no native_decide).

## 10. Scope and non-claims (repeated)

* The ensemble is the maximal Haar diagonal-phase ensemble. Nothing is claimed for the fixed kick (τ = 10⁻⁸⁰), the 16-mode ensemble of BGS-TRACE-126, or band-limited ensembles. The beyond-Ehrenfest ℤ[√2]-norm classification for those remains open (`bgs-lineC/REPORT.md` §7).
* All theorems are fixed-m statements. Theorem 6 is not uniform in m (threshold 4^m; C_m super-exponential), and nothing is proved at fixed τ = m/p. The Monte Carlo of `bgs-lineC/REPORT.md` §8 is a diagnostic only.
* The explicit remainder of Corollary 6′ is non-informative for p < (C_m/2m²)².
* The small-p exactness ranges are finite computations.
* BGS-TRACE-005 and BGS-BGS-001 remain open.
