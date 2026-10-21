> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/phase_planck_hole_time_scale_test.md`. Embedded SHA256: `a2a9841076214829102027a862cdb92c10dba93bef376dc06481bfc3082ceb4d`.
> [Thematic guide](../../topics/dephasing.md).

# Planck-width diagonal removal: an exact dimension-and-time test

Research continuation, 21 October 2026.

**Status.** This note gives an exact finite-dimensional bound for the original doubled quantum map
$\mathcal C_N=\operatorname{Ad}_{U_N}$, after a positive coherent-state cutoff of a Planck-width neighborhood of the classical pair diagonal. It rules out uniform exponential decay in the physical operator norm, and in norms polynomially equivalent to it, for this opened operator. It does not rule out cancellation of its trace, does not transfer a spectral statement from anisotropic spaces without a norm comparison, and does not prove $H_{\rm diag}$.

No semiclassical trace formula is needed.

## 1. Exact finite Weyl tight frames

Choose any unit vector $v_N\in\mathbb C^N$, and define

$$
v_z=T_N(a,b)v_N,\qquad z=(a,b)\in(\mathbb Z/N\mathbb Z)^2.
$$

A periodically summed discrete Gaussian is one possible choice when a spatially localized coherent state is wanted:

$$
v_N(x)=c_N\sum_{\ell\in\mathbb Z}
 \exp[-\pi(x+\ell N)^2/N],
$$

where $c_N>0$ normalizes the vector. The algebraic statements below hold for every unit $v_N$.

Weyl character orthogonality gives the exact twirl identity

$$
\frac1N\sum_z|v_z\rangle\langle v_z|=I_N.
\tag{1}
$$

Here is a direct proof. The $(x,y)$ entry of
$\sum_{a,b}T(a,b)|v\rangle\langle v|T(a,b)^*$
contains the factor $\sum_b e_N(b(x-y))=N\mathbf1_{x=y}$. When $x=y$, the remaining sum is
$N\sum_a|v(x+a)|^2=N$.
The modular midpoint phases cancel; oddness is used only in the definition of the Weyl system.

Identify the Hilbert--Schmidt space
$\mathcal V_N=M_N(\mathbb C)$ with
$\mathbb C^N\otimes\overline{\mathbb C^N}$.
It has dimension $D_N=N^2$. Its normalized rank-one vectors

$$
\phi_{z,w}=v_z\otimes\overline{v_w}
$$

satisfy

$$
\frac1{N^2}\sum_{z,w}
 |\phi_{z,w}\rangle\langle\phi_{z,w}|=I_{\mathcal V_N}.
\tag{2}
$$

## 2. A Planck-scale pair-diagonal effect with exact trace

Fix $c>0$, independent of $N$, and put
$R_N=\lfloor c\sqrt N\rfloor$.
For sufficiently large $N$, $2R_N+1<N$.
For a residue $a\pmod N$, write $|a|_N$ for the minimum absolute value of its integer representatives. Let

$$
\chi_N(z-w)
=\mathbf1_{\{|a_z-a_w|_N\le R_N,\,
              |b_z-b_w|_N\le R_N\}}.
$$

The centers $z/N,w/N$ then differ by at most $cN^{-1/2}$ in each torus coordinate. Define the positive effect

$$
E_N=\frac1{N^2}\sum_{z,w}\chi_N(z-w)
 |\phi_{z,w}\rangle\langle\phi_{z,w}|.
\tag{3}
$$

Equations (2)--(3) imply

$$
0\le E_N\le I_{\mathcal V_N}.
$$

Since every $\phi_{z,w}$ is a unit vector and each $z$ has exactly
$(2R_N+1)^2$ allowed differences $z-w$,

$$
\boxed{\displaystyle
q_N:=\operatorname{Tr}_{\mathcal V_N}E_N
=(2R_N+1)^2=4c^2N+O_c(\sqrt N).}
\tag{4}
$$

This exact trace is the relevant quantum size of the removed diagonal tube. It is order $N$, while the whole doubled quantum space has dimension $N^2$.

One may replace $\chi_N$ by any weights in $[0,1]$; the same argument gives positivity and the exact trace $\sum_\delta\chi_N(\delta)$. Thus sharp spatial indicators are not essential to the estimates below.

## 3. Opening the exact doubled propagator

On $\mathcal V_N$, the exact map

$$
\mathcal C_N(X)=U_NXU_N^*
$$

is unitary. Let $S_N=(I-E_N)^{1/2}$, and open the map by

$$
\mathcal K_N=\mathcal C_N S_N.
\tag{5}
$$

This is a contraction, and

$$
\mathcal K_N^*\mathcal K_N=I-E_N.
\tag{6}
$$

For every $m\ge1$, the elementary telescoping identity is

$$
I-\mathcal K_N^{*m}\mathcal K_N^m
=\sum_{j=0}^{m-1}
 \mathcal K_N^{*j}E_N\mathcal K_N^j.
\tag{7}
$$

Taking traces and using
$\mathcal K_N^j\mathcal K_N^{*j}\le I$ gives

$$
0\le D_N-\|\mathcal K_N^m\|_{\rm HS}^2
=\sum_{j=0}^{m-1}
 \operatorname{Tr}(E_N\mathcal K_N^j\mathcal K_N^{*j})
\le m q_N.
$$

Consequently

$$
\boxed{\displaystyle
\|\mathcal K_N^m\|_{\rm HS}^2\ge N^2-m(2R_N+1)^2,\qquad
\|\mathcal K_N^m\|_{\rm op}
\ge\sqrt{\max\{0,1-mq_N/N^2\}}.}
\tag{8}
$$

All phases of the original $U_N$ are retained in $\mathcal K_N$. The proof has not replaced the quantum operator by a classical stochastic matrix.

Two time-scale consequences are immediate.

First, for every fixed $a>0$,

$$
\|\mathcal K_N^{\lfloor a\log N\rfloor}\|_{\rm op}
\ge1-O_{a,c}((\log N)/N).
\tag{9}
$$

Second, for $0<t<1/(4c^2)$,

$$
\liminf_{\substack{N\to\infty\\N\ {\rm odd}}}
\|\mathcal K_N^{\lfloor tN\rfloor}\|_{\rm op}
\ge\sqrt{1-4c^2t}>0.
\tag{10}
$$

Thus Planck-width diagonal removal does not create a fixed exponential contraction rate on the remaining physical quantum space.

More generally, for any positive effect $0\le E\le I$ on a $D$-dimensional Hilbert space and any unitary $\mathcal C$, the same proof gives
$\|(\mathcal C\sqrt{I-E})^m\|_{\rm op}^2
 \ge1-m\,\operatorname{Tr}E/D$.
If a reduction requires this norm to be at most $1/2$ already at time $m$, it is necessary that

$$
\operatorname{Tr}E\ge\frac{3D}{4m}.
\tag{11}
$$

At $D=N^2$ and $m=O(\log N)$, this requires an effect of trace
$\Omega(N^2/\log N)$. For the same square-tube quantization, its radius is at least order $(\log N)^{-1/2}$, rather than $N^{-1/2}$.

## 4. The exact scope of the Dolgopyat norm obstruction

There cannot exist fixed $A,C,\gamma>0$ such that

$$
\|\mathcal K_N^m\|_{\rm op}\le C N^A e^{-\gamma m}
\tag{12}
$$

for all sufficiently large odd $N$ and every $m$ beyond a fixed multiple of $\log N$. Indeed choose a fixed $a$ larger than both that multiple and $(A+1)/\gamma$, and set $m=\lfloor a\log N\rfloor$. The right side tends to zero while (9) tends to one.

The same conclusion holds if the proposed norm is polynomially equivalent to the physical norm: assume, for a vector norm $\|\cdot\|_{*,N}$,

$$
N^{-B}\|X\|_2\le \|X\|_{*,N}\le N^B\|X\|_2
$$

for a fixed $B$. Such a comparison only adds a factor $N^{2B}$ to (12), and the same choice of a larger logarithmic time contradicts (9).

No statement is made here about arbitrary anisotropic norms. They need not be polynomially equivalent to the physical norm on the relevant states. A theorem in such a norm must be supplied with the comparison needed to control the particular quantum trace functional before it can be used.

Nor does (8) rule out a bound on the **signed trace**
$\operatorname{Tr}_{\mathcal V_N}\mathcal K_N^m$.
Large operator or Hilbert--Schmidt norm is compatible with a small trace. This trace distinction is precisely what remains relevant for the original question.

## 5. Attempted conversion of leakage into the needed trace bound

The leakage identity (7) is positive and controls total lost norm. To test whether it could by itself estimate the original trace pair, write

$$
\mathcal C_N-\mathcal K_N
=\mathcal C_N(I-S_N).
$$

Since $0\le I-\sqrt{I-E_N}\le E_N$,

$$
\|\mathcal C_N-\mathcal K_N\|_1
=\operatorname{Tr}(I-S_N)\le q_N.
$$

The exact telescoping difference of powers yields

$$
\boxed{\displaystyle
|\operatorname{Tr}(\mathcal C_N^m-\mathcal K_N^m)|
\le m q_N.}
\tag{13}
$$

Here
$\operatorname{Tr}_{\mathcal V_N}\mathcal C_N^m
=|\operatorname{Tr}U_N^m|^2$.
For a fixed bounded weight $w$ supported in $[0,B]$, (13) only gives

$$
\frac1{N^2}
\left|
\sum_{m\ge1}w(m/N)
 \operatorname{Tr}(\mathcal C_N^m-\mathcal K_N^m)
\right|
\le
\frac{q_N\|w\|_\infty}{N^2}
 \sum_{m\le BN}m
=O_{B,c,w}(N).
\tag{14}
$$

The desired normalized error would be $o(1)$. This executed estimate therefore misses the needed scale by at least one power of $N$. Passing from (7) to a trace estimate by absolute values has not gained the required cancellation.

The sign information in the trace difference is absent from the positive terms in (7). Hence the leakage calculation does not justify discarding the opened part, replacing it by a universal term, or resumming the signed return words. The first unresolved trace-pair estimate is still the one specified in the original task.

