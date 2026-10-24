# An exact tail symbol and phase regularization of smooth resonances

Status: project theorem with proof; external priority and full Lean formalization are not established. This is a theorem about the dynamical covariance of Poisson-bracket observables, not a local eigenphase law.

## 1. Definitions

Let A in SL(2,Z) be hyperbolic, Cg=g composed with A^T, lambda>1 its expanding eigenvalue in modulus, and mu=sign(tr A)*lambda. Choose real eigen-covectors xi,eta such that xi(Av)=mu xi(v), eta(Av)=mu^(-1)eta(v), and

    det(u,v)=xi(u)eta(v)-eta(u)xi(v).

For real g with M1(g)=sum_(v!=0)|v||ghat(v)| finite, put h_r={g,C^r g}/(4 pi). Let J collect Fourier coefficient sums on oriented nonzero A-orbits, and define S_g x=sum_r x_r lambda^(-r)J(h_r), G_g=S_g^*S_g. Boundedness on l2 follows from weighted_wiener_resonance.md.

Choose representatives v_a for ALL oriented A-orbits, with paired representatives v_(-a)=-v_a. Write

    ghat(A^j v_a)=c_(a,j), P_a(z)=sum_(j in Z)c_(a,j)z^j.

P_(-a) has coefficientwise conjugate coefficients. Both orientations are included in every following sum. Define

    X_g(theta)=sum_a xi(v_a)^2 |P_a(lambda exp(i theta))|^2,
    Y_g(theta)=sum_a eta(v_a)^2 |P_a(lambda^(-1) exp(i theta))|^2,
    F_g(theta)=pi^2 X_g(theta)Y_g(theta).                    (1)

These functions are continuous; X_g,Y_g are even. For example,

    sum_(a,j)|xi(v_a)| lambda^j |c_(a,j)|
      =sum_(v!=0)|xi(v)||ghat(v)| <= ||xi|| M1(g).

The stable-coordinate counterpart proves uniform convergence at the other circle. Under a representative change v_a -> A^t v_a, the filter becomes z^(-t) P_a(z). The weighted boundary functions xi(v_a) P_a(lambda exp(i theta)) and eta(v_a) P_a(lambda^(-1) exp(i theta)) each change by the modulus-one factor sign(tr A)^t exp(-i t theta). Reciprocal rescaling of xi,eta leaves F_g unchanged.

## 2. Exact finite-polynomial normal form

Suppose g has finite Fourier support. For sufficiently large positive k,k', the oriented orbits of v_a+A^k v_b are distinct for distinct ordered labels (a,b,k).

Here is the algebraic gap argument. Identify real eigen-coordinates with conjugate embeddings of a quadratic-field coordinate beta(v), in a fixed fractional lattice preserved by the algebraic unit mu. For the finite representative set bound both embeddings by M, and bound the absolute norm of a nonzero lattice element below by delta>0. In a vanishing four-atom relation, a gap B with lambda^B>16 M^2/delta splits the relation into independently vanishing pieces: the high piece has conjugate embedding at most 4M, so its real embedding is at least delta/(4M), and cannot be cancelled across that gap. Singleton pieces are impossible. If both k,k'>3B, a relation between two pairs splits into two cross-cancellations. Ordering the exponents forces the low atoms to match and the high atoms to match. Uniqueness of oriented representatives forces a,b,k to agree. This excludes all integer translates, not just a finite orbit window.

Set R_(a,b)(z)=P_a(lambda^(-1)z^(-1)) P_b(lambda z). For x supported at sufficiently large lags, the coordinate of S_g x at the orbit (a,b,k) is exactly

    pi * sign(tr A)^k
       *[eta(v_a)xi(v_b)-lambda^(-2k)xi(v_a)eta(v_b)]
       *(R_(a,b)*x)_k.                                    (2)

The term with k=r+j-i has Fourier product c_(a,i)c_(b,j); simultaneous translation by A^i preserves the determinant, and lambda^(-r)=lambda^(j-i)lambda^(-k). This proves (2), including complex Fourier phases and either trace sign.

The constant part of the squared Gram form is Toeplitz, with symbol

    pi^2 sum_(a,b)eta(v_a)^2 xi(v_b)^2 |R_(a,b)(exp(i theta))|^2
       =pi^2 Y_g(-theta)X_g(theta)=F_g(theta).

The other diagonal weights differ from their limits by O(lambda^(-2k)). With finitely many channels and finite filters this is trace class on the high-lag tail. The excluded input columns contribute a finite-rank correction. Hence G_g-T(F_g) is trace class for every finite Fourier polynomial.

## 3. Completion to the weighted Wiener space

Finite Fourier truncations g_L converge in M1. The uniform synthesis bound gives G_(g_L)->G_g in operator norm. Section 1 gives uniform convergence of F_(g_L), hence norm convergence of their Toeplitz operators. Compact operators form a norm-closed ideal, so

    G_g=T(F_g)+K_g, K_g compact.                           (3)

Trace class for arbitrary M1 data is not inferred. If E_R projects onto lag indices greater than R, then

    lim_(R->infinity) inf_(||x||=1, x=E_R x) <x,G_g x>
          =min_theta F_g(theta).                         (4)

The lower bound is Toeplitz positivity and ||E_R K_g E_R||->0. The upper bound uses long finite plane waves centered at a minimizing frequency and translated to arbitrarily large indices. Their Toeplitz forms converge to that symbol value and the compact term vanishes. Thus a uniformly coercive sufficiently-high-lag tail exists exactly when F_g has no zero.

## 4. A sine quadrature repairs every real-even background

Assume g is real and inversion-even, so its Fourier coefficients are real. For any nonzero integer v set

    s_v=i(e_v-e_(-v))=-2 sin(2 pi v.x), g_epsilon=g+epsilon*s_v.

The opposite oriented orbit filters receive opposite imaginary increments. Their squared moduli cancel the mixed terms exactly:

    X_(g_epsilon)=X_g+2 epsilon^2 xi(v)^2,
    Y_(g_epsilon)=Y_g+2 epsilon^2 eta(v)^2.                  (5)

Therefore, for every epsilon!=0,

    min F_(g_epsilon)
      >=4 pi^2 epsilon^4 xi(v)^2 eta(v)^2
       =4 pi^2 epsilon^4 det(v,Av)^2/(tr(A)^2-4)>0.         (6)

The bound is independent of the background. By (4), a sufficiently-high-lag actual Gram tail is bounded below by half this number. The required starting lag can depend on g and epsilon.

If v is already supported, no new Fourier frequency is introduced: only an existing mode's phase quadrature changes. This covers smooth infinite-support backgrounds as well as finite polynomials. It breaks inversion-evenness and cannot be silently restricted to an odd parity block that the perturbed observable no longer preserves.

## 5. An explicit same-support crossover

Let t=|tr A|, b_v=e_v+e_(-v), q>=1 fixed, and

    g_0=(C^2-t C+I)^q b_v, g_epsilon=g_0+epsilon*s_v.

Set u(theta)=2-2cos(theta), H(theta)=u(theta)[t^2-4+u(theta)]. Then exactly

    F_(g_epsilon)=4 pi^2 xi(v)^2 eta(v)^2
      *[H^(2q)+(lambda^(2q)+lambda^(-2q))*epsilon^2*H^q+epsilon^4].  (7)

For the n by n Gram block of normalized lags R+1,...,R+n, with fixed R>=2q, positive constants independent of n and epsilon give

    lambda_min(G_(R,n)(g_epsilon))
          comparable to (n^(-2q)+epsilon^2)^2.              (8)

The one-mode normal form has a common row weight (1-lambda^(-2k))^2, bounded above and below for k>=R+1-2q. The finite Gram matrix is therefore uniformly Loewner-comparable to T_n(F_(g_epsilon)), without an epsilon-dependent additive error. H is comparable to u. Lower bounds for T_n(u^q) and T_n(u^(2q)) follow from the first Dirichlet difference eigenvalue and Jensen's inequality. For matching upper bounds use x_j=(j/(n+1))^(2q)(1-j/(n+1))^(2q), extended by zero; its differences of orders q and 2q give n^(-2q) and n^(-4q), including boundary terms. Inserting these estimates in (7) proves (8).

The phase threshold is |epsilon| comparable to n^(-q). Below it the n^(-4q) soft law persists; above it the lower edge is comparable to epsilon^4. This is a proved covariance crossover at fixed spatial support, not a fit to quantum level statistics and not BGS universality.
