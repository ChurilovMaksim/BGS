> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round10_2026_10_21/root_operator_route_scope.md`. Embedded SHA256: `579b1f4721dfaef4e6da1d914d90cab934b2fc625ebe37ef93b87839b57722a2`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Operator comparison after phase normalization: the attempted bridge and its remaining gap

21 October 2026. Round 10. Coordinator's research note.

## 0. Status

This is a record of an executed attempt to control the original signed
sum by comparing quantum operators after the Round 9 phase
normalization. It contains no new estimate for that original sum.
The possible Hölder and prequantum improvements described below have
not been proved here and are not used as hypotheses in a claimed
solution. The exact original family, fixed parameter, and all odd
dimensions remain unchanged.

## 1. The quantity that an operator argument must actually control

For an arbitrary unitary matrix $U$, let

$$
\mathcal C_U(X)=UXU^*,\qquad X\in\operatorname{End}(\mathbb C^N).
$$

In matrix units its operator trace is

$$
\operatorname{Tr}_{\rm HS}\mathcal C_U^m
=\sum_{i,j}(U^m)_{ii}\overline{(U^m)_{jj}}
=|\operatorname{Tr}U^m|^2.
\tag{1.1}
$$

The operator acts on a space of dimension $N^2$. Consequently,
for any comparison errors $R_{m,N}$ and any fixed continuous weight

$$
\left|N^{-2}\sum_{1\le m\le BN}w(m/N)
                     \operatorname{Tr}_{\rm HS}R_{m,N}\right|
\le \sum_{1\le m\le BN}|w(m/N)|\,\|R_{m,N}\|.
\tag{1.2}
$$

Indeed, the absolute trace of an operator on a $d$-dimensional
Hilbert space is at most $d$ times its operator norm: sum its $d$
diagonal matrix elements in any orthonormal basis. Apply this with
$d=N^2$ term by term to obtain (1.2).

Thus a uniform $o(N^{-1})$ bound on the errors in the powers would
be sufficient by this particular argument. A bound on the one-step
operator is not that bound. Nor is a uniform $O(N^{-1})$ bound on
the powers sufficient without more information about their traces.
The independent mixed-source branch supplies an exact CUE example
which saturates this distinction, not merely the dimension estimate.

There is a separate obstruction to replacing this with a contraction
estimate for the exact adjoint itself. If $U\psi_j=z_j\psi_j$,
then all $N$ independent matrices 
$\psi_j\psi_j^*$ are fixed by $\mathcal C_U$. There are therefore
at least $N-1$ fixed directions after removal of scalar matrices.
Moreover, $\mathcal C_U$ is unitary for the Hilbert--Schmidt norm.
Neither classical mixing nor a change of matrix basis changes these
two exact facts.

## 2. What the preceding normalization does and does not estimate

The actual Round 9 construction produces a unitary sequence

$$
\widetilde U_N=e^{iQ_N(v_{j(N)})/N}U_N
$$

and removes the first scalar graph phase with relative error
$o(N^{-1})$ per edge, hence relative error $o(1)$ uniformly along
every orbit of length at most $BN$, for each fixed $B$.
It also proves the stated eigenangle matching and local-law
stability. The source is
`root_diagonal_cocycle_normalization.md`, SHA-256
`afeaa52cea23836c5b4fa58d1040daa6df792d0b9adea83f8eb1de8690211921`.

These conclusions concern individual scalar products and an actual
unitary correction. They do not assert a bound of the form (1.2)
for a simpler operator whose statistics are known. If

$$
A_m=\sum_{\gamma}a_\gamma,\qquad
\widetilde A_m=\sum_{\gamma}a_\gamma(1+\epsilon_\gamma),
$$

the bound $\sup_\gamma|\epsilon_\gamma|=o(1)$ only directly gives

$$
|\widetilde A_m-A_m|
\le o(1)\sum_\gamma|a_\gamma|.
\tag{2.1}
$$

It does not give $o(1)|A_m|$. This is an elementary linear
algebra issue before any dynamical estimate: two terms $1,-1$
already have zero sum and can acquire a nonzero sum under a small
unequal relative change. For the actual orbit formula the number
of terms grows exponentially with time. No estimate for the fully
signed change was obtained in this round.

The new orderwise repulsion theorem improves the transfer of
moments between the two already matched quantum sequences. It
does not turn the leading scalar periodic sum into a unitary
operator with an independently established CUE limit.

## 3. The prequantum comparison checked in the primary text

Primary source: Faure--Tsujii, *Prequantum transfer operator for
symplectic Anosov diffeomorphism*, Astérisque 375 (2015),
[author text, arXiv:1206.0282v2](https://arxiv.org/pdf/1206.0282).
The actual pages read include 25--29, 39, and 160--162.

Theorem 1.69 gives an intertwining with a Toeplitz quantization
with an operator error $O(h^\delta)$ for some $\delta>0$, and a
modified potential $V'=V+\mathcal M$ with $\mathcal M$ continuous.
Theorem 1.35 controls the resolvent between spectral bands and
outside a fixed neighborhood of the outer band. The constants and
thresholds depend on that fixed neighborhood. Theorem 1.38 bounds
its own outer-band trace remainder by $CN^d(r_1^++\varepsilon)^n$.
This decreases with time when $r_1^++\varepsilon<1$, in particular
for a sufficiently small neighborhood at the reference potential.
Proposition 1.42 concerns
spectral uniqueness from such trace data; it is not a bound for
the norm of an intertwiner to the matrix in this problem.

The following are deductions about applicability, not additional
claims attributed to that source.

* A bound $O(h^\delta)$ with unspecified positive exponent does
  not imply $o(h)$. With $h=(2\pi N)^{-1}$, the latter is the
  elementary sufficient scale for directly matching unfolded
  eigenangles by unitary operator norm.
* A resolvent statement for each fixed $\varepsilon>0$ cannot be
  specialized to $\varepsilon=1/N$ without new bounds on its
  constants and thresholds. The microscopic radial window
  $e^{2s/N}=1+2s/N+O_s(N^{-2})$ lies inside every such fixed
  excluded neighborhood for all sufficiently large $N$.
* A spectral identification, if supplied, would still leave the
  local statistics inside the outer band to be proved. A gap from
  inner bands is a different spectral question.

I examined whether the normalized scalar could first be upgraded
from continuity to a Hölder space and then used as a uniformly
small multiplier on an anisotropic space. The graph contraction
and the base expansion suggest such a regularity calculation, but
three further requirements remain: the actual multiplier norm
uniform in $h$, a comparison for the varying potentials, and a
bound which survives (1.2). None was established. Merely listing
those requirements is not an operator estimate.

## 4. Smooth metaplectic comparison does not fill that gap

Primary source: L. Charles, *Semi-classical properties of geometric
quantization with metaplectic correction*,
[arXiv:math/0602168](https://arxiv.org/pdf/math/0602168),
published DOI [10.1007/s00220-006-0155-5](https://doi.org/10.1007/s00220-006-0155-5).
The actual statements on pages 3--4, 7--8, 12, and 14 were read.

Theorems 1.1--1.2 provide unitary identifications for smooth
compatible complex polarizations with $O(k^{-1})$ errors in
functoriality and parallel transport. Theorem 5.3 compares a
smooth Hamiltonian propagator with the associated geometric
quantization modulo $O(h)$. Theorem 3.3 calculates a
subprincipal intertwining term. These are not statements about
the nonsmooth invariant polarization of the present prequantum
outer band, nor an $o(h)$ comparison to that band.

Primary source: L. Charles, *Subprincipal symbol for Toeplitz
operators*, [arXiv:1410.2066](https://arxiv.org/pdf/1410.2066).
The actual statements on pages 2--5 and 7 were read.

Theorem 1.1 and Proposition 1.2 construct subprincipal symbols
using a connection and smooth geometric data. Equal principal
and subprincipal symbols give equality modulo $k^{-2}$ in the
specified Toeplitz class. Applying this conclusion requires first
placing both operators in that class and identifying both symbols.
Those requirements have not been verified for the proposed
outer-band comparison.

The implication needed here therefore cannot be obtained by
calling the operators two quantizations of the same classical
map. The missing comparison is mathematical content, not a
choice of notation or phase convention.

## 5. A recent semiclassical route and its scale

I also read the actual pages 2--4 of *Semiclassical foundation of
universality in chaotic quantum circuits*,
[arXiv:2605.27052](https://arxiv.org/pdf/2605.27052).
Its form factor includes an averaging operation. Its periodic
orbit reduction uses a central-limit scaling with a fixed
interaction parameter $\Lambda$, and its discussion of the
Heisenberg-scale plateau explicitly requires a further
resummation and states the extrapolation as a conjecture. This
does not supply an all-time error for the fixed one-map family
in the question.

There is a concrete scale distinction in attempting to use a
central limit theorem here. For a Birkhoff sum $S_m$ with
fluctuation scale $\sqrt m$, an action factor of the form
$e^{iN\tau S_m}$ probes the characteristic function of
$S_m/\sqrt m$ at argument $N\tau\sqrt m$. On $m\asymp N$
this argument is of order $\tau N^{3/2}$, which tends to
infinity for the fixed nonzero $\tau$. Convergence of the
characteristic function at every fixed argument gives no estimate
at those growing arguments. No uniform high-frequency estimate
for the actual fully weighted orbit sums was obtained.

## 6. Precise remaining original estimate

With the fixed admissible test $b_*$ defined in the Round 10
checkpoint, the first target is still

$$
\frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
\left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)\longrightarrow0
$$

through every odd dimension. The attempted comparisons above
neither establish this limit nor produce an infinite original
countersequence. They also do not exclude a future direct
operator argument with a genuinely summation-safe error.

