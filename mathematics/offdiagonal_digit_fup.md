# Off-diagonal digit alphabets: an exact parity classification

**Claim ID:** `BGS-FUP-001`

Date: 30 September 2026.

Status: project geometric proof plus an application of Cohen's Theorem 2,
arXiv:2206.14131v3 (5 October 2024), printed p. 3.
The source is published in Analysis & PDE 18 (2025), 743--772.
This is a corollary of that prior theorem, not a claimed new FUP mechanism.

## 1. Statement and separation from the frozen map

For an integer $M\ge2$, put
$$
\mathcal A_M=\{(r,s)\in\{0,\ldots,M-1\}^2:r\ne s\},\quad N=M^k,
$$
and let $X_k\subset(\mathbb Z/N\mathbb Z)^2$ be the points whose paired
base-$M$ digits all belong to $\mathcal A_M$. Use the unitary two-dimensional
Fourier transform with kernel $N^{-1}e^{-2\pi i x\cdot\xi/N}$.
Then some $C,\beta>0$, independent of $k$, satisfy
$$
\|1_{X_k}\mathcal F_N1_{X_k}\|\le C N^{-\beta}                 \tag{1}
$$
**if and only if $M$ is odd or $M=2$.** For $M=2$ and $k\ge1$,
the norm is exactly $\sqrt{2/N}$. For even $M\ge4$ the norm is
exactly 1 at every $k\ge1$.

In particular the ideal base-7 alphabet in the submitted note satisfies
(1). This does not identify any open compression of
$\operatorname{Ad}_{U_N}$ with this Fourier operator. Actual Markov coding,
cutoffs, distorted canonical coordinates and long-time errors remain open.
No edge from this auxiliary theorem to BGS-TRACE-005 is asserted.

## 2. Lines and closed-drawing boundary issues

Let $X$ be the limiting closed digit set. The first closed drawing is the
union of the closed squares for the allowed digit pairs. Its complement
contains the open diagonal squares
$J_r\times J_r$, $J_r=(r/M,(r+1)/M)$.
A line with irrational slope is dense in the torus and cannot lie in the
proper closed set $X$. Rational directions can be scaled to integer
$(a,b)\ne(0,0)$.

If $ab>0$ and $a\ne b$, orient both positively. The difference of the
coordinates runs around the circle, so the line meets the diagonal.
An intersection inside $J_r\times J_r$ is forbidden. At a diagonal
grid vertex, a sufficiently small positive displacement moves both
coordinates into the same open square. Thus such a full line is excluded
already by the first drawing.

Horizontal and vertical lines need a separate boundary argument: an axis
line at a grid boundary can lie in the first closed drawing. If a vertical
coordinate $x$ is not a first-level grid point, $(x,x)$ is forbidden.
If $x=j/M$, the only possible length-two digit prefixes for $x$ are
$(j,0)$ and $(j-1,M-1)$, interpreted modulo $M$ for $x=0$.
Choose $y$ with unique first two digits $(j,M-1)$ and a nonboundary tail.
Its first digit kills the first prefix; its second kills the other.
Hence this point is not in $X_2$'s closed drawing. No vertical line is
contained in $X$; by symmetry neither is a horizontal line.

For the antidiagonal direction $(1,-1)$, a full line has equation
$x+y=c\pmod1$. Its two diagonal intersections are separated by $1/2$.
When $M$ is odd, they cannot both be first-level grid points. One therefore
lies in a forbidden open diagonal square. Antidiagonal lines are excluded.

If $M$ is odd, these facts exclude orthogonal pairs: a negative-slope
direction other than the antidiagonal has a perpendicular direction of
positive unequal slope, already excluded. A diagonal direction has the
excluded antidiagonal perpendicular; axis directions are absent.
Cohen's prior criterion, with both alphabets equal to $\mathcal A_M$,
now proves (1). The required criterion concerns entire affine torus lines
in the limiting closed sets, not the presence of rows in the first grid.

## 3. Skew lines: the submitted exclusion is false

The limiting set does contain the entire line
$$
y=(1-M)x\pmod1.                                             \tag{2}
$$
For $x=(r+s)/M$, $0<s<1$, the second coordinate traverses the complement
of the open $r$th cell; its cell label differs from $r$ away from grid
boundaries. Multiplication of both coordinates by $M$ preserves (2).
Points avoiding all digit boundaries consequently have unequal paired
digits at every level. Such points are dense in the line, so closedness
includes the whole line. At $M=7$ this is direction $(1,-6)$, contradicting
the note's assertion that all contained lines have direction $(1,1)$.
Its perpendicular direction $(6,1)$ is excluded by Section 2.

For odd $M\ge3$, $y=x+1/2$ is also contained: a separation $1/2$ cannot
fit in one open cell of width $1/M$, and multiplication by odd $M$
preserves this offset. Boundary points follow by closedness again.
Thus exclusion of *all* lines would be the wrong hypothesis.

## 4. Even bases and the binary exception

For even $M\ge4$, $y=-x$ belongs to $X$: away from boundaries its digits
are $s=M-1-r$, which never equal $r$ for even $M$; the relation is
preserved at every scale. Also $y=x+1/(M-1)$ belongs to $X$.
Its offset is preserved modulo 1 by multiplication by $M$, and lies in
$[1/M,1-1/M]$, so its two coordinates cannot share an open digit cell.
These are perpendicular full lines, the obstruction in Cohen's criterion.
Here we can prove a stronger failure directly, without using its sharpness
proof. Put $d=(N-1)/(M-1)$, whose $k$ digits are all 1, and define
$$
f(x,y)=N^{-1/2}1_{\{y=N-1-x\}}e^{2\pi i d y/N}.
$$
This has norm 1 and support in $X_k$: the digits of $N-1-x$ are
$M-1-r$, unequal to $r$ when $M$ is even. Fourier summation in $x$
shows that its transform is supported on $\eta=\xi+d\pmod N$.
This entire discrete line lies in $X_k$ as well. In adding $d$ to $\xi$,
each digit increases by $1+c$ modulo $M$, where the incoming carry
$c$ is either 0 or 1. For $M\ge4$ this increment is never zero modulo
$M$, including across the final wrap. Both projections therefore preserve
the unit vector and its Fourier transform. The compression norm is at
least 1 and, by unitarity, at most 1. This proves exact equality at every
scale and is stronger than merely ruling out polynomial decay.

At $M=2$, paired digits are complementary, so
$X_k=\{(j,N-1-j):0\le j<N\}$. Restricting Fourier to these indices gives
an $N\times N$ matrix whose entries, up to separate unit-modulus row and
column factors, are $N^{-1}e^{-2\pi i(2j\ell)/N}$.
The Gram matrix is $N^{-1}$ times the indicator of
$2(\ell-\ell')=0\pmod N$, up to diagonal unitary conjugation.
Since $N$ is even, there are $N/2$ blocks of size 2, each with nonzero
eigenvalue $2/N$. This proves the asserted exact norm and completes the
classification without a separate limiting-line argument for the binary
case.

## 5. Execution and priority boundary

The [finite verifier](../computations/verification/heisenberg_note_audit.py)
checks digit membership at exact rational points and the binary norm at
specified finite scales. These checks do not prove (1) for odd $M$;
the geometric proof and the pinned external theorem do.
No quantitative exponent for base 7 is extracted, no stability under
nonlinear canonical deformation is proved, and no priority search for
this particular alphabet corollary was completed.
