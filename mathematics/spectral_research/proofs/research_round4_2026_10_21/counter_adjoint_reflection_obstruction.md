> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/counter_adjoint_reflection_obstruction.md`. Embedded SHA256: `7b800ee5f2b088a4e4449816ff4680e0079a6b48c5c7f3a2458ddda2741f266e`.
> [Thematic guide](../../topics/symmetry.md).

# Adjoint-flat involutions: an obstruction to closure from norms alone

21 October 2026.

This is an auxiliary construction, not the family specified in the spectral-statistics problem. Its purpose is to test what the proved one-step entry and Schatten bounds can imply without additional information. It preserves the exact structure of unitary conjugation, rather than replacing the adjoint action by an arbitrary unitary matrix.

## 1. Statement

There is a deterministic family of Hermitian unitaries $\widetilde U_N\in U(N)$, indexed by every odd $N\ge3$, with the following properties:

$$
\widetilde U_N^2=I,\qquad
\operatorname{Tr}\widetilde U_N=1.
\tag{1.1}
$$

Let $W_v=T_N(l,k)$, $v=(k,l)$, be the original modular Weyl basis, let
$\Lambda_N=(\mathbb Z/N\mathbb Z)^2\setminus\{0\}$, and let $D=N^2-1$. The matrix of conjugation on the traceless space,
$$
\widetilde C_N(w,v)=N^{-1}
\operatorname{Tr}(W_w^*\widetilde U_NW_v\widetilde U_N^*),
\qquad v,w\in\Lambda_N,
\tag{1.2}
$$
satisfies
$$
\boxed{\quad
\max_{v,w\in\Lambda_N}|\widetilde C_N(w,v)|
\le a_N:=100\,\frac{\sqrt{\log N}}N.
\quad}
\tag{1.3}
$$
In particular, its entrywise maximum tends to zero. Every weighted permutation branch $K_\pi$, retaining only $\widetilde C_N(\pi(v),v)$, satisfies
$$
\|K_\pi\|\le a_N,\qquad
D^{-1/2}\|K_\pi\|_{\rm HS}\le a_N,
\tag{1.4}
$$
and for every finite $p\ge1$,
$$
\|K_\pi\|_{S^p}\le D^{1/p}a_N.
\tag{1.5}
$$
These statements are uniform over all permutations. Nevertheless,
$$
\widetilde C_N^2=I_D,\qquad
\operatorname{Tr}\widetilde C_N^{2j}=D\quad(j\ge1).
\tag{1.6}
$$
The auxiliary family also fails the pair comparison $H_{\rm diag}$, with its pair moments diverging for every fixed nonzero admissible $b$.

The proof uses Haar measure only to establish the existence of a deterministic auxiliary matrix in each dimension. The final family is selected deterministically. No averaging is imposed on, or used to replace, the prescribed $U_N$.

## 2. The one external theorem and verification of its hypotheses

The sole external probabilistic input is Corollary 17 of Elizabeth S. Meckes and Mark W. Meckes, “Spectral measures of powers of random matrices,” Electronic Communications in Probability 18 (2013), no. 78, 1--13, DOI 10.1214/ECP.v18-2551. The author manuscript is arXiv:1210.2681v3, dated 20 September 2013. The result is on printed page 13, PDF page index 12.

Primary sources read:

- [Author manuscript, Corollary 17](https://arxiv.org/pdf/1210.2681);
- [Publication metadata and DOI](https://arxiv.org/abs/1210.2681).

For one Haar-distributed $V\in U(N)$, the corollary states that a real $L$-Lipschitz function $F$, for the ordinary Hilbert--Schmidt distance, obeys
$$
\Pr\{F(V)\ge\mathbb EF(V)+s\}
\le\exp\!\left(-\frac{Ns^2}{12L^2}\right),\qquad s>0.
\tag{2.1}
$$
This is the case of one factor in that corollary; its independence assumption is then vacuous. The metric is not the normalized Hilbert--Schmidt metric. The proof in the paper uses its Theorem 15, with logarithmic Sobolev constant $6/N$.

In the application below $F$ is one of the real or imaginary parts of a smooth matrix coefficient, or its negative. The group is exactly $U(N)$, the law is exactly Haar, the expectation is exactly zero, and the Lipschitz constant for that unnormalized metric is checked to be $4/\sqrt N$. Thus every hypothesis of (2.1) will be verified directly.

## 3. A balanced involution has exactly zero mean adjoint coefficient

For odd $N$, set
$$
R_0=\operatorname{diag}\left(
\underbrace{1,\ldots,1}_{(N+1)/2},
\underbrace{-1,\ldots,-1}_{(N-1)/2}\right),
\qquad R(V)=VR_0V^*.
\tag{3.1}
$$
Every $R(V)$ is Hermitian and unitary, its square is $I$, and its trace is one.

Define the linear map
$$
\mathcal T(X)=\mathbb E_V[R(V)XR(V)^*].
\tag{3.2}
$$
Haar invariance implies that $\mathcal T$ commutes with conjugation by every fixed unitary. An elementary matrix-unit calculation identifies its action.

First, conjugation by diagonal unitaries assigns the matrix unit $E_{ij}$, $i\ne j$, the character $z_i\overline z_j$. Its eigenspace is exactly the span of $E_{ij}$. Thus
$\mathcal T(E_{ij})=\alpha_{ij}E_{ij}$.
Permutation conjugations make all these scalars equal to a single $\alpha$. Next, the unitary $2\times2$ Hadamard matrix on the span of coordinates $i,j$ conjugates $E_{ii}-E_{jj}$ to $E_{ij}+E_{ji}$. Covariance therefore implies
$$
\mathcal T(E_{ii}-E_{jj})=\alpha(E_{ii}-E_{jj}).
$$
Off-diagonal units and diagonal differences span the traceless matrix space. Hence $\mathcal T$ acts there by $\alpha I$, while $\mathcal T(I)=I$.

For any unitary $R$, the trace of its conjugation map on the full $N^2$-dimensional matrix space is
$$
\operatorname{Tr}_{\rm super}(X\mapsto RXR^*)=|\operatorname{Tr}R|^2.
\tag{3.3}
$$
To verify (3.3), its diagonal coefficient at $E_{ij}$ is $R_{ii}\overline{R_{jj}}$; sum over $i,j$. In the present case this trace equals one for every $V$. Taking the trace in (3.2) therefore gives
$$
1+\alpha(N^2-1)=1,\qquad \alpha=0.
\tag{3.4}
$$

Every nonzero Weyl mode is traceless. Consequently the complex function
$$
f_{w,v}(V)=N^{-1}\operatorname{Tr}
\bigl(W_w^*R(V)W_vR(V)^*\bigr)
\tag{3.5}
$$
has exact mean zero whenever $v\ne0$. This proves the centering required by (2.1) without a representation-theoretic assumption left unproved.

## 4. Lipschitz constant and simultaneous concentration

Since all factors in (3.1) are unitary,
$$
\|R(V)-R(V')\|_{\rm HS}
\le2\|V-V'\|_{\rm HS}.
\tag{4.1}
$$
Subtract the two products in (3.5), one factor at a time. Hilbert--Schmidt Cauchy--Schwarz, together with $\|W_v\|_{\rm HS}=\sqrt N$, gives
$$
|f_{w,v}(V)-f_{w,v}(V')|
\le\frac2{\sqrt N}\|R(V)-R(V')\|_{\rm HS}
\le\frac4{\sqrt N}\|V-V'\|_{\rm HS}.
\tag{4.2}
$$
Thus each real or imaginary part, and its negative, is $L$-Lipschitz with $L=4/\sqrt N$.

If a mean-zero complex number has modulus at least $u$, either its real or its imaginary part has magnitude at least $u/\sqrt2$. Apply (2.1) to the two signs of those two parts. Equations (3.4) and (4.2) prove
$$
\Pr\{|f_{w,v}(V)|\ge u\}
\le4\exp\!\left(-\frac{N^2u^2}{384}\right).
\tag{4.3}
$$
There are $(N^2-1)^2<N^4$ pairs of nonzero labels. A union bound with
$$
u=a_N=100\frac{\sqrt{\log N}}N
$$
therefore yields
$$
\Pr\left\{\max_{v,w\ne0}|f_{w,v}(V)|\ge a_N\right\}
\le4N^{4-10000/384}
=4N^{-529/24}<1
\tag{4.4}
$$
for every $N\ge3$. Thus a suitable matrix exists in every odd dimension. The bound need not be below one in small dimensions to be valid; it tends to zero as $N\to\infty$.

## 5. Deterministic selection and the exact revival

For a deterministic definition, minimize the continuous function
$$
V\longmapsto\max_{v,w\in\Lambda_N}|f_{w,v}(V)|
$$
over the compact group $U(N)$. It has a nonempty compact set of minimizers. Select one by successive lexicographic minimization of the real and imaginary parts of its entries, in a fixed row-major ordering. Each step leaves a nonempty compact set; after the finitely many coordinates a unique matrix $V_N$ remains. This defines a deterministic $V_N$ with no residual randomness.

Put
$$
\widetilde U_N=V_NR_0V_N^*.
\tag{5.1}
$$
The existence estimate (4.4) shows that this minimizer satisfies (1.3). Equation (3.1) proves (1.1), and hence conjugation by $\widetilde U_N$ squares to the identity. This proves (1.6). In fact,
$$
\operatorname{Tr}\widetilde U_N^n=
\begin{cases}
1,&n\ \text{odd},\\
N,&n\ \text{even},
\end{cases}
\qquad
\operatorname{Tr}\widetilde C_N^n=
\begin{cases}
0,&n\ \text{odd},\\
N^2-1,&n\ \text{even}.
\end{cases}
\tag{5.2}
$$

A weighted permutation matrix has singular values equal to the moduli of its selected entries. This proves (1.4)--(1.5) directly from (1.3). For the particular exponent $p=35$,
$$
\sup_\pi\|K_\pi\|_{S^{35}}
\le100\,N^{-33/35}\sqrt{\log N}\longrightarrow0.
\tag{5.3}
$$
These bounds are stronger than a fixed entry gap, a decaying normalized HS bound, or a bounded unnormalized $S^{35}$ norm of the selected branches. Their coexistence with (5.2) proves that those bounds alone cannot control the full coherent trace.

## 6. An explicit failure of the auxiliary pair comparison

The eigenphases of $\widetilde U_N$ are $0$, with multiplicity
$r=(N+1)/2$, and $1/2$, with multiplicity $s=(N-1)/2$. Let $b$ be any fixed nonzero admissible function from the original criterion. In particular $b\ge0$, $b$ is Schwartz, and $\int b^2>0$.

Keeping only the nonnegative contributions of pairs within the same cluster gives
$$
M^{\widetilde U}_{2,N}(b)
\ge\frac{r(r-1)+s(s-1)}2\int_0^1b_N(t)^2\,dt
=\frac{(N-1)^2}{4}\int_0^1b_N(t)^2\,dt.
\tag{6.1}
$$
Because all periodized terms are nonnegative,
$$
\int_0^1b_N(t)^2\,dt
\ge\int_0^1\sum_{\ell\in\mathbb Z}b(N(t+\ell))^2\,dt
=\frac1N\int_{\mathbb R}b(x)^2\,dx.
\tag{6.2}
$$
Therefore the exact finite-dimensional CUE bound
$M^{\rm CUE}_{2,N}(b)\le(\int b)^2/2$ gives
$$
M^{\widetilde U}_{2,N}(b)-M^{\rm CUE}_{2,N}(b)
\ge\frac{(N-1)^2}{4N}\int b^2-\frac12\left(\int b\right)^2
\longrightarrow+\infty.
\tag{6.3}
$$

For completeness, a nonzero admissible $b$ exists without an additional assumption: choose a nonzero $\varphi\in C_c^\infty(\mathbb R)$, let $g$ be its inverse Fourier transform, and take $b=c|g|^2$ with a sufficiently small positive $c$. Its Fourier transform is a smooth compactly supported convolution, and its supremum is less than one.

There is also a direct bounded-observable obstruction to the sine-process limit for this auxiliary family. For a compact interval $[-L,L]$, the translated microscopic process has any point there only when the uniformly selected origin is within $L/N$ of one of the two phases $0,1/2$. The probability is at most $4L/N$. Thus its Laplace functionals tend to those of the empty process, even though its intensity is one at every finite $N$. This explains the diverging moments as rare large clusters.

## 7. Exact logical scope

The deterministic family (5.1) is not the prescribed $e^{i\tau N A_N}M_N$, and this note is not a refutation of $H_{\rm diag}$ for that prescribed family. Its concentration theorem is used solely to certify a deterministic auxiliary existence construction; it is not transferred to the original spectral functional.

What the construction rules out is a universal closure implication based only on the new all-entry bounds, a fixed entrywise gap, selected-permutation HS or Schatten estimates, exact unitary conjugation structure, and exact trace closure. All those properties hold here, some with much stronger rates, while full coherent revivals and a divergent pair comparison remain. Additional information specific to the original dynamics is necessary for the desired universality proof.
