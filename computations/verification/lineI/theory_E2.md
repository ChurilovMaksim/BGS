# Line I, step (3): (E'') as an off-diagonal problem — what was tried, what holds

Notation: z_nu = (nu+i)/2h (nu mod 2h) on SL2(Z)\H, C(k) = sum_{n,n'} Phihat(n) conj(Phihat(n')) 1[P(n)-P(n') ≡ k mod 2h],
so that (Parseval) C(k) = (1/2h) sum_{nu mod 2h} |Z_nu|^2 e(nu k/2h)  and  sum_k |C(k)|^2 = (1/2h) sum_nu |Z_nu|^4.

## I5 restated (exact) [P]
For f on SL2(Z)\H with Fourier expansion f(x+iy) = sum_k c_k(y) e(kx):
  sum_{nu mod 2h} |Z_nu|^2 f(z_nu) = 2h sum_k C(-k) c_k(1/2h) ... (only k ≡ P'-P mod 2h survive; c_0 sees the diagonal).
For a Maass cusp form f_j (Laplace eigenvalue 1/4+t_j^2): c_k(y) = rho_j(k) sqrt(y) K_{it_j}(2 pi |k| y), so only |k| ≲ 2h(1+|t_j|)
contribute (K decays exponentially), and the diagonal (k=0) is invisible.

## Route A: Deshouillers–Iwaniec large sieve for Maass coefficients  -> barrier [P]
DI: sum_{|t_j|<=T} |sum_{|k|<=N} a_k rho_j(k)|^2 / cosh(pi t_j) << (T^2 + N^{1+eps}) sum |a_k|^2.
With a_k = C(k) K(...) and N ≍ 2h this gives, for S_j := sum_nu |Z_nu|^2 f_j(z_nu):
  sum_{|t_j|<=T} |S_j|^2 << h^{1+eps} * sum_nu |Z_nu|^4.
(E'') needs S_j = o(m h).  Even if the fourth moment were exactly RMT-sized on the bulk, sum_nu |Z_nu|^4 ≍ m^2 h, the bound is
h^{2+eps} m^2 versus the needed o(m^2 h^2): it misses by h^eps, and the resonant residues (|Z_rho|^4 ~ mu^{4m} ≫ h^2) make the
unrestricted fourth moment exponentially too large.  So the large sieve cannot give (E'') even on spectral average without a
power-saving fourth-moment input that RMT itself says is false.  This is a genuine barrier for Route A, not a technical gap.

## Route B: Kuznetsov / Kloosterman  -> same l^1 obstruction [P]
Opening rho_j(k) via Kuznetsov turns S_j into sums over Kloosterman sums S(k,k';c) weighted by C(k)C(k'); Weil's bound saves
sqrt(c) but the weights must be bounded in l^1: sum_k |C(k)| <= (sum_n |Phihat(n)|)^2 = (sum_j |J_j(1.8)|)^{2m} ≈ 2.36^{2m} = 5.57^m,
against the target m h ≍ 2.414^m.  Exponential loss; no cancellation among the Phihat weights is exploited.

## Route C: Bowen–Margulis / closed geodesic of the Pell unit -> wrong measure [assessment]
The points z_nu lie on ONE closed horocycle of length 2h (not on the closed geodesic of lambda); their unweighted equidistribution
is classical (Zagier/Sarnak, rate h^{-1/2}).  The geodesic of lambda governs the cyclic structure of P(n) (P ≡ y' Nm(alpha_n) mod h),
i.e. the transfer-operator side, which we already use (G2 law).  The weighted measure |Z_nu|^2 delta_{z_nu} is not invariant under
any unipotent/diagonal flow, so Ratner/Margulis-type or effective-mixing theorems do not apply to it.

## What CAN be said rigorously
(i) Prop I8 (one-sided reduction) [P]. Since F >= (1/phi) sum over resonant residues of |Z|^2,
  W'_m >= -RMT_m (1 - N_res/phi) + (1/phi) sum_{rho, d incl.} Dev_d(rho),   Dev_d(rho) := sum_{nu in M_d(rho)} (|Z_nu|^2 - |Z_rho|^2/d^2).
  So the LOWER half of R' (W' >= -o(m)) is exactly the statement that the bulk is not much BELOW RMT plus dilation-deviation control;
  W'/m >= -4 + (1/(m phi)) sum Dev holds unconditionally.
(ii) Prop I2' + certificates give the square part of Dev_7 exactly and rigorously small (step 2).
(iii) Positive-density / average-over-m versions: no unconditional statement obtained.  Every route needs either the fourth
moment of the bulk (A), l^1 control of Phihat (B), or invariance of the weighted measure (C).

## Halo near theta = ±1/2 (8|b) — quantified [N]
Contribution of |theta - 1/2| <= 0.1 to W'/m: +.073, +.068, +.062, +.048 (m = 11..17); in F units (times m): 0.80, 0.88, 0.93, 0.82.
By e = b - 4|a| (q=4 family, |e| <= 40): +.047, +.115, +.071, +.050 W/m (m = 11, 13, 15, 17); q=8 family: -.008, +.033, +.024, +.009.
Per-residue excess at fixed e grows (e=8: 4.3, 6.1, 9.3, 12.6) but the counts at fixed e also grow (~2.2x per Δm=2) while the
SUM stays O(1) in F units: halo = O(1) in F, hence contributes O(1/m) -> 0 to W'/m, consistent with R'.  Exact halo formula:
Z(nu_rho + delta) = Z_rho sigmahat_rho(delta) (Prop I1); a closed-form law in (e,b) was not found (not a 1/d'^2 law).
