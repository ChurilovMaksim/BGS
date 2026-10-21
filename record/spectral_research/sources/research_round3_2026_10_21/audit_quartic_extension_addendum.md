> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round3_2026_10_21/audit_quartic_extension_addendum.md`. Embedded SHA256: `e5d0e52f4deefeb70b9c52e2e19e47b357e62e72e649cf4141aa8f985003ec57`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Audit addendum: all divisors, all characters, and the signed pair removal

Date: 2026-10-21.

## Verdict and frozen files

**The arithmetic theorem and its extensions are justified at the exact source
version below.** The load-bearing operator estimate was independently
reconstructed in audit_quartic_commutator_word.md, SHA-256
ac9afae71b2c9ad15bc00b4a2b98da25473131bcff15072432c605060b4118c6.

This addendum audits the revised arithmetic manuscript
arithmetic_comb_fourth_difference_gap.md, SHA-256
0b7bd5a0c21b79f1dd45d6b6377e58cd9f9afcdb8ed017199c874ace8e2fcc66,
including its new Sections 6.1–6.2. The earlier complete draft was read;
the changed operator proof and new sections of this frozen version were
then read and checked directly.

The right-to-left conjugation expansion and the explicit Zak transform
now appear in the source itself. They resolve the two previously
load-bearing issues: a uniform norm remainder at $h\asymp\delta^4$,
and transfer of the line estimate to the exact finite odd torus.

No historical source was changed in this audit.

## 1. Divisor range and a uniform threshold

Suppose $N=d^2m$ is odd and $d\ge N^{1/4}$.
Let $x=dN^{-1/4}$, $b=\lfloor x\rfloor$, and $\delta=b/d$.
Since $x\ge1$, $x/2\le\lfloor x\rfloor\le x$, so
$$
\frac12N^{-1/4}\le\delta\le N^{-1/4},\qquad
\beta=N\delta^4\in[1/16,1].
$$
Also $N\delta=dmb$ is an integer. This endpoint translation is an
integer power of an oldspace fixing translation.

The previously proved word remainder is $C\tau\delta^5/h$, with $h$
held fixed during differentiation. At this endpoint it becomes
$2\pi C\tau\beta\delta=O(\tau N^{-1/4})$.
The leading term is $i\beta\tau Q_N(g)$, where $g=a_{qqqq}$.
The linear-in-$K_h$ quadratic-$\tau$ error acquires a factor $\beta$;
the exponential remainder acquires $\beta^2$. Both factors are at most
one. Thus the source's uniform bound
$$
C_3=I+i\beta\tau Q_N(g)+
O_{\rm op}(10^{18}\tau^2+10^{21}\tau N^{-1/4})
$$
is valid.

Compression of $Q_N(g)^*Q_N(g)$ is exactly $\sigma^2P$ whenever
$d>18$. For the fixed $\tau$, choose one large threshold in $N$
so that each error is at most $\tau\sigma/64$.
Since $\beta\tau\sigma\ge\tau\sigma/16$, the lower bound on the
commutator defect is at least $\tau\sigma/32$.
The word's eight conjugated-translation factors give the upper bound
$16\|(I-P)E_Nv\|$. Hence
$$
\|(I-P)E_Nv\|\ge\tau\sigma/512.
$$
All thresholds are uniform over the eligible divisors $d$.
The squared denominator $512^2=262144$ in the norm-gap statement is correct.

For precision, the canonical oldspace is defined by both independent
$q$- and $p$-translation characters. In the same-direction word
$R=S$ are $q$ translations, but both fix this smaller simultaneous
fixed space. The Fourier compression uses both independent characters.

## 2. Exact same-direction constant

Direct expansion gives
$$
r=1+\cos2\pi q-\cos14\pi q
-\tfrac12\cos12\pi q-\tfrac12\cos16\pi q,
$$
$$
r\sin2\pi q=
\sin2\pi q+
\tfrac12(\sin4\pi q+\sin12\pi q-\sin16\pi q)
+\tfrac14(\sin10\pi q-\sin18\pi q).
$$
In particular the potential $\sin14\pi q$ terms cancel.

The nonzero cosine amplitudes of the $p$-independent symbol are
$$
C_1=1/10,\quad C_6=-1/20,\quad C_7=9/10,\quad C_8=-1/20.
$$
Its sine amplitudes are
$$
S_1=1/100,\ S_2=1/200,\ S_5=1/400,\ S_6=1/200,\
S_8=-1/200,\ S_9=-1/400.
$$
The shifted $r(q+1/2)$ has cosine amplitudes
$D_1=-1,D_6=D_8=-1/2,D_7=1$; its constant disappears under four
$q$-derivatives.

Orthogonality in $q,p$ therefore gives
$$
\frac{\sigma^2}{(2\pi)^8}
=\frac12\sum_jj^8(C_j^2+S_j^2)
+\frac1{40000}\sum_jj^8D_j^2
=\frac{377350620897}{160000}.
$$
Both the polynomial expansion and the last exact rational sum were
independently checked. Thus
$$
\sigma\approx2393492.2002178063.
$$
The source's simpler lower bound $10^6$ is valid and already sufficient.

## 3. Every oldspace character

For $H_d(s,u)=T_N(sN/d,uN/d)$, the modular Weyl cocycle is exactly one:
each symplectic product contains
$(N/d)^2=Nm$. Multiplication by the modular inverse of two still
leaves an integer multiple of $N$ in the finite phase.
Thus this is an honest representation of $(\mathbb Z/d\mathbb Z)^2$.

The character projectors are mutually orthogonal and sum to $I_N$.
Every nonidentity group element has trace zero, so every character
space has dimension $m=N/d^2$. A Fourier mode changes its character
unless both frequency indices are divisible by $d$.
This proves the same exact compression identity in every character space:
$$
P_\chi Q_N(g)^*Q_N(g)P_\chi=\sigma^2P_\chi.
$$

If the word translation acts as $r_\chi$ on that space, divide both
$R$ and $B=E_N^*RE_N$ by $r_\chi$.
Central phases disappear from every group commutator, so the word is
unchanged. The normalized $R$ fixes the vector, and the normalized
$B$ has defect at most twice its escape from the character space.
The same estimate therefore proves
$$
\sup_\chi\|P_\chi E_NP_\chi\|
\le \rho:=\sqrt{1-\tau^2\sigma^2/262144}<1.
$$
There is no choice of a favorable character and no character-dependent
dimension threshold.

## 4. Exact metaplectic action and the itinerary contraction

Independent substitution in the finite kernel confirms
$$
T_N(a,b)M_N=M_NT_N(3a-4b,-2a+3b).
$$
The linear map on the right is
$L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix}$, with determinant one.
Consequently $M_NP_\chi M_N^*=P_{\chi\circ L}$, with the same direction
of composition as in the source.

Set
$$
D=\sum_\chi P_\chi E_NP_\chi,\qquad \mathcal K=DM_N.
$$
Then
$$
\mathcal K=\sum_\chi P_{\chi\circ L}U_NP_\chi,\qquad
\|\mathcal K\|=\|D\|\le\rho.
$$
The equality is a direct reindexing of the orthogonal character blocks.
No metaplectic scalar is omitted: the covariance is for the given
finite matrix $M_N$.

The canonical invariance $M_NJ=JM_m$ is also exact at arbitrary odd
$N=d^2m$. In the input sum write $y=d(z+km)$, $0\le k<d$.
All quadratic-in-$k$ terms and the terms involving $z k$ are multiples
of $N$; the remaining character sum vanishes unless $d\mid x$.
For $x=dy$, its constant phase reduces to the $m$-dimensional kernel
because the inverse of eight reduces modulo $m$.
The factor $dN^{-1/2}d^{-1/2}=d^{-1/2}m^{-1/2}$ is exactly the
embedding normalization. Thus the stated escape for the full $U_N$
follows as well as escape for $E_N$.

## 5. Fixed characters at every composite modulus

The trace of $\mathcal K^n$ receives contributions only from characters
fixed by $L^n$. Each contributing block has dimension $m$ and norm
at most $\rho^n$. Hence, with $c_n=\operatorname{Tr}\mathcal K^n$,
$$
|c_n|/N\le \rho^nF_d(n)/d^2.
$$

The composite-modulus counting argument is valid. If an integral matrix
$B$ is invertible over $\mathbb Q$, the map
$$
x\bmod d\longmapsto Bx/d\bmod B\mathbb Z^2
$$
is well-defined on $\ker(B\bmod d)$: changing $x$ by $dz$ changes
the image by $Bz$. If its image is zero, $Bx/d=By$ for some integer
$y$, so $B(x-dy)=0$; invertibility gives $x=dy$.
The map is therefore injective.

Take $B=(L^T)^n-I$. It is nonsingular for every $n\ge1$.
The index of $B\mathbb Z^2$ equals $|\det B|$, by integer row/column
reduction. With $\lambda=3+2\sqrt2$,
$$
F_d(n)\le\lambda^n+\lambda^{-n}-2\le\lambda^n.
$$
Combining this with $F_d(n)\le d^2$ gives exactly
$$
\frac{|c_n|}{N}\le
\rho^n\min(1,\lambda^n/d^2).
$$

## 6. Entire bounded-weight signed pair removal

Put $p_n=\operatorname{Tr}U_N^n$ and $r_n=p_n-c_n$.
For every $n\ge1$,
$$
|p_n|\le N,\quad |c_n|\le N,\quad |r_n|\le2N,
$$
and consequently
$$
\big||p_n|^2-|r_n|^2\big|\le3N|c_n|.
$$
For any bounded, possibly $N$-dependent weights this gives
$$
\frac1{N^2}\left|
\sum_{n\ge1}w_n(|p_n|^2-|r_n|^2)\right|
\le3\|w\|_\infty
\sum_{n\ge1}\rho^n\min(1,\lambda^n/d^2).
$$

Split at $L_d=\lfloor2\log d/\log\lambda\rfloor$.
The initial part is bounded by
$d^{-2}\sum_{n\le L_d}(\rho\lambda)^n=O_\tau(\rho^{L_d})$,
because $\rho\lambda>1$. The tail is
$\rho^{L_d+1}/(1-\rho)=O_\tau(\rho^{L_d})$.
Since the fractional part of $2\log d/\log\lambda$ only contributes
a bounded factor,
$$
\rho^{L_d}=O_\tau(d^{-\kappa}),\qquad
\kappa=-2\log\rho/\log\lambda>0.
$$
This verifies the source's rate and all its quantifiers.

The grouped difference series is absolutely convergent even for
nondecaying bounded weights. The statement does not subtract two
undefined unweighted infinite positive series. It applies directly to
compact Fourier weights and to the full Abel weights. It includes
the signed cross term between the removed itinerary trace and every
remaining history.

The exponent is positive but extremely small for the specified $\tau$;
the theorem is asymptotic and gives no practical rate at moderate $N$.
No claim of such a rate is made.

## 7. Safe conclusion

The new result removes the complete unperturbed character itinerary
from the normalized pair sum with an $o(1)$ error for the stated
growing-divisor range. It does not evaluate the complementary traces
$r_n$, which contain all histories with at least one change of
itinerary. No CUE comparison for those traces, and no full
$H_{\rm diag}$, follows from this removal alone.

No mathematical gap was found in the frozen statement.
