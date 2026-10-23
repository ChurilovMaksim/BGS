# Right-frame bound for the independent conditional resummation worker

Author candidate proved in Sections 2--3 of `right_overlap_and_unmasked_insertions.md`; independent review of this extension is still pending. The parent has separately assigned conditional CP resummation to a native worker. The already saved composition/resummation sections here are author derivations, not an accepted premise for that worker.

Let A_c be the row-minus-column-c slice of U, C e_c=A_c*, and R_U X=XU. For every fixed r>=1 the actual source-bound proof gives

    ||C* R_U^r C|| <= C_r sqrt(log(2N)/N).

The right overlap is derived directly as

    sum_y U_(y+c,y) conjugate(U_(y+d,y)) (U^r)_(y+d,y+c).

The cyclic internal Hessian is -(3/2)I+(P+P*)/4. Its boundary vectors differ from the left case; direct elimination gives cat reduced mixed derivative (A_r+1)/(4B_r), 1/4 at r=1 and 3/16 at r=2. Actual perturbations preserve the [1/10,1/3] interval for every alias. The prior independently reviewed fixed-r Poisson/stationary-phase/TT* argument then applies to these newly verified hypotheses.

For arbitrary unitary B, including arbitrary other Kraus labels and other coherent run lengths, set

    F_n(B)=(1/N)sum_b |Tr(U^n K_b B)|^2,
    C_B=L_(B*) C,  K_b=Z_b U Z_b*.

Then C_B* R_U^r C_B=C* R_U^r C and F_n(B)=N||C_B* U^n/sqrt(N)||^2. Consequently, for every integer A and M>=0,

    sum_(n=A)^(A+M-1) F_n(B)
      <=N [M gamma_(L,N)+C_flat L],
    gamma_(L,N)=C_flat/L+(1-1/L)max_(1<=r<L)||C*R_U^r C||.

This is uniform in B, A and M, and survives probability averaging over B. **B must stay fixed during the n-sum.** Varying a single run at fixed total length generally changes the remaining B and is not authorized by this estimate. Total-time/composition regrouping needs its own argument.

## Interface to the native first-pinch resummation

The parent subsequently supplied the independently developing identity

    F_m(z)=q sum_(n+p=m-1) z^n Tr_H(T^n D T_z^p),
    T_z=zT+qD, q=1-z,
    F_m(z)=Tr_H(T_z^m)-z^m Tr_H(T^m)>=0.

For fixed p and z, T_z^p is a probability mixture of adjoints of unitary words B. Its law depends on p,z,N,U, but not on n. Exact composition of adjoints gives `Tr_H(T^n D T_z^p)=E_B F_n(B)`. This is precisely the fixed-B quantifier above.

For total times A<=m<=M, each fixed p has n in a consecutive interval starting at max(0,A-1-p). Weighted prefix summation by parts with z^n gives a boundary term at most `N C_flat L z^max(0,A-1-p)`. Summing p and multiplying q/N^2 bounds this by `C_flat L q M/N`. The main term is exactly

    (gamma_(L,N)/N) sum_(m=A)^M (1-z^m).

Thus the native proposed use of the right-frame bound is valid and yields the conditional unmasked result for q_N->0 by first fixing L, then N->infinity, then L->infinity. No fixed-total-time n-dependent B was substituted. This interface check does not declare the native worker's independent review complete and supplies no masks or deconvolution.

## Quantitative fixed-lag boundary

The Hessian spectral margin, inverse row-sum bound and reduced mixed derivative interval are uniform in r. For a common compact internal cutoff, each gradient component touches only a bounded number of one-step phases. The number of relevant aliases is therefore at most K^r for a fixed K, and the branch count is 4^(r+2). These observations alone do not give a uniform C_r.

The unresolved quantitative step is an explicit r-dependent bound for the parameter-dependent stationary-phase remainder and amplitude derivatives: the current proof chooses arbitrarily high integration-by-parts order after fixing r, and uses fixed-order smooth bounds. A quantitative common analytic neighborhood/Morse-coordinate derivative bound, or a controlled sequence of one-dimensional eliminations, would be needed before allowing r to grow with N in the overlap theorem. No such bound was completed or assumed. The fixed-block estimate above is sufficient whenever the conditional resummation can first fix L and subsequently let L grow; it does not require growing-r stationary-phase constants.

Exact controls verify the right orientation, including a counterexample to the invalid left covariance. Their ranges and arithmetic are in `checks.json`; they do not certify the analytic limit.

The parent's subsequent transpose shortcut is verified separately in `transpose_reduction.md`: linear HS transposition and the sign-flip permutation identify the right compression with the left compression for U^T. The note makes the reusable parametrix hypotheses explicit and verifies all of them under transposition. This is a shorter alternative proof of the right step; independent review of the extension is still pending.
