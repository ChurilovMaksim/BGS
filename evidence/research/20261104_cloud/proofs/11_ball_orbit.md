# Ball bounds on the phased lambda-carry orbit

Status: **[CA]** for every box in the table below, on the computed prefix of the orbit. **[N]** is not used for those prefixes. Boxes this process has not finished are not in the table. The identification of the sharp box with the full bounded carry is **[P]**, proved in `10_green_tail.md`. H1 is not closed.

## The map that is enclosed

The single-window step is

(TY)_(e, a) = Σ_b T_v(Y_(a, b)), v = e − 6a + b, |v| ≤ 60, |e|, |a|, |b| ≤ E,

with T_v(Y) = Σ_n N_n Y N_(n−v)^* and N_n = w_4(n) M_n / s. The blocks M_n are the sector-4 core Galerkin blocks at K = 55, nine cores, dimension 495, 61 modes, disk radius 1.2, η = 2, kick 1.8. The same formulae as `phase_carry.py`. The mass is the sum of Frobenius norms.

The scalar s is the Rayleigh quotient ψ\* A(0) φ / ψ\* φ of the computed unit vectors. Its enclosure has radius 7.64×10^{-13} about a midpoint of modulus 1.9154732041332574. The float Rayleigh used by the binary64 rebuild, modulus 1.9154732041332583, lies in that disk. This is not a separate enclosure of the exact eigenvalue of A(0). Dividing the blocks by the whole disk means every rate below is valid for every normalisation inside the disk, including that Rayleigh quotient.

One block midpoint was compared with the binary64 rebuild: the largest entrywise gap on the sampled mode was 8.8×10^{-17}. The E = 1 orbit opens at 0.9162133165, the published `g_carry` digits.

## Disk arithmetic

Each block entry is built in a flint ball at precision 80 and stored as a complex128 midpoint plus a float64 radius. The disk contains the flint rectangle and the rounding of the midpoint. Products use

mid = fl(AB),

rad = (1+θ) (|A|β + α|B| + αβ + γ |A||B|),

with θ = 10^{-8} and γ = 16 K u / (1 − 16 K u) = 9.77×10^{-14}, K = 55, u = 2^{-53}. Sums add radii and add one unit roundoff times the new magnitude. The factor θ covers downward rounding in the three nonnegative matrix products that build the radius.

The Frobenius norm of every matrix inside the disks lies between

sqrt(Σ max(0, |m|−r)^2) and sqrt(Σ (|m|+r)^2).

The rate interval of a step is [mass_lo(TY) / mass_hi(Y), mass_hi(TY) / mass_lo(Y)]. After the step the collection is scaled by the midpoint of the output-mass interval, and the disks are widened so that they contain division by every mass inside the interval. States are discarded as soon as they have been applied, so only one generation is live.

## Prefix prefactor

Let rate_i ∈ [ℓ_i, h_i] be the enclosed growth of step i, and let

P_n = (∏_{i<n} h_i) / (0.28)^n.

On the certified prefix, the unnormalized mass of the orbit satisfies μ_n ≤ P_n (0.28)^n, hence μ_n ≤ P_* (0.28)^n with P_* = max_{n≤N} P_n. Early steps sit above 0.28. The product still peaks at n = 3 and then falls, on every box computed so far, because the later upper endpoints lie below 0.28.

This bounds the computed prefix. It does not by itself bound step N+1. On these boxes the disk width grows by a factor of about 7 to 11 per step, which is the wrapping of the entrywise arithmetic. The true orbit is much stabler than that factor: the same runs reproduce the binary64 lock 0.27255. The wrapping is what exhausts the gap to 0.28 after roughly ten steps. A bound for every n would be a bound on the spectral radius, and this note does not claim one.

## Certified prefixes

P_* is the maximum of the upper envelope. “Last rate” is the last computed step. Every last upper endpoint below is strictly less than 0.28, and so is every upper endpoint from step 3 onward.

| E | steps | last rate interval | (0,0) share interval | P_* | rel. width at the end |
|---|---|---|---|---|---|
| 0 | 8 | [0.272549775, 0.272552304] | 1, up to 1.0×10^{-5} | 1.62610257 | 6.61×10^{-6} |
| 1 | 8 | [0.272542088, 0.272559982] | [0.234898, 0.234930] | 6.92654067 | 5.04×10^{-5} |
| 2 | 8 | [0.272539508, 0.272562561] | [0.150246, 0.150272] | 10.8328510 | 6.55×10^{-5} |
| 3 | 8 | [0.272538158, 0.272563909] | [0.115400, 0.115422] | 14.1082483 | 7.35×10^{-5} |
| 4 | 8 | [0.272537442, 0.272564622] | [0.093046, 0.093065] | 17.5072948 | 7.77×10^{-5} |
| 5 | 6 | [0.272549139, 0.272549383] | [0.076570175, 0.076570317] | 21.2895613 | 6.97×10^{-7} |
| 6 | 6 | [0.272548446, 0.272548690] | [0.064878635, 0.064878755] | 25.1398208 | 6.99×10^{-7} |
| 7 | 6 | [0.272547777, 0.272548024] | [0.057064060, 0.057064167] | 28.5948449 | 7.08×10^{-7} |

E = 1 opens 0.9162133165, 0.5742382743, 0.2890025980, then steps below 0.28. That is the published prefix. The upper envelope of P_n is 3.272, 6.711, 6.927, 6.766, 6.587, 6.411, 6.241, 6.075. The maximum is the third term.

E = 2 opens 1.3640659991, the published first digit string, and its upper envelope peaks at 10.8328510, again at the third step. The binary64 prefactor in `09_phase_carry.md` was 10.833. The disk run reproduces it from above.

E = 3 opens 1.7315921782 and 0.6184123690. There is no published E = 3 log to match. The upper envelope peaks at 14.1082483, still at the third step, and the last rate interval lies strictly below 0.28. The relative disk width at the end is 7.35×10^{-5}. The same factor, about 10 per step, appears on every box so far.

E = 4 opens 2.1335094588, 0.6235919423, 0.2888670933. Those are the published `g_carry_E4` digits. The upper envelope peaks at 17.5072948, the binary64 value 17.507 read from above. The (0,0) share at step 5 is 0.093055, the same digits as the binary64 run. The last disk is the widest of the eight, and it still lies below 0.28.

E = 5 was stopped at six steps, before the wrapping had widened the disk. The last rate interval has width 2.4×10^{-7}. The prefix prefactor is 21.2895613. The first step is 2.5730702482. Six steps are enough for the peak, which is still the third step on every box.

E = 6 opens at 2.9887379853. The prefix prefactor is 25.1398208, against the binary64 value 25.140. The (0,0) share is 0.0648786, against the binary64 0.064879. The last rate interval has width 2.4×10^{-7} and lies under 0.27255.

E = 7 opens at 3.3389468083. The prefix prefactor is 28.5948449. The last rate interval has width 2.5×10^{-7}. The prefactor is still rising, by about 3.5 per unit of E over the last several boxes. That rise is the mass leaving (0,0). It is not a rise in the rate.

E = 0 and E = 1 were run with the same disk rules. The generation-popping change used for the later boxes does not alter the arithmetic.

## The full carry

By `10_green_tail.md`, every bounded solution that visits 0 has |e| ≤ 14, and the two constant solutions |e| = 15 do not meet 0. The orbit started at (0,0) of the untruncated bounded carry is the orbit in the box E = 14. A prefix bound for that box is a prefix bound for the full single-window carry. There is no further geometric series in E.

The ε-system, cut off at 51, is not this operator.

## What is not claimed

The (0,0) share is N15’s proxy. P_* is the growth prefactor of this Frobenius orbit at rate 0.28. It is not the shell constant C, and it is not 8.8×10^{-4}. On the E = 1 prefix, 1/share is about 4.26, while P_* is 6.93. They are different numbers. H1-bad stays open. Frozen R′ and BGS-BGS-001 stay open.
