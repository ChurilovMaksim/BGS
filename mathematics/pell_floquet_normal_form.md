---
title: "A resonance-scale spectral law for a deterministically kicked Pell cat map"
author: "BGS research programme"
date: "5 September 2026"
---

# Status and main result

This is a project derivation with a complete argument below, not a claim of
priority, external referee acceptance, or full Lean formalization. The result
concerns the actual kicked quantum propagator, but its **K-th power at the
arithmetic recurrence scale**, not microscopic nearest-neighbour statistics.
The critical quantum kick tends to zero. A fixed nonzero classical
perturbation is not covered. Section 7 additionally proves a negative
microscopic pair-correlation consequence under global mean-density unfolding.

Put
$$
 \alpha=1+\sqrt2,\quad \lambda=\alpha^2,\quad
 T=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$
Let K tend to infinity through odd primes, and define positive integers N,F by
$$
 N+F\sqrt2=\alpha^K,\qquad N^2-2F^2=-1.
$$
The moduli N may be composite. On the odd subspace of the standard
N-dimensional torus quantization, let U_N be the phase-normalized quantization
of T described in Section 1, and let
$$
 B_N f(x)=2\cos(2\pi x/N)f(x),\quad
 U_{\varepsilon,N}=e^{i\varepsilon B_N}U_N,\quad
 d_N=(N-1)/2.
$$

**Theorem A (critical resonance law).** For every fixed real tau and every
integer m, with epsilon=tau/sqrt(2K),
$$
 \lim_{K\longrightarrow\infty}
 \frac{1}{d_N}\operatorname{Tr}_{-}
       U_{\varepsilon,N}^{mK}
       =\exp(-m^2\tau^2/2).                                      \tag{A}
$$
Consequently the empirical eigenvalue measure of U_(epsilon,N)^K converges
weakly on the unit circle to the wrapped normal law. For tau nonzero its
angular density on [-pi,pi) is
$$
 w_\tau(\theta)=\frac{1}{\sqrt{2\pi}|\tau|}
       \sum_{\ell\in\mathbb Z}
       \exp\!\left[-\frac{(\theta+2\pi\ell)^2}{2\tau^2}\right].   \tag{B}
$$
For tau=0 the limit is the point mass at 1. In particular the normalized
resonance echo obeys
$$
 d_N^{-2}\left|\operatorname{Tr}_{-}U_{\varepsilon,N}^{mK}\right|^2
       \longrightarrow e^{-m^2\tau^2}.                          \tag{C}
$$
This is a deterministic limit: there is no parameter average in (A).

The principal finite estimate, proved before any limit is taken, is
$$
 \left\|V_\varepsilon U_{\varepsilon,N}V_\varepsilon^*
            -e^{i\varepsilon\overline B}U_N\right\|_{2,-}
       \leq \frac{12\varepsilon^2}{\sqrt K},\qquad K\geq11,        \tag{D}
$$
for an explicit unitary V_epsilon. Here the norm is normalized
Hilbert--Schmidt norm on the entire odd subspace. It does not control an
individual level or an operator-norm spectral gap. The finite comparison
error in (A) is at most 6|m|tau^2/sqrt(K); an additional Gaussian
characteristic-function convergence error is o(1), not assigned that rate.

# 1. Arithmetic and the fixed classical observable

The recurrence (N_j,F_j)=(N_(j-1)+2F_(j-1),N_(j-1)+F_(j-1)), starting at
(1,0), shows that N is odd. Put, in Z/NZ,
$$
 s=F^{-1},\qquad s^2=2,\qquad h=3+2s,\qquad q=-F.
$$
Since (1+s)^K=N+Fs=1, h^K=1. Also h-1=2(1+s) is a unit. For every prime
ell dividing N, the order of h modulo ell is therefore precisely K: K is
prime and that order is not 1. Hence 1-h^j is a unit for 1<=j<K, and
1+h^j is a unit for every j, because K is odd. In particular ell=1 mod K,
and N=1 mod 2K. Neither squarefreeness nor primality of N is required.

Use the counting-measure inner product and centered Weyl operators
$$
 W(a,b)f(x)=e_N(a(x-b/2))f(x-b),\qquad
 S_u f(x)=f(u^{-1}x),\qquad Rf(x)=f(-x).
$$
Divisions in Weyl exponents mean inverses in Z/NZ. The multiplication and
covariance formulas are
$$
 W(a,b)W(c,d)=e_N((ad-bc)/2)W(a+c,b+d),
$$
$$
 S_uW(a,b)S_u^*=W(u^{-1}a,ub),\qquad RW(v)R=W(-v).
$$
Individual Weyl translations need not preserve parity; their symmetrized
sums do. On the odd subspace take
$$
 U_0=S_h^{-1},\qquad B=W(q,1)+W(q,1)^*,\qquad
 U_\varepsilon=e^{i\varepsilon B}U_0.                            \tag{1}
$$
In these coordinates U_0^K=I exactly.

For completeness this is unitarily equivalent to the fixed-map formulation
in Theorem A, including the kick, not merely to its compressed observable.
Let C_t f(x)=e_N(tx^2/2)f(x) and let F_N have kernel e_N(xy)/sqrt(N). Set
$$
 M=\begin{pmatrix}-1/(2s)&1\\-1/2&-s\end{pmatrix},\qquad
 V=C_{s^{-1}}S_{1/2}F_N C_{2s}.
$$
Its factors have Weyl covariance matrices respectively
$$
 \begin{pmatrix}1&t\\0&1\end{pmatrix},\quad
 \begin{pmatrix}u^{-1}&0\\0&u\end{pmatrix},\quad
 \begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$
Multiplication gives covariance M, det M=1, and
T=M diag(h,h^(-1)) M^(-1). Define U_N=VU_0V*. The index of
V*W(1,0)V is M^(-1)(1,0)=(-s,1/2). Further conjugation by S_2, which
commutes with U_0, changes this to (-s/2,1)=(-F,1) modulo N. Thus
S_2 V* conjugates the entire physical kicked propagator to (1). These
unitaries all preserve parity.

With the usual semiclassical convention e^(i action/hbar), the classical
kick amplitude corresponding to epsilon is proportional to hbar*epsilon.
Here hbar is proportional to 1/N. At the critical scale this amplitude is
of order 1/(N sqrt(K)), not a fixed classical perturbation.

# 2. Two summable phase estimates

Write C(A)=U_0 A U_0*, and
$$
 B_j=C^j(B)=W(v_j)+W(-v_j),\qquad v_j=(qh^j,h^{-j}),
 \qquad \overline B=K^{-1}\sum_{j=0}^{K-1}B_j.                    \tag{2}
$$
The conjugation C shifts the label cyclically, so C(bar B)=bar B.
Define
$$
 a_j=\left|e_N(q(h^j-h^{-j}))-1\right|,\qquad
 c_j=\frac{K-1-2j}{2K},\qquad G=\sum_{j=0}^{K-1}c_jB_j.          \tag{3}
$$
Then a_0=0, a_(K-j)=a_j. Direct subtraction of the coefficients gives the
exact cohomological equation
$$
 G-C(G)=B-\overline B.                                         \tag{4}
$$
The coefficients have zero mean. Importantly, they are small at the
half-period at which the large commutator phases accumulate.

Let P_t denote the second Pell sequence, alpha^t=Q_t+P_t sqrt(2).
For the signed representative delta of j mod K one has
$$
 q(h^j-h^{-j})=-2P_{2\delta}\pmod N.                            \tag{5}
$$
Indeed h^delta=(3+2s)^delta=Q_(2delta)+P_(2delta)s, and F*s=1.
For delta=(K-1)/2-ell positive,
$$
 \frac{P_{2\delta}}{N}
 =\frac{\lambda^{-\ell}}{\sqrt2\,\alpha}
       \frac{1-\lambda^{-2\delta}}{1-\lambda^{-K}}.              \tag{6}
$$
Put r=lambda^(-1), A=4pi/(sqrt(2)alpha). Using |exp(it)-1|<=|t| and
summing both signed representatives proves
$$
 L_K:=\sum_{j=0}^{K-1}a_j
 \leq\frac{2A}{(1-r)(1-\lambda^{-K})}
 =\frac{2\sqrt2\pi}{1-\lambda^{-K}}<9\quad(K\geq3).              \tag{7}
$$
There is a sharper weighted estimate. At j=(K-1)/2-ell the weights at j and
K-j have absolute values ell/K and (ell+1)/K. Therefore
$$
 \sum_j |c_j|a_j
 \leq\frac{A}{K(1-\lambda^{-K})}\sum_{\ell\geq0}(2\ell+1)r^\ell
 =\frac{2\pi}{K(1-\lambda^{-K})}.                              \tag{8}
$$
The final identity follows from A(1+r)/(1-r)^2=2pi. The estimates are
analytic inequalities; the regression's decimal phase values are only
finite checks of them.

# 3. Quadratic lifting and orthogonal commutator supports

**Lemma 1 (lifting).** Fix m. For all sufficiently large K, every signed
m-term reciprocal relation
$$
 \sum_{\nu=1}^m\epsilon_\nu h^{j_\nu}
 =\sum_{\nu=1}^m\epsilon_\nu h^{-j_\nu}=0\pmod N,
 \qquad \epsilon_\nu\in\{-1,1\},                               \tag{9}
$$
can be cyclically rotated to a polynomial P with P(lambda)=0. Its
coefficient l1 norm is at most m and its degree is at most
K-ceil(K/m). For m=4 this holds for every odd prime K>=11, and the relation
is then coefficientwise balanced.

**Proof.** Cancel opposite signs at identical labels. If anything remains,
cut the cyclic support at a largest gap and rotate. There are at most m
support points, giving the stated degree bound. Both congruences in (9)
survive. Divide P by the monic polynomial Z^2-6Z+1 over the integers. Its
remainder aZ+b vanishes at h and h^(-1); their difference 4s is a unit.
Hence N divides a and b. A nonzero quadratic norm of P(lambda) is thus an
integer divisible by N^2, but
$$
 |P(\lambda)P(\lambda^{-1})|
 \leq m^2\lambda^{K-\lceil K/m\rceil}<N^2                       \tag{10}
$$
for sufficiently large K at fixed m. This is impossible, so P(lambda)=0.
For m=4 a sufficient condition is
lambda^(K/4)(1-lambda^(-K))^2>64. It holds for K>=11: lambda>5,
5^(11/4)>80, and 1-5^(-11)>9/10 already give a strict lower bound 64.8.
A nonzero polynomial of l1 norm at most 4 cannot vanish at lambda>3:
its leading term strictly dominates the total of all lower terms.
Thus in this case the polynomial was zero. End of proof.

It follows that the 2K(K-1) vectors
$$
 \epsilon v_t+\delta v_s,\qquad 0\leq t<s<K,\quad
 \epsilon,\delta\in\{-1,1\},                                  \tag{11}
$$
are nonzero and distinct for K>=11. Any collision would give a balanced
four-letter relation, forcing precisely the original unordered signed
pair. The matrices W(v) form an orthonormal basis for the full normalized
Hilbert--Schmidt inner product, also for composite odd N, because
Tr W(v)=N times the indicator v=0.

Each of the four Weyl coefficients in [B_t,B_s] has modulus a_(s-t).
Different unordered time pairs have disjoint support by (11). Since
c_t-c_s=(s-t)/K, exact orthogonality gives
$$
 \|[G,\overline B]\|_{2,N}^2
 =\frac4{K^4}\sum_{j=1}^{K-1}(K-j)j^2a_j^2
 =\frac2{K^3}\sum_{j=1}^{K-1}j(K-j)a_j^2
 \leq\frac9K.                                                  \tag{12}
$$
Here ||A||_(2,N)^2=Tr(A*A)/N. The middle identity uses a_(K-j)=a_j;
the last uses j(K-j)<=K^2/4, a_j^2<=2a_j, and (7).

The operator norm needs no orthogonality. Four Weyl coefficients, (7),
and (8) give
$$
 \|[G,B]\|_{\rm op}<\frac{26}{K},\qquad
 \|[B,\overline B]\|_{\rm op}<\frac{36}{K}.                     \tag{13}
$$
For a parity-preserving A, positivity of A*A implies
$$
 \|A\|_{2,-}\leq\sqrt{\frac{2N}{N-1}}\,\|A\|_{2,N}.             \tag{14}
$$
No orthogonality of Weyl operators restricted to the odd subspace is assumed.

# 4. A finite normal form without a small generator

For finite Hermitian A,D, real epsilon, and any unitarily invariant norm,
$$
 \|e^{i\varepsilon A}e^{i\varepsilon D}
           -e^{i\varepsilon(A+D)}\|
 \leq\frac{\varepsilon^2}{2}\|[A,D]\|.                          \tag{15}
$$
This is the usual two-factor commutator estimate, not a new general product
formula. To prove it, differentiate
exp(i(epsilon-t)(A+D)) exp(itA) exp(itD). After factoring unitaries, the
integrand is exp(itA)D exp(-itA)-D. Integrate its derivative once more;
the resulting triangular integration domain has area epsilon^2/2.
Negative epsilon follows by replacing A,D by -A,-D. In particular there is
no assumption that |epsilon|*||A|| is small.

Set V_epsilon=exp(-i epsilon G). By (4),
$$
 V_\varepsilon U_\varepsilon V_\varepsilon^*
 =e^{-i\varepsilon G}e^{i\varepsilon B}
       e^{i\varepsilon C(G)}U_0.
$$
Apply (15) first to -G,B, then to B-G,C(G). Their total sum is bar B,
and [B-G,C(G)]=[B-G,bar B]. Equations (12)--(14) show
$$
 \begin{split}
 \|V_\varepsilon U_\varepsilon V_\varepsilon^*
       -e^{i\varepsilon\overline B}U_0\|_{2,-}
 &\leq\frac{\varepsilon^2}{2}
   \left(\frac{62}{K}+3\sqrt{\frac{2N}{(N-1)K}}\right)\\
 &\leq\frac{12\varepsilon^2}{\sqrt K},\qquad K\geq11.
 \end{split}\tag{16}
$$
For the last step it even suffices to use N>=7 and
31/sqrt(11)+(3/2)sqrt(7/3)<12. This proves (D) for all real epsilon.
G may have operator norm of order K. Expanding its exponential in powers
of epsilon and requiring epsilon*K small would incorrectly discard the
critical regime. Estimate (15) avoids that requirement.

Since bar B commutes with U_0 and U_0^K=I, telescoping unitary powers in the
same norm yields, for any integer m,
$$
 \left|\tau_-(U_\varepsilon^{mK})
       -\tau_-(e^{im\varepsilon K\overline B})\right|
 \leq12|m|\varepsilon^2\sqrt K,\qquad
 \tau_-(A)=d_N^{-1}\operatorname{Tr}_{-}A.                      \tag{17}
$$
For negative m use adjoints. Cauchy--Schwarz for the normalized trace
justifies the passage from the norm to traces.

# 5. A self-contained global law for the averaged observable

The remaining input is established here directly on the whole odd subspace;
no unproved claim about the old arithmetic-moment corpus is imported.
Define
$$
 X_K=\sqrt{K/2}\,\overline B=(2K)^{-1/2}\sum_{j=0}^{K-1}B_j.
$$

**Lemma 2 (Gaussian average).** For each fixed integer r>=1,
$$
 \tau_-(X_K^{2r})=(2r-1)!!+O_r(K^{-1})+O_r(K^r/N),               \tag{18}
$$
and for each fixed odd m, eventually
$$
 |\tau_-(X_K^m)|\leq (2K)^{m/2}/(N-1).                         \tag{19}
$$
The empirical measures of X_K converge weakly and in quadratic
Wasserstein distance to the standard normal law.

**Proof.** In the full Weyl representation Tr(RW(v))=1 for every v: the
unique fixed point x=-b/2 of RW(a,b) contributes phase 1. Thus the normalized
odd trace of a word e_N(phi)W(v) is
$$
 e_N(\phi)\frac{N\mathbf1_{v=0}-1}{N-1}.                       \tag{20}
$$
Expanding X_K^m, the noncentral part is bounded by (2K)^(m/2)/(N-1).
The central part is the weighted count of the reciprocal relations (9),
with normalization N/(N-1) times (2K)^(-m/2).

Here is the required count including structurally forced nonbalanced
relations. For a polynomial of l1 norm at most m vanishing at lambda,
a gap d>2 log_lambda m separates two independently vanishing pieces.
Indeed write P=P_low+Z^(a+d)P_high with deg P_low<=a and nonnegative
exponents in P_high. If P_high(lambda) is nonzero, its algebraic-integer
norm is a nonzero integer. Since |P_high(lambda^(-1))|<=m,
|P_high(lambda)|>=1/m. Cancellation with |P_low(lambda)|<=m lambda^a
would force lambda^d<=m^2, a contradiction.

Repeatedly splitting gives components with span bounded in terms of m,
for example by D_m=(m-1)(ceil(2 log_lambda m)+1). Every nonzero component
has at least three signed occurrences: two distinct positive powers cannot
cancel with signs of magnitude one. Restore previously cancelled opposite
pairs as two-occurrence components. A nonbalanced 2r-letter word therefore
has at most r-1 components. For each of finitely many partitions of the
2r positions, signs and bounded relative offsets, each component has at
most K translations on the cyclic time set. There are only O_r(K^(r-1))
such words. There is no additional factor K from choosing a cut: the count
is over the component translations themselves, and the largest-gap cut
was used only to prove bounded width. Their normalized contribution is
O_r(1/K).

For odd m, a lifted P is an integer multiple of Z^2-6Z+1, so P(1) is
divisible by -4. But P(1) is the sum of an odd number of signs. Thus no
central word exists once Lemma 1 applies, proving (19).

A balanced 2r-word pairs identical time labels with opposite signs.
Assignments with repeated pair labels cause only O_r(K^(r-1)) overcount.
For every matching of the 2r positions there are K^r choices of pair
labels and 2^r orientations. The Weyl phase of such a word is a product,
over the crossing pairs, of factors e_N(q(h^a-h^(-a))) or their conjugates.
This follows by summing the symplectic products of the signed indices in
word order: disjoint or nested pairs cancel; a crossing pair retains one
full symplectic product.

Each crossing difference of independent uniform pair labels is uniform
mod K. Independence of the different crossing factors is neither true in
general nor needed. The elementary inequality
|product u_l-1|<=sum |u_l-1| for |u_l|=1 and (7) give an average phase
error at most 9 times the number of crossings divided by K. Hence each
matching contributes 1+O_r(1/K) after normalization. There are
(2r-1)!! matchings. Together with the nonbalanced count and (20), this
proves (18).

The second-moment bound gives tightness. Higher even moments give uniform
integrability when passing moments to subsequential limits. The Gaussian
moment sequence is determinate, for example by Carleman's criterion, since
((2r-1)!!)^(1/(2r))<=sqrt(2r). Every subsequential limit is therefore
standard normal. Convergence of the second moments upgrades weak
convergence to quadratic Wasserstein convergence. End of proof.

# 6. Critical and subcritical propagator spectra

For epsilon=tau/sqrt(2K), (17) becomes
$$
 \left|\tau_-(U_\varepsilon^{mK})-
              \tau_-(e^{im\tau X_K})\right|
       \leq \frac{6|m|\tau^2}{\sqrt K}.                        \tag{21}
$$
Lemma 2 and bounded continuity of exp(im tau x) give (A). Integer Fourier
coefficients determine measures on the circle: trigonometric polynomials
are dense in continuous functions there. Applying the characteristic
function of a normal variable proves (B), and taking absolute squares
proves (C). No eigenphase labelling across the old degenerate sectors is
used or asserted.

There is also a genuine extension of the earlier subcritical global
transfer, but for **folded phases** rather than individually isolated
clusters. Let epsilon_K be nonzero and tau_K=epsilon_K sqrt(2K) tend to
zero. If exp(i theta_l) are the eigenvalues of U_(epsilon,K), define
$$
 y_l=\frac{\operatorname{Arg}(e^{iK\theta_l})}{\tau_K},
 \qquad \operatorname{Arg}\in[-\pi,\pi).
$$

**Corollary B (subcritical folded Gaussian law).** The empirical measures
of y_l converge in quadratic Wasserstein distance to the standard normal
law whenever epsilon_K sqrt(K) tends to zero.

**Proof with a quantitative tail control.** For two unitary matrices, the
squared absolute overlaps of their orthonormal eigenbases form a doubly
stochastic matrix. The corresponding average squared chord distance equals
their normalized squared Hilbert--Schmidt difference. Decomposing this
matrix into permutation matrices gives an eigenvalue matching with no
larger average cost. The decomposition can be obtained by Hall's matching
criterion and successive subtraction; it uses no eigenvalue simplicity.
Thus (16), telescoped K times, matches the powered spectrum to
exp(i tau_K x_l), where x_l are the eigenvalues of X_K, with root mean
square chord error at most 6 tau_K^2/sqrt(K).

If |tau_K x_l|<=pi/2, principal argument differences obey
|Arg u-tau_K x_l|<=4|u-exp(i tau_K x_l)|. On the complementary set
|Arg u/tau_K-x_l|<=3|x_l|. Consequently
$$
 \begin{split}
 W_2(\operatorname{law}(y),\operatorname{law}(X_K))
 &\leq\frac{24|\tau_K|}{\sqrt K}
   +3\sqrt{\tau_-\!\left(X_K^2
       \mathbf1_{|X_K|>\pi/(2|\tau_K|)}\right)}\\
 &\leq\frac{24|\tau_K|}{\sqrt K}
       +\frac{6|\tau_K|}{\pi}\sqrt{\tau_-(X_K^4)}.
 \end{split}\tag{22}
$$
The fourth moment stays bounded by Lemma 2, so the right side tends to zero.
Combine with the W_2 conclusion of that lemma. End of proof.

The former isolated-cluster argument required epsilon_K K^(3/2) tending to
zero. Corollary B permits an additional factor K in the kick scale, but its
observable is a folded spectral measure. It must not be restated as an
individual-cluster rank or no-overlap theorem.

# 7. A compact-test microscopic obstruction

A negative statement about microscopic correlations needs less information
than a positive universality theorem. The recurrence law above supplies
such a statement through Fourier positivity. This section concerns the
whole odd spectrum, with its multiplicities and the **global mean-density
unfolding**. It is not a claim about a further symmetry sector or an
unfolding which first removes a nonconstant mesoscopic intensity profile.

Let x_1,...,x_d be the eigenphases of a d-dimensional unitary U, measured in
turns, so its eigenvalues are exp(2 pi i x_j). For a compactly supported
continuous test phi define the ordered factorial pair statistic
$$
 C_d(U;\phi)=\frac1d\sum_{a\ne b}\sum_{n\in\mathbb Z}
              \phi\bigl(d(x_a-x_b+n)\bigr).                    \tag{23}
$$
Distinct indices, not distinct eigenvalues, are required in this definition.
For L>0 use the compact triangular test
$$
 \phi_L(s)=\frac1L(1-|s|/L)_+,\quad
 \int\phi_L=1,\quad \phi_L(0)=1/L,\quad
 \widehat\phi_L(u)=\operatorname{sinc}^2(Lu)\geq0,               \tag{24}
$$
where sinc(v)=sin(pi v)/(pi v), with value 1 at zero. Fourier transforms use
exp(-2 pi i u s). Absolute convergence of the periodized Fourier series
(the coefficients decay quadratically) gives the exact identity
$$
 C_d(U;\phi_L)=d^{-2}\sum_{t\in\mathbb Z}
   \widehat\phi_L(t/d)(|\operatorname{Tr}U^t|^2-d).              \tag{25}
$$
If d>L, the total diagonal subtraction is exactly 1/L, because
sum_n phi_L(d n)=phi_L(0). For any distinct positive integers r_1,...,r_M,
positivity therefore gives
$$
 C_d(U;\phi_L)\geq1-\frac1L+
   2\sum_{j=1}^M\operatorname{sinc}^2(Lr_j/d)
                   |d^{-1}\operatorname{Tr}U^{r_j}|^2.         \tag{26}
$$
No control or truncation of the remaining high-frequency traces is needed
for this lower bound; their contribution is nonnegative.

There is an equivalent counting interpretation. Let N_L(y) count the
phases in the circular interval [y,y+L/d), with y uniform in [0,1).
Then E_y N_L=L and an overlap-of-intervals calculation gives
$$
 \operatorname{Var}_y N_L
      =L^2\bigl(C_d(U;\phi_L)-1\bigr)+L.                       \tag{27}
$$
This identity is also verified independently by integrating the
piecewise-constant counting function, rather than reusing the pair sum.

**Theorem C (obstruction and necessary kick scale).** For the kicked Pell
family of Theorem A, put tau_K=epsilon_K sqrt(2K).
If tau_K tends to a finite nonzero tau, then for every fixed L>0,
$$
 \liminf_{K\to\infty} C_{d_N}(U_{\varepsilon_K,N};\phi_L)
      \geq \Theta(\tau)-\frac1L,\qquad
 \Theta(\tau)=\sum_{m\in\mathbb Z}e^{-m^2\tau^2}>1,             \tag{28}
$$
and
$$
 \liminf_{K\to\infty}\operatorname{Var}_y N_L
      \geq L^2\bigl(\Theta(\tau)-1\bigr).                      \tag{29}
$$
If tau_K tends to zero, C_(d_N)(U_(epsilon_K,N);phi_L) tends to positive
infinity for every fixed L. Consequently, convergence of the globally
unfolded pair measures to a bounded density rho(s) satisfying
rho(s)->1 as |s|->infinity requires
$$
             |\varepsilon_K|\sqrt K\longrightarrow\infty.     \tag{30}
$$
This is a necessary condition only, not a sufficient universality criterion.

**Proof.** The recurrence trace limit remains valid if tau_K->tau varies
with K. Indeed Lemma 2 bounds tau_-(|X_K|), and
|tau_-(exp(im tau_K X_K))-tau_-(exp(im tau X_K))|
<=|m| |tau_K-tau| tau_-(|X_K|). The error in (21) is uniform for bounded
tau_K. Thus the normalized mK trace tends to exp(-m^2 tau^2/2) for each
fixed m, including tau=0.

Apply (26) with r_j=jK. Since K/d_N->0, the sinc factors tend to 1.
For every fixed M the resulting lower bound is
1-1/L+2 sum_(m=1)^M exp(-m^2 tau^2). Let M tend to infinity *after* taking
the lower limit in K. This proves (28), or divergence when tau=0.
Equation (27) gives (29).

Suppose the pair measures converge vaguely to rho(s)ds, where rho is bounded
and clusters to unit intensity. For every fixed L the limiting triangular
statistic would be
$$
 A_L=\int_{-1}^1(1-|u|)\rho(Lu)\,du.
$$
Dominated convergence gives A_L->1 as L->infinity. But (28) requires
A_L>=Theta(tau)-1/L for every L, a contradiction. For tau=0 a finite
locally bounded target already contradicts the fixed-L divergence.
Finally, if |epsilon_K|sqrt(K) does not tend to infinity, there is a
subsequence on which tau_K is bounded and then a further subsequence
converging to a finite tau. The same contradiction applies. End of proof.

The use of a compact test is essential for the logical scope. A Gaussian
test without an independently controlled tail would only obstruct a
Schwartz-test limit, not automatically vague local convergence. If the
pair convergence definition uses only smooth compact tests, positive
measures acquire locally uniform mass bounds by testing a bump which is
one on a given compact set; approximation then extends convergence to the
continuous triangular tests. Alternatively, start directly with a smooth
nonnegative compact f of integral one, take phi=f*tilde(f), and scale it:
phi_hat=|f_hat|^2>=0 and the same proof uses phi(0)/L instead of 1/L.
No unproved high-frequency-tail assumption is hidden in Theorem C.

The Poisson pair density rho=1 and the sine-kernel density
rho_2(s)=1-sinc(s)^2 are both excluded. More explicitly, keeping only the
first resonance gives
$$
 \liminf C_{d_N}(U_{\varepsilon_K,N};\phi_L)
        \geq1+2e^{-\tau^2}-1/L.                               \tag{31}
$$
Since integral phi_L rho_2<=1, taking L=exp(tau^2) yields a gap of at least
exp(-tau^2) from the sine-kernel prediction. At tau=1, already L=2 gives
lower bound 1.2357588823..., greater than both that prediction and the
Poisson value 1.

The standard GOE bulk pair density is excluded by the bounded-clustering
part of the theorem, not by an assumed pointwise bound rho<=1. In unit
intensity normalization it is the even continuation of
$$
 \rho_1(s)=1-S(s)^2-S'(s)\int_s^\infty S(t)\,dt,\qquad
 S(s)=\operatorname{sinc}(s),\quad s\geq0.                       \tag{32}
$$
This standard formula is recorded in Brezin--Hikami, equation (181) after
unfolding. It is bounded at zero, and integration by parts in the sine tail
shows rho_1(s)=1+O(s^(-2)) at infinity. The same elementary criterion
therefore applies. The random-matrix formulas, Fourier positivity and
counting-variance identity are standard ingredients; no priority is claimed
for those general tools.

This changes the route toward a positive BGS result: the critical and
subcritical globally unfolded odd spectra considered here are not merely
unproved universal families; they are **excluded** from the bounded
clustering pair limits just specified. The statement does not settle
nearest-neighbour distributions individually, density-adapted re-unfolding,
a further desymmetrized block, or fixed nonzero classical kicks. It is not
a refutation of a correctly qualified generic BGS conjecture.

The finite verifier keeps forty configurations (K=3,5,7, several tau and L)
and two synthetic controls. At K=7,tau=1,L=2 it numerically gives
C_d=1.30936229449... and Var N_L=3.23744917797..., while the finite lower
bound retaining K and 2K is 1.21861711382... . These are floating-point
checks of finite identities, not the proof of (28). In particular the
asymptotic bound is not incorrectly enforced on small K.

# 8. Verification, reproducibility, and limits

The Python verifier constructs the cohomological generator explicitly,
checks (4), compares the exact Fourier-support expression (12) to direct
matrix multiplication, and compares all small odd-sector block spectra
against the spectrum of X_K. Dense propagators and a separate chirp--FFT
implementation agree numerically. The C++20 verifier works instead in the
original integral T-coordinates with multiprecision integers; it verifies
the signed-pair cardinalities and Pell arithmetic independently of the
Python diagonal-coordinate representation.

The Lean module has general cleared-denominator identities for c_j and a
finite original-coordinate K=11 certificate. Its compilation status must
be checked separately. It does not formalize Duhamel estimates, Lemma 2,
Wasserstein convergence, or Theorem A.

Extended numerical experiments estimate normalized traces with independent
uniform fourth-root-of-unity vectors in an orthonormal odd basis. If R
probes are used, the estimate is unbiased and its complex mean-square
error is at most 1/(R d_N): the off-diagonal matrix-square sum is at most
d_N for a unitary. The recorded square-root bound is an RMS bound over
random probes, not a deterministic interval and not a 95 percent confidence
interval. Fixed seeds ensure reproducibility. Both m=1 and m=2, including
visible finite-size deviations, are retained. Finite agreement is not a
proof of (A).

Reproduce the independent checks with CMake and
the script `pell_floquet_regression.py` in the verification directory,
passing `--cpp` and the compiled verifier path.
The extended option is `--extended --probes 32`. Promoted evidence records
source hashes and the scope of each check. The figure generator consumes
that evidence rather than rerunning or editing selected points.

The ordinary two-factor product estimate is established mathematics.
Tracial central limit theorems and semiclassically small perturbations of
cat maps also have an existing literature. The arithmetic weighted-phase
construction and the exact statement here require separate priority review;
none is inferred from a few search results. See the companion source audit
in `literature/pell_floquet_sources.md`.

Finally K is of order log N, whereas the odd-space Heisenberg scale is of
order d_N. Equation (A) is a one-point spectral law of U_epsilon^K and a
trace law at recurrence times. It does not supply positive local universality or fixed-strength classical
BGS universality. Section 7 does supply a negative compact-test pair
obstruction. A positive route must go beyond its necessary kick scale,
justify the symmetry reduction and unfolding, and obtain joint trace
control at times of order d_N for the intended classical perturbation.

# Related primary records

Greg Kuperberg, *A tracial quantum central limit theorem*, Transactions of
the AMS 357 (2005), 459--471; [arXiv:math-ph/0202035](https://arxiv.org/abs/math-ph/0202035).
The stated i.i.d. tracial setting is relevant precedent, not an assumption
verified for our deterministic array.

*Theory of Trotter Error with Commutator Scaling*, Physical Review X 11
(2021), 011020; [DOI:10.1103/PhysRevX.11.011020](https://doi.org/10.1103/PhysRevX.11.011020).
The two-factor estimate used above is standard; the arithmetic commutator
bounds, rather than a new general product formula, are the specific input.

Martin Horvat and Mirko Degli Esposti, *Egorov property in perturbed cat map*,
Journal of Physics A 40 (2007); [arXiv:0706.4397](https://arxiv.org/abs/0706.4397).
Its abstract concerns quantum--classical fidelity measured by phase-space
overlap, a different statistic. This comparison uses primary abstracts and
records, not a complete full-text priority review.

E. Brezin and S. Hikami, *New correlation functions for random matrices and
integrals over supergroups* (2002);
[arXiv:math-ph/0208001](https://arxiv.org/abs/math-ph/0208001).
Equation (181) supplies the standard GOE two-point function used only as
a comparison target; its bounded-clustering property is checked above.
