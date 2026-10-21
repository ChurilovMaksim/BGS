> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/fermionic_root_trace_audit.md`. Embedded SHA256: `449aa3d72f26a6b3b195395f5ef714ecebcd3a42071718b569f8d7658c0712eb`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Audit of the quantitative trace lemma, followed by a denominator test

## Status and frozen inputs

The first part independently audits `root_quantitative_trace_and_sectors.md`.
The second part constructs one explicit **different** deterministic family to
test what its sector conclusion can imply. That family is a smooth quantum
conjugate of the bare cat map. It is not the matrix family in the question and
does not refute `H_diag` for the prescribed `U_N`.

| Read-only input | SHA-256 |
|---|---|
| `root_quantitative_trace_and_sectors.md` | `0a174f5de9d070c31311f4fdfd4ebc58b15df0b6bfd86baf5d6f169a99b2ef6a` |
| `arithmetic_oldspace_escape.md` | `596d44605310cc898fa75e23df4aa811189a1764fed21ce8b9f5d07ae734813a` |
| `../research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md` | `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b` |
| `../research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` |
| `fermionic_pseudoorbit_cutoff.md` | `03173e53d1a10e2c1afad517c48943a5330d43fc4059b80fc0e37d5b1598a9eb` |

## Part I. Independent audit

### 1. Quantization and aliases

**Pass.** The ordinary Weyl operators are defined for integer Fourier labels
before reduction. Direct coordinate multiplication gives

$$
W_N(v)W_N(w)=e^{\pi i\Omega(v,w)/N}W_N(v+w),
\quad\Omega((k,l),(k',l'))=lk'-kl'.
$$

The identity `W_N(k,l)=(-1)^(kl)T_N(l,k)` uses the integer representative
`(N+1)/2` of the modular inverse. It is valid for all integer labels, including
aliased ones.

For the Hilbert--Schmidt estimate, the normalized trace of
`W_N(v)^*W_N(w)` is zero unless `v-w` belongs to `N Z^2`. If `v!=w` in the
latter case, at least one index has norm at least `N/2`. Therefore the absolute
sum of off-diagonal alias terms is at most

$$
2|a|_0\sum_{|v|\ge N/2}|\widehat a(v)|
\le 8N^{-2}|a|_2^2.
$$

The diagonal terms sum exactly to the squared continuum `L^2` norm. Taking a
square root gives

$$
N^{-1/2}\|\operatorname{Op}_N(a)\|_{\rm HS}
\le\|a\|_{L^2}+\sqrt8N^{-1}|a|_2.
$$

The integration-by-parts bounds `|a|_1<=C||a||_(C^5)` and
`|a|_2<=C||a||_(C^6)` are more than sufficient in dimension two. Their weighted
Fourier majorants are summable, with constants independent of `N`. No alias
error has been dropped for a varying cutoff.

### 2. Analytic sublevel exponent

**Pass.** At any zero of a nonzero real analytic function on the connected
torus, some finite derivative is nonzero. A nonzero homogeneous derivative
tensor has a direction with a nonzero repeated directional derivative. On a
small rotated rectangle this derivative remains bounded away from zero.

On each parallel interval, the divided-difference argument is valid: if a
sublevel set has length `L>0`, its measure quantiles provide `j+1` points
separated by a fixed multiple of `L/(j+1)`. Their divided difference is
`O_j(epsilon/L^j)` and equals `f^(j)(xi)/j!` for a point in their convex hull.
This gives the claimed one-dimensional bound. The zero-measure case needs no
estimate. Integrating over the transverse coordinate and using a finite cover
of the compact zero set proves

$$
\operatorname{vol}\{v\le\epsilon\}\le C\epsilon^{1/r}
$$

with one finite integer `r`. The empty zero set is harmless: sufficiently small
sublevel sets are empty. The proof does not assert a uniform `r` for different
analytic maps.

### 3. There is no hidden uniform Egorov assumption

**Pass.** This is the important point of the trace argument. Put
`B_j=Op_N(b_j)`, `C_j=Op_N(b_j composed with kappa)`, and

$$
R_{j,N}=F_N B_jF_N^*-C_j,
\qquad\|R_{j,N}\|\le C_jN^{-1},
$$

where each `b_j` is one of the two fixed coordinate characters. For an
arbitrary varying smooth symbol `a`, cyclicity gives

$$
\frac1N\operatorname{Tr}\bigl(\operatorname{Op}(a)(B_j-C_j)F_N\bigr)
=\frac1N\operatorname{Tr}[\operatorname{Op}(a),B_j]F_N
+\frac1N\operatorname{Tr}\operatorname{Op}(a)R_{j,N}F_N.
$$

The product formula converts the left side to
`mu_N(a(b_j-b_j composed with kappa))` with error
`O(N^-1 |a|_1)`. On the right, the commutator costs `O(N^-1 |a|_1)`, and
the **fixed-symbol** Egorov remainder costs at most `C N^-1 |a|_0`.
Consequently

$$
|\mu_N(a g_j)|\le C N^{-1}|a|_1
$$

holds for varying `a` without ever applying Egorov to that varying symbol.

For `a_(j,delta)=(1-chi(v/delta)) conjugate(g_j)/v`, derivatives through order
five cost at most `C delta^-6`; the extension by zero is smooth because the
cutoff is identically one near `v=0`. Derivatives through order six of
`chi(v/delta)` cost at most `C delta^-6`. Thus both Fourier seminorm bounds
used in the proof have the stated power.

With `beta=1/r`, the audited estimates are exactly

$$
|\operatorname{Tr}F_N|/N
\le C\delta^{\beta/2}+CN^{-1}\delta^{-6}.
$$

Setting `delta=N^(-2/(12+beta))` balances the two terms. The exponent is

$$
\boxed{c=\frac{\beta}{12+\beta}=\frac1{12r+1}>0.}
$$

All cutoff and sublevel thresholds are satisfied for sufficiently large `N`.
No uniform long-time assertion is involved.

### 4. The companion fixed-time hypotheses

**Pass for the hypotheses used here.** I checked Sections 5, 7 and 8 of
`arithmetic_oldspace_escape.md`; its separate transcendence and exact-minor
theorems are not needed for this audit.

The commutator expansion uses `|sin t-t|<=|t|^3/6`, with a finite Fourier
Hamiltonian. The third weighted Fourier seminorm of a fixed transported
symbol is bounded on a fixed compact time interval. Duhamel therefore gives
the asserted `O_b(N^-2)` fixed-time Egorov error. Its sign agrees with
`X=(a_p partial_q-a_q partial_p)/(2 pi)` and the stated ordinary Weyl product.

The nonidentity argument for every nontrivial `(g,h)` also checks. Iterating
the lifted translation-conjugacy equation `d` times forces `h=-g` on the
torus. The relative flow comparison is essential for small translations and
is correctly proved: the finite Fourier support gives
`||D(X-X_h)||_infinity<=4000||X-X_h||_infinity`, and its integral equation
yields a remainder bounded by `10^5 t^2||X-X_h||_infinity`. At the fixed
`tau`, this excludes a translation symmetry of the time map unless it is a
symmetry of the vector field. The nonzero `(1,0)` and `(0,1)` coefficients
exclude the latter. This remains valid for every fixed odd denominator `d`.

### 5. All characters and the normalization

**Pass.** The operators `G_N(a,b)=T_N(dm a,dm b)` form an ordinary
representation because their **modular** Weyl cocycle is trivial:
`(dm)^2=N m`. This assertion concerns the modular `T_N`; it should not be
replaced by an ordinary-half phase calculation without the corresponding
parity factors.

Their character projectors have rank `N/d^2=m`. Expanding

$$
\|P_\chi E_NP_\psi\|_{\rm HS}^2
=\operatorname{Tr}(P_\psi E_N^*P_\chi E_N)
$$

gives coefficient `d^-4` times the finite group sum of word traces. Only the
identity pair contributes `N`; the rest are `O_d(N^(1-c_d))`. Dividing by
`m=N/d^2` gives `1/d^2+O_d(N^-c_d)` with the claimed normalization.

The exact cat Egorov map permutes these projectors; it need not fix each
individual character. Because the conclusion already holds for **every**
character pair, right multiplication by `M_N` gives the same conclusion for
`U_N`. The singular-value counting inequality then follows directly from the
nonnegative trace of `P_psi U_N^*P_chi U_NP_psi`.

**Audit conclusion:** the quantitative trace lemma and the all-character sector
theorem pass. Their scope is fixed `d`, fixed classical time and one-step
sector averages. Neither an exponent uniform in `d` nor a Heisenberg-time
spectral estimate is proved by this argument.

## Part II. A fixed analytic conjugacy tests the missing denominator step

### 6. One explicit family, with no auxiliary averaging

Set `kappa=tau=10^-80` and define, for every odd `N`,

$$
B_N=\operatorname{diag}_{x\in\mathbb Z/N\mathbb Z}
\exp[-i\kappa N\cos(2\pi x/N)],\qquad
\widetilde U_N=B_NM_NB_N^*.
\tag{T1}
$$

This is an explicit different deterministic family. The parameter is fixed;
there is no additional randomization and no `N`-dependent small parameter.

Its fixed classical map is

$$
H(q,p)=(q,p+\kappa\sin2\pi q),\qquad
\widetilde\Psi=H L H^{-1},\quad
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix}.
\tag{T2}
$$

This is real analytic, area preserving and Anosov. The last assertion follows
directly by transporting the two invariant lines of `L` by `DH`: boundedness
of `DH,DH^-1` converts the exact rates `lambda^(-n)` for `L` to the same rates
up to a fixed factor. The periodic multipliers are exactly `lambda^m` and
`lambda^-m`.

In coordinates, with `Q` denoting the first output coordinate,

$$
Q=3q-4p+4\kappa\sin2\pi q,
\qquad
P=-2q+3p-3\kappa\sin2\pi q+\kappa\sin2\pi Q.
\tag{T3}
$$

### 7. Direct Egorov check for this fixed analytic model

For an ordinary Weyl mode with labels `(k,l)`, conjugation by `B_N` multiplies
its midpoint coefficient by

$$
\exp[-2i\kappa N\sin(\pi l/N)\sin(2\pi(q+l/(2N)))].
$$

The corresponding coefficient of the quantization of the mode composed with
`H^-1` is

$$
\exp[-2\pi i\kappa l\sin(2\pi(q+l/(2N)))].
$$

The two factors differ in absolute value by at most

$$
2|\kappa|\,|N\sin(\pi l/N)-\pi l|
\le\frac{|\kappa|\pi^3|l|^3}{3N^2}.
$$

Summing the absolutely convergent Fourier series gives the explicit fixed-time
bound

$$
B_N\operatorname{Op}_N(b)B_N^*
=\operatorname{Op}_N(b\circ H^{-1})
+O\left(|\kappa|N^{-2}|b|_3\right).
\tag{T4}
$$

The inverse conjugation has the same estimate. The exact modular Egorov
identity for `M_N`, together with `L=I mod 2`, gives exact ordinary-Weyl
covariance with `L^-1`. Composing these three fixed maps therefore proves

$$
\widetilde U_N\operatorname{Op}_N(b)\widetilde U_N^*
=\operatorname{Op}_N(b\circ\widetilde\Psi^{-1})+O_b(N^{-2}).
\tag{T5}
$$

No unproved uniform Egorov theorem is needed.

### 8. All fixed odd arithmetic sectors mix in this model

First establish a stronger translation fact. Suppose a translation
`h=(h_q,h_p)` has the property that
`widetilde Psi(z+h)-widetilde Psi(z)` is constant as a torus map. Its continuous
lift difference is then constant as a real vector, up to one constant integer
vector. From the first equation in (T3),

$$
3h_q-4h_p+4\kappa
\bigl(\sin2\pi(q+h_q)-\sin2\pi q\bigr)
$$

must be independent of `q`. The sine difference has zero mean, so it must
vanish identically. Because `kappa!=0`, this forces `h_q` integral. The change
in `Q` is now `C=3h_q-4h_p`. The second equation in (T3), and the fact that
`Q` ranges through all real values when `p` varies, force `C` integral.
Hence `4h_p` is integral. If `h` has odd rational denominator `d`, both
coordinates of `h` are integral. Thus

$$
\widetilde\Psi\text{ sends no nontrivial odd rational translation
to a translation by conjugacy.}
\tag{T6}
$$

For `N=d^2m` and the same canonical sector projectors as in the audited root
note, the word `G_N(g) widetilde U_N^* G_N(h) widetilde U_N` has classical map

$$
\widetilde\Psi^{-1}\circ t_h\circ\widetilde\Psi\circ t_g.
$$

If it were the identity, `widetilde Psi` would conjugate the translation
`t_g` to `t_-h`, contradicting (T6) unless both are trivial. All nontrivial
words satisfy the audited analytic trace lemma by (T5). Repeating the finite
character expansion, for every fixed odd `d>=3`,

$$
\boxed{
\frac1m\|P_{\chi,N}\widetilde U_NP_{\psi,N}\|_{\rm HS}^2
=\frac1{d^2}+O_d(N^{-c_d})
}
\tag{T7}
$$

simultaneously for every pair of characters, along all odd `m` tending to
infinity. This is the same sector conclusion as for the original matrix, and
it occurs within a fixed analytic Anosov quantization.

### 9. The exponential trace bounds and hyperbolic orbit formula also survive

By exact unitary conjugacy, every trace and every characteristic coefficient
of `widetilde U_N` equals the corresponding one for `M_N`. Let

$$
S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
$$

The exact Weyl covariance gives

$$
|\operatorname{Tr}M_N^j|^2
=\#\ker(S^j-I\pmod N).
\tag{T8}
$$

For an invertible real integer matrix `A`, the map from its kernel modulo `N`
to `Z^2/AZ^2` that sends `x mod N` to `Ax/N mod AZ^2` is well defined and
injective. Injectivity follows from `Ax/N=Ay`, since then `A(x-Ny)=0`.
The latter quotient has order `|det A|`. In dimension two this last fact can
be checked by the Euclidean algorithm: an integral row operation of determinant
one sends the nonzero first column of `A` to `(g,0)`, where `g` is the positive
gcd of that column. The resulting matrix is `[[g,b],[0,d]]`. Reducing the second
coordinate modulo `|d|` and then the first modulo `g` gives exactly `g|d|`
distinct quotient representatives, which equals `|det A|`.
Applying this to `A=S^j-I` yields

$$
\boxed{
1\le|\operatorname{Tr}\widetilde U_N^j|^2
\le\lambda^j+\lambda^{-j}-2<\lambda^j.
}
\tag{T9}
$$

This holds for every odd `N` and every positive `j`. In particular, it is
stronger than the prior exponential trace bound used in the determinant
cutoff theorem.

The geometric relation is exact as well. Put

$$
G(q)=-\frac\kappa{2\pi}\cos2\pi q.
$$

The real plane generating function of (T1), with the already checked scalar
`zeta_N`, is

$$
F_0(Q,q)+G(Q)-G(q).
\tag{T10}
$$

In every lifted closed sector, the sum of the last two terms telescopes to
zero because `G` is periodic. This holds on the **entire** cyclic integration
domain, not just at a stationary point. The winding character and boundary
term are unchanged. Thus the exact orbit phases are those of the bare map
under the fixed bijection `H:Fix L^j -> Fix widetilde Psi^j`.

The bare cyclic phase is quadratic, so its Gaussian integral is exact. In the
normalization of the checked all-time input, its transverse trace is
`1/(1-rho^j)` with `rho=lambda^-1`. Therefore the leading orbit sum is

$$
\widetilde{\mathcal P}_{j,N}
=(1-\rho^j)\operatorname{Tr}\widetilde U_N^j,
\qquad
\widetilde E_{j,N}=\rho^j\operatorname{Tr}\widetilde U_N^j.
\tag{T11}
$$

In particular `|widetilde E_(j,N)|<=lambda^(-j/2)`, uniformly for all times.
The leading primitive amplitudes have squared modulus exactly
`lambda^(-d_p)`. The same-orbit trace diagonal is consequently
`j+O(j^2 lambda^(-j/2))`, by the fixed-point count and the bound on proper
periods. The complete fermionic and reciprocal coefficient diagonals have the
constants `7 sqrt(2)/16` and `1/sqrt(2)` from the earlier audited file.

For the corresponding leading dynamical determinant,

$$
\widetilde{\mathcal Z}_N(z)
=\frac{D_N^{\rm cat}(z)}{D_N^{\rm cat}(\rho z)}.
\tag{T12}
$$

This follows directly by summing (T11). In particular, the full post-`N`
pseudo-orbit cutoff and its signed different-subset cancellation remain
available. No orbit-phase averaging is involved.

### 10. An explicit infinite odd-dimensional short-period sequence

Write

$$
J=\begin{pmatrix}0&2\\1&0\end{pmatrix},\quad J^2=2I,\quad S=3I+2J,
$$

and define integers `t_r,N_r` by

$$
S^r=t_r I+2N_rJ,
\qquad
N_r=\frac{\lambda^r-\lambda^{-r}}{4\sqrt2}.
\tag{T13}
$$

The recurrence `N_(r+1)=6N_r-N_(r-1)`, with `N_0=0,N_1=1`, proves both
integrality and `N_r=r mod 2`. The determinant relation gives
`t_r^2-8N_r^2=1`. Thus, for odd `r`,

$$
S^{2r}=I\pmod{N_r}.
\tag{T14}
$$

Every Weyl matrix commutes with `M_(N_r)^(2r)` by exact covariance. Since the
Weyl matrices span all matrices, that power is scalar. Consequently

$$
|\operatorname{Tr}\widetilde U_{N_r}^{2r\ell}|=N_r
\quad(\ell\ge1).
\tag{T15}
$$

This subsequence can be chosen inside a nontrivial fixed arithmetic sector
tower. Indeed `S^3=99I+70J=I+21J mod 49`; raising to the seventh power gives
`S^21=I mod 49`. Hence `49|N_r` for every
`r=21(2j+1)`. Along this sequence `N_r` is odd, tends to infinity, and
`log N_r/r -> log lambda`. The quantitative mixing law (T7), for example with
the fixed value `d=7`, therefore holds on the very sequence with the short
quantum periods (T15).

### 11. The sector law does not give the pair statistic or a bounded local limit

Use the original fixed bump `b_*`; more generally, any nonzero allowed test
has `w(u)=|bhat(u)|^2` continuous with `w(0)>0`. Choose fixed `epsilon,c_w>0`
so that `w>=c_w` on `[0,epsilon]`. Its support is contained in a fixed compact
interval, so

$$
N^{-2}\sum_{j\ge1}w(j/N)\min(j,N)\le C_w.
$$

Using only the multiples in (T15) in the nonnegative quantum term, the exact
pair formula gives

$$
\boxed{
\Delta^{\widetilde U}_{2,N_r}(b_*)
\ge c_w\left\lfloor\frac{\epsilon N_r}{2r}\right\rfloor-C_w
\longrightarrow+\infty.
}
\tag{T16}
$$

This lower bound is of order `N_r/log N_r`. It concerns the different model
(T1), not the original kicked family.

There is also a bounded-observable failure. A unitary matrix whose `2r`-th
power is scalar has at most `2r` distinct eigenphases. For a nonnegative smooth
test `F` supported in `[-L,L]`, the probability over the uniformly translated
center that any of these phases contributes to this interval is at most
`4Lr/N_r`. Outside that event the Laplace observable equals one. Hence

$$
\mathbb E_\alpha e^{-\langle F,\Xi_{N_r,\alpha}^{\widetilde U}\rangle}
\longrightarrow1.
\tag{T17}
$$

Thus the local process tends to the empty measure on this subsequence, in
spite of its exact intensity-one identity before passage to the limit. The
Sine_2 Laplace functional is strictly below one for a nonzero nonnegative `F`:
its nonnegative linear statistic has positive finite expectation. This proves
a bounded-observable obstruction, independently of moment uniform
integrability.

### 12. Direct failure of the missing reciprocal norm bound

Fix `s>0`, set `R_N=e^{-s/N}`, and consider `N=N_r` as above. There is an
eigenphase with multiplicity at least `M>=N/(2r)`. On the angle interval of
length `2/N` centered at its reciprocal root,

$$
|1-R_Ne^{it}\lambda_0|\le(s+1)/N.
$$

All other factors in the unitary determinant have modulus at most two.
For `N>s+1`, which holds eventually on this subsequence, therefore

$$
\begin{split}
\int_0^{2\pi}|D_N^{\rm cat}(R_Ne^{it})|^{-2}\frac{dt}{2\pi}
&\ge\frac1{\pi N}
\left(\frac N{s+1}\right)^{2M}2^{-2(N-M)}\\
&\ge\frac1{\pi N}
\exp\left[\frac N r\log\frac N{s+1}-2N\log2\right].
\end{split}
\tag{T18}
$$

Because `log N_r/r -> log lambda` and `lambda>4`, the exponent in (T18) is at
least `cN` for all sufficiently large `r`, with any fixed
`0<c<log(lambda/4)`, for example `c=log(lambda/4)/2`.

The analytic factor in (T12) cannot remove this growth. By (T9), for `|z|<=1`,

$$
|\log D_N^{\rm cat}(\rho z)|
\le\sum_{j\ge1}\frac{\lambda^{-j/2}}j
=-\log(1-\lambda^{-1/2}).
$$

The logarithm here is the branch vanishing at the origin. In particular
`|D_N^{cat}(rho z)|>=1-lambda^(-1/2)`. Thus

$$
\boxed{
\int_0^{2\pi}|\widetilde{\mathcal Z}_N(R_Ne^{it})|^{-2}\frac{dt}{2\pi}
\ge\frac{(1-\lambda^{-1/2})^2}{\pi N}e^{cN}
}
\tag{T19}
$$

on the same infinite sequence. In contrast, the completely computed positive
reciprocal pseudo-orbit diagonal is asymptotic to
`N/(2s sqrt(2))`. The different-multiset terms in the actual reciprocal norm
are therefore indispensable and are not controlled by the sector law, even
together with the stated fixed analytic geometry, trace growth, exact
all-time orbit formula and fermionic cutoff.

This directly tests the denominator step; it does not merely assert that an
unspecified generic unitary could have different statistics.

### 13. A precise property of the original map that this model does not share

The original classical map is not `C^1` conjugate to `L`. This can be checked
at one fixed point, without a genericity assumption.

Use the exact effective symbol of the original family,

$$
a(q,p)=\cos14\pi q+r(q)/10+r(q)\sin2\pi q/100-1/10
+r(q+1/2)\cos(2\pi p-\alpha_0)/100.
$$

At `(0,0)`, its gradient vanishes and its Hessian is

$$
D^2a(0,0)=\begin{pmatrix}c_0&0\\0&0\end{pmatrix},
\qquad
c_0=-196\pi^2+\frac{392\pi^2}{10}
+\frac{8\pi^2}{100}\left(-\frac35\right)
=-\frac{19606\pi^2}{125}.
\tag{T20}
$$

Here `r(0)=r(1/2)=r'(0)=r'(1/2)=0`,
`r''(0)=392 pi^2`, and `r''(1/2)=8 pi^2`. The sine term has zero quadratic
part at the origin. The point is fixed by the Hamiltonian flow and by `L`.

For `t_*=tau/(2pi)`, the derivative of the original flow `phi_a^(-t_*)` at
this fixed point is exactly `[[1,0],[t_* c_0,1]]`: its infinitesimal matrix is
nilpotent of order two. Hence

$$
\boxed{
\operatorname{Tr}D\Psi(0,0)
=6-4t_*c_0
=6+\frac{39212\pi}{125}\tau\ne6.
}
\tag{T21}
$$

Every fixed point of `H L H^-1` has derivative similar to `L` and trace six.
A `C^1` conjugacy would preserve this derivative trace at a fixed point, so
(T21) excludes that specific coboundary mechanism for the original map.

This exclusion is a real distinction, but it is not an estimate of the
missing mixed hook products or reciprocal orbit sums. The countermodel proves
only that the previously listed sector and determinant results cannot supply
that estimate by themselves. The first original pair test and all-order
`H_diag` remain unproved.
