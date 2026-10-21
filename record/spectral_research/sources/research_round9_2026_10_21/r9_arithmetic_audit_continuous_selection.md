> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round9_2026_10_21/r9_arithmetic_audit_continuous_selection.md`. Embedded SHA256: `e2ffa265abd856e9c8dc827e66438b74e9fbef299a3d8c5c4bbb841477dd5908`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: continuous-symbol stability and the common diagonal choice

21 October 2026. Auditor: `/root/r9_original_arithmetic`.

## 0. Verdict and exact scope

**PASS** for Sections 1--7 of the frozen continuous-symbol stability
note, including the positive quantization in Section 7, the
unconditional comparison of local laws, and the equivalence of full
`H_diag` as a predicate.

**PASS** for the joint threshold selection and spectral argument in
Sections 5--6 of the frozen root normalization note, given the
fixed-polynomial analytic conclusions explicitly stated in its
Sections 2--4. The latter analytic kernel and graph construction has
its own completed independent audit,
`r9_sector_analytic_normalization_independent_audit.md`, SHA-256
`0fc9a15bcccab691e2912e64c4d018aba8c822494d00ad848d468fbb5933cd51`.
This report does not claim to have independently repeated that full
analytic audit as well.

There is no uncovered limit exchange or first unproved estimate in
the spectral-selection argument audited here. In particular:

* all sufficiently large odd dimensions are retained;
* no growing-symbol or growing-time Egorov estimate is used;
* the unconditional Laplace comparison does not assume `H_diag`
  or any higher count moment;
* higher count moments are derived only after assuming one endpoint
  satisfies the entire `H_diag`, exactly where that assumption is
  permitted for proving its equivalence;
* the canonical continuous-symbol endpoint is an actual unitary
  matrix, with an actual `o(N^{-1})` operator-norm comparison to
  the diagonal polynomial endpoint;
* the common threshold sequence works for every fixed time-window
  multiple and every fixed test, without enumerating uncountably
  many tests in the threshold construction.

This verdict proves neither endpoint satisfies `H_diag`. The first
unproved original weighted pair estimate is recorded in Section 10.

## 1. Frozen files and raw inputs

The following hashes were computed from the actual bytes read.
The continuous-symbol note was first reviewed at SHA-256
`0480f20a662fe949041b42c81ded24c0d2b55105e7b1d80c57d9082b906f9d91`.
Its author then changed only a dummy Riemann-sum index and the
scope/provenance text to identify the completed analytic proof.
Those touched paragraphs in Sections 0, 7--9 were reread, and the
final frozen hash is the one in the table. The norm, QE, matching,
and moment arguments did not change.

| Source | SHA-256 |
|---|---|
| `research_round9_2026_10_21/r9_sector_continuous_symbol_stability.md` | `0145256f03ad92f70a5852ecb11280dc3b1bccfa54b74af8b70e459b2e6577df` |
| `research_round9_2026_10_21/root_diagonal_cocycle_normalization.md` | `afeaa52cea23836c5b4fa58d1040daa6df792d0b9adea83f8eb1de8690211921` |
| `research_round3_2026_10_21/subprincipal_stability_theorem.md` | `63597dea1e627925280e79644ccc54ed68b9327c9ab757f6eea9ad69962e2381` |
| `research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md` | `355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c` |

For the old subprincipal source, the original normalization,
fixed-time Weyl/Duhamel calculation, normalized trace proof, and
time-average argument in Sections 1--3 were read. For the classical
source, Sections 1--3 were read, including the explicit weighted
Fourier operator estimate. The ergodicity used below is therefore
not accepted merely because an external theorem was called
standard in another file.

The actual physical map has the convention

$$
 \Psi=\phi_{a^{(0)}}^{-\tau/(2\pi)}\circ L,
 \qquad L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},
$$

and it is this map that occurs in
`U_N^{-1}Q_N(a)U_N=Q_N(a circ Psi)+o(1)`. The opposite
adjoint convention used in some other old notes is not silently
substituted here.

## 2. Fixed-symbol estimates and classical ergodicity

The ordinary-half operators are exactly

$$
 W_N(k,l)=(-1)^{kl}T_N(l,k),
 \qquad
 W_N(\kappa)W_N(\eta)
 =e^{\pi i\omega(\kappa,\eta)/N}W_N(\kappa+\eta).
 \tag{2.1}
$$

These are identities for integer labels before their reductions,
including the signs on aliases. For fixed smooth symbols the
weighted Fourier sums in the product error and commutator error
converge. Thus the displayed fixed-symbol product estimate and
fixed-time Duhamel proof apply through every odd dimension.
Normalized trace convergence follows because every additional
alias pair has at least one frequency of size at least `N/2`;
rapid Fourier decay controls the total alias mass.

The norm lemma is valid with exactly its stated quantifiers. Fix
real smooth `a` and `M>||a||_infty`, and put
`c=(M^2-a^2)^(1/2)`. It is a fixed smooth real function. The
product estimate yields

$$
 Q_N(a)^2+Q_N(c)^2=M^2I+O_{a,M}(N^{-1}).
 \tag{2.2}
$$

Since both squares are positive, one first obtains
`limsup ||Q_N(a)||<=M` and then lets `M` decrease. There is
no assertion of finite-`N` positivity of Weyl quantization, and
no uniform boundedness claim for its extension to arbitrary
continuous functions.

For completeness, the weighted classical Fourier construction does
imply the ergodicity needed for QE. The raw source proves
`R=1 direct-sum R_perp`, where `R` is trace class and
`||R_perp||<=1-1/8000<1`. Its matrix is

$$
 R_{nk}=\frac{w_n}{w_k}\langle e_n,e_k\circ\Psi\rangle.
 \tag{2.3}
$$

For finite Fourier projections `P_M`, the weight factors telescope
in every matrix entry of `(P_M R P_M)^r`. Trace-class compactness
gives operator-norm convergence on the weighted side; the
corresponding truncated Koopman operators converge strongly to
the unitary Koopman operator, and so do their fixed powers.
Consequently, for fixed `r,n,k`,

$$
 (R^r)_{nk}=\frac{w_n}{w_k}
             \langle e_n,e_k\circ\Psi^r\rangle.
 \tag{2.4}
$$

The contraction bound gives decay of all correlations of
mean-zero trigonometric polynomials. Their density in `L^2`,
together with the isometry of composition by the area-preserving
map, gives mixing on `L^2`. This in particular proves ergodicity.
This passage does not use an illicit bounded conjugation by the
unbounded diagonal weight operator.

The same argument proves directly the time-average consequence
needed later. For fixed mean-zero `a`,

$$
 \left\|\frac1T\sum_{r<T}a\circ\Psi^r\right\|_2^2
 =\frac1{T^2}\sum_{r,s<T}
       \langle a\circ\Psi^r,a\circ\Psi^s\rangle\to0.
 \tag{2.5}
$$

Indeed, correlations at large `|r-s|` tend to zero, while the
number of pairs with `|r-s|` bounded is `O(T)`. No quantum
decorrelation assertion follows from this classical statement.

## 3. The diagonal approximation retains every odd dimension

Let `v_j` be the real rectangular Fejer approximants to the fixed
continuous `v`. Positivity and normalization of the Fejer kernel
give

$$
 \|v_j-v\|_\infty\to0,
 \quad \|v_j\|_\infty\le\|v\|_\infty,
 \quad \int v_j=\int v=\mu.
 \tag{3.1}
$$

At stage `j`, the symbols `v_j` and `v_j-v_l`, `1<=l<=j`,
form a finite list of fixed smooth symbols. The norm lemma supplies
one finite threshold beyond which, for every odd `N`,

$$
 \|Q_N(v_j)\|\le\|v\|_\infty+1/j,
 \qquad
 \|Q_N(v_j-v_l)\|
 \le\|v_j-v_l\|_\infty+1/j.
 \tag{3.2}
$$

Increasing that threshold preserves all these inequalities. Requiring
`n_j>=2j+3` and `n_j>n_(j-1)` gives a finite increasing integer
sequence. For every sufficiently large odd `N`,

$$
 j(N)=\max\{j:n_j\le N\}
 \tag{3.3}
$$

exists and is finite. It tends to infinity along all odd `N`:
for fixed `J`, every odd `N>=n_J` has `j(N)>=J`.
Some stage intervals may contain no odd integer; that does not
discard any dimensions or affect this conclusion.

For `B_N=Q_N(v_(j(N)))`, equation (3.2) gives a uniform norm
bound and, for each fixed `l`,

$$
 \limsup_{N\ {\rm odd}}\|B_N-Q_N(v_l)\|
 \le\|v-v_l\|_\infty.
 \tag{3.4}
$$

The inequality `N>2j(N)` prevents a nonconstant Fourier
frequency of `v_(j(N))` from aliasing to zero. It follows that
`N^(-1)Tr B_N=mu` exactly. Only finitely many initial matrices
need separate definitions, and they do not affect any limit.

No threshold depending on an arbitrary local test `b` is needed
here. Later test-specific arguments use the already constructed
universal displacement estimate, rather than building a new
diagonal sequence for each test.

## 4. Uniform QE does not transport a varying symbol

For `V_N(s)=exp(isB_N/N)U_N`, unitarity and the uniform norm
bound give

$$
 \sup_s\|V_N(s)-U_N\|\le C/N.
 \tag{4.1}
$$

For each fixed integer `r`, telescoping powers gives
`sup_s ||V_N(s)^r-U_N^r||<=|r|C/N`, also for negative
powers. Hence the already verified Egorov statement for a
**fixed** smooth `a` transfers uniformly in `s` to `V_N(s)`.

Let `a` have mean zero, and fix a time-average length `T`.
For every orthonormal eigenbasis of `V_N(s)`, diagonal
expectations of its quantum time average equal those of `Q_N(a)`.
The diagonal Hilbert--Schmidt inequality therefore gives

$$
 \limsup_N\sup_{s,\mathcal E}\frac1N
 \sum_{\psi\in\mathcal E}|\langle\psi,Q_N(a)\psi\rangle|^2
 \le\left\|\frac1T\sum_{r<T}a\circ\Psi^r\right\|_2^2.
 \tag{4.2}
$$

At fixed `T`, all observables and their finite iterates are fixed
smooth functions. The operator errors tend to zero before `T`
is allowed to grow. Equation (2.5) then makes the right side
arbitrarily small.

Now fix `l`, use `a=v_l-mu`, and apply the normalized
`ell^2` triangle inequality to diagonal expectations:

$$
 q_N^{1/2}\le
 \sup_{s,\mathcal E}
 \left(\frac1N\sum_{\psi\in\mathcal E}
  |\langle\psi,Q_N(v_l-\mu)\psi\rangle|^2\right)^{1/2}
 +\|B_N-Q_N(v_l)\|.
 \tag{4.3}
$$

The first term tends to zero for fixed `l`; the limit superior of
the second is at most `||v-v_l||_infty`. Sending `l` to infinity
last proves `q_N->0`. At no point is `v_(j(N))` inserted into
Egorov. Its possibly diverging derivative seminorms are therefore
irrelevant to this step.

The supremum over eigenbases is legitimate even at degeneracies:
the Hilbert--Schmidt inequality applies to every orthonormal basis,
and time averaging preserves the diagonal in every eigenvector.

## 5. Eigenangle motion through degeneracies

The path is analytic in the real parameter for each fixed `N`.
Local cuts outside the finite unitary spectrum give smooth
Hermitian logarithms. Their ordered eigenvalues are locally
Lipschitz and can be glued, using permutations and integer shifts,
to absolutely continuous real eigenangle branches on `[0,1]`.
A finite covering suffices for each fixed dimension; no uniform
spectral gap or uniform choice of cuts is required.

The first-order compression formula remains valid at repeated
eigenvalues. One way to justify it without differentiating an
arbitrary choice of eigenvectors is to use a local Hermitian
logarithm `H(s)`. Inside an eigenspace at `s_0`, its first-order
eigenvalue displacements are the eigenvalues of
`P H'(s_0)P`: write its block matrix relative to `P` and its
complement, and eliminate the complement with its fixed nonzero
gap at that parameter; the correction from off-diagonal blocks is
`O((s-s_0)^2)`. Differentiating the exponential of the logarithm
shows that this compression equals `P B_N P/N` in radians.
At almost every parameter the continued branches are differentiable,
and their slopes can consequently be represented as

$$
 \theta_j'(s)=\frac1{2\pi N}
       \langle\psi_j(s),B_N\psi_j(s)\rangle
 \tag{5.1}
$$

in an eigenbasis diagonalizing the indicated compressions.
The uniform QE bound covers exactly this basis.

The bounded generator controls every individual angle speed by
`C/(2pi N)`. Cauchy--Schwarz in the `N` eigenstates gives

$$
 \sup_{s\le1}\sum_j
 |\theta_j(s)-\theta_j(0)-s\mu/(2\pi N)|
 \le\frac{\sqrt{q_N}}{2\pi}\to0.
 \tag{5.2}
$$

After centering, each microscopic displacement is bounded by one
fixed constant. This proves the precise matching needed below.
It does not prove the largest centered microscopic displacement
tends to zero, nor is that stronger conclusion used.

## 6. The local-law comparison is unconditional

Let the matched, centered phase differences be `epsilon_j`, and
put `eta_N=sum_j |epsilon_j|->0`. Scalar centering is absorbed
exactly by the uniform origin, so both endpoint laws are unchanged.
For every `f` in `W^(1,1)(R)`, positivity of the absolute summands
and the exact `alpha,ell` change of variables give

$$
\begin{split}
&\mathbb E_\alpha\sum_{j,\ell}
 |f(N(\theta_j+\epsilon_j-\alpha+\ell))
       -f(N(\theta_j-\alpha+\ell))|\\
&\qquad=\frac1N\sum_j
  \|f(\cdot+N\epsilon_j)-f\|_1
 \le\|f'\|_1\eta_N.
\end{split}
\tag{6.1}
$$

For nonnegative compact smooth `f`, the function `exp(-x)` is
1-Lipschitz on `[0,infinity)`. Thus

$$
 |\mathbb E e^{-\langle f,\Xi_N^1\rangle}
  -\mathbb E e^{-\langle f,\Xi_N^0\rangle}|
 \le\|f'\|_1\eta_N\to0.
 \tag{6.2}
$$

Nothing in (6.1)--(6.2) assumes `H_diag`, a limiting law, or a
uniform moment of order greater than one.

To justify the metric statement directly, take a countable smooth
compactly supported family generating the vague topology and its
usual bounded metric

$$
 d(\xi,\zeta)=\sum_{r\ge1}2^{-r}
       \min(1,|\langle f_r,\xi-\zeta\rangle|).
 \tag{6.3}
$$

Equation (6.1) makes every summand of `E d` tend to zero, and
the summable geometric weights allow dominated convergence.
The bounded-Lipschitz distance between the laws is at most this
coupled expected distance. They therefore have the same weak
subsequential limits, whenever such limits exist. Exact intensity
one also supplies local tightness, but is not needed to manufacture
higher moments for this bounded-observable argument.

## 7. Higher moments enter only under one full H_diag hypothesis

This is logically separate from Section 6. Suppose one endpoint
satisfies the full criterion. For each fixed compact interval `I`,
an admissible nonnegative bandlimited Schwartz function `beta`
can be chosen with `beta>=c_I>0` on `I`: the inverse Fourier
transform of a compact smooth bump with nonzero integral is
nonzero near the origin, and its squared modulus can be dilated,
translated, and rescaled. Its supremum can be made less than one.

Its periodized weights `w_j` lie in `[0,1]` for sufficiently
large `N`, independently of the spectrum. Put `Z=sum_j w_j`.
The nonnegative full-periodization sum gives
`Z>=c_I Xi_N(I)`. Expanding `Z^p` by distinct labels, and
using `w_j^d<=w_j`, gives

$$
 Z^p\le\sum_{r=1}^p r!S(p,r)e_r(w_1,\ldots,w_N).
 \tag{7.1}
$$

The assumed criterion supplies bounded expectations of each
`e_r` for `2<=r<=p`; the first moment is exact. The finite
CUE upper bound supplies the corresponding numerical bounds.
Thus all fixed local count moments of the source endpoint are
bounded. Finitely many small odd `N` can be included by increasing
the constants.

The matching from Section 5 has `N|epsilon_j|<=C` and holds
pointwise for each common origin. Therefore

$$
 \Xi_N^{\rm target}(I)
 \le\Xi_N^{\rm source}(I+[-C,C]).
 \tag{7.2}
$$

This transfers all these moments to the target. Stationarity under
real translations follows exactly from uniformity of `alpha`, so
the constants are uniform over interval translates. For any
Schwartz `b`, the sequence
`c_n=sup_[n,n+1] |b|` is summable. Minkowski's inequality for
partial sums, followed by monotone convergence, yields

$$
 \sup_N\mathbb E\langle |b|,\Xi_N^0+\Xi_N^1\rangle^p<\infty
 \quad\text{for each fixed }p.
 \tag{7.3}
$$

For the required nonnegative test `b`, write its two periodized
weight arrays as `w^0,w^1`, let
`D=sum_j|w_j^1-w_j^0|` and `S=sum_j(w_j^0+w_j^1)`.
Telescoping the distinct-label products gives the correctly
normalized bound

$$
 |e_k(w^1)-e_k(w^0)|
 \le\frac{D S^{k-1}}{(k-1)!}.
 \tag{7.4}
$$

Equation (6.1) gives `E D<=||b'||_1 eta_N`. On `S<=R`,
use that bound; on `S>R`, use `D<=S` and the moment of order
`k+1` from (7.3). The expectation in (7.4) is at most

$$
 \frac{R^{k-1}\|b'\|_1\eta_N+C_{k+1,b}/R}{(k-1)!}.
 \tag{7.5}
$$

Taking `N` to infinity first and then `R` to infinity proves
the required factorial-moment difference tends to zero. The
matching is symmetric, so the implication reverses if the other
endpoint is the one assumed to satisfy `H_diag`.

Thus there is no hidden all-order uniform-integrability hypothesis:
the required moments are actually obtained from the assumed full
criterion. A lone pair estimate would not suffice for this step,
and the proof does not say otherwise. The equivalence concerns
the entire criterion; it does not assert equality of every
individual possibly unbounded moment without either endpoint
satisfying that criterion.

## 8. Canonical positive quantization: signs, bounds, and norm comparison

Let `rho_N=|varphi_N><varphi_N|` for the centered indicator packet
of length `2L_N+1`, `L_N=floor sqrt(N)`. The finite Weyl
expansion of `rho_N` and character orthogonality give exactly

$$
 \sum_{u,v}T_N(u,v)\rho_NT_N(u,v)^*=NI.
 \tag{8.1}
$$

Hence

$$
 Q_N^+(a)=\frac1N\sum_{u,v}
 a(-u/N,v/N)T_N(u,v)\rho_NT_N(u,v)^*
 \tag{8.2}
$$

is positive and unital. Order bounds prove
`||Q_N^+(a)-Q_N^+(c)||<=||a-c||_infty` for real continuous
symbols; this assertion needs no Weyl boundedness theorem on
`C^0`.

The sampling signs in (8.2) were independently reconstructed.
Put `eta=(v,u)` and `kappa=(k,l)`. The Fourier sample is
`e_N(-ku+lv)=e_N(-omega(eta,kappa))`. Conjugation of a
Weyl mode `W_lambda` by `T_N(u,v)` multiplies it by
`e_N(omega(eta,lambda))`. The finite sum selects
`lambda=kappa` modulo `N`. Consequently

$$
 Q_N^+(e_\kappa)=\chi_N(\kappa)W_N(\kappa),
 \qquad
 \chi_N(\kappa)=\langle\varphi_N,W_N(\kappa)^*\varphi_N\rangle.
 \tag{8.3}
$$

The products `chi_N(kappa)W_N(kappa)` are independent of
the choice of integer lift, since the alias signs occur twice.

For every fixed `k,l`, the packet overlap has no wraparound for
large `N` and loses at most `|l|` sites. The modular-half sign
is removed exactly by the definition of `W_N`, leaving the real
midpoint phase. On the overlapping interval that midpoint has
absolute value at most `L_N`. Therefore

$$
 |1-\chi_N(k,l)|
 \le\frac{|l|}{2L_N+1}+\frac{2\pi|k|L_N}{N}\to0.
 \tag{8.4}
$$

Finite Fourier summation proves `||Q_N^+(a)-Q_N(a)||->0`
for every fixed polynomial. For fixed `l`, insert `v_l` between
the actual diagonal generator and the continuous target:

$$
 \limsup_N\|B_N-Q_N^+(v)\|
 \le2\|v-v_l\|_\infty.
 \tag{8.5}
$$

Sending `l` to infinity proves an actual operator-norm `o(1)`
comparison. Both generators are self-adjoint, so the unitary
Duhamel formula gives

$$
 \|e^{iB_N/N}U_N-e^{iQ_N^+(v)/N}U_N\|
 \le\frac{\|B_N-Q_N^+(v)\|}{N}=o(N^{-1}).
 \tag{8.6}
$$

The canonical endpoint also satisfies the direct spectral argument
of Sections 4--7. Its norm is bounded by `||v||_infty` and
its operator-norm approximation by every fixed `Q_N(v_l)`
has limit superior at most `||v-v_l||_infty`. Centering by
`mu=int v` is legitimate even though its normalized trace is
only asymptotic to `mu`: the fixed-symbol QE approximation
already controls that scalar difference. The exact trace formula
is the continuous Riemann sum, as stated in the source.

This avoids assuming an unproved spectral perturbation principle
for the canonical endpoint. Its matrices are actual unitaries;
no analytic kernel for merely continuous `v` is claimed.

## 9. Compatibility with the root note's analytic thresholds

This part audits the diagonal selection, not the derivation of
the fixed-stage analytic estimates. Suppose the root note's
Sections 2--4 have supplied, for each fixed `v_j`, positive
`h_j`, finite `C_j`, and finite analytic-shift norm `ell_j`.
They are the explicit input in its Section 5.

At stage `j`, increase `n_j` until all of the following hold
for every odd `N>=n_j`:

$$
 h_N\le h_j,
 \quad C_j h_N\le1/j,
 \quad h_N\ell_j\le1/j,
 \quad N>2j,
 \tag{9.1}
$$

together with all the finitely many norm inequalities (3.2) and
the fixed-stage graph neighborhood threshold. Each is an eventual
condition for one fixed stage, so their finite maximum is still
a valid finite threshold. Strictly increasing thresholds can
then be chosen inductively. No lower bound on the amount of
time spent at each stage is needed.

The root target is the single fixed continuous real function
`v=-(sigma circ Psi^(-1))/(2pi)`. Uniform Fejer approximation
and the fixed-stage graph remainder give, on the selected full
odd-dimensional sequence,

$$
 \sup_x\left|
 \frac{\widetilde\gamma_N(x)}{\gamma_0(x)}-1\right|
 \le h_N\epsilon_N,
 \qquad
 \epsilon_N=2\pi\|v_{j(N)}-v\|_\infty+1/j(N)\to0.
 \tag{9.2}
$$

For any positive integer `m`, telescoping a product whose
factors have deviations bounded by `h_N epsilon_N` gives

$$
 \left|\prod_{r<m}(1+z_r)-1\right|
 \le e^{m h_N\epsilon_N}-1.
 \tag{9.3}
$$

For every fixed `B`, `m<=BN` bounds the last expression by
`exp(B epsilon_N/(2pi))-1`, which tends to zero. The same
already chosen sequence works for all fixed `B`; it is
unnecessary to select a new threshold for each `B`. The common
graph bounds, if supplied uniformly for every positive iterate
at each fixed-stage threshold as stated in the analytic part,
also survive this diagonal choice without a new time-dependent
condition.

Additional countably many eventual fixed-stage requirements may
be included by imposing only their first finitely many at each
stage. This does not require simultaneous control of all
derivatives, all bands, or all moment orders. The QE and local-law
proofs use fixed probes after the sequence is selected, and the
moment transfer follows from the universal matching estimate.

The feared incompatibility between spectral thresholds and analytic
thresholds is therefore absent. Increasing thresholds improves
both sets of eventual estimates; no estimate demands a conflicting
upper bound on `N`.

## 10. What remains unproved

The audited argument establishes the unconditional local-law
comparison and the full-criterion equivalence. It does not supply
a model endpoint with known sine statistics.

Even after the root note's analytic construction is separately
accepted, the bound (9.3) is an orbitwise relative error. Summing
its absolute value over exponentially many periodic points is
not a small error on the time scale `m` comparable to `N`.
The complete signed error sum remains uncontrolled.

In particular, for the original exact family, the first fixed-test
estimate remains

$$
 \frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
 \left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)=o(1),
 \tag{10.1}
$$

with the original explicit admissible bump-square `b_*`. No
passage audited here proves (10.1), gives a fixed-test
countersequence, or allows the assumed one-endpoint `H_diag`
from Section 7 to be used as an unconditional fact.

No old source or either audited manuscript was edited by this
auditor. This report contains an independent mathematical audit;
no numerical spectral test is used as an asymptotic premise.
