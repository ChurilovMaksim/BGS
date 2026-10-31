# NOTES N9 (started Sat Oct 31 21:56:58 +05 2026)
Sat Oct 31 22:08:40 +05 2026
- Plan analysis: op*HS*HS with box (Selberg/Poisson) averaging: A and B cores share zeta (zeta_B=-eps^{-1}zeta_A) => joint twist seq is base-eps; 1-D near-collision heuristic rate ~A(0)^2/eps = 5.42/2.414 = 2.25 per letter > 1.481 needed. Separate-core Holder variants give 1.855 per D >1. => R1 via HS moments looks blocked [H].
- NEW concern: composite (multi-bump) classes zeta = zeta_a + lam^g zeta_b: by rank-one collapse w(comp) -> w_a*w_b-type, not decaying in g; #such classes ~ k => sum_nonfam |w| grows linearly in k ('dilute gas'). Testing with n9_cert on alpha = 1 + s sqrt2 lam^g (base 1/4) g=1..6.
Sat Oct 31 22:15:18 +05 2026
- Composite classes alpha=1+s sqrt2 lam^g (base 1/4) [CA] (logs/n9_cert_comp_*): |w| does NOT decay in g: g=3..6 all Re in ~[1.5e-9,2.1e-8], |w|<=2.4-2.7e-8 (rank-one collapse limit). Re lower>0 for g=3..6 (these are positive).  => #classes with |w|>=c grows ~linearly in k ('dilute gas') [CA evidence + H].
- Parent steering 22:11: (1) N8b erratum: lambda has 4 fixed points (sqrt2/8)O/O^vee; (2) other isotropic lines at composite h_p; (3) proper-divisor consistent classes are deep classes.
- a_bases.py: all 4 fixed points, coset e in -8z gbar + 2sqrt2 O. p=29: z in {sqrt2/8, 1/4+sqrt2/8} classes |w|<=1e-24 (tiny). MISSED by N7: z=0, e=4 (N=16): w=1.041e-6-3.116e-6i (|w|=3.29e-6, 0.83% of |w*|); z=0,e=4sqrt2: 1.8e-8. N7 base-0 list used alpha odd only; correct coset for z=0 is all of 2sqrt2 O.
Sat Oct 31 22:17:05 +05 2026
- [CA] z=0,e=4 (missed by N7): Re w in [3.55e-9, 2.079e-6] >0 (droppable), |w|<=4.77e-6; parity k1 identical. z=0,e=4sqrt2: |w|<=4.24e-8, Re indeterminate.
- a_bases p47: z in {sqrt2/8,1/4+sqrt2/8} classes |w| ~6e-39 (p29: 1e-25): exponentially decaying in p, no p-indep limit [N]; (s,qs) reps pair up (same points).
- 3-bump composites alpha = 1+lam^g1+lam^g2 launched (prediction w ~ w*^3, |w*|^3=6.2e-11, mult ~k^2/2).
Sat Oct 31 22:21:24 +05 2026
- 3-bump alpha=1+lam^g1+lam^g2 [CA upper]: |w|<=1.16e-9 (2,5), 7.6e-10 (3,7), 5.4e-10 (4,9); midpoint |rA rB|^3 ~ 6e-11 = |w*|^3 (multiplicativity, r_A(3b) ~ r_A(fam)^3 |0.0276| vs |rA| 0.0285).
- Referee N7 report landed (22:19 steering): F3 budget, F6 cross lines, F1, F8-F11; suggested route = Fejer/Selberg near-collision r2(eta).
- b_automaton.py: single core (base lam) rate 1.0511-1.0519 per letter [CA*] (=r2, <1.481 OK). Joint A+B cores of the same class (base eps, zeta_B=-eps^{-1}zeta_A) rate 2.32569 per letter [CA* upper, N lower via power iteration] -> per lam-step 5.409 vs needed 1.481^2=2.193. Referee route fails as a majorant for the period product.
Sat Oct 31 22:22:47 +05 2026 REPORT_N9.md and REPORT_N7_v2.md written. Hashing.
