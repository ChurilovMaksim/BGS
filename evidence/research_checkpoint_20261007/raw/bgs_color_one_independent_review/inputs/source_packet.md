# One-color phase CFT: frozen source packet for fresh audit

7 October 2026. Read-only canonical base observed at d37c92e563d10d25bb1d6ab85bedffc1f160f773. All work here is outside the canonical BGS repository.

## Exact claim to audit

For each independent coordinate phase, the color group is U(1), hence N_c=1. Physical site dimension M, the number of factors U(1)^M, and the retarded/advanced bosonic flavor counts are separate parameters. Test the proposed standard flat-measure superintegral for the one-site ratio

E[(1-c ζ)(1-d ζ^-1)/((1-a ζ)(1-b ζ^-1))] = 1+(a-c)(b-d)/(1-ab),  |a|,|b|<1.

Let Z=[[z,α],[β,w]], tilde Z=[[bar z,γ],[δ,-bar w]], with four independent odd variables and |z|<1, w in C. Set A=diag(a,c), B=diag(b,d). The proposed bulk is

I_bulk[F] = π^-2 ∫_{disk×C} d²z d²w ∂_odd { SDet(1-tilde Z Z) F },
F = SDet^-1(1-tilde Z A Z B).

Use the source's Berezin ordering, not an inferred positivity measure.

## Pinned primary references and exact PDF locators

1. Martin R. Zirnbauer, *Color-Flavor Transformation Revisited*, arXiv:2109.10272v1 (21 September 2021), local sources/z21v1.pdf. Section 2.4, printed pp.12–13, equations (2.55)–(2.58): standard type-A formula, square-flavor stable range N_c≥2n_b. Section 4, printed pp.26–34: pair case m_0=n_0=m_1=n_1=1. Equation (4.21), p.28: flat bulk normalization is zero at N_c=1. Equation (4.27), p.29: a quadratic fermionic moment diverges. Equations (4.28)–(4.31), p.30: explicit bulk-plus-surface replacement with normal radial derivative. Section 4.4, (4.39)–(4.54), pp.32–34: reproducing-kernel proof. Section 4.5 gives a different random-phase representation, not a microscopic uniformity theorem. The HTML rendering renumbers equations; these locators refer to the pinned PDF.

2. H. A. Weidenmüller, *Massive Modes for Quantum Graphs*, arXiv:1812.00655v1. Section 2, equations (3)–(9), printed pp.3–4: independent directed-coordinate phases, one 1|1 Z matrix per phase, disk/plane body, flat integration. The text immediately after (9) calls this an exact representation. No one-color boundary functional is displayed there.

3. Gnutzmann–Altland, arXiv:nlin/0508009v1: equations (41)–(42), printed p.6 explicitly specify one color and F flavors and impose unit normalization on the standard measure; actual graph application has F=4 (direction and time reversal). Appendix C, printed pp.12–14, uses the coherent-state projector/invariance/normalization argument without a one-color boundary prescription.

4. Pluhař–Weidenmüller, arXiv:1407.1148v2: equations (30)–(35), printed pp.10–11, use one U(1) phase per undirected bond; directions and replicas are flavor indices. Equation (31) has SDet power one and explicitly flat Berezinian. There is no explicit one-color boundary completion in this step. Its domain sentence following (33) puts a bound on the FF block; do not silently use that typo as the intended BB-domain contract.

5. Zirnbauer, *Supersymmetry for systems with unitary disorder: circular ensembles*, J. Phys. A 29 (1996), 7113–7136, source z96.pdf: (3), printed p.7116, and its footnote acknowledge that the flat Berezin measure is only local and has a global anomaly. This caveat is not an explicit boundary-source estimate for the coordinate-phase graph model.

PDF hashes are in sources.json. The critical correction page was rendered and visually inspected as sources/z21_boundary_page.png.

## Independent elementary discriminator

At c=d=0, A Z B has only the BB entry ab z, so F=(1-ab|z|²)^-1 contains no odd variables. Put x=|z|², y=|w|². Source (4.16) gives the top odd coefficient of SDet(1-tilde Z Z) as (1-y)/(1+y)^3. Thus

I_bulk[F] = [∫₀¹ dx/(1-ab x)] [∫₀∞ (1-y)/(1+y)^3 dy] = 0.

The actual U(1) average is 1/(1-ab). This holds strictly inside the source domain and is already 1 versus 0 at a=b=0. It is a counterexample to the uncorrected integral identity, not to universality or to the scalar coercivity inequality.

In the corrected source functional, the surface normal derivative is multiplied by S_0=(1-|z|²)/(1+|w|²). Its derivative acts on S_0 at |z|=1; the term differentiating F is killed by S_0=0. The surface evaluation therefore multiplies I_surface[1]=1 by F(|z|=1)=1/(1-ab), exactly repairing the source-dependent discrepancy.

## Questions for fresh audit

- Reconstruct the source conventions and the one-site ratio directly; confirm the source placement and all boundary factors.
- Check whether the graph sources supply a nonliteral invariant-integral prescription that changes the conclusion above. Do not identify a formal global-anomaly caveat with a proved bound.
- For nonzero c,d, retain a common w-plane cutoff before adding bulk and surface; individual terms can diverge.
- Distinguish the repaired finite-N identity from any uniform-in-M estimate at radial sources exp(-s/M).

The independent full-source calculation is being finalized separately. No canonical changes or publication are authorized by this packet.
