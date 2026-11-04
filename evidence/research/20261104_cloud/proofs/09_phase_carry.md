# Phase-keeping carry boxes through E = 10

Status: the runs are **[N]**. They reproduce the published E = 1, 2, 4 rates to the printed digits, and they extend the box. They do not enclose the spectral radius in an interval, and they do not close H1-bad.

## What was iterated

The single-window collision step of N14/N15,

(TY)_(e, a) = Σ_e T_v(Y_(a, b)), v = e − 6a + b, |v| ≤ 60,

on the box |e| ≤ E. Here T_v(Y) = Σ_n N_n Y N_(n−v)^*, and N_n = w_4(n) M_n / s, with M_n the sector-4 core Galerkin block. The blocks were rebuilt in binary64 from that formula (K = 55, nine cores, dimension 495, 61 modes, |s| = 1.915473204). The mass is the sum of Frobenius norms, as in `g_carry.py`.

This keeps the phases inside the blocks. It is not the 24 580-vertex norm majorant. The state is one 495×495 matrix per carry pair. At E = 10 that is 441 matrices, about 4.4 GB resident. The joint ε-system and the full |e| ≤ 51 box were not stored.

Low rank does not remove the cost. The first image of ΦΦ* under T_v already has rank up to the number of modes, and the second image fills the 495-dimensional space. A Kronecker form is the same map written on vec(Y). Neither reduction was available, so the iteration is the dense one, matrix-free only in the sense that N_n is applied through its 477 core blocks rather than as a dense 495×495 factor.

The letters u ∈ {−1, 0, +1} being acyclic does not remove the blocks either. Every carry step with |v| ≥ 2, which the box produces as soon as E ≥ 1, is a heavy letter. The iteration already phases those letters. Restricting the norm majorant to the acyclic letters and phasing the rest is this same computation.

## Rates

| E | final rate | (0,0) share | 1/share | max of P_n(0.28) |
|---|---|---|---|---|
| 0 | 0.272551040 | 1 | 1 | 1.626 |
| 1 | 0.272551351 | 0.234914 | 4.2569 | 6.927 |
| 2 | 0.272551034 | 0.150259 | 6.6552 | 10.833 |
| 4 | 0.272551031 | 0.093055 | 10.7463 | 17.507 |
| 6 | 0.272551028 | 0.064879 | 15.4134 | 25.140 |
| 8 | 0.272551024 | 0.051891 | 19.2713 | 31.455 |
| 10 | 0.272545687 | 0.044470 | 22.4873 | 36.725 |

P_n(0.28) = (∏_{i<n} rate_i) / (0.28)^n. It peaks at n = 3 for every box and then falls, because the locked rate is strictly below 0.28. For each of these boxes the growth therefore satisfies a bound of the shape mass_n ≤ P_*(E) (0.28)^n, with P_* the maximum in the last column. That prefactor is finite. It is a property of the truncated box, read off the computed orbit of ΦΦ*, not an operator-norm certificate.

The published runs match. E = 1 begins 0.91621332, 0.57423827, 0.28900260, against 0.916213316, 0.574238274, 0.289002598 in `g_carry_E1.json`. E = 4 begins 2.13350946, 0.62359194, 0.28886709, against the same digits in `g_carry_E4.json`. The locked rate 0.272551 is their ρ(𝒦) power iterate. The gap to 0.28 is 7.449×10^{-3}. The digit-for-digit match on the old boxes puts that gap far above a rebuild or rounding artefact.

E = 10 was stopped after six steps. Its last rate, 0.2725457, is still climbing toward the same lock and is already within 6×10^{-6} of it. The share has settled. Resident memory at E = 10 was 4.4 GB. E = 12 was not started.

## The prefactor has not saturated

Forward differences of 1/share, per unit of E:

| interval | slope |
|---|---|
| 1 → 2 | 2.398 |
| 2 → 4 | 2.046 |
| 4 → 6 | 2.334 |
| 6 → 8 | 1.929 |
| 8 → 10 | 1.608 |

N15’s picture through E = 4 was a slope near +2. The slope is still positive at E = 10, and it has come down: 2.33, then 1.93, then 1.61. That is a slowing, not a level. The E = 4 value 1/share = 10.75 is not the limit. At E = 10 it is 22.49.

The same statement holds for P_*(0.28): 17.51 at E = 4, 31.45 at E = 8, 36.73 at E = 10.

## What is not claimed

The sharp lambda-carry box is |e| ≤ 14, and the ε-carry box is |e| ≤ 51. Neither was iterated. A norm-majorant bound on the omitted carries is useless: that majorant has spectral radius hundreds, so it cannot promote these runs into a rate certificate for the untruncated operator.

The (0,0) share is the proxy N15 already refused to call the shell prefactor. Multiplying the certified shell constant 4.36×10^{-4} by 1/share(E) is not a theorem. Done anyway as a scale check, 4.36×10^{-4} × 19.27 is about 8.4×10^{-3}, above 8.8×10^{-4} and below 0.082. That arithmetic does not obstruct H1 and does not prove it.

H1-bad at C ≤ 8.8×10^{-4} stays open. On every box through E = 8 the phased rate locks at 0.272551, below 0.28. At E = 10, after six steps, it is 0.272546 and still approaching that lock. The prefactor at rate 0.28 is finite on each of these boxes and is still growing at E = 10.
