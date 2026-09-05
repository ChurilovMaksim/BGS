# Short recurrence traces force a microscopic second-correlation obstruction

Status: analytic continuation with proofs below. No priority claim is made.
The abstract statements in Sections 1-3 are independent of the Pell model.
The Pell application in Section 4 explicitly depends on the indicated
normal-form and Gaussian-average hypotheses; a successful computer run is
not a substitute for those hypotheses. No new execution or Lean compilation
is asserted in this note.

## 1. Precise normalization

Let U_D be a D-dimensional unitary matrix, with eigenvalues
exp(2 pi i x_a), 0 <= x_a < 1, including multiplicities. All statements use
uniform unfolding by the overall mean density D. No adaptive unfolding by
a locally varying spectral density is performed.

For 0 < L < D, put

    N_D(x,L) = #{a : (x_a-x) mod 1 belongs to [0,L/D)},
    V_D(L) = integral_0^1 (N_D(x,L)-L)^2 dx.

For a Schwartz test phi on the real line, define the factorial statistic

    R_D(phi) = (1/D) sum_(a != b) sum_(ell in Z)
                         phi(D(x_a-x_b+ell)).

The Fourier transform convention is

    phihat(u) = integral_R phi(s) exp(-2 pi i u s) ds.

The mean of N_D(x,L) over x is exactly L, irrespective of the spectrum.

## 2. An abstract resonance theorem

**Theorem 1.** Suppose D tends to infinity, q_D is a positive integer with
q_D/D -> 0, and for every fixed positive integer m,

    D^(-1) Tr(U_D^(m q_D)) -> a_m.

Then, for every fixed L > 0,

    liminf V_D(L) >= 2 L^2 sum_(m>=1) |a_m|^2.                 (1)

The right side is permitted to be infinite. Also, whenever phihat is real,
nonnegative everywhere, and phihat(0) > 0,

    liminf R_D(phi)
       >= phihat(0) (1 + 2 sum_(m>=1) |a_m|^2) - phi(0).     (2)

These are lower bounds, not existence statements for limiting local
correlations. They use no control of the other Fourier modes.

**Proof.** The nonzero Fourier coefficient of the interval indicator of
length L/D has squared modulus sin^2(pi k L/D)/(pi k)^2. Parseval gives
exactly

    V_D(L) = 2 sum_(k>=1) sin^2(pi k L/D)/(pi k)^2
                                      |Tr(U_D^k)|^2.        (3)

Every term is nonnegative. Retain k=q_D,...,M q_D for a fixed M. For each
retained m,

    D sin(pi m q_D L/D)/(pi m q_D) -> L.

Take liminf and then let M increase to infinity. This proves (1).

Poisson summation and subtraction of the a=b terms give the exact identity

    R_D(phi)
       = sum_(k in Z) phihat(k/D) |D^(-1)Tr(U_D^k)|^2
           - sum_(ell in Z) phi(D ell).                     (4)

The second term tends to phi(0). The k=0 summand is phihat(0). Retain only
k=0 and k=+/-m q_D for 1<=m<=M in the first sum. Positivity of phihat
allows this without an estimate for the discarded traces. Continuity at
zero, the trace hypotheses, and then M -> infinity prove (2). End of proof.

The proof of (2), unlike a variance-only argument, directly supplies a
Schwartz-test obstruction to convergence of second factorial correlation
measures. Weak convergence of point processes without uniform integrability
of their second moments is a different assertion and is not ruled out by
(1) alone.

### A finite, directly testable version

Write b_D=|D^(-1) Tr(U_D^q_D)| and sinc(u)=sin(pi u)/(pi u), sinc(0)=1.
Equation (3) implies, without a limit,

    V_D(L) >= 2 L^2 sinc(q_D L/D)^2 b_D^2.                    (5)

For phi_L(s)=exp(-(s/L)^2)/(sqrt(pi)L), equation (4) implies

    R_D(phi_L) >= 1 + 2 exp(-(pi L q_D/D)^2) b_D^2
                                  - sum_(ell in Z) phi_L(D ell). (6)

Neither finite bound is an equality in general.

## 3. Explicit comparison with the orthogonal and unitary reference kernels

The unit-density unitary sine-kernel two-point function is

    R_unit(s) = 1-S(s)^2,  S(s)=sin(pi s)/(pi s).

Consequently its phi_L statistic is at most 1. This conclusion follows
immediately from phi_L >= 0 and integral phi_L = 1.

For the orthogonal bulk reference, use its explicit even two-point function
whose expression for s>0 is

    R_orth(s) = 1-S(s)^2-S'(s) F(s),
    F(s) = integral_s^infinity S(t) dt.

The improper integral has F(0)=1/2. Put h=R_orth-1. A deliberately coarse,
self-contained bound adequate for the comparison is

    integral_R |h(s)| ds < 8.                               (7)

Here are the details. On 0<s<=1, use
S(s)=integral_0^1 cos(pi s t)dt, |S'|<=pi/2, and |F|<=1/2+s<=3/2.
This gives |h|<=1+3pi/4. On s>=1, integration by parts gives
|F(s)|<=2/(pi^2 s), while |S|<=1/(pi s) and
|S'|<=1/s+1/(pi s^2). Hence

    |h(s)| <= (3+2/pi)/(pi^2 s^2),  s>=1.

The integral over the positive half-line is at most
1+3pi/4+(3+2/pi)/pi^2 < 4; evenness proves (7).

It follows that the reference Gaussian-test statistic is bounded above by

    integral_R phi_L(s) R_orth(s) ds
       <= 1 + 8/(sqrt(pi)L).                                (8)

For a process with this pair correlation, its interval number variance is
L+integral_(-L)^L (L-|s|)h(s)ds, and is at most 9L by (7). The sharper
logarithmic asymptotic is not needed here.

Thus any positive value chi=2 sum |a_m|^2 excludes the orthogonal reference
under the uniform unfolding whenever one chooses the fixed Schwartz test
phi_L with L>9/(sqrt(pi)chi). This is an explicit comparison of correlation
functionals, not an inference from a global eigenvalue density.

## 4. Application to the proposed arithmetic Floquet construction

Use odd prime K, alpha=1+sqrt(2), lambda=alpha^2, and

    N+F sqrt(2)=alpha^K, D=(N-1)/2, q_D=K,
    T=((3,2),(4,3)).

Here q_D/D -> 0. In diagonal coordinates let

    s=F^(-1) mod N, h=3+2s mod N, q=-F mod N,
    U_0=S_h^(-1), B=W(q,1)+W(q,1)^*,
    U_e=exp(i e B) U_0,
    Bbar=K^(-1) sum_(j=0)^(K-1) U_0^j B U_0^(-j),
    X_K=sqrt(K/2) Bbar.

The dependence on the preceding argument is exactly the following two
hypotheses, stated here so the microscopic deduction can be audited
independently:

(H1) There is a unitary V_e for which, on the whole odd space,

    ||V_e U_e V_e^* - exp(i e Bbar)U_0||_(2,-)
                           <= 12 e^2/sqrt(K), K>=11,

where ||A||_(2,-)^2=Tr_-(A^*A)/D. Also U_0^K=I and [Bbar,U_0]=0.

(H2) The empirical measures of X_K tend weakly to the standard normal law,
and their second moments stay bounded.

The proposed proofs of H1 and H2 are in the Floquet normal-form note. They
must be assessed as analytic arguments, not inferred from finite tests.

For any real sequence tau_K=e_K sqrt(2K) tending to a finite tau,
telescoping H1 and using H2 gives

    D^(-1)Tr_-(U_(e_K)^(mK)) -> exp(-m^2 tau^2/2)             (9)

for every fixed integer m. Indeed the telescoping error is at most
6|m|tau_K^2/sqrt(K). Changing the characteristic-function argument from
m tau_K to m tau costs at most
|m||tau_K-tau| (Tr_-(X_K^2)/D)^(1/2), which tends to zero.
This also checks the variable-parameter step needed below.

**Corollary 2, conditional only on H1-H2.** If tau is nonzero, set

    chi(tau) = 2 sum_(m>=1) exp(-m^2 tau^2) > 0.

Then for every fixed L>0,

    liminf V_D(L) >= chi(tau) L^2,
    liminf R_D(phi_L) >= 1+chi(tau)-1/(sqrt(pi)L).             (10)

In particular uniformly unfolded second correlations cannot converge to
the orthogonal or unitary bulk reference. For tau=1, the single recurrence
m=1 and the fixed test L=16 already suffice. The gap between the lower
bound for the deterministic statistic and the upper bound (8) is at least

    2/e - 9/(16 sqrt(pi)) > 0.                              (11)

No numerical decimal evaluation is needed: e<3 and sqrt(pi)>1 make this
strictly greater than 2/3-9/16=5/48.

If tau=0, the sum in Theorem 1 is infinite. Thus V_D(L) diverges for every
fixed L>0, and R_D(phi) diverges for every test covered by (2). This is a
second-correlation divergence statement, not a claim about every bounded
point-process observable.

**Necessary scale.** Under H1-H2, convergence to the above uniformly
unfolded random-matrix second correlations requires

    |e_K| sqrt(K) -> infinity.                              (12)

Otherwise there is a bounded subsequence of tau_K, with a further convergent
subsequence. Equation (9) and (10), or their tau=0 version, contradict the
proposed correlation limit. Condition (12) is necessary, not sufficient.
It gives no theorem of universality in the supercritical regime.

## 5. Common unitary symmetry is not the explanation

Here is a separate finite statement, not using H1-H2. Let N be any odd
integer at least 3, and let a torus propagator for an integer symplectic
matrix ((A,B),(C,D)) have C invertible mod N. Its centered-Weyl kernel is,
up to a nonzero global scalar of modulus N^(-1/2),

    U(x,y)=exp_N((A x^2-2xy+D y^2)/(2C)).

This formula can be checked against the multiplication and translation
Weyl generators. Restrict to the odd basis (delta_x-delta_(-x))/sqrt(2),
1<=x<=(N-1)/2. For every such x,

    U_-(x,1)=c exp_N((A x^2+D)/(2C))
                    [exp_N(-x/C)-exp_N(x/C)] != 0.           (13)

Indeed 2 and C are units and x is nonzero mod N.
The diagonal cosine observable has entries 2cos(2pi x/N), all distinct on
this basis. A linear operator commuting with this observable must therefore
be diagonal. If it also commutes with U_-, (13) forces every diagonal entry
to equal the entry at x=1. Its common commutant is just the scalars.

For the Pell cat matrix C=4 is always invertible. Consequently there is no
nontrivial epsilon-independent unitary projector commuting with the whole
kicked family on its odd sector. To see the equivalence, commute with
exp(i epsilon B)U for every epsilon in a neighbourhood of zero and then
differentiate at zero. This establishes irreducibility of the pair (B,U).
It does not assert simple eigenvalues for every individual epsilon, or the
absence of antiunitary time reversal.

## 6. What the obstruction does and does not establish

The conclusion concerns actual propagator eigenphases and second factorial
statistics under uniform mean-density unfolding. It is stronger than a
fourth-moment statement about a compressed observable. Nevertheless it is
not a counterexample to a fixed-strength, fixed-system formulation of BGS:
the quantum kick tends to zero, and its corresponding classical amplitude
is smaller by a factor proportional to 1/N.

The mechanism is a spectral density modulation on the shrinking scale 1/K,
still much larger than the mean spacing 1/D. Let rho_tau be the density on
R/Z of a normal angle of variance tau^2 reduced modulo 2pi. Its Fourier
coefficients are exp(-m^2 tau^2/2), and

    integral_0^1 (rho_tau(u)-1)^2 du = chi(tau).

Thus chi is the surviving intensity-variance contribution. An adaptive
unfolding using this modulation can change the microscopic test and is
not ruled out by (10). No local-statistics theorem after that alternative
unfolding is supplied. Similarly, the estimate in H1 is normalized
Hilbert--Schmidt, not an eigenvalue-by-eigenvalue estimate on the 1/D scale.

The next scientific obligations are a source-audited priority comparison,
independent verification of H1-H2 and their hypotheses, and analysis of
local correlations after density-adapted unfolding or beyond the necessary
scale (12). No claim of completed numerical verification accompanies this
analytic continuation.
