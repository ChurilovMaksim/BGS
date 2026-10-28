# Kick-blind arithmetic spikes, 28 October 2026

**Claim:** BGS-TRACE-117. **State:** project proof. BGS-TRACE-005 and BGS-BGS-001 remain open.

## Result

For the maintained odd-dimensional family, with \(u_m+v_m\sqrt2=(1+\sqrt2)^m\):

1. For every odd integer \(n\ge5\), at \(N=u_n\), the cat-map propagator satisfies \(M_N^n=\zeta I\) with \(|\zeta|=1\), and \(L_N(M_N;1)\ge1-2n/N>3/4\).
2. For every odd integer \(n\) with \(5\le n\le201\), the fixed kick \(\tau=10^{-80}\) satisfies \(L_N(U_N;1)>3/4\).

The distance from either value to the CUE Abel number \((1-e^{-2})/4<1/4\) is greater than \(1/2\). The integer \(u_{201}\) has 77 decimal digits. Any effective statement that this distance is less than \(1/2\) for every odd \(N\ge N_0\) requires \(N_0>u_{201}\).

The one-term lower bound is still a contraction at \(n=203\) and no longer exceeds \(3/4\). That is a limit of the estimate. It is not a proved drop of \(L_N\), and it is not the \(N\to\infty\) question.

## What the proof uses

Phase polynomials of \(M_NW\) and \(W(C\cdot)M\) are identical over \(\mathbb Q\). For odd \(n\), \(C^n-I=2u_nP^n\), so \(N=u_n\) makes \(M_N^n\) scalar. Unitarity is the geometric sum for the quadratic phase. The kick comparison is the operator-norm majorant \(B=184981/160000\) of the 32 Fourier modes, the scalar bound \(\exp(y)-1\le y/(1-y)\), and one Abel term. The range \(7\le n\le201\) is reduced to a single rational inequality by monotonicity of \(\delta_n=2n/u_n\) and of \(\rho_n\). The endpoint \(n=5\) is a separate rational inequality. The recurrence used is \(u_{n+2}=5u_n+2u_{n-1}\), not the trace recurrence of \(C\).

## Certificates actually run

- `python3 computations/verification/kick_blind_spike.py --output evidence/executions/20261028/kick-blind-spike/receipt.json` passed. Exact `Fraction` arithmetic, 32 modes, norm through \(n=203\), 99 direct gaps, uniform comparison, sentinel \(n=203\).
- `g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -fsanitize=undefined computations/cpp/kick_blind_spike.cpp` and the resulting binary passed: `u_201_digits=77`, `odd_n=5..201 count=99`, `sentinel_203=below`. `__int128` is used for the Fourier field and draws `-Wpedantic` warnings; undefined-behavior sanitizer reported no failure.
- `lean formalization/Bgs/KickBlindRational.lean` with Lean 4.33.1 exited 0. The module is imported from `formalization/Bgs.lean`. Aggregate `lake build` was not run: the Mathlib cache is not present.

## Non-claims

No estimate of \(Y_{m,N}\), of a generic odd dimension, of any \(k>2\), or of \(\lim_{N\to\infty}\). The next obstruction is the signed cancellation of the kicked trace for odd \(N\) past this finite list, beginning with the dimensions where one return no longer forces the constant \(3/4\).
