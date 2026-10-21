> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/dual_original_pointwise_interference.md`. Embedded SHA256: `650d508cae0e6e19576497f03404d2beb1a5ab196081d177b402f8b221147408`.
> [Thematic guide](../../topics/histories.md).

# Order-one physical interference for the original fixed kick

Round 5, 21 October 2026. Owner: Weyl-dual branch.
Base checkpoint: round-4 package SHA256
e74f697134ea0d7d0ad5776c118ac267cf4999ae029e5b1f0252de364596fa4a.

## 1. Statement and input

This note proves a property of the exact original $U_N$, with
$\tau=10^{-80}$ fixed. It refutes the proposed auxiliary assertion
$\sup_{x,y}|N|U_N(x,y)|^2-1|\to0$; it is not a counterexample to
$H_{\rm diag}$ or to the desired point-process limit.

The proved input is the four-branch kernel in
dual_physical_four_branch_kernel.md, SHA256
0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c.
In particular its phase, amplitude, and column remainder are used with their
exact modular convention.

**Theorem.** Set
$$
 N_k=24k+3,\quad x_k=N_k/3,\quad y_k=0,\qquad
 F_k=N_k|U_{N_k}(x_k,0)|^2-1.
$$
Then
$$
 \limsup_{k\to\infty}|F_k|>\frac15.
 \tag{1.1}
$$
In fact the set of indices on which the absolute deviation is at least
$1/10$ has lower density at least $1/39$:
$$
 \liminf_{K\to\infty}
 \frac1K\#\{0\le k<K:|F_k|\ge1/10\}\ge\frac1{39}.
 \tag{1.2}
$$
This arithmetic progression is used only to falsify the pointwise
flatness assertion. The main spectral problem is not restricted to it.

## 2. Four distinct exact actions at one physical point

Write $t=\tau/(2\pi)$, and evaluate the kernel phases at
$(q,r)=(1/3,0)$. The four initial momenta are
$$
 p_m^0=(m-1)/4,\qquad m=0,1,2,3.
$$
In the exact symbol $a(q,p)=V(q)+r(q+1/2)\cos(2\pi p-\alpha_0)/100$,
one has
$$
 r(5/6)=(1-\tfrac12)(1+\tfrac12)=\frac34.
$$
Using $\cos\alpha_0=-3/5$ and $\sin\alpha_0=4/5$, the four values of
$a(1/3,p_m^0)-V(1/3)$ are, in order,
$$
 \left(-\frac3{500},-\frac9{2000},
                  \frac3{500},\frac9{2000}\right).
 \tag{2.1}
$$
They are strictly ordered with indices $0,1,3,2$, and the smallest
positive separation is $3/2000$.

Let $s_m=S_m(t,1/3,0)$ and $b_m=B_m(t,1/3,0)$, using the functions in
the kernel source. Its uniform action estimate gives
$$
 |s_m-t a(1/3,p_m^0)|\le35000t^2.
$$
The smallest leading separation is therefore perturbed by at most
$70000t^2$, which is strictly smaller than $3t/2000$ at the fixed
original $t$. Thus the exact actions, without truncating their series,
satisfy
$$
 s_0<s_1<s_3<s_2.
 \tag{2.2}
$$
In particular
$$
 \delta=s_2-s_0>0
 \tag{2.3}
$$
is the unique largest ordered difference among all $s_m-s_n$.
Also $|s_m|\le2t$, so every difference lies in $[-4t,4t]$, and
$0<24\delta<1$.

The amplitudes are positive and obey
$$
 |b_m^2-1|\le40000t,\qquad
 \frac{b_2b_0}{4}\ge\frac{1-40000t}{4}>\frac15.
 \tag{2.4}
$$

## 3. Exact modular coefficients on the progression

For $N_k\equiv3\pmod8$ one has $\nu_N=5$. Hence, on writing
$z=e^{\pi i/4}=e^{-15\pi i/4}$,
$$
 (g_0,g_1,g_2,g_3)=\tfrac12(z,1,-z,1).
$$
The $y$-dependent scalar is one at $y=0$. Moreover
$$
 e^{2\pi iN_k(\Theta_m-\Theta_0)(1/3,0)}
 =e^{2\pi iN_km/12}=i^m,
$$
because $N_k=24k+3$. The four constant coefficients after removing
the common initial phase are therefore
$$
 (c_0,c_1,c_2,c_3)=\tfrac12(z,i,z,-i).
 \tag{3.1}
$$
In particular $c_2\overline{c_0}=1/4$.

The per-column remainder in the kernel theorem gives an entry error
$O(N_k^{-1})$. Multiplying the entry by $\sqrt{N_k}$, and using the
boundedness of the four amplitudes, yields
$$
 F_k=
 \left|\sum_{m=0}^3 c_m b_m e^{2\pi i(24k+3)s_m}\right|^2-1+o(1).
 \tag{3.2}
$$
The error is in fact $O(N_k^{-1/2})$. All $s_m,b_m,c_m$ in (3.2)
are fixed numbers independent of $k$.

## 4. A nonvanishing Fourier coefficient in the dimension variable

Multiply (3.2) by $e^{-2\pi i24k\delta}$, sum from $k=0$ to $K-1$,
and divide by $K$. For a fixed real $\beta$,
$$
 \frac1K\sum_{k=0}^{K-1}e^{2\pi ik\beta}
 \longrightarrow
 \begin{cases}1,&\beta\in\mathbb Z,\\0,&\beta\notin\mathbb Z.\end{cases}
 \tag{4.1}
$$
This is the finite geometric-series formula, including its case
of ratio one. Thus no equidistribution theorem or irrationality
hypothesis on the actions is required.

For a term indexed by $(m,n)$, its frequency relative to the chosen
one is $24(s_m-s_n-\delta)$. Its absolute value is at most $192t<1$.
Consequently it can be an integer only if it is zero. By (2.2), only
$(m,n)=(2,0)$ has $s_m-s_n=\delta$. The constant term and the
subtracted one also have nonzero relative frequency, since
$0<24\delta<1$. The $o(1)$ error in (3.2) has Cesaro mean zero.
We have proved the exact limiting identity
$$
 \boxed{
 \lim_{K\to\infty}\frac1K\sum_{k=0}^{K-1}
 F_k e^{-2\pi i24k\delta}
 =\frac{b_2b_0}{4}e^{2\pi i3\delta}.}
 \tag{4.2}
$$
Its right-hand side has absolute value strictly greater than $1/5$.
The triangle inequality gives
$$
 \liminf_{K\to\infty}\frac1K\sum_{k=0}^{K-1}|F_k|
 \ge\frac{b_2b_0}{4}>\frac15,
 \tag{4.3}
$$
which proves (1.1).

Finally (3.2) and $\sum|c_m|=2$ imply
$$
 |F_k|\le4
$$
for all sufficiently large $k$: the squared amplitude in (3.2)
is between zero and $4(1+40000t)$, and its error tends to zero.
Let $p_K=K^{-1}\#\{0\le k<K:|F_k|\ge1/10\}$. Ignoring the finitely
many initial indices changes an average by $o(1)$, and
$$
 \frac1K\sum_{k<K}|F_k|
 \le\frac1{10}+\left(4-\frac1{10}\right)p_K+o(1).
$$
Combining this with (4.3) gives
$$
 \liminf p_K\ge
 \frac{1/5-1/10}{4-1/10}=\frac1{39}.
$$
This proves the claimed positive-density assertion.

## 5. What this excludes

The four-branch interference is a feature of the exact matrices at the
fixed kick, even though that kick is extremely small. A uniformly flat
physical modulus cannot be substituted for this kernel in an asymptotic
argument. The phase accumulated as $N$ grows distinguishes the
branches.

The theorem is compatible with convergence of the physical transition
matrix $P_N=(|U_{xy}|^2)$ to the constant matrix in operator norm up to
a small fixed smooth term: an entry deviation of order $1/N$ is not
an operator-norm obstruction. It is also compatible with sine-kernel
spectral statistics. The result is an exact discriminator for a
proposed proof step, not a spectral-statistics counterexample.

