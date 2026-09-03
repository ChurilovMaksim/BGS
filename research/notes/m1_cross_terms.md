# M1 note — from historical cross terms to the exact key-table collapse

## What the old diagnostic established

Independent Python and C++ implementations reproduced the historical Möbius-fiber assembly and showed that its diagonal-only energy decomposition was false: cross terms were nonzero at `N=53` and `N=199`.

That result remains a valid falsifier of the old proof mechanics. It is no longer the active M1 object, because the historical Möbius graph itself has now been shown to differ from the exact pair-key image.

## Fixed Fourier normalization

Use the unnormalized finite Fourier transform

`f_hat(xi)=sum_d f(d)e_N(-xi d)`

with inverse

`f(d)=(1/N)sum_xi f_hat(xi)e_N(xi d)`.

Then

`<f,g>=(1/N)sum_xi f_hat(xi)conjugate(g_hat(xi))`

and `hat(f*g)=f_hat g_hat`.

For any family of amplitudes `A_tau`, if `F_tau=A_tau*A_tau`,

`<F_tau,F_sigma>=(1/N)sum_xi A_hat_tau(xi)^2 conjugate(A_hat_sigma(xi)^2)`

and

`||sum_tau F_tau||_2^2=(1/N)sum_xi |sum_tau A_hat_tau(xi)^2|^2`.

This normalization is exact and remains valid.

## The stronger identity for the correct amplitudes

For the exact pair-key table, define

`A_(chi,psi)(d)=sum_{r:d_r=d} n_r chi(u_r)psi(v_r)`.

Double annihilator-character orthogonality then gives

`sum_(chi,psi) (A_(chi,psi)*A_(chi,psi))(t)=m^2 B(t)`

for every `t`, and therefore

`sum_(chi,psi) A_hat_(chi,psi)(xi)^2=m^2 B_hat(xi)`

for every frequency `xi`.

So the full cross-Gram problem **collapses exactly**. The quantity that must be estimated is not a sum of separate twist energies; it is the single coupled difference distribution `B(t)`.

The active Python verifier checks both identities through `N=199`. The C++ verifier repeats the test with direct DFT and direct circular convolution, independently of NumPy FFT.

## Consequence

The previous wording “find cancellation among cross twists” was one layer too early. The active problem is now

`Var_(t!=0) B(t)=O(K^2 N)`.

This is exactly equivalent to `std_(q!=0) Sigma_4(q)=O(NK)` by finite Fourier orthogonality.

The historical cross-term numbers are preserved in `results/diagnostics/m1_cross_term_energy.json` only to document why the old proof failed.
