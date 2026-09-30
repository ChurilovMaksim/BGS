# Prime-resonant reference law and priority boundary

Checked 30 September 2026 against primary source text.

Eric M. Rains, [*Images of eigenvalue distributions under power maps*,
arXiv:math/0008079v1](https://arxiv.org/pdf/math/0008079v1), Theorem 1.3,
PDF pp. 2--3, equation (8). Published in *Probability Theory and Related
Fields* 125 (2003), 522--538. Registered as `EXT-RAINS-2003`.

For Haar $V\in U(n)$ and any integer $d\ge1$, the eigenvalues of $V^d$
have the distribution of the union of $d$ independent Haar spectra of
dimensions $\lceil(n-i)/d\rceil$, $0\le i<d$. Zero-size components are
omitted. The theorem is exact, with no large-dimension or fixed-power
restriction. The notation $p$ in Rains denotes a power, not a prime;
the project uses $n=p$ for dimension and $d=d_p$ for the power.

The reference trace variance is $\min(rd,p)$, also immediate from the
existing finite CUE identity for $\operatorname{Tr}V^{rd}$.
This explains why replacing the deterministic block by Haar CUE($p$)
would be a wrong benchmark. Rains' theorem gives no independence,
equidistribution or cancellation for the deterministic block in this repo.
The elementary sector criterion, determinant bound and spectral-comb
identities do not depend on that external distribution theorem.

The matrix-order divisibility, raw Weyl convention, exact iteration and
scalar-return exclusion are already in the project corpus. The Fejer
kernel, root-of-unity filter, positive-measure atom test and unitary
telescoping are standard tools. The audit assembles them into a scoped
sector criterion; no claim of a world-first theorem or full priority
search is made.

The broader literature search included Degli Esposti--Winn,
[*The quantum perturbed cat map and symmetry*](https://www.dm.unibo.it/fismat/pub/a5_26_005.pdf),
*J. Phys. A* 38 (2005), 5895--5912, DOI 10.1088/0305-4470/38/26/005.
Its abstract and model discussion describe dimension-dependent symmetry
obstructions in other perturbed cat families. Those models are not the
maintained frozen family, and no theorem from that paper is used as a
load-bearing input here. Eigenfunction quantum ergodicity references
likewise do not provide the required block trace-energy estimate.
