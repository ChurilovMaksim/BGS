# Exact-source check for the Heisenberg note

Checked: 30 September 2026. This records primary-text inspection, not an
independent referee opinion, broad priority search or model universality.

## Cohen: the load-bearing ideal-model source

Alex Cohen, *Fractal uncertainty for discrete two-dimensional Cantor sets*,
[arXiv:2206.14131v3](https://arxiv.org/abs/2206.14131v3), 5 October 2024;
Analysis & PDE 18 (2025), 743--772,
[DOI:10.2140/apde.2025.18.743](https://doi.org/10.2140/apde.2025.18.743).
Pinned locator: Theorem 2, printed p. 3. Section 5.2 was also inspected for
the stated sharpness; the project's even-base failure is proved directly.

Hypothesis map: both alphabets are $\mathcal A_M$, both iterates have
side length $N=M^k$, and the Fourier normalization is $1/N$.
The project proves absence of perpendicular full affine lines for odd
$M$ using the limiting closed digit set, including boundary issues.
The criterion then supplies some positive exponent. For even $M\ge4$
the project additionally constructs a discrete unit vector and its Fourier
transform in the allowed supports, proving norm 1 at every scale internally.
The binary norm is calculated internally. No exponent is claimed for
base 7 and no theorem is applied to the actual doubled quantum map.

The primary PDF's relevant statements were inspected through the web tool. This is the only new
load-bearing external leaf, `EXT-COHEN-2025`.

## Faure--Tsujii: genuine natural operator, insufficient identification

Frédéric Faure and Masato Tsujii, *Prequantum transfer operator for
symplectic Anosov diffeomorphism*,
[arXiv:1206.0282v2](https://arxiv.org/abs/1206.0282v2), 10 May 2013.
The full primary paper text was retrieved with alphaXiv's raw `fullText`
option; no AI-generated paper overview was used as theorem evidence.

Theorem 1.38, printed p. 27, concerns the isolated outer-band quantum
operator defined by the prequantum/Grassmannian construction. Its orbit
sum uses effective damping $D=V-V_0$ and has error
$CN^d(r_1^++\epsilon)^n$ under that construction's assumptions.
Problem 1.41 and Corollary 1.37 discuss the special undamped choice and
quasi-unitarity. This is not an all-time formula for every quantization.

Theorem 1.69, printed p. 39, compares its natural operator with a Toeplitz
operator after a potential correction $V'=V+M$, at order $O(\hbar^\delta)$
for some $\delta>0$. It supplies neither arbitrary-order matching nor
identification with the maintained matrix $e^{i\tau NA_N}M_N$.
Dimensions, the norm/identification, potential correction and a common
all-order family still require model-specific proof. The conditional
telescoping theorem is proved internally in `heisenberg_trace_support.md`;
this paper is not registered as a proved input for the actual map.

## Jin--Zhang--Zhang: anisotropy cannot be dropped

Long Jin, An Zhang and Hong Zhang, *Anisotropic 2D FUP and quantum open
baker's map*, [arXiv:2606.23160v1](https://arxiv.org/abs/2606.23160v1),
22 June 2026. Full primary text was retrieved through the same raw-content
endpoint; the version header and actual theorem statements were checked.

Section 1.1, printed p. 3, assumes $M_1>M_2\ge2$; its quantum open baker
is explicitly defined in (1.1). Theorem 1.2, printed p. 5, characterizes
the anisotropic discrete FUP using row/column conditions for these bases.
Equal base 7 is outside its hypothesis. Theorem 1.1 is a spectral theorem
for that open baker, not a closed-map or eigenphase-universality theorem.
Remark 1.4 explicitly leaves the general anisotropic continuous counterpart
unproved. Theorems 1.5 and 1.6 are different continuous statements with
specified isotropic/reflected transforms; neither automatically handles
arbitrary nonlinear coordinate distortion of our proposed survivor sets.
No load-bearing leaf is added from this paper for the base-7 route.

## Remaining citations and priority boundary

Charles, Zelditch, Han--Schlag, higher-dimensional Cohen, Dyatlov--Zworski,
Braun--Haake and Müller--Novaes are suggestions in the submitted programme.
No claim here uses them to solve an unspecified symbolic, holonomy,
normal-form, renewal or Heisenberg-time cancellation obligation. Their
complete source-to-model maps were not supplied or verified in this pass.
The new exact results are scoped project deductions from elementary
algebra/geometry and the specifically pinned Cohen theorem.
