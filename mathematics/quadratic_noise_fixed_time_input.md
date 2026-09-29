# Fixed-time trace input for the maintained map: conditional source adaptation

**Claim ID: BGS-FM-013. Status: CONDITIONAL APPLICATION.**
29 September 2026. The parity calculation below is exact. The proposed
application of the plane semiclassical trace estimate to the maintained
odd-dimensional quantization is recorded separately from the proved
abstract noise theorems. It is not a Heisenberg-time estimate.

## 1. Input actually needed

For the fixed family $U_N=e^{i\tau N A_N}M_N$, $\tau=10^{-80}$,
the short-time results in [FLOW-004](quadratic_noise_coupling.md) and
[FLOW-005](quadratic_noise_reversibility.md) need only
$|p_1(U_N)|+|p_2(U_N)|=O(1)$. The fixed-trace CLT needs
$|p_j(U_N)|=O_j(1)$ at every fixed $j$, plus convergence of the finitely
many chosen initial traces (or passage to an appropriate subsequence).

The expected source is Faure, arXiv:nlin/0610004v2, Proposition 11,
equation (69), a local plane trace estimate. Its full torus Theorem 12
cannot be imported unchanged: Section 2.2.2 assumes even $N$, whereas
our family uses odd $N$. See [the source review](../literature/quadratic_noise_sources_20260929.md).

## 2. Exact parity repair

Put $h=(2\pi N)^{-1}$ and $\chi_N(n)=(-1)^{Nn_1n_2}$.
For plane Weyl translations, the formal periodization for periodic
position and momentum boundary conditions is

$$
P_N=\sum_{n\in\mathbb Z^2}\chi_N(n)T_n.
$$

The sum is interpreted on the standard distributional periodic space,
not as a norm-convergent bounded-operator series.
Here $S=\left(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\right)$ and
$S^{-1}\equiv I\pmod2$, hence $\chi_N(S^{-1}n)=\chi_N(n)$.
Its metaplectic lift preserves this boundary condition, as does a
periodic Hamiltonian kick. For $L=(S^{-1})^j$ and
$n'=n+(L-I)k$, the translation phase in the cell argument is determined by

$$
2F=n\wedge Lk-k\wedge(n+Lk). \tag{1}
$$

Since $L\equiv I\pmod2$, (1) is even and $(L-I)k$ has even components.
Thus $F\in\mathbb Z$, $e^{iF/h}=1$, and $\chi_N(n')=\chi_N(n)$ for
odd as well as even $N$. This removes the specific lattice parity
obstruction. A finite exact verifier checks 1,875 examples, but this
modulo-two argument proves the general identity.

## 3. Proposed fixed-time application and its remaining check

The required periodized trace formula is

$$
\operatorname{Tr}M_{\rm torus}^j
=\sum_{n\in\mathbb Z^2/(L-I)\mathbb Z^2}
 \chi_N(n)\,\mathcal T(T_{-n}M_{\rm plane}^j). \tag{2}
$$

There are $|\det(L-I)|$ terms at fixed $j$; signs have unit modulus.
The plane fixed-point estimate would give a bounded leading amplitude
and a vanishing remainder for each term, hence $|p_j|=O_j(1)$.
The proposed parameter map is $H_1=-\tau g/(2\pi)$, with $g$ the
physical ordinary Weyl symbol of [FM-001](fixed_model_symmetry_theorem.md),
including its momentum half-shift. The classical map is
$\Phi_g^{-\tau/(2\pi)}S^{-1}$.

Before promoting this application to proved, check (2) with the
distributional cell-trace regularization and remainder hypotheses of
the plane proposition, and explicitly identify its odd-dimensional
restriction with the maintained $M_N,A_N$. Exact Weyl conjugation would
identify the two irreducible metaplectic restrictions up to a scalar;
that scalar does not affect absolute traces. Parity alone does not
complete this source-to-model identification. No abstract noise theorem
depends on assuming that this check has already been completed.

Conditional on that identification and fixed-time remainder control,
the maintained geometric bound for the forward map gives
$DG\ge B=\left(\begin{smallmatrix}5/2&7/2\\3/2&5/2\end{smallmatrix}\right)$
entrywise. Thus $\operatorname{Tr}DG\ge5$ and
$\operatorname{Tr}D(G^2)\ge\operatorname{Tr}B^2=23$.
The period-one and period-two fixed-point counts are $4$ and $32$;
the leading trace amplitudes then imply

$$
\limsup_{N\ {
m odd}}|p_1|\le4/\sqrt3,\qquad
\limsup_{N\ {
m odd}}|p_2|\le32/\sqrt{21}. \tag{3}
$$

In particular $|p_1|<3$, $|p_2|<8$ eventually, so $K=20$ would be
admissible in the coupling theorems. No effective threshold in $N$
is supplied. Even successful completion of this fixed-time application
would establish neither Dyson relaxation for this starting spectrum
nor removal of the added noise. BGS-TRACE-005 remains open.
