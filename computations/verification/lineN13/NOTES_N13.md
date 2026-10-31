Sun Nov  1 00:03:01 +05 2026 N13 start
00:09 launched b_arb.py (B: arb adapted-norm checks)
00:10 c_replay tested (odd single |rA|=0.302087 matches N12 float; 6.9 s/job shared); run_C.sh queued after b_arb (1360 jobs, resumable)
00:14 finding: N12 e_tailH best cut was t=0 (Qt Phi=0 => K~1e-16), so its tail = pure assumption dev(G0+m)<=dev(G0)kap^m -> N12 tail claim is [H]; d_decay.py written (proof via midpoint cut, single-chain constants)
00:22 b_arb: Mn_H all ok (61), Lip_H<=167.213, L2<=4977.59, Nsum<=8.3288, V1 cond<=21.103, V2/V3a/V3b ok eta=1e-6 [CA]. K-block quad cert infeasible -> killed; 2x2 route next. Steering: N12 referee landed.
00:22 replay running (pass 1: 1360 coded+singles); run_C2 queued for 200 short types (F1)
00:39 d_decay G0=16 done: max rel class-dev sum 0.249 (four-four), odd-odd win dev bound 5.0e-4/1.7e-3 at G=16, rate ~0.41/step; abs tail G>=16 <= 5.76e-9 [P + N constants]. Launching G0=10 for validation vs d_merged measured devs
00:39 replay cross-check: midpoint sums equal N12 float (4.4263e-7 on 128 pairs); arb upper 6.9e-7 (ball radii). e_shell MC launched (j=6,10,14,18; 24 samples)
00:41 g_K: rho(K)=0.27255 (iid-uniform second-moment rate) < lam^-1/2=0.414 [N]
00:42 lambda_cert copy: docstring fixed (charge = 200|c16| = 4.4e-7), per referee F4
00:43 REPORT_N13.md written
00:44 hashes written (replay files excluded, live)
