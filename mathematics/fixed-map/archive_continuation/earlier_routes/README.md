# Earlier fixed-map routes: signed classes, return obstructions, and arithmetic

This is a scope and dependency map for six source chapters of the November
BGS-F contribution. They all use the original odd-dimensional modular-Weyl
matrix (U_N=\exp(i\tau N A_N)M_N), (\tau=10^{-80}), except where an
explicitly auxiliary example or variation of the parameter is identified.
See the [fixed-map definitions](../../fixed_map_resolvent_frontier.md) and
[the unresolved programme](../../../open_questions.md). The TeX files
retain the submitted derivations and original numbering. This map checks
scope against the maintained corpus; it is not an independent re-audit of
every analytic argument. Finite checks do not upgrade these chapters or
change the status of the signed Heisenberg comparison.

## 1. Pressure and selected signed path classes

[Submitted proof, §§1–10](BGS_pressure.tex) ·
[replay sources](../../../../computations/verification/bgs_f_november/continuation/)

Write (h=\log(3+2\sqrt2)), (p=P_{\mathrm{top}}(-v/2)) for the
unstable log-Jacobian (v), and (p_{m,N}=\operatorname{Tr}U_N^m).
The logarithmic-band argument has three steps:

1. Two fixed points have unequal unstable multipliers, so (v) is not
   cohomologous to a constant. Strict convexity between the geometric
   potential and the zero potential gives (p<h/2).
2. The odd-comb correction (L_n=(-1)^{Nn_1n_2}D_n), with (B\equiv I
   \pmod2), is used to adapt Faure's logarithmic local trace formula to
   the exact odd sector. This adaptation, not just the classical pressure
   inequality, is a load-bearing analytic input. The source cites
   [Faure, arXiv v2: admissibility (21), Theorem 12 and equations (70)–(72)](https://arxiv.org/pdf/nlin/0610004)
   and Bowen/Parry–Pollicott for the pressure arguments.
3. Once (|p_{m,N}|\ll e^{(p+\epsilon)m}) holds in that band, choose
   (2/h<a<1/(p+\epsilon)). Summing gives
   (N^{-2}\sum_{m\le a\log N}|p_{m,N}|^2=O(N^{-2\eta})).

The logarithmic-band conclusion and decay at (m=k,N=h_k) must not be
counted as new: the registered [uniform trace bound](../../fixed_kick_uniform_trace_bound.md)
already implies both (choose (2/h<a<1/\log a_0) for its base
(a_0<\sqrt{3+2\sqrt2})). Keep the separate odd-sector derivation and
pressure-variation computation as a route comparator.

For (N<m<2N), §§5–9 treat **different** families of pairs. A marked
two-contact class has a positive weighted lower limit after cyclic
subtraction; an explicitly once-counted class has signed asymptotic
(-N(m/N)^3/6+o(N)); the same-directed-edge family can grow
exponentially. These statements use eventual entry flatness and
intensity-chain contraction, corresponding to the input of
[position-chain mixing](../../position_chain_mixing.md). A separate
two-position calculation at (m=N=h_{209}) is finite, not an
asymptotic sign claim. Neither the coexistence of signs nor a marked
subfamily yields the signed complement of all non-cyclic pairs.

## 2. Growing reconnections and a compensating complement

[Submitted proof, §§1–7](BGS_Reconnection.tex) ·
[replay sources](../../../../computations/verification/bgs_f_november/reconnection/)

The class has a fixed root and (r) prescribed short common pieces of
length (\ell=\lceil8\log_2 N\rceil) separated by free gaps. The
labels of the pieces are permuted subject to a root constraint; the
result counts a pair of words just once, including when two labelings
coalesce. For the stated regime (m\asymp N),
(r=O(\sqrt{N\log N})), the signed mass is
```
(1 + O(N^-5)) N/[r(r+1)]
  * (prod(j=0..r, 1+j/N) - prod(j=0..r, 1-j/N)).
```
Unitarity contracts the unrestricted gaps; the
(B^\ell-J) contraction and entry flatness control the marked segments
and repeated-piece error. The remaining cycle sum is the
[Stanley long-cycle identity, Theorem 3.1 with cycle type (r)](https://math.mit.edu/~rstan/papers/cycles.pdf);
it is derived in the source by Schur–Weyl duality and hook characters.
For choices giving mass (cN+o(N)), its complement **inside the
common-root class** gives (-cN+o(N)), not the missing global
plateau contribution. The last two sections construct a separate
sequence (V_N) with these kinds of controls and non-Sine₂ behavior;
it is not the fixed quantization.

Compare the previously accepted
[three-block](../../three_block_unmarking.md) and
[four-block](../../four_block_unmarking.md) distinct-port cancellations
and the [earlier cycle count](../../../spectral_research/proofs/research_round5_2026_10_21/root_reconnection_permutation_computation_note.md).
The additional scope is the specified growing, root-anchored class,
not all reconnections or an unmarked Heisenberg sum.

## 3. Nonzero translated returns

[Submitted proof, §§1–8](BGS_Translated.tex) ·
[replay sources](../../../../computations/verification/bgs_f_november/translated/)

For each fixed (\delta>0), the asserted all-time bound is
`sup_{m in Z, n(v)>=delta N} |Tr(T_N(v)* U_N^m)|/N`
`= O_delta((log log log N)^(-1/2))`, where
(n(v)=|v_1|+\sqrt2|v_2|) on centered representatives.
The time (m) in this conclusion is unrestricted, but the proof first
bounds entries of the conjugation channel only for
(1\le j\le \lfloor c\log\log\log N\rfloor), by
(\exp[-(\log N)^{3/4}]). A short averaged orbit of almost-orthogonal
observables is then tested against operators that commute with (U_N).
Inputs are the uniform classical nontranslation geometry from the Weyl
chapter below, an analytic sublevel estimate, and growing-window
Egorov errors. Qualitative small-label and sector-projector versions
have their own quantifiers in §§4–7; the macro-label rate quoted above
should not be carried over to them.

On (N=7^k), the explicit partial linear return (m=3N/49) has
49 Weyl coefficients, 48 nonzero-label ones. Their suppression gives
a normalized Hilbert–Schmidt distance at least
(\sqrt{12/7}-o(1)) from every phase multiple of (M_N^m).
This complements the existing
[arithmetic translation-algebra exclusion](../../../spectral-obstructions/arithmetic_translation_exclusion.md),
which is a one-step compression bound; the earlier
[all-oldspace analysis](../../../spectral_research/proofs/research_round2_2026_10_20/arithmetic_iterated_all_oldspaces.md)
already uses short conjugation windows. The present target is an overlap
with arbitrary powers, not an eigenvector-mass statement or a substitute
for the [torsion-sector continuation](../torsion_transport/README.md).
In particular the scalar template (v=0), the ordinary trace and the
full local law are not controlled by the translated-return estimate.

## 4. Weyl-channel deletions and exact resonance arithmetic

[Submitted proof, §§1–17](BGS_Weyl.tex) ·
[replay sources](../../../../computations/verification/bgs_f_november/weyl/)

For (W_N=\operatorname{Ad}U_N), (|p_{m,N}|^2=\operatorname{Tr}W_N^m).
Sections 1–7 study two different deletions. Any selected (O(N))
diagonal Weyl channels have vanishing normalized weighted mass
when the absolute value is taken *after* summing over time in each
channel. Separately, a traceless small-label compression with
(0<n(v)\le N/16) has a power of length
(\lceil400\log N\rceil) of norm at most (N^{-12});
the determinant identity in the source uses it to remove paths spending
too long consecutively in that region. Neither deletion controls all
surviving channels or their coherent exterior returns. Sections 8–12 add
finite arithmetic-return calculations, classical all-iterate
nontranslation, and decay of individual outer-label transitions for
each fixed iterate. The latter estimate is not uniform at Heisenberg
time.

Sections 13–17 use the Lindemann–Weierstrass specialization of finite
exponential polynomials for the literal nonzero algebraic parameter
(t=N/10^{80}). They distinguish the exact finite-dimensional
contraction of transition probabilities for each fixed (N,m)
((N\ne7)) from any positive uniform gap. If
(o_N=\operatorname{ord}(S\bmod N)), then an algebraic balanced monomial
in the eigenvalues lies in (\mu_{o_N}). The arithmetic bound
(o_N\le 4N/3) excludes nonzero algebraic phase differences shorter
than (3/4) of the mean gap; it does not exclude such gaps with
transcendental endpoints' ratio. Simultaneous specialization coarsens
classes of exact ratio coincidences to those of (M_N); orbit counting
there gives
`max_z # {(i,j): lambda_i/lambda_j=z} / N^2`
`<= (log(3+2sqrt(2))/2 + o(1))/log N`.
The prior [scalar-return rigidity](../../frozen_arithmetic_trace_rigidity.md)
is not novel here. The earlier
[one-step Weyl self-overlap study](../../../spectral_research/proofs/research_round8_2026_10_21/r8_original_uniform_weyl_self_overlap.md)
also treats near-commutation of Weyl operators, a different question
from deleting their time-summed diagonal channels. The quantitative
small-mode deletion, balanced
monomial scope, and exact-ratio multiplicity bound are distinct routes
to scrutinize, not quantitative estimates of near-coincidence.

## 5. Classical normalizers and noncommuting canonical templates

[Submitted proof, §§1–10](BGS_Symmetries.tex) ·
[replay sources](../../../../computations/verification/bgs_f_november/symmetries/)

For the physical map (F=\phi^\tau B), the chapter claims
that any area-preserving homeomorphism normalizing (F^n) up to
inversion, (n\ge1), is a power of (F) and hence is not a reversor.
The conjugacy to (B) makes a topological candidate affine. Two Fourier
orbit sums restrict the translation and exact fixed-point multipliers
then rule out remaining cases. Equilibrium-measure uniqueness, the
geometric potential, and Livšic cohomology enter the area-preserving
argument and its singular-pushforward companion; the finite Hessian
test does not check those inputs.

For a fixed analytic canonical template (\kappa\notin\{F^j:j\in
\mathbb Z\}) with an Egorov quantization (Q_N), the reported result
is `sup_m |Tr(Q_N* U_N^m)|/N -> 0`. The rate
(O_\kappa((\log\log\log N)^{-1/2})) needs the stated (C^7)
quantitative Egorov input for both directions. This extends a comparison
with translations to more general templates, not the scalar template
(\mathrm{id}=F^0). The earlier
[algebraic/Affine quantum symmetry results](../../frozen_arithmetic_trace_rigidity.md)
and [metaplectic symmetry gap](../../../spectral_research/proofs/research_round8_2026_10_21/r8_original_uniform_metaplectic_symmetry_gap.md)
are different statements; neither a classical smooth classification
nor a missing symmetry by itself assigns the spectral statistics.

## 6. Spectral multiplicities and zero-time response

[Submitted proof, §§1–11](BGS_Spectrum.tex) ·
[replay sources](../../../../computations/verification/bgs_f_november/spectrum/)

Generic algebraic rank is specialized to (t=N/10^{80}) using minors
of matrices with entries that are finite exponential polynomials. The
same method applies to (\operatorname{Ad}(U_N(t)^m)-zI) for algebraic
(z). Simplicity on (3^k) and (5^k) and the maximal-order inert
prime criterion with its lifting condition were already given in
[exact spectral simplicity](../../../spectral_research/proofs/research_continuation_2026_10_20/exact_spectral_simplicity.md);
they should not be recounted. Simplicity under powers requires
(\gcd(m,o_N)=1).

On (7^k), the primitive doublets split at first order in a
proportion (83/96+O(N^{-1/2})). The inherited bound
(\liminf s_{7^k}/7^k\ge345/392) is superseded by the
[later exact-splitting proof](../exact_splitting/README.md), but the
stationary-phase formulas and the treatment of clumped levels are
prerequisites worth preserving. The ordinary Cesàro average takes
(T\to\infty) **first** at fixed (N); it does not describe
(m\asymp N). The curvature calculation at (m=3N/7), (k\ge3),
is
`I_N''(0) = -(34112649/14000000) N^3` in the **physical strength**
variable, for (I_N(u)=N^{-2}|\operatorname{Tr}(e^{iNuA_N}M_N)^{3N/7}|^2).
It is not a Taylor bound at (u=10^{-80}) uniform in (N).
