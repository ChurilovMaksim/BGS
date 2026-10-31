Sun Nov  1 00:46:00 +05 2026 N14 start
2026-11-01 00:55:09 +05 N14 started: fastops.py (block-sparse, validated 2e-26 vs dense), digits.py (eps-chain integer letters E_k; types odd=[1], sq2=[1,-1], two=[1,0,-1], 2sq2=[1,0,1], four=[1,-1,0,1,1]); a_enum.py 0..12 running (exact class enumeration e=2alpha, both bgs)
2026-11-01 00:58:53 +05 b_cp.py: Perron matrix Y* of K singular; Y*+eps I certifies only 0.62; kappa_v with raw (c_n,M_n) scaling meaningless (|M_n|~1e16). -> b_cp2.py Neumann certificate, balanced N_n=c_nM_n/s. N13 referee landed (F1 Lemma D Gamma^2/e^{Gamma sigma}; F2 4.26e3; F3 replay radii 2.9x/G vacuous G>=14).
2026-11-01 01:00:27 +05 c2_mid.py (N13-F3 fix): float mid + rigorous H-norm a-posteriori error, radii flat 2e-9..8e-9 for G=5..15 (arb replay: 59% at G=15). Full 1560-job run started.
2026-11-01 01:04:05 +05 b_cp2 rb=0.30 m=120 CERTIFIED [CA-fp] margin 3.7e-6 vs errors 7.3e-13; rho_true<=0.3003; letterwise CP (Gram/AM-GM) kappa_v up to 38 => useless for collisions. g_carry E=1 (phases kept): rate 0.272551 = rho(K) [N] (collisions don't change rate; prefactor: (0,0) share 0.235). a_post (j<=11): A_bad 0.7e-6..3.7e-6 (g0=2..6) <= 0.6% budget; C_emp<=4.4e-4 vs C_needed(J0=12) 0.04-0.11.
2026-11-01 01:09:05 +05 c2_mid done: f_post2 coded delta_int <= 5.14415e-7 [CA-fp core functional] (mid 5.14405e-7); shorts: 27 model relabellings (+4 to 'four'), 96 genuine classes sum|w|_up 9.970e-7 (x2 per site 1.99e-6). NOTES_N13/SHA256_N13 rehashed (27 OK).
N13/logs/d_decay_G16.json abs tail 5.759e-09 max sum_cls 0.249
N14/logs/d_decay2_G16.json abs tail 1.556e-08 max sum_cls 0.691
2026-11-01 01:24:23 +05 REPORT_N14 drafted (sections 0-5)
2026-11-01 01:40:56 +05 final: a_cert all 5109 classes (g0=4: 2.03157e-6 certified); b_cp2 rb=0.28 m=400 certified (rho_true 0.28028); g_carry E=2 rate 0.272551 share 0.150. Arb replay N13 at 589/1560, still running (not hashed; live).
