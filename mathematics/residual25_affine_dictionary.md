# Residual-25 affine-return discriminator

Claim family: BGS-FM-026. Source-bound [independent review](../archive/record/residual25_affine_review.md).
The frozen original SHA256 is `afc110371271dcb24a52c5059184ee5ebdd9db8b5a127bb10f13d414819bf421`;
its exact bytes, original status and execution records remain in the
[provenance map](../archive/evidence/intermediate_old_layers_20261007/input_map.json).
Inherited [oldform](oldform_tower_compression.md),
[newest-sector](even_new_sector_first_jet.md), and
[rank-transfer](algebraic_time_rank_transfer.md) proofs retain their own scopes.
The [literal-time theorem owner](literal_time_multiplicity_bounds.md) is the
only maintained owner of the resulting fixed-time simple-eigenvalue counts.

The portable maintained command is
`python3 computations/verification/intermediate_old_layers_certificates.py`
(or the same command with `python3 -O`). Original bare script names below
identify archived historical implementations; the portable entry replays the
independent reviewers' algorithms in scratch storage and verifies their
outputs against the frozen reviewed results.

Status: independently reviewed uniform residual-25 splitting theorem, using the separately accepted general return-operator proof.

## Accepted family and precise matrix dictionary

The target is e=2j+2, j≥2, n=5^e, h=5^j, m=25, W_j=H_7⊗J_j H_25. First-order compression vanishes exactly. The 24 intermediate product-cat blocks have dimension 7; the three deepest blocks of dimensions 3,2,2 are covered by the prior deepest theorem. This is an intermediate family for every even e≥6, not an extrapolation from the finite N=109375 control.

Use δ*=1−q^(5h), where q is the induced primitive 5^e-th root. The leading matrix is the residue of 4000²δ* times the common second-order operator. The entries below include the actual coefficients and the raw seven-factor Weyl cocycle.

Let F=F_5[t]/(t^6+t^4+3t^3+t²+1), w=t^9, and let ξ be the recorded primitive sixth root. Put H_7=G_7/Tr(G_7), with eigenbasis V_7 and eigenvalue labels z_i∈{1,ω,ω²}, repeated with multiplicities 3,2,2, where ω=ξ².

For each c∈{1,2,3,4}, choose and record one norm circle O_c={y∈F_5²:Q(y)=c}, numbered y_k=S^k y_0, k=0,...,5. For each t=0,...,5 put γ_i=ξ^t/z_i.

For each of the 17 actual upper/upper pairs (v,u) with equal INTEGER norm Q(v)=Q(u):

1. Find the unique a mod 6 with S^a u=−v mod 5.
2. Retain the full seven-dimensional matrix

       B_7(v,u)=V_7^(-1)T_7(v)T_7(S^a u)V_7.

3. Let L_v=span_(F_5)(Jv), J=[[0,2],[1,0]], and define

       R_v(x,y)=1 if x−y∈L_v, else 0.

4. Form the residual matrix element, including its unit projector denominator,

       P_(i,j)(v;c,t)=(1/6)∑_(kx,ky=0)^5
          γ_i^kx γ_j^(−ky) R_v(y_kx,y_ky).

5. Add to the seven-by-seven matrix the entrywise product

       [2 d_v d_u/Q(v)] B_7(v,u)_(i,j) P_(i,j)(v;c,t),

   with d_v,d_u the unchanged Gaussian-integer coefficients reduced at i→2.

No 1/5 factor is introduced. The five-term line orbit-sum is unnormalized; only the six-term CAT orbit eigenvector projection contributes 1/6. A tangent intersection is counted once by the indicator definition. This prevents the identity-plus-reflection mnemonic from double counting tangent points.

The script computes all 24 matrices by this literal dictionary, stores their entries and characteristic polynomials, and checks gcd(p,p')=1 in F[z]. It uses eight exact determinant evaluations and interpolation for degree seven, avoiding division by characteristic five in Newton identities.

## Result

All 24 derivative gcds have degree zero: four norm-circle labels times six tame-character labels. This proves squarefreeness of these 24 exact finite matrices, not by itself their identification with every characteristic-zero compression.

Artifacts:

- residual25_affine_residue.py
- residual25_affine_residue.json
- residual25_affine_residue.log
- residual25_affine_manifest.json

Reproduce with `python residual25_affine_residue.py`. The initial attempt completed all arithmetic but failed while serializing NumPy integers; that output-only problem was fixed and the full computation rerun successfully. The final certificate includes the executed source hash.

## Independently accepted uniform-identification bridge

The following bridge is independently accepted in the linked review. The general identities are derived in the separate return-operator note; the review checks this character-compression bridge independently.

A. Phase-safe scalar regime. For e=2j+2 and j≥2, L=6·5^(j−1) is a multiple of 30, so M_25^L=I and μ^(−L)=1. Thus X_u=z_u T_25(b_u). The residual cat and character are eliminated here by their actual orders, not by approximation.

B. Entrywise normalization. In the residual coherent basis indexed by F_5², T_25(b_u) is a monomial permutation with cycles of length 5. Its cycle holonomy has fifth-root phase. Therefore the holonomy of X_u on a cycle is z_u^5 times a fifth root. Since z_u^5 has order 5^(j+1), every cycle denominator has valuation v_5(δ*), and δ*/(1−η_cycle) reduces to Q(u)^(-1). The exact five-step inverse numerator reduces to the UNNORMALIZED line sum. Scalar phases of five-power order reduce to 1.

C. Initial-factor cancellation on the line. If c_a=(v+S^a u)/h, equal integer norms imply that the polar pairing of v and c_a vanishes mod 5. Its kernel is span(Jv). The initial translation c_a therefore lies on the same line as the conjugated return cycle, so it preserves that line-sum matrix. The seven-factor operator remains T_7(v)T_7(S^a u), and a mod 3 is fixed by the unique return mod 5.

D. Actual coefficient filter. Upper modes have unit d_v. Every other primitive pair has positive extra Gaussian coefficient valuation and disappears after the entrywise normalization. For the pair of nonprimitive modes, use the shorter return period L'=6·5^(j−2). Its five-cycle holonomy has conductor j, one below the primitive conductor j+1. Its inverse loses at most 4v_5(δ*) relative to the primitive normalization, whereas the two actual coefficients gain total valuation 2. Hence those terms vanish for j≥2. Mixed contents do not return. The k=0 subtraction is integral before multiplying by δ* and vanishes. The five upper integer norm values are distinct modulo 25, leaving exactly the 17 pairs at all j≥2.

E. Integral cat-character projection. The residual coherent basis has one zero label and four primitive S-circles of length 6. Each circle spans an invariant monomial-cycle space. Diagonalizing an individual circle uses a denominator 6, which is a unit at 5; its six eigenvalues have distinct tame reductions. The six eigenvector amplitudes are units; their inverse matrix has denominator 6 and unit phase entries. Each circlewise eigenbasis therefore has unit determinant, and their block-diagonal union with the origin vector has unit determinant as well, despite ramified eigenvalue coincidences ACROSS different circles. The wild phase distinguishing the four circles is retained by selecting the actual circle before reduction. A full dimension-seven product block uses one such circle and three cubic-related residual eigenvalues, with reductions γ_i=ξ^t/z_i. Thus its reduction is exactly the dictionary above. This step does not use the nonintegral global M_25 projector of denominator 30.

F. Lift. Integral seven-factor projectors and the circlewise integral eigenvectors identify each normalized characteristic-zero compression with an integral matrix reducing to one of the 24 certified matrices. Squarefree residue then gives nonzero characteristic-zero discriminant; removing the nonzero scalar normalization gives second-order simplicity of that block. Steps A–E and the finite certificate passed the source-bound independent review; the original pre-review condition remains in the archived source.

## Boundary

The discriminator covers a fixed residual dimension, with j arbitrary through the accepted bridge above. It does not handle residual 5^s with s≥3, where residual cycle denominators and wild-character effects require further work. It does not assert full U simplicity, a gap estimate, or BGS universality.
