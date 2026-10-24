# All fixed correlation orders for the original coboundary chain

**Claim ID:** BGS-FLOW-017. **Status:** project proof with independent internal
review of the new implications and the stated prior reference/ergodicity inputs.
The chain is the original uncentered Gaussian coboundary chain. Nonlinear
centering is a comparison coordinate only, never an algorithmic step.
This result is about a stochastic perturbation, not deterministic BGS.

## 1. Statement and exact dependency contract

For odd $N$, let deterministic $A_N$ satisfy
$|p_1(A_N)|+|p_2(A_N)|\le K$ eventually. Use independent normalized
GUE matrices, with entry covariance $1/N$, in

$$
U_0=A_N,\qquad
U_{j+1}=\exp[i\varepsilon_N(G_j-U_jG_jU_j^*)]U_j,
\quad h_N=\varepsilon_N^4/2,\quad n_N=\lfloor t_N/h_N\rfloor.
\tag{C1}
$$

Assume $1/N\le t_N\to0$, $t_N^2\log N\to0$, and
$\varepsilon_N>0$ with

$$
N^b\varepsilon_N\to0\quad\hbox{for every fixed }b>0.
\tag{C2}
$$

Assume FLOW-014's Dyson reference theorem applies from $\Pi A_N$ at
$t_N$. Then the periodic unfolded spectrum of $U_{n_N}$ viewed from
an independent uniform origin converges to Sine$_2$, with convergence of
every fixed factorial test expectation for compact continuous or Schwartz
tests. Every fixed bounded-window count moment is uniformly bounded.

For each fixed such test, the conditional expectation over the uniform
origin for one realized chain converges in $L^2$ over the Gaussian chain
to the Sine$_2$ expectation. This is convergence in probability as well;
no almost-sure claim along the full sequence is made.

One explicit choice for the actual frozen map is
$t_N=8g_N$ from FLOW-014 and
$\varepsilon_N=N^{-\log\log N}$ for sufficiently large $N$.
This is one sequence for all fixed correlation orders. It uses
$n_N=\lfloor2t_NN^{4\log\log N}\rfloor$ steps; this is not a polynomial
step-count theorem. FLOW-014's cheaper polynomial schedule remains valid
for its original bounded Laplace conclusion.

Dependencies: FLOW-010's fixed-order fast contraction and weak expansion;
FLOW-011's dimension-uniform localized $C^6$ semigroup bound;
FLOW-012's actual-start chart and boundary layer;
FLOW-016's all-moment transport; FLOW-014's reference law;
TRACE-001's exact distinct-label trace partition identity. Spatial
ergodicity of Sine$_2$ is prior Soshnikov, Theorem 7, not a new claim.

## 2. Strengthening discrete localization to arbitrary powers

Use the stops and larger charts of FLOW-012: $|m_1|=a=1/1024$ or
$|m_2(\Pi U)|=2/5$, plus the inherited large-jump event. Write $\sigma$
for the first stop, $x_j=m_1(U_j)$, and $\rho=\varepsilon/N+\varepsilon^4$.
For every fixed integer $p\ge1$, FLOW-010 (5) and FLOW-012 (G4)--(G5) give

$$
\mathbb E[|x_j|^{2p};j<\sigma]
\le e^{-c_p\varepsilon^2j}|x_0|^{2p}+C_p\rho^{2p},
\quad
h\sum_{j<n}\mathbb E[|x_j|;j<\sigma]
\le C\varepsilon^2|x_0|+Ct\rho.
\tag{C3}
$$

For the frozen stopped variable, drop the negative drift in that same
one-step inequality, rather than summing a union bound on the initial
term. For $p\ge2$ this proves

$$
\mathbb E|x_{n\wedge\sigma}|^{2p}
\le|x_0|^{2p}+C_pn\varepsilon^2\rho^{2p}
\le C_{p,K}N^{-2p}
+C_p(t+1)(\varepsilon^{2p-2}N^{-2p}+\varepsilon^{8p-2}).
\tag{C4}
$$

On a first-trace exit $|x_{\sigma}|\ge a$, so divide this bound by $a^{2p}$.
This reasoning is unchanged if another stopping condition occurs first.

For a centered second-trace exit use a nonnegative smooth extension of
$F_r(Y)=|p_2(Y)|^{2r}$ that agrees on the larger chart, in particular
through good overshoots with $|m_2|\le9/20$. As in FLOW-010's
extension for $r=1$, $\|F_r\|_6\le C_rN^{2r}$ and its sup norm has the
same bound. On $|m_2|\le1/2$, (T10) and Itô imply

$$
\overline LF_r\le
-\frac{16r}{25}|p_2|^{2r}
+\frac{300r}{N}|p_2|^{2r-1}
+128r^2|p_2|^{2r-2}\le C_r.
\tag{C5}
$$

The negative coefficient $16/25$ is a weakening of $3/4$ valid in this
region. Only pre-exit points with $|m_2|<2/5$ use the generator bound;
no bound is asserted along the entire globally localized diffusion.
The bracket coefficient is deliberately enlarged: writing $p_2=X+iY$,
the Hessian's maximum eigenvalue is at most $4r^2|p_2|^{2r-2}$, and
$\overline\Gamma(p_2,\bar p_2)\le64$. The negative leading term absorbs
the remaining powers, uniformly in $N\ge3$. At $p_2=0$ this has the
usual polynomial interpretation, including $r=1$.

Apply FLOW-010 (8) up to the stop, use (C3) and
$|p_2(\Pi A_N)|\le C_K$. Positivity gives

$$
\mathbb EF_r(\Pi U_{n\wedge\sigma})
\le C_{r,K}(1+t)
+C_rN^{2r+4}\{\varepsilon^2|x_0|+t(\rho+\varepsilon^2)\}.
\tag{C6}
$$

At a second-trace exit without a large jump, the chosen larger-chart
extension agrees and is at least $N^{2r}(2/5)^{2r}$. A large jump over
$O(t\varepsilon^{-4})$ steps has probability $C_L\varepsilon^L$ for any
fixed $L$, uniformly in $N$, by the inherited Gaussian estimate. Thus
(C4)--(C6) prove, for every fixed $L>0$, after choosing $p,r$ sufficiently
large, and using $0<t\le1$, $|x_0|\le K/N$, $0<\varepsilon\le1$,

$$
\mathbb P(\sigma\le n)\le
C_{L,K}(N^{-L}+N^4\varepsilon).
\tag{C7}
$$

Constants may depend on the fixed moment order. The process and stopping
chart do not. In view of (C2), this probability times any fixed power of
$N$ tends to zero. Merely retaining the previous $O(N^{-2})$ exit bound
would not suffice for all factorial tests.

## 3. Weak comparison for polynomially bounded smooth tests

Let $F_N$ be any conjugation- and scalar-rotation-invariant smooth test
with $\|F_N\|_6+\|F_N\|_\infty\le C N^b$, for a fixed $b$.
Let $Y$ be FLOW-011's full localized projected diffusion from $\Pi A_N$.
Telescope its backward semigroup. Its $C^6$ bound is $Ce^{Ct}\|F_N\|_6$,
with no exponential in $N$. FLOW-010 (8), (C3) and (C7) give

$$
|\mathbb EF_N(\Pi U_n)-\mathbb EF_N(Y_t)|
\le C\|F_N\|_\infty\mathbb P(\sigma\le n)
+CN^4\|F_N\|_6
\{\varepsilon^2|x_0|+t(\varepsilon/N+\varepsilon^2)\}.
\tag{C8}
$$

The left term denotes a bounded smooth extension on discarded paths.
One-step semigroup-time and final-rounding errors are included as in
FLOW-011 (P14); $t\ge1/N$ permits their absorption in the displayed bound.
Nothing in this telescoping requires $0\le F_N\le1$: sup norms multiply
the discarded paths and $C^6$ norms multiply the weak remainders.

Return to the uncentered terminal matrix. On $n<\sigma$, the chart has
$\|U_n-\Pi U_n\|_{\rm HS}\le C\sqrt N|x_n|$. Thus its additional error
is at most

$$
C\sqrt N\|F_N\|_1
\{e^{-c\varepsilon^2 n}|x_0|+C\rho\}
+C\|F_N\|_\infty\mathbb P(\sigma\le n).
\tag{C9}
$$

The square-root use of (C3) changes the absolute contraction constant,
denoted again by $c$. Since $n\ge t/\varepsilon^4$ eventually,
$\varepsilon^2n\ge t/\varepsilon^2\ge1/(N\varepsilon^2)$ grows faster
than every fixed power of $N$. All terms in (C8)--(C9) vanish by (C2),
choosing $L>b$ in (C7). Consequently

$$
\mathbb EF_N(U_n)-\mathbb EF_N(Y_t)\longrightarrow0.
\tag{C10}
$$

This is not a uniform theorem over arbitrary growing $b$ or test order.

## 4. Collision-safe factorial tests have polynomial derivative norms

For $\psi\in C_c^\infty(\mathbb R^k)$ supported in $[-R,R]^k$, let
$F_{N,\psi}(U)$ be its distinct-label factorial sum for the periodic
unfolded spectrum averaged over a uniform origin. For $N>2R$ it agrees
with the full-line local factorial statistic. Periodize $\psi$ separately
in its $k$ coordinates. With Fourier convention
$\widehat\psi(\xi)=\int\psi(x)e^{-2\pi i\xi\cdot x}dx$, TRACE-001 gives

$$
F_{N,\psi}(U)=\frac1{N^k}
\sum_{m\in\mathbb Z^k,\,\sum_i m_i=0}\widehat\psi(m/N)
\sum_{\pi\in\mathcal P(k)}\mu(\pi)
\prod_{B\in\pi}p_{\sum_{i\in B}m_i}(U),
\quad
\mu(\pi)=\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!.
\tag{C11}
$$

Zero trace indices mean $p_0=N$. Charge zero comes from origin averaging,
so the test is rotation invariant; traces make it conjugation invariant.
For a unitary polar extension, the $j$th multilinear Hilbert--Schmidt
derivative of $p_m$ is bounded by $C_jN(1+|m|)^j$ for fixed $j$,
including negative $m$ and $m=0$. The product rule then bounds a partition
term by $C_{j,k}N^k(1+|m|_1)^j$. Schwartz decay and a $(k-1)$-dimensional
lattice sum imply

$$
\sum_{\sum_i m_i=0}|\widehat\psi(m/N)|(1+|m|_1)^j
\le C_{j,k,\psi}N^{k-1+j}.
\tag{C12}
$$

Absolute termwise differentiation is therefore justified, and
$\|F_{N,\psi}\|_6\le C_{k,\psi}N^{k+5}$; the looser $N^{k+6}$
also suffices. No eigenvalue-gap denominator is used, so collisions
cause no regularity failure. For $k=1$ the charge constraint leaves only
$m=0$ and the statistic is the constant $\int\psi$.

Apply (C10) for every fixed $k$. FLOW-016 already proves convergence of
these expectations for $Y_t$. Hence the original uncentered chain has
the claimed smooth factorial limits. Choose a nonnegative compact smooth
bump at least one on a given interval and use its tensor powers as
factorial majorants. The Stirling identity bounds every ordinary count
moment, uniformly in $N$. FLOW-014 and FLOW-012 supply the weak Laplace
limit under (C2), or alternatively repeat (C8)--(C9) for their polynomial
$C^6$ Laplace norm. Weak convergence plus these count moments extends
smooth factorial limits to compact continuous tests and, by the tiling
argument of FLOW-016, to Schwartz tests.

## 5. From an averaged law to one-chain origin averages

Let $Q_{N,\omega}$ be the conditional law of the translated point field
over its independent uniform origin, for one chain realization $\omega$.
Its barycenter $Q_N$ is the weak local law just proved. For a local
factorial observable $\varphi=Z_\psi$, let
$F_N(\omega)=\int\varphi\,dQ_{N,\omega}$ and
$c=\int\varphi\,dQ_{\rm sine}$.
For a fixed positive $S$ put

$$
\mathcal A_S\varphi(\xi)=\frac1S\int_0^S\varphi(T_u\xi)du.
\tag{C13}
$$

Periodicity makes $\int\mathcal A_S\varphi\,dQ_{N,\omega}=F_N(\omega)$
exactly, for every $S$, without a relation between $S$ and $N$. Jensen
then gives

$$
\mathbb E_\omega|F_N-c|^2
\le\int|\mathcal A_S\varphi-c|^2dQ_N.
\tag{C14}
$$

For compact continuous $\psi$, this averaged observable is continuous
in the vague topology and bounded by a constant times a fixed enlarged
window count to power $k$. The moment bounds of order greater than $2k$
make its square uniformly integrable. Thus the right side converges, for
each fixed $S$, to $\int|\mathcal A_S\varphi-c|^2dQ_{\rm sine}$.
The Sine$_2$ kernel $\sin\pi(x-y)/(\pi(x-y))$ is translation invariant,
is a locally trace-class positive contraction, and satisfies Soshnikov's
Theorem 7 on spatial translation ergodicity (arXiv:math/0002099v4,
printed pp.38--42). The mean ergodic theorem makes this last expression
tend to zero as $S\to\infty$. Taking first $N\to\infty$, then
$S\to\infty$, proves $L^2$ convergence in (C14).

For Schwartz tests, truncate in space; the tiled moment bound at order
$2k$ controls the $L^2$ tail uniformly in $N$. Bounded local Laplace
observables follow by the same argument using their continuity. This
self-averaging principle is standard; it identifies neither an almost-sure
rate nor a deterministic realization valid for the whole sequence.

There is also a complete signed Fourier consequence. For
$\widehat\psi\in C_c^\infty(\mathbb R^k)$, let $V_N$ be Haar CUE and put
$b_N=\mathbb E_{\rm CUE}F_{N,\psi}(V_N)$. The standard Haar kernel in
unfolded coordinates, after an immaterial scalar gauge, is
$\sin\pi(x-y)/(N\sin(\pi(x-y)/N))$ for odd $N$.
It tends locally uniformly to the sine kernel; its diagonal is one and
Hadamard bounds its factorial densities by one. Compact convergence and
the same stationary tiled-tail bound prove $b_N\to c$ for Schwartz $\psi$.
For the chain, the full-line statistic in (C14) and the periodized
circle-label statistic in (C11) differ on tuples containing two distinct
period copies of one circle label. Such tuples have coordinate diameter
at least $N$, and thus a coordinate outside $[-N/2,N/2]$. Their absolute
sum is bounded by the Schwartz tail; the tiled count moments of order
$2k$ bound this tail in $L^2$, uniformly in $N$. It tends to zero.
Hence the circle-label statistic also has the $L^2$ limit used below.
Therefore

$$
\mathbb E_\omega\left|
\frac1{N^k}\sum_{\sum_i m_i=0}\widehat\psi(m/N)
\sum_{\pi\in\mathcal P(k)}\mu(\pi)
\left[\prod_{B\in\pi}p_{\sum_{i\in B}m_i}(U_{n_N})
-\mathbb E_{\rm CUE}\prod_{B\in\pi}p_{\sum_{i\in B}m_i}(V_N)\right]
\right|^2\longrightarrow0.
\tag{C15}
$$

For this Fourier-support hypothesis the sum is finite and still retains
all partition counterterms and zero indices. The modulus is outside the
entire signed sum. This is the noisy analogue of the signed all-order
trace target, with convergence in $L^2$ for every fixed test and order.
It is not an absolute termwise estimate or an unperturbed TRACE-005 theorem.

The exact remaining all-order transfer condition can now be stated without
an unproved noisy uniform-integrability premise. Let $T_\varepsilon$ be
the one-step Markov operator of the original chain (C1), and define

$$
\mathfrak D^{\rm chain}_{N,\psi}=
\sum_{j=0}^{n_N-1}\mathbb E[(T_{\varepsilon_N}-I)
F_{N,\psi}(U_j)]
=\mathbb EF_{N,\psi}(U_{n_N})-F_{N,\psi}(A_N).
\tag{C16}
$$

This is a finite-$N$ telescoping identity for the uncentered chain, with
no continuous-time approximation or centering in the definition.
For every fixed test in (C15), that equation proves the equivalences

$$
F_{N,\psi}(A_N)-b_N\to0
\quad\Longleftrightarrow\quad
\mathfrak D^{\rm chain}_{N,\psi}\to0
\quad\Longleftrightarrow\quad
\mathbb E|F_{N,\psi}(U_{n_N})-F_{N,\psi}(A_N)|^2\to0.
\tag{C17}
$$

Indeed $\mathbb EF_{N,\psi}(U_{n_N})-b_N\to0$, and its variance tends
to zero by (C15). Use the exact variance-plus-squared-mean identity for
complex random variables. The modulus in (C16) must remain outside the
whole signed expectation sum. The actual vanishing in (C17) is open;
an absolute sum of step errors has not been bounded.

## 6. Remaining deterministic target

For the actual $A_N=U_N$ at the unchanged fixed coupling $10^{-80}$,
FM-013 supplies the first two trace bounds and FLOW-014 supplies the
reference hypotheses at $t_N=8g_N$. The theorem therefore applies to
the original random chain, including all odd dimensions eventually,
with the inherited ineffective startup threshold.
The Gaussian perturbation is still present. None of (C7), (C10) or (C14)
bounds the difference between the output and the unperturbed spectrum
of $A_N$. FLOW-015's actual signed defect and the direct Heisenberg
signed-sum target TRACE-005 remain open. Full BGS is not closed.
