> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/root_audit_quantitative_gauge_reversal.md`. Embedded SHA256: `adeb7344ee728cccfb90b169582e8d4afac89d5e92f2e2cff367057a2b5c87f2`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/symmetry.md).

# Independent reconstruction of the quantitative gauge-reversal obstruction

21 October 2026. Reviewer: `/root`.

Reviewed source: `audit_quantitative_gauge_reversal_obstruction.md`, SHA-256
`7cb30d1ef2cba42132c5aff08d06fd931be1175c87fd2bdc26a8b4de3a8c2c29`.
The complete source was read and the argument below was reconstructed from
the specified matrices. This is a mathematical audit, not a Lean certificate
or an assertion of external peer review.

## Verdict and exact scope

The proof establishes, for every odd integer $N\ge10^7$, every diagonal
unitary $D$, and every unit scalar $\eta$,

$$
 N^{-1/2}\|D\overline{U_N}D^*-\eta U_N^*\|_{\rm HS}>10^{-328}.
$$

There is no restriction on the diagonal phases or their dependence on $N$.
The same lower bound follows for operator norm. This excludes an approximate
reversal in this precise coordinate-gauge class; it does not exclude
arbitrary antiunitaries, prove simplicity of the spectrum, or imply any
local spectral-statistics limit.

## 1. Convention and cut-chain checks

For unreduced integer labels, the ordinary-half Weyl matrix satisfies
$W_N(k,l)=(-1)^{kl}T_N(l,k)$. Indeed the modular inverse of two is
$(N+1)/2$, and the additional exponential factor is exactly
$e^{\pi i kl}=(-1)^{kl}$. It follows that the actual Hamiltonian symbol
in this convention has mixed coefficient $R(q)=r(q+1/2)$, not $r(q)$.
For $l=\pm1$, multiplication of the original Fourier coefficients by
$(-1)^k$ gives this translation directly. The $l=0$ symbol is unchanged.

The original modular hopping entry is
$\gamma r((x+(N+1)/2)/N)$, with
$\gamma=(-3-4i)/1000$. The odd grid contains exactly $\gcd(7,N)$
zeros, all from $7q\in\mathbb Z$; the zero at $q=1/2$ is absent.
Thus a phase-gauged path decomposition exists, including one cut when
$7\nmid N$. There is no uncut magnetic cycle on which to base a flux
argument. The geometric-sum estimate on each path is
$2/|1-e^{2i\alpha_0}|=5/4$, and the displayed cat defect follows
entry by entry from $|M_{xy}|^2=1/N$.

## 2. Exact commutators and the remainder

Multiplication gives
$W_uW_v=e^{\pi i(u_2v_1-u_1v_2)/N}W_{u+v}$. Combining the two
orders yields the exact generator

$$
 (i/h)[A_N,W_v]
 =-4\pi N\sum_u a_u\sin(\pi\omega(u,v)/N)W_{u+v}.
$$

No large-$N$ replacement has occurred here. The cat transports
$(1,0)$ to $(3,4)$. The parity needed to transfer the cat identity
from modular to ordinary halves holds since
$(3k+2l)(4k+3l)-kl=12k^2+16kl+6l^2$ is even.

The Fourier coefficient mass is bounded by
$1.1+.04+.04=1.18<2$. At bracket number $j+1\le5$,
$|\omega(u,v)|\le39+18j\le111$. Therefore the fivefold commutator
has operator norm less than $14208^5<10^{21}$, uniformly in $N$.
The exact integral Taylor remainder uses unitary conjugation, whose
operator norm as a map on matrices is one. Hence its contribution to the
normalized trace is at most $10^{21}t^5$, independently of $N$.
In particular no factor such as $e^{cNt}$ has been discarded.

## 3. The fourth coefficient

Returning the shift label four to zero in four brackets forces four
$l=-1$ insertions. All lower orders vanish for $N\ge35$. At order
four the possible modulation differences from the target label one lie
in $[-30,34]$, so no modular aliases occur in this range of $N$.

With $\mathcal D=(2\pi i)^{-1}\partial_q$, define
$B_L=R\mathcal D+L(\mathcal D R)$, where the last term denotes
multiplication. The composition identity
$B_1\cdots B_j=\mathcal D^jR^j$ follows by induction:

$$
 R^j\bigl(R\mathcal D+(j+1)(\mathcal D R)\bigr)
 =\mathcal D\circ R^{j+1}.
$$

This identity does not divide by $R$ and remains valid at its zeros.
Acting on frequency three and extracting frequency one makes the
derivative factor equal to one. The limiting real coefficient is thus

$$
 (R^4)_{-2}
 =\frac{35}{8}\frac74=\frac{245}{32}.
$$

The two factors have frequencies in $7\mathbb Z$ and $[-4,4]$,
respectively; only the zero frequency of the former can contribute to
frequency $-2$. Replacing each real factor $b$ by
$(N/\pi)\sin(\pi b/N)$, with $|b|\le35$, and telescoping four
factors gives the stated error $<10^{13}/N^2$. Thus $C_N>7$ for
$N\ge10^7$.

The exact phase calculation is
$\overline\gamma^{\,4}=(-527+336i)/10^{12}$. It gives a positive
imaginary fourth coefficient, with limit
$343\pi^8/12500000000$. The conservative bound in the source exceeds
$10^{-4}t^4$ before the remainder; since $t<10^{-80}$, the
remainder is much smaller than half that lower bound. Finally
$t=\tau/(2\pi)>\tau/8$ and
$(20000\,8^4)^{-1}>10^{-8}$, proving the constant $10^{-328}$.

The auxiliary script `audit_gauge_coefficient_check.py` was executed by the
reviewer and returned its exact-coefficient and rational-inequality checks
successfully. It supports these calculations; the preceding symbolic
derivation is the proof for arbitrary $N$.

## 4. Gauge invariance of the discriminator

For diagonal unitary $W$, set
$F(U)=N^{-1}\operatorname{Tr}(W^*UWU^*)$. Expanding entries gives

$$
 F(U)=N^{-1}\sum_{x,y}\overline{W_x}W_y|U_{xy}|^2.
$$

For $V=\zeta DU^TD^*$, its entry moduli transpose those of $U$.
Exchanging $x,y$ proves $F(V)=\overline{F(U)}$. Telescoping the
two unitary factors and applying Hilbert--Schmidt Cauchy--Schwarz gives
$|F(U)-F(V)|\le2N^{-1/2}\|U-V\|_{\rm HS}$. Hence the distance is
at least $|\operatorname{Im}F(U)|$.

To check the final conjugation orientation, conjugate
$D\bar U D^*-\eta U^*$, then multiply on the left by $D$ and
on the right by $D^*$. The result is
$U-\bar\eta DU^TD^*$. These operations preserve the required norm,
so the discriminator applies exactly to the claimed difference.

## 5. What the proof leaves open

The lower bound is effective at a very small fixed scale. A separate
oscillatory-kernel argument proves $\|Q_N\|\to0$ and gives a stronger
asymptotic obstruction for this same gauge class, without an explicit
onset dimension; this does not alter the validity or the effective scope
of the present estimate. Neither result controls the nonreversed
cross terms in $|\operatorname{Tr}U_N^n|^2$ at $n\asymp N$.
