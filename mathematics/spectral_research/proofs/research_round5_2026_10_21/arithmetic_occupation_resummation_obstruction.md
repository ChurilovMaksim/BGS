> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/arithmetic_occupation_resummation_obstruction.md`. Embedded SHA256: `1aeefa2931e83e4368ecdc4b5b0aa3b31c81beef8eb6fbb69ea825e08e5b0556`.
> [Thematic guide](../../topics/histories.md).

# Exact occupation resummation and the remaining cross-sector phases

21 October 2026. Exploratory algebraic completion of the directed-arc investigation. The original fixed $\tau=10^{-80}$, the prescribed $U_N$, and all odd dimensions remain unchanged.

This note proves finite identities and identifies their precise scope. It gives a complete coherent resummation across all edge arrays with the same vertex occupation vector. It does not evaluate the resulting coefficients at Heisenberg times, does not prove or refute $H_{\rm diag}$, and makes no claim of historical novelty for the log-determinant identity.

## 1. Rooted words and occupation sectors

For any $N\times N$ matrix $U$, an integer $n\ge1$, and a rooted cyclic word $x=(x_0,\ldots,x_{n-1})$, with $x_n=x_0$, define
$$
 a_U(x)=\prod_{j=0}^{n-1}U_{x_j,x_{j+1}},\qquad
 d_v(x)=\#\{j:x_j=v\},
$$
$$
 L_{uv}(x)=\#\{j:(x_j,x_{j+1})=(u,v)\}.
$$
Thus
$$
 \sum_vd_v(x)=n,\qquad d_v(x)=\sum_wL_{vw}(x)=\sum_wL_{wv}(x).
 \tag{1.1}
$$
Words here are actual ordered vertex lists, with no division by rotations, periods, edge labels, or factorials.

For $d\in\mathbb Z_{\ge0}^N$, $|d|=n$, put
$$
 A_{n,d}(U)=\sum_{x:\,d(x)=d}a_U(x).
 \tag{1.2}
$$
The matrix product formula gives
$$
 p_n(U)=\operatorname{Tr}U^n=\sum_{|d|=n}A_{n,d}(U).
 \tag{1.3}
$$

Every literal reordering of directed arcs partitions and permutes the existing vertex occurrences, and therefore preserves $d$. In the last-exit construction which preserves every directed edge multiplicity, preservation of $d$ follows directly from (1.1). Increasing the number of cuts to a positive fraction of $n$, or even to $n$, does not remove this invariant. This statement concerns these specified combinatorial operations; it does not assert that every possible use of unitarity preserves occupations term by term.

## 2. An exact resummation including different edge arrays

Let $z_0,\ldots,z_{N-1}$ be commuting formal variables and $Z=\operatorname{diag}(z_0,\ldots,z_{N-1})$. Set
$$
 D_U(z)=\det(I-ZU).
$$
Its constant term is $1$, so its formal logarithm at the origin is well defined. Then
$$
 \boxed{
 A_{n,d}(U)=n[z^d]\{-\log D_U(z)\},\qquad |d|=n.
 }
 \tag{2.1}
$$
In particular, (2.1) sums all directed edge arrays compatible with $d$, with their exact original complex amplitudes.

Here is a direct proof of the identity and its normalization. Introduce one more formal variable $t$. The adjugate formula for the derivative of a determinant gives
$$
 -\frac{d}{dt}\log\det(I-tZU)
   =\operatorname{Tr}((I-tZU)^{-1}ZU)
   =\sum_{m\ge1}t^{m-1}\operatorname{Tr}(ZU)^m.
$$
The inverse is a formal geometric series; every coefficient uses finitely many operations. Both sides integrate with zero constant term, hence
$$
 -\log\det(I-tZU)
   =\sum_{m\ge1}\frac{t^m}{m}\operatorname{Tr}(ZU)^m.
 \tag{2.2}
$$
The word expansion of the trace is
$$
 \operatorname{Tr}(ZU)^m
   =\sum_{|e|=m}A_{m,e}(U)z^e.
$$
Comparing the coefficient $t^nz^d$ proves (2.1), including repeated words and periodic words.

Multilinearity of the determinant also gives
$$
 D_U(z)=\sum_{S\subset\{0,\ldots,N-1\}}
       (-1)^{|S|}\det(U_{S,S})\prod_{v\in S}z_v.
 \tag{2.3}
$$
To check this formula, choose the $I$-row or the $-ZU$-row in each row of the determinant. The identity rows outside $S$ force the same columns there; expansion along those rows leaves the principal submatrix indexed by $S$, with sign $(-1)^{|S|}$. Thus the exact occupation amplitudes are determined by coefficients of the logarithm of the finite multiaffine principal-minor polynomial (2.3). No nonvanishing assumption on those minors is used.

## 3. The complete within-occupation signed sum

Define the finite sums
$$
 \mathcal O_n(U)=
 \sum_{x,y:\,d(x)=d(y)}a_U(x)\overline{a_U(y)}
 =\sum_{|d|=n}|A_{n,d}(U)|^2,
 \tag{3.1}
$$
$$
 \Omega_n(U)=
 \sum_{x,y:\,d(x)\ne d(y)}a_U(x)\overline{a_U(y)}.
 \tag{3.2}
$$
Both are real, because each indexing set is invariant under exchanging $x,y$, and
$$
 |p_n(U)|^2=\mathcal O_n(U)+\Omega_n(U).
 \tag{3.3}
$$
In particular $\mathcal O_n(U)\ge0$, although the individual terms inside (3.1) can have either sign.

For a unitary $U$,
$$
 \boxed{0\le\mathcal O_n(U)\le N^2.}
 \tag{3.4}
$$
The proof is exact Fourier coefficient extraction. Let
$$
 D_\theta=\operatorname{diag}(e^{i\theta_0},\ldots,e^{i\theta_{N-1}}),
 \qquad \theta\in[0,2\pi)^N.
$$
Each departure from $v$ adds a factor $e^{i\theta_v}$, so
$$
 \operatorname{Tr}(D_\theta U)^n
   =\sum_{|d|=n}A_{n,d}(U)e^{id\cdot\theta}.
 \tag{3.5}
$$
Orthogonality of the finite family of torus characters gives
$$
 \mathcal O_n(U)
 =\int_{[0,2\pi)^N}|\operatorname{Tr}(D_\theta U)^n|^2
                  \prod_v\frac{d\theta_v}{2\pi}.
 \tag{3.6}
$$
For every $\theta$, $D_\theta U$ is unitary and its power has trace of modulus at most $N$, proving (3.4).

Equation (3.6) is an algebraic tool to bound the exact original sum (3.1). The task's ensemble has not been changed: we do not replace $|p_n(U_N)|^2$ by this auxiliary phase integral.

### Consequence for the original exponential coherent class

Let
$$
 \mathcal F_n(U)=\sum_{x,y:\,L(x)=L(y)}
       a_U(x)\overline{a_U(y)}
$$
and let
$$
 \mathcal R_n(U)=
 \sum_{\substack{x,y:\,d(x)=d(y)\\L(x)\ne L(y)}}
       a_U(x)\overline{a_U(y)}.
$$
By (1.1), this is an exact disjoint decomposition
$$
 \mathcal O_n(U)=\mathcal F_n(U)+\mathcal R_n(U).
$$
Consequently every unitary matrix satisfies
$$
 \boxed{
 -\mathcal F_n(U)\le\mathcal R_n(U)
                  \le N^2-\mathcal F_n(U).
 }
 \tag{3.7}
$$
This localizes the necessary compensation to pairs with the same occupation vector but different edge arrays.

For the original family, the fully proved input in root_exponential_coherent_edge_classes.md, SHA256 001fd27ca128f1a00417838e0f4b07d7ad19f291e8c2c5fbb593e614d2ec29e0, gives, uniformly for $cN\le n\le BN$, $0<c\le B<\infty$, $s=n/N$,
$$
 \mathcal F_n(U_N)\ge
 \exp\left\{\frac{\log2}{6}e^{-s}s^3N-O_{c,B}(1)\right\}.
 \tag{3.8}
$$
Its hypotheses $\max |U_{uv}|^2\le9/N$ and
$\||U_{uv}|^2-J\|_{\rm op}\le1/2$ were established for all sufficiently large odd $N$ in the source's specified original-family inputs. Substituting (3.8) into (3.7) proves that the same-occupation, different-edge sum $\mathcal R_n(U_N)$ already supplies an exponentially large negative compensation.

This corollary uses the existing exponential theorem, not a newly computed spectral asymptotic. The polynomial-scale quantity $\mathcal O_n(U_N)$ is still unevaluated. In particular (3.7) does not control the desired $O(N)$ scale of $|p_n(U_N)|^2$ at $n\asymp N$.

## 4. The exact phase information which remains

The Fourier polynomial in (3.5) yields
$$
 |\operatorname{Tr}(D_\theta U)^n|^2
 =\sum_{\substack{|d|=|e|=n}}
       A_{n,d}(U)\overline{A_{n,e}(U)}
       e^{i(d-e)\cdot\theta}.
 \tag{4.1}
$$
The constant Fourier coefficient is exactly $\mathcal O_n(U)$. Its value at $\theta=0$ is $|p_n(U)|^2$, so their difference is exactly $\Omega_n(U)$.

All individual terms with $d(x)=d(y)$ are invariant under arbitrary row phases. Moreover
$$
 P(D_\theta U)=P(U),\qquad
 Q(D_\theta U)=D_\theta Q(U)D_\theta^*,
 \tag{4.2}
$$
where $P(U)_{xy}=|U_{xy}|^2$ and
$Q(U)_{xy}=U_{xy}\overline{U_{yx}}$.
These formulas follow entry by entry.

Thus the complete within-occupation pair data, $P$, and the unitary conjugacy invariants of $Q$ do not distinguish the members of the row-phase family. Formula (4.1) identifies precisely the additional data needed to evaluate its form factor at a specified row phase: the nonconstant Fourier coefficients indexed by $d-e$.

This is an obstruction to the proposed universal cancellation rule that all unequal-occupation terms vanish solely by unitarity or by the occupation-preserving pairing identities. It is not an obstruction to a new argument using further special structure of the prescribed $U_N$.

## 5. The candidate cancellation rule is not an exact identity for the original row-phase polynomial

For completeness, the nonconstant modes in (4.1) are nonzero for the actual original matrices. The short verification uses the same algebraic mechanism already proved in the no-exact-scalar-powers note.

Every entry of $A_N$ and $M_N$ is algebraic: roots of unity and $\sqrt N$ are algebraic, and the Fourier coefficients are algebraic because $e^{i\alpha_0}=(-3+4i)/5$. Let $\Lambda$ be the distinct eigenvalues of the Hermitian algebraic matrix $A_N$. They are algebraic, and its spectral projectors
$$
 P_\lambda=\prod_{\substack{\mu\in\Lambda\\\mu\ne\lambda}}
              \frac{A_N-\mu I}{\lambda-\mu}
$$
are algebraic matrices, even if eigenvalues have multiplicity. Hence
$$
 U_N(s)_{uv}=\sum_{\lambda\in\Lambda}
        (P_\lambda M_N)_{uv}\,e^{iN\lambda s}.
 \tag{5.1}
$$
At least one coefficient is nonzero, since their sum is
$(M_N)_{uv}\ne0$.

We use the following precise published theorem: Cheng-Chao Huang,
Explicit Bounds for Linear Forms in the Exponentials of Algebraic Numbers,
Proceedings of ISSAC 2022, Theorem 1.1, DOI
https://doi.org/10.1145/3476446.3536170.
The author version https://arxiv.org/pdf/2112.05004v2 (16 May 2022), page 1, was opened and checked on 21 October 2026; it displays the publication metadata and states the distinct-exponent Lindemann--Weierstrass theorem. This theorem says that exponentials of distinct algebraic numbers are linearly independent over the algebraic numbers.

Discard zero coefficients in (5.1). At $s=\tau=10^{-80}$, the remaining exponents $iN\lambda\tau$ are distinct algebraic numbers and the coefficients are nonzero algebraic numbers. All hypotheses are therefore verified, and
$$
 U_N(\tau)_{uv}\ne0
 \qquad\text{for every odd }N\ge3\text{ and all }u,v.
 \tag{5.2}
$$
No exclusion of $N=7$ is needed here.

Fix $u\ne v$. There is exactly one pair of nonnegative occupation vectors of total size $n$ with
$d-e=n(e_u-e_v)$: namely $d=ne_u$ and $e=ne_v$. Indeed its $u$-coordinate forces $d_u=n,e_u=0$, and its $v$-coordinate forces $e_v=n,d_v=0$; the total-size constraint forces all remaining coordinates to vanish. Each constant word has amplitude $U_{uu}^n$. Therefore the Fourier coefficient of (4.1) at this mode is exactly
$$
 \boxed{
 [e^{in(\theta_u-\theta_v)}]\,
 |\operatorname{Tr}(D_\theta U_N)^n|^2
       =U_{N,uu}^{\,n}\overline{U_{N,vv}^{\,n}}\ne0.
 }
 \tag{5.3}
$$
This proves that the original matrix's row-phase form factor is not constant, at every positive $n$. In particular there is no universal exact identity deleting all unequal-occupation modes.

Equation (5.3) makes no quantitative claim at $\theta=0$. It does not even assert $\Omega_n(U_N)\ne0$, since different nonzero modes could cancel there. In the available flat-entry range its displayed coefficient is at most $(9/N)^n$, which is superpolynomially small when $n\asymp N$. It provides no obstruction to the proposed spectral limit.

## 6. Exact remaining leaf

The complete determinant resummation (2.1) genuinely sums different edge classes at arbitrary numbers of changed centers. Bound (3.4) also proves their collective compensation of the exponential coherent class. The phase polynomial (4.1) shows why that completion still does not evaluate the original form factor.

For an admissible test $b$, the exact $k=2$ discrepancy is
$$
 \Delta_{2,N}(b)=\frac1{N^2}\sum_{n\ge1}
       |\widehat b(n/N)|^2
       \bigl(|p_n(U_N)|^2-\min(n,N)\bigr).
 \tag{6.1}
$$
Indeed in the problem's finite Fourier formula
$D(n,-n)=|p_n|^2-N$; the $n=0$ terms cancel against CUE and the positive and negative terms agree. The CUE second moment for $n>0$ is verified from its circular kernel $\sum_{j=0}^{N-1}e^{2\pi ij(x-y)}$: the diagonal terms contribute $N$, while the squared-kernel term subtracts the number of index pairs with difference $n$, namely $(N-n)_+$. The constant-density off-diagonal term integrates to zero. Thus the benchmark is $N-(N-n)_+=\min(n,N)$, as also established in section 7 of root_exact_identities_and_closure.md in the frozen round-4 proof collection.

In the present exact decomposition, the still unproved estimate is
$$
 \frac1{N^2}\sum_{n\ge1}|\widehat b(n/N)|^2
  \left\{\mathcal O_n(U_N)-\min(n,N)+\Omega_n(U_N)\right\}
 \longrightarrow0
 \tag{6.2}
$$
through all odd $N$. The sum is finite because $\widehat b$ has compact support. No separate smallness of its two brace terms has been proved or assumed. Even (6.2) would only establish the pair case; all higher $k$ required by $H_{\rm diag}$ would remain.

The raw identities here therefore finish this particular algebraic investigation without supplying the missing Heisenberg-time cancellation estimate.
