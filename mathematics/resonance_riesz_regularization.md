# One-mode regularization of the full hyperbolic resonance lattice

**Stable claim IDs:** BGS-RES-014.

Status: project theorems with proofs. Independent referee acceptance, priority, and complete Lean formalization are not claimed. These are classical observable theorems, not microscopic BGS universality.

## 1. Two distinct Fourier variables

Let A in SL(2,Z) be hyperbolic, C f=f composed with A^T, lambda>1 the expanding eigenvalue in modulus, and mu=sign(tr A)*lambda. For a real zero-mean function g set

    M_s(g)=sum_(v!=0) |v|^s |ghat(v)|,
    h_r(g)={g,C^r g}/(4 pi),  r>=1.

Initially assume M1(g)<infinity. The bracket has absolutely summable Fourier coefficients and zero mean. Fix one representative v_O of each oriented nonzero A-orbit. Define its dynamical Fourier transform by

    J_omega(f)_O=sum_(j in Z) fhat(A^j v_O) exp(i j omega).

Thus J_omega(Cf)=exp(i omega)J_omega(f). Fourier orthogonality gives

    ||f||_L2^2=integral ||J_omega(f)||_l2^2 d omega/(2 pi).

The variable omega is dual to simultaneous time translation by C. A second variable theta below is dual to the lag index r. Neither is a quantum eigenphase.

For finite sequences x put

    S_g(omega)x=sum_(r>=1) x_r lambda^(-r) J_omega(h_r(g)),
    G_g(omega)=S_g(omega)^*S_g(omega).

## 2. Uniform boundedness, including all frequencies

Let kappa_A=sup_(r>=1)lambda^(-r)||A^r||_op. Then

    sup_omega ||S_g(omega)|| <= sqrt(2) pi kappa_A M1(g)^2.   (1)

The bilinear version is bounded by sqrt(2) pi kappa_A M1(g)M1(f). To prove it, fix two nonzero integer frequencies u,v. Every oriented A-orbit contains u+A^r v for at most two values of r. Indeed the invariant q_A(k)=det(k,Ak) has the form

    q_A(u+A^r v)=q_A(u)+q_A(v)+a mu^r+b mu^(-r), ab!=0.

A fixed value gives a quadratic equation in mu^r. The absence of rational eigenlines guarantees ab!=0. Thus the synthesis matrix for a fixed Fourier pair has at most two entries in each row and one in each column. Its coefficients have modulus at most pi kappa_A |u||v|; the dynamical Fourier phases have modulus one. Cauchy--Schwarz in each row and the triangle inequality over Fourier pairs prove (1).

In particular finite Fourier truncations converge to S_g uniformly in omega and in operator norm whenever they converge in M1. This is a uniform operator statement, not entrywise convergence.

## 3. The exact two-variable tail symbol

Choose real eigen-covectors xi,eta with

    xi(Av)=mu xi(v), eta(Av)=mu^(-1)eta(v),
    det(u,v)=xi(u)eta(v)-eta(u)xi(v).

Use representatives v_a for all oriented A-orbits, paired by v_(-a)=-v_a, and write

    P_a(z)=sum_j ghat(A^j v_a) z^j,
    X_g(theta)=sum_a xi(v_a)^2 |P_a(lambda exp(i theta))|^2,
    Y_g(theta)=sum_a eta(v_a)^2 |P_a(lambda^(-1)exp(i theta))|^2.

Both orientations are included. Reality gives coefficientwise conjugate filters on opposite orbits, so X_g,Y_g are even, continuous, nonnegative functions. The uniform convergence follows from

    sum_(a,j)|xi(v_a)|lambda^j |ghat(A^j v_a)| <= ||xi|| M1(g),

and its stable-coordinate analogue. Define

    F_g(omega,theta)=pi^2 X_g(theta)Y_g(omega-theta).         (2)

**Theorem 1.** For every real g with M1(g)<infinity,

    G_g(omega)=T(F_g(omega,.))+K_g(omega),                   (3)

where T is the Toeplitz operator on positive lag indices. The remainder K_g(omega) is compact, self-adjoint, and continuous in omega in operator norm. For finite Fourier polynomials it is trace class. No trace-class claim is made for arbitrary M1 data.

Proof for finite Fourier support. For sufficiently large pair gap k, the oriented orbits of v_a+A^k v_b are distinct for distinct ordered labels (a,b,k). A complete gap proof is given in phase_regularized_resonance.md: a four-atom quadratic-field relation with both internal pair gaps sufficiently large splits into two cross-cancellations, which force the labels to agree. It excludes every integer translate.

At the output label (a,b,k), a term from coefficients with times i,j and input lag r has k=r+j-i, is translated by A^i, and therefore acquires dynamical phase exp(i i omega). Its exact finite filter is

    R_(a,b)(omega,z)=P_a(lambda^(-1)exp(i omega)z^(-1))
                     P_b(lambda z).

The output of S_g(omega) on a sufficiently-high-lag vector x is

    pi sign(tr A)^k
       [eta(v_a)xi(v_b)-lambda^(-2k)xi(v_a)eta(v_b)]
       (R_(a,b)(omega,.)*x)_k.                             (4)

This follows by expanding the Fourier bracket and using
lambda^(-r)=lambda^(j-i)lambda^(-k). Taking squared norms, the constant part of the row weights has symbol

    pi^2 sum_(a,b)eta(v_a)^2 xi(v_b)^2 |R_(a,b)(omega,exp(i theta))|^2
        =F_g(omega,theta).

The remaining diagonal weights decay as O(lambda^(-2k)); the filters are finite and their omega dependence is continuous. The correction is trace class on the tail. The finitely many excluded input columns add a finite-rank correction.

For general g, approximate in M1 by finite Fourier polynomials. Equation (1) gives uniform operator-norm convergence of G. The Fourier absolute-sum estimates give uniform convergence of F on the two-torus. Toeplitz operators are bounded by the supremum norm of their symbols. Compact operators form a norm-closed ideal, so the remainders converge uniformly to a continuous compact-valued function. This proves (3).

## 4. The full translated resonance lattice

Let E_R project onto lag indices greater than R. Compactness and norm continuity on the compact omega circle imply

    sup_omega ||E_R K_g(omega)E_R|| -> 0.

Indeed cover the compact image of K_g by a finite operator-norm net and use the tail convergence of each compact operator in that net. Consequently

    lim_(R->infinity) inf_omega inf_(||x||=1,x=E_R x)
                       <x,G_g(omega)x>
       =pi^2 min_theta X_g(theta) min_theta Y_g(theta)
       =: c_infinity(g).                                  (5)

The lower bound follows from Toeplitz positivity. For the upper bound select theta at a minimum of X and omega-theta at a minimum of Y, and use increasingly long finite plane waves shifted to arbitrarily large lag indices.

**Theorem 2 (eventual Riesz criterion).** There exist R and c>0 such that, for every finite complex array x_(r,l) supported on r>R and l in Z,

    c sum_(r,l)|x_(r,l)|^2
       <= ||sum_(r,l) x_(r,l)lambda^(-r) C^l h_r(g)||_L2^2
       <= 2 pi^2 kappa_A^2 M1(g)^4 sum_(r,l)|x_(r,l)|^2      (6)

if and only if both X_g and Y_g are strictly positive on the circle.

Proof. The norm in (6) equals the integral of the Gram form G_g(omega) on the lag vector whose rth component is sum_l x_(r,l)exp(i l omega). Parseval and (1),(5) prove sufficiency. If c_infinity=0, choose a nearly-null high-lag vector at a minimizing omega and localize its dynamical Fourier mass near that frequency by a long scalar trigonometric polynomial. Continuity gives arbitrarily small ratios in (6), proving necessity.

The constants are uniform in both the number of lags and the simultaneous translation window. Thus this conclusion is stronger than positivity of each fixed finite-lag matrix or positivity only at omega=0.

## 5. Same-support phase repair of every even background

Suppose g is real and inversion-even. For any nonzero integer v put

    s_v=i(e_v-e_(-v)), g_epsilon=g+epsilon s_v.

The coefficients of the background's orbit filter are real. Opposite oriented channels cancel the mixed terms exactly, so

    X_(g_epsilon)=X_g+2epsilon^2 xi(v)^2,
    Y_(g_epsilon)=Y_g+2epsilon^2 eta(v)^2.

It follows that

    c_infinity(g_epsilon)
       >=4 pi^2 epsilon^4 det(v,Av)^2/(tr(A)^2-4)>0          (7)

for every epsilon!=0. Equation (6) holds on a sufficiently-high-lag tail with half the lower bound (7). The starting lag can depend on g and epsilon. When v is already supported, the perturbation adds no spatial Fourier frequency, only its sine quadrature.

This repairs the full two-index classical resonance lattice, not merely its zero-frequency covariance. It breaks inversion-evenness, so the resulting observable cannot be silently confined to an old odd quantum parity block.

## 6. Arbitrary smooth backgrounds: one complex coefficient is enough generically

Let g be real with M_(1+delta)(g)<infinity for some delta>0; every smooth g is included. Fix any nonzero v and change only its conjugate coefficient pair:

    g_(u,w)=g+(u+i w)e_v+(u-i w)e_(-v), (u,w) in R^2.

Choose v as the representative of its orbit and decompose its filter P=A0+i B0 with coefficientwise real A0,B0. The stronger Fourier moment makes their boundary functions on both radii lambda and lambda^(-1) continuously differentiable. A zero of the modified X requires

    A0(lambda exp(i theta))+u=0,
    B0(lambda exp(i theta))+w=0.

Thus every bad pair (u,w) lies on the compact rectifiable curve

    theta -> (-Re A0(lambda exp(i theta)),-Re B0(lambda exp(i theta))).

A zero of Y gives the analogous curve at radius lambda^(-1). Their union has two-dimensional Lebesgue measure zero.

**Theorem 3.** For almost every complex coefficient perturbation (u,w), including almost every one in an arbitrarily small disk, c_infinity(g_(u,w))>0 and the full Riesz inequality (6) holds eventually. Only one prescribed harmonic is varied.

The set of real M1 observables satisfying (6) is open and dense in the M1 topology. Openness follows from uniform continuity of X,Y. For density, first approximate by a finite Fourier polynomial, then apply the one-coefficient argument to it. The same property is open and dense in the smooth topology.

For a merely M1 background the curves need not be rectifiable; the almost-everywhere one-coefficient assertion is not extended to that borderline class by assumption.

## 7. Quantitative probability for the infinite-lattice gap

Let L_+,L_- be lengths of the two curves in Section 6, and let the random coefficient pair have a two-dimensional density bounded by M. If c_infinity(g_(u,w))<=epsilon, then min X<=sqrt(epsilon)/pi or min Y<=sqrt(epsilon)/pi. The corresponding coefficient pair lies within distance

    delta_+=epsilon^(1/4)/(sqrt(2 pi)|xi(v)|),
    delta_-=epsilon^(1/4)/(sqrt(2 pi)|eta(v)|)

of one of the two curves. The area of a delta-neighborhood of a rectifiable curve of length L is at most 2L delta+pi delta^2. Therefore

    P(c_infinity<=epsilon)
      <=min(1,M[2L_+delta_++2L_-delta_-+pi(delta_+^2+delta_-^2)]). (8)

In particular all negative moments of c_infinity of order p<1/4 are finite under this density bound, with constants explicit in (8). No optimality of the exponent for a fixed background is asserted.

This is a quantitative gap for a complete classical observable lattice. It does not supply joint traces or local resolvents of a perturbed quantum propagator at Heisenberg time. Exact finite quantum returns can obstruct transporting this classical bound unchanged; see information-theory/quadratic_response_limits.md.
