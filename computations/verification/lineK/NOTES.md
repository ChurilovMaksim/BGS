# Line K notes (started 2026-10-31 09:59 +0500)
Goal: prove H♮ (or replacement) -> unconditional refutation of frozen R′ along m=3p; or structural theorem. Inputs: Line J v2, J3 v2 (../bgs-lineJ).
- 09:59 Plan after analysis (see REPORT §1 for reasoning):
  K1 coset/light-cone formula for prime levels (structural form of O♮): cross_q = 2Re(Zbar D_iso) - (2/q)Re(Zbar E_b), D_iso = excess mass of words with
     lambda-adic position x_w = sum n_i lam^i in the prime ideals q|q (folded polynomial P_w(l)=0, l primitive p-th root mod q).
  K2 large levels d >= L_m ~ (mu*^2/xi)^{m(1+eta)} negligible by positivity Dev_d >= -n_d|Z|^2/d^2 + Euler product over q >= 2p+1 [P+CA].
  K3 remove H_arg: rational case via Dirichlet + sieve (Kanold-type) gap bound + finite exact gap check [P + finite computation].
  K4 BGK range q <= p^C: equidistribution of cosets of the order-p subgroup + order-free norm product bound; needs avg norm rate < 1.2836 (test [N]).
  Averaging-over-p idea (owner idea 1) evaluated: fails as a standalone tool because W′_A and Q are uncontrolled from above (only one-sided info); recorded.
- 10:01 K3 DONE: H_arg removed. code/k3_harg.py: exact gap check b' in [447,6000] (fails only b' in {504,560,616,840}, none compatible with the certified enclosure of arg xi/2pi), sieve bound covers b'>2644. => S+ infinite unconditionally (Vinogradov if irrational; Dirichlet if rational).
- 10:10 K2 DONE (honest, weaker than hoped): code/k2_large.py (arb). Dev_d >= -n_d|Z|^2/d^2 + Rankin over primes q>=2p+1 (worst case omega = log h/log(2p+1)).
  Result: threshold L_m = (mu*^2/xi)^{m(1+eta_m)}, eta_m -> 0 like ~1/log m [P given Z-bound]; but L_m < sqrt(h) only from m ~ 1.7e9 (S_Z=1e14); eta=0.59 at m=501. So K2 is asymptotic only.
- 10:11 K4 launched: code/k4_normrate.py (block op-norm rates R_k over iid tau, toy Galerkin b=8). log -> logs/k4_normrate.log
- 10:17 K1 identity verified (k1_cone_check). K4b cat-map block rates: R_36=1.131<1.2836 [N]. REPORT.md written (Theorem K: S+ unconditional; H♮ -> H♮_mid).
