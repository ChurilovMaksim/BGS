# Separate synthesis: disjoint Hamming and low-switch removal

This corollary is separate from the frozen fractional-Hamming candidate. It was requested after the core reconstruction and does not enlarge that candidate's review scope or analytic dependency set silently.

**Verdict: proved under the two separately accepted input families.** It combines the fractional-Hamming theorem audited in `review.md` with the whole-difference-fiber subset bound L8 of the accepted low-switch theorem. It inherits the latter's additional all-translation/diagonal-run analytic dependencies and their exact review boundaries. The acceptance and raw theorem are frozen under `inputs/synthesis/`; `synthesis_input_manifest.json` records their hashes. In particular, the accepted low-switch review has SHA-256 `eb50ca67558a40bdfc15bad02a5639bae90cd67de1ec8a2df27b6ed5b124db81` and its proof has SHA-256 `f8780f4c15d677d9ded64ff29884780526ef86ca5c4b9ed58e770b14b231ad95`.

## Exact raw masks

For rooted cyclic coordinate words x,y∈(Z/N)^m set

    c_j=y_j−x_j mod N,
    h(c)=#{j:c_j≠0}=Hamming(x,y),
    s(c)=#{j:c_j≠c_(j+1)},
    t(c)=Σ_j c_j mod N.

Let L_high be the orthogonal matrix-unit projector selecting exactly

    s(c)≤R_N,  t(c)≠0,  h(c)>r_off.

Each condition depends only on c. It therefore selects whole fibers
F(c)=Σ_x A_U(x) conjugate(A_U(x+c)), never a coordinate-dependent subset inside a fiber. The selected set excludes the constant-zero difference word. L8 consequently bounds the complete signed sum selected by L_high with the same envelope as the original low-switch family.

Occupation balance implies t(c)=0, so every selected pair is off-charge. The converse is neither asserted nor needed. In particular one may not use this argument to select only off-charge terms inside a checksum-zero fiber.

The cyclic pair amplitude is A_U(x)=∏_j U_(x_j,x_(j+1)). For the two-sided full cycle R, the literal trace of any cycle-invariant diagonal matrix-unit mask M is

    Tr_E(R M C_U)=Σ_(x,y selected by M) A_U(x) conjugate(A_U(y)).

This follows by expanding the trace: the intermediate matrix unit is the simultaneous one-slot rotation of the final ket and bra, and the mask is invariant under that rotation. Both the low-Hamming off-charge mask O_(r_off) and L_high satisfy this condition. Thus the exact once-counted union is

    {occupation mismatch and Hamming≤r_off}
       disjoint-union
    {s(c)≤R_N, t(c)≠0, Hamming>r_off}.

The first set may partially cut checksum-zero fibers; it is controlled by the independent raw off-charge Hamming theorem. The second set cuts no fiber internally and is controlled by L8. No inference from one signed-sum bound to an arbitrary subset is used.

## Genuine residual projector

Let P_(r_bal) be the genuine centered balanced Hamming-range projection from the core theorem. Then P_H and P_(r_bal) are orthogonal and balanced. Both O_(r_off) and L_high are off-charge. Their Hamming conditions are complementary, so they are orthogonal to one another as well. Therefore

    Q=I−P_H−P_(r_bal)−O_(r_off)−L_high

is an orthogonal projector. All four removed projectors commute with R. No commutation with C_U is assumed. The centered balanced projector P_(r_bal) is not identified with a raw pair mask.

Using the accepted exact Haar-cycle trace Tr(RP_H)=min(m,N), one obtains

    |Tr U_N^m|²−min(m,N)
      =Tr(R Q C_(U_N))
        +Tr(R P_(r_bal) C_(U_N))
        +Tr(R O_(r_off) C_(U_N))
        +Tr(R L_high C_(U_N)).

This is an exact identity at every finite N,m for which the objects are defined.

## Uniform actual-map consequence

Fix 0<a<b<∞. Choose δ_bal>0 satisfying the two core entropy constraints and set r_bal=floor(δ_bal m). Set r_off=floor(0.49m). Let R_N=floor(κN/log N), with κ and η supplied by the accepted low-switch theorem on the same band.

Uniformly for aN≤m≤bN at sufficiently large odd N, each of the last three traces is exponentially small:

- the balanced term by the core centered-range estimate;
- the off-charge low-Hamming term by the core denominator-free bound and eventual t_N≤10^−63;
- the disjoint high-Hamming low-switch term by L8's whole-fiber subset bound.

Their sum is O(e^(−cN)) for some fixed c>0 after taking a strict common exponent. Its original N^−2 bounded-weight compact-band aggregate is exponentially small. Hence the pair comparison on the band is reduced, with an exponentially small error, to the single remaining signed trace Tr(R Q C_(U_N)). This does not estimate Q, the plateau, or higher factorial correlations.

## Finite convention check

`check_synthesis.py` exhaustively enumerates literal pairs for N=2,3 and m=1,…,4. For every 0≤r_off≤m and 0≤R≤m it checks Hamming/support equality, checksum implication, simultaneous-cycle invariance, off-charge containment, and disjoint-union cardinality. There are 108 radius-pair cases across eight coordinate families; the largest family has 3^8=6561 ordered pairs. Arithmetic is exact integer arithmetic. The output `synthesis_results.json` is a bounded mask check, not proof of either analytic input.
