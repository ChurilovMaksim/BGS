> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/root_audit_phase_concentration.md`. Embedded SHA256: `be8b3f2d4cd1bc62ea6ab8385f5087c945d0ae861c3ea2181af0d41962994aec`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Second-reader audit: concentration and all-order isolated occupations

Date: 21 October 2026. Source:
`r6_dense_phasechaos_isolated_all_orders.md`, SHA256
`88bc04559c4961bb0441984b1f9df5fc1d0ab2f99349d603e171a67bac7bebbe`.
Reviewer: root. All sections, including the finite-band restriction and
the fixed-dimension example, were read and reconstructed.

**Verdict: the two finite estimates (1.5) and (1.6) are proved with their
stated band restrictions.** The stronger estimate is the one used below
for the original unequal-occupation class. This is a proof audit, not a
formal verification certificate.

## 1. The small operator difference is uniform

For $V(z)=U\operatorname{diag}(z)U$, replacing one coordinate gives
$V'=V+\delta z\,cr$, where $c=U_{:v}$, $r=U_{v:}$.
The difference of absolute squares is exactly
$$
\delta z\operatorname{diag}(c)\overline{V'}\operatorname{diag}(r)
+\overline{\delta z}\operatorname{diag}(\bar c)V\operatorname{diag}(\bar r).
$$
No random conditional bound is used: $V,V'$ are unitary for every phase
vector. Both diagonal factors have norm at most $\sqrt{C/N}$, so the
change is at most $4C/N$ in operator norm. Subtracting the deterministic
mean $P^2$ does not change this difference.

The self-adjoint dilation has dimension $2N$; every coordinate
difference has square at most $(4C/N)^2I$. The independent variables,
bounded measurability, fixed deterministic bounds, and centering all
meet Tropp's Corollary 7.5 exactly. The published theorem was personally
opened and its statement checked in *Foundations of Computational
Mathematics* 12 (2012), printed page 428:
<https://link.springer.com/content/pdf/10.1007/s10208-011-9099-z.pdf>.
The variance proxy is $16C^2/N$, and the theorem therefore gives
$$
\Pr(\|D(z)\|\ge s)\le2N\exp[-Ns^2/(128C^2)].
$$
Its largest-eigenvalue event is already the norm event for the dilation;
there is no extra two-sided-tail factor.

## 2. Exact class extraction and spectral-radius bounds

In the doubled space, deleting only off-diagonal-to-off-diagonal
transitions forbids precisely neighboring literal mismatches. The trace
expansion includes each rooted word pair once, even at the maximal
mismatch density and at the cyclic boundary. Phase integration keeps
exactly equal occupations. The empty mismatch class is $\operatorname{Tr}P^n$.

Block elimination gives the smaller companion
$$
\mathcal T=\begin{pmatrix}P&D\\ I&0\end{pmatrix},\qquad
D=|U\operatorname{diag}(z)U|^{\circ2}-P^2,
$$
where the block display means first row $(P,D)$ and second row
$(I,0)$. Its determinant and every positive-power trace agree with
the large transfer. This identity follows as a formal identity near
zero and requires no estimate on resolvents.

On the mean-zero block, an eigenvalue satisfies
$|\lambda|^2\le q|\lambda|+\|D\|$. The trace is the sum of eigenvalue
powers with algebraic multiplicity, including defective eigenvalues.
The resulting bound remains valid without normality. Also
$\|D\|\le1+q^2$ follows from stochastic contractivity on the
mean-zero space. The scalar inequalities
$r(q,1+q^2)\le1+q$ and $r(1/4,1/2)<7/8$ were checked directly.

## 3. Removing the dimension factor in the good event

The distinct characters $z_u\bar z_v$, $u\ne v$, have mutually
orthogonal coefficient matrices in phase $L^2$. Thus
$$
\mathbb E\|D\|_{\rm HS}^2
=\sum_{u\ne v}
  \left(\sum_aP_{au}P_{av}\right)
  \left(\sum_bP_{ub}P_{vb}\right)\le C.
$$
Together with $\|P-J\|_{\rm HS}^2\le C-1$, this proves the source's
$\mathbb EM\le2C-1$.

For a nonempty independent mismatch set, every $J$ term in the cyclic
expansion vanishes because $DJ=JD=0$. A pattern with $r$ mismatches
has $n-r$ factors after this exact cancellation. At $n\ge3$ there
are at least two factors. Schatten Cauchy--Schwarz with two factors in
Hilbert--Schmidt norm, and all the others in operator norm, gives
$M(z)(1/4)^{n-r-2}$ on the event $\|D\|\le1/4$.

The cyclic independent-set generating function was recomputed:
$$
\sum_{n\ge1}Z_n(a,b)s^n
=\frac{as+2bs^2}{1-as-bs^2}-\frac{as}{1-as}.
$$
At $a=b=1/4$, the sum through all positive lengths is $7/6$,
$Z_2=1/2$, and the sum for $n\ge3$ is $2/3$.
This gives the constant $32(2C-1)/3$.

On the bad event, $|G_n|\le3N(1+q)^n$, while its probability is at
most $2N e^{-N/(2048C^2)}$. For $n\le BN$ and
$Bq\le1/(4096C^2)$, the exponent is at most
$-N/(4096C^2)$. There are at most $BN$ terms. Dividing by $N^2$
therefore gives precisely
$$
\frac1{N^2}\sum_{n\le BN}|H_n^{\rm iso}|
\le\frac{32(2C-1)}{3N^2}
+6BN e^{-N/(4096C^2)}.
$$
The complete terms at $n=1,2$ vanish; no separate good-event claim is
made for those small lengths. The estimates used here are of fully
contracted signed pattern sums, not individual path-amplitude moduli.

## 4. Fixed parameter and the rare-phase obstruction

For the original family, the previous theorem gives
$q_N\le40000t+o(1)$ with fixed positive $t=10^{-80}/(2\pi)$.
It does not give $q_N\to0$. The legitimate eventual choice is
$\bar q=10^{-76}$, since $40000t=(2/\pi)10^{-76}<\bar q$.
Consequently the stronger estimate permits exactly the stated range
$$
B\le 10^{76}/331776\quad(C=9).
$$
This is a finite range. Its size supplies no proof for all fixed Fourier
bands. At fixed $N$, the bad-event estimate also cannot be extended to
arbitrarily large times under a general Abel weight of scale $N$.

The orthogonal $2\times2$ example was recomputed. Its nonconstant
defect eigenvalue is $(1-q^2)\cos\varphi$. In the cyclic polynomial,
all even powers survive phase integration with a central-binomial
coefficient at least $1/(n+1)$, and odd powers vanish. The positive
root $(q+\sqrt{4-3q^2})/2$ exceeds one for $0<q<1$. The asserted
exponential lower bound at even fixed-dimensional times follows.
This rules out a blanket polynomial cap for these signed subsets, but
does not provide any countersequence for the original matrix family.
