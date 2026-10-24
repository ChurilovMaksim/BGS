# Exact Gaussian reciprocity for the complete WKB path sum

Project finite identity, independently internally reviewed on 6 October 2026.
Gaussian reciprocity is classical; no priority claim.

## 1. Result and scope

For every fixed finite WKB order J, every odd N, and EVERY m>=1, the trace
of the explicit matrix V_(N,J)^m has the exact representation (G6) below.
It includes all 4^m branches and all winding classes, with their exact
normalizations. The FULL nonlinear fixed-tau phase remains in the integrand.
No stationary-phase approximation, action linearization, long-time Egorov
estimate, or global contour deformation is used to obtain this identity.

Combined with factorial_wkb_reduction.md, it is an exact Gaussian-operator
representation of a surrogate for every fixed TRACE-005 order and compact
Heisenberg band, with the already-quantified operator replacement error.
It does not estimate the resulting signed winding-class sum.

## 2. Cyclic quadratic form and periodic nonlinear factor

Write x_m=x_0 and r=(r_0,...,r_(m-1)) in {0,1,2,3}^m. Let P_m be the
cyclic shift and define

B_m=6I-P_m-P_m^T,  K_m=B_m/4,
t_(r,j)=r_j-3r_(j-1).

For m=1 this gives B_1=[4]; for m=2 the off-diagonal entry is -2.
Thus repeated neighbours are counted correctly. B_m is positive integral,
with diagonal even, and

D_m:=det B_m=(3+2sqrt(2))^m+(3-2sqrt(2))^m-2.          (G1)

The zero-time cyclic action is exactly

Phi_r^0(x)=-(1/8)x^T B_m x +(1/4)t_r^T x -(3/8)sum_j r_j². (G2)

Put
A_r(x)=product_j [sum_(ell=0)^J N^-ell a_(r_j,ell)(tau,x_j,x_(j+1))],
F_r(x)=exp(2pi i N[Phi_r(tau,x)-Phi_r^0(x)]) A_r(x).

The nonlinear phase corrections and amplitudes are 4-periodic in each
coordinate, by the published phase/transport gluing.
Indeed under a coordinate shift by 4 the phase changes by an affine
polynomial with integral derivative; periodicity of the Hamiltonian and
Hamilton–Jacobi uniqueness preserve that change. Higher phase derivatives
are unchanged, while first derivatives enter periodic symbol coefficients.
Transport uniqueness preserves amplitude periodicity at each fixed order.
Analytic characteristic flow and its invertible projection, followed by
finite analytic transport induction, give real analyticity. Compactness of
the fixed-dimensional torus yields a positive complex strip and absolute
Fourier summability. Strip norms may grow exponentially in N and m; no
dimension-uniform Wiener norm follows. Thus F_r is analytic
and 4-periodic on R^m. Its Fourier series is absolutely convergent for
each fixed N,m (no dimension-uniform Fourier norm is asserted):

F_r(x)=sum_(ell in Z^m) Fhat_r(ell) exp(2pi i ell.x/4).

On the SAMPLING lattice, the complete branch sum is also 1-periodic in
each x coordinate, by the exact gluing identities for V. Consequently

sum_(j in {0,...,N-1}^m) sum_r e(N Phi_r^0(j/N))F_r(j/N)
 =4^-m sum_r sum_(j in {0,...,4N-1}^m)
                 e(N Phi_r^0(j/N))F_r(j/N).           (G3)

Only the complete branch sum has been extended in (G3); an individual
branch is not incorrectly declared 1-periodic off the sampling lattice.

## 3. Finite Gaussian reciprocity, including its proof

For a symmetric positive-definite integral matrix B, even L, and integer a, with the finite quadratic
chirp well-defined modulo L, one has

sum_(j mod L) e(-j^T B j/(2L)+a.j/L)
 = e^(-i pi m/4) L^(m/2)/(sqrt(det B))
   sum_(nu in Z^m/B Z^m)
       e((L/2)(nu+a/L)^T B^-1(nu+a/L)).              (G4)

Here e(z)=exp(2pi i z). The representatives on the right do not matter:
shifting nu by Bz changes the phase by an integer since L is even.
Our application has L=4N and the positive even-diagonal B_m above.
There is NO hypothesis gcd(N,det B)=1: the inverse is over R/Q, never
a modular inverse. Resonant dimensions are included without removal.

A self-contained proof uses ordinary Poisson summation on
exp[-pi(epsilon+i/L)x^T Bx+2pi i a.x/L]. On the original lattice,
grouping modulo L and letting epsilon decrease to zero gives common
Gaussian divergence epsilon^(-m/2)/(L^m sqrt(det B)) times the left finite
sum. On the Fourier side the Gaussian prefactor tends to
L^(m/2)e^(-i pi m/4)/sqrt(det B). Grouping Fourier indices modulo B Z^m
gives exactly the same common divergence times the finite sum on the right.
The phase first has nu-a/L; replace nu by -nu to get (G4).

For completeness, the real Fourier damping is
 epsilon L²/(1+epsilon²L²) times the B^-1 quadratic form.
Its lattice scale is epsilon^(-1/2), while the error in the limiting
quadratic phase coefficient is O(epsilon²). Their product is O(epsilon),
so the grouped Gaussian Riemann sums converge to the claimed factors.
Gaussian domination after rescaling justifies the limit. This argument
proves a finite identity at each m,N; it needs no asymptotic uniformity
in their subsequent values.

## 4. The Fourier-defined Gaussian operator

For a 4-periodic F in the Wiener algebra (sum_ell |Fhat(ell)|<infinity), define

(G_(N,B) F)(x)=sum_ell Fhat(ell)
 e(ell^T B^-1 ell/(8N)) e(ell.x/4).                    (G5)

Pointwise values in (G5) are defined by absolute Fourier convergence on this
class. Its abstract L² extension alone does not supply point evaluation.
Its Fourier multiplier has unit modulus, so G_(N,B) is unitary on the
4-periodic L² space. This does NOT give a uniform bound on its values at
the sampled stationary centers.

Choose any representatives nu of Z^m/B_m Z^m, and put

x_(r,nu)=B_m^-1(t_r+4nu),
A_(r,nu)^0=(t_r+4nu)^T B_m^-1(t_r+4nu)/8
                        -(3/8)sum_j r_j².

Substitute the absolutely convergent Fourier series of F_r into (G3)
and apply (G4) with a=N t_r+ell, L=4N. Expanding the quadratic form shows
that its ell-linear part is ell.x_(r,nu)/4 and its ell-quadratic part is
ell^T B_m^-1 ell/(8N). Therefore the EXACT trace identity is

Tr V_(N,J)^m
 = e(3mN/8) e^(-i pi m/4)/(4^m sqrt(D_m))
   sum_(r in {0,1,2,3}^m) sum_(nu mod B_m)
       e(N A_(r,nu)^0) (G_(N,B_m) F_r)(x_(r,nu)).     (G6)

The normalization comes from
(2sqrt(N))^-m *4^-m *(4N)^(m/2)=4^-m.
Neither the 4^m branch count nor the D_m winding count is hidden in an
error constant. The 4^-m average is part of the exact formula.

Representatives remain immaterial in (G6): nu->nu+Bz shifts x by 4z,
and changes A^0 by the integer z.(t+4nu)+2z^T Bz.

## 5. Exact global Fresnel-integral interpretation

For K=B/4, the operator in (G5) is also

e^(i pi m/4) sqrt(det K) N^(m/2)
 lim_(epsilon down to 0) integral_(R^m)
   exp(-pi epsilon |y|²) e(-N y^T K y/2) F(x+y) dy.   (G7)

To verify this, insert a single Fourier mode. The elementary Gaussian
integral gives exactly the multiplier in (G5); its damped modulus is
uniformly bounded as epsilon decreases to zero. Absolute convergence of
the Fourier coefficients then allows dominated summation. Thus (G7)
is a defined center-based Abel/Fresnel integral: damping is in y about the
chosen center x. No cutoff-independent improper integral or contour rotation
is asserted. Comparison to U uses the separate finite-order norm error in
[factorial WKB reduction](factorial_wkb_reduction.md), never equality U=V.

For x=x_(r,nu), the phase after multiplying by e(N A^0) is precisely

Phi_r(tau,x+y)+nu.(x+y),

because Phi_r^0(x+y)+nu.(x+y)=A^0-y^T K y/2. Thus (G6) gives genuine
global oscillatory integrals for the full nonlinear lifted actions, with
an explicit Gaussian regularization. It avoids choosing compact real
chart cutoffs at this stage.

Each such real phase has a unique global stationary point near its cat
center: write its stationary equation y=K^-1 grad(Phi_r-Phi_r^0)(x+y).
The nonlinear gradient has a sufficiently small global Lipschitz row norm
at the fixed tau, and K^-1 has row sum one. Hence this is a contraction
on R^m, uniformly in m and the lifted class. Its displacement is bounded
by a fixed O(tau) constant in max norm. This is an equation for the
lifted phase, not a claim that the overcomplete (r,nu) list is a list of
distinct physical periodic orbits.

## 6. What is solved, and what is not

The exact global identity removes one bookkeeping ambiguity: the initial
conversion from the finite lattice path sum to lifted global Fresnel
integrals does not require the unresolved plane-to-odd-torus trace theorem
or a speculative saddle approximation. It uses the actual four-branch
sampling identities and finite Gaussian reciprocity only.

A uniformly controlled saturated-contour deformation and summed tail are
now proved in [the global rotated-box theorem](global_rotated_box_trace.md),
conservatively for m<=2N, with additional strictly bounded bandwidths
stated there. The periodic nonlinear factor is not rotated along an
unbounded imaginary ray. This is a separate theorem; (G7) alone does
not supply the deformation or its estimates.
Despite that finite-band deformation, the local O(N^-1/2) relative first-loop error
cannot be summed absolutely over exponentially many classes at m~N.
An optimal remainder or a signed/operator-level collective resummation is
still necessary. The L² unitarity in (G5) does not control the winding-center
sampling functional and therefore does not establish that cancellation.

## Verification boundary

Portable independent exact cyclotomic controls and their finite coverage are
recorded in the execution receipt. No numerical test certifies a uniform
Heisenberg winding-sum estimate.
