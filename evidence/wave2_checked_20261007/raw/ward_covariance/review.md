# Independent focused audit: Fourier-weighted phase coherence covariance

## Claim and verdict

**Primary verdict: proved as written.** This verdict concerns the new finite-unitary inequalities, their centered covariance corollaries, the complete signed Ward action for the tests |p_m|² on the stated slow upper-half window, and the actual-model transpose-product/degree-two corollary. It uses the maintained accepted fixed-map parametrix, flatness, position mixing, and reverse-decay inputs. It is not a fresh audit of the entire inherited parametrix or repository, and does not establish the absorbed Ward obligation (13), a Heisenberg window, microscopic CUE identification, or the deterministic offcharge hierarchy.

The audited authoritative candidate is `input/weighted_coherence.md`, 18,437 UTF-8 bytes, SHA256 `5b0de64a25485a305558e852deaabad705487deedd1db014a4f685f3638ec800`. It was obtained by the authorized administrative export from Work thread `01a114a6-3438-70d0-9d5f-88c63cc000d2`, turn `01a114c8-c31b-7671-8cdd-a6f7878c18db`. Both supported Library transfers failed with HTTP 403; the ZIP was not downloaded or independently hash-checked. Library metadata confirmed the resolved archive identity and 30,038-byte size. The export was complete and its provided proof byte count/hash were independently reproduced. The original verifier, receipts, and source-pins file inside the ZIP were not accessible and were not replayed.

### Normalized claim card

For a finite unitary U, uniform independent diagonal D, V=DU, P=|U|², J=11ᵀ/N, Q_ab=U_ab conjugate(U_ba), max P≤C/N, and r=||Q||, the candidate proves

e_m=m![C^(m−1)r+C^(m−1/2)N^(−1/2)+m(m−1)C^m/N],

||S_m−L_m||≤e_m/N for m≥2, where S_m=E[d_m d_m*], d_m(a)=(V^m)_aa, and L_m=Σ_(u=0)^(m−1) P^u ∘ (P^(m−u))ᵀ. For m=1 the separately stated exact diagonal covariance holds. No restriction m≤N is silently imposed.

Under ||P−J||≤ρ<1, with Π=I−J, R=(I−P+J)^(−1), H=R+Rᵀ−I, and c_m=(I−P)d_m, this implies

||NΠS_mΠ−ΠHΠ||≤e_m+k_m,

||NE[c_m c_m*]−(I−PPᵀ)||≤(1+ρ)²(e_m+k_m),

k_m=m(C−1)ρ^(m−2)+2ρ^m/(1−ρ).

For m≥3, the whole averaged overlap-error operator from the accepted phase Ward identity satisfies

|E R_(G−G_H)|p_m|²|≤m²(C−1)ρ^(m−2)+m(1+m/N)e_m.

For the unchanged odd-N actual family at literal fixed τ=10^(−80), eventually C=5, ρ=1/2, r_N→0. The specified T_N→∞ and all three errors tend uniformly to zero for ceil(T_N/2)≤m≤T_N. The asserted convergence is on this upper-half window. It is not convergence at every fixed m, nor uniform convergence over the prefix 1≤m≤T_N.

The additional actual-model matrix B_ab=U_ab U_ba satisfies ||B||=O_τ(sqrt(log(2N)/N)), which gives E[p_1² conjugate(p_2)]=O_τ(sqrt(log(2N)/N)). This is a precise mixed-moment family, not an all-fixed-degree CUE theorem.

## Dependency graph

1. Literal phase occupation averaging → distinct-coordinate permutation expansion.
2. Directed-cycle classification + unitarity / ||Q|| + entrywise flatness → noncyclic permutation bounds.
3. Two explicit collision removals → full covariance and trace/mixed-trace inequalities.
4. Stochastic centering + singular gap → Green–Kubo leading covariance and coherence transform.
5. Accepted phase stationarity + exact normalized CUE polynomial generator → complete signed Ward action.
6. Eventual actual C,ρ and reverse decay → slow growing-window convergence.
7. Accepted raw branch expansion + actual-time C² phase bound → unconjugated transpose-product norm.
8. Exact degree-two occupation identity + branch norm → actual exceptional mixed-moment decay.

Leaves 1–5 and the window arithmetic are directly audited internal algebra. Leaves 6–7 use the maintained accepted actual-model sources, whose relevant definitions, normalizations, and quantitative statements were read. No new external-source theorem is load-bearing in this candidate. There is no circular dependence on Ward (13).

## Obligation matrix

| Obligation | Status | Finding |
|---|---|---|
| Literal operator, phase law, odd-N/fixed-τ scope | Passed | Same raw quantization and accepted phase law; no rescaled coupling or changed family enters the actual proof. |
| Conjugations and covariance orientation | Passed | Z_m=h*d_m, hence S_m=E[d_m d_m*]. Selected reversed edge uses Q or its conjugate; selected single edge uses U or its conjugate. Both preserve the stated norm. B is separately unconjugated. |
| Full occupation average and repeated coordinates | Passed | Each exact repeated-occupation contribution is dominated by its permutation expansion; overcounting is absorbed by the first collision removal. The second removal extends distinct permutations to unrestricted sums. |
| Weighted collision bound | Passed | If marks coincide/are identified, use Σ|h|²; otherwise Σ|h_a h_b|≤||h||₁²≤N||h||². This gives N^(m−2)||h||² for each equality. |
| Cyclic reference L_m | Passed | Rotation u gives (P^u)_ab(P^(m−u))_ba. u=0 is diagonal(P^m), not J or P^m. Rotation pairing gives real symmetry. Grouping cyclic roots gives positivity even for periodic paths. |
| Unmatched-edge selection | Passed | Nonrotation implies a missing directed edge. For coincident formal marks it can be selected away from that vertex; preservation of the chain on the remaining vertices would force the whole cycle. |
| Endpoint/weight placements and degree loss | Passed | Each of zero, one, two distinct endpoint marks or one coincident off-edge mark yields N^(m−2)||h||² after contraction. Remaining factors give q^(m−1) for Q and q^(m−1/2) for U. |
| Two-cycle mixed trace boundary | Passed | m≥3 permits the same single-cycle missing-edge argument even when one positive trace is a loop. m=2 does not; it is separately corrected. |
| Centering and Green–Kubo term | Passed | Π removes the J/N term only. H remains nontrivial; replacing it with I would be unjustified. |
| Coherence transform and transpose | Passed | (I−P)Π=(I−P), c_m=(I−P)d_m exactly, and (I−P)(R+Rᵀ−I)(I−Pᵀ)=I−PPᵀ on the full space. |
| Signed Ward normalization | Passed | Raw Hessian and cotangent diagonal terms cancel; the prefactor N/(N+1), m² product cross term, and m/N splitting term are correct. |
| Trace bound for nonnormal P | Passed | |Tr(P−J)^m|≤||P−J||_HS²||P−J||^(m−2)≤(C−1)ρ^(m−2), using ordinary unnormalized HS. |
| Slow window | Passed | Equation (16) gives e_m≤2/T_N⁴ for m≤T_N; the lower endpoint forces k_m and the classical Ward remainder to zero. Every fixed T is eventually feasible. |
| Actual B phase curvature | Passed | Each initial S_r,xy=1/4, so the sum phase has initial mixed derivative 1/2. The stated actual-time Taylor bound keeps it in [1/3,2/3]. |
| Sampling aliases and normalization | Passed | For row separation d≤1, increments lie in [d/3,2d/3]; distance to every integer is ≥d/3. Summation by parts gives TT* entries O(1/N) and O(1/(N|i−i'|)); Schur gives squared norm O(log N/N). |
| Actual m=2 subtraction and bilinear norm | Passed | The full exact expression retains the diagonal subtraction. |vᵀ conjugate(B)v|≤||v||²||B|| applies to complex v. |
| Original 30 covariance/check receipts | Not addressed | Their source files were unavailable after transfer failure; they are not needed as proof premises and their execution provenance is not certified here. |
| Absorbed Poisson/Ward (13), microscopic pair law | Out of scope | Infinite-degree Poisson test remains unestimated. |

## Decisive derivations

### Complete Ward action, independently reconstructed

For W_rs=Σ_(j,k)G_jk λ_j^r λ_k^s=Σ_a(V^r)_aa(V^s)_aa, the Haar reference is W_rs^H=(p_r p_s+p_(r+s))/(N+1). Let C_rs=W_rs−W_rs^H. For positive m,n, the raw eigenangle Hessian/cotangent formula reduces exactly to

R_E(p_m p_(−n))=−(m/2)p_(−n)Σ_(u=1)^(m−1) C_(u,m−u)−(n/2)p_m Σ_(u=1)^(n−1) C_(−u,−n+u)+mn C_(m,−n).

In this reconstruction the terms Σ_j E_jj λ_j^m from the Hessian cancel their drift counterparts; no IPR term or endpoint remains. For m=n, stationarity and the normalized CUE generator give candidate equation (14) exactly. For m≠n the averaged expression vanishes by the common phase symmetry; no additional off-diagonal Fourier-degree covariance hypothesis is implied.

### Short cycle, including the prior failed version

At m=2, direct exact occupation averaging gives

E[p_1² conjugate(p_2)]=2Σ_(a,b)U_aa U_bb conjugate(U_ab U_ba)−Σ_a|U_aa|⁴.

The missing-edge proof cannot be used here because the two-vertex cycle contains both directed edges between the chosen endpoints. The candidate correctly retracts the generic m=2 version of (5). Separately, the spatial covariance at m=2 satisfies exactly S_2=L_2−diag(P_aa²), so the core covariance estimate does not inherit that mixed-trace defect.

The skew-Hermitian Fourier control in Section 7 indeed has P=J, r=N^(−1/2), B=J, and p_2=p_1², yielding the nonvanishing moment 2−1/N. The candidate's Section 8 excludes that mechanism only for the unchanged actual operator through its new phase-curvature input.

### Window constants

For m≤T, equation (16) bounds the first two terms of e_m jointly by T^(−4). The collision term is at most T^(−4) because m²/√N≤T²/√N≤1 and r_N+N^(−1/2)≥N^(−1/2). Thus e_m≤2T^(−4). On m≥ceil(T/2), k_m=(16m+4)2^(−m)→0 and m²4·2^(−m+2)→0; the other Ward error is O(T^(−3)). The factor N^(−1/2) in (16) also forces T=O(log N/log log N). Reverse decay has no supplied effective rate and may make T substantially smaller.

## Computation and source checks

Fresh checks are in `checks/independent_covariance_check.py` and `checks/independent_permutation_check.py`; outputs are the two JSON result files beside them.

Commands:

    python3 checks/independent_covariance_check.py > checks/independent_results.json
    python3 checks/independent_permutation_check.py > checks/permutation_results.json

The covariance check independently enumerates closed paths, groups exact phase occupations, and constructs full exact Gaussian-rational covariance matrices for two rational complex unitary families at N=3,4, m=1,…,6, including m>N. Hermitian symmetry, the m=1 equality, the m=2 diagonal subtraction, and the exceptional mixed-moment formula are exact assertions. Operator norms and quantitative inequalities are numerical assertions, clearly labeled. The check additionally evaluates six raw Hessian/cotangent Ward expressions over exact rational eigenbasis/eigenvalue data and compares them to the reduced complete signed expression exactly.

The permutation check exhaustively covers all 46,197 nonrotation covariance permutations for m=3,…,8, including all 5,906 coincident-mark cases, and 34,404 two-cycle split/permutation cases for m=3,…,7, including 11,820 loop-boundary cases. This independently reproduces the mathematical scope behind the author's 46,197 number; it does not authenticate the author's original run. The finite coverage supports the combinatorics, while the universal theorem rests on the explicit argument.

Canonical repository read-only pin: `129c676b8e6457e7e5f1bd6f786b3939cbd84653`; no repository changes were made. The parent identified the candidate's 3930 snapshot as mathematics-byte-equivalent. Its unavailable source-pins file was not independently compared here. Relevant canonical source hashes:

- phase_ward_identity.md: `1fccba816add7065c611edf21164bbef36fa4bad9edf6e30bb39ff9b8d737479`
- position_chain_mixing.md: `3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09`
- actual_body_coercivity_constants.md: `23566b86660c089b6005f0165d4a4dee2d0528e7c7e99ee34a831ff475182ae8`
- reversed_path_decay.md: `c8fea232fdc36fed8d0c8ce9975025050179fca1f3d67e6ddf4d5fb4515ded47`
- four_branch_parametrix.md: `c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7`

## Remaining gap and strongest safe statement

No missing implication was found in the candidate's stated theorem. Its slow-window coherence and signed Ward conclusions can be accepted at their precise scope, together with the actual B-kernel/degree-two corollary. They retain the nontrivial classical spatial leading term, arbitrary spatial weights, repeated occupations, and full signed Hessian-plus-cotangent action.

The next mathematical implication remains exactly the candidate's stated boundary: estimate the complete signed contractions selected by the absorbed Poisson solution, including degrees Θ(N), larger degrees, and mixed terms. Factorial e_m cannot supply it. Applying the low-degree bounds term by term to the Poisson expansion would be invalid. The cheapest remaining administrative check is obtaining the original verifier and source-pins/receipt files for provenance replay; it would not close that analytic gap.
