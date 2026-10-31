# NOTES_N8 (Line N8), started 2026-10-31 21:33 UTC+5
Sat Oct 31 21:37:09 +05 2026
- n8_cert.py validated: fam (t0=1/2,e=2) reproduces N6 r_A,r_B: Re w in [2.8837e-4,3.9878e-4] [CA] (slightly wider than N6 due to window). near0 (t0=0,e=2sqrt2, k even): Re w0 in [2.3588e-5,3.6143e-5] > 0 [CA] -> droppable (k even). Matches e_isodepth sg=-1 value conj. 
- n8_cert sg convention = e_isodepth sg=-1 (conj). Added KPAR (k parity) seeds from Lemma P'. Batch1 launched (fam/near0 k odd + 14 small classes x 2 parities).
- K60 p47 data: Re<0 small-depth classes total |r| = 1.7e-7 (base 1/4), 1.1e-8 (base 0) vs Re w* 3.4e-4.
Sat Oct 31 21:41:05 +05 2026 
- Parity: fam_k1, near0_k1, q_3_0_k1, q_5_1_k1 give endpoints identical to k0 to ~1e-15 [CA]: w(z,e) independent of k mod 2 for these classes.
- r_other.py [P+CA]: Bop (twist-indep ||L_{a,tau}||) <= 40.849; R2'(a0)=369.4, R2'(a2)=R2'(a6)=739.9 (Riesz on |z|=1, sup_n||L_a^n||<=R2'); sector-4 R2'=3224.84.
  Other-sector ratio (3 sectors, family windows KK=18) <= 1e-6 Re w*_lo for p >= 485. 
- Riesz-Dunford: L^n(I-Pi) = (1/2 pi i) oint_{|z|=1} z^n (z-L)^{-1} dz => sup_n ||L^n(I-Pi)|| <= R2' (r2=1 in Line F cert). This is the missing justification of the 'coll' term [P].
- q_propx2.py (class version, conservative s=|zeta|max/b, L_e window shift): fam p0=1169 (conservative; N6 exact-b gives 1165), near0 E<=1e-6 at p0=1201 -> Re(Zhat/Z) >= 2.2650e-5 > 0 [P mod X' + CA]. q_3_0: |w|<=4.467e-7 (+E 1e-8 for p>=1237); q_5_1: |w|<=6.147e-8 (p>=1205).
Sat Oct 31 21:53:47 +05 2026 batch1 done (16 classes x 2 parities). Positive: fam, near0, (1±2√2) both bases. Absolute total 1.215e-6 (0.42% Re w*_lo). q_propx2 p0 <= 1289 (tau=1e-9). REPORT_N8.md written. Referee N7 report not landed; interim ref_robin16 says p>=498 (vs 339).
