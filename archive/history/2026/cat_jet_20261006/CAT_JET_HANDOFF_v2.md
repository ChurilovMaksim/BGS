# Subsequent cat-eigenspace and perturbation-jet results

This packet is separate from SPECTRAL_HANDOFF.md and the current all-odd common-commutant publication. Canonical files were not edited. No result here establishes full uniform kicked-U simplicity or BGS.

## Accepted finite first-order mechanism

For N35 and175, every actual M-eigenspace compression P A P is simple. The nonzero exponential discriminant and registered Lindemann–Weierstrass theorem give simple U at every nonzero real algebraic time. N175 extends the previously accepted finite list; N35 is an independent mechanism/control.

Source first_order_cat_split.md:
afdb9f47bc1d5823b922d8caaa1fc45d71d0b951c4adb6da7b07ca83bd1b2e17
Review /workspace/shared/bgs_cat_compression_independent_review/REPORT.md:
dd0c6aab34e877d5bca3d2c54bfdd67970798143b9999be3514c11bbc901f48d
Independent portable projector reconstruction and manifests are in that review directory.

## Accepted uniform cat multiplicity reduction

M_(5^e) is simple. For N=7*5^e, all M eigenspaces have size at most7, with exact parity distributions. This is an unperturbed-cat statement, not U simplicity.

Source uniform_cat_multiplicity_v2.md:
b6e219832f094136f0ca80201ae61f80a9d2435bebc59dd2f18163e3444c8e1e
Review /workspace/shared/bgs_cat_multiplicity_independent_review/REPORT.md:
c9ea460328b7e5aca3bd12378bc46e93edd0b9e5fc379ae114900409779ece5a
Final V2_BINDING.md:
dbe6d39858060fa0540dc551cb2ecf227bf476821ddff306dcb673a86f6ec2be
Manifest_v2.json:
b33a7ae03970f92a6838a421fb6640ca6cbf3878110aca2e9eb6b4ea7bfbe609
The v2 change corrects a matrix-factor valuation phrase; it does not alter the theorem. The underlying inert multiplicity-free fact has prior provenance in Kelmer, arXiv:0802.3237v2, Lemma3.2; kelmer_source_lead.md records the verified locator without importing a new dependency.

## Accepted failure of the uniform first-order criterion

For every e>=4, a sum of complete actual M eigenspaces of dimension7*5^(e-4) has zero A compression. The j=1 old layer retains exactly two modes with coefficients ±i/800; deeper old layers retain none.

Source oldform_tower_compression.md:
d359482763667a6707ed9a060a3874e951f95336561a4ac645df453022b085ae
Review /workspace/shared/bgs_oldform_tower_review/REPORT.md:
f3d142204ed6d10015e70595633c714acaf097fa1b0e6f19fdf6a51d4e663be5

The earlier even-depth3,2,2 special case and second-order Schur formula have separate review /workspace/shared/bgs_oldform_obstruction_review/REPORT.md, hash f208aecb761c8bf7da960da994dc3dcbc08b8e88269aad040232b87573758224, bound to even_depth_first_order_obstruction.md hash37482d57477777ac40bc6a6375bcbf53667f16070e1bcf7e33db04fb9737f654.

This is a criterion failure, not an actual U eigenvalue-collision result. The scalar direct-power threshold9k<5^j does not bound effective perturbation-jet order because resolvents contain rotated Weyl modes.

## Accepted uniform even-core second-order splitting

For N=7*5^(2r), r>=2, the deepest oldform core consists of three full M eigenspaces of dimensions3,2,2. Their first-order slopes vanish and their second-order Hermitian phase matrices are simple. Thus those groups split at exactly order two near zero, uniformly in r.

Source uniform_oldform_second_jet.md:
c504620ef3111c7cf40af636eb7d00a1b4103463986c3ff3f7d8e3f01fee0e3a
Review /workspace/shared/bgs_uniform_second_jet_review/REPORT.md:
c3a98ad153737e4cdac381bf6318eff2d3c44e073a81a7387dbee785ab6a172c
The review independently reconstructs the fixed17-pair residue matrix, all three compressed characteristic polynomials and the complete primitive/nonprimitive return dictionary. Its manifest binds all three transitive author imports omitted from the initial author manifest.

## Accepted uniform odd-core second-order splitting

For N=7*5^(2r+1), r>=2, the deepest oldform core has dimension35 and six complete cat blocks7,7,7,4,5,5. Their first-order slopes vanish and their second-order phase matrices are simple. The proof controls a five-dimensional cat-stable lattice, an exact operator-valued geometric resolvent, and pairwise coprimality of the three fixed K7 block polynomials.

Source odd_core_second_jet_extension.md:
38b1e1b442f942a81a3ea7f89c9bd6a91f4a6ed39f12beb644d0c44064d0b46e
Review /workspace/shared/bgs_odd_core_second_jet_review/REPORT.md:
2b8f451ebca20251be2dec5864e8d8a6497eabeb4259cc5edcbc28da33ede101

## Accepted newest-even-sector first-order splitting

For N=7*5^(2l), l>=1, every complete cat block in the newest sector has dimension7 and simple A compression. This sector has dimension24N/25. The coherent-packet proof treats the exact common4000L denominator, all primitive norm circles, actual phases/aliases, and both l=1 and l>=2 degeneration regimes before using48 finite squarefreeness certificates.

Source even_new_sector_first_jet.md:
7e043149e73445cdd0f413f8ce9460b4c1de9690355c83d992e88ad3fbb2ad39
Review /workspace/shared/bgs_even_new_sector_review/REPORT.md:
ee5bf38c202fa9094fbae66666a8b2564874316258865928542d1c405500fb2e
Replay run_audit.py in that review directory. The independent implementation uses F5[w]/Phi7, projector-column bases and polynomial determinants rather than the author interpolation.

## Accepted literal-time rank consequences

For the actual family N=7*5^e and every nonzero real algebraic t, including t=10^(-80)N:

- every U_N(t) eigenvalue has multiplicity at most7, for all e>=1;
- at least24N/25+7 eigenvalues are simple for even e>=4;
- at least35 eigenvalues are simple for odd e>=5.

Source algebraic_time_rank_transfer_v2.md:
673f0831080263e6d28b85ce91ae4a5fa705d637aa34fb9fd6d54700cda3b62d
Review /workspace/shared/bgs_rank_transfer_review/REPORT.md:
d87128f695157a914f9ebb7b50e250b9a4f3185d3d28382d8afc2ba5cdb5c06d

The review binds17 inputs and records the newest-sector premise as accepted. The source's conditional wording is preserved as historical proof structure, but the dependency is now satisfied. The precisely registered LW theorem is the only external rank-transfer input.

Guardrails: rank chi'(U) counts SIMPLE eigenvalues, not all distinct ones. Rank of the derivative stack is the total dimension of eigenspaces with multiplicity at most k; it is not N minus the gcd degree. Only full-column-rank iff gcd=1 is used. The argument does not assume a single higher derivative is invertible.

## Exact remaining frontier

For even e>=4, at mostN/25-7 dimensions can belong to repeated eigenspaces at a nonzero algebraic time. This is a count, not a claim that a fixed oldform subspace stays U-invariant. Near zero the unresolved groups are in the old M sector outside the deepest seven-dimensional core.

The old layer j=1 has dimension24N/625 above its next layer and carries exactly the two-mode compressed observable. Deeper layers have zero first-order compression. The raw p-adic cat projectors at intermediate depths have 5-primary denominators; the prime-to-five projector/lattice argument used for the deepest cores does not automatically extend to them.

A two-mode coherent diagnostic separates first-old-layer norm classes: generic classes2,4 have squarefree candidate residues; class1 has no geometric intersection; class3 is a singular root-lifting regime. first_old_layer_coherent_residue.py/.json are research diagnostics, not additional accepted theorems. Full uniform U-simplicity remains open.

## Diagnostics, not promotion claims

Exact CRT compression tests at N875 and4375 are in crt_compression_discriminator.py/.json and the second-prime control. At N4375 nine first-order blocks vanish modulo two primes; second_order_discriminator.py splits all nine at the next modular jet. These computations were used to identify the actual oldform obstruction. They have not received their own independent full-U certificate audit and are not additional accepted U dimensions in this handoff.
