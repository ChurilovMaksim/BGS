> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/r6_original_audit_combined_gap2.md`. Embedded SHA256: `619b5ccb97f5d713eafb123555df9d4f768e391a78ac6c0946eaa6d0ab53cacd`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Independent audit of the complete isolated unequal-occupation sector

Date: 21 October 2026. Reviewer: `r6_original_obstruction`.

Audited source: `root_original_gap2_combined.md`, SHA256
`f764a95fddaccebfe5a84c231279e0c6036b9495cea9c0d752aa7e6fe1cf9ed2`.

Concentration source: `r6_dense_phasechaos_isolated_all_orders.md`, SHA256
`88bc04559c4961bb0441984b1f9df5fc1d0ab2f99349d603e171a67bac7bebbe`.

**Verdict.** The displayed estimate with constant 776 is valid for the
specified literal rooted-pair class, every sufficiently large odd
dimension, and every band
$0<B\le 10^{76}/331776$. The weighted conclusion follows even from
the stronger estimate on the sum of absolute values of the completely
contracted length contributions. No additional assumption is required.
This is an independent audit of the combination and the concentration
input, not a formal verification certificate. The physical two-step
input was proved by this reviewer and separately audited by the
occupation agent.

## 1. The two subtractions refer to the same rooted class

For an ordered pair of rooted words $x,y$ of length $n$, let
$I(x,y)=\{j:x_j\ne y_j\}$. The raw class $F_n^{(2)}$ consists
exactly of pairs with nonempty $I$ and no adjacent elements of $I$
on the cycle. The source defines the exceptional small lengths
explicitly: the length-one class is empty; at length two its two
singleton mismatch sets are allowed. No root is divided out.

The equal-occupation class in the concentration source uses exactly
the same literal condition. With
$d_v(x)=\#\{j:x_j=v\}$, multiplication of a pair weight by
$z^{d(x)-d(y)}$ and integration over independent uniform coordinate
phases retains precisely $d(x)=d(y)$. Accordingly
$$
\Omega_n^{(2)}=F_n^{(2)}-H_n^{\mathrm{iso}}
$$
is an exact disjoint subtraction. It does not sum different markings,
unrooted representatives, colorings, or overlapping supersets.

In particular, for any complex weights $|w_{n,N}|\le W$,
$$
\left|\sum_{n\le BN}w_{n,N}\Omega_n^{(2)}\right|
\le W\sum_{n\le BN}|\Omega_n^{(2)}|
\le W\sum_{n\le BN}(|F_n^{(2)}|+|H_n^{\mathrm{iso}}|).
\tag{1.1}
$$
The absolute values occur after the complete finite signed contractions.

## 2. Direct reconstruction of the raw-class bound

Put
$$
P=|U_N|^{\circ2},\qquad E=P-J,\qquad
D=|U_N^2|^{\circ2}-P^2.
$$
The two physical estimates imply, for all sufficiently large odd $N$,
$$
\max P_{ab}\le9/N,\quad
\max |(U_N^2)_{ab}|^2\le36/N,\quad
\|E\|,\|D\|\le1/4.
\tag{2.1}
$$
All stochastic matrices here are doubly stochastic. Hence
$$
\|E\|_{\mathrm{HS}}^2\le8,
\qquad
\bigl\||U_N^2|^{\circ2}-J\bigr\|_{\mathrm{HS}}^2\le35.
$$
Since $P^2-J=E^2$,
$$
\|D\|_{\mathrm{HS}}
\le\sqrt{35}+\|E\|\|E\|_{\mathrm{HS}}
\le\sqrt{35}+\sqrt8/4<7.
\tag{2.2}
$$
The original one-step bound suffices for $\|E\|\le1/4$.
The two-step bound gives
$$
\|D\|\le8\cdot10^6t+(40000t)^2+o(1)<1/4
$$
eventually, with the actual fixed $t=10^{-80}/(2\pi)$.

If a literal independent mismatch set has $r$ elements and cyclic
gaps $g_1,\ldots,g_r\ge2$, summing its labels gives
$$
\operatorname{Tr}(DP^{g_1-2}\cdots DP^{g_r-2}).
\tag{2.3}
$$
This remains correct for repeated labels and maximal density. Since
$DJ=JD=0$, every positive exponent of $P$ can be replaced by
that of $E$ in this trace. A zero exponent is the identity. Thus
the product has $n-r$ factors, each an $E$ or a $D$.
For $n\ge3$, this number is at least two. Schatten
Cauchy--Schwarz, using two factors in Hilbert--Schmidt norm and the
remaining factors in operator norm, yields
$$
\left|\operatorname{Tr}(DP^{g_1-2}\cdots DP^{g_r-2})\right|
\le49(1/4)^{n-r-2}=784(1/4)^{n-r}.
\tag{2.4}
$$

Let
$$
Z_n(q,d)=\operatorname{Tr}
\begin{pmatrix}q&d\\1&0\end{pmatrix}^{n}-q^n.
$$
This is the nonempty cyclic independent-set sum with monomer weight
$q$ and dimer weight $d$. Each literal set is counted once.
For $q=d=1/4$, its weight is exactly $(1/4)^{n-r}$.
Its elementary generating function is
$$
\sum_{n\ge1}Z_n(q,d)s^n
=\frac{qs+2ds^2}{1-qs-ds^2}-\frac{qs}{1-qs}.
\tag{2.5}
$$
Both roots of the companion have modulus less than one at
$q=d=1/4$, so evaluation at $s=1$ is legitimate. It gives
$7/6$. Here $Z_1=0$, $Z_2=1/2$, and therefore
$\sum_{n\ge3}Z_n=2/3$.

The length-two contraction is $F_2^{(2)}=2\operatorname{Tr}D$.
Both $\operatorname{Tr}|U_N^2|^{\circ2}$ and
$\operatorname{Tr}P^2$ are nonnegative, bounded respectively by
36 and 9. Their difference consequently has modulus at most 36.
Thus
$$
\sum_{n\ge1}|F_n^{(2)}|
\le72+784\cdot\frac23=\frac{1784}{3}.
\tag{2.6}
$$

## 3. Published concentration input and its hypotheses

The published theorem was independently opened and checked on
21 October 2026: Joel A. Tropp, *User-Friendly Tail Bounds for Sums of
Random Matrices*, Foundations of Computational Mathematics **12**
(2012), 389--434, Corollary 7.5, printed page 428 (PDF page 40),
DOI [10.1007/s10208-011-9099-z](https://doi.org/10.1007/s10208-011-9099-z).
The full publisher PDF is
<https://link.springer.com/content/pdf/10.1007/s10208-011-9099-z.pdf>.

In the form used here, a self-adjoint matrix function of independent
variables with deterministic coordinate-difference square bounds
$A_v^2$ has upper-tail estimate
$d\exp[-s^2/(8\|\sum_v A_v^2\|)]$ about its mean. The source
uses this precise factor 8 and makes no commutativity improvement.

For $V(z)=U\operatorname{diag}(z)U$, replacing the coordinate
$z_v$ by $z_v'$ gives
$V'=V+\delta z\,c r$, where
$c=U_{:v}$, $r=U_{v:}$, and $|\delta z|\le2$.
The following matrix identity is exact:
$$
|V'|^{\circ2}-|V|^{\circ2}
=\delta z\,\operatorname{diag}(c)\overline{V'}\operatorname{diag}(r)
+\overline{\delta z}\,\operatorname{diag}(\bar c)V\operatorname{diag}(\bar r).
\tag{3.1}
$$
If $\max|U_{ab}|^2\le C/N$, both $V,V'$ are unitary and
each diagonal factor has norm at most $\sqrt{C/N}$. Therefore
the operator change is at most $4C/N$, uniformly over all values
of every phase. The self-adjoint dilation of $|V|^{\circ2}$
has dimension $2N$, independent bounded measurable coordinates,
and deterministic squared difference bound
$(4C/N)^2I_{2N}$ for each of its $N$ coordinates. Also
$\mathbb E|V|^{\circ2}=P^2$. Thus its variance proxy is
$16C^2/N$, and the largest eigenvalue of the centered dilation
is exactly $\|D(z)\|$, where
$D(z)=|V(z)|^{\circ2}-P^2$. The theorem gives
$$
\Pr\{\|D(z)\|\ge s\}
\le2N\exp[-Ns^2/(128C^2)].
\tag{3.2}
$$
There is no missing two-sided-tail factor.

## 4. Reconstruction of the equal-occupation estimate

Deleting the off-diagonal-to-off-diagonal transitions in the doubled
pair transfer forbids exactly consecutive literal mismatches,
including the cyclic boundary. Its determinant is the determinant
of the companion
$$
\mathcal T(z)=\begin{pmatrix}P&D(z)\\I&0\end{pmatrix}.
$$
The Schur-complement identity is polynomial/formal, and hence their
positive-power traces agree. The empty mismatch contribution is
$\operatorname{Tr}P^n$. Consequently
$$
H_n^{\mathrm{iso}}=\mathbb E G_n(z),\qquad
G_n(z)=\operatorname{Tr}\mathcal T(z)^n-\operatorname{Tr}P^n.
\tag{4.1}
$$
No inverse at a problematic spectral parameter is used.

On the constant subspace the companion contributes trace 1 at every
positive power. On its complementary block each eigenvalue satisfies
$|\lambda|^2\le q|\lambda|+\|D(z)\|$, where
$q=\|P-J\|$. Stochastic contractivity implies
$\|D(z)\|\le1+q^2$. The positive scalar root is at most
$1+q$ for $0\le q\le1$, so
$$
|G_n(z)|\le3N(1+q)^n.
\tag{4.2}
$$
The trace estimate uses eigenvalues with algebraic multiplicity and
does not assume the companion is normal or diagonalizable.

The distinct phase characters $z_u\bar z_v$, $u\ne v$,
are orthogonal. Expansion of $D$ by these characters gives
$$
\mathbb E\|D(z)\|_{\mathrm{HS}}^2
=\sum_{u\ne v}
\left(\sum_aP_{au}P_{av}\right)
\left(\sum_bP_{ub}P_{vb}\right)\le C.
\tag{4.3}
$$
Indeed, the second factor is at most $C/N$, while the sum of the
first factor over all $u,v$, even including equality, is $N$.
For
$M(z)=\max(\|E\|_{\mathrm{HS}}^2,\|D(z)\|_{\mathrm{HS}}^2)$,
this proves $\mathbb E M\le2C-1$.

On the good event $\|D(z)\|\le1/4$, assuming $q\le1/4$,
the exact contraction and the same two-factor argument as in (2.4)
give
$$
\sum_{n\ge3}|\mathbb E[\mathbf1_{\mathrm{good}}G_n]|
\le16\mathbb E M\sum_{n\ge3}Z_n(1/4,1/4)
\le\frac{32(2C-1)}3.
\tag{4.4}
$$
On the bad event, (3.2) at $s=1/4$ and (4.2) give
$$
|\mathbb E[\mathbf1_{\mathrm{bad}}G_n]|
\le6N^2\exp[q n-N/(2048C^2)].
\tag{4.5}
$$
For $n\le BN$ with $Bq\le1/(4096C^2)$, the exponent
is at most $-N/(4096C^2)$. There are at most $BN$ indices.
The entire equal-occupation terms for $n=1,2$ are zero; no such
claim is needed for their separate good and bad parts. Therefore
$$
\frac1{N^2}\sum_{n\le BN}|H_n^{\mathrm{iso}}|
\le\frac{32(2C-1)}{3N^2}
+6BN\exp[-N/(4096C^2)].
\tag{4.6}
$$

## 5. Constants, uniformity, and precise scope

For the actual family, $C=9$, so
$32(2C-1)=544$ and $4096C^2=331776$.
Moreover
$$
q_N\le40000t+o(1),\qquad
40000t=(2/\pi)10^{-76}<10^{-76}.
$$
Thus $q_N\le10^{-76}$ eventually, uniformly for the purposes
of every $B\le10^{76}/331776$. This does not assert
$q_N\to0$. The threshold can be taken simultaneously with the
finite collection of eventual physical bounds in (2.1).

Combining (1.1), (2.6), and (4.6) yields exactly
$$
\frac{W}{N^2}\sum_{n\le BN}|\Omega_n^{(2)}|
\le\frac{W(1784+544)}{3N^2}
+6BNW e^{-N/331776}
=\frac{776W}{N^2}+6BNW e^{-N/331776}.
$$
The theorem permits a linear number of literal changes, including
maximum density $\lfloor n/2\rfloor$, with arbitrary changed
coordinate labels. It does not cover adjacent mismatches, determine
the complete equal-occupation contribution, or establish all-order
spectral moment limits. The permitted band range is finite. These
limitations are correctly preserved in the audited source.
