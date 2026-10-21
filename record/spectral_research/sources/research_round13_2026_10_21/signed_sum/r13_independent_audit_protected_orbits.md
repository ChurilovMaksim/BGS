> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round13_2026_10_21/signed_sum/r13_independent_audit_protected_orbits.md`. Embedded SHA256: `87f055e1805f700088f6439e40b6d022269834f7df658e697b5a51a31df4e8d5`.
> [Thematic guide](../../../../../mathematics/spectral_research/topics/classical_trace.md).

# Independent audit: protected actions and one-step trace

Date: 21 October 2026. Reviewer: `/root/r13_original_signed_sum`.

## 1. Normalized claim and verdict

**Primary verdict: proved as written.** This verdict concerns the raw file
`orbit_correlations/protected_actions_and_one_step_trace.md` at SHA-256
`b1dc645d52f16f7ca653f113796fb5d0b41764e7036f76a35b86328894ae714d`.
Its sixteen-point invariant set, ten primitive action entries, original
one-step trace asymptotic, strict fixed-time lower bound, and protected
principal-family subtraction estimate are correct as stated.

The verdict does **not** assert the original $H_{\rm diag}$, an original
countersequence, or a new limit of the remaining Heisenberg-time sum.
The one-step theorem is fixed-time. The subtraction theorem uses the
separately constructed exact orbit cocycle; it is not obtained by extending
one-dimensional stationary phase to growing times.

The author was asked for the raw claim, proof and source paths without an
author verdict. I derived the sixteen-point kinematics and four fixed-point
relative phases before reading the new source. Critical calculations below
were reconstructed directly. Agreement with a prior review label is not
evidence for them.

## 2. Exact input revisions and actual read scopes

| Input | SHA-256 | Actual scope |
|---|---|---|
| New orbit source | `b1dc645d52f16f7ca653f113796fb5d0b41764e7036f76a35b86328894ae714d` | Complete |
| `research_continuation_2026_10_20/exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` | Complete |
| `research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md` | `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b` | Sections 1–9, through line 570 |
| `research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` | Sections 1–9, through the start of Section 10 at line 800 |
| `research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md` | `355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c` | Sections 1–2, through line 105 |
| `research_round3_2026_10_21/audit_trace_foundation_independent.md` | `8cc14d6dbcae730a9a0b0a139f23fc285ce2a6a9772a1f58109f50c2b12614ac` | Complete, as navigation; the raw load-bearing sources were then read |

An initial batched display of old sources was truncated. The stated scopes
were subsequently read in smaller, untruncated ranges. No claim of reading
the unneeded algebraic-rigidity sections or the complete cumulative master
is made.

## 3. Obligation matrix

| Obligation | Status | Decisive check |
|---|---|---|
| Actual ordinary symbol and physical-map sign | Passed | Modular factor $(-1)^{kl}$; physical flow $X_{-a}=(-a_p,a_q)$ |
| Maximal protected set | Passed | Two-step membership forces $8p\in\mathbb Z$ |
| Action phases | Passed | Odd character cancels the half-winding term |
| All rational table entries | Passed | Direct rational substitution for every protected starting point |
| Global Abel stationary phase | Passed | Two tail integrations by parts and the local Fourier Gaussian |
| Four-sector normalization | Passed | Exact comb scalar; relative phases reproduce the finite Gauss trace |
| Marked Hessians and monodromy | Passed | Direct derivatives and square-zero kick linearization |
| Error $O(N^{-1})$ | Passed | Four fixed one-dimensional integrals with integral error $O(h^{3/2})$ and prefactor $h^{-1/2}$ |
| Strict lower bound | Passed | Mean-value and convexity inequalities with the displayed constants |
| All-time principal weights used in Section 7 | Passed within the cited construction | Exact amplitude, exact sectors, contour and graph decomposition were checked separately |
| Protected-family pair subtraction | Passed | Geometric bound and $|\operatorname{Tr}U_N^m|\le N$ |
| Original remaining $H_2$ or all-order $H_{\rm diag}$ | Not addressed by those claims | The complementary sum remains unestimated |

## 4. Independent geometry and rational action calculation

For $h=(2\pi N)^{-1}$, an ordinary Weyl Fourier mode acts on the comb as
$(-1)^{kl}T_N(l,k)$. The mixed term of the true ordinary symbol is therefore
$r(q+1/2)\cos(2\pi p-\alpha_0)/100$, as in the new source. At both $q=0$
and $q=1/2$, $r(q),r(q+1/2)$ and their first derivatives vanish. Hence $da=0$
on both lines, and the Hamiltonian kick fixes their points.

If $z$ and $\Psi z$ are both on those lines, the inverse kick fixes
$\Psi z$, so $Lz$ is on the lines. For $q=0,1/2$ this means
$3q-4p\in\frac12\mathbb Z$ modulo one, equivalently $p\in\frac18\mathbb Z$.
Conversely the resulting sixteen points are invariant. Their map is

$$
(q,j/8)\mapsto(q-j/2,3j/8)\pmod1.
$$

Its square is the identity, and its fixed values of $j$ are exactly 0 and 4.
Thus there are four fixed points and six two-cycles. This is maximality
inside the two lines, not a classification of all periodic points.

Along a protected edge the full characteristic is constant, so the exact
Hamilton–Jacobi integral gives $F_{t_*}=F_0+t_*a$ at that edge. Let the
primitive winding be $(n_q,n_p)$. In the exact sector factor,

$$
(-1)^{n_qn_p}e^{-in_pn_q/(2h)}
=e^{i\pi(1-N)n_qn_p}=1
$$

because $N$ is odd. Consequently the reduced phase is exactly
$e^{2\pi iNB}e^{i\tau NC}$ with the source's $B,C$; neither an unretained
half-winding nor a time-squared correction remains.

Here is the independent unreduced rational calculation for the ten
primitive starting points. It uses $z_j=L^jz_0$ and
$B=\sum F_0(q_{j+1},q_j)-n_pq_0$ directly.

| Starting point | Period | Unreduced $B$ | $B\bmod1$ | $C$ |
|---|---:|---:|---:|---:|
| $(0,0)$ | 1 | $0$ | $0$ | $9/10$ |
| $(0,1/2)$ | 1 | $-3/2$ | $1/2$ | $9/10$ |
| $(1/2,0)$ | 1 | $-1/4$ | $3/4$ | $-11/10$ |
| $(1/2,1/2)$ | 1 | $-1/4$ | $3/4$ | $-11/10$ |
| $(0,1/8)$ | 2 | $-51/16$ | $13/16$ | $-1/5$ |
| $(0,7/8)$ | 2 | $-2499/16$ | $13/16$ | $-1/5$ |
| $(0,3/8)$ | 2 | $-459/16$ | $5/16$ | $-1/5$ |
| $(0,5/8)$ | 2 | $-1275/16$ | $5/16$ | $-1/5$ |
| $(0,1/4)$ | 2 | $-51/4$ | $1/4$ | $9/5$ |
| $(1/2,1/4)$ | 2 | $-5/4$ | $3/4$ | $-11/5$ |

All six other starting points on the two-cycles were checked as well and
have the same reduced entries as their partners. Exact `fractions.Fraction`
arithmetic was used, with no floating-point spectral calculation. The
geometric proof above establishes why the finite list is exhaustive.

## 5. Independent fixed-point phase normalization

Since $L-I=2\left(\begin{smallmatrix}1&-2\\-1&1\end{smallmatrix}\right)$
and the inner matrix is unimodular, the deck classes can be represented by
$n=(a,b)\in\{0,1\}^2$. The zero-kick fixed point is, modulo one,
$(q,p)=(a/2,(a+b)/2)$, and its unreduced stationary sector action is
$-a^2/4+b^2/2$.

With the odd character, the four phases are

$$
1,\quad-1,\quad\eta_N,\quad\eta_N,
\qquad\eta_N=e^{-i\pi N/2}.
$$

Multiplying their sum by the equal zero-kick amplitudes $1/2$ and by the
actual comb scalar $\zeta_N=e^{i\pi(3N-1)/4}$ gives

$$
\operatorname{Tr}M_N=\zeta_N\eta_N=e^{i\pi(N-1)/4},
$$

in agreement with the finite quadratic Gauss sum. In particular, omitting
the odd character and assigning four equal positive phases would be wrong.
The new source retains the correct signs.

For the prescribed nonzero time, the increments are exactly
$t_*\cdot9/10$ or $t_*\cdot(-11/10)$ at the unchanged fixed points.
Since $t_*/h=N\tau$, the two exponential factors in (5.3) have the correct
normalization and signs.

## 6. Global stationary phase with the Abel interpretation

To check the tail in Lemma 4.1, write $a=(1-\chi)b_h$, with $\chi$ equal
to one near the critical point. The phase derivative $s'$ is bounded away
from zero there and grows linearly at infinity. Two integrations by parts
produce the amplitude

$$
\left[\frac1{s'}\left(\frac a{s'}\right)'\right]'
=\frac{a''}{(s')^2}-\frac{3a's''}{(s')^3}
 -\frac{as'''}{(s')^3}+\frac{3a(s'')^2}{(s')^4}.
$$

It is uniformly integrable; the worst decay is $O(|q|^{-2})$.
Expanding compact cutoffs justify the integrations and their derivative
terms vanish. For Gaussian damping the additional first and second
derivatives are $-2\epsilon q e^{-\epsilon q^2}$ and
$(4\epsilon^2q^2-2\epsilon)e^{-\epsilon q^2}$. After division by the
indicated powers of $s'$, their extra $L^1$ norms tend to zero. The largest
such estimate is $O(\epsilon\log(1/\epsilon))$. Thus the Abel tail is
indeed $O(h^2)$.

In the local Morse coordinate, Fourier inversion gives

$$
\int e^{-iu^2/(2h)}g_h(u)\,du
=e^{-i\pi/4}\sqrt{2\pi h}\int
\widehat g_h(\xi)e^{2\pi^2ih\xi^2}\,d\xi.
$$

The error after replacing the last exponential by one is bounded by
$2\pi^2h\int\xi^2|\widehat g_h(\xi)|d\xi=O(h)$.
Four bounded derivatives and fixed compact support make this Fourier moment
uniformly finite. The Morse derivative at zero supplies
$|s''(q_*)|^{-1/2}$. Hence the local integral error is $O(h^{3/2})$, while
the tail is smaller. The lemma's order is correct.

The required uniform derivative norms come from the exact amplitude source.
Its finite Weyl-shift equation has removable real-$h$ quotients; allocating
the strip gap across the Dyson factors gives summable $n^{2r}q^n$ bounds
for the required derivatives. The bounded fixed-$h$ equation after factoring
$e^{iG/h}$ identifies the solution with the actual operator exponential.
Thus a formal WKB identification is not being used to supply the lemma's
input.

## 7. Hessians, coefficients and lower bound

Direct derivatives give

$$
r''(0)=392\pi^2,\quad r''(1/2)=8\pi^2,
\quad V''(0)=-784\pi^2/5,\quad V''(1/2)=984\pi^2/5.
$$

Using the corrected mixed term, the four values of $a_{qq}$ in the order
$(0,0),(0,1/2),(1/2,0),(1/2,1/2)$ are

$$
\frac{\pi^2}{125}(-19606,-19594,24306,24894).
$$

At these points $a_{pp}=a_{qp}=0$. Since the points are equilibria, the
linearized kick is the exact square-zero shear

$$
D\phi_{-a}^{t_*}
=\begin{pmatrix}1&0\\t_*a_{qq}&1\end{pmatrix},
\quad \operatorname{Tr}D\Psi=6-4t_*a_{qq}.
$$

This confirms all four constants $T_{ij}$ in the source.
For $J=F_{Qq}$, differentiating the generating equations gives
$Q_p=-1/J$, $Q_q=-F_{qq}/J$, $P_p=-F_{QQ}/J$. Hence

$$
\psi_n''=F_{QQ}+2J+F_{qq}=J(2-\operatorname{Tr}D\Psi).
$$

The negative stationary-phase scalar cancels the metaplectic
$e^{i\pi/4}$. With $B_0=2\sqrt J$, the coefficient becomes exactly
$(\operatorname{Tr}D\Psi-2)^{-1/2}$. There are four fixed sectors; the
aggregate error is $O(h)=O(N^{-1})$.

For the lower bound, $|(x^{-1/2})'|\le1/16$ on $[4,\infty)$, and convexity
gives $(4-x)^{-1/2}\ge1/2+x/16$ for the source's positive small $x$.
Therefore

$$
|\mathsf A|\le\tfrac32v,\qquad
\mathsf B\ge1+6150v,\qquad v=\pi\tau/125,
$$

and the reverse triangle inequality gives exactly

$$
\liminf_{N\text{ odd}}|\operatorname{Tr}U_N|
\ge1+\frac{12297\pi}{250}\tau>1.
$$

No irrational-rotation density argument is needed. The same asymptotic
bounds the unnormalized trace, so the individual target term at $m=1$
still has size $O(N^{-2})$.

## 8. All-time foundation and the principal-family subtraction

For the new source's Section 7, I checked the raw foundation separately:

- The comb scalar follows from the finite eight-term Gauss sum; the
  ordinary symbol follows from the midpoint factor.
- The finite coherent frame and translation-uniform Gaussian integrals
  justify the exact sector identity at each finite $m,N$. Grouping deck
  classes tiles the plane once, with no determinant multiplier.
- The exact one-step kernel can then be substituted in the Abel product.
- The cyclic Hessian is uniformly negative, including the actual duplicated
  cyclic edges at $m=1,2$.
- On the bounded contour $u-i\psi(u)$, monotonicity and the small perturbation
  Hessian give coercivity. The saturated tails are exponential, not falsely
  claimed globally Gaussian tails.
- The weighted kernel estimate gives one trace-norm neighborhood of the
  reference Gaussian independent of the number of iterates.
- Compatible right and left graph sections kill mixed products exactly;
  reflection and real finite jets make the first scalar $h$ coefficient
  imaginary. The Gaussian Hill formula and repeated Gaussian normalization
  then give the source's uniform modulus estimate (9.6).

The cone bound also has the stated range. In eigen-coordinates the derivative
is within $10^{-70}$ of $\operatorname{diag}(\lambda,\lambda^{-1})$.
On $|s|\le|u|/10$, the $u$ component grows by more than five and the image
remains in the cone. The projective map contracts; a periodic unstable line
therefore has a positive multiplier at least $5^m$.

Consequently the source's exact principal weights satisfy
$|\mathcal A_{m,N}(x)|\le5^{-m/2}e^{Cmh^2/2}$ uniformly. For $m\le B_0N$,
$mh^2\le B_0/(4\pi^2N)$, so at most sixteen protected starting points give
$|Q_{m,N}|\le C_{B_0}5^{-m/2}$.

Finally,

$$
\big||p_m|^2-|p_m-Q_m|^2\big|
\le2N|Q_m|+|Q_m|^2
$$

by $|p_m|\le N$. Both geometric sums converge. Multiplying by the fixed
bounded weight and dividing by $N^2$ proves the stated $O(N^{-1})$ bound.
Every cross term with the complementary principal sum and the residual is
included. Equality of the classical action phases is never converted into
equality of the full $h$-dependent amplitudes.

## 9. Independently checked stronger full-sector extension proposed by root

This paragraph audits the formula communicated by root separately; it does
not change the frozen author source. It is a direct corollary of the raw
Gaussian kernel bound and exact sector identity, requiring neither the
modulus estimate (9.6) nor the rank-one splitting.

For all sufficiently large odd $N$, the raw uniform edge estimate is
$\|K_h(x)-K_G\|_1\le10^{-4}$. Since $K_G$ has eigenvalues
$1,\lambda^{-1},\lambda^{-2},\ldots$,

$$
\|K_h(x)\|\le1.0001,\qquad
\|K_h(x)\|_1\le\frac{1+\sqrt2}{2}+10^{-4}<1.208.
$$

For a protected fixed point of $\Psi^m$, the exact full sector has outside
modulus $\lambda^{-m/2}$ and inside trace of the product of the $m$ edge
operators. One trace norm and $m-1$ operator norms therefore give

$$
|\mathcal S_{m,N}(x)|
\le1.208\lambda^{-m/2}(1.0001)^{m-1}.
$$

There are at most sixteen such sectors. Thus their full sum, retaining all
transverse terms, satisfies

$$
|Q^{\rm full}_{m,N}|
\le19.4\left(\frac{1.0001}{\sqrt\lambda}\right)^m
\quad\text{for every }m\ge1,
$$

with a single sufficiently-large-$N$ threshold. The rate is less than one.
The same elementary quadratic inequality proves the $O(N^{-1})$ pair
subtraction bound for every finite range, uniformly in its endpoint.
It also proves absolute convergence and the bound for an infinite series
of **termwise differences** with bounded weights. In that infinite version,
one must not express it as subtraction of two possibly divergent positive
series; the termwise-difference formulation is the valid one.

The finite protected sectors are indexed without duplication because the
exact fixed-point/sector bijection has already been checked. For odd $m$
there are four; for even $m$ there are sixteen. The upper bound sixteen is
valid in both cases.

## 10. Limits of the verdict

The original first unestimated sum is still

$$
N^{-2}\sum_{1\le m<2N}w(m/N)
\bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr).
$$

The audited subtraction removes a finite protected family at $o(1)$ cost
but gives no limit for the complement. The strict one-step excess over one
contributes only $O(N^{-2})$. Neither fact proves the all-order local limit
or an admissible original countersequence.

No author file was edited. The rational check verifies only the explicitly
exhaustive finite action computation. Historical verdict labels were used
for navigation and did not replace the raw source reconstruction described
above. The full-sector extension in Section 9 is audited as a separate
root-proposed consequence, not falsely attributed to the frozen source.
