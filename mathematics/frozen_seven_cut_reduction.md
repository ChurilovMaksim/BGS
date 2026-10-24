# Seven-cut reduction at the exact frozen coupling

**Claim ID:** `BGS-FM-007`. **Status:** project proof, author-level audit and
exact finite regression. Based on Sections 13–17 and 35–37 of the submitted
87-page article *Local spectral statistics of a fixed quantum cat map* (24
September 2026; PDF SHA-256
`aeb0f82d35b3d40eb2e9a3fded9417c55df95e393f3de148f01457ecad844454`).
This is a maintained, self-contained version of its new reduction, not an
independent referee decision or a local CUE theorem. The raw-versus-ordinary
Weyl correction and Jacobi structure were already recorded in `BGS-FM-001`
and `BGS-FM-005` respectively.

## Statement and exact normalization

Let $N\ge3$ be odd, $h=2^{-1}\pmod N$, $\tau=10^{-80}$ and
$U_N=e^{i\tau N A_N}M_N$ with the raw modular Weyl symbol of
[`fixed_model_symmetry_theorem.md`](fixed-map/fixed_model_symmetry_theorem.md). In the
standard coordinate basis the *unmodified* Hermitian generator has the exact
cyclic Jacobi form

$$
(A_N\psi)(x)=v(x/N)\psi(x)+b_N(x)\psi(x+1)
                   +\overline{b_N(x-1)}\psi(x-1),\quad
b_N(x)=\frac{e^{-i\alpha}}{200}
 r\left(\frac{x+h}{N}\right),                         \tag{1}
$$

where $r(q)=(1-\cos14\pi q)(1+\cos2\pi q)$,
$e^{i\alpha}=(-3+4i)/5$ and
$v(q)=\cos14\pi q+r(q)/10+r(q)\sin2\pi q/100-1/10$.
For $N\ge15$ define

$$
s_j=\left\lfloor\frac{jN}{7}+\frac12\right\rfloor,\quad
x_j=s_j-h\pmod N\quad(0\le j<7),\qquad s_7=N,
$$

and erase precisely the seven off-diagonal edges $x_j\leftrightarrow x_j+1$
from $A_N$, obtaining $A_N^{\rm cut}$. Define the **full** approximant
$V_N=e^{i\tau N A_N^{\rm cut}}M_N$. Put $V_N=U_N$ at the finitely many odd
$N<15$. In particular, **$M_N$ is retained**; the approximant is not a
direct sum of seven quantum propagators.

**Theorem 1 (generator and full propagator).** The generator
$A_N^{\rm cut}$ is a sum of seven path Jacobi matrices, each of size
$s_{j+1}-s_j\in\{\lfloor N/7\rfloor,\lceil N/7\rceil\}$. For $7\mid N$,
$A_N^{\rm cut}=A_N$ exactly. For $7\nmid N$, the difference has rank 12.
For all odd $N\ge15$, with unnormalized nuclear norm $\|\cdot\|_1$,

$$
\begin{aligned}
 \|A_N-A_N^{\rm cut}\|_1&\le\frac{28\pi^2}{25N^2},&
 \|A_N-A_N^{\rm cut}\|&\le\frac{9\pi^2}{50N^2},\\
 \|U_N-V_N\|_1&\le\frac{28\pi^2\tau}{25N},&
 \|U_N-V_N\|&\le\frac{9\pi^2\tau}{50N}.       \tag{2}
\end{aligned}
$$

In particular $|\operatorname{Tr}U_N^m-\operatorname{Tr}V_N^m|
\le(28\pi^2\tau/25N)|m|$ for *every integer* $m$. This is a bound on
absolute trace **differences**, not an estimate of either trace.

Let $C_{k,N}^W(H)$ be the translation-invariant factorial local statistic
of [`trace_to_local_statistics_bridge.md`](trace-bridge/trace_to_local_statistics_bridge.md),
with phases $\theta_j\in\mathbb R/\mathbb Z$ and unfolded spacing $1$:

$$
C_{k,N}^W(H)=\frac1N\sum_{\substack{j_1,\ldots,j_k\\j_a\ \mathrm{distinct}}}
\sum_{n\in\mathbb Z^{k-1}}
H\!\left(\bigl(N(\theta_{j_a}-\theta_{j_k}+n_a)\bigr)_{a<k}\right).
$$

Write $F_{N,W}(s)=N^{-2}\sum_{m\ge1}e^{-2sm/N}|\operatorname{Tr}W^m|^2$.

**Theorem 2 (microscopic transfer).** For any sequences of unitary $N$ by
$N$ matrices $W_N,Z_N$ satisfying
$\|W_N-Z_N\|,\|W_N-Z_N\|_1=O(N^{-1})$, the full fixed-$k$
sine-kernel law for all Schwartz tests holds for $W_N$ **if and only if** it
holds for $Z_N$. If a single nonnegative $H_0\in\mathcal S(\mathbb R^{k-1})$
with $H_0\ge1$ on $[-1,1]^{k-1}$ satisfies
$\sup_N C_{k,N}^{Z}(H_0)<\infty$, then for any fixed Schwartz $H$,

$$
|C_{k,N}^{W}(H)-C_{k,N}^{Z}(H)|=O_{H,k}(N^{-1/k}). \tag{3}
$$

Consequently the all-order sine-kernel statements for **$U_N$ and $V_N$ are
equivalent**. The seven path blocks are not independent sectors of $V_N$.

**Theorem 3 (unconditional pair transfer).** For every fixed $s>0$ and
$H\in\mathcal S(\mathbb R)$,

$$
F_{N,U}(s)-F_{N,V}(s)=O_s(\tau/\log N),\qquad
C_{2,N}^{U}(H)-C_{2,N}^{V}(H)=O_H(\tau/\log N).        \tag{4}
$$

Both differences tend to zero on the *whole odd sequence* at the unchanged
fixed $\tau$. Equation (4) does not assert convergence of either Abel sum.
For higher $k$, (3) applies when the indicated positive test is bounded; no
unconditional $O(\tau/\log N)$ assertion is made.

## Proof of Theorem 1

The matrix form (1) follows directly from the raw Weyl convention
$e^{2\pi i(kq+\ell p)}\mapsto T_N(\ell,k)$: the $\ell=1$ term has matrix
entry $e^{-i\alpha}r((x+h)/N)/200$ at $(x,x+1)$. The diagonal terms give
$v$, including the scalar centering. This also checks that the half-shift of
the *ordinary symbol* must never replace the modular $h$ in (1).

The differences $s_{j+1}-s_j$ have the asserted sizes, and the selected
edges have disjoint endpoints because each interval has length at least
$\lfloor N/7\rfloor\ge2$. Set $\delta_j=s_j/N-j/7$. If $7\nmid N$,
multiplication by $N$ permutes the nonzero residue classes modulo $7$;
nearest-integer rounding therefore gives exactly

$$
\max_{0\le j<7}|\delta_j|=\frac3{7N},\qquad
\sum_{j=0}^6\delta_j^2=\frac4{7N^2}.                \tag{5}
$$

If $7\mid N$, these errors all vanish. By $1-\cos t\le t^2/2$ and
$1+\cos(2\pi q)\le2$,
$r(s_j/N)\le196\pi^2\delta_j^2$. Each erased off-diagonal edge is a
Hermitian two by two matrix with two singular values $|b_N(x_j)|$.
Their endpoints are disjoint, hence (5) gives the two generator bounds in
(2). The $j=0$ edge vanishes exactly; for $7\nmid N$ the other six are
nonzero since on an odd grid $1+\cos2\pi q\ne0$ and
$1-\cos14\pi s_j/N=0$ would force $N\mid7s_j$. Thus the rank is 12.

For self-adjoint $A,B$ and real $t$, Duhamel's formula gives, for both the
operator and nuclear norms,
$\|e^{itA}-e^{itB}\|_*\le|t|\|A-B\|_*$. Take $t=\tau N$ and multiply
by the unitary $M_N$. Telescoping $U^m-V^m$ in nuclear norm proves the
unrestricted trace comparison. The proof does **not** require $\tau N$ to
stay small.

## Proof of Theorem 2: simultaneous phase coupling and occupancy

For unitary $W,Z$ take a Hermitian logarithm $K$ of $WZ^*$ with spectrum in
$[-\pi,\pi]$. Since $|x|\le(\pi/2)|e^{ix}-1|$ on this interval, spectral
calculus gives
$\|K\|_*\le(\pi/2)\|W-Z\|_*$ for $*\in\{\mathrm{op},1\}$.
Follow the eigenphases of $e^{itK}Z$, including crossings by diagonalizing
the compressed derivative at each crossing. A single labelling then yields
$\theta_j(W)=\theta_j(Z)+d_j/N\pmod1$ and **simultaneously**

$$
D:=\max_j|d_j|\le\frac N4\|W-Z\|,\qquad
L:=\sum_j|d_j|\le\frac N4\|W-Z\|_1.                 \tag{6}
$$

For a phase configuration $\Phi$, let $M_\Phi$ be the largest number of
points in a half-open interval of length $1$ in its periodic unfolding
$\{N(\phi_j+n):j\le N,n\in\mathbb Z\}$. Interpolate the coupled phases
linearly. If $D$ is bounded, throughout the path the occupancy is at most
$(\lceil2D\rceil+2)M_\Phi$. Differentiate the periodized $C_{k,N}$.
When a coefficient $d_j$ occurs, choose its point as anchor; changing from
the old anchor has determinant $\pm1$ on the integer lift lattice.
Summing the derivatives of $H$ on unit cubes gives, for every Schwartz $H$,

$$
|C_{k,N}^{W}(H)-C_{k,N}^{Z}(H)|
 \le C_{H,k,D}\frac{L}{N}M_Z^{k-1}.                 \tag{7}
$$

This also holds for $k=2$ and $h_s(x)=s/(s^2+\pi^2x^2)$ because its
derivative has summable unit-interval suprema.

Choose nonnegative $H_0\ge1$ on $[-1,1]^{k-1}$. If an unfolded unit
interval contains $M_Z$ points, the falling factorial $(M_Z)_k$ ordered
distinct tuples contribute at least $(M_Z)_k/N$ to $C_{k,N}^Z(H_0)$.
For $M_Z\ge2k$, $(M_Z)_k\ge(M_Z/2)^k$. Thus

$$
M_Z\le2k+2\bigl(NC_{k,N}^{Z}(H_0)\bigr)^{1/k}.    \tag{8}
$$

Under the hypotheses of Theorem 2, (6) gives $D,L=O(1)$, and a bounded
positive test gives $M_Z=O(N^{1/k})$. Insert in (7). Sine-kernel convergence
for all Schwartz tests implies the positive test is bounded. The argument is
symmetric in $W,Z$, proving both directions of equivalence.

## Short-time trace input used for the unconditional bound

For completeness, the following is the model-specific input of Theorem 3;
it is the logarithmic-time result of Section 16 of the submitted article.
There exist $c,C>0$ such that for every large odd $N$ and
$1\le m\le c\log N$,

$$
|\operatorname{Tr}U_N^m|\le C N^{39/40}.           \tag{9}
$$

Here are its needed analytic estimates and geometric argument. In ordinary
midpoint quantization $A_N=\operatorname{Op}_N(g)$ for the explicitly
corrected finite symbol of `BGS-FM-001`, and
$M_N\operatorname{Op}_N(a)M_N^{-1}=\operatorname{Op}_N(a\circ S)$ exactly.
Fourier multiplication gives

$$
\|\operatorname{Op}_N(a)\operatorname{Op}_N(b)-
\operatorname{Op}_N(ab)\|\le C N^{-1}\|a\|_{C^4}\|b\|_{C^4},
$$

$$
\|U_N^m\operatorname{Op}_N(a)U_N^{-m}
 -\operatorname{Op}_N(a\circ G^m)\|
\le C N^{-2}e^{Cm}\|a\|_{C^6},\quad
G=S\circ\Phi_g^{\tau/(2\pi)}.                   \tag{10}
$$

The second estimate follows by expanding the Weyl sine commutator to third
order (one-step remainder $O(N^{-2})$ after multiplying by $i\tau N$),
using Duhamel on the fixed classical time, and iterating the $C^6$ bounds.
Four Fourier integrations by parts give the displayed $C^4$ product estimate;
six give the cubic remainder. The conjugation convention in (10) is
$U_N^m(\cdot)U_N^{-m}$, so there is no inverse-map switch.

In entrywise order $DG(z)\ge B=\left(\begin{smallmatrix}5/2&7/2\\3/2&5/2
\end{smallmatrix}\right)>0$: $\|DG-S\|_\infty<1/2$ follows from the
fixed $\tau=10^{-80}$ and the explicitly bounded derivatives of $g$.
Because $G$ preserves area, $\det DG^m=1$, and
$\operatorname{Tr}DG^m\ge\operatorname{Tr}B^m=\lambda_-^m+\lambda_-^{-m}$
with $\lambda_-=(5+\sqrt{21})/2>1$. The displacement
$z\mapsto G^m z-z$ is a covering of degree
$d_m=|\det(S^m-I)|=\lambda^m+\lambda^{-m}-2$ and its Jacobian
has absolute value at least $c\lambda_-^m$ (in fact
$\det(DG^m-I)=2-\operatorname{Tr}DG^m$). For measurable $E$,

$$
|\{z:G^mz-z\in E\}|\le C(\lambda/\lambda_-)^m|E|.  \tag{11}
$$

Put $b_1(z)=e^{2\pi iq}$, $b_2(z)=e^{2\pi ip}$,
$d_j=b_j\circ G^m-b_j$, $D_m=|d_1|^2+|d_2|^2$.
Equation (11) gives $|\{D_m\le2\delta^2\}|\le Ce^{Cm}\delta^2$.
Let $\chi_\delta=\chi(D_m/\delta^2)$ with $\chi=1$ on $[0,1]$ and
$0$ on $[2,\infty)$, and set
$a_j=(1-\chi_\delta)\overline d_j/D_m$ away from $D_m=0$ (zero
near it). Then $\sum a_jd_j=1-\chi_\delta$ and
$\|\chi_\delta\|_{C^4}\le Ce^{Cm}\delta^{-8}$,
$\|a_j\|_{C^4}\le Ce^{Cm}\delta^{-10}$.
Cyclicity of the trace applied to $\operatorname{Op}_N(b_j)$,
equation (10) and the product estimate imply, for
$\mathcal L_m(a)=N^{-1}\operatorname{Tr}(U_N^{-m}\operatorname{Op}_N(a))$,
$|\mathcal L_m(a_jd_j)|\le C N^{-1}e^{Cm}\|a_j\|_{C^4}$.
The normalized Hilbert–Schmidt estimate
$N^{-1}\operatorname{Tr}\operatorname{Op}_N(\chi)^*
\operatorname{Op}_N(\chi)
\le\|\chi\|_{L^2}^2+C N^{-1}\|\chi\|_{C^4}^2$
then gives

$$
N^{-1}|\operatorname{Tr}U_N^m|
 \le C e^{Cm}\bigl(\delta+N^{-1/2}\delta^{-8}
                    +N^{-1}\delta^{-10}\bigr).       \tag{12}
$$

Taking $\delta=N^{-1/20}$ and $m\le c\log N$ for sufficiently small
$c>0$ proves (9). This proof uses logarithmic-time Egorov only; it does not
assume Heisenberg-time trace cancellation.

## Proof of Theorem 3 and precise remaining obstruction

For $J=\lfloor c\log N\rfloor\ge3$ and any phase interval of length
$1/N$ centered at $a$, the positive Fejér polynomial
$\mathcal F_J(t)=J^{-1}|\sum_{\ell=0}^{J-1}e^{2\pi i\ell t}|^2$
obeys $\mathcal F_J(t)\ge4J/\pi^2$ on that interval when $J\le N$.
By (9),

$$
\sum_{j=1}^N\mathcal F_J(\theta_j-a)
 \le N+2\sum_{m=1}^{J-1}|\operatorname{Tr}U_N^m|
 \le N+2CJ N^{39/40}\le2N.
$$

Therefore $M_U\le C N/\log N$. Equation (6) for $U,V$ gives
$D\le9\pi^2\tau/200$ and $L\le7\pi^2\tau/25$.
A shifted unit interval is covered by a bounded number of original
intervals, so $M_V\le C N/\log N$ as well. Put $k=2$ in (7) to obtain the
second estimate (4) without any assumed pair limit.

The Fourier transform of $h_s(x)=s/(s^2+\pi^2x^2)$ is
$e^{-2s|\xi|}$ in our convention. Its periodization gives the **exact**
identity for any unitary $W$,

$$
F_{N,W}(s)=\tfrac12 C_{2,N}^{W}(h_s)
                  +\frac1{2N}\coth(s/N)-\tfrac12.     \tag{13}
$$

The spectrum-independent terms cancel on subtraction, and (7) for $h_s$
proves the first estimate (4) for the entire infinite Abel sum.

Finally, for the path projector $P_a$ of rank $L_a$, the flat kernel
$|(M_N)_{xy}|^2=1/N$ yields
$\|P_aV_NP_b\|_{\rm HS}^2=L_aL_b/N$. For any proper nonempty union
$P_J$ of paths of total dimension $d$,

$$
\|(I-P_J)V_NP_J\|_{\rm HS}^2=\frac{d(N-d)}N,
\quad \|[P_J,V_N]\|_{\rm HS}^2=\frac{2d(N-d)}N>0.  \tag{14}
$$

Thus the seven path projectors do not commute with the full propagator.
No bound in this note controls the **values** of the joint traces of $V_N$
at $|m|\asymp N$. The mixed-sign cancellations required by
`BGS-TRACE-005` and the sine-kernel statement `BGS-BGS-001` remain OPEN.

## Verification boundary

[`frozen_seven_cut.py`](../computations/verification/frozen_seven_cut.py)
replays exact rational geometry, the constants in (2)/(6), and finite
combinatorial identities used in (7)/(8)/(13). The finite direct raw-Weyl
matrix check and full submission audit are documented in
[`record/frozen_seven_cut_review_20260924.md`](../archive/record/frozen_seven_cut_review_20260924.md).
Neither computation proves (9), the all-$N$ statement, or a CUE limit.
