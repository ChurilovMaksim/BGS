# M1 note — cross terms in the historical Möbius-fiber assembly

A clean Python implementation and an independent C++20 implementation reproduce the historical fiber assembly and agree on the missing cross energy.

For `N=53,K=13,m=4`:
- diagonal raw energy: `934952569968`;
- cross raw energy: `7805905040`;
- cross/diagonal: `0.0083489851`.

For `N=199,K=11,m=18`:
- diagonal raw energy: approximately `1.1635012135e16`;
- cross raw energy: approximately `3.1752387617e14`;
- cross/diagonal: `0.0272903777`.

A substantial part is trivial/nontrivial coupling; the correction is not confined to nontrivial/nontrivial pairs.  Therefore the historical diagonal-only identity is false for this assembly.

The code/result live at:
- `experiments/m1/cross_term_energy.py`;
- `src/cpp/m1/cross_term_energy.cpp`;
- `results/diagnostics/m1_cross_term_energy.json`.

## Fixed Fourier normalization and exact cross-Gram formula

Use the unnormalized finite Fourier transform

`f_hat(xi) = sum_d f(d) e_N(-xi d)`,

with inverse `f(d)=(1/N) sum_xi f_hat(xi)e_N(xi d)`.  Then

`<f,g> = (1/N) sum_xi f_hat(xi) conjugate(g_hat(xi))`

and `hat(f*g)=f_hat g_hat`.  Hence, for `F_tau=A_tau*A_tau`,

`G_(tau,sigma)=<F_tau,F_sigma>`
`=(1/N) sum_xi A_hat_tau(xi)^2 conjugate(A_hat_sigma(xi)^2)`,

and the entire energy is exactly

`E=(1/N) sum_xi |sum_tau A_hat_tau(xi)^2|^2`.

This is the correct starting point for cancellation.  It says that the proof
should control the **summed squared Fourier amplitudes at each frequency**, not
bound each twist energy separately and add the bounds.  The Python diagnostic
now evaluates the time-domain and Fourier-domain formulas independently; at
`N=53,199` they agree to relative floating-point error of order `1e-16`.
