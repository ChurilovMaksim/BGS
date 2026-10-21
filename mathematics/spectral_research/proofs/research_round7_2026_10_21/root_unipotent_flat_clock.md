> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round7_2026_10_21/root_unipotent_flat_clock.md`. Embedded SHA256: `8f8e4cdbcd5c6576eb6bb9ce976d7a29ae4e77a310271576719ee8e39ad9d0bd`.
> [Thematic guide](../../topics/algebra.md).

# An explicit obstruction to short-power mixing and reverse-edge criteria

Research continuation, 21 October 2026. All assertions in Sections 1–8
below are proved directly. This is a theorem about a **different**, fully
specified deterministic family of matrices. It is not a counterexample
to the prescribed $e^{i10^{-80}NA_N}M_N$, and it does not establish
any spectral asymptotic for that original family.

## 1. Exact statement and purpose

For every prime $p>3$, put $d=p^2$. We construct a unitary
$C_p\in U(d)$ satisfying simultaneously:

$$
C_p^p=I,
\qquad |(C_p^n)_{xy}|^2=\frac1d
\quad(1\le n<p,\ x,y\in\mathbb F_p^2),
\tag{1.1}
$$

and, for the reverse-edge matrix
$Q(C_p)_{xy}=(C_p)_{xy}\overline{(C_p)_{yx}}$,

$$
\|Q(C_p)\|_{\mathrm{op}}=d^{-1/2}.
\tag{1.2}
$$

Thus the transition probability matrix of every one of the first
$\sqrt d-1$ powers is exactly the uniform projection
$J_d=d^{-1}{\bf1}{\bf1}^T$. The reverse-edge operator norm tends
to zero as well. Nevertheless, for every fixed nonzero admissible
$b$ in the question,

$$
\frac{\Delta_{2,d}^{C_p}(b)}{\sqrt d}
\longrightarrow\int_0^\infty|\widehat b(u)|^2\,du>0,
\tag{1.3}
$$

and its randomly rotated local point process converges in probability
to the zero measure. The family therefore defeats a proposed argument
whose only inputs are flat entries, mixing of a growing number of
physical powers, and small reverse-edge norm. The original family has
additional phase structure; this theorem says nothing against an
argument that quantitatively uses that structure.

## 2. The finite-field propagator

Work in $\mathcal H_p=\ell^2(\mathbb F_p^2)$. Coordinates in this
section are $(k,l)$. All fractions in finite-field exponents mean
inverses in $\mathbb F_p$, possible because $p>3$. Define

$$
a_t(k,l)=\frac{t l^2}{2}+\frac{t^2kl}{2}+\frac{t^3k^2}{6},
\qquad
(V_t\psi)(k,l)=e_p(a_t(k,l))\psi(k,l+tk),
\quad t\in\mathbb F_p.
\tag{2.1}
$$

The coordinate map is a permutation and the multiplier has modulus
one, so every $V_t$ is unitary. Direct expansion gives

$$
\begin{aligned}
a_t(k,l)+a_s(k,l+tk)
={}&\frac{(t+s)l^2}{2}
  +\left(\frac{t^2+s^2}{2}+st\right)kl\\
&+\left(\frac{t^3+s^3}{6}+\frac{st^2+s^2t}{2}\right)k^2\\
={}&a_{t+s}(k,l).
\end{aligned}
\tag{2.2}
$$

Consequently

$$
V_tV_s=V_{t+s},\qquad V_0=I,\qquad V_1^n=V_{n\bmod p}.
\tag{2.3}
$$

No projective representation or unspecified Gauss phase enters this
identity.

Let the unitary Fourier transform be

$$
(\mathcal F\psi)(k,l)=p^{-1}
\sum_{x=(x_1,x_2)\in\mathbb F_p^2}
 e_p(kx_1+lx_2)\psi(x),
\qquad C_{p,t}=\mathcal F^*V_t\mathcal F,
\qquad C_p=C_{p,1}.
\tag{2.4}
$$

The unitarity follows from character orthogonality in each coordinate.
Equations (2.3) imply $C_p^n=C_{p,n\bmod p}$ and $C_p^p=I$.

## 3. Every nontrivial power is a flat matrix

Multiplying the three matrices in (2.4), with their stated Fourier
signs, yields

$$
(C_{p,t})_{xy}=p^{-2}\sum_{k,l\in\mathbb F_p}
e_p\left(a_t(k,l)+k(y_1-x_1+ty_2)+l(y_2-x_2)\right).
\tag{3.1}
$$

Write $z=(k,l)^T$, $v=Y_ty-x$, where

$$
H_t=\begin{pmatrix}t^3/3&t^2/2\\t^2/2&t\end{pmatrix},
\qquad Y_t=\begin{pmatrix}1&t\\0&1\end{pmatrix}.
\tag{3.2}
$$

The exponent is $\tfrac12z^TH_tz+z^Tv$. Its Hessian satisfies

$$
\det H_t=t^4/12\ne0\quad(t\ne0).
\tag{3.3}
$$

For completeness, if $H$ is any invertible symmetric matrix of
size two over $\mathbb F_p$, its quadratic Gauss sum
$G(H)=\sum_z e_p(\tfrac12z^THz)$ has modulus $p$. Indeed,
putting $z=w+r$ gives

$$
\begin{aligned}
|G(H)|^2
&=\sum_{r,w}e_p\left(w^THr+\tfrac12r^THr\right)\\
&=\sum_r e_p(\tfrac12r^THr)
       \sum_w e_p(w^THr)=p^2.
\end{aligned}
\tag{3.4}
$$

Only $r=0$ contributes, because $H$ is invertible. Completing
the square in (3.1) is a translation by $H_t^{-1}v$ and gives

$$
(C_{p,t})_{xy}=\frac{\gamma_{p,t}}p
e_p\left(-\frac12(Y_ty-x)^TH_t^{-1}(Y_ty-x)\right),
\qquad |\gamma_{p,t}|=1.
\tag{3.5}
$$

Thus $|(C_{p,t})_{xy}|=1/p=d^{-1/2}$ for every $t\ne0$,
which proves the flatness assertion for all $1\le n<p$.

## 4. The reverse-edge norm is also small

Set $G_t=H_t^{-1}$. The exact inverse and its mixed coefficient
are

$$
G_t=\begin{pmatrix}12/t^3&-6/t^2\\-6/t^2&4/t\end{pmatrix},
\qquad
D_t=G_tY_t=
\begin{pmatrix}12/t^3&6/t^2\\-6/t^2&-2/t\end{pmatrix}.
\tag{4.1}
$$

If $S_t(x,y)$ denotes the exponent in (3.5), expansion gives

$$
S_t(x,y)=-\tfrac12x^TG_tx
+x^TD_ty-\tfrac12y^TY_t^TG_tY_ty.
\tag{4.2}
$$

Therefore

$$
S_t(x,y)-S_t(y,x)
=A_t(x)-A_t(y)+x^TL_ty,
\tag{4.3}
$$

where $A_t(x)=\tfrac12x^T(Y_t^TG_tY_t-G_t)x$ and

$$
L_t=D_t-D_t^T
=\begin{pmatrix}0&12/t^2\\-12/t^2&0\end{pmatrix},
\qquad \det L_t=144/t^4\ne0.
\tag{4.4}
$$

It follows that $Q(C_{p,t})$ is obtained from the matrix
$R_t(x,y)=p^{-2}e_p(x^TL_ty)$ by left and right diagonal unitary
multipliers. Character orthogonality now gives

$$
(R_tR_t^*)_{xx'}=p^{-4}
\sum_y e_p((x-x')^TL_ty)=p^{-2}\delta_{xx'}.
\tag{4.5}
$$

Hence every singular value of $Q(C_{p,t})$ equals $1/p$.
In particular (1.2) holds, and in fact the same bound holds for
all the first $p-1$ powers. This last property is the part
missing from the simpler one-dimensional periodic chirp examples.

## 5. Exact traces and multiplicities

The trace can be computed before the Fourier conjugation. For
$t\ne0$, a coordinate $(k,l)$ is fixed by the permutation in
$V_t$ exactly when $k=0$. Consequently

$$
\operatorname{Tr}C_{p,t}=\sum_{l\in\mathbb F_p}e_p(tl^2/2),
\qquad |\operatorname{Tr}C_{p,t}|^2=p.
\tag{5.1}
$$

The one-dimensional version of the difference calculation (3.4)
proves the stated modulus. For every integer $n$, we have exactly

$$
|\operatorname{Tr}C_p^n|^2=
\begin{cases}
p^4,&p\mid n,\\
p,&p\nmid n.
\end{cases}
\tag{5.2}
$$

Here is also the full multiplicity description. Each fixed nonzero
$k$ gives one $p$-cycle in the $l$-coordinate. Its product
of phase factors is one, since

$$
\sum_{l\in\mathbb F_p}a_1(k,l)
=\tfrac12\sum_l l^2+\tfrac{k}{2}\sum_l l
 +\tfrac{k^2}{6}\sum_l1=0
\quad\text{in }\mathbb F_p.
\tag{5.3}
$$

For $p>3$, the two nonconstant power sums vanish. A weighted
cycle of length $p$ with phase product one has characteristic
polynomial $z^p-1$: an eigenvector recurrence goes once around
the cycle and imposes precisely $z^p=1$. Its roots are simple
over $\mathbb C$. Thus the $p-1$ nonzero $k$'s contribute
each $p$-th root with multiplicity $p-1$. The $k=0$
subspace contributes the diagonal eigenvalues $e_p(l^2/2)$.
The multiplicity of $e_p(a)$ is therefore

$$
\mu_a=p-1+\#\{l\in\mathbb F_p:l^2/2=a\}.
\tag{5.4}
$$

It lies between $p-1$ and $p+1$. In particular all $p$
roots occur.

## 6. A fixed factorial test diverges

Define the statistics of $C_p$ by exactly the rules in the
question, replacing dimension $N$ with $d=p^2$. For a fixed
admissible $b$, let $w(u)=|\widehat b(u)|^2$. It is a smooth
compactly supported nonnegative function. The exact order-two
Fourier identity is

$$
\Delta_{2,d}^{C_p}(b)
=d^{-2}\sum_{n\ge1}w(n/d)
\left(|\operatorname{Tr}C_p^n|^2-\min(n,d)\right).
\tag{6.1}
$$

To check its normalization, the ordered distinct-index sum at
$(n,-n)$ is $|\operatorname{Tr}C_p^n|^2-d$. The negative
index contributes its identical value; these two terms cancel the
factor $1/2!$. The zero index is the same for both spectra and
cancels. The CUE trace moment is $\min(|n|,d)$ for $n\ne0$,
as can equivalently be read from its explicit rank-$d$ Fourier
projection kernel.

More explicitly, this kernel is
$K_d(t,s)=\sum_{j=0}^{d-1}e^{2\pi i j(t-s)}$. Its two-point
factorial density is $d^2-|K_d(t,s)|^2$. For $n\ne0$,
integrating it against $e^{2\pi i n(t-s)}$ and adding the
diagonal contribution $d$ gives
$d-(d-|n|)_+=\min(|n|,d)$: in $|K_d|^2$, exactly
$(d-|n|)_+$ ordered Fourier pairs have the needed difference.
This supplies the trace-moment normalization directly from the
finite CUE kernel used in the question's reference construction.

Substituting (5.2) into the non-CUE part of (6.1) gives the exact
finite sum

$$
\frac1{d^2}\sum_{n\ge1}w(n/d)|\operatorname{Tr}C_p^n|^2
=\sum_{r\ge1}w(r/p)
+p^{-3}\sum_{\substack{n\ge1\\p\nmid n}}w(n/p^2).
\tag{6.2}
$$

Since $w$ has fixed compact support, the second term is
$O_b(p^{-1})$. Elementary Riemann-sum estimates, for instance
on each interval of length $1/p$ using $\int|w'|<\infty$,
give

$$
\sum_{r\ge1}w(r/p)=p\int_0^\infty w(u)\,du+O_b(1).
\tag{6.3}
$$

The CUE term in (6.1) is bounded independently of $p$: if
$\operatorname{supp}w\subset[-B,B]$, then

$$
0\le d^{-2}\sum_{n\ge1}w(n/d)\min(n,d)
\le B\|w\|_\infty.
\tag{6.4}
$$

This proves (1.3). If $b\ne0$, its nonnegativity implies
$\widehat b(0)=\int b>0$; continuity then makes the integral
in (1.3) strictly positive. Thus the same conclusion applies to
the one fixed test $b_*$ in the original research ledger, with
no choice of test depending on dimension.

The exact finite trace formula and the Riemann-sum argument are the
proof of the asymptotic. Small-prime computations only audit their
normalizations and do not supply that proof.

## 7. The local law tends to the empty process

There are exactly $p$ distinct eigenangles $a/p$. For a fixed
compact interval $[-L,L]$, the event that the unfolded point
process places any mass there requires the uniform rotation
$\alpha$ to lie within circular distance $L/p^2$ of at
least one of these $p$ angles. For sufficiently large $p$,
the union bound gives

$$
\mathbb P_\alpha\{\Xi_{d,\alpha}([-L,L])>0\}
\le\frac{2L}{p}\longrightarrow0.
\tag{7.1}
$$

Multiplicity does not enlarge this event. For every compactly
supported continuous test function $g$, its integral against
$\Xi$ is therefore zero with probability tending to one. This
is convergence to zero in probability in the vague topology: any
basic neighborhood of the zero measure is specified by finitely
many such tests, and one interval contains all their supports.

The intensity of every process remains exactly one by uniform
rotation. There is no contradiction: on an event of probability
of order $1/p$, a compact window can contain order $p$
coincident points. Their counts are not uniformly integrable.

## 8. Why this leaves the original problem open

The model is a quadratic propagator on $\mathbb F_p^2$, has
dimension $p^2$, and has period $p$. It is neither the given
one-dimensional Weyl quantization nor a subsequence of it. The
preceding theorem removes a possible abstract route to the
original result: no theorem based on the flatness and
reverse-edge assumptions in Sections 1 and 4 alone can imply
$H_{\mathrm{diag}}$.

In particular, knowing those estimates for the first 49 fixed
powers is insufficient by itself: even exact flatness for a number
of powers tending to infinity is insufficient. The needed original
estimate must use additional, quantitatively controlled phase
information at the scale relevant to its weighted trace sums.

A separate companion proof considers arbitrarily small deterministic
perturbations of this model and tests whether simplicity, absence of
exact gap coincidences, nonzero minors, and absence of a dark return
subspace can change this obstruction. Such perturbations are used
only to strengthen this abstract counterexample, never to replace
the original $U_N$.

## 9. Source status and reproducibility

The finite-field identities and limits in Sections 2–7 are proved
here without appealing to a metaplectic representation theorem.
Their interpretation is an exact obstruction to specified
assumptions, not a claim of priority in the literature.

The companion exact check script and its manifest specify the
finite ranges actually executed. They are independent of the
analytic asymptotic argument and are not an exhaustive search over
the original deterministic family.
