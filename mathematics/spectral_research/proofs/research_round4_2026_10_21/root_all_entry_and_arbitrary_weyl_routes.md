> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/root_all_entry_and_arbitrary_weyl_routes.md`. Embedded SHA256: `c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd`.
> [Thematic guide](../../topics/dephasing.md).

# All-entry bounds and arbitrary prescribed Weyl permutation routes

21 October 2026. Root-owned proof for the exact original family and its fixed
`tau=10^(-80)`. This extends the one-step translation estimate to every
matrix coefficient of quantum conjugation. The resulting all-time estimate
removes a stated class of coherent contributions; it does not evaluate the
remaining trace and does not prove or refute `H_diag`.

## 1. Statement

Let `W_v=T_N(l,k)` for `v=(k,l)` denote the original modular Weyl basis. On
the traceless operator space, use the orthonormal basis indexed by

$$
 \Lambda_N=(\mathbb Z/N\mathbb Z)^2\setminus\{0\},\quad M=N^2-1,
$$

where the inner product of original matrices is `N^(-1)Tr(X*Y)`. Define

$$
 C^E_{w,v}=N^{-1}\operatorname{Tr}(W_w^*E_NW_vE_N^*),\quad
 C_{w,v}=N^{-1}\operatorname{Tr}(W_w^*U_NW_vU_N^*).
$$

Write `|v|_N` for the Euclidean norm of its centered integer representative.
There are fixed `C_*,N_*` and `rho<1`, depending on the prescribed family
only, such that for every odd `N>=N_*` and nonzero `v,w`,

$$
 \boxed{|C^E_{w,v}|\le C_*(1+|v|_N)^{-1/17}+C_*/N,\qquad
        |C^E_{w,v}|\le C_*(1+|w|_N)^{-1/17}+C_*/N,}
 \tag{1.1}
$$

$$
 \boxed{\max_{w,v\in\Lambda_N}|C^E_{w,v}|\le\rho<1.}
 \tag{1.2}
$$

The same maximum bound holds for `C`, and its column bound uses `|Sv|_N`
in place of `|v|_N`, with `S=[[3,2],[4,3]]`. This follows from the exact
identity `M_N W_v M_N*=W_(Sv)`.

For every time `j` choose any permutation `pi_(j,N)` of `Lambda_N`, and put

$$
 D_j e_v=C_{\pi_{j,N}(v),v}e_{\pi_{j,N}(v)},\qquad R_j=C-D_j.
 \tag{1.3}
$$

The choices are deterministic, may depend on `N` and the whole matrix, and
may vary at every time. There is one fixed `delta>0` such that the sum
`B_(n,N)` of all terms in

$$
 C^n=(D_n+R_n)\cdots(D_1+R_1)
$$

with at most `floor(delta n)` factors `R_j` satisfies, uniformly in the
entire choice of permutations,

$$
 \boxed{\frac1{N^2}\sum_{n\ge1}|\operatorname{Tr}B_{n,N}|
                  \le C N^{-1/17}.}
 \tag{1.4}
$$

There is also the stronger bound after the single time `n=1`:

$$
 \boxed{\frac1{N^2}\sum_{n\ge2}|\operatorname{Tr}B_{n,N}|
                  \le C N^{-2/17}.}
 \tag{1.5}
$$

Thus one may obtain the rate in (1.5) for a full correction by explicitly
leaving time one unchanged. Without that convention (1.4) is the asserted
all-time bound. Both estimates allow multiplication by arbitrary weights
of bounded supremum, with that supremum as an additional factor.

This manuscript supplies the raw proof below. Independent checking of this
new extension is required separately from the audits of its earlier inputs.

## 2. Exact finite-quantization inputs and a derivative improvement

The WKB construction in `counter_one_step_pinching_hs.md`, SHA-256
`a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629`,
Sections 1--5, proves the following for the original modular quantization.
Put

$$
 h=(2\pi N)^{-1},\quad t=\tau/(2\pi),\quad
 \widetilde W_v=(-1)^{kl}W_v,
 \quad Q_N(F)=\sum_v\widehat F(v)\widetilde W_v.
$$

The exact ordinary-half symbol is

$$
 a(q,p)=\cos14\pi q+r(q)/10+r(q)\sin2\pi q/100-1/10
       +r(q+1/2)\cos(2\pi p-\alpha_0)/100.
 \tag{2.1}
$$

In particular, `A_N=Q_N(a)`. There exist a fixed real analytic phase
`mathcal S=S_t` and a fixed positive real analytic amplitude `b=b_t` such
that, for `F=b exp(i mathcal S/h)`,

$$
 N^{-1/2}\|E_N-Q_N(F)\|_{\rm HS}\le C/N,
 \quad \int b^2=1,\quad
 \|\nabla\mathcal S\|_\infty\le200t,
 \quad \|\mathcal S''\|_{2\to2}\le1.6\,10^6t<1/10.
 \tag{2.2}
$$

All fixed derivatives of the phase and amplitude are bounded independently
of `N`. The exact multiplication law is

$$
 \widetilde W_u\widetilde W_v
      =e^{\pi i\omega(u,v)/N}\widetilde W_{u+v},
 \quad \omega(u,v)=u_2v_1-u_1v_2,
 \quad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
 \tag{2.3}
$$

The source proves its rapidly oscillating approximation by a pointwise
residual for an exact finite-shift equation, passed to HS norm through the
identity `N^(-1/2)||Q_N(G)||_HS<=2||G||_infty`. It also proves the exact
trace pairing with half-period aliases. These statements are used as proved
inputs, not inferred from classical dynamics. Their independent audit is
`audit_one_step_pinching_hs.md`, SHA-256
`7c59bc69854347e4615db94691d7d15bd86e0e776ce4bc639c07878bc611acce`.

The strip improvement in `counter_center_phase_c17_bound.md`, SHA-256
`992f35db1916f680083fe304caa3001bc71720e2a864f28ea3513f080b5340c5`,
proves `||mathcal S/t-a||<=20000t` on the complex tube of width `3/4000`.
Cauchy's estimate on polydisks therefore gives the following additional,
explicit bound in the maximum-partial-derivative convention:

$$
 \left\|\mathcal S/t-a\right\|_{C^{18},\max}
 \le20000t\,18!\,(4000/3)^{18}
 <\frac{127903052333056}{3378810882568359375}<\frac1{4000}.
 \tag{2.4}
$$

The first strict rational bound uses `t<10^(-80)/6`. The final inequality
is the integer comparison obtained on multiplying the numerator by 4000.
Every derivative of lower order is covered by the same upper bound. The
polydisk estimate at the open-strip boundary is understood as the limit of
smaller radii, on which the same supremum bound holds.

Every input in this section also holds for `E_N*` after replacing the real
symbol `a` by `-a`. The flow, midpoint contraction, transport and residual
arguments use the same absolute Fourier bounds. The two marked Fourier
coefficients only change sign. This checks the negative-kick application
needed for the row estimate later, without assuming it follows from a
statement proved for positive time alone.

## 3. Uniform oscillation despite an arbitrary added linear phase

We need derivatives of order at least two, because a large linear modulation
can cancel a first derivative. Here they are available at a fixed order.
Use `D_q=(2pi i)^(-1)partial_q`, `D_p=(2pi i)^(-1)partial_p`, and

$$
 \mathcal K=\{\pm1,\pm2,\pm5,\pm6,\pm7,\pm8,\pm9\},\qquad
 P_1(s)=s\prod_{k\in\mathcal K\setminus\{1\}}\frac{s-k}{1-k}.
$$

The exact Fourier support of (2.1) gives the coefficient extractors

$$
 \mathcal L_1=D_q(1-D_p^2)P_1(D_q),\qquad
 \mathcal L_2=\frac{D_p^2(D_p+1)}2
       \prod_{k\in\{1,6,7,8\}}(1-D_q^2/k^2).
 \tag{3.1}
$$

They give `mathcal L_1 a=a_(1,0)e^(2pi iq)` and
`mathcal L_2 a=a_(0,1)e^(2pi ip)`. The extra `D_q` or `D_p` leaves the
selected coefficient unchanged. Every differential monomial now has order
at least two, with maximum orders 17 and 11. Their formal coefficient
one-norms are at most 27 and 3, respectively. For clarity the first bound is
`2 prod_(k in K\{1})(1+|k|)/|1-k|=27`; the second is bounded by
`2(37/36)(50/49)(65/64)<3`. Replacing the formal `D` variables by ordinary
derivatives can only decrease these bounds. The coefficient magnitudes are

$$
 |a_{1,0}|=|1/20-i/200|\ge1/20,\qquad |a_{0,1}|=1/200.
$$

For any nonzero centered translation `z`, write `eta=dist(z,Z^2)` and
`F_z^A(x)=(A(x+z)-A(x))/eta`. At least one coordinate of `z` has magnitude
at least `eta/sqrt(2)`, and `|e^(2pi iu)-1|>=4|u|` on the centered interval.
Applying (3.1) therefore shows, at every point,

$$
 \max_{2\le|\alpha|\le17}|\partial^\alpha F_z^a|
                         \ge\sqrt2/300.
$$

For `R=mathcal S/t-a`, the integral mean-value formula bounds every derivative
of `F_z^R` of order at most 17 by `sqrt(2)||R||_(C18,max)`. Equation (2.4)
consequently proves a fixed lower bound greater than `1/2000` for the same
maximum with `A=mathcal S/t`. The normalized family includes `z=0` through
the directional limits `omega dot grad A`; the integral formula gives
continuous dependence in all required derivatives.

It follows that, for every real vector `ell`, every `lambda>=1`, and uniformly
`C^1`-bounded amplitudes `a_z`,

$$
 \boxed{\left|\int_{\mathbb T^2}a_z(x)
 e^{i\lambda(\mathcal S(x+z)-\mathcal S(x))+i\ell\cdot x}\,dx\right|
 \le C\sup_z\|a_z\|_{C^1}(1+\lambda\eta)^{-1/17}.}
 \tag{3.2}
$$

For a nonintegral modulation the torus integral here means the integral over
a fixed fundamental region; the applications below have periodic modulations.
Here are the details of uniformity in `ell`. The finite jet bound reduces,
by the invertible Vandermonde systems of directional derivatives, to a finite
cover on which some directional derivative of order between 2 and 17 is
bounded below. Smooth spatial localization is uniform over the compact
normalized translation family. Adding a linear function changes none of
those derivatives. The one-dimensional divided-difference and integration
by parts proof in `root_uniform_analytic_oscillation.md`, SHA-256
`5eaae7946e30df2507a870535ec46c2dbc2bce07cc96c8b85366772cab590d31`,
Section 4, uses no upper bound on the first derivative when its order is at
least two: its sublevel set and monotone sign intervals are controlled by the
specified higher derivative. It thus applies with constants independent of
the added slope. Summing the finite cover and using absolute integration for
`lambda eta<1` proves (3.2). One can equivalently perform this localization
inside a finite collection of translated coordinate rectangles before
integrating over the fixed fundamental region. There are only finitely many
boundary pieces, and the one-dimensional estimate allows interval endpoints.

## 4. Exact pairing for arbitrary input and output labels

For this calculation use the ordinary-half basis `tilde W`. Changing from
it to the original basis multiplies coefficients by unit signs and never
changes their absolute values. Represent `v,w` by centered integer vectors.
Equation (2.3), first on single Fourier modes and then on absolutely
convergent series, gives

$$
 \widetilde W_{-w}Q_N(F)\widetilde W_v
 =\zeta_{v,w}Q_N\!\left(e^{2\pi i(v-w)\cdot x}
             F(x-J(v+w)/(2N))\right),\quad
 \zeta_{v,w}=e^{\pi i\omega(v,w)/N}.
 \tag{4.1}
$$

Replacing each `E_N` in the normalized trace pairing by `Q_N(F)` costs
`O(N^(-1))`, uniformly in both labels. Indeed normalized HS
Cauchy--Schwarz bounds the error by `eta_N(2+eta_N)`, where
`eta_N=N^(-1/2)||E_N-Q_N(F)||_HS`, since every Weyl matrix is unitary.

In the exact alias trace identity set, for `m=(r,s)`,

$$
 H_m=(s/2,r/2),\quad k_m=v-w-Nm,
 \quad z_m=-J(v+w)/(2N)-H_m.
$$

Since `H_m` equals `Jm/2` modulo the integer lattice,

$$
 \boxed{z_m\equiv-J(v-k_m/2)/N\pmod{\mathbb Z^2}.}
 \tag{4.2}
$$

Shift the integration variable by `H_m`. The result is the exact oscillatory
pairing, up to the already bounded matrix error,

$$
 C^E_{w,v}=\sum_{m\in\mathbb Z^2}\gamma_m
   \int b(x)b(x+z_m)
    e^{2\pi i\{N(\mathcal S(x+z_m)-\mathcal S(x))+k_m\cdot x\}}dx
     +O(N^{-1}),\qquad |\gamma_m|=1.
 \tag{4.3}
$$

In the ordinary-half basis the exact constants are
`gamma_m=zeta_(v,w)(-1)^(rs) exp(-2pi i k_m dot H_m)`; the basis signs
give one further constant of modulus one. All aliases, including the half
periods, remain in (4.3). The sum converges at each fixed `N` by absolute
Fourier convergence; the following bounds also make it uniformly summable.

## 5. A two-case estimate proves the uniform column bound

Put `V=|v|_N>0`. If `|k_m|<=V`, the distance to the lattice and (4.2) give

$$
 \operatorname{dist}(z_m,\mathbb Z^2)
 \ge V/N-|k_m|/(2N)\ge V/(2N).
 \tag{5.1}
$$

This remains valid at the boundary of the centered box. Apply (3.2) with
`lambda=2pi N` and linear modulation `2pi k_m`: the integral is bounded by
`C(1+V)^(-1/17)`. There are at most a fixed number of such aliases, since
the `k_m` are spaced by `N` and `V<=N/sqrt(2)`.

If `|k_m|>V`, use the actual lift `z=-J(v-k_m/2)/N` in the mean-value
formula. Let the real phase in braces in (4.3) be `Phi`. The Hessian bound
in (2.2) implies

$$
 \|N\nabla(\mathcal S(x+z)-\mathcal S(x))\|_2
 \le\tfrac1{10}(V+|k_m|/2)<\tfrac3{20}|k_m|.
$$

Choose a coordinate with `|(k_m)_j|>=|k_m|/sqrt(2)`. Then
`|partial_j Phi|>|k_m|/2`. For every fixed positive derivative order the
phase `Phi/|k_m|` has uniform bounds: for the periodic part this follows by
the same mean-value argument using one additional derivative of `mathcal S`,
and the linear part has bounded first derivative. The translated amplitudes
have uniform fixed derivative bounds as well. Repeated integration by parts
in this coordinate therefore gives, for any fixed integer `K`,

$$
 \left|\int b(x)b(x+z_m)e^{2\pi i\Phi(x)}dx\right|
                                  \le C_K(1+|k_m|)^{-K}.
 \tag{5.2}
$$

Boundary terms cancel: the amplitude and the integration-operator
coefficients are periodic, and `k_m` is an integer vector. Among aliases
with `|k_m|<=2N` there are only a bounded number. Their total in this case
is at most `C(1+V)^(-K)`. The rest sum to `O(N^(-K))` for `K>2`, by
centered lattice shells of the mesh `N`. Combining both cases and the
uniform matrix error in (4.3) proves the first bound in (1.1).

Apply the identical argument to `E_N*`, whose checked inputs were described
after (2.4). Its adjoint matrix is the Hermitian transpose of `C^E`.
Interchanging `v,w` proves the second bound in (1.1).

## 6. Fixed labels have strict modulus loss

For fixed nonzero integer `v,w`, the coefficient has a classical limit that
can be proved directly from the finite commutator, as follows. Let

$$
 Z=J\nabla a,\qquad \Psi_s'=Z(\Psi_s),\quad\Psi_0(x)=x,\qquad
 f_s(x)=e^{2\pi i v\cdot\Psi_s(x)}.
$$

Then `partial_s f_s=Z dot grad f_s`. For fixed `v`, these symbols and all
their fixed derivatives are uniformly bounded for `0<=s<=t`. From (2.3),
the Fourier multiplier of `(i/h)[Q_N(a),Q_N(f_s)]` is
`-2h^(-1)sin(2pi^2h omega)`, whereas that of `Q_N(Z dot grad f_s)` is
`-4pi^2 omega`. The elementary bound `|sin x-x|<=|x|^3/6` gives

$$
 \|(i/h)[Q_N(a),Q_N(f_s)]-Q_N(Z\cdot\nabla f_s)\|
 \le C_v h^2.
$$

The coefficient sum here is finite in the `a` index and summable in the
other index: `sum (1+|u|)^3|widehat f_s(u)|` is bounded by a fixed `C^6`
norm in dimension two. No low-frequency truncation or unproved Egorov
theorem is used. Conjugation by the exact propagator preserves operator
norm, so its inhomogeneous Duhamel formula gives

$$
 \|E_N\widetilde W_vE_N^*-Q_N(f_t)\|\le C_v h^2.
 \tag{6.1}
$$

The exact Weyl trace then gives, in the ordinary-half basis,

$$
 C^E_{w,v}\longrightarrow\widehat f_t(w).
 \tag{6.2}
$$

All nonzero aliases in this last fixed-frequency trace are `O(N^(-K))`
for every fixed `K`, by smooth Fourier decay. Basis signs do not change the
limiting modulus. Only finitely many fixed pairs will be used below, so no
uniformity in growing `v,w` is being asserted in (6.1)--(6.2).

We claim `|widehat f_t(w)|<1` for every `v!=0` and every `w`. Equality in
the triangle inequality for a unit-modulus continuous integrand would imply

$$
 e^{2\pi i v\cdot\Psi_t(x)}=c e^{2\pi i w\cdot x}
 \quad\hbox{at every }x.
$$

The lift `Psi_t(x)=x+d_t(x)` has periodic displacement. On the connected
covering space this equality forces `(v-w) dot x+v dot d_t(x)` to be
constant: its values lie in one translate of the discrete set of integers.
Integer shifts of `x` then force `w=v`. It remains to exclude a constant
function `v dot d_t`.

The real-flow bounds `||Z||_infty<=200`, `||DZ||_(infty->infty)<=10000`
give, by integration of the displacement,

$$
 \|d_t-tZ\|_\infty\le10^6t^2.
 \tag{6.3}
$$

The marked Fourier coefficients of `Z` are `2pi i J e_j a_(e_j)`. Put
`V_infty=max(|v_1|,|v_2|)`. If the maximum is `|v_2|`, use the `e_1`
coefficient; otherwise use `e_2`. In either case the corresponding
coefficient of `v dot d_t` has modulus at least

$$
 (2\pi/200)tV_\infty-2\,10^6t^2V_\infty>0,
 \tag{6.4}
$$

because the original `t` is at most `10^(-10)`. This excludes constancy and
proves the strict loss in (6.2).

Choose a fixed radius `R_*` and then a fixed threshold in `N` so that the
two high-label bounds in (1.1) are at most `1/2` whenever either label has
norm at least `R_*`. For the remaining finite set of integer pairs, the
strict limits (6.2)--(6.4) have maximum `gamma<1`. Uniform convergence over
this finite set makes every such coefficient at most `(1+gamma)/2` for
all sufficiently large odd `N`. Taking a number `rho<1` at least both this
bound and `1/2` proves (1.2). This is a uniform gap for individual matrix
entries, not a contraction of the unitary matrix `C^E` as an operator.

## 7. Uniform HS bounds for every selected permutation

The covariance `M_N W_v M_N*=W_(Sv)` gives `C_(w,v)=C^E_(w,Sv)`.
The label map is invertible for every modulus. For every permutation in
(1.3), the selected columns have mutually orthogonal output supports, so

$$
 \|D_j\|\le\rho,\qquad
 \frac{\|D_j\|_{\rm HS}^2}{M}
   =\frac1M\sum_{v\ne0}|C_{\pi_{j,N}(v),v}|^2
   \le C N^{-2/17}.
 \tag{7.1}
$$

For the last bound, square (1.1), reindex by `Sv`, and use the shell count
`8r` for centered labels of maximum-coordinate norm `r`. The sum of
`r(1+r)^(-2/17)` through `N/2` is `O(N^(2-2/17))`; also
`M>=8N^2/9`. The error term `O(N^(-2))` after squaring is smaller.
Thus all `D_j` have normalized HS norm at most a common
`sigma_N=C N^(-1/17)`. No restriction on the chosen permutations appears
in this estimate.

## 8. The all-time coherent bound

Choose `g=min(1-rho,1/2)>0` and, if necessary, replace `rho` in the
following bounds by `1-g`, still an upper bound for every `||D_j||`.
Then `||R_j||<=2-g`. Define the fixed numbers

$$
 \delta=\frac{-\log(1-g/2)}{2\log(2(2-g)/g)},\quad
 z_g=\frac{g}{2(2-g)},\quad\eta=\sqrt{1-g/2}<1.
 \tag{8.1}
$$

Here `0<delta<1/2`. In a length-`n` word with `r<=floor(delta n)`
complementary letters there is at least one `D_j`. Put one such factor in
HS norm and the rest in operator norm. This proves

$$
 |\operatorname{Tr}(\mathrm{word})|/M
 \le\sigma_N\rho^{n-r-1}(2-g)^r.
$$

Summing all placements uses the exact binomial majorant

$$
 \sum_{r\le\lfloor\delta n\rfloor}\binom nr\rho^{n-r}(2-g)^r
 \le z_g^{-\delta n}(\rho+z_g(2-g))^n=\eta^n.
$$

Consequently

$$
 \|B_{n,N}\|\le\eta^n,\qquad
 |\operatorname{Tr}B_{n,N}|/M\le(\sigma_N/\rho)\eta^n.
 \tag{8.2}
$$

As `rho>=1/2` and `1-eta>=g/4`, summation gives the explicit bound
`N^(-2)sum_(n>=1)|Tr B_(n,N)|<=8 sigma_N/g`, which proves (1.4).
For an arbitrary bounded weight array the same absolute sum is bounded by
`8 W sigma_N/g`.

For `n>=2`, the same inequality `delta<1/2` ensures at least two selected
factors in every word. Split the cyclic trace at those two factors and use
HS Cauchy--Schwarz and the HS ideal inequality. The improved bound is

$$
 |\operatorname{Tr}(\mathrm{word})|/M
 \le\sigma_N^2\rho^{n-r-2}(2-g)^r.
$$

For example `|Tr(A D_a B D_b)|<=||A D_a||_HS||B D_b||_HS`, with all
other factors absorbed into `A,B`; complex conjugation in Cauchy--Schwarz
does not change either norm. Summation of the same binomial majorant gives
`|Tr B_(n,N)|/M<=sigma_N^2 rho^(-2)eta^n`. Its series for `n>=2` is at
most `16 sigma_N^2/g`, proving (1.5). No claim that the time-one trace
vanishes for an arbitrary permutation is made.

The arguments also permit a separately chosen list of permutations for each
`n`; all estimates at that time are uniform in the list. This still describes
one selected route list at each time, not the union of all possible lists.

## 9. Relation to the original pair statistic and the exact remaining gap

The scalar identity operator contributes one eigenvalue to quantum
conjugation. Therefore its restriction used here satisfies exactly

$$
 \operatorname{Tr}C^n=|\operatorname{Tr}U_N^n|^2-1.
$$

For every finite weighted sum, its change upon deleting the specified
contributions is exactly `N^(-2)sum_n w_(n,N)Tr B_(n,N)`. Bounds
(1.4)--(1.5) include the complete original squared trace through this
identity; they do not discard a cross-term by replacing amplitudes with
entrywise probabilities. The correction is absolutely summable for all
bounded weights, including every compact Fourier window and the full
infinite Abel weights. Separate convergence of two unweighted infinite
series is not asserted.

For the specific admissible test `b_*` defined in Section 7 of
`root_exact_identities_and_closure.md`, write `w=|widehat b_*|^2`.
Its Fourier support is contained in `[-2,2]`, so the first missing limit
for that test, even after these estimates, is

$$
 \frac1{N^2}\sum_{1\le n<2N}w(n/N)
 \left[\operatorname{Tr}(C^n-B_{n,N})-(\min(n,N)-1)\right]
 \longrightarrow0.
 \tag{9.1}
$$

It has not been evaluated. For a general admissible test replace the displayed
range by all positive integers; the Fourier weight makes that sum finite.
The retained trace need not be real for an
arbitrary route choice, although the whole exact sum is real. It is not
asserted to be a squared trace or a moment of a new unitary matrix. The
number of possible length-`n` route lists is enormous; uniform control of
one chosen list does not justify summing this bound over them all. No
assertion about higher fixed factorial orders follows from (1.4).

