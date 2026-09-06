# Two-window resonance crossover

Status: project theorem with a complete finite-difference proof. Priority, independent referee acceptance and analytic Lean formalization are not claimed. This is the smallest eigenvalue of a classical observable Gram matrix, not the spectral edge of a quantum Hamiltonian or a BGS eigenphase statistic.

## 1. The finite matrix and the result

Let A in SL(2,Z) be hyperbolic, C f=f composed with A^T, t=|tr A|, lambda=(t+sqrt(t^2-4))/2, and v!=0 an integer frequency. Fix q>=1 and R>=2q. Put

    b_v=e_v+e_(-v), s_v=i(e_v-e_(-v)),
    g_epsilon=(C^2-tC+I)^q b_v+epsilon s_v,
    h_r={g_epsilon,C^r g_epsilon}/(4 pi).

For n,m>=1 define the nm by nm Hermitian Gram matrix L_(R,n,m)(epsilon) of the L2 functions

    lambda^(-r) C^l h_r,
    R+1<=r<=R+n, 1<=l<=m.

The inner product is normalized Lebesgue measure on the torus. Let a=min(n,m).

**Theorem.** There are constants 0<c<C, depending only on A,v,q,R, such that for every n,m>=1 and every real epsilon,

    c (n^(-2q)+epsilon^2)(a^(-2q)+epsilon^2)
      <= lambda_min(L_(R,n,m)(epsilon))
      <= C (n^(-2q)+epsilon^2)(a^(-2q)+epsilon^2).           (1)

The constants do not depend on the two window lengths or on epsilon. This is a matching two-sided order estimate, not an assertion of an exact asymptotic leading constant.

For m>=n there is one threshold |epsilon| comparable to n^(-q), and (1) reduces to (n^(-2q)+epsilon^2)^2. For m much smaller than n there are two thresholds:

    |epsilon| much smaller than n^(-q):       n^(-2q)m^(-2q),
    n^(-q) much smaller than |epsilon|
             much smaller than m^(-q):       epsilon^2 m^(-2q),
    |epsilon| much larger than m^(-q):         epsilon^4.

The full expression (1) covers the transition regions as well. The spatial Fourier support of g_epsilon is fixed throughout: only the phase quadrature at v varies.

## 2. Exact reduction to a two-variable positive symbol

Choose eigen-covectors xi,eta normalized by det(u,w)=xi(u)eta(w)-eta(u)xi(w). Let

    u(theta)=2-2cos(theta),
    H(theta)=u(theta)[t^2-4+u(theta)].

The exact two-variable tail symbol from resonance_riesz_regularization.md is

    F_epsilon(omega,theta)
      =4 pi^2 xi(v)^2 eta(v)^2
          [lambda^(2q) H(theta)^q+epsilon^2]
          [lambda^(-2q) H(omega-theta)^q+epsilon^2].         (2)

This follows from

    |(z^2-tz+1)^q|^2 at z=lambda exp(i theta)
          =lambda^(2q)H(theta)^q

and the reciprocal-circle identity. The opposite oriented Fourier channels cancel the sine perturbation's mixed terms.

For this single-orbit family every output pair-gap k has the same additional squared row weight

    (1-lambda^(-2k))^2.

The degree of the temporal filter is 2q. Since r>R>=2q, all its output gaps satisfy k>=R+1-2q>=1. Therefore the actual finite Gram form is bounded above by the Toeplitz form with symbol (2) and below by

    [1-lambda^(-2(R+1-2q))]^2

times that form. This is a relative Loewner comparison, uniform in epsilon. No small additive remainder is used near a closing gap.

Finally H is bounded above and below by positive A-dependent multiples of u, because 0<=u<=4 and t^2-4>0. It suffices to prove (1) for the form with symbol

    [u(theta)^q+epsilon^2][u(omega-theta)^q+epsilon^2].       (3)

## 3. A finite-difference identity on the rectangle

Extend a coefficient array x_(r,l), 1<=r<=n,1<=l<=m, by zero to Z^2. Let D_1 be the first difference in direction (1,0), and D_2 the first difference in direction (-1,1). Their Fourier multipliers have squared moduli u(theta) and u(omega-theta), respectively. Thus the form (3) is exactly

    ||D_1^q D_2^q x||_2^2
      +epsilon^2(||D_1^q x||_2^2+||D_2^q x||_2^2)
      +epsilon^4 ||x||_2^2.                               (4)

All differences are on the zero extension; boundary terms are retained.

For a one-dimensional sequence supported on L consecutive sites, the first Dirichlet difference eigenvalue is

    4 sin^2(pi/(2(L+1))).

Fourier Jensen's inequality gives, for q>=1,

    ||D^q y||_2^2 >= [4 sin^2(pi/(2(L+1)))]^q ||y||_2^2
                  >= c_q L^(-2q)||y||_2^2.                 (5)

## 4. Lower bound

Horizontal chains have length at most n, so

    ||D_1^q x||_2^2 >= c_q n^(-2q)||x||_2^2.

Diagonal chains in direction (-1,1) have length at most a=min(n,m), so

    ||D_2^q x||_2^2 >= c_q a^(-2q)||x||_2^2.

The support of D_1^q x is contained in a rectangle of side lengths n+q and m. Its diagonal chains have length at most min(n+q,m)<=(q+1)a. Apply (5) first along these chains and then horizontally to x. The commuting differences give

    ||D_1^q D_2^q x||_2^2
       >= c'_q n^(-2q)a^(-2q)||x||_2^2.

Inserting all three inequalities into (4) gives the lower half of (1).

## 5. Upper bound

Use the explicit array

    x_(r,l)=f(r/(n+1))f(l/(m+1)),
    f(s)=s^(2q)(1-s)^(2q), 0<=s<=1,

and set f to zero off that interval. Its derivatives through order 2q-1 vanish at both endpoints. Standard integral formulas for finite differences, including those crossing the boundary, give for 0<=j<=2q

    ||D_r^j f_n||_2 <= C_q n^(-j)||f_n||_2,

with the finitely many small n included in the constant. Also ||f_n||_2^2 is bounded above and below by positive q-dependent multiples of n.

If E_r,E_l denote coordinate shifts, then

    D_2=E_r^(-1)(D_l-D_r).

Expand D_2^q by the binomial theorem. For the product array this gives

    ||D_1^q x||_2 <= C_q n^(-q)||x||_2,
    ||D_2^q x||_2 <= C_q(n^(-1)+m^(-1))^q||x||_2
                  <= C'_q a^(-q)||x||_2,
    ||D_1^q D_2^q x||_2 <= C_q n^(-q)a^(-q)||x||_2.

Substitution into (4) bounds this trial vector's Rayleigh quotient by the upper side of (1), finishing the proof.

## 6. Consequence for limit order

With a single translation time m=1 and epsilon=0, the lower edge has order n^(-2q). When the translation window is at least as long as the lag window, its order is n^(-4q). The difference is not a numerical artifact: the second low-frequency direction is available only when the simultaneous time window is long enough. Setting omega=0 before specifying the time window would miss this distinction.

No claim is made that this classical two-window law is the spectral form factor of a perturbed quantum cat map. A quantum transfer requires control of modular Fourier aliases and of the actual propagated dynamics, neither of which is supplied by covariance positivity alone.
