> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/dual_audit_explicit_finite_type16.md`. Embedded SHA256: `34ecf87576cb73990458a656200d9b6e41016f0082796beacea247106c4ed90e`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the explicit finite-type-16 supplement

21 October 2026. Auditor: the Weyl dual-dynamics branch.

Audited source: `audit_explicit_symbol_finite_type16.md`, SHA-256
`1da0fbd15dec74a90a742804f69165f478673ce07aaf7eb38760de7f60cb7ffb`.
The full source, Sections 1--7, was read and its hash checked. It was not
modified. This audit reconstructs the support and extractor identities before
checking the perturbation and oscillatory consequences.

## Verdict

**The finite-type lemma and its application to the exact center phase are
proved as stated.** The coefficients, degrees, formal polynomial one-norms,
positive-order restriction, translated derivative estimate, C17 perturbation
margin and exact rational Cauchy calculation are correct. In conjunction with
the separately audited exact WKB/pinching source, the displayed rates
$$
|\sigma_{N,d}^2-d^{-2}|\le C N^{-1/16},
\qquad \sigma_{N,d}\le d^{-1}+C N^{-1/32}
$$
follow with constants independent of N and d. They are statements about the
original fixed kick, not about a linearized phase substituted in an exponential.

## 1. Exact support reconstruction

Write $\theta=2\pi q$. Multiplying
$(1-\cos7\theta)(1+\cos\theta)$ gives
$$
r_0=1,\quad r_{\pm1}=1/2,\quad r_{\pm7}=-1/2,
\quad r_{\pm6}=r_{\pm8}=-1/4,
$$
with all other coefficients zero. In the pure-q part of a, the constant
$r_0/10$ cancels the subtracted $1/10$. Its sine contribution at frequency
k is $-i(r_{k-1}-r_{k+1})/200$. Combining this with the cosine and r terms
gives the positive-frequency coefficients
$$
\begin{array}{c|ccccccc}
k&1&2&5&6&7&8&9\\\hline
a_{k,0}&1/20-i/200&-i/400&-i/800&-1/40-i/400&9/20&-1/40+i/400&i/800.
\end{array}
$$
The negative coefficients are conjugates. All listed coefficients are nonzero
and there are no other pure-q frequencies. The mixed rows have l equal to
plus or minus one and q support $0,\pm1,\pm6,\pm7,\pm8$; replacing r(q)
by r(q+1/2) multiplies them by $(-1)^k$ without changing their support.
The required magnitudes are consequently
$$
|a_{1,0}|\ge1/20,\qquad |a_{0,1}|=1/200.
$$
These are identities for the continuous finite symbol before modular aliasing;
the extractor argument correctly operates on that symbol.

## 2. Extraction identities and positive derivative orders

The source uses $D_q=(2\pi i)^{-1}\partial_q$ and
$D_p=(2\pi i)^{-1}\partial_p$, whose Fourier multipliers are k and l.
Let $\mathcal K$ be the fourteen pure-q frequencies reconstructed above.
For
$$
P_1(s)=s\prod_{k\in\mathcal K\setminus\{1\}}\frac{s-k}{1-k},
$$
all denominators are nonzero, $P_1(1)=1$, and $P_1$ vanishes at all
other elements of $\mathcal K$ and at zero. Its degree is fourteen and
its constant term is zero. Multiplying $P_1(D_q)$ by $1-D_p^2$ kills
both mixed rows, so exactly
$$
\mathcal D_1a=a_{1,0}e^{2\pi iq}.
$$
Its maximal total differential order is sixteen and every monomial has
strictly positive order.

For
$$
\mathcal D_2=\frac{D_p(D_p+1)}2
 \prod_{k\in\{1,6,7,8\}}(1-D_q^2/k^2),
$$
the p multiplier is one at l=1 and zero at l=0,-1. The remaining q polynomial
is one at zero and vanishes at all nonzero q frequencies of the mixed row.
Thus exactly $\mathcal D_2a=a_{0,1}e^{2\pi ip}$. Its order is at most ten,
and its p factor again excludes a constant differential monomial.

Constant-coefficient differential operators commute with translation, proving
the same exact extraction identities for the normalized translated differences.
No integration or pointwise approximation enters this step.

## 3. Polynomial coefficient budgets, independently checked exactly

The coefficient one-norm of a product is at most the product of the one-norms.
Each negative k in P1 contributes
$(1+|k|)/|1-k|=1$. Its six positive k other than one contribute
$$
3\cdot\frac64\cdot\frac75\cdot\frac86\cdot\frac97\cdot\frac{10}8
=\frac{27}{2}.
$$
The initial s factor has one-norm one, and $1-D_p^2$ has one-norm two.
Therefore the full D1 budget is 27. The q and p supports do not introduce an
additional factor two beyond this one.

For D2 the p factor has one-norm one. Its four q factors give
$$
2\cdot\frac{37}{36}\cdot\frac{50}{49}\cdot\frac{65}{64}
=\frac{60125}{28224}<3.
$$
An independent exact rational expansion of P1 verified all its interpolation
values and found
$$
\|P_1\|_{\ell^1}=\frac{6409325}{3048192},\qquad
\|\mathcal D_1\|_{\ell^1(D_q,D_p)}
=\frac{6409325}{1524096}.
$$
Thus the product upper bound is correctly used as an upper bound, not as an
asserted equality after coefficient cancellation.

Converting a monomial to ordinary derivatives multiplies its coefficient
magnitude by $(2\pi)^{-j}\le1$, where its order j is positive. Hence,
at each point, the maximum of ordinary derivatives of orders 1 through 16
controls the two extracted values with constants 27 and 3 respectively, as
claimed in (3.2) of the source.

## 4. Translation, finite jets and perturbation

For a centered translation z with length delta, one coordinate has modulus
at least $\delta/\sqrt2$. The elementary sine inequality on the centered
interval gives $|e^{2\pi iu}-1|\ge4|u|$. The exact extractor at that
coordinate consequently gives, at every point x,
$$
J_{16}(F_z^a;x)\ge
\begin{cases}
\sqrt2/270,&\text{if the q coordinate is used},\\
\sqrt2/300,&\text{if the p coordinate is used}.
\end{cases}
$$
The isolated Fourier exponential has modulus one, so these are pointwise
lower bounds, not estimates only at a maximizing point of the phase.

For $R=A-a$, the segment identity is exact:
$$
\partial^\alpha F_z^R(x)
=\int_0^1 (z/\delta)\cdot
 \nabla\partial^\alpha R(x+uz)\,du.
$$
If $|\alpha|\le16$, each gradient component is controlled by the
maximum C17 norm. The sum of absolute coordinates of the unit vector
$z/\delta$ is at most $\sqrt2$, giving an error at most
$\sqrt2/4000$. The maximum jet obeys the reverse triangle inequality.
Using even the weaker unperturbed lower bound $J_{16}>1/1000$ gives
$$
J_{16}(F_z^A;x)>\frac1{1000}-\frac{\sqrt2}{4000}>\frac1{2000}.
$$
The integral formula extends the normalized differences continuously in C16
to $z=r\omega$, r=0, when A is C17. The stated non-strict lower bound
therefore also holds at every directional limit. No analyticity is being
assumed in this perturbative lemma.

## 5. C17 bound for the exact center phase

The source uses the already constructed holomorphic action on the strip of
width $\rho/2=1/2000$, with $\|\nabla S_s\|_\infty\le200s$.
The complex Hamilton--Jacobi argument $x-J\nabla S_s/2$ lies in the wider
width-$2\rho$ strip. Integrating the differential of a along the connecting
segment bounds the Hamilton--Jacobi difference by $40000s$, because there
are two partial derivatives, each at most 200, and coordinate displacements
at most 100s. Integration in s gives
$\|S_t/t-a\|_\infty\le20000t$ on the complex strip.

A polydisk of radius $1/2500<1/2000$ is strictly inside that strip. The
successive Cauchy formulas give
$$
\|S_t/t-a\|_{C^{17},\max}
\le20000t\,17!\,2500^{17}.
$$
Since $2\pi>6$, substituting the exact t makes this strictly smaller than
$$
\frac{20000\cdot17!\cdot2500^{17}}{6\cdot10^{80}}
=\frac{28945917}{419430400000}.
$$
Independent Fraction arithmetic confirmed that equality and the integer
comparison
$$
419430400000-4000\cdot28945917=303646732000>0.
$$
Thus the maximum C17 norm is indeed below $1/4000$.

The stronger sum-of-derivatives bound in the separate wider-strip supplement
was already independently audited in `dual_audit_center_phase_c17.md`, SHA-256
`f9389738b8ff10a520d3c8a9c2d1ad4467e7990273433de4d7e517ccfdd87ad0`.
The present maximum-norm computation is itself sufficient and does not depend
on using the stronger estimate.

## 6. Oscillatory exponent and what the application does not replace

The exact normalized translated phase for S_t is t times that for S_t/t.
Its finite jet therefore has the fixed positive lower bound $t/2000$ with
orders at most sixteen. The parameter compactification, finite directional
Vandermonde reduction, localized one-dimensional estimates and grid averaging
were independently checked in `dual_audit_root_uniform_analytic_oscillation.md`,
SHA-256 `beafab75dc06644b22aa2395f6fd05dcc3628ab20d895ccb8e560b093819a9ff`.
Applying those arguments with the present explicit maximal order fixes the
decay exponent to $1/16$. Constants may depend on the fixed extremely small
t, but do not depend on N, d, the translation or the point.

The exact kick representation and its uniform $O(N^{-1})$ remainder are
inputs from the separately audited WKB/pinching theorem. Averaging its nonzero
translation terms gives $C N^{-1/16}$, while its identity term is exactly
$d^{-2}$. The uniform matrix remainder also averages to $O(N^{-1})$,
with no factor d. This proves the stated bound for the absolute difference
of the squared pinching norm. Finally
$\sqrt{x+y}\le\sqrt x+\sqrt y$ for nonnegative x,y gives the exponent
$1/32$ for the pinching norm itself.

At no point is $e^{iS_t/h}$ replaced by $e^{ita/h}$. The C17 closeness
certifies only finite type; the oscillatory phase and the matrix comparison
retain S_t exactly. Consequently the proof does not incur a hidden error
$(S_t-ta)/h$ at large N. It also makes no claim of full pair or higher-order
spectral universality.
