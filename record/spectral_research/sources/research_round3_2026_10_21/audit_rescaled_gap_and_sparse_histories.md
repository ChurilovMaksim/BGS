> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round3_2026_10_21/audit_rescaled_gap_and_sparse_histories.md`. Embedded SHA256: `3dc9d2822133c2b6108216834f36d8e29801fdad9332bf05088f095a11b6f950`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: rescaled arithmetic escape and sparse character histories

Date: 21 October 2026.

## 0. Exact snapshots and verdict

The following source snapshots were read and their critical estimates
reconstructed directly:

- arithmetic_comb_rescaled_gap.md, SHA-256
  898528107bfc2691c0f17fe6d8a096592c46de537b045c6bbc41949d0f3bfd2f.
  This includes Section 3.1 on every input/output character pair.
- phase_sparse_character_histories.md, SHA-256
  33e39b8eca7f331db2bf78671d57d60cdebf18c1c3702cf7734da01de663a761.
- The exact finite-word derivation in audit_quartic_commutator_word.md,
  SHA-256 ac9afae71b2c9ad15bc00b4a2b98da25473131bcff15072432c605060b4118c6,
  was checked at the stage before imposing $N\delta^4=1$.
- The translated-kick estimate used below is independently derived in
  audit_phase_logtime_dispersion.md, SHA-256
  f806c3b85c026b11535f7dae1513171ddbba4df52a3c76075883dd0a8b8d92e2,
  auditing its primary source
  phase_logtime_dispersion_and_missing_modes.md, SHA-256
  40dd41555520f712b99f7467ed14fd41ff0369db4b44a9b78f21c7f5a8314b4b.

**Verdict:** no load-bearing gap was found in either new claim.
For the actual fixed $\tau=10^{-80}$, the enlarged auxiliary lattice
step gives the uniform numerical escape $1/64$.
The same bound holds for every input/output character pair.
The sparse-history argument removes, with its full signed cross-term,
all histories with at most a fixed positive density of deviations
from the unperturbed character permutation. The remaining coherent
trace sum is not evaluated.

The two scale parameters must be distinguished. Here
$h=(2\pi N)^{-1}$, $t=\tau/(2\pi)$ in the word proof.
The dispersion source uses $h_{\rm WKB}=N^{-1}$.
All conversions below preserve these factors.

## 1. The word estimate at an arbitrary permitted lattice step

The exact smooth real symbol is the corrected physical symbol $a$
in the rescaling source. Let $g=\partial_q^4a$.
For $H_0=-P$, $H_1=E_h^*(-P)E_h$, the exact Fourier Heisenberg
series gives
$$
 K_h=Q_h(\partial_q^3v_h),\qquad
 \|K_h-tQ_h(g)\|\le2\cdot10^{12}t^2.
$$
This is an estimate for the actual exponential
$E_h=e^{itQ_h(a)/h}$.

The three nested group commutators form a word with 22 exponential
factors, eight involving $H_1$. Its left logarithmic generator has
Taylor polynomial $4u^3K_h$, and bounded remainder
$10^{20}|t|u^4$, for $0\le u\le1$.
In the proof, $h$ and $t$ remain fixed while $u$ varies.
The remainder estimate uses depth-four scaled commutators and unitary
conjugation, rather than a norm Taylor series for unbounded generators.
Unitary Duhamel comparison yields
$$
 \|C_3(\delta)-e^{i\delta^4K_h/h}\|
 \le\frac{10^{20}|t|\delta^5}{5h}.
$$
No relation between $h$ and $\delta$ has been used yet.

If $N\delta$ is an integer, the endpoint word and its comparison
operator are decomposable in the explicit continuous Zak fibers.
The finite odd torus matrix is the trivial fiber. The line norm bound
holds on almost every fiber and then on every fiber by continuity.
Intermediate real values of $u$ need not preserve that fiber.
This point excludes an invalid restriction of a line estimate to
distributional combs.

Put $\gamma=\tau N\delta^4$. Subtracting the two self-adjoint
generators in the bounded exponential, and applying unitary Duhamel,
gives exactly the upper bounds
$$
 \frac{\delta^4}{h}\,2\cdot10^{12}t^2
 =\frac{10^{12}}{\pi}\gamma\tau,\qquad
 \frac{10^{20}|t|\delta^5}{5h}
 =\frac{10^{20}}5\gamma\delta.
$$
Consequently the looser displayed source bound
$$
 \|C_3(\delta)-e^{i\gamma Q_N(g)}\|
 \le10^{12}\gamma\tau+10^{21}\gamma\delta
$$
is valid. Crucially, there is no $\gamma^2$ error.
The bounded exponential has been retained exactly.
Nothing here expands the original $\tau N$ in operator norm.

## 2. Independent coefficient and numerical checks

Writing $\cos j=\cos(2\pi jq)$ and similarly for sine, the purely
cosine coefficients of $a$ are
$$
 (C_1,C_6,C_7,C_8)=(1/10,-1/20,9/10,-1/20).
$$
The identity
$$
 r(q)\sin(2\pi q)
 =\sin1+\tfrac12(\sin2+\sin6-\sin8)
       +\tfrac14(\sin5-\sin9)
$$
follows by expanding
$r=1+\cos1-\cos7-\frac12(\cos8+\cos6)$.
Also
$$
 r(q+1/2)=1-\cos1+\cos7-\tfrac12(\cos8+\cos6).
$$
After four $q$ derivatives, the three Fourier one-norm upper bounds,
divided by $(2\pi)^4$, are respectively
$$
 2430.6,\qquad45.015,\qquad50.98.
$$
Their sum is $2526.595=505319/200$.
Thus
$$
 \|Q_N(g)\|\le\|g\|_{\mathcal F}
 \le(505319/200)(2\pi)^4<11\cdot10^6,
$$
where even the crude bound $\pi<4$ suffices.

The modes $k=\pm7,l=0$ alone give
$$
 \sigma:=\Big(\sum|\widehat g(k,l)|^2\Big)^{1/2}
 \ge\frac9{10\sqrt2}(14\pi)^4>2\cdot10^6.
$$
The source's elementary estimates $\pi>31/10$ and
$\sqrt2<10/7$ make the latter lower bound larger than
$139694557023/62500>2\cdot10^6$.

The support of $g$ lies in $|k|\le9,|l|\le1$.
The product $Q_N(g)^*Q_N(g)$ has modes in
$|k|\le18,|l|\le2$. Character compression kills every nonzero
such mode when $d>18$; its constant mode is exactly $\sigma^2$.
Therefore, for every character,
$$
 P_\chi Q_N(g)^*Q_N(g)P_\chi=\sigma^2P_\chi.
$$
No asymptotic positivity assertion is used.

For $N=d^2m,\ m\le\sqrt N$, one has $d\ge N^{1/4}$.
Set
$$
 b_0=2\cdot10^{18},\quad
 b=\lfloor b_0dN^{-1/4}\rfloor,\quad
 \delta=b/d,\quad \gamma_N=\tau N\delta^4.
$$
The floor argument is at least $b_0$, so
$$
 \gamma_0(1-b_0^{-1})^4\le\gamma_N\le\gamma_0,
 \qquad
 \gamma_0=\tau b_0^4=1/6250000,
 \qquad
 \gamma_N\ge0.99\gamma_0.
$$
Also $N\delta=bdm$ is an integer.
For $N\ge10^{140}$,
$$
 \delta\le2\cdot10^{-17},\quad
 10^{12}\gamma_N\tau+10^{21}\gamma_N\delta
 \le1.6\cdot10^{-75}+2/625<1/250.
$$
The spectral range obeys
$\gamma_N\|Q_N(g)\|<44/25<2$.
On $[-2,2]$,
$$
 |e^{ix}-1|=2|\sin(x/2)|\ge(5/6)|x|.
$$
The finite self-adjoint spectral theorem and exact compression imply,
for every unit $v\in P_\chi$,
$$
 \|(e^{i\gamma_NQ_N(g)}-I)v\|
 \ge(5/6)\gamma_N\sigma>33/125.
$$
Hence
$$
 \|(C_3(\delta)-I)v\|>33/125-1/250=13/50>1/4.
$$

## 3. Every input/output character pair

Let $R=T_N(-bN/d,0)$, $B=E_N^*RE_N$, and take a unit vector
$v\in P_\chi$. To test an arbitrary output character $\psi$, put
$\epsilon=\|(I-P_\psi)E_Nv\|$.
If $r_\chi,r_\psi$ are the respective eigenvalues of $R$, then
$$
 (R/r_\chi)v=v,\qquad
 \|(B/r_\psi-I)v\|
 =\|(R-r_\psi)E_Nv\|\le2\epsilon.
$$
The inverse has the same residual norm.
Independent scalar multiples of $R$ and $B$ cancel in the first
group commutator, and therefore in the full nested word.
The fourteen normalized $R$ factors fix $v$; the eight normalized
$B$ factors each cost at most $2\epsilon$.
The elementary product telescoping inequality gives
$$
 \|(C_3-I)v\|\le16\epsilon.
$$
It follows that $\epsilon>13/800>1/64$, uniformly in both characters.
Thus
$$
 \sup_{\chi,\psi}\|P_\psi E_NP_\chi\|
 \le\sqrt{4095/4096}=:\rho_*.
$$
The corresponding statement for $U_N=E_NM_N$ follows because
$M_N$ permutes the character spaces exactly.

Selecting any permutation of input/output sectors consequently gives
an operator of norm at most $\rho_*$, since both input and output
blocks are mutually orthogonal. This reasoning does not bound a
noninjective selection by the same constant, and the source makes
no such claim.

The source's pure-itinerary signed estimate now follows from the
already checked exact character permutation. In particular
$$
 |\operatorname{Tr}K^n|/N
 \le\rho_*^n\min(1,\lambda^n/d^2),\quad \lambda=3+2\sqrt2.
$$
The composite-modulus fixed-point count is valid: if an integer matrix
$B$ is invertible over the rationals, the map
$x\mapsto Bx/d\bmod B\mathbb Z^2$ injects
$\ker(B\bmod d)$ into $\mathbb Z^2/B\mathbb Z^2$.
Splitting the geometric sum at
$\lfloor2\log d/\log\lambda\rfloor$ gives the source's exponent
$-2\log\rho_*/\log\lambda$ and its displayed constant.

## 4. Sparse histories: exact total operator bound

Let
$$
 K=\sum_\chi P_{\mathsf S\chi}U_NP_\chi,\quad
 R=U_N-K,\quad
 \mathsf S\chi=\chi\circ L.
$$
Then $\|K\|\le\rho_*$, $\|R\|\le1+\rho_*$.
Inserting character projections into $(K+R)^n$ shows that each
$R$ is exactly a deviation from $\mathsf S$. There is no duplication:
$K$ and $R$ have complementary sets of matrix blocks.

With $\rho=\rho_*$, set
$$
 z=\frac{1-\rho}{2(1+\rho)},\quad
 r_*=\frac{1+\rho}2,\quad
 \epsilon=\frac{-\log r_*}{2\log(1/z)},\quad
 \eta=\sqrt{r_*}.
$$
For the sum $S_n$ of every noncommutative word with
at most $\lfloor\epsilon n\rfloor$ letters $R$,
$$
 \begin{aligned}
 \|S_n\|
 &\le\sum_{j\le\lfloor\epsilon n\rfloor}
       \binom nj\rho^{n-j}(1+\rho)^j\\
 &\le z^{-\epsilon n}(\rho+z(1+\rho))^n
 =\eta^n.
 \end{aligned}
$$
Here $z^j\ge z^{\epsilon n}$ on the retained range.
The estimate has already summed every placement and every permitted
number of deviations. Hence $|s_n|:=|\operatorname{Tr}S_n|\le N\eta^n$.

## 5. Fixed-time trace smallness and the full signed sum

Finite character orthogonality gives the exact identity
$$
 \sum_\chi P_\chi E_NP_\chi
 =|G|^{-1}\sum_{g\in G}T_G(g)E_NT_G(g)^*.
$$
Consequently $K$ is an average of the unitary operators
$U_g=T_G(g)E_NT_G(g)^*M_N$, and $R$ is $U_0$ minus that average.
Each occurrence of $K$ has coefficient one-norm one in this expansion,
and each $R$ has coefficient one-norm at most two.
The complete $S_n$ therefore has coefficient one-norm at most
$\sum_j\binom nj2^j\le3^n$, independently of $|G|=d^2$.

Exact Weyl conjugation turns the Hamiltonian into the real translation
$a(q+a_g/N,p-b_g/N)$.
Its Fourier coefficient absolute values are unchanged.
The independent uniform translated-kick WKB proof gives
$$
 \max_{x,y}|(U_{g_n}\cdots U_{g_1})_{xy}|
 \le C A^n N^{-1/2}
$$
for every translation sequence, with fixed constants.
Taking traces and applying the coefficient one-norm bound yields
$$
 |s_n|\le C\sqrt N\,B^n,\qquad B=3A.
$$
This is a deterministic identity and bound, not an ensemble average.

Put $p_n=\operatorname{Tr}U_N^n$, $q_n=p_n-s_n$, and
$$
 a_{n,N}=\min(CN^{-1/2}B^n,\eta^n)\le1.
$$
Since $|p_n|\le N$, the exact square difference obeys
$$
 N^{-2}\big||p_n|^2-|q_n|^2\big|
 \le2a_{n,N}+a_{n,N}^2\le3a_{n,N}.
$$
For each fixed $n$, $a_{n,N}\to0$, whereas
$\sum_n\eta^n<\infty$. Dominated convergence therefore gives a
vanishing full signed difference uniformly over all bounded weights
with a common supremum bound. It includes the cross-term with all
retained histories.

For the claimed rate, set
$$
 \beta=\frac{-\log\eta}{2\log(B/\eta)},\qquad
 L_N=\left\lfloor\frac{\log(\sqrt N/C)}{\log(B/\eta)}\right\rfloor.
$$
Then $CN^{-1/2}B^{L_N}\le\eta^{L_N}$, and
$$
 \sum_{n\ge1}a_{n,N}
 \le\eta^{L_N}\left(\frac B{B-1}+\frac\eta{1-\eta}\right)
 \le\eta^{-1}C^{2\beta}N^{-\beta}
       \left(\frac B{B-1}+\frac\eta{1-\eta}\right).
$$
This reproduces the source's quantitative bound with its stated
floor convention. The difference series is absolutely summable for
every bounded weight. For a nondecaying weight this need not be the
difference of two separately convergent infinite sums.

## 6. Exact boundary of the result

All conclusions concern the given original matrices on the specified
odd dimensions and square divisors. The perturbation time remains
exactly $\tau N$. Rescaling changes only an auxiliary translation
used to prove the norm gap.

The sparse deletion leaves only histories with more than
$\lfloor\epsilon n\rfloor$ deviations at time $n$. The resulting
trace functional is not asserted to arise from the spectrum of another
unitary. The proof does not estimate cancellation within the retained
dense-transition class, identify its pair limit, or control higher
factorial orders. Thus it is a rigorous reduction of the pair problem,
not a proof of $H_{\rm diag}$.
