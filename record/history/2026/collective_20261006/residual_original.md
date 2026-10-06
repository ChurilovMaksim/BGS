# Exact projector residual after the collective hierarchy

6 October 2026. Supporting interface for the frozen collective hierarchy;
no change to its bytes. The all-degree analytic verdict is still pending.

Use the full ordered End(W_m), R_m=Ad(slot cycle), C_U=Ad(U_N^tensor m),
P_H the full U(N)-invariant projector, Pi the balanced-occupation projector,
and P_coll the orthogonal projector onto the entire Haar-removed collective
hierarchy described in C1–C3.

Every collective diagonal insertion lies in ran Pi, and ran P_H is also
contained in ran Pi. Therefore

 P_H P_coll=0,  P_H+P_coll<=Pi,
 Q=I-P_H-P_coll=(Pi-P_H-P_coll)+(I-Pi).                              (I1)

Both summands on the right are orthogonal projections with mutually
orthogonal ranges. They, P_H, P_coll and Q commute with R_m. No commutation
with C_U is assumed or needed to split its trace.

The exact full pair identity is

 |Tr U_N^m|²=min(m,N)+S_(m,N)(U_N)+Tr(R_m Q C_U).                    (I2)

If the all-degree theorem is accepted, its actual flatness/gap inputs give
S_(m,N)(U_N)=O(1) through every fixed positive Heisenberg band. Hence

 N^-2 sum_m w(m/N)(|Tr U_N^m|²-min(m,N))
    =N^-2 sum_m w(m/N)Tr(R_m Q C_U)+O_w(N^-1).                       (I3)

There is no normalization by rank Q. Common-origin rotations cancel in C_U,
so all terms retain the prescribed probability convention.

The two explicit unresolved pieces are the remaining balanced range
Pi-P_H-P_coll and the off-charge range I-Pi. They are not correctly described
as ONLY nontrivial permutation sectors. For example, at m=1 the off-diagonal
traceless matrices lie in Q, yet the cycle is the identity. Some remaining
vectors can be cycle-fixed. I1, rather than a sector slogan, is authoritative.

This is an exact projector decomposition in the actual U replica space.
It is distinct from the stationary-label residual for fixed-J V. The latter
has an accepted aggregate comparison to U, but no operator identification
between its path masks and the projectors in I1 has been established.
