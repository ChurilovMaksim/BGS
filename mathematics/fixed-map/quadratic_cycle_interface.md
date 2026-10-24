# Explicit ambient-space and cycle interface

6 October 2026. Companion to the frozen whole-sector report; no change to
its formulas, scope, or original bytes.

The ambient Hilbert space is the FULL ORDERED tensor space

    W=(C^N)^(tensor m),  dim W=N^m.

There is no restriction to Sym^m(C^N). The replica space is End(W), of
dimension N^(2m), equipped with ordinary Hilbert-Schmidt inner product.
In the whole-sector report, Sym^2 D_0 parametrizes only the symmetric
TWO-SLOT diagonal coefficient tensors inserted into this full W.

Let C be the slot-cycle unitary
C(v_1 tensor ... tensor v_m)=v_m tensor v_1 tensor ... tensor v_(m-1).
The replica cycle is

    R_m=Ad C,  R_m(X)=C X C^*.

Thus the SAME cycle acts on ket and bra indices. It is not a one-sided
operator X->CX or X->XC^*. With C_U=Ad(U^(tensor m)),

    Tr_(End W)(R_m C_U)
      =Tr_(End W) Ad(C U^(tensor m))
      =|Tr_W(C U^(tensor m))|^2
      =|Tr_(C^N)(U^m)|^2.                                  (C1)

The middle equality follows by evaluating the superoperator trace in the
matrix-unit basis. The last follows by the cyclic index contraction; either
cycle orientation gives the same power trace. No replica symmetrization,
independent phase average, or reduced trace is present in (C1).

For A in Sym^2 D_0, J_m(A)=sum_(r<s) A_rs commutes with EVERY slot permutation.
A permutation relabels the complete set of unordered slot pairs, and if it
reverses a pair's order the local tensor is unchanged by its defining
two-slot symmetry. Therefore Ad C fixes J_m(A) pointwise.

The full Haar projection P_0 commutes with slot conjugation, because every
slot permutation commutes with U^(tensor m). It follows that the Haar-removed
embedding F_m, and hence the entire orthogonally projected quadratic sector,
are also fixed pointwise by R_m. Consequently

    R_m P_quad=P_quad R_m=P_quad,
    Tr(R_m P_quad C_U)=Tr(P_quad C_U).                        (C2)

This is the precise cycle interface used in formula (1) of the whole-sector
report. It does not assert that the entire ambient replica space is fixed
by R_m. A one-sided-cycle problem would have a different block and is not
being evaluated here.

`cycle_checks.json` additionally checks the full-W cyclic contraction in
(C1), using the actual symbol at an auxiliary nonzero time, for the same
finite pairs used in the sector checker. Those floating checks audit the
index convention; the identities (C1)--(C2) are exact algebra.

## Supporting scope

This is a supporting result for TRACE-020, not an extra core theorem or
control of the full balanced/complement trace. Review and original-byte
mappings are in record/collective_promotion_mapping.json. Any full-kernel
identity used by an unregularized corollary retains its separate hypothesis;
the regularized slow-source obstruction does not require identifying Haar
invariants with the entire deterministic kernel.
