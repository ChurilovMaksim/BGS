# Independent reconstruction of the prime-resonant summary

**Verdict:** exact block algebra retained after an orientation repair;
claimed CUE equivalence and claimed reduction of the full problem rejected.
An exact whole-sector criterion and spectral-comb reduction are proved in
[BGS-TRACE-009](../mathematics/prime_resonant_sector.md). Actual fixed-map
sector cancellation, `BGS-TRACE-005` and `BGS-BGS-001` remain **OPEN**.
This is author-level adversarial self-review, not external refereeing.

## Input and disposition

The full 770-line supplied summary was read, not inferred from its title.
Its [inactive text rendition](../evidence/reference/prime-resonant-20260930/submitted_summary.txt)
preserves the read API's text; newline normalization means it is not claimed
byte-identical to the original 20,614-byte upload. Source identity, rendition
hash and execution hashes are recorded in the new manifest.
Neither the summary nor its unsupported claims became an authority.

| Submitted assertion | Independent finding |
|---|---|
| Raw Weyl law and section-dependent ordinary Weyl signs | Correct, already in the corpus. Raw coefficients require $(-1)^{mn}$. |
| 32 modes, degree 9, zero mean, coefficient mass $19/20+\sqrt{101}/50$ | Reconstructed through the existing exact Laurent checker. Correct and prior corpus data. |
| Kick exponential as twisted convolution; finite $k=2,3$ partition formulas | Correct finite algebra, already supplied by the Weyl and partition bridges; no cancellation estimate follows. |
| Inverse Egorov covariance with $S^{-1}$ | Correct covariance; incompatible with the summary's ordering for $U=e^{itA}M$. |
| $A_j=M^{-j}AM^j$ in the left-to-right block for $U$ | Incorrect. Replace by $M^jAM^{-j}$. Numerical control shows that even the block trace square changes. |
| $d_p\mid p-\chi_p$ and proper-period repetition | Correct prior arithmetic; exact block identity holds for every integer repetition. |
| Pointwise CUE leading square or uniform pointwise CUE comparison is equivalent to the pair goal | Incorrect. Weighted comparison is sufficient; one ensemble expectation is not a deterministic trace law. |
| One selected $O(\sqrt p)$ bound is the remaining full-BGS bottleneck | Incorrect scope. It handles one mode only; nonresonant times, composites and higher correlations remain. |
| A fixed block may be compared as Haar CUE($p$) | Wrong reference. The appropriate reference is the power $V^d$, with variance $\min(rd,p)$; Rains' theorem describes its smaller independent reference components. |
| Split $q=2$ and nonsplit odd $q$ | Nonsplit odd is exact. Split $q$ is even, but $q=2$ is not guaranteed. |
| $\omega(v,Sv)=-2Q(v)$ | Correct for the submitted inverse $S$, not for the maintained positive covariance. The maintained sign is $+2Q(v)$; $\det(I+S)=8$ passes. |
| Selected invariant $-98$; collision primes 29,97 | Exact reconstruction below. These are candidate norm collisions, not automatic orbit collisions or scalar exceptions. |
| Radical directions in a claimed constrained modular phase | No actual phase/radical computation is supplied in the summary. Not certified or promoted. |
| Tiny fixed $\tau$ supplies an asymptotic obstruction | Incorrect inference. Coherence is rigorously finite-size; the relevant control parameter is $|\tau|p^2$. |
| Pair estimates imply all orders or point-process convergence | No proof supplied. Existing higher-order and positive-measure bridge requirements remain. |

The scalar-return exclusion and qualitative nonzero traces already proved
in FM-010 are stronger than the summary's safe-prime exclusion. This audit
does not claim those results as new.

## Exact reconstruction of the scalar test

For raw frequency $v=(m,n)$, $Q(v)=m^2-2n^2$. The selected frequency
$(0,7)$ has $Q=-98$ and coefficient $9/20$. All other support classes
give differences
$$
-64,-30,-29,1,26,27,48,90,96,97,99.
$$
Their prime divisors are exactly $\{2,3,5,11,13,29,97\}$; the summary's
entry 1 is not a prime. At $p>17$ away from 29,97, only the selected
frequency and possibly its negative occur in its oriented orbit.

At 29, four additional $(\pm1,\pm8)$ frequencies are in that orbit,
but the coefficient sum is $903/1000$. At 97, the candidate
$(\pm1,\pm1)$ points have the same norm and are in the other orbit;
the selected orbit sum is $9/10$. The proof includes the complete
29-orbit and a square-character certificate at 97. Both exceptional
exclusions can therefore be removed from this scalar test.

The prior negative-real-mass argument gives a uniform selected orbit sum
real part at least $169/500$ for every prime at least 19. The new proof
records the exact linearized variance identity, but does not infer
small traces from that positive variance.

## Corrected sector and obstruction statements

For $K\subset[a,b]\subset(0,\infty)$, the requested normalized absolute
sector sum $S_p(K)$ and actual mass $E_p(K)$ satisfy
$$
|S_p(K)-E_p(K)|\le (b-a)/d_p+1/p.
$$
The integer determinant proves $d_p>2\log p/\log(3+2\sqrt2)$.
Hence **$S_p(K)\to0$ is equivalent to $E_p(K)\to0$**. In a growing
interval sector, the needed average trace square is $o(pd_p)$.
Uniform square-root cancellation across the sector is sufficient and
stronger than needed; single-mode $o(p)$ is enough for that mode only.

An exact Fejer identity converts this to a block-spectrum energy.
Its pullback is the average of width-$1/p$ pair kernels centered at all
shifts $h/d_p$. The missing quantitative input is baseline $1+o(1)$
for that average, not merely a bounded occupancy estimate. The audit
proves this implication, but not its hypothesis for the specified block.

A single coherent trace $\ge cp$ at a positive bounded Heisenberg time
on an infinite subsequence already disproves pair CUE comparison: it
creates a persistent positive time-mass that a narrow smooth test detects
against an atom-free reference. A positive fraction is unnecessary.
The finite regime $p\ll10^{40}$ at fixed $\tau$ cannot supply that
infinite subsequence, and the audit finds no actual asymptotic obstruction.

## Reproduction and trust boundary

The [new checker](../computations/verification/prime_resonant_audit.py)
passed 302 odd primes through 2000 for order/parity/determinant checks,
296 selected orbit sums, four independently assembled matrix controls,
and nine clock/cluster/deterministic spectral controls. Maximum product
error over $r=1,2,3$ was $3.65\times10^{-13}$; the opposite-orientation
operator distances were between 0.11 and 0.32, and the trace squares
differed as well. These numerical checks use control times, never a
floating substitute for the physical tiny coupling.

Integer arithmetic and Gaussian rationals establish the finite arithmetic
certificates. The analytic sector, positivity and Fejer deductions are
proved in the mathematical source, not by finite regression. The prior
Laurent checker is an explicit dependency of the new verifier. No Lean
compilation, external referee certificate or asymptotic computation is
claimed. Focused repository checks and the manuscript build are recorded
in a separate execution manifest; publication follows review of the diff.
