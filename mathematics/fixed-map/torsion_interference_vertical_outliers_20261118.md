# Torsion-history interference and exceptional vertical channels (18 November 2026)

**Status:** supplementary, independently reconstructed exact argument for the prescribed fixed-map family. **No registry promotion.** This note is not a proof or disproof of BGS-BGS-001, BGS-TRACE-005, the pair limit, or the higher-order hierarchy.

**Source and precedence:** derived from the six-round external research packet of 18 November 2026, especially its round-6 arithmetic square-sum and vertical-outlier notes; checked against the frozen family in [fixed_map_resolvent_frontier.md](fixed_map_resolvent_frontier.md), the ordinary-midpoint convention in [fixed_model_symmetry_theorem.md](fixed_model_symmetry_theorem.md), and the arithmetic setup in [arithmetic_oldspace_escape.md](../spectral_research/proofs/research_round2_2026_10_20/arithmetic_oldspace_escape.md). The associated [scope audit](../../evidence/research/20261118_six_round_review/README.md) distinguishes this exact argument from unreviewed analytic claims in the packet.

## 1. Exact model and scalar-centering convention

For odd N, take the raw Weyl matrices T_N and the cat-map matrix M_N of the maintained model. The **canonical BGS generator** is

$$
A_N=\sum_{k,l}c_{kl}T_N(l,k),\qquad
f-\tfrac1{10}=\sum_{k,l}c_{kl}e^{2\pi i(kq+lp)}.
$$

The physical ordinary-midpoint symbol is

$$
g(q,p)=\cos(14\pi q)+\frac{r(q)}{10}
+\frac{r(q)\sin(2\pi q)}{100}
+\frac{r(q+\tfrac12)\cos(2\pi p-\alpha_0)}{100}
-\frac1{10},
\quad
r(q)=(1-\cos14\pi q)(1+\cos2\pi q).
$$

Here \(e^{i\alpha_0}=(-3+4i)/5\). In particular \(r(q+\tfrac12)\), rather than \(r(q)\), multiplies the momentum Fourier mode. Let

$$
K_N(t)=e^{itA_N},\qquad V_N(t)=K_N(t)M_N,
\qquad U_N=V_N(\tau N),\quad \tau=10^{-80}.
$$

The uploaded packet often uses the **uncentered** generator \(A_N+\tfrac1{10}I\). That convention multiplies \(V_N(t)\) by \(e^{it/10}\). It leaves the two assertions below unchanged, since they concern squared trace moduli or singular values; it must **not** be dropped in individual complex trace or resonance statements.

## 2. Nonvanishing of the fully summed torsion-history interference

**Proposition 1 (an exact obstruction to incoherent history summation).**
For every \(j\ge2\), set

$$
N=7^j,\qquad r_j=3\,7^{j-1}=3N/7.
$$

There are 49 pairwise orthogonal rank-\(N/49\) projections \(P_a\), \(a\in H=(\mathbb Z/7\mathbb Z)^2\), summing to I, such that \(M_N\) permutes their ranges. For any \(k\ge1\), any \(\mathbf a\in H^k\), and real \(t\), let

$$
F_{\mathbf a}(t)=
P_{a_k}V_N(t)P_{a_{k-1}}V_N(t)\cdots P_{a_1}V_N(t)
$$

and define the **complete signed interference**, not an individual cross term, by

$$
\mathcal I_{N,k}(t)=
|\operatorname{Tr}V_N(t)^k|^2-
\sum_{\mathbf a\in H^k}|\operatorname{Tr}F_{\mathbf a}(t)|^2.
$$

If \(r_j\mid k\), then

$$
\boxed{\mathcal I_{N,k}(0)=\frac{48}{49}N^2, \qquad
\mathcal I_{N,k}(\tau N)\ne0.}
$$

The latter assertion remains true for every nonzero **real algebraic** \(t\). It also holds for any finite positive algebraically weighted sum of \(\mathcal I_{N,k}(t)\) with \(r_j\mid k\). In particular the four times \(k=r_j,2r_j,3r_j,4r_j\) are all below \(2N\).

**Proof.** Put \(G_{u,v}=T_N((N/7)u,(N/7)v)\). Because \(49\mid N\) and the modular inverse of 2 is used in T_N, the Weyl composition cocycle on these labels is identically one. Thus \(G_{u,v}\) form an ordinary representation of H. Nonidentity elements have zero trace, hence its character projections

$$
P_a=\frac1{49}\sum_{h\in H}\overline{\chi_a(h)}\,G_h
$$

are orthogonal, sum to I, and have rank \(N/49\). Exact cat Egorov permutes this group and hence its character projections.

A direct integer multiplication gives

$$
S^3=\begin{pmatrix}99&140\\70&99\end{pmatrix}=I+7B
$$

for an integer matrix B. The binomial theorem gives \(S^{3\cdot7^{j-1}}\equiv I\pmod {7^j}\). Exact modular Egorov and irreducibility of the Weyl representation imply that \(M_N^{r_j}=\gamma_j I\), \(|\gamma_j|=1\). Thus \(M_N^k\) is scalar for every multiple k of \(r_j\).

At \(t=0\), successive orthogonality of the projections forces all labels in a nonzero history to follow the unique cat-induced permutation. There are precisely 49 such histories. Each has trace modulus \(N/49\), while \(|\operatorname{Tr}M_N^k|=N\). Consequently

$$
\mathcal I_{N,k}(0)
=N^2-49(N/49)^2=(48/49)N^2.
$$

Every entry of \(A_N\), \(M_N\) and \(P_a\) is algebraic: the Fourier coefficients and the phase \(e^{i\alpha_0}\) are algebraic, and the Weyl phases are roots of unity. Since \(A_N\) is Hermitian, its distinct eigenvalues \(\beta\) are real algebraic and its spectral projections are matrices with algebraic entries (Lagrange interpolation). On the real line, each trace of a history is therefore a finite sum of terms \(c_\beta e^{it\beta}\), with algebraic \(c_\beta\); its squared modulus is again such a finite exponential polynomial. Group terms by their distinct algebraic frequencies \(\beta\).

The Lindemann-Weierstrass linear-independence form says that exponentials of distinct algebraic numbers are linearly independent over the algebraic numbers. At any nonzero algebraic t, the exponents \(it\beta\) are distinct algebraic numbers. Hence a finite algebraic-coefficient exponential polynomial can vanish there only if all its grouped coefficients vanish, in which case the same polynomial vanishes at \(t=0\). The displayed positive value at zero excludes this possibility. For a positive algebraically weighted finite sum, its value at zero is again strictly positive, so the same reasoning applies. QED.

**Exact scope.** The proof establishes \(\mathcal I_{N,k}(\tau N)\ne0\), **not** a uniform lower bound of order \(N^2\), a fixed sign, or nonvanishing of the prescribed bump-weighted sum. It therefore does not refute (P). Nor does it exclude a signed cancellation between histories sufficient to yield Sine2. What it does rule out is the false inference that orthogonality of the torsion projectors makes all trace-history cross terms vanish at the fixed nonzero kick.

For comparison, summation of **complete Hilbert-Schmidt norms** is exact:

$$
\sum_{\mathbf a\in H^k}\|F_{\mathbf a}(t)\|_{\mathrm{HS}}^2=N.
$$

This follows recursively from orthogonality and unitarity. Taking a trace before squaring inserts the identity direction in Hilbert-Schmidt space and destroys that orthogonality. Equivalently, with \(\mathcal D(X)=\sum_aP_aXP_a\), the incoherent sum is \(\operatorname{Tr}_{HS}[(\mathcal D\circ\operatorname{Ad}V_N(t))^k]\), whereas the coherent total is \(\operatorname{Tr}_{HS}[(\operatorname{Ad}V_N(t))^k]\).

## 3. Exceptional almost-retained vertical channels

**Proposition 2 (no operator-norm inference from bulk vertical singular laws).**
Let \(d\ge3\) be any fixed odd integer and \(d\mid N\), with N odd. Let \(E_d\) multiply by the indicator of \(d\mid x\). In centered residue representatives, for any integer \(0\le L\le N/4\), put \(Q_L=E_d{\bf1}_{|x|\le L}\). The compression \(E_dK_N(\tau N)E_d\) has at least

$$
2\lfloor L/d\rfloor+1
$$

singular values not smaller than

$$
\boxed{1-\frac{121\pi^2\tau(L+1)^2}{N}.}
$$

In particular, as N tends to infinity along odd multiples of fixed d,

$$
\|E_dK_N(\tau N)E_d\|\longrightarrow1.
$$

One may let \(L\to\infty\) with \(L=o(\sqrt N)\); then an unbounded (but vanishing-density) number of singular values tend to one.

**Proof.** For the canonical **centered** generator, the exact raw-Weyl matrix has diagonal

$$
A_N(x,x)=
\cos(14\pi x/N)+\frac{r(x/N)}{10}
+\frac{r(x/N)\sin(2\pi x/N)}{100}-\frac1{10},
$$

and its only off-diagonal entries connect \(x\) to \(x\pm1\), with the forward hopping coefficient

$$
A_N(x,x+1)=\frac{e^{-i\alpha_0}}{200}
r\left(\tfrac12+\frac{x+1/2}{N}\right).
$$

These formulas use the modular inverse \((N+1)/2\) and the required \(r(q+\tfrac12)\) shift. For real \(|q|\le1/4\), \(1-\cos u\le u^2/2\) and \(|\sin u|\le1\) give

$$
\left|\cos14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin2\pi q}{100}-1\right|
\le120\pi^2q^2,
\quad
r(\tfrac12+q)\le4\pi^2q^2.
$$

The diagonal and two weighted shifts consequently satisfy

$$
\|(A_N-\tfrac9{10}I)Q_L\|
\le121\pi^2(L+1)^2/N^2.
$$

Apply the unitary Duhamel formula to \(K_N(t)-e^{i(9/10)t}I\); at \(t=\tau N\),

$$
\|(K_N(\tau N)-e^{i(9/10)\tau N}I)Q_L\|
\le121\pi^2\tau(L+1)^2/N.
$$

Since \(E_dQ_L=Q_L\), the same lower isometry bound holds for \(E_dK_N(\tau N)E_d\) on the rank-\(2\lfloor L/d\rfloor+1\) space ran \(Q_L\). The singular-value min-max characterization gives the claim. QED.

**Boundary.** This is a statement about a *vertical* projector and the *kick* K_N, not the full 49-character oldspace nor the compression of \(U_N=K_NM_N\). It is compatible with a bulk vertical squared-singular-value distribution supported below \(4(d-1)/d^2\), because exceptional subspaces may have asymptotic density zero. It does not contradict the exact oldspace-escape theorem already maintained in the repository.

## 4. Relation to the open programme

These two exact facts identify **two prohibited shortcuts**, not a route to a completed BGS proof:

1. A dephased/incoherent sum of all 49 arithmetic histories is not identical to the coherent squared trace at the prescribed algebraic kick.
2. Weak convergence of vertical singular-value measures with upper edge below one cannot be promoted to a uniform operator-norm gap.

The unsolved part of BGS-TRACE-005 still requires quantitative **signed** control of the complete, model-specific joint-trace expression at Heisenberg times. Its second-order ramp-to-plateau cancellation and the all-order Sine2 criterion remain open.
