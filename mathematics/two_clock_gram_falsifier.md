# A CUE Gram-moment match with non-CUE pair statistics

**Claim ID:** `BGS-TRACE-008`. **Status:** exact elementary construction;
proof below. This note concerns abstract unitary spectra, **not** the frozen
propagator `U_N` of the BGS programme. It isolates the logical strength of
the necessary Gram-moment milestone in [`open_questions.md`](open_questions.md).

## Statement

For a unitary matrix $W$ of size $N$, write

$$
p_m(W)=\operatorname{Tr}W^m,\quad
\Gamma_N(W)=\left[N^{-1}p_{b-a}(W)\right]_{0\le a,b<N},\quad
G_N(W)=N^{-1}\operatorname{Tr}\Gamma_N(W)^2,
$$

where $p_{-m}=\overline{p_m}$ and $p_0=N$. There is a sequence of
**odd-dimensional**, simple unitary spectra $W_{2n+1}$ whose empirical
eigenphase measures tend weakly to Haar measure and whose unfolded
unit-interval occupancy is at most three, such that

$$
p_m(W_{2n+1})\ne0\quad(m\ge1),\qquad
G_{2n+1}(W_{2n+1})\longrightarrow\frac43,                 \tag{1}
$$

but, for every $s>0$, its pair Abel statistic converges to

$$
\begin{split}
L_{2n+1}(s)&=(2n+1)^{-2}\sum_{m\ge1}e^{-2sm/(2n+1)}
                  |p_m(W_{2n+1})|^2\\
&\longrightarrow B_\phi(s):=
\sum_{k\ge1}e^{-sk}\cos^2(k\phi/2),
\quad \phi=\arccos(-1/3).                                  \tag{2}
\end{split}
$$

This function differs from the CUE target
$(1-e^{-2s})/(4s^2)$; for example, $B_\phi(s)=O(e^{-s})$ as
$s\to\infty$ while the CUE target is asymptotic to $1/(4s^2)$.
The empirical cyclic nearest-neighbor gaps in mean-spacing units have
the explicit weak limit

$$
\frac12\delta_{\phi/\pi}
 +\frac12\delta_{2-\phi/\pi}.                          \tag{2a}
$$

Thus the three properties in (1), **even in combination**, do not imply
the pair CUE law. In particular, a proof of the Gram milestone for the
actual frozen map would be necessary but insufficient to close
`BGS-TRACE-005`.

There is also an even-dimensional exact benchmark: for every even
$N=2n\ge4$, a simple union of two regular $n$-gons has

$$
G_N=\mathbb E_{\mathrm{CUE}(N)}G_N
      =\frac43-\frac1{3N^2},                               \tag{3}
$$

while its Abel limit is again (2), and hence not CUE.

## Proof and normalizations

For any $W$, count the pairs $(a,b)$ with $b-a=m$:

$$
G_N(W)=1+\frac2{N^3}\sum_{m=1}^{N-1}(N-m)|p_m(W)|^2.   \tag{4}
$$

The standard finite CUE trace identity
$\mathbb E|p_m|^2=\min(m,N)$ gives, by the elementary sum
$\sum_{m=1}^{N-1}(N-m)m=N(N^2-1)/6$,

$$
\mathbb E_{\mathrm{CUE}(N)}G_N
 =1+\frac{N^2-1}{3N^2}=\frac43-\frac1{3N^2}.       \tag{5}
$$

For completeness, use the CUE eigenangle density
$|\det(e^{ia\theta_j})_{0\le a<N,1\le j\le N}|^2/
(N!(2\pi)^N)$. Expanding the determinants and integrating all but
two angles gives its two-point function
$\rho_2(\theta,\eta)=(N/(2\pi))^2-|K_N(\theta,\eta)|^2$,
where $K_N=(2\pi)^{-1}\sum_{a=0}^{N-1}e^{ia(\theta-\eta)}$.
The diagonal $j=k$ part of $\mathbb E|p_m|^2$ is $N$; integrating
$e^{im(\theta-\eta)}\rho_2$ for $m>0$ subtracts the number of
pairs $(a,b)$ with $b-a=m$. This is $N-m$ for $m<N$, so
$\mathbb E|p_m|^2=m$. Only $m<N$ is used in (5).

Let $\omega=e^{2\pi i/n}$. Two disjoint regular $n$-gons at relative
angle $\phi/n$ have points

$$
\{\omega^j:0\le j<n\}\ \cup\
\{e^{i\phi/n}\omega^j:0\le j<n\},\quad 0<\phi<\pi.     \tag{6}
$$

Their power sums vanish unless $n\mid m$; for $m=kn$ they equal
$n(1+e^{ik\phi})$. At $N=2n$, (4) has only the $m=n$ term, giving

$$
G_{2n}=1+\cos^2(\phi/2).                              \tag{7}
$$

Choose $\phi_N\in(0,\pi)$ by
$\cos^2(\phi_N/2)=1/3-1/(3N^2)$. Equations (5) and (7)
prove the exact equality (3). Moreover $\phi_N\to\phi$ with
$\cos\phi=-1/3$. For either fixed $\phi$ or this varying $\phi_N$,
the Abel statistic of (6) is

$$
L_{2n}(s)=\sum_{k\ge1}e^{-sk}\cos^2(k\phi_N/2)
\longrightarrow B_\phi(s).                            \tag{8}
$$

The limit is justified by the geometric majorant $e^{-sk}$.

To obtain the *odd* sequence in (1), fix $\phi=\arccos(-1/3)$ and
append the same transcendental point $z$ on the unit circle to (6) for
every $n\ge2$. Such a point exists, since the algebraic points are
countable. The original $2n$ points are algebraic: $e^{i\phi}$ is a
root of $3X^2+2X+3=0$, so each $e^{i\phi/n}\omega^j$ is algebraic.
Thus the resulting $2n+1$ phases are distinct. For $n\nmid m$,
$p_m=z^m\ne0$; for $m=kn$, the term
$n(1+e^{ik\phi})$ is algebraic whereas $z^{kn}$ is transcendental.
Hence $p_m\ne0$ for *every* positive integer $m$.
For each fixed $m>0$, eventually $n\nmid m$, so
$N^{-1}p_m=z^m/N\to0$; the same holds for negative $m$ by conjugation.
Density of trigonometric polynomials proves weak Haar convergence of
the empirical phases. In the original two-gon spectrum, every two
consecutive circular gaps sum to $2\pi/n$. Any unfolded unit interval
for the **odd** dimension has angular length $2\pi/(2n+1)<2\pi/n$
and therefore contains at most two of those points. The appended point
increases this maximum by at most one, giving occupancy $\le3$ for
every $n\ge2$, independently of how close $z$ lies to a polygon point.
Before insertion, the $2n$ circular gaps alternate between $\phi/n$
and $(2\pi-\phi)/n$. In units of the **odd** mean gap
$2\pi/(2n+1)$, these are
$(2n+1)\phi/(2\pi n)$ and
$(2n+1)(2\pi-\phi)/(2\pi n)$, converging to the two atoms
in (2a). Inserting $z$ removes exactly one old gap and creates two
new gaps. Including the change from denominator $2n$ to $2n+1$,
the difference on any bounded test $f$ is at most
$4\|f\|_\infty/(2n+1)$. This proves (2a).

Equation (4) has $p_m=z^m$ for all $m\in[1,2n]$ except $m=n,2n$.
These nonmultiples contribute $O(n^{-1})$ to $G_{2n+1}-1$.
The $m=2n$ term also contributes $O(n^{-1})$ because its weight
$N-m$ is one. The $m=n$ term equals

$$
\frac{2(n+1)}{(2n+1)^3}
   \left|n(1+e^{i\phi})+z^n\right|^2
\longrightarrow\cos^2(\phi/2)=\frac13.               \tag{9}
$$

This proves (1). For fixed $s>0$, the Abel contribution of the
nonmultiples is bounded by
$(2n+1)^{-2}\sum_{m\ge1}e^{-2sm/(2n+1)}=O_s(n^{-1})$.
For the multiples, $p_{kn}=n(1+e^{ik\phi})+z^{kn}$; relative to the
two-gon term, the normalized squared modulus differs by $O(n^{-1})$
uniformly in $k$. As
$e^{-2skn/(2n+1)}\le e^{-sk/2}$ for $n\ge1$,
dominated convergence proves (2). Finally, $0\le\cos^2\le1$ gives
$B_\phi(s)\le e^{-s}/(1-e^{-s})$, whereas the stated CUE asymptotic
is polynomial. No dynamical realization of this abstract example by
the maintained $U_N$ is asserted.

For reference the non-CUE limit also has the elementary closed form,
with $x=e^{-s}$,

$$
B_\phi(s)=\frac12\left(\frac{x}{1-x}
 +\frac{x\cos\phi-x^2}{1-2x\cos\phi+x^2}\right).       \tag{10}
$$

## Proof boundary

The CUE benchmark in (3) and (5) is an **ensemble expectation** at finite
$N$; neither (1) nor (3) claims equality of the full CUE distribution.
The odd example only matches the *limit* of this one Gram moment. Its
weak Haar limit and bounded unit occupancy do not force CUE pairs.
Its nonzero traces are qualitative: no upper or mixed-sign Heisenberg trace
estimate is obtained. The construction is deliberately independent of
the cat-map dynamics and is not evidence against the fixed-map conjecture.
