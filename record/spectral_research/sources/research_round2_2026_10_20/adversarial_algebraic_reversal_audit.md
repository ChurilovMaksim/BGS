> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_algebraic_reversal_audit.md`. Embedded SHA256: `c4068f322442a34ecf336c2adda435edb7dfdc1998f82a538aaed62a047d6d1c`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/symmetry.md).

# Independent audit: common reversal and algebraic return lines

## Inputs and verdicts

The following files were read in full, without modification:

| File | SHA-256 | Verdict |
|---|---|---|
| `arithmetic_banded_time_reversal.md` | `39d017750473ee6779fc52656613b06dee5cd5591e4dbd288c64c10904cae6dd` | PASS |
| `root_all_time_algebraic_nonrecurrence.md` | `d4bb6ae891984cff12b9fb437b3c4bda2edb58247a3d0d398b4efb477d70e3a7` | PASS |

The cubic trace formulas were checked directly by hand from the specified
Fourier coefficients and exact Weyl multiplication. The projective
Lindemann--Weierstrass arguments were checked separately, including the
possibility of a transcendental projective scalar. Neither conclusion
is being interpreted as a quantitative spectral-statistics estimate.

## 1. Weyl convention and no-alias range

For the ordinary auxiliary Weyl operators
$W(k,l)=(-1)^{kl}T(l,k)$, direct multiplication gives

$$
 W(k,l)W(k',l')
 =e^{\pi i(lk'-kl')/N}W(k+k',l+l').
$$

The prescribed metaplectic kernel gives

$$
 MW(k,l)M^*=W(3k+2l,4k+3l).
$$

The parity difference
$(3k+2l)(4k+3l)-kl$ is even, so passage from modular to ordinary
halves introduces no residual sign. The corrected ordinary symbol is

$$
 a(q,p)=V(q)+\gamma R(q)e^{2\pi ip}
 +\overline\gamma R(q)e^{-2\pi ip},
 \quad \gamma=(-3-4i)/1000,
 \quad R(q)=r(q+1/2).
$$

The support has $|k|\le9,|l|\le1$; at $|k|=9$, only
$l=0$ occurs. Consequently the image support under $S^T$ has
$|k|\le27,|l|\le36$, rather than the larger bounds that one
would obtain from the containing rectangle alone. The two cubic
trace supports are bounded by $(63,73)$ and $(45,38)$.
Thus for odd $N\ge75$, exact trace orthogonality selects only
the zero integer frequency. There is no asymptotic approximation in
the calculations below.

## 2. Direct computation of the asymmetric cubic trace

Put $B=MAM^*$ and $x=\pi/N$. Cyclicity gives

$$
 I_N=\operatorname{Tr}(AB^2)-\operatorname{Tr}(A^2B).
$$

Among the nonzero Fourier indices of $a$, the only ones with
$|4k+3l|\le2$ are $(1,-1),(-1,1)$. Hence only the two
frequencies $(1,1),(-1,-1)$ of $B$ can meet the support of
$A^2$ in the second trace. The inverse transformation gives the
corresponding pair for the first trace.

Let

$$
 Q(x)=\sum_j V_jR_{1-j}\cos(jx).
$$

The two orderings of a $q$-only factor and a positive-
$p$-frequency factor have Weyl phases $e^{\pm ijx}$. Thus
the exact $A^2$ coefficient at $(1,1)$ is $2\gamma Q$,
and that at $(1,-1)$ is $2\overline\gamma Q$. Pairing with
the two cat-image coefficients gives

$$
 \frac1N\operatorname{Tr}(A^2B)=-2\Re(\gamma^2Q),
 \qquad
 \frac1N\operatorname{Tr}(AB^2)=-2\Re(\gamma^2\overline Q).
$$

Since $\gamma^2=(-7+24i)/10^6$, their difference is
$-96\cdot10^{-6}\Im Q$. The imaginary coefficients of $V$
follow directly from

$$
 \Im V_j=-\frac{r_{j-1}-r_{j+1}}{200}.
$$

Combining the positive and negative indices produces

$$
 3200\Im Q=
 -16\cos x+4\cos2x-\cos5x
 +4\cos6x+4\cos8x-\cos9x.
$$

Finally,

$$
 \cos9x+\cos5x-4\cos8x-4\cos6x-4\cos2x+16\cos x
 =2(2-\cos7x)(4\cos x-\cos2x).
$$

This proves the stated formula

$$
 \frac{I_N}{N}=\frac3{50000000}
 (2-\cos7x)(4\cos x-\cos2x).
$$

For $N\ge3$, $c=\cos(\pi/N)\in[1/2,1]$, and
$4c-\cos(2\pi/N)=1+4c-2c^2\ge5/2$. The factor
$2-\cos7x$ is at least 1. The lower bound
$I_N/N\ge3/20000000$ therefore follows with room to spare.

## 3. Arbitrary common antiunitaries and the norm bound

Both traces defining $I_N$ are real because they are traces of
products of Hermitian matrices. Antiunitary conjugation preserves
product order and conjugates the trace. Hence a common antiunitary
with $DAD^{-1}=A$ and $DMD^{-1}=M^{-1}$ would interchange
these two real traces, contradicting their strict difference.
No geometric, coordinate, or algebraic assumption on this common
antiunitary is used.

For an approximate common antiunitary, telescope the five factors in
$A'M'(A')^2(M')^*$ against those in $AM^*A^2M$. There are
three errors bounded by $R^2\delta_A$ and two bounded by
$R^3\delta_M$ after dividing the trace by $N$, with
$R=59/50$. All intermediate $A$-factors retain norm at most
$R$, since $A'$ is antiunitarily conjugate to $A$.
Thus

$$
 3R^2\delta_A+2R^3\delta_M\ge\frac3{20000000}.
$$

The exact sum $3R^2+2R^3=932908/125000$ yields
$\max(\delta_A,\delta_M)\ge3/149265280>2\cdot10^{-8}$.

## 4. Independent check of the odd moment

Write $t=2\pi q$, $C=\cos7t$, and

$$
 w=\frac{\cos t}{10}+\frac{(1+\cos t)\sin t}{100},
 \qquad V=.9C+(1-C)w.
$$

The necessary elementary averages are

$$
 \langle w\rangle=0,\quad
 \langle w^2\rangle=\frac{81}{16000},\quad
 \langle w^3\rangle=\frac3{400000}.
$$

For example, the only surviving term in the cube is
$3(\cos t/10)((1+\cos t)\sin t/100)^2$; its average is
$3/400000$. Since $w^j$ has frequencies of magnitude at
most 6 for $j\le3$, these products do not meet nonconstant
frequencies of powers of $C$. Thus

$$
 \langle V^3\rangle
 =-\frac{27}{10}\langle w^2\rangle+\frac52\langle w^3\rangle
 =-\frac{273}{20000}.
$$

The Jacobi path expansion gives the remaining contribution

$$
 3|\gamma|^2\int
 [V(q-1/(2N))+V(q+1/(2N))]R(q)^2\,dq.
$$

Only the real coefficients at $1,6,7,8$ contribute. Inserting
$(R^2)_1=-3/2$, $(R^2)_6=(R^2)_8=-1$, and
$(R^2)_7=3/2$, together with $|\gamma|^2=1/40000$, gives

$$
 \frac{\operatorname{Tr}(A^3)}N
 =-\frac{273}{20000}
 +\frac{3\cos8x+81\cos7x+3\cos6x-9\cos x}{400000}.
$$

Its upper bound is $-1341/100000<0$. Unitary or antiunitary
conjugation of $A$ to $-A$ is therefore impossible.

## 5. Projective evaluation at an algebraic parameter

The algebraic spectral-projector expansion of $A$ shows that
every matrix entry of the relevant products, including each projective
minor, is a finite sum $\sum c_j e^{\beta_jz}$, with algebraic
coefficients and frequencies. Equal frequencies must first be
collected. At nonzero algebraic $z_0$, the distinct exponents
$\beta_jz_0$ remain distinct algebraic numbers. The
Lindemann--Weierstrass theorem cited precisely in the input then
forces every coefficient to vanish if the sum vanishes at $z_0$.

This eliminates an arbitrary initial scalar without assuming it
algebraic: use two-by-two entry minors before applying the theorem.
Near zero, invertibility supplies a nonzero entry of the comparison
matrix and hence a holomorphic proportionality factor $\eta(z)$.

For an antiunitary product reverser, the zero-parameter equality is
$M_D=\eta(0)M^{-1}$. The nonzero quadratic Gauss trace gives
$|\operatorname{Tr}M|=1$, so taking traces fixes $\eta(0)=1$.
The Gauss identity works for every odd composite dimension: the map
$(j,k)\mapsto(j-k,j+k)$ is bijective modulo $N$, and the
bilinear character sum vanishes except at zero first coordinate.
Differentiation at zero then gives

$$
 -iNA_D=\eta'(0)I-iNM^{-1}AM.
$$

Taking traces proves $\eta'(0)=0$. Therefore $MD$, not
necessarily $D$, is a common antiunitary of $A,M$, already
excluded above.

For a unitary product reverser the derivative has the opposite sign
and gives $JAJ^{-1}=-M^{-1}AM$, because $\operatorname{Tr}A=0$
in the stated no-alias range. For an antiunitary product commuter it
gives $DAD^{-1}=-A$. The negative odd moment excludes both.
The zero-parameter scalar in these latter two cases need not be 1;
only its nonvanishing and the trace-forced zero logarithmic derivative
are needed. The input uses precisely that weaker fact.

## 6. The stronger all-time algebraic-line nonrecurrence

The second audited file retains the original modular Weyl coefficients
and writes, in every odd dimension,

$$
 A_N=\frac12T(v_0)+\frac12T(-v_0)+\sum_w r_{w,N}T(w),
 \qquad v_0=(0,7),\quad
 \sum_w|r_{w,N}|\le\frac{19}{50}.
$$

This bound survives arbitrary collisions of Fourier indices modulo
$N$, since combining coefficients cannot increase their absolute
sum. It follows from the coefficient masses $3/10,4/100,4/100$
of the three remaining terms after retaining the original
$\cos(14\pi q)$ pair. Thus it also covers $N=3,5,9$.

Let $d$ be the orbit length of $v_0$ under the exact modular
Egorov action. In the incomplete sum

$$
 Q_{m,N}=\sum_{j=0}^{m-1}M^jA_NM^{-j},
$$

the coefficient at $v_0$ samples the successive points
$S^{-j}v_0$. The starting point itself occurs exactly
$\lceil m/d\rceil$ times. Each other orbit point occurs at most
that often. The displayed contribution from $-v_0$, if present,
has nonnegative real part. The residual contribution can therefore
decrease the real coefficient by at most
$(19/50)\lceil m/d\rceil$. Hence

$$
 \Re q_{v_0}\ge\frac3{25}\lceil m/d\rceil>0.
$$

For odd $N\ne7$, $v_0\ne0$, and orthogonality of the
modular Weyl basis proves that $Q_{m,N}$ is nonscalar. Crucially,
this holds for arbitrary $m$, without requiring $d\mid m$.

If $U_N(z_0)^m$ lay on an algebraic matrix line, the projective
entry equations would vanish identically by the same evaluation
principle. Thus $U_N(z)^m=c(z)B$ for all complex $z$.
At zero, $M_N^m=c(0)B$ and $c(0)\ne0$. Differentiating
and cancelling $M_N^m$ would make $Q_{m,N}$ scalar, a
contradiction. No trace-zero hypothesis or determinant identity is
needed in this argument.

At $N=7$, both the original grid and its modular midpoints have
$r=0$, so $A_7=(9/10)I$. The exceptional algebraic-line
returns in that single dimension are genuine. This does not affect
an asymptotic statement along all odd $N$.

## 7. Exact scope

The results rule out every common antiunitary, quantify approximate
common reversal, exclude the stated algebraic product intertwiners,
and exclude all positive-time algebraic matrix lines in every odd
dimension except 7. Arbitrary finite-dimensional spectral-basis
antiunitary reversers still exist, and their linear parts need not
be algebraic. Algebraic matrix lines are dense. Consequently exact
nonrecurrence supplies no lower bound for their distance from the
actual powers, nor a bound for a weighted trace sum at times of order
$N$. Nothing in this audit fills that missing cancellation.
