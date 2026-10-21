> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round12_2026_10_21/r12_signed_trace_kick_audit.md`. Embedded SHA256: `febe87b367a5078bf87469c2096eac1ed1561d0ced90197dea29f2bb9b7c2458`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: the uniform physical-kick trace theorem

## 0. Frozen object and verdict

Audited raw:
`research_round12_2026_10_21/r12_countersequence_kick_recurrence.md`.
Frozen SHA-256:
`7bb8b677cdee6f7a0a94f1d20833aec3069200056de5d6c587c365bbb89e8e1e`.

Sections 0--7 of this frozen version were read directly. The preceding
version, SHA-256
`e315d1d3e72d05e4ccc5e09fd659513e5dec19c9e558da14bab2e30d4a9199e7`,
had been read in full; the update changes attribution/provenance, not
the audited mathematics. Both associated exact-check files were read.

**Verdict:** Theorem 1 and its stated consequences in Sections 1--7
pass this independent audit. In particular the argument proves

$$
 \left|N^{-1}\operatorname{Tr}e^{itNA_N}\right|
 \le C_T(N|t|)^{-c_T},\qquad
 0<|t|\le T,\quad N|t|\ge1,
$$

with positive finite constants depending on the fixed finite $T$,
uniformly in all odd dimensions. The proof does not assume a prime
modulus, Egorov for a varying cutoff, or a parameter-independent
bound after silently discarding a factor $t$. Its original exponent
$c_T=\beta_T/(12+\beta_T)>0$ is valid as written.

The conclusion concerns the one-generator group $e^{itNA_N}$.
No conclusion about the Heisenberg-time traces of
$(e^{i10^{-80}NA_N}M_N)^m$ follows from this audit. Section 8's
historical theorems were not independently re-audited here.

## 1. Symbol, sign, and the exact shear

For integer labels, direct multiplication of the original Weyl
operators gives

$$
 W(v)W(w)=e^{\pi i\Omega(v,w)/N}W(v+w),
 \quad W(k,l)=(-1)^{kl}T_N(l,k),
 \quad\Omega(v,w)=lk'-kl'.
$$

The parity factors cancel because
$kl+k'l'+\Omega(v,w)-(k+k')(l+l')=-2kl'$ is even.
This is valid also when labels alias modulo a composite odd $N$.
The $l=\pm1$ Fourier coefficients therefore require the shift
$r(q+1/2)$ in the ordinary-half symbol. The audited symbol is the
correct symbol of the prescribed $A_N$.

At $q=0$, the factors in $r$ and in $r(q+1/2)$ give
$r''(0)=392\pi^2$ and $[r(q+1/2)]''_{q=0}=8\pi^2$.
The term $r(q)\sin(2\pi q)$ vanishes through second order there.
It follows directly that

$$
 a(0,p)=9/10,\quad da(0,p)=0,\quad
 a_{pp}=a_{pq}=0,
$$
$$
 a_{qq}(0,p)
 =-\frac{2\pi^2}{25}[1960-\cos(2\pi p-\alpha_0)]<0.
$$

For $X=(a_p,-a_q)/(2\pi)$, each $(0,p)$ is stationary.
Its derivative matrix has only the lower-left entry
$-a_{qq}/(2\pi)$; it is nonzero and has square zero. The
variational equation thus gives $D\kappa_t=I+tDX$ there at every
finite real time, not just to first order. Consequently
$\kappa_t\ne\operatorname{Id}$ for every $t\ne0$.

This check verifies the mathematics. It makes no independent novelty
claim about the shear; the frozen author's version explicitly
attributes the older occurrence.

## 2. Uniform Egorov retains exactly the factor needed at zero time

For Fourier modes,

$$
 \{e_v,e_w\}=4\pi^2\Omega(v,w)e_{v+w},
$$

whereas the coefficient in $iN[Q_N(a),Q_N(b)]$ is
$-2N\sin(\pi\Omega/N)$. Therefore the linear terms cancel in

$$
 iN[A_N,Q_N(b)]+\frac1{2\pi}Q_N(\{a,b\}),
$$

and the remainder is bounded by
$C_aN^{-2}|b|_3$. The bound
$|\sin x-x|\le|x|^3/6$ is global, so there is no restriction
$|\Omega|\ll N$.

The transport equation is
$\partial_t(b\circ\kappa_t)=-\{a,b\circ\kappa_t\}/(2\pi)$,
with the same sign. On a fixed interval $[-T,T]$, all fixed
derivatives of $b\circ\kappa_t$ are uniformly bounded. Duhamel
integration of the preceding defect, using a unitary conjugation,
gives the actual uniform estimate

$$
 \|E_N(t)Q_N(b)E_N(t)^*-Q_N(b\circ\kappa_t)\|
 \le C_{b,T}|t|N^{-2}.                                  \tag{2.1}
$$

The author uses (2.1) only with the two fixed characters
$b_1=e^{2\pi iq}$ and $b_2=e^{2\pi ip}$. The cutoff depending
on $N,t,\delta$ is never inserted into this Egorov estimate.
Thus no unproved uniformity in a growing symbol has entered.

## 3. The finite-jet argument is spatial and is uniform in the parameter

The normalized differences

$$
 d_j(t,z)=[b_j(z)-b_j(\kappa_tz)]/t
$$

extend analytically to $t=0$, where they equal $-Xb_j$.
Thus $v_t=|d_1|^2+|d_2|^2$ is jointly real analytic. For each
fixed $t$, it is not identically zero: for $t\ne0$, otherwise
both characters would imply $\kappa_t=I$; for $t=0$, otherwise
the vector field would vanish identically.

At any zero $(t,z)$, not all **spatial** derivatives of $v_t$
can vanish. If they did, the convergent Taylor expansion would vanish
near $z$, and the identity property along overlapping analytic
charts on the connected torus would make $v_t$ identically zero.
A nonzero homogeneous derivative has a direction on which it is
nonzero. Continuity supplies a product of a time interval and a
rotated spatial rectangle on which this particular directional
derivative has modulus bounded below.

A finite collection of such products covers the compact zero set in
$[-T,T]\times\mathbb T^2$. On the compact complement their union,
$v$ has a positive lower bound. These facts give a uniform finite
maximum order $r_T$, a positive lower derivative bound in each
rectangle, and a common sufficiently small sublevel threshold.

For completeness, the one-dimensional estimate used on each parallel
slice is valid without an assumption about the number of components
of a sublevel set. If $|F^{(j)}|\ge c$ and
$E=\{|F|\le\delta\}$ has measure $L>0$, choose $j+1$
quantiles of its measure. Approximating by points of $E$, consecutive
nodes can be separated by a fixed positive multiple of $L/(j+1)$.
Their divided difference is bounded by $C_j\delta/L^j$, while
the repeated mean-value theorem identifies it with
$F^{(j)}(\xi)/j!$. Hence
$L\le C_j(\delta/c)^{1/j}$. Fubini and the finite covering give

$$
 \sup_{|t|\le T}\operatorname{vol}\{v_t\le\delta\}
       \le C_T\delta^{1/r_T}.
$$

No derivative in the time variable was substituted for the required
spatial derivative. This is the key point in the claimed uniformity.

## 4. Cyclicity and the cutoff losses

Put $F=E_N(t)$, $B=Q_N(b_j)$,
$C=Q_N(b_j\circ\kappa_t)$, and $R=FBF^*-C$.
Then

$$
 \operatorname{tr}_N Q_N(u)(B-C)F
 =\operatorname{tr}_N[Q_N(u),B]F
     +\operatorname{tr}_NQ_N(u)RF.                      \tag{4.1}
$$

Indeed, the term containing $FBF^*F$ is
$\operatorname{tr}_NQ_N(u)FB$, which cyclicity changes to
$\operatorname{tr}_NBQ_N(u)F$. This checks both the sign and
the order of the commutator in the author's equation (6.2).

After replacing the product by its Weyl quantization and dividing by
$t$, the commutator and product errors are
$O((N|t|)^{-1}|u|_1)$. The Egorov error in (2.1) becomes only
$O(N^{-2}|u|_0)$, which is absorbed in the same bound because
$|t|\le T$ and $N\ge3$. This proves the required estimate
with a variable cutoff $u$, without an Egorov claim for that cutoff.

For $\chi_\delta=\chi(v_t/\delta)$ and
$u_j=(1-\chi_\delta)\overline{d_j}/v_t$, the functions vanish
smoothly near $v_t=0$. On $v_t\ge\delta$, derivatives of
$v_t^{-1}$ of order $h$ cost at most $C_T\delta^{-h-1}$.
Splitting at most five derivatives among the three factors in
$u_j$ therefore costs at most $\delta^{-6}$. Derivatives of
$\chi_\delta$ through order six cost at most $\delta^{-6}$.
The Fourier estimates
$|u|_1\le C\|u\|_{C^5}$ and
$|\chi|_2\le C\|\chi\|_{C^6}$ on the two-dimensional torus
follow by coordinate integration by parts and a convergent lattice
sum. Thus the author's full $\delta^{-6}$ budget is sufficient.

The Hilbert--Schmidt alias estimate is also valid for all odd moduli.
In its square, the unequal Fourier labels can survive the trace only
if they differ by an element of $N\mathbb Z^2$. At least one label
then has size at least $N/2$, giving a cross-term bound
$8N^{-2}|b|_2^2$. Taking square roots gives

$$
 \|Q_N(b)\|_{\rm HS}/\sqrt N
 \le\|b\|_2+C N^{-1}|b|_2.
$$

Combining the sublevel mass and the cutoff losses proves

$$
 |\operatorname{tr}_N E_N(t)|
 \le C_T\bigl[\delta^{\beta_T/2}
                 +(N|t|)^{-1}\delta^{-6}\bigr].
$$

The choice $\delta=(N|t|)^{-2/(12+\beta_T)}$ gives exactly the
stated exponent $\beta_T/(12+\beta_T)$. The bounded remaining
range of $N|t|\ge1$ is covered by enlarging the finite constant.

## 5. Spectral consequences and the scope boundary

For each fixed nonzero integer $m$,
$E_N(t_N)^m=E_N(mt_N)$. The theorem on the fixed larger interval
$[-|m|T,|m|T]$ makes every nonzero fixed Fourier coefficient of
the empirical spectral measure vanish when $N|t_N|\to\infty$.
Uniform approximation by Fejer means proves convergence to Haar
measure. The argument is global spectral equidistribution of the
kick, not local spectral universality.

The identity
$\inf_{|z|=1}N^{-1}\|E-zI\|_{\rm HS}^2
=2-2|\operatorname{tr}_NE|$ gives the Hilbert--Schmidt limit.
Haar convergence gives an eigenvalue in every member of any finite
fixed arc cover for all large $N$. Applying this cover near the
antipode of an arbitrary $z$ makes the operator-norm lower bound
uniform in $z$, and its infimum tends to two. Right multiplication
by $M_N^*$ gives the stated distance between $U_N$ and
$zM_N$.

This excludes asymptotically scalar **matrix** kicks. It does not
exclude equal or nearby unordered spectra under a further arbitrary
unitary conjugation. Most importantly, no step in the proof estimates
the noncommuting sequence of conjugated kicks in $U_N^m$ for
$m\asymp N$; the original pair estimate remains unproved.

## 6. Computation and read scope

The author's exact rational script and its JSON were read in full.
Their scalar identities were also checked directly from the displayed
symbol in Section 1 of this audit. The audit does not infer an
asymptotic statement from these finite computations.

| File | SHA-256 |
|---|---|
| Audited frozen raw | `7bb8b677cdee6f7a0a94f1d20833aec3069200056de5d6c587c365bbb89e8e1e` |
| `r12_countersequence_exact_check.py` | `1b55b94e3ccad1b4494516dc1db012402f82216eca19739222b4517b6bd20268` |
| `r12_countersequence_exact_check.json` | `5951bddcd7b82b61ba509ca6cba116fe3a977e55b78be1386acbbd89e0cbc6cc` |

The proof audited here is self-contained in the frozen author's
Sections 2--7. No external universality theorem and no uninspected
historical input is used to validate Theorem 1.
