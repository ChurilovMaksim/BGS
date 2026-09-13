# Sources for return laws, lost intensity, and unfolding

Checked 12--13 September 2026 from base commit
26fa76b8eeb6d1259381474372b40e161383f219.
This is a targeted source comparison, not a priority certification.

## Exact external leaves

1. Nizar Demni and Taoufik Hmidi, *Spectral Distribution of the Free unitary
   Brownian motion: another approach*,
   [arXiv:1103.4693v1](https://arxiv.org/html/1103.4693v1),
   24 March 2011. Sections 1, 4, and 5 were read for the moment convention,
   support endpoints, and density representation. The source gives moments
   $e^{-nt/2}L_{n-1}^{(1)}(nt)/n$ and, for $0<t<4$, support
   $|\vartheta|\le\sqrt{t(4-t)}/2+\arccos(1-t/2)$.
   Our circle coordinate is $y=\vartheta/(2\pi)$ modulo one, and the
   repository's harmonic parameter is $t=\tau^2$. Hence the complement has
   Haar length $1-b(t)/\pi$. These are known free-probability facts.
   The inference to an empty component of a cat-map local limit uses the
   separate internal Theorem 3 and the project harmonic return theorem.
   No conclusion at the transition point $t=4$ is imported.

   Public preprint retained in the ignored local source cache; PDF SHA-256
   99a593e85af29a546862de6067b6105baf139a29738dc6c2c2b431d145975e0a.
   Text extraction with pdftotext is available. Its presence and hash establish
   source identity, not independent verification of every proof in the paper.

2. Alexander Soshnikov, *Determinantal random point fields*,
   [arXiv:math/0002099v4](https://arxiv.org/pdf/math/0002099v4),
   28 November 2000. Section 2.1(b), formulas (2.10)--(2.11), printed
   pages 19--20, and Section 2.3(b), printed page 22, identify Haar unitary
   eigenphases and their rescaled sine-kernel limit. Theorem 7 and its proof,
   printed pages 40--42, give ergodicity and mixing for translation-invariant
   determinantal fields. The circle-to-line scale here is
   $D\vartheta/(2\pi)$, giving intensity one. The sine projection kernel
   satisfies the stated Hermitian positive-contraction assumptions.
   These leaves justify the starting CUE example in (S26); the density
   transport is proved internally. No CUE theorem for the cat map is inferred.

## Discovery scope and overlap

Web searches used combinations of “point process local weak convergence
ergodic mesoscopic density”, “spectral statistics unfolding nonuniform
density mixture”, “pair correlation prescribed distribution”, and
“free unitary Brownian motion support”. A second discovery pass used
alphaXiv for local point-process limits, unfolding, loss of intensity, and
short-time traces. Its related-work candidates were not treated as proofs.

The abstract of Berkovits,
[arXiv:2303.04755v1](https://arxiv.org/abs/2303.04755v1), was inspected only
as a discovery lead about unfolding ensembles with fluctuating densities.
Its full proof was not audited and it is not a dependency here.
The earlier positivity/equidistribution comparison with
Aistleitner--Lachmann--Pausinger and Steinerberger remains in the main proof.

Classification: the free Brownian and CUE inputs are **known after translation
of notation**. The density-change mechanism uses standard transport and
invariant-coupling arguments. The precise intensity-cap formulation,
sharp spectral constructions, and cat-map consequences are project
derivations with **priority unverified**. The search did not cover all
probability textbooks, ergodic-decomposition literature, or unpublished work.
No “apparently new” or global novelty conclusion is asserted.
