# Author self-audit and independent-review handoff

This is a separate self-audit of the current candidate, not independent acceptance. The previous left-overlap theorem's acceptance was reported by the parent; its frozen file remains unchanged. No agents or broad searches were started in this turn.

## Checked mathematical transitions

1. **Right orientation.** Derived `Tr(A_c A_d* U^r)` directly. Its right frame has `C_B=L_(B*)C`, and the crucial covariance is with R_U. Exact Gaussian-rational fixtures verify this covariance and reject its false left-multiplication replacement. The row-minus-column slice label is explicitly distinguished from the source's opposite charge label.
2. **Right phase.** The new internal chain starts at x_0+d and ends at x_0+c. The exceptional vectors are (-e0,0) at r=1 and (-(5/4)e0+(1/4)e_(r-1), -(1/4)e0+(1/4)e1) at r>=2. They differ from the left vectors. Direct quadratic elimination gives `(A_r+1)/(4B_r)`; the r=2 value is 3/16. Branch and alias affine terms do not change a quadratic Schur Hessian. The actual perturbation uses the full sparse Hessian row sum, not entrywise closeness multiplied by dimension.
3. **Analytic inheritance.** The existing reviewed Poisson/stationary-phase/TT* argument is reused only after verifying the right phase's global concavity and reduced mixed derivative. All branches and aliases remain. Each r is fixed. The composition result with growing j uses a fixed block length L and then a double limit, not uniform stationary-phase constants for growing r.
4. **Uniformity over B.** B can depend on N, the other gap lengths and all other Kraus labels. It must remain fixed while the distinguished coherent gap is summed. Grouping the full composition sum has exactly this property; a prescribed collection of gaps all changing together would not.
5. **Composition boundaries and multiplicities.** All weak compositions occur, including zero gaps. The root/marked-insertion count is m/j, with binomial normalization `binom(m,j)`. It does not use a presumed rotation orbit size. Prefix summation by parts produces an explicit endpoint term; the fiber count in (13) is checked exactly. Raw coefficients and normalized averages are kept distinct.
6. **Annealed extension.** The arbitrary bounded B_theta is placed inside a trace-norm duality bound. No independence from theta is assumed. The finite-rank approximation remains uniform after V_theta because V_theta is unitary. A smooth majorant on the whole integer line handles gaps near zero; negative auxiliary coherent powers are unitary conjugations and keep the physical full trace nonnegative. This bounds the original nonnegative-gap sum without changing its definition. The extension is derived here, not misattributed to the earlier consecutive-block theorem.
7. **Three-pinch tail.** The ordinary superoperator S2 bound is C_flat N, not N^2 or a normalized trace. Collective compactness gives a fixed-rank singular-value cutoff, hence S3^3=o(N). Three Schatten factors and the remaining operator-norm contractions control any number of separated insertions. Every identity-sector contribution is exactly 1 and is retained. Uniform singular values of V_theta D are sufficient; occupation-uniform strong classical convergence is not asserted.
8. **Final normalization.** Positive binomial weights sum to at most one. Low orders 1,2 are controlled after the compact time sum; all orders >=3 have one pointwise bound. Therefore no factor equal to the number of orders multiplies an unspecified o(1). Signed occupation subtraction is performed between the two complete sums. The zero-insertion term survives with z^m and remains unknown at the undamped endpoint.

## Highest-value independent audit questions

- Recompute the right phase, its boundary vectors, and the general Schur mixed derivative, without importing the left conclusion.
- Check the fixed-B quantifier and how it is used when the other lengths and Kraus labels are frozen.
- Verify both normalization factors in (10), and independently reconstruct the decreasing-weight endpoint count in (13).
- Check the bounded-factor annealed lemma with theta-dependent B, including the positive extension to negative auxiliary run lengths.
- Verify the Schatten-3 tail's normalization and identity-mode subtraction. Test whether the claimed uniformity over all insertion orders needs any extra factor; the author finds none for complete unmasked words.
- Confirm that the binomial expansion conclusion does not remove Hamming/high-switch masks or determine the zero-insertion term. No derivative or deconvolution of a bare o(1) is allowed.

## Exact controls and their limit

`check_separated.py` uses non-assert failure checks. It verifies right-frame identities at N=3,5; rejects the wrong orientation; checks cyclic Hessians and perturbation envelopes for r=1,...,16; checks all rooted coefficients through m=8; verifies the fiber endpoint identity in three bands; and checks the S2 normalization and small complete CP traces. Both normal and optimized runs are recorded. None of these finite checks proves the analytic N-limit. No proof-assistant, C++ or rescaled-tau claim is made.

## Execution state

At the parent's environment-disconnection warning, a real exec call read the saved proof and check report and wrote `environment_probe.txt` successfully. No tool reconnection or source download was attempted or needed. The current proof is durable in this task directory.
