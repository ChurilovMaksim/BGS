# NOTES_N12
Sat Oct 31 23:08:05 +05 2026 start
Sat Oct 31 23:13:09 +05 2026 power-bound cert: C_L(0.8)<=93.0 (vs R2'=15206), C_L(0.85)<=82.8; singles reproduce w*,c0,c4; c_pairs A/B/C G<=30 launched
Sat Oct 31 23:15:19 +05 2026 c_pairs: decay ~0.38/step, odd+sq2 G=6 9.07e-3 matches N10 finite-p; launched d_merged all ordered pairs G<=34 (h=0,1)
Sat Oct 31 23:17:16 +05 2026 steering: adapted norm is the bottleneck for both gaps; make reusable
23:19 f_adapted: Stein/Lyapunov norm kap=0.45: cond=21.06, ||A0/s||_H=1, ||B||_H=0.449, Lip_H=167 (vs Lip_2=484, naive Cpow*2piN1/mu~6e6). [N] float
23:22 verify_adapted ALL_OK (V1-V3, eta=1e-8, Pert in H 2.1e-8). Slow twists: sector a at tau == sector-4 op at tau+(a-4)/8, so A0 serves all four slow fixed twists (b -> sector 4-8b). In-sector A(1/4) radius 0.877 (not slow). nproc=1: killed old e_tail, e_tailH G8/G20.
23:36 steering: N11 referee landed; apply F1,F2,F6,F3,F4,F7 as REPORT_N11_v2 section
23:36 lambda_cert.py archived (N11-F3): ReL_lo=6.23837e-4, with c16 charged x10: 6.23397e-4; bracket alone p>=75 (F4)
23:37 restarted d_merged with Gmax=16 (tail G>=16 covered by e_tailH)
23:37 quad_stepbound: Re(psi E1 Phi)=1e-16 (|mu| stationary); N_H(t)<=sigma2x2+L2 t^2/2 => N_H(t)<=1+3.19e3 t^2 for t<=1/256 (measured 602 t^2). D2 per stay ~ cond*prod N_H ~ 21*O(1).
00:01 g_dint: coded (n>=5) merged types 1350 explicit + adapted tail: delta_int ~ 5.1e-7 (ratio 8e-4 of ReL_lo) [N float]; n<5 'pairs' are single types/uncoded (dev up to 4.5e8 = relabelling)
00:01 REPORT_N12.md written
