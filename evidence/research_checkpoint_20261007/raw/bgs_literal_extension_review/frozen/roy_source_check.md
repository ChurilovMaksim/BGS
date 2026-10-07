# Roy quantitative-source application check

Checked 7 October 2026. Source: Damien Roy, arXiv:1607.00579v1, posted 3 July2016,
“Une version effective du théorème de Lindemann-Weierstrass par des méthodes
d’indépendance algébrique,” Theorem1.1, printed page2.
Primary URL: https://arxiv.org/pdf/1607.00579v1 . Existing registration is
EXT-ROY-2016; its prior frozen application is copied in
inputs/frozen_effective_gap_floor.md. The precise primary statement was
re-read through the web PDF tool, not inferred from a search snippet. No
authorized local primary PDF copy was found by the bounded workspace search.

The theorem permits complex algebraic exponents, with rational linear
independence, a conjugate modulus bound c, integral denominator q, and field
degree d. For r exponents and integer polynomial degree D, height H, it gives
the lower bound H^(-3dS^r)exp(-(cqS)^(18S^r)), S=6dr(r!)D.

New application: r=1, nonzero exponent beta=i*alpha where alpha is a root
of an integer polynomial of degree<=L and height<=h_L; d<=2L,
c<=2h_L, q<=h_L. Use polynomial Z+1, D=H=1. Thus S<=12L and
the bound is at least exp(-(24L h_L^2)^(216L)). Root scaling proves q*beta
integral. The nearby-root argument is fully written in growing_word_window.md.

The mapping is a formal new application of the registered theorem. It is
qualitative only after its displayed enormous effective lower bound is
inserted; no microscopic spectral estimate is inferred. The application and
analytic continuation still need independent review. No novelty claim.
