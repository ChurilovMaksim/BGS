# One-step transport between exact torsion sectors

**Registry:** BGS-TRACE-358.

**Scope.** This archive continuation concerns the original deterministic
operator $U_N=K_NM_N$, $K_N=\exp(i\tau N A_N)$, with $\tau=10^{-80}$ fixed
and odd $N$. The parameter in $\exp(itA_N)$ is $t=\tau N$, not $\tau$.
The [full archived proof](BGS_Torsion_Transport.tex) is preserved as received.
See the [model and Weyl conventions](../../fixed_model_symmetry_theorem.md),
the [claim registry](../../../../record/claims.json) for maintained statuses,
and the [archive verification suite](../../../../computations/verification/bgs_f_november/)
for the scope of the finite checks. No Heisenberg-time spectral statement or
microscopic universality is implied.

## Statements

Let $L\ge3$ with $L^2\mid N$, write $d=N/L^2$, and set
$W_z=T_N((N/L)a,(N/L)b)$ for $z=(a,b)\in(\mathbb Z/L)^2$, using raw
modular Weyl operators. The product phases vanish identically on this group,
so the character projections are
$$
P_\chi=L^{-2}\sum_z \overline{\chi(z)}W_z,\qquad \operatorname{rank}P_\chi=d.
$$
Exact Egorov for $M_N$ permutes these projections. Uniformly in both
characters and in $3\le L\le N^{1/20000}$,
$$
\frac1d\operatorname{Tr}(P_\chi U_NP_\psi U_N^*)
   =L^{-2}\bigl(1+O_\tau(N^{-1/6000})\bigr).
$$
The same estimate holds with $U_N$ replaced by $K_N$. In the Weyl basis
normalized by $\operatorname{Tr}/N$, every matrix coefficient of
$\operatorname{Ad}_{U_N}T_N(a,b)$ is $O_\tau(N^{-9/64000})$ when the input
has centered $\max(|a|,|b|)\ge N^{99/100}$, with no condition on its output.

Separately, for **all** $L^2\mid N$, $L\ge3$, and every nonzero real
algebraic $t$, the map
$$
(I-P_\chi)\exp(itA_N)M_N\big|_{\operatorname{ran}P_\psi}
$$
is injective, as is the corresponding map with $M_N$ omitted. No lower
bound on its least singular value is claimed.

## Quantitative argument

Use ordinary midpoint quantization
$\operatorname{Op}_N(e^{2\pi i(kq+lp)})=(-1)^{kl}T_N(l,k)$.
Its real symbol $g$ for $A_N$ has the shifted hopping coefficient
$r(q+1/2)\cos(2\pi p-\alpha_0)/100$, not $r(q)$.
The support is contained in $[-9,9]\times[-1,1]$ and
$\widehat g(1,0)=1/20-i/200$, $\widehat g(0,1)=e^{-i\alpha_0}/200$.
Let $\varphi$ be its time-$\tau$ flow for
$Y=(-g_p,g_q)/(2\pi)$, the convention for conjugation by $K_N^*$.
The Weyl product estimate costs $O(N^{-1})$ at fixed smooth norms;
in the commutator the cubic sine remainder gives an $O(N^{-2})$
Egorov error with a $C^8$ symbol norm.

For Weyl translates with torus shifts $h,u$ let $V=W_hK_NW_uK_N^*$.
Average the conjugates of $V$ by all Weyl modes from $[-R,R]^2$.
This preserves the trace. After multiplying by $V^*$ the averaged symbol
is
$$
a_R(x)=D_R(x_1-G_1(x))D_R(x_2-G_2(x)),\quad
G=T_h\varphi T_u\varphi^{-1},
$$
where $D_R$ denotes the normalized Dirichlet kernel. The resulting bound is
$$
|\operatorname{Tr}V|/N
\le \|a_R\|_2+O_\tau(N^{-1/2}(1+R)^6+N^{-1}(1+R)^8).
$$
The key quantitative input concerns small nonzero $u$: changing variables
by $y=\varphi(x)$ gives the lifted displacement
$$
G(\varphi(x))-\varphi(x)
=h+u+\tau\big(Y(x+u)-Y(x)\big)+E(x+u)-E(x),\qquad
E=\varphi-\mathrm{id}-\tau Y .
$$
In the coordinate with the largest $|u_j|$, the nonzero unit Fourier
mode of $Y$ supplies a coefficient of size at least
$\tau |u|_\infty/50$ in a component of this displacement. A Lagrange
Fourier selector of order $20$ isolates it from the finite support and
kills the constant. Cauchy bounds in the complex strip control the selected
remainder by $10^{62}\tau^2|u|_\infty$. Thus at every point some positive-order
derivative, of order at most $20$, has magnitude at least $c\tau|u|_\infty$.
A finite-direction divided-difference bound gives sublevel measure at most
$C(\varepsilon/(\tau|u|_\infty))^{1/20}$ for distance $\varepsilon$ to an
integer in this component. Combined with the Dirichlet bound at
$\varepsilon=R^{-1/2}$, this yields
$$
\|a_R\|_2\le C(\tau|u|_\infty)^{-1/40}R^{-1/80}+CR^{-1/2}.
$$
For $R=\lfloor N^{1/32}\rfloor$, the normalized trace of $V$ is
$O_\tau(|u|_\infty^{-1/40}N^{-1/2560})$. On the torsion grid a nonzero
$u$ has $|u|_\infty\ge L^{-1}$. Expanding both $P_\chi$ and $P_\psi$
gives main term $L^{-4}$ for the trace normalized by $N$ and relative
error $O_\tau(L^{4+1/40}N^{-1/2560})$, bounded as stated. For the large
Weyl modes, use $|u|_\infty\gtrsim N^{-1/100}$ and
$1/2560-1/4000=9/64000$. These are asymptotic bounds at fixed $\tau$; a
numerical dimension at which the error is small is not established.

## Exact leakage and prior results

A character sector is supported on a single residue class modulo $L$.
The two Jacobi shifts land in distinct adjacent residue classes. The two
edges incident on any coordinate of the odd position grid cannot both
vanish: zeros are separated by $1/7$ at the accessible midpoint sites
and $N\ge9$. Thus $(I-P_\psi)A_NP_\psi$ is injective on the input sector.
If $\chi\ne\psi$, the leakage map is already injective at $t=0$.
In either case some full-column-rank minor is a nonzero analytic
exponential polynomial with algebraic coefficients and frequencies.
[Lindemann–Weierstrass, Theorem 3.2](https://arxiv.org/pdf/2306.14352v2)
preserves its nonvanishing at each nonzero algebraic $t$. This is the
same coefficient separation used in the repository's
[algebraic-time rank transfer](../../algebraic_time_rank_transfer.md).

The [canonical-oldspace proof](../../../spectral_research/proofs/research_round2_2026_10_20/arithmetic_oldspace_escape.md)
already proves exact escape and mean overlap for the trivial character.
The narrower comparison in the archived TeX is not a general novelty claim:
[fixed-divisor sector mixing](../../../spectral_research/proofs/research_round2_2026_10_20/root_quantitative_trace_and_sectors.md)
already handles every pair with a divisor-dependent power saving.
[Uniform logarithmic sector estimates](../../../spectral_research/proofs/research_round2_2026_10_20/arithmetic_iterated_uniform_all_old_logarithmic.md)
already cover divisors up to $N^{1/4096}$ on a logarithmic time window
starting at a fixed $r_0$, with absolute error and an uncomputed exponent.
The new quantitative scope here is the explicit **relative** error at one
step on the stated, more restrictive divisor range and the separate
large-input-label estimate. Exact injectivity generalizes canonical escape;
it is compatible with the [sevenfold compression norm tending to one](../../seven_oldspace_singular_spectrum.md).

## Why this does not decide the pair test

On the $L^2$-dimensional Hilbert–Schmidt space spanned by the torsion
operators, the normalized compressed trace of the pair resolvent is at
most $L^2/(Ns^2)$ for $s>0$. This vanishes in the range above; it leaves
the full complementary trace uncontrolled. More directly the unitary
$F_{L^2}\otimes I_d$, with normalized discrete Fourier transform
$F_{L^2}$, has exactly flat sector overlaps and zero traceless one-step
compression, but its fourth power is the identity. Its weighted pair
defect is of order $N$. This is a counterexample to transfer from
one-step sector data alone, not to BGS for the prescribed operator.
