# Why the order-unit norm does not give H1-bad at C ≤ 8.8×10^{-4}

Status: **[P]** as a comparison of two explicit constants. H1-bad is not proved at this constant, and this note does not claim that it fails.

## The budget

H1-bad at ρ = 0.28 asks for

S_2(j) = Σ_{bad, shell j} |r_A r_B|^2 ≤ C · 2^{j(1−β)}, C = 8.8×10^{-4},

for every j > 12. The number of fundamental-domain classes in shell j is at most 2^j (the census gives about 0.62·2^j; the cruder bound is enough). A uniform per-class bound |r_A r_B|^2 ≤ P · ρ^{θ j}, with θ = log_ε 2, produces

S_2(j) ≤ 2^j · P · ρ^{θ j} = P · 2^{j(1−β)},

because 2^{−β j} = ρ^{θ j}. The shell inequality holds for every j as soon as P ≤ C.

## The order-unit prefactor

N14 §2.4 records the generic CP conversion, one window at a time,

(ψ Y_c ψ)(Φ Y_c^{−1} Φ) = 1.53 × 2.22 = 3.3966.

Those two figures are the project’s stated constants, not recomputed here. The joint second moment is a product of two windows, so the generic prefactor is

P_gen = (1.53 × 2.22)^2 = 11.5369.

Then P_gen / C = 1.311×10^4. The same ratio against the wider constant 0.082 is 141.

Doubling both input constants multiplies P_gen by 16 and widens the gap. Halving both divides P_gen by 16 and leaves P_gen / C > 800. No reading of those two-digit figures at the factor-of-two level puts P_gen under 8.8×10^{-4}, or under 0.082.

## What a phase-keeping proof has to beat

The order-unit bound uses 𝒦, the averaged operator, with ρ(𝒦) ≤ 0.28. It does not see the phases that make the measured shells small. Thm A has C_cert ≤ 4.36×10^{-4} through j = 14, which is below 8.8×10^{-4} and about 3×10^4 below P_gen. That improvement is certified only for those shells.

A tail proof at C = 8.8×10^{-4} has to keep the phases on the joint collision system: 6145 carry pairs, Fourier differences |u| ≤ 60, and, by the alphabet theorem, digits in {−1, 0, 1} with no 4 consecutive zeros. Remembering the number of trailing zeros takes 4 states, so the restricted graph has 6145 × 4 = 24 580 vertices. The edge operators are the sesquilinear blocks T_u on the core space. N15 already found that the single-window version, 961 carries and one core matrix per state, was about 3.7 GB per iterate and was not run. The joint blocks are the tensor product of two such matrices. They are not a computation on this machine, and no estimate in this note replaces them.

The digit alphabet {−1, 0, 1} does not reduce the 6145. Those states index Fourier carries, not the digits E_k.

## The rate that would close it

Suppose a phase-keeping bound supplied |r_A r_B|^2 ≤ P ρ^{θ j} with the same ρ = 0.28. The shell sum would lie under C · 2^{j(1−β)} for every j once P ≤ 8.8×10^{-4}. Relative to P_gen this is a prefactor improvement by at least 1.3×10^4. The finite shells show that an improvement of that size is compatible with the core functional through j = 14. They do not produce it for j > 14.

N15’s single-window carry scan is the closest numerical probe. The rate stayed ρ(𝒦) for carry boxes E ≤ 4, while the reciprocal Perron share grew roughly linearly, about +2 per unit E. That scan is [N], it is not the joint system, and a linear extrapolation to |e| ≤ 51 is not a bound. It does show that enlarging the carry box has so far increased the prefactor, which is the wrong direction for a constant as tight as 8.8×10^{-4}.
