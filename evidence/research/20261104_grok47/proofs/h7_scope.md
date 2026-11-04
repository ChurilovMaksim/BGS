# Scoping note for H7* at the three included crossings

This note is the registry-ready statement of scope. It does not assign a claim id. `record/claims.json` was not edited. The certificates it quotes are in `proofs/h7_multidisc.md` and `logs/h7_multidisc_enclose.json`. The aggregate comparison is in `proofs/h7_lin.md`.

H7* (BGS-TRACE-305) asks for \(|\mathrm{Lin}_d|\le\varepsilon_d|Z_\rho|^2/h_p\) with \(\sum\varepsilon_d\le\kappa_0\), over the included levels below \(L_{\mathrm{fl}}\) other than \(h_p\) and \(e\cdot h_p\). The draft's phrase "cross-correlation growth \(< T'=1.42785\)" is a sufficient majorant of that sum, obtained by replacing \(\sum_\beta\kappa_d(N\beta)\hat Z(\beta)\) with \((\sum|\kappa|)\max|\hat Z|\). It is not the closure condition.

**The sufficient per-orbit reading fails on the finite section at the three included levels.** The section is the multi-disc vertex operator of BGS-TRACE-223 compressed to centres \(|c|\le 3\), modes of degree \(<40\), and letters \(|n|\le 16\). In sector \(a=0\) the certified per-step rates are

| \(d\) | factorisation | \(p\) | \(\beta\) | lower endpoint |
| --- | --- | --- | --- | --- |
| \(3437426497\) | \(457\cdot 7521721\) | \(19\) | \((-208,0)\) | \(1.458772466390154\) |
| \(24061985479\) | \(7\cdot 457\cdot 7521721\) | \(19\) | \((227,227)\) | \(1.5119805975188876\) |
| \(2735635252619983\) | \(7\cdot 13921\cdot 28073057689\) | \(29\) | \((-89,0)\) | \(1.4686852948918232\) |

Each lower endpoint lies above \(T'=1.42785\). Each conductor divides \(K_p\), is not \(h_p\) and not \(e\cdot h_p\), and satisfies \(d^2\le h_m\). Decreasing a printed endpoint by \(10^{-12}\) leaves the gap positive. This is a statement about that finite section. It is not a statement about the untruncated monodromy: the one-step tail is \(<9.65\cdot 10^{-5}\), and the product of \(57\) or \(87\) such steps was not bounded by a useful multiple of that constant.

**The aggregate is open.** The closure condition is a bound on \(\sum_{\beta\not\equiv 0}\kappa_d(N\beta)\hat Z(\beta)\), not on one orbit. That sum was not enclosed at these three conductors. One \(\lambda\)-orbit, including each of the three above, is a single term of the sum. `proofs/h7_lin.md` encloses those terms and compares them with \(\varepsilon_d|Z|^2/h_p\); they do not decide the sum. H7* is not shown to hold at these levels, and it is not shown to fail.

**Theorem v5 is unaffected because \(p<1409\).** Theorem R♯-mod v5 (BGS-TRACE-325) concludes that frozen R′ fails along \(m=3p\) for \(p\in\mathcal{P}\) only if H0, H1, H6 and H7* hold, \(p\ge p_{\mathrm{thr}}\), and \(\mathcal{P}\) is infinite. The draft's threshold is \(p\ge 3307\) under H1 as stated, and \(p\ge 1409\) if \(C\le 8.8\cdot 10^{-4}\). Both \(19\) and \(29\) lie below \(1409\), and below \(3307\). A failure of the sufficient reading at these primes does not fire the implication, and it does not remove H7* from the hypotheses at \(p\ge p_{\mathrm{thr}}\).

Frozen R′ (BGS-TRACE-206) stays open. No claim row was changed.
