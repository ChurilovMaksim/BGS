# A genuine residual after disjoint Hamming and low-switch removal

Claim ID: BGS-TRACE-021. Scoped pair residual reduction; the signed residual remains open.

This accepted synthesis is separate from the fractional-Hamming theorem. It
combines that theorem with the accepted whole-difference-fiber subset bound
L8 of the low-switch theorem. The new core residual identity may be recorded
as TRACE-021; the fixed-k factorial statement TRACE-020 is unchanged.

## 1. Exact projectors and disjoint masks

Use the unnormalized Hilbert-Schmidt conventions and genuine centered
balanced projector P_r of
[fractional_hamming_cancellation.md](fractional_hamming_cancellation.md).
For rooted cyclic coordinate words x,y in (Z/N)^m, define

    c_j = y_j-x_j mod N,
    h(c) = #{j:c_j!=0} = Hamming(x,y),
    s(c) = #{j:c_j!=c_(j+1)},
    t(c) = sum_j c_j mod N.

Let O_low=O_(r_off)=(I-Pi)F_(r_off). Let L_high be the diagonal
matrix-unit projector selecting exactly

    s(c)<=R_N,  t(c)!=0,  h(c)>r_off.

Equal coordinate occupations imply t(c)=0. Thus L_high is off-charge.
The converse is false and is not used. Every condition defining L_high depends
only on c, so it selects whole difference fibers

    F(c) = sum_x A_U(x) conjugate(A_U(x+c)),
    A_U(x) = product_j U_(x_j,x_(j+1)).

It excludes the constant zero word. Therefore L8 of the
[accepted low-switch theorem](low_switch_offcharge_family.md) applies to this
complete subset with its original envelope. In particular, it does not permit
retaining only off-charge terms within a checksum-zero fiber.

For any simultaneous-cycle-invariant diagonal matrix-unit mask M, expansion
in the literal matrix units gives

    Tr_E(R M C_U) = sum_(x,y selected by M)
                       A_U(x) conjugate(A_U(y)).

The intermediate matrix unit is the simultaneous one-slot rotation of the
final ket and bra; the mask is unchanged under that rotation. O_low and
L_high both meet this condition. Their exact once-counted union is

    {occupation mismatch, Hamming<=r_off}
      disjoint-union
    {s(c)<=R_N, t(c)!=0, Hamming>r_off}.

The first part can cut a checksum-zero fiber; it is estimated by the separate
raw off-charge Hamming theorem. The second part never cuts a fiber internally;
it is estimated by L8. No monotonicity or arbitrary subset principle for
signed sums is used.

Let P_bal=P_(r_bal). P_H and P_bal are orthogonal balanced projectors;
O_low and L_high are off-charge and mutually orthogonal by their disjoint
Hamming conditions. Hence

    Q = I-P_H-P_bal-O_low-L_high                             (S1)

is a genuine orthogonal projector. All four removed projectors commute with
R. Commutation with C_U is neither required nor asserted. In particular,
P_bal is a centered range projector, not a raw coordinate-pair mask.

The accepted exact Haar-cycle identity Tr(RP_H)=min(m,N), together with
C_U P_H=P_H, now gives the finite identity

    |Tr U_N^m|^2-min(m,N)
      = Tr(R Q C_(U_N)) + Tr(R P_bal C_(U_N))
        + Tr(R O_low C_(U_N)) + Tr(R L_high C_(U_N)).         (S2)

This algebra holds at every finite N,m with the stated objects; it is not
an asymptotic assertion or an identification of Q with a stationary family.

## 2. Uniform fixed-coupling consequence

Fix 0<a<b<infinity and the unchanged actual odd-dimensional family U_N at
fixed tau=10^-80. Write h(delta)=-delta log delta-(1-delta)log(1-delta)
and lambda=(1/2)log(160/159). Choose 0<delta_bal<1/2 satisfying BOTH

    h(delta_bal)<(1-2 delta_bal)lambda,
    b h(delta_bal)<1/160.                                   (S3)

Set r_bal=floor(delta_bal m), r_off=floor(0.49m), and
R_N=floor(kappa N/log N), with kappa and eta from the accepted low-switch
result on the same band. Uniformly for aN<=m<=bN at sufficiently large odd N,

- The P_bal trace is exponentially small by the centered Hamming estimate
  with every strict exponent below its positive gamma_(a,b,delta_bal).
- The O_low trace is exponentially small by the denominator-free estimate
  and eventual ||P_N-J_N||<=10^-63. The accepted limsup <=10^-64 implies this
  strictly larger eventual bound, not eventual <=10^-64.
- The L_high trace is exponentially small by L8's whole-fiber subset bound.

For precision, L8 bounds any selected subset of low-switch difference words
excluding zero by

    C N^2 exp(-gamma m)
      + N exp(-gamma m) sum_(r=1)^R binom(m,r)(K N)^r,
    K=C exp(gamma).

The accepted choice kappa=gamma a/8 and R=floor(kappa N/log N) gives
O(exp(-eta N)), with eta=gamma a/2 after a constant enlargement. Polynomial
factors are absorbed with strict exponent slack. Taking a strict common
positive exponent c in these three estimates, (S2) becomes

    |Tr U_N^m|^2-min(m,N) = Tr(R Q C_(U_N)) + O(exp(-cN)).   (S4)

For any bounded weight w supported in [a,b], the original N^-2 weighted
sum of the error is O_(a,b,w)(N^-1 exp(-cN)). The radius 0.49m applies only
to O_low; the balanced radius still needs both inequalities (S3).

## 3. Additional dependencies and exact boundary

The synthesis inherits the fractional-Hamming analytic inputs FM-021 and
Haar tail O5/C9, and additionally the accepted all-translation power theorem
[all_coordinate_translation.md](all_coordinate_translation.md) through
[low_switch_offcharge_family.md](low_switch_offcharge_family.md), L8-L9.
Low-switch diagonal-run decay explicitly requires BOTH uniform nonzero-charge
all-translation powers and FM-021 for zero-charge runs. The inherited
all-translation chain includes FM-018 O8 (one-step Egorov), O9 and O11 for the
same actual nonlinear G=S composed with Phi_g^(tau/(2 pi)), and its actual
normalized invariant area. Its FM-001/FM-006, Markov coding, Ruelle/Pesin and
checked Parry-Pollicott review boundaries remain unchanged. Topological
conjugacy alone or a substituted invariant measure does not supply the input.
No new external theorem leaf is introduced by this synthesis.

The accepted separate synthesis has SHA-256
69ac748eb3d6dcfdccfa144845d75384533e0024e3b3c709518f1fb317ea4f7a.
Its frozen low-switch proof and review have SHA-256
f8780f4c15d677d9ded64ff29884780526ef86ca5c4b9ed58e770b14b231ad95 and
eb50ca67558a40bdfc15bad02a5639bae90cd67de1ec8a2df27b6ed5b124db81.
See the [curated review](../record/fractional_hamming_review.md) and
[raw mapping](../record/fractional_hamming_raw_mapping.json) for the precise
source closure and retained history.

The exact integer synthesis check covers N=2,3; m=1,...,4; every
0<=r_off<=m and 0<=R<=m: 108 radius pairs across eight coordinate families,
with at most 6561 ordered pairs in a family. It checks Hamming/support equality,
checksum implication, cycle invariance, off-charge containment and exact
union cardinality. It is a finite convention check, not analytic evidence.

Q remains unestimated. Balanced high-Hamming contributions and residual
off-charge contributions remain, including checksum-zero fibers that the
whole-fiber low-switch argument cannot split. No full pair comparison,
plateau correction, higher factorial result or BGS bound follows from (S4).
The accepted earlier sparse theorem is retained as prior; no boundary witness
or pending candidate is used as a theorem dependency.
