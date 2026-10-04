# Research review: the folded square and block crowding

Date: 1 October 2026. No subagents. Author self-review, independent
finite representations and Wolfram symbolic evaluation; no external
referee or new Lean compilation.

The [final audit of 4 October](folded_quadratic_audit_20261004.md)
pins the revised proof, clarifies the block's common scalar phase and
adds direct rotation controls. Its scope remains author self-review.

## Verified advance and exact boundary

[BGS-TRACE-012](../mathematics/folded_quadratic_resonance_control.md)
refines the signed three-strip estimate to
$|Z_N(W)|\le C_W\sqrt{E_NG_{d,N}}$, where
$G_{d,N}=\|P_d(\rho_N^2)\|_2^2$. Projecting the product before
Cauchy--Schwarz retains arithmetic alignment of density peaks.
The exact factorial counterterm budget is retained. The conditions
$EG_d\to0$ and $(1/d+1/N)\sqrt{G_d}\to0$ suffice.

The improvement over $EM_4\to0$ is strict: a clock background plus
K=L^2 phases at zero, N=L^4,d=L^3, has $EM_4\gtrsim L$ but
$EG_d=O(L^{-2})$. Simple odd-dimensional perturbations preserve this.
The example has no claimed CUE pair law and is not the frozen map.

The identity $G_d=\int B_d^2f_{C,N/d}^4$ keeps root allocation;
the block density alone omits it. Identical C=I can give a d^2 ratio
between concentrated and balanced root energies. The proof also gives
positive shifted four-point and fourth joint-trace formulas for G.

Separately, K block eigenvalues in an epsilon*d/N arc force microscopic
r-point factorial mass at least $(K-(r-1)d)_+^r/(Nd^{r-1})$.
The exact minimum is the balanced falling-factorial count. If d=o(N),
epsilon->0 and K reaches $(Nd^{r-1})^(1/r)$ with a positive constant,
Sine_2 factorial comparison fails. No actual-map infinite subsequence
or weak-process failure is proved.

## Adversarial review

| Risk | Resolution |
|---|---|
| Discard root allocation | Same-block spectra demonstrate a d^2 loss. |
| Drop the sum strip or intersection | Exact three-strip union identity, common coefficient -2. |
| Count absolute summands | Keep the signed integral; absolute sums are recorded separately. |
| Drop factorial terms | Retain Q/d and the exact finite CUE counterterm. |
| Use moving tests for the obstruction | Fix a positive smooth neighborhood first, then shrink it after the lower limit. |
| Assert actual multiplicities 35,34,... at p=239 | These are the convex minimum, not computed actual multiplicities. |
| Treat tiny tau as shrinking with N | Tau remains 1e-80; coherence is finite-dimensional. |
| Collapse the ordered product | Noncommutative words remain; the Duhamel certificate grows with tau*N^2 at Heisenberg times. |
| Infer BGS from this sector | Nonresonant times, other cones and higher factorial orders stay open. |

The finite CUE expectation bound is derived from its empirical frequency
Gram kernel. For the actual p=239,d=7 map, analytic norm telescoping gives
epsilon<3e-76, actual cubic mass at least 254694/239 and finite CUE
expectation below 1e-600. No float computation represents the actual
kick. Earlier finite coherence is credited; this is not an asymptotic
BGS counterexample.

## Controls and corrections during development

The [verifier](../computations/verification/folded_quadratic_audit.py)
checks 24 direct Gaussian/trace-convolution/FFT product cases at
N=17,31,81 and d=1,2,3,7, with complex filters; 15,500 exact allocations
in 240 minimum problems (K=0..14,d=1..4,r=2..5); the strict family through
N=6561; three same-block root controls; 1,089 Sine and 1,156 finite CUE
Gram cases; and 24 noncommuting ordered Duhamel controls. SymPy series,
integrals and matrix powers agree with the
[Wolfram values](../evidence/20261001/folded_quadratic_wolfram.json).
Finite checks corroborate the proofs, rather than prove the limits.

An unproved trial constant 4(1+L) failed at L=3; it was replaced by a
positive-kernel triangle bound, rather than fitted. FFT noise invalidated
ratios in tiny Gaussian tails: ratios now use positive direct sums and
omit underflow cells; the division-free energy identity covers all cells.
Centered integer grid coordinates avoid endpoint cancellation. A temporary
variable collision in the added finite-CUE check and the first Wolfram
JSON export were corrected before promotion. The final
[execution packet](../evidence/executions/20261001-folded-quadratic.json)
records actual commands, statuses, hashes and manuscript build scope.
Focused checks are separate from a full workspace/Lean build.

## Next load-bearing obligation

Prove actual E=o(1) and the required shifted fourth energy control, or
derive signed cancellation bypassing this sufficient condition. A block-
only analysis must quantify root allocation. An obstruction needs the
crowding premise on an infinite subsequence. These asymptotic inputs,
TRACE-005 and BGS-BGS-001 remain OPEN.
