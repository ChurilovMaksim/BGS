# Distance to the unperturbed spectral orbit: proved global bounds

**Claim:** BGS-TRACE-110. **Status:** analytic proof with self-review.
The continuation, self-reviewed on 22 October, closes input (T) in [TRACE-113](fixed-map/fixed_kick_uniform_trace_bound.md).
An independent [TRACE-112 proof](fixed-map/displacement_density_trace_bound.md)
also gives the upper bound without pressure or the all-time quantum formula.

## Distances and the required trace input

For the original matrices of [TRACE-106](physical_kick_trace_decay.md), set

$$
d_N=\inf_{W\in U(N),\ |z|=1}\|U_N-zWM_NW^*\|_{\rm op}.
$$

The following quantitative input is now proved in TRACE-113:

$$
\exists C<\infty,\ N_0<\infty,\ a\in(1,\sqrt\lambda)\quad
\forall N\ge N_0\text{ odd}\quad\forall m\ge1:
\quad |\operatorname{Tr}U_N^m|\le Ca^m,
\qquad\lambda=3+2\sqrt2.                          \tag{T}
$$

The complete exact-amplitude, odd-sector and Gaussian arguments have now
been reconstructed, and the classical external input checked in its primary
source. For this application uniform continuity of the Gaussian scalar
at h=0 suffices; the older quantitative O(h^2) expansion is unnecessary.
Single-kick decay TRACE-106 alone does not imply (T).

## Exact scalar-root comparison

Let $U,V$ be unitaries of size $N$, with $V^m=\omega I$, $|\omega|=1$,
and put $A=|\operatorname{Tr}U^m|/N$. Then

$$
\|U-V\|_{\rm op}\ge2\sin\!\left(\frac{\arccos A}{2m}\right),
\quad
\frac{\|U-V\|_{\rm HS}}{\sqrt N}\ge\frac{\sqrt{2-2A}}m.
                                                               \tag{1}
$$

To prove the first bound, write $\delta=\|U-V\|$ and
$\beta=2\arcsin(\delta/2)$. The eigenvalues of $V^*U$ lie in
the arc of angles $[-\beta,\beta]$. A unitary path of angular length
$\beta$ joins $V$ to $U$; its $m$th power has angular length at most
$m\beta$. Since it starts at $\omega I$, if $m\beta<\pi/2$,
$|\operatorname{Tr}U^m|/N\ge\cos(m\beta)$. This proves the result;
if $m\beta\ge\pi/2$, it is immediate. For the second bound,
telescoping gives $\|U^m-V^m\|_{\rm HS}\le m\|U-V\|_{\rm HS}$,
and minimization over a scalar phase gives
$\inf_{|z|=1}N^{-1}\|U^m-zI\|_{\rm HS}^2=2-2A$.

There is also an eigenphase-count version. For any rotated $m$-clock,
the proportion of $U$ eigenphases within angular distance $b/m$,
$0<b<\pi$, is at most

$$
\frac{1+A}{1+\cos b}.                              \tag{2}
$$

Indeed the corresponding phases of $U^m$ have real part at least
$\cos b$ after rotation; all remaining real parts are at least $-1$.
Their average has real part at most $A$. This proves (2).

## Pell lower bound and global upper bound

Let $N_r=(\lambda^r-\lambda^{-r})/(4\sqrt2)$, with odd $r\ge3$.
Exact covariance gives $M_{N_r}^{2r}$ scalar. By (T),
$|\operatorname{Tr}U_{N_r}^{2r}|/N_r\to0$, since $a^2<\lambda$.
Taking $m=2r$ in (1) yields

$$
\liminf_{r\to\infty,\ r\text{ odd}}(\log N_r)d_{N_r}
\ge\frac{\pi\log\lambda}{4}.                      \tag{3}
$$

For the upper bound, the exact bare trace identity gives
$|\operatorname{Tr}M_N^m|^2=\#\ker(S^m-I)\le\lambda^m$.
By (T), both empirical spectral measures have exponentially bounded
short Fourier moments divided by $N$. A squared Fejér approximation to
interval indicators, truncated at a sufficiently small constant times
$\log N$, bounds both discrepancies by $O(1/\log N)$. Sorting the
eigenphases and matching the quantiles then gives

$$
d_N=O(1/\log N).                                  \tag{4}
$$

The full interval approximation and sorted matching argument, including
the cyclic endpoint, are in the
[source proof](spectral_research/proofs/research_round14_2026_10_21/obstruction/r14_original_spectral_orbit_barrier.md).
Equations (3)--(4) therefore give $\Theta(1/\log N_r)$ for the original
fixed family. The independent TRACE-112 argument supplies (4) as well. The exact tower $r=3\cdot7^s$ has $v_7(N_r)=s+1$.

## Why this does not contradict the single-kick theorem

TRACE-106 gives $\inf_z\|U_N-zM_N\|_{\rm op}\to2$ without varying
the conjugating basis. Here $W$ is arbitrary. These are different
distances. Neither global spectral matching at scale $1/\log N$ nor
its Pell lower bound determines spacings at scale $1/N$.
