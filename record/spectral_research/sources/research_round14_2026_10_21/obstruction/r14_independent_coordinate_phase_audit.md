> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round14_2026_10_21/obstruction/r14_independent_coordinate_phase_audit.md`. Embedded SHA256: `04389d7783357bb74d6d7db1cd4904238309b63c6a54b1e5affbd9358c7f37fd`.
> [Thematic guide](../../../../../mathematics/spectral_research/topics/classical_trace.md).

# Independent audit of the original coordinate-phase bridge test

Date: 21 October 2026. Auditor: /root/r14_original_obstruction.

## 1. Exact input and verdict

The audited source is
research_round14_2026_10_21/structural/r14_original_coordinate_phase_bridge_test.md,
SHA-256
7b6657c8e1ca2ee91391509c2c97b9054715681a0afa2cedff94f8dd4c4ecc3f,
24,172 bytes. The entire file was read directly at this hash.
The source was not modified.

**Theorem A and Corollary B pass this independent mathematical audit.**
The conclusion proved for the original prescribed family is
$$
\mathcal D_N:=\sum_x|U_N(x,x)|^2
\longrightarrow\int_0^1 k_{t_*}(q,q)\,dq,\qquad
|k_{t_*}-1|\le10^{44}\tau^4,
\quad t_*=\tau/(2\pi),\quad \tau=10^{-80},
$$
and
$$
\liminf_{N\ {\rm odd}}
\bigl(|\operatorname{Tr}U_N|^2-\mathcal D_N\bigr)\ge200\tau.
$$
The proof handles all odd dimensions, exact modular phases, wrapped
coordinate shifts, and all Poisson aliases. The trace-like diagonal
sum uses an adequate Hilbert--Schmidt error; it is not deduced from
an inadequate operator-norm convergence statement.

This is a nonzero discrepancy at one unnormalized time. It does not
establish or refute the original microscopic $H_2$, the full
$H_{\rm diag}$, or the weaker weighted ensemble bridge.
The source states that limitation correctly.

The following sections give the independent checks and their proofs.

## 2. Four-sheet Gauss normalization: exact arithmetic

Write $d=x-3y$, $Q_{xy}=3x^2-2xy+3y^2$, and
$\zeta_8=e^{2\pi i/8}$. The sum remaining after the ordinary
quadratic factor is removed is
$$
G_{N,d}=\sum_{m=0}^3\zeta_8^{\,2dm-3Nm^2}.
$$
The terms with $m=0,2$ sum to
$$
1+(-1)^{d-3N}=1-(-1)^d.
$$
The terms with $m=1,3$ sum to
$$
e^{-3\pi iN/4}(i^d+i^{3d})
=e^{-3\pi iN/4}i^d(1+(-1)^d).
$$
Here the replacement of $27N/4$ by $3N/4$ changes the angle by
$6\pi N$, an integer multiple of $2\pi$. Thus
$$
G_{N,d}=
\begin{cases}
2e^{-3\pi iN/4}i^d,&d\ \text{even},\\
2,&d\ \text{odd}.
\end{cases}
\tag{2.1}
$$

This equals
$$
2e^{-3\pi iN/4}\zeta_8^{\,3Nd^2}
\tag{2.2}
$$
in both cases. For odd $d$, $d^2\equiv1\pmod8$.
For $d=2v$, the last factor is
$(-1)^{3Nv^2}=(-1)^v=i^d$, because $N$ is odd.

The identity
$$
3(x-3y)^2-Q_{xy}=-16xy+24y^2\in8\mathbb Z
$$
converts (2.2) to the phase $\zeta_8^{NQ_{xy}}$.
If the modular inverse of eight is represented by $(1+kN)/8$,
then $k\equiv-N\pmod8$. Hence
$$
e_N(-8^{-1}Q_{xy})
=e^{-2\pi iQ_{xy}/(8N)}e^{2\pi iNQ_{xy}/8}.
$$
Including the scalar $e^{3\pi iN/4}/(2\sqrt N)$ therefore yields
the exact matrix $M_N$. The relative sheet phases and the factor
two in the denominator are both correct.

The companion exact check reduces powers of $\zeta_8$ in
$\mathbb Z[z]/(z^4+1)$ for all odd residues of $N$ modulo eight
and all residues of $d$ modulo eight. This is an arithmetic
bookkeeping check of (2.1)--(2.2), not a numerical approximation
to the tiny kick.

## 3. Grid wraps and the propagation of the deck identities

The two initial identities can also be checked by subtracting the
quadratic polynomials:
$$
\begin{split}
F_0(Q,s+4)-F_0(Q,s)&=Q-3s-6,\\
F_0(Q+1,s)-F_0(Q,s-3)&=-2s+3.
\end{split}
\tag{3.1}
$$
They persist under
$F_t=a(Q,F_Q)$. In the first identity the derivative in $Q$
changes by the integer one, and $a$ is periodic in momentum.
In the second identity the coordinate changes by the integer one,
and $a$ is periodic in that coordinate. In each case subtracting
the displayed affine term gives the same Hamilton--Jacobi initial
value problem, so characteristic uniqueness proves the identity
at all the times used.

The mixed derivatives of the affine terms vanish. Therefore
$B=2\sqrt{F_{Qs}}$ has the same sheet permutations, with no sign
ambiguity: its analytic root stays near one after multiplication
by two, and the real root is positive.

At $Q=x/N,s=y/N$, all the affine changes in (3.1), after
multiplication by $N$, are integers. A change $s\mapsto s+1$
merely permutes the four sheets, using the first identity once for
the sheet crossing the endpoint. A change $Q\mapsto Q+1$
permutes them by $m\mapsto m-3$, with the second identity and,
as needed, the first. Thus the four-sheet sum is exactly periodic
on the finite grid.

This is precisely what is required when the finite Weyl shift
$x\mapsto x+l$ wraps through $0$ or $N-1$. One first evaluates
the smooth lifted expression at $Q+l/N$; its value equals the
value at the reduced grid representative. The Taylor expansion
can use the lifted expression on its fixed enlarged real region.
It does not require a discontinuous choice of representative.

## 4. Subprincipal sign and the Duhamel norm

For one Fourier label set
$c=2\pi l$, $E=e^{2\pi i(kQ+lF_Q)}$.
After extracting $e^{iF/h}$, exact finite-shift expansion gives
$$
\begin{split}
&e^{2\pi ik(Q+\pi hl)}
e^{i(F(Q+ch)-F(Q))/h}B(Q+ch)\\
&\qquad=
E\left[
B+h\{2\pi l B_Q+
2\pi^2i(kl+l^2F_{QQ})B\}+O(h^2)
\right].
\end{split}
\tag{4.1}
$$
The finite Fourier sum converts $2\pi l$ into $-ia_p$;
it converts $2\pi^2i(kl+l^2F_{QQ})$ into
$-i(a_{Qp}+a_{pp}F_{QQ})/2$. Therefore the sign and factor in
the source are correct:
$$
A_h(Be^{iF/h})
=e^{iF/h}\left[
a(Q,F_Q)B
-ih\left\{a_pB_Q+
\tfrac12(a_{Qp}+a_{pp}F_{QQ})B\right\}
+O(h^2)
\right].
\tag{4.2}
$$
The momentum $p_0=-3Q/4+s/4$, the corrected mixed coefficient
$r(Q+1/2)$, and the positive evolution $+iA_h/h$ are used
consistently.

With $J=F_{Qs}$, direct differentiation gives
$$
J_t=a_pJ_Q+(a_{Qp}+a_{pp}F_{QQ})J.
$$
Thus $B=2\sqrt J$ solves exactly the first transport equation,
and multiplication of the $O(h^2)$ term in (4.2) by $i/h$
leaves $O(h)$. Including the four-sheet normalization gives a
residual matrix $R_N(t)$ with
$$
\sup_{x,y}|R_N(t;x,y)|\le C h/\sqrt N,\qquad0\le t\le t_*.
\tag{4.3}
$$
The constants may depend on the fixed phase and fixed time but do
not depend on $N$. Finite Fourier support and the strip derivative
bounds give the uniform Taylor remainder. Real times make each
phase factor unimodular.

Consequently each residual column has norm at most $Ch$.
For the exact finite evolution
$U_N(t)=e^{itA_N/h}M_N$, Duhamel and its unitarity give
$$
\|(U_N(t_*)-V_N(t_*))e_y\|_2\le Ct_*h=O(N^{-1}).
$$
Summing the squared column bounds yields
$$
\|U_N-V_N\|_{\rm HS}=O(N^{-1/2}).
\tag{4.4}
$$
This is sufficiently strong for the specific observable.
There are four bounded leading amplitudes, so
$\|\operatorname{diag}V_N\|_2\le C'$. Diagonal extraction is a
contraction from matrix Hilbert--Schmidt norm to vector Euclidean
norm, and hence
$$
\left|\|\operatorname{diag}U_N\|_2^2
-\|\operatorname{diag}V_N\|_2^2\right|
\le O(N^{-1/2})(2C'+O(N^{-1/2}))=o(1).
\tag{4.5}
$$
There is no illicit factor $\sqrt N$ left in (4.5).
In contrast, (4.4) would only give an $O(1)$ bound for
$|\operatorname{Tr}(U_N-V_N)|$; the source does not use that
invalid stronger conclusion.

## 5. Equal-sheet cancellation and the fourth-order remainder

After the change $p=(s-3Q)/4$, differentiation in $Q$ at fixed
$s$ is $D=\partial_Q-\tfrac34\partial_p$. The exact equation
for the correction is
$$
\partial_t\mathcal G=a(Q,p+D\mathcal G).
$$
If $\mathcal G=\sum_{n\ge1}t^n\mathcal G_n$, then
$\mathcal G_n$ has momentum Fourier degree at most $n$.
At order $t^{n-1}$, each nonlinear term is
$$
\frac{\partial_p^r a}{r!}
\prod_{\nu=1}^rD\mathcal G_{j_\nu},
\qquad \sum_\nu j_\nu=n-1.
$$
The degree is at most $1+\sum_\nu j_\nu=n$.
The derivative $D$ changes coefficients but does not change Fourier
frequencies, so this induction has no missing shift.

The four translates $p+m/4$ annihilate every Fourier frequency
not divisible by four. At $n=1,2,3$, only frequency zero can
remain. The mixed derivative $\partial_Q\partial_s$ then
annihilates that remainder. Thus the first three Taylor coefficients
of
$$
k_t-1=\sum_{m=0}^3G_{Qs}(t,Q,s+m)
$$
vanish as claimed.

For completeness, the complex-time Cauchy step is legitimate.
On a complex disk of time radius $T=10^{-12}$, the bounded
analytic characteristic field has displacement at most $300T$.
The endpoint equation remains a contraction with derivative defect
below $2.1\cdot10^{-8}$, on the stated invariant strip.
Picard integrals along the segment $[0,t]$ prove holomorphic
dependence on time. Therefore the phase bound
$\|G(t)\|_{.003}\le10|t|$ implies
$\|G_n\|_{.003}\le10T^{1-n}$.

For $|t|\le T/2$, summing the geometric tail gives
$$
\left\|G-\sum_{n=1}^3t^nG_n\right\|_{.003}
\le20|t|^4/T^3=2\cdot10^{37}|t|^4.
$$
A mixed derivative across the strip gap $0.001$ costs at most
$10^6$, and four translates cost four. This gives exactly
$$
\|k_t-1\|_\infty\le8\cdot10^{43}|t|^4
\le10^{44}\tau^4\quad(t=t_*).
\tag{5.1}
$$
The estimate does not truncate the definition of $U_N$.

## 6. Unequal sheets and every discrete alias

On the diagonal, direct expansion gives
$$
F_0(q,q+m)-F_0(q,q+n)
=-\frac{m-n}{2}q-\frac{3(m^2-n^2)}8.
\tag{6.1}
$$
The perturbation $d_{mn}(q)$ has derivative bounded by
$4\cdot10^4t_*<1/8$.

For odd $m-n$, the slope in (6.1) is a half integer, at distance
at least $3/8$ from every integer after perturbation.
Every Poisson alias is nonstationary, including the nearest ones.

For even nonzero $m-n$, it equals $2$ or $-2$.
The linear phase is then an integer multiple of $q$, and on
$q=x/N$ its exponential is exactly one. It must be removed before
applying the oscillatory argument. The remaining zero alias can
have stationary points; the source addresses it explicitly.

At $Q=0$, both $R(0)$ and its first derivative vanish, and
$V'(0)=0$. Therefore the characteristic is an equilibrium for
every momentum and $G(t,0,m)=9t/10$. Hence $d_{mn}(0)=0$.
At $q=1/4$, $R(q)=1$ and $p_0=m/4-1/8$. For
$(m,n)=(0,2)$ and $(1,3)$, the first time coefficient of the
difference is respectively
$$
\frac2{100}\left(-\frac7{5\sqrt2}\right),\qquad
\frac2{100}\left(\frac1{5\sqrt2}\right).
$$
Each absolute value is at least $1/(250\sqrt2)>1/400$.
The difference of the two Taylor remainders is at most
$4\cdot10^{13}t_*^2<t_*/800$. Thus
$$
|d_{m,m+2}(1/4)|\ge t_*/800>0.
\tag{6.2}
$$
The phases $d_{mn}$ are nonconstant analytic functions for the
actual positive fixed parameter. Reversing a pair changes only
its sign.

Here is the full alias conclusion in explicit order of limits.
Insert an endpoint cutoff with omitted interval length $O(\delta)$.
The discarded grid sum is $O(\delta)+O(N^{-1})$.
For the compactly supported amplitude, Poisson summation gives
$$
\sum_{j\in\mathbb Z}
\int A_\delta(q)e^{2\pi iN(d(q)-jq)}\,dq.
$$
For $j\ne0$, repeated integration by parts gives
$C_{M,\delta}N^{-M}(1+|j|)^{-M}$, a summable majorant
when $M\ge2$. For $j=0$, nonconstant analyticity implies that
the zeros of $d'$ on the compact support are finite.
Removing neighborhoods of arbitrarily small total length and
integrating by parts on the remainder proves its limit is zero.
First send $N\to\infty$, then shrink those neighborhoods and the
endpoint cutoff. All constants are allowed to depend on the fixed
$t_*$.

In the odd-difference case the same argument has no stationary
alias. All twelve ordered unequal-sheet terms tend to zero.
Combining this with the equal-sheet Riemann sum and (4.5) proves
Theorem A through all odd $N$.

## 7. The original trace input and Corollary B

The raw Round 13 file
research_round13_2026_10_21/orbit_correlations/protected_actions_and_one_step_trace.md,
SHA-256
6bbde35d4fb3873976d6182b3fb6d9cc969349a3a6ce78e7b9dc48cf480c9fe6,
was read here in §§1--6. Its one-step proof only uses a finite
number of nondegenerate critical points. Its Abel stationary-phase
lemma supplies an $O(h)$ error after the kernel prefactor.
The old exact sector identity and amplitude input were also
read directly in this audit branch; their hashes and proof scopes
are recorded in the companion spectral-orbit report.

The four Hessians are
$$
a_{qq}(z_{00},z_{01},z_{10},z_{11})
=\frac{\pi^2}{125}(-19606,-19594,24306,24894).
$$
The linearized kick is an exact shear at each protected fixed
point, giving derivative traces
$$
6+39212v,\quad6+39188v,\quad6-48612v,\quad6-49788v,
\qquad v=\pi\tau/125.
$$
Their exact action factors have relative signs $(+,-,+,+)$.
The mean-value bound for the first difference is $3v/2$;
convexity bounds the second sum below by $1+6150v$.
Thus the precise consequence used in the structural report is
$$
\liminf |\operatorname{Tr}U_N|
\ge1+c\tau,\qquad c=12297\pi/250.
$$
Since Theorem A gives
$\limsup\mathcal D_N\le1+10^{44}\tau^4$,
$$
\liminf(|\operatorname{Tr}U_N|^2-\mathcal D_N)
\ge2c\tau+c^2\tau^2-10^{44}\tau^4\ge200\tau.
$$
Indeed $2c>295$ already from $\pi>3$, and
$10^{44}\tau^3=10^{-196}$. This proves the stated Corollary B.

## 8. Scope of what survives this audit

The independent-coordinate-phase integral eliminates off-diagonal
pairs of coordinate visits. A common spectral shift eliminates only
unequal total degree. Their one-step second moments differ by the
strict positive amount just proved for the original family.

After the microscopic normalization, that fixed-time contribution
is $O(N^{-2})$. It does not disprove
$$
\frac1{N^2}\sum_{1\le m<2N}w(m/N)
\left[
|\operatorname{Tr}U_N^m|^2
-\int_{\mathbb T^N}|\operatorname{Tr}(D_\varphi U_N)^m|^2d\varphi
\right]\longrightarrow0.
$$
The source leaves this weighted bridge unproved, and separately leaves
the actual $H_2$ sum with CUE benchmark $\min(m,N)$ unproved.
There is no hidden transfer of an ensemble theorem to the original
matrices in Theorem A or Corollary B.

No correction to the mathematical source was necessary at the audited
hash. The result is a valid original-family calculation and a valid
obstruction to a pointwise phase-ensemble replacement; it is not a
resolution of the full requested spectral-statistical problem.

