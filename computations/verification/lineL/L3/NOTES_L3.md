# NOTES_L3
- start: Line L3 (inherited-level folding; recursive structure across divisors; numerics).
- 15:10 Structural facts: (S1) P(n)=y'N(alpha_n)-2h sum y n n exactly (TRACE-212 congruence) => A(x)=B_m(x)chi(x), B_m = law of walk positions, Bhat_m(y)=prod_j g(Tr lam^j y), g(t)=sum ghat(n)e(nt)=exp(i1.8cos2pi t) unimodular.
  (S2) CRT: for q||h, chi = chi_q * chi_{2h/q}; on x in q-ideal chi_q=1 => A(ideal)=sum_{x in ideal} B(x) psi_{2h/q}(x)  (complementary level).
  (S3) inherited q|h_p: h_{3p}=h_p(4h_p^2+3); B_{3p}=B_p*lam^p B_p*lam^{2p}B_p, mod 2h_p = B_p^{*3}; but phase has a level-(4h_p^2+3) factor that does not fold => Gauss-side folding blocked.
  (S4) transfer side: rank-p level => twist period p => Zhat^{(3p)}_beta = c*Tr[(I x |0><1|) Pi_beta^3], Pi_beta = p-step twisted operator (m=3p automaton constants). Test numerically vs Zhat^{(p)}.
  (S5) exact line quadrature: (1/q) sum_{beta in l(q)} F(beta/q) = sum_{gamma in q-ideal} c_gamma(F); frequencies of norm<q integrate exactly. Orbit sums of length m have frequencies of norm up to lam^m >> q: beyond-Ehrenfest-time correlations not controlled (FND minimal-period scarring regime).
  (S6) [P] cusp-excursion lemma: isotropic beta!=0: no run longer than log_lam q + O(1) with all twists in [-eps,eps]; non-iso: 2 log_lam q + O(1).
- 15:40 inherit tests done (p=5 q=41, p=7 q=239): spectral identity Zhat^{(3p)}=c Tr[R Pi^3] to 1.7e-13; Zhat^{(p)}^3 does NOT match (m=p automaton case differs). Excursion check consistent with Lemma E. Trivial unimodular bound |A(q-ideal)|<=2h/q [P] reproduces 1.88^m. Writing REPORT_L3.
- 15:55 REPORT_L3.md written; manifest next.
