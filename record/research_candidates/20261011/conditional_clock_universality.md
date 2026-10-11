# Conditional matrix-clock universality under random Schur elimination

**VERIFICATION-PENDING.** Candidate continuation of BGS-TRACE-055.
Finite word identities do not certify the stopped asymptotic moment induction.
The all-time entry-flat event and microscopic cavity identification are unproved.


8 October 2026. Research theorem candidate outside the repository. The all-time entry-flatness premise is separate and unproved here. The finite-order bootstrap below is being independently audited. The previously audited conclusions through the fourth trace moment are recorded in fourth_delay_law.md. No external novelty or BGS solution is claimed.

## Exact setting and proposed theorem

Start with F_N(z)=zU_N, deterministic unitary U_N. Eliminate coordinates in an independent uniform order, using their original independent uniform phases. At retained size u, let S_u=F_u(1), incoming delay T_u=F_u(1)*F_u'(1)≥I and outgoing delay Q_u=S_uT_uS_u*. Let ell=log(2N), fix kappa>0, m=ceil(ell^(1+kappa)), m<N, and let A be all-time entry flatness max|S_u,ij|²≤K ell/u for u≥m.

For each fixed L there is a deterministic epsilon_N→0 such that

P(A intersect {some u≥m violates any of the following bounds})→0:

max_j |(u/N)^r(T_u^r)_jj−f_r(u/N)|≤epsilon_N,
max_j |(u/N)^r(Q_u^r)_jj−f_r(u/N)|≤epsilon_N,
max_(j≠k) [(u/N)^r |(T_u^r)_jk|+(u/N)^r |(Q_u^r)_jk|]≤epsilon_N,
max_(j,k) (u/N)^r |(S_uT_u^r)_jk|≤epsilon_N,             (1)

for every 1≤r≤L. Constants depend on the fixed L,kappa,K, not on N. The same original phases are used throughout; no future good event is conditioned upon.

The reference moments f_r(x), x=u/N, are defined by f_1=1 and the triangular evolution, with tau=−log x,

d_tau f_r=−(r−1)f_r+r [z^r]{−log(1−M(z,tau)²)},
M(z,tau)=sum_(r≥1) f_r(exp(−tau))z^r,  f_r(1)=1.        (2)

The coefficient on the right uses only orders below r. In particular

f_2=2−x,
f_3=6−6x+x²,
f_4=22−32x+12x²−x³,
f_5=90−170x+100x²−20x³+x⁴.

At m/N→0, the proposed theorem identifies every fixed moment of H_m=mT_m/N with the large Schroeder numbers 1,2,6,22,90,... and hence its empirical measure with

rho(h)=sqrt((b−h)(h−a))/(2 pi h²),   a=3−2sqrt(2), b=3+2sqrt(2),        (3)

on [a,b]. To infer an actual convergence-in-probability law one must separately prove P(A^c)→0. There is no endpoint intensity-gap assumption for this clock theorem. Clock spectral universality does not imply universality of the eigenphases of DU_N.

## 1. Closed high-moment input and stopping

The exact congruences, Jensen argument and noncommuting word bound in all_moment_delay_bootstrap.md prove that, under a joint first-diagonal stop, every fixed killed normalized trace moment has bounded expectation. For any fixed sufficiently large p and zeta=1/4, cap

M_p(u)=u^(p−1)Tr T_u^p/N^p ≤ B_u=B(u/m)^zeta,
B=ell^b, b>0 fixed.

The cap-exit probability before the other stops is O(C_p/B), not O(log N/B). All crossing states are retained in frozen martingales; only separate moment expectations are killed. Additional entry/power barriers can be included in the stop because they only lower the killed quantities. Choose p after L, and keep it fixed in the N→infinity limit.

On this cap put H=uT/N, V=uQ/N and R_p(u)=1+(uB_u)^(1/p). Then ||H||=||V||≤R_p(u). This bound is deliberately crude. It permits the use of higher diagonal moments without assuming their concentration before their induction stage.

## 2. Base matrix entries, including off-diagonal delay entries

The first input/output diagonals have the already proved local version of the joint bootstrap. Its noise and bias accumulated down to a current size u are bounded by

C[sqrt(ell B^(1/p)m^(−zeta/p) log(2u)/u^((p−1−zeta)/p))
 +sqrt(ell/u)log(2u)+ell/u].                            (4)

This follows by summing only blocks above the current u in the same martingale event.

For j≠k, the exact one-step first-clock formula is

T'_jk=T_jk+q T_je S_ek+conj(q)conj(S_ej)T_ek
             +T_ee |q|² conj(S_ej)S_ek.                (5)

Its phase mean replaces |q|² by (1−|S_ee|²)^−1. Averaging e and using column orthogonality, the forcing after normalizing uT/N is O((epsilon_1(u)+delta_u)/u), apart from the negative scaling drift −(1+O(1/u))H_jk/u. Omitting e=j,k costs O(delta_u/u); varying T_ee/(N/u) from 1 costs epsilon_1(u)/u, because sum_e |S_ej S_ek|≤1. The outgoing proof uses row orthogonality.

The increment variance and jump have the same bounds as the first-diagonal proof. A stable constant supersolution for the drift error and a union bound on v² live pairs prove the off-diagonal base case. It is important that H need not converge to I in Hilbert–Schmidt norm: each individual off-diagonal goes to zero while the aggregate of their squares can remain order u.

For Gamma=S T, the exact identity

Gamma'_jk=Gamma_jk+q(S_je Gamma_ek+S_ek Gamma_je)+q²S_je S_ek Gamma_ee

gives a compressed complex martingale. Its normalized drift is negative and its variance is the first-clock variance, so all of its entries obey the same local envelope. This completes the r=1 case of (1).

## 3. Finite-word induction lemma

Fix k≥2. Assume (1) through order k−1 with a size-dependent error envelope E_(k−1)(u), and stop the order-k input/output diagonals before exceeding a fixed bound C_k=max_(x∈[0,1])f_k(x)+2. Define the order-k errors by subtracting f_k(u/N)I from H^k and V^k and using S H^k for the mixed family. Before this enlarged stop, there are constants depending only on k such that:

(a) The conditional drift of the order-k incoming/output errors consists of a diagonal scaling coefficient −k/u+O(1/u²), the transport of their own diagonal errors by conjugation with S with coefficient 1/u+O(1/u²), and lower-order forcing. In the entrywise maximum norm the absolute transport row sum is ≤1+O(delta_u). Thus its homogeneous update contracts live rows by at least (k−1)/(2u) eventually. The mixed errors have coefficient −k/u+O(1/u²), no own-diagonal transport, and lower-order forcing.

(b) The lower-order and reference drift error is bounded by

C_k [E_(k−1)(u)+sqrt(delta_u)] R_p(u)^(2k)/u + C_k/u².    (6)

(c) Every centered real or imaginary entry increment has

variance≤C_k[ell R_p(u)^(2k)/u²
             +E_(k−1)(u)² R_p(u)^(2k)/u+1/u²],
jump≤C_k[sqrt(delta_u)+E_(k−1)(u)]R_p(u)^k+C_k/u.        (7)

The top-order diagonal cap controls top-order off-diagonals by positivity, and controls mixed entries by |(S H^k)_ij|²≤(V^k)_ii(H^k)_jj. No off-diagonal concentration at order k is assumed in proving the increment estimates.

### Proof by orientation and degree

The exact formulas are

T'^k=K* T(R_w T)^(k−1)K,
S'T'^k=J* S T(R_w T)^(k−1)K,
R_w=I+qev*+conj(q)ve*, v=S*e.

Each term is a finite cyclic or open rank-one word, with positive powers of T between rank-one factors and total clock degree k. At a=0, phase averaging retains only balanced numbers of q and conjugate q. At |a|≤sqrt(delta_u), fixed-degree balanced moments differ from their a=0 values by O(delta_u); unbalanced moments are O(sqrt(delta_u)). These statements follow directly from convergent geometric series, uniformly at |a|≤1/2.

Adjacent identical orientations yield a diagonal mixed moment (S H^r)_ee or its conjugate with r<k. Such a word is an error by induction. Alternating orientations have internal diagonal moments of H or V. Replace those moments by the deterministic lower-order f_r, accumulating the first term in (6). The retained endpoint sums over e then reduce by unitarity to a lower power H^r or V^r, or to a lower mixed power S H^r. Excluding the retained endpoints e=j,k costs entry-flatness terms or lower off-diagonal errors.

In the incoming/output formula, the sole term involving an unknown diagonal moment of order k is the word with no interior rank-one insertions and both boundary K terms. It is conj(S_ej)S_ek (H^k)_ee. Its averaged transport has absolute coefficient sum at most sum_e |S_ej S_ek|≤1. All other scalar moments have order at most k−1. In the mixed formula the two boundary terms have net phase q², so this prospective top-diagonal word averages to zero; other surviving words reduce to lower mixed powers. This establishes the top-order stability in (a).

For any error-word endpoint product, Cauchy–Schwarz over e gives a higher diagonal moment at the retained endpoint. Such a moment of degree ≤2k is bounded by R_p(u)^k times the stopped order-k diagonal bound when it exceeds k, or by a bounded lower diagonal moment when it does not. This proves the coarse R_p(u)^(2k) allowances in (6) without demanding new higher-order diagonal concentration.

For (7), the terms with no interior insertion and one boundary phase have a factor S_ej or S_ek; uniform-coordinate averaging and row/column norm identities give the first variance term. Every term with an interior insertion has a retained-to-eliminated endpoint factor of a lower clock or mixed power, hence an off-diagonal lower clock entry or a lower mixed entry. Bound that factor by E_(k−1)(u); square and sum the other endpoint over e, using the same higher-diagonal Cauchy–Schwarz bound. This gives the second variance term. The scaling/deletion/reference increments contribute C_k/u². Cross terms between different words are bounded by the finite word count and Cauchy–Schwarz, so no phase-monomial independence is assumed. The jump bound follows from the same factors and |q|≤2.

### Identification of the constant forcing

In a trace word, every surviving alternating cycle with 2q rank-one factors has product of 2q scalar moments. Summing its positive gap compositions n_i≥1, sum n_i=k, gives coefficient k/q: the cyclic placement factor k/(2q) and two alternating orientations. Thus the normalized mean trace increment, before the deterministic normalization, has main polynomial

k sum_(q=1)^floor(k/2) (1/q) sum_(n_1+...+n_(2q)=k) product_i f_(n_i)
 = k [z^k]{−log(1−M(z)^2)}.                            (8)

Every nonalternating cycle contains a lower mixed diagonal and is negligible. The same lower-matrix reductions in the diagonal drift must therefore supply the constant (8); the unknown top-diagonal transport has total trace equal to the top trace. Equivalently the ideal diagonal equation is −(k−1)f_k plus (8). This identifies (2), without assuming that finite matrices with all ideal moments exactly exist.

## 4. A local envelope closes all fixed orders

Take D_1=8 and D_k=D_(k−1)+4k+4. For each fixed L choose p large enough that D_L(1+zeta)/p<1/8 and 2D_L(1+kappa+b)/p<kappa/4. Enlarge p if required for the fixed lower-moment variance bookkeeping. It remains fixed.

An admissible coarse envelope is

E_k(u)=C_(k,p)[sqrt(ell/u) R_p(u)^(D_k)(log(2u))^(k+3)
                    +ell/u R_p(u)^(D_k)].             (9)

With p as chosen, it decreases geometrically as u increases, up to harmless logarithmic factors. It dominates the base envelope (4). Before the first exit of any of these envelopes, (6) is bounded by C E_k(u)/u with an arbitrarily large constant margin available in C_(k,p). The stable live-row maximum principle absorbs the forcing; frozen rows are identities and cause no accumulation of the deterministic error.

Conditionally on the starting history of a block [v/2,v], Freedman applied to (7) and a union over O(v²) live entries controls its raw noise at cost

C_k R_p(v)^k log(2v)[sqrt(ell/v)+E_(k−1)(v)].             (10)

The event probability can be made O(v^(−r0−3)) with any fixed r0. The exponents D_k and the logarithm in (9) dominate (10) and the drift error with spare powers. The pathwise block decomposition avoids future-dependent martingale transforms. Summing only blocks above a current u gives (9); the power decay prevents an N/m factor. The frozen-label references f_k(u/N) have O(1/u²) residuals in their conditional drift, since f_k is a fixed smooth polynomial and the deletion probability is included.

At the endpoint,

E_L(m)≤C ell^(−kappa/2+D_L(1+kappa+b)/p)(log ell)^(L+3)+o(1)→0.

The cap exit has probability O(C_p ell^−b); the summed entry martingale exceptions are O(m^−r0). A first additional power or mixed-envelope exit must therefore lie in these exceptional events on A. This closes (1) for every fixed L. At no step are the phase averages conditioned on A or on future survival.

## 5. Algebraic moment transform and empirical clock law

Writing x=exp(−tau), the generating series defined by (2) satisfies

partial_tau M=M+z partial_z M[−1+2M/(1−M²)],
M(z,0)=z/(1−z).

Solving characteristics gives

z=M(1−M)/[(1+M)(1−xM)],
(1−xz)M²−[1−(1−x)z]M+z=0.                            (11)

This is a formal-power-series identity and also analytic near z=0. At x=0,

M(z,0-depth)= [1−z−sqrt(1−6z+z²)]/2.

Its coefficients are the large Schroeder moments. The corresponding Stieltjes transform is

G(w)= [3w−1−sqrt(w²−6w+1)]/(2w²), G(w)~1/w at infinity,

whose density is (3). The square-root branch is chosen positive at large positive w. The moments grow at most exponentially, so they determine a unique compactly supported probability measure. Convergence of every fixed empirical clock moment, together with the first-moment tightness, therefore gives weak convergence in probability once P(A^c)→0. This assertion concerns the positive matrix mT/N; it has no implication that S or DS has a Haar/CUE eigenphase law.

## Audit status

The higher-order finite-word induction lemma and its envelope closure are the outstanding audit obligations for this candidate. The exact second through fourth identities and the first-power cross-clock were independently checked earlier; that does not certify the general induction. The all-time flatness probability is an external unresolved input even if this induction passes.
