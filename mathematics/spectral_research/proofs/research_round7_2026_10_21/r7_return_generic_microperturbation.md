> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round7_2026_10_21/r7_return_generic_microperturbation.md`. Embedded SHA256: `1127ad366de39f1c9293bb54fa4fe9ca88183e3baf44d355262f031d73b6cb34`.
> [Thematic guide](../../topics/dephasing.md).

# An obstruction with no dark sector, distinct nontrivial eigenvalue ratios, and almost flat short powers

21 October 2026. This is a theorem about an **auxiliary deterministic sequence**, in dimensions $N=p^2$, where $p>3$ runs through the primes. It is not the family $e^{i\tau N A_N}M_N$ prescribed in the problem. In particular, none of the failures of $H_{\rm diag}$ below is a counterexample for that prescribed family.

The purpose is to settle a specific possible route to the missing signed estimate. Entry flatness, strong mixing of all physical powers up to a growing time, a vanishing reverse-transfer norm, distinct nontrivial ordered eigenvalue ratios, nonzero minors, absence of dark states, and the exact first-return mean do not jointly control the full signed spectral functional. All these properties can coexist with a limit equal to the empty process and with a pair defect tending to positive infinity.

There is also a quantitative return-theoretic conclusion: after a microscopic perturbation removes every dark state, nearly all first-return probability can remain at time $\sqrt N$, while nearly all of its normalized first moment lies after time $N^{12}$. Thus the exact first-moment identity cannot be used as a uniform integrability statement.

## 1. The base construction and the exact properties needed below

Work on $\mathbb C^{\mathbb F_p^2}$, with the coordinate order fixed lexicographically. Write $e_p(a)=\exp(2\pi i a/p)$. All fractions in finite-field exponents below denote inverses in $\mathbb F_p$. Let
$$
 (\mathcal F\psi)(k,l)=p^{-1}\sum_{x_1,x_2\in\mathbb F_p}
 e_p(kx_1+lx_2)\psi(x_1,x_2),
$$
and, for $t\in\mathbb F_p$, put
$$
 (V_t\psi)(k,l)
 =e_p\left(\frac{t l^2}{2}+\frac{t^2kl}{2}
                     +\frac{t^3k^2}{6}\right)\psi(k,l+tk).
 \tag{1.1}
$$
These are unitary: $V_t$ is a permutation followed by multiplication by phases, and Fourier orthogonality proves unitarity of $\mathcal F$. Direct expansion gives
$$
 P_t(k,l)+P_s(k,l+tk)=P_{t+s}(k,l),
$$
where $P_t$ denotes the polynomial in (1.1). Consequently
$$
 V_tV_s=V_{t+s},\qquad
 U_t=\mathcal F^*V_t\mathcal F,\qquad U_tU_s=U_{t+s}.
 \tag{1.2}
$$
Set $U^{(0)}_N=U_1$. In particular $(U^{(0)}_N)^p=I$, and its entries are algebraic numbers.

For completeness, the other two properties used here follow from the same explicit formula. For $t\ne0$, the kernel is
$$
 (U_t)_{xy}=p^{-2}\sum_{k,l\in\mathbb F_p}
 e_p\left(\frac12(k,l)H_t(k,l)^T+(k,l)(L_ty-x)\right),
 \tag{1.3}
$$
where
$$
 H_t=\begin{pmatrix}t^3/3&t^2/2\\t^2/2&t\end{pmatrix},
 \qquad L_t=\begin{pmatrix}1&t\\0&1\end{pmatrix},
 \qquad\det H_t=t^4/12\ne0.
$$
For any invertible symmetric $2$-by-$2$ matrix $H$, the squared modulus of its quadratic exponential sum is $p^2$. Indeed, after setting one summation vector equal to the other plus $h$, the sum over the other vector is
$\sum_v e_p(v^THh)$, which vanishes unless $h=0$. Completing the square in (1.3) therefore proves
$$
 |(U_t)_{xy}|=p^{-1}=N^{-1/2}\qquad(t\ne0).
 \tag{1.4}
$$
In particular, if $J_N$ is the matrix whose entries are $1/N$,
$$
 |(U_N^{(0)})^n|^{\circ2}
 =\begin{cases}J_N,&p\nmid n,\\ I_N,&p\mid n.\end{cases}
 \tag{1.5}
$$

Define the reverse-transfer matrix of a unitary $U$ by
$$
 Q(U)_{xy}=U_{xy}\overline{U_{yx}}.
$$
Completing the square also shows that the mixed endpoint term in the phase of $(U_t)_{xy}$ is $x^TC_ty$, with
$$
 C_t=H_t^{-1}L_t
 =\begin{pmatrix}12/t^3&6/t^2\\-6/t^2&-2/t\end{pmatrix}.
$$
Thus $Q(U_t)$, up to multiplication on both sides by diagonal unitaries, has entries
$p^{-2}e_p(x^T(C_t-C_t^T)y)$. The alternating matrix $C_t-C_t^T$ has determinant $(12/t^2)^2\ne0$. Fourier orthogonality yields
$$
 \|Q(U_t)\|_{\rm op}=p^{-1}=N^{-1/2}\qquad(t\ne0).
 \tag{1.6}
$$
The statements (1.2), (1.5), and (1.6), together with algebraicity, are the complete input from the base construction. In particular no metaplectic representation theorem or restriction on $p\bmod3$ is used.

## 2. A deterministic choice of a nearby algebraic eigenbasis

Choose an algebraic unitary matrix $V$ such that
$$
 U_N^{(0)}=V\operatorname{diag}(\lambda_0,\ldots,\lambda_{N-1})V^*,
 \qquad \lambda_j^p=1.
 \tag{2.1}
$$
Here and below repeated $\lambda_j$'s are retained with their multiplicities. An algebraic choice exists without any simplicity assumption. The spectral projectors for the distinct roots that occur in (2.1) are polynomials in $U_N^{(0)}$ with algebraic coefficients. Choose the first linearly independent columns of each such projector in the fixed coordinate order and apply Gram--Schmidt. All operations, including the positive square roots of positive real algebraic squared norms, stay within the algebraic numbers. Ordering the roots by their representatives $0,\ldots,p-1$ makes this a deterministic rule.

Fix the positive rational numbers
$$
 \eta_N=N^{-12},\qquad \varepsilon_N=2^{-N}\eta_N.
 \tag{2.2}
$$
There exists an algebraic unitary matrix $G$ with
$$
 \|G-I\|_{\rm HS}<\eta_N
 \tag{2.3}
$$
such that $H=GV$ satisfies both of the following:

1. Every square minor $\det H[I,J]$, for equally sized nonempty index sets $I,J$, is nonzero.
2. The intensity matrix
   $$
   \mathcal B_H=(|H_{vj}|^2)_{v,j=0}^{N-1}
   \tag{2.4}
   $$
   has nonzero determinant.

Here is a proof that also specifies a deterministic selection. For each individual minor, its squared modulus is a real-analytic function of the entries of $G$ on $U(N)$. It is not identically zero: $H$ can be chosen to be a permutation matrix mapping the column index set to the row index set. Likewise $\det\mathcal B_H$ is not identically zero, since it equals one at $H=I$.

A nonzero real-analytic function on $U(N)$ cannot vanish on an open set. One direct justification of the needed continuation is as follows. Any two unitaries $G_0,G_1$ are joined by an analytic curve $G_0e^{itA}$, $0\le t\le1$, for some Hermitian $A$: diagonalize $G_0^*G_1$ and choose real arguments of its eigenvalues. If a function vanishes on a neighborhood of $G_0$, its restriction to this curve vanishes for a nonempty interval and hence on the full curve by the elementary one-variable analytic identity theorem. It would then vanish at every $G_1$, a contradiction. It follows that each of the required nonzero conditions defines an open dense subset, and their finite intersection is open dense. This intersection meets the ball (2.3).

Finally, algebraic unitaries are dense near the identity. The Cayley map
$$
 A\longmapsto (I+iA)(I-iA)^{-1}
 \tag{2.5}
$$
is a local analytic bijection from Hermitian matrices near zero to unitary matrices near the identity. Hermitian matrices with rational diagonal entries and off-diagonal entries in $\mathbb Q(i)$ are dense; their Cayley transforms have algebraic, indeed $\mathbb Q(i)$, entries. Fix an enumeration of these rational Hermitian matrices and take the first Cayley transform satisfying (2.3) and the finitely many nonzero conditions. Existence follows from the established open density. These are exact tests on algebraic numbers; using the Hilbert--Schmidt norm in (2.3) avoids any need to select approximate singular values. This defines $G$, and hence $H$, without randomness or unspecified exceptional choices.

## 3. Microscopic spectral splitting and exact nondegeneracy

Define the auxiliary unitary
$$
 \widetilde U_N
 =H\operatorname{diag}\bigl(\lambda_j e^{i\varepsilon_N2^j}\bigr)_{j=0}^{N-1}H^*.
 \tag{3.1}
$$
Since $|e^{ix}-1|\le |x|$ for real $x$,
$$
 \delta_N:=\|\widetilde U_N-U_N^{(0)}\|_{\rm op}
 \le 2\|G-I\|_{\rm op}+\varepsilon_N2^{N-1}
 <\frac52\eta_N<3N^{-12}.
 \tag{3.2}
$$

The one external transcendence theorem used in this note is the qualitative Lindemann--Weierstrass theorem in Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the Exponentials of Algebraic Numbers*, ISSAC 2022, Theorem 1.1, DOI [10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170). Its [author PDF](https://arxiv.org/pdf/2112.05004), version 2, page 1, was opened on 21 October 2026. The theorem says that a nontrivial linear combination over the algebraic numbers of exponentials with distinct algebraic exponents cannot vanish. In particular, $e^a$ is transcendental when $a\ne0$ is algebraic: otherwise the two exponents $0,a$ would violate that statement.

### 3.1 Simple eigenvalues and pairwise distinct ordered ratios

For $j\ne k$,
$$
 \frac{\widetilde\lambda_j}{\widetilde\lambda_k}
 =\frac{\lambda_j}{\lambda_k}
    e^{i\varepsilon_N(2^j-2^k)}
 \tag{3.3}
$$
is transcendental. Indeed the first factor is nonzero algebraic and the exponent of the second is a nonzero algebraic number. Thus it is not one, proving simplicity; it is not a root of unity either.

Moreover, all the $N(N-1)$ ordered ratios in (3.3) are distinct. Equality for $(j,k)$ and $(l,m)$ would make
$e^{i\varepsilon_N(2^j-2^k-2^l+2^m)}$ algebraic. The transcendence consequence just checked forces
$2^j-2^k=2^l-2^m$. Nonzero ordered differences of powers of two are distinct: their sign specifies the orientation; for a positive difference the exponent of two dividing it gives the smaller index, after which the larger index is determined. Therefore $(j,k)=(l,m)$.

These conclusions hold at the displayed matrix $\widetilde U_N$, not merely at almost every choice of some additional phases. In particular, no positive power of $\widetilde U_N$ is a scalar matrix.

They are pairwise statements, not an assertion that all higher multiplicative resonances are absent. The binary choice retains higher integer relations: for $j+2<N$,
$2\cdot2^j-3\cdot2^{j+1}+2^{j+2}=0$, so
$(\widetilde\lambda_j^2\widetilde\lambda_{j+1}^{-3}\widetilde\lambda_{j+2})^p=1$
after the algebraic base roots are removed by the $p$-th power. None of the proofs uses absence of such higher relations.

### 3.2 Every square minor is nonzero

For equally sized nonempty index sets $I,J$, Cauchy--Binet gives the exact finite expansion
$$
 \det\widetilde U_N[I,J]
 =\sum_{\substack{S\subset\{0,\ldots,N-1\}\\|S|=|I|}}
 \det H[I,S]\,\overline{\det H[J,S]}
 \left(\prod_{j\in S}\lambda_j\right)
 e^{i\varepsilon_N\sum_{j\in S}2^j}.
 \tag{3.4}
$$
Every coefficient is nonzero algebraic by the choice of $H$. The exponents are algebraic and pairwise distinct, since different subsets have different binary sums. Lindemann--Weierstrass therefore applies directly and proves
$$
 \det\widetilde U_N[I,J]\ne0
 \quad\text{for every square minor.}
 \tag{3.5}
$$
This includes all entries and all leading principal minors. No lower bound on the sizes of these minors is asserted.

The same proof works for every nonzero integer power $\widetilde U_N^q$: replace $\lambda_j$ by $\lambda_j^q$ and $\varepsilon_N$ by $q\varepsilon_N$. All coefficients remain nonzero algebraic and all subset exponents remain distinct. The conclusions of Section 3.1 also persist under this replacement. Thus every nonzero power has simple spectrum, distinct nontrivial ordered ratios, and every square minor nonzero.

## 4. The physical powers remain nearly flat through time $\sqrt N-1$

For every positive integer $n$, telescoping powers of unitaries gives
$$
 \|\widetilde U_N^n-(U_N^{(0)})^n\|_{\rm op}\le n\delta_N.
 \tag{4.1}
$$
For $1\le n<p$, (1.4) and (4.1) imply
$$
 \max_{a,b}|(\widetilde U_N^n)_{ab}|
 \le N^{-1/2}+n\delta_N.
 \tag{4.2}
$$
Entrywise,
$$
 \left|| (\widetilde U_N^n)_{ab}|^2-N^{-1}\right|
 \le 2N^{-1/2}n\delta_N+n^2\delta_N^2.
$$
The operator norm of an $N$-by-$N$ matrix is at most $N$ times its largest absolute entry. Therefore
$$
 \max_{1\le n<p}
 \bigl\||\widetilde U_N^n|^{\circ2}-J_N\bigr\|_{\rm op}
 \le 2N\delta_N+N^2\delta_N^2\longrightarrow0.
 \tag{4.3}
$$
Thus the number of controlled physical powers grows with $N$; it is not just any fixed list.

For the reverse transfer, write $D=\widetilde U_N-U_N^{(0)}$. Expanding one of the two factors in each entry gives
$$
 \|Q(\widetilde U_N)-Q(U_N^{(0)})\|_{\rm HS}
 \le \bigl(2N^{-1/2}+\delta_N\bigr)\|D\|_{\rm HS}
 \le 2\delta_N+\sqrt N\delta_N^2.
$$
Together with (1.6),
$$
 \|Q(\widetilde U_N)\|_{\rm op}
 \le N^{-1/2}+2\delta_N+\sqrt N\delta_N^2\longrightarrow0.
 \tag{4.4}
$$
In fact the same argument applied to (4.1) and (1.6) gives the stronger uniform bound
$$
 \max_{1\le n<p}\|Q(\widetilde U_N^n)\|_{\rm op}
 \le N^{-1/2}+2p\delta_N+\sqrt Np^2\delta_N^2
 \longrightarrow0.
 \tag{4.5}
$$

## 5. Absence of dark states at the actual auxiliary matrix

For a finite unitary $U$, let $W=U\otimes\overline U$, let $\Pi$ be the orthogonal projection onto the span of the coordinate pair vectors $e_v\otimes\overline{e_v}$, and put $O=I-\Pi$. Relative to $\operatorname{ran}\Pi\oplus\operatorname{ran}O$, write
$$
 W=\begin{pmatrix}P&B\\ C&S\end{pmatrix},
 \qquad P=|U|^{\circ2},\quad S=OWO.
 \tag{5.1}
$$
A unit-modulus eigenvector of $S$ is an eigenvector of $W$ lying in $\operatorname{ran}O$. Indeed if $Sv=\zeta v$, $|\zeta|=1$, then
$\|Wv\|^2=\|\Pi Wv\|^2+\|Sv\|^2=\|v\|^2$
forces $\Pi Wv=0$. Conversely a $W$ eigenvector lying in $O$ is such an $S$ eigenvector. A dark reducing subspace, on which $S$ is unitary, exists if and only if at least one such eigenvector exists, since its finite-dimensional unitary restriction can be diagonalized.

For $U=\widetilde U_N$, eigenvectors of $W$ are
$h_j\otimes\overline{h_k}$, with eigenvalues $\widetilde\lambda_j/\widetilde\lambda_k$, where $h_j$ are the columns of $H$. By Section 3, every eigenvalue other than one has a one-dimensional eigenspace. Its projection onto $\Pi$ is the vector with components
$H_{vj}\overline{H_{vk}}$, all of which are nonzero by the choice of $H$.

The eigenspace for the eigenvalue one is exactly
$\operatorname{span}\{h_j\otimes\overline{h_j}:0\le j<N\}$.
Projection onto $\Pi$ sends its coefficient vector $c$ to $\mathcal B_Hc$, and is injective because $\det\mathcal B_H\ne0$. Consequently no eigenspace has a nonzero vector annihilated by $\Pi$, and
$$
 \mathcal H_{\rm dark}(\widetilde U_N)=\{0\}.
 \tag{5.2}
$$
All eigenvalues of $S$ then have modulus strictly less than one. Its powers tend to zero: Jordan blocks are a fixed-degree polynomial in the power index times a decaying geometric sequence. This is a fixed-$N$ conclusion; no decay rate uniform in $N$ follows.

## 6. Exact return probability and a first moment beyond $N^{12}$

Define the first-return operators on the $N$-dimensional range of $\Pi$ by
$$
 F_1=P,\qquad F_r=BS^{r-2}C\quad(r\ge2).
 \tag{6.1}
$$
There are $r$ copies of $W$ in $F_r$, with a projection $O$ between consecutive copies and endpoint projections $\Pi$.

For clarity, the normalization and mean used below have an elementary finite-dimensional proof. Unitarity gives
$P^*P+C^*C=I$, $B^*B+S^*S=I$, and $CC^*+SS^*=I$. Telescoping yields
$$
 \sum_{r=1}^{m+1}F_r^*F_r=I-C^*S^{*m}S^mC.
 \tag{6.2}
$$
For the matrix in Section 5 the remainder tends to zero. With $a_m=\|S^m\|_{\rm HS}^2$, it follows that
$$
 \sum_{r\ge1}\|F_r\|_{\rm HS}^2=N,\qquad
 \sum_{r>m}\|F_r\|_{\rm HS}^2
 =\|S^{m-1}C\|_{\rm HS}^2=a_{m-1}-a_m.
 \tag{6.3}
$$
The last equality uses $CC^*=I-SS^*$. Since $a_m\to0$, nonnegative tail summation gives
$$
 \sum_{r\ge1}r\|F_r\|_{\rm HS}^2
 =N+\sum_{m\ge1}(a_{m-1}-a_m)
 =N+(N^2-N)=N^2.
 \tag{6.4}
$$
Thus
$$
 \nu_N(r)=N^{-1}\|F_r(\widetilde U_N)\|_{\rm HS}^2
 \tag{6.5}
$$
is a probability distribution on the positive integers with exact mean $N$.

For the base matrix, the unrestricted returns are (1.5). Splitting a path at its first return proves the exact formal renewal relation
$$
 R(z)=\sum_{n\ge0}z^n\Pi W^n\Pi
       =\left(I-\sum_{r\ge1}z^rF_r\right)^{-1}.
$$
In (1.5), the two complementary projections $J_N$ and $I-J_N$ give
$$
 R(z)=\frac{J_N}{1-z}+\frac{I-J_N}{1-z^p}.
$$
Its inverse can be read off on the two projection ranges, proving the all-time identity
$$
 F_1(U_N^{(0)})=J_N,\qquad F_p(U_N^{(0)})=I-J_N,
 \qquad F_r(U_N^{(0)})=0\quad(r\ne1,p).
 \tag{6.6}
$$

The doubled matrices obey
$\|\widetilde W-W^{(0)}\|_{\rm op}\le2\delta_N$.
Telescoping the $r$ unitary factors, all intervening projections being contractions, proves
$$
 \|F_r(\widetilde U_N)-F_r(U_N^{(0)})\|_{\rm op}
 \le2r\delta_N,
\quad
 \|F_r(\widetilde U_N)-F_r(U_N^{(0)})\|_{\rm HS}
 \le2r\sqrt N\delta_N.
 \tag{6.7}
$$
In particular
$$
 \nu_N(p)\ge
 \left(\sqrt{1-\frac1N}-2p\delta_N\right)^2
 \longrightarrow1.
 \tag{6.8}
$$
The expression in parentheses is positive for the parameters used here. Because $P$ is doubly stochastic, $P-J_N$ is Hilbert--Schmidt orthogonal to $J_N$, so
$\|P\|_{\rm HS}^2=1+\|P-J_N\|_{\rm HS}^2\ge1$.
Therefore $\nu_N(1)\ge1/N$, and (6.8) yields the stronger estimate
$$
 \nu_N\bigl(\mathbb N\setminus\{1,p\}\bigr)
 \le4p\delta_N\le12N^{-23/2}.
 \tag{6.9}
$$

Let $X_N=r/N$ under the law $\nu_N$. From (6.8), $X_N$ converges in probability to zero, whereas (6.4) gives $\mathbb E X_N=1$ exactly. More quantitatively, (6.9) implies
$$
\begin{aligned}
 \mathbb E\bigl[X_N\mathbf1_{\{r\le N^{12}\}}\bigr]
 &\le \frac pN
   +\frac{N^{12}}N\nu_N\bigl(\mathbb N\setminus\{1,p\}\bigr)\\
 &\le\frac{13}{\sqrt N}.
\end{aligned}
$$
Consequently
$$
 \boxed{\quad
 1-\frac{13}{\sqrt N}
 \le\frac1{N^2}\sum_{r>N^{12}}r\|F_r(\widetilde U_N)\|_{\rm HS}^2
 \le1.
 \quad}
 \tag{6.10}
$$
The conclusion is about the full first-return sequence at the actual displayed matrix. It does not use a phase average.

In particular $(X_N)$ is not uniformly integrable. For every fixed $B>0$, once $p/N<B$,
$$
 \mathbb E[X_N\mathbf1_{\{X_N\le B\}}]
 \le p/N+B(1-\nu_N(p))\longrightarrow0,
$$
and hence $\mathbb E[X_N\mathbf1_{\{X_N>B\}}]\to1$. The exact mean alone therefore supplies no useful uniform cutoff at a fixed multiple of $N$.

The power 12 is not intrinsic. In (2.2) one can choose any positive rational $\eta_N\le N^{-12}$ and put $\varepsilon_N=2^{-N}\eta_N$. The proofs are unchanged. Replacing the cutoff in (6.10) by $\eta_N^{-1}$ gives the same lower bound, because $\delta_N\le3\eta_N$. The escaping mean can therefore be placed beyond any preassigned polynomial scale, or beyond a rationally specified exponential scale. This observation concerns the auxiliary construction only.

## 7. The local process tends to the empty process

Write $\lambda_j=e^{2\pi i a_j/p}$, with $a_j\in\{0,\ldots,p-1\}$. A representative of the perturbed eigenphase is
$$
 \widetilde\theta_j=\frac{a_j}{p}
                    +\frac{\varepsilon_N2^j}{2\pi}\pmod1.
 \tag{7.1}
$$
The second term lies between zero and
$\rho_N=\eta_N/(4\pi)$. Thus all eigenvalues lie in at most $p$ clusters whose phase diameters are at most $\rho_N$.

For uniform $\alpha\in[0,1)$, let $\widetilde\Xi_{N,\alpha}$ be the periodic unfolded point measure defined in the problem, using $\widetilde U_N$. If this measure has a point in $[-L,L]$, then $\alpha$ lies at circular distance at most $L/N+\rho_N$ from one of the $p$ roots $a/p$. Therefore
$$
 \mathbb P_\alpha\{\widetilde\Xi_{N,\alpha}([-L,L])>0\}
 \le2p(L/N+\rho_N)
 =\frac{2L}{p}+2p\rho_N\longrightarrow0.
 \tag{7.2}
$$
Every finite collection of compactly supported continuous test functions has its supports contained in some $[-L,L]$. On the event in which that interval is empty all corresponding integrals are zero. The neighborhoods defining the vague topology therefore give
$$
 \widetilde\Xi_{N,\alpha}\longrightarrow0
 \quad\text{in probability in the vague topology.}
 \tag{7.3}
$$
Here 0 denotes the empty point measure. In particular the limit is not $\mathrm{Sine}_2$. The exact intensity remains one for every $N$; the interval counts are not uniformly integrable.

## 8. Every nonzero admissible pair test has a divergent defect

Fix any nonzero nonnegative real Schwartz function $b$ satisfying the admissibility conditions in the problem. Put
$$
 C_b(t)=\int_{\mathbb R}b(x)b(x+t)\,dx,
 \qquad C_b(0)=\|b\|_2^2>0,
 \qquad H_b=\int_{\mathbb R}b(x)\,dx.
$$
The function $C_b$ is nonnegative and continuous. Expanding the periodizations, using nonnegativity to interchange sums and integrals, and then unfolding one of the two period indices gives the exact identity
$$
 \int_0^1 b_N(\theta_i-\alpha)b_N(\theta_j-\alpha)\,d\alpha
 =\frac1N\sum_{\ell\in\mathbb Z}
 C_b\bigl(N(\theta_i-\theta_j+\ell)\bigr).
 \tag{8.1}
$$
Let $m_a$ be the number of indices with base phase $a/p$, including zero multiplicities, so $\sum_{a=0}^{p-1}m_a=N$. For two distinct indices in one cluster, choose the representatives (7.1). Their unfolded difference is at most $N\rho_N\to0$. By continuity, the corresponding term on the right of (8.1) is at least $C_b(0)/(2N)$ for all sufficiently large $N$.

Keeping only these ordered same-cluster pairs in the definition of $M_{2,N}$, and retaining its factor $1/2$, gives
$$
 M_{2,N}^{\widetilde U}(b)
 \ge\frac{C_b(0)}{4N}\sum_{a=0}^{p-1}m_a(m_a-1).
$$
Cauchy--Schwarz gives $\sum_a m_a^2\ge N^2/p$. Since $N=p^2$,
$$
 M_{2,N}^{\widetilde U}(b)
 \ge\frac{C_b(0)}4(p-1).
 \tag{8.2}
$$
The exact CUE positive-matrix estimate from the problem is
$M_{2,N}^{\rm CUE}(b)\le H_b^2/2$. Hence
$$
 \boxed{\quad
 \Delta_{2,N}^{\widetilde U}(b)
 \ge\frac{\|b\|_2^2}{4}(p-1)-\frac{H_b^2}{2}
 \longrightarrow+\infty.
 \quad}
 \tag{8.3}
$$
The test $b$ is fixed independently of $N$. The argument applies to every nonzero admissible $b$, not to an $N$-dependent shrinking Fourier band. The Fourier form of the same conclusion is divergence of the full signed, weighted pair form-factor difference. It is not an estimate obtained by replacing that signed sum by a sum of absolute values.

### 8.1 The exact leading coefficient also survives the perturbation

Let $w(u)=|\widehat b(u)|^2$, with support in $[-B,B]$. The exact pair formula in the problem gives
$$
 \Delta_{2,N}^{U}(b)
 =N^{-2}\sum_{n\ge1}w(n/N)
       \bigl(|\operatorname{Tr}U^n|^2-\min(n,N)\bigr).
 \tag{8.4}
$$
For two unitaries at operator distance $\delta_N$, (4.1) implies
$$
 \bigl||\operatorname{Tr}\widetilde U_N^n|^2
       -|\operatorname{Tr}(U_N^{(0)})^n|^2\bigr|
 \le 2N^2 n\delta_N.
$$
Consequently the full signed functional differs by
$$
 |\Delta_{2,N}^{\widetilde U}(b)-\Delta_{2,N}^{U^{(0)}}(b)|
 \le2\delta_N\sum_{1\le n\le BN}n w(n/N)
 =O_b(N^2\delta_N)=O_b(N^{-10}).
 \tag{8.5}
$$
This estimate is used to compare an exactly evaluated auxiliary matrix with its perturbation; it is not a proposed bound for the original family.

The base trace is elementary. For $t\ne0$, the fixed coordinates in the permutation defining $V_t$ have $k=0$, so
$$
 \operatorname{Tr}U_t=\sum_{l\in\mathbb F_p}e_p(tl^2/2),
 \qquad |\operatorname{Tr}U_t|^2=p.
$$
The second equality follows by the same difference-sum calculation as in Section 1, in one dimension. At $t=0$, $U_t=I$. Thus, for $N=p^2$,
$$
 N^{-2}\sum_{n\ge1}w(n/N)|\operatorname{Tr}(U_N^{(0)})^n|^2
 =\sum_{r\ge1}w(r/p)
  +p^{-3}\sum_{\substack{n\ge1\\p\nmid n}}w(n/p^2).
$$
The last term is $O_b(p^{-1})$; the first is
$p\int_0^\infty w(u)\,du+O_b(1)$, by a Riemann sum. The CUE part of (8.4) is bounded independently of $N$. Combining with (8.5) proves the exact asymptotic
$$
 \boxed{\quad
 \frac{\Delta_{2,N}^{\widetilde U}(b)}{\sqrt N}
 \longrightarrow\int_0^\infty|\widehat b(u)|^2\,du>0.
 \quad}
 \tag{8.6}
$$
Positivity follows already from $\widehat b(0)=\int b>0$ and continuity.

## 9. Exact scope of the obstruction

The single deterministic sequence (3.1) has, simultaneously:

- entry bounds asymptotic to the perfectly flat bound, and physical probability matrices converging to $J_N$, uniformly for every $1\le n<\sqrt N$;
- reverse-transfer operator norm tending to zero, uniformly for those same powers;
- simple spectrum and distinct nontrivial ordered eigenvalue ratios;
- transcendental nontrivial eigenvalue ratios and no exact scalar period;
- every square minor of every nonzero power nonzero, fully supported eigenvectors, and an invertible eigenvector intensity matrix;
- no dark reducing subspace for the diagonal-pair return problem;
- exact first-return normalization and mean $\sum r\|F_r\|_{\rm HS}^2=N^2$;
- almost all first-return probability at $r=\sqrt N$, while almost all normalized first moment lies after $N^{12}$;
- an empty local weak limit and a divergent pair defect with the exact positive leading coefficient (8.6) for every fixed nonzero admissible test.

This rules out deducing the desired signed trace cancellation from that collection of properties alone. In particular, simply appending qualitative simplicity, transcendence, nonzero principal minors, or absence of dark states does not repair a proof based on short physical powers and return-energy identities.

The construction does not share the exact Weyl polynomial, Gaussian kernel, fixed classical perturbation, or all-odd arithmetic quantization of the problem. A successful argument for that original family must use further quantitative structure that excludes the microscopic coherent clusters constructed here. Nothing in this note establishes or refutes the required original estimate
$$
 \frac1{N^2}\sum_{n\ge1}|\widehat b(n/N)|^2
 \bigl(|\operatorname{Tr}U_N^n|^2-\min(n,N)\bigr)\longrightarrow0,
$$
even before the higher orders of $H_{\rm diag}$ are considered. That original signed estimate remains an open step in the work.
