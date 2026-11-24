# Powers of seven: finite witnesses and changed-coupling results

**Status: source preservation and scope map.** The original chapters below
are included as research material. Unlike the specifically audited items in
the [Pell](../pell/README.md), [exact splitting](../exact_splitting/README.md)
and [effective gaps](../effective_gaps/README.md) notes, the estimates in
this document were classified from the sources, not independently
refereed theorem by theorem. Their inclusion is not a promotion into the
core registry. Some companion computations are available in the
[central verifier](../../../../computations/verification/bgs_f_november/);
finite checks do not verify asymptotic arguments. Use the chapter itself
for the exact hypotheses and proof.

All the results use the same generator and linear propagator as the
[maintained model](../../fixed_map_resolvent_frontier.md). Put $N=7^k$,
$m=3N/7$ and $U_N(t)=e^{itA_N}M_N$. A physical coupling $u_N$ means
$t=Nu_N$. Thus the original problem has $t=N10^{-80}$, and the
critical scaling below has $t=\kappa N^{-1/2}$. These are different
regimes.

## Finite witnesses at the literal coupling

The reported bounds in this table are **finite** statements about the
original operator, not assertions for all $k$ or for the critical
scaling. The CUE subtraction in $\Delta_2$ is for the original
band-two weight.

| Dimensions | Reported witness | Original source |
| --- | --- | --- |
| $N=7^k$, $2\le k\le56$ | $\lvert\operatorname{Tr}U_N^m\rvert>0.979N$ and $\Delta_{2,N}>0.040$; a bounded continuous local test also separates these dimensions from Sine₂ | [ordinary trace and zero mode](BGS_Zero.tex) |
| $N=7^k$, $2\le k\le59$ | $\lvert\operatorname{Tr}U_N^m\rvert>0.957N$ and $\Delta_{2,N}>0.053$; the chapter also gives a separate composite-dimension return | [second-order expansion](BGS_Second.tex) |
| $N=7^{60},7^{61}$ | $\lvert\operatorname{Tr}U_N^m\rvert/N>0.9526$, $\lvert\operatorname{Tr}U_N^{2m}\rvert/N>0.8914$ and $\Delta_{2,N}>0.054$ | [resolvent transport](BGS_Resolvent.tex), §6 |
| $N=7^{62}$ | Excess greater than $0.019$ for the specified bounded continuous test on close pairs; not a bound on $\Delta_{2,N}$ | [resolvent transport](BGS_Resolvent.tex), §§7–8 |

A few sections also discuss exact transcendence or return identities at
fixed coupling. Those are not spacing laws. Distinguish the
Heisenberg-scale time $m=3N/7$ of these witnesses from the short time
$m=k$ used in the [Pell proof](../pell/README.md).

## Shrinking couplings and local cluster laws

* [Ordinary trace and zero mode](BGS_Zero.tex),
  [second-order expansion](BGS_Second.tex),
  [resolvent transport](BGS_Resolvent.tex),
  [fourth-order estimate](BGS_Fourth.tex) and
  [sign-sensitive decay](BGS_Signed_Decay.tex) are successive
  treatments of the shrinking-kick regime. The last of these gives,
  under $u_N=o(N^{-3/2}/\log\log N)$, the weak limit of the local
  process as a randomly shifted lattice of spacing $7/3$, with
  multiplicities $2(1+\nu_7(B+j))$ at lattice index $j$ for uniform
  $B\in\mathbb Z_7$. It also gives uniform closeness of ordinary
  normalized traces to the linear reference on every fixed
  Heisenberg-scale time window. This limit is not Sine₂.
* The [fourth-order chapter](BGS_Fourth.tex) separately reports
  convergence of the original pair defect to the linear value in
  $(0.08443,0.08656)$, under the stronger hypothesis
  $u_N=o(N^{-8/5}(\log N)^{-2/5})$. This is a second-moment conclusion;
  it must not be inferred from the weaker local-process theorem alone.
* The [doublet splitting law](BGS_Split_Law.tex) selects nodes with
  conductor parameter $\ell\equiv3\pmod7$. For $t_N\ne0$ with
  $|t_N|\sqrt N\log\log N\to0$, the two actual eigenangles near a
  typical selected node, when their gap in radians is rescaled by
  $\sqrt N/|t_N|$, have limiting gap
  $(7/300)|2Y_1-Y_2-Y_3|$ with independent arcsine variables $Y_i$.
  This is a law for selected doublets, not for the whole fixed-kick
  spectrum.

## The critical scaling is still a compression problem

The [critical-block source](BGS_Critical_Block.tex) treats
$u_N=\kappa N^{-3/2}$ with fixed $\kappa$. It reports joint limits
for finite selections of projected blocks and a weighted
Hilbert–Schmidt limit for the specified compression of the exact
propagator. The [critical-oscillation source](BGS_Critical_Oscillation.tex)
gives subsequence-dependent singular-value and finite Hermitian
compression laws for a different inter-node selection. The selections
are not interchangeable, and neither conclusion controls coupling to
all remaining nodes. In particular, there is no stated full spectral
limit at the critical scaling, much less at $u_N=10^{-80}$.

The source files are the original Russian-language TeX from the
22 November cumulative packet, with no claim-state or notation changes.
