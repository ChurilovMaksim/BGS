# Joint limit of tensor path occupations and positive scattering currents

17 October 2026. Analytic continuation of positive_bernstein_path_law.md.
The limit here is K->infinity for a FIXED finite colligation. It does not
interchange K and N, identify a Haar law, or prove two-port universality.

## 1. Full occupation law

Let S in U(N), retain A={1,2}, E=A^c, r=N-2>=1, and put

    F(Z)=S_AA+S_AE(I-ZS_EE)^(-1)Z S_EA.

For source b=1,2 and a=3-b write f_b=F_ab, g_b=F_bb. If

    f_b(Z)^k g_b(Z)^(K-k)=sum_alpha c_(b,k,alpha) Z^alpha,

define a probability law on k=0,...,K and alpha in Z_+^r by

    Q_K(k,alpha)=(1/2)binom(K,k)sum_b |c_(b,k,alpha)|^2.      (1)

The earlier length measure is its pushforward L=|alpha|. Define torus
coordinates phi, boundary columns x_b(phi)=F(e^(i phi))e_b, and D_e=-i partial_phi_e.
At almost every phase the rational map is smooth and unitary. Put

    A_(b,e)(phi)=x_b(phi)^* D_e x_b(phi).                    (2)

These quantities are real and NONNEGATIVE. More explicitly, leave only the
marked e unclosed to get V_e=[[a_e,b_e],[c_e,d_e]], independent of phi_e.
For r_e=1-|d_e|^2>0 let Pi_e=b_e b_e^*/r_e and
tau_e=r_e/|1-e^(i phi_e)d_e|^2; set both to zero when r_e=0. Then

    partial_phi_e F=i tau_e Pi_e F,
    A_(b,e)=tau_e x_b^*Pi_e x_b>=0,
    sum_(b=1,2) A_(b,e)=tau_e.                             (3)

These are the actual quantum cavity directions and clocks, without replacement
by a classical absorption chain.

## 2. The joint limit and its first-moment strength

**Theorem.** For each fixed S and its fixed r, as K->infinity,

    Q_K law of (k/K,alpha/K)
        -> law of (T(phi),A_b(phi)) in W1,                 (4)

where phi is Haar on T^r, b is an independent uniform source in {1,2},
T=|F_12|^2=|F_21|^2, and W1 uses distance
|t-t'|+sum_e |a_e-a'_e|. No flatness, mixing, Gaussian input or irreducibility
is required. Uncoupled dark channels contribute zero correctly.

In particular the path occupations do not reduce to independent classical
steps when K grows. Their limiting randomness is the phase-dependent current
(3), jointly with the original T whose law is still unknown asymptotically.

### Exact characteristic function

For real s and theta in R^r, Parseval and the binomial theorem give

    E_(Q_K) exp{i[s k+theta.alpha]/K}
      =(1/2)sum_b integral_(T^r)
        [e^(is/K) f_b(phi+theta/K) conjugate(f_b(phi))
             +g_b(phi+theta/K) conjugate(g_b(phi))]^K dphi. (5)

Both boundary columns have norm one almost everywhere, and multiplication
of one output coordinate by e^(is/K) is unitary. Hence the bracket in (5)
has modulus at most one for almost every phi. At each regular phi it equals

    1+(i/K)[s T(phi)+theta.A_b(phi)]+O_phi(K^-2).          (6)

The exceptional pole/critical set has Haar measure zero. Dominated convergence
therefore sends (5) to the characteristic function of (4)'s right side.
Its continuity at zero and the characteristic-function continuity theorem
give weak convergence. In particular no second clock moment is assumed.

### Why convergence is in W1

For each fixed set of the other phases, dependence on z_e is a one-variable
matrix inner function of determinant degree zero or one. The exact degree/
Kac identity for its two tensor columns gives

    E_(Q_K)[alpha_e/K]=(1/2)E_phi tau_e<=1/2.              (7)

Equivalently apply the tensor differentiation identity
(x_b^tensor K)^*D_e(x_b^tensor K)=K x_b^*D_e x_b and Parseval, then integrate
the nonnegative one-variable clock. Its integral is 1 when r_e>0 and 0
otherwise, so there is no uncontrolled boundary derivative or UI assumption.
The right side of (7) is exactly E A_(b,e). The binomial marginal already
gives E_(Q_K) k/K=E T. All coordinates in (4) are nonnegative. Thus their
norm first moments agree at every K with the finite first moment of the
weak limit. Weak convergence plus convergence of norm first moments implies
W1 convergence, proving (4).

For irreducible |S|^2 all marked channels couple almost surely, so (7) is
exactly 1/2 for each e and the total mean current is r/2. Neither this
normalization nor (4) makes T uniform.

## 3. Exact second moments when the necessary integrals are finite

Fix real theta and put D_theta=sum_e theta_e D_e, A_b= x_b^*D_theta x_b,
V_theta=theta.alpha. Write E for phase and uniform-source averaging, and
P_a for the output projection onto the transmitted coordinate a=3-b.
If E||D_theta x_b||^2<infinity, then tensor differentiation and Parseval give

    E_(Q_K)(V_theta/K)^2
        =E A_b^2 + K^-1 E[||D_theta x_b||^2-A_b^2],        (8)
    E_(Q_K)(k/K)^2
        =E T^2 + K^-1 E[T(1-T)],                         (9)
    E_(Q_K)[k V_theta/K^2]
        =E[T A_b]+K^-1 E[Re(x_b^*P_a D_theta x_b)-T A_b]. (10)

To check (8), the derivative of x^tensor K has K terms. Equal-slot products
give K||D_theta x||^2; distinct-slot products give K(K-1)A_b^2. Divide by K^2.
The output count is a sum of the K commuting slot projections P_a. The same
equal/distinct slot division gives (9) and (10). After phase integration the
last expression is real, since the output-count operator commutes with
D_theta. Its real part may therefore be taken before integration.

The excess in (8) is nonnegative by Cauchy--Schwarz and ||x_b||=1. It is
the squared norm of the component of D_theta x_b orthogonal to x_b.
No second-moment conclusion is made when its displayed finiteness input fails.

## 4. A quantitative characteristic-function estimate under extra regularity

For ONE direction theta and source b let
u_b(phi)=s T+theta.A_b and

    R_b(phi)=s^2+2|s| ||D_theta x_b||+||D_theta^2 x_b||.

If these quantities have the indicated integrable squares/derivatives, Taylor's
formula along phi+t theta, invariance of torus measure, and |bracket|<=1 give

    | CF_(Q_K)(s,theta)-E exp(iu_b) |
       <= [E R_b+E u_b^2]/(2K).                          (11)

Here CF uses the normalized variables in (5) and E includes both sources.
Indeed, for a(phi,h)=x_b(phi)^* exp(is h P_a)x_b(phi+h theta),
the integrated remainder in a(phi,1/K)=1+i u_b/K+remainder is <=E R_b/(2K^2).
Also |exp(iu_b/K)-1-i u_b/K|<=u_b^2/(2K^2). Telescoping the Kth powers of
two complex numbers of modulus <=1 gives (11). No supremum of a rational
resolvent is used. Bound (11) is OPTIONAL; proof (4) uses only first moments.

## 5. What this changes and the unresolved order of limits

Formula (4) identifies the classical probability object underlying the high
tensor-power path law: a positive SCATTERING CURRENT. It gives joint endpoint/
occupation information that the binomial marginal and mean Kac law did not.
Equations (8)--(10) retain its fluctuations and correlations with transmission.

For an N-dependent family, (11)'s derivative moments may grow with N or be
infinite. No bound has been proved making their ratio to the previously chosen
K_N=floor((log N)^(2/3)) vanish. Consequently one cannot insert that K_N into
(4) without an additional uniform argument. Nor is the current (3) known to
have the Haar conditional law. These are explicit remaining obligations,
rather than a change of variables solving the conjecture.

The companion uniform_heisenberg_path_current.md now supplies a uniform-in-N
transfer under the additional fixed-level TV compactness input [TC], and extends
it to the entire normalized clock by sampling and UI. That further input was
not part of the fixed-S theorem above; the flatness-only assertion remains open.

Finite evidence: verify_tensor_current.py evaluates complete infinite Taylor
sums by rational generating functions in a nonconstant one-internal-channel
example. It checks (7)--(10) for K=1,...,6, including both sources. A polynomial
example checks all K=1,...,100. These
are finite controls; the general proof is (3)--(7).
