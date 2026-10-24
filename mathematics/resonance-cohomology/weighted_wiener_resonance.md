# Uniform resonance synthesis and one-harmonic regularization

Status: project proof with explicit hypotheses; priority and full Lean verification are not claimed. This result concerns classical observables and their dynamical covariance, not local eigenphase statistics of a quantum propagator.

## 1. The space and the exact covariance

Let A be an integral two by two matrix of determinant one with |tr A|>2, and let C f = f composed with A^T on the normalized torus. Let lambda>1 be the expanding eigenvalue in modulus, mu=sign(tr A)*lambda, and let

    M1(f) = sum_(v != 0) |v| |fhat(v)|.

We consider real functions with M1(f)<infinity, modulo constants. Their first derivatives have absolutely convergent Fourier series. Every bracket

    h_r(g) = {g,C^r g}/(4 pi),  r>=1,

is a zero-mean function with absolutely summable Fourier coefficients. On the Hilbert space with one coordinate for each oriented nonzero A-orbit define

    J(f)_O = sum_(v in O) fhat(v),
    V_A(f) = ||J(f)||_2^2.

All series in this definition converge absolutely. Fourier orthogonality gives

    V_A(f) = sum_(j in Z) integral f * C^j f
           = lim_(n -> infinity) (1/n)||sum_(j=0)^(n-1) C^j f||_2^2.

Indeed the absolute sum of the correlations is at most ||fhat||_1^2: for two nonzero frequencies there is at most one integer iterate taking one to the other. This also justifies the variance limit without an unmentioned mixing theorem.

## 2. A two-visit lemma

For fixed nonzero integer u,v put k_r=u+A^r v. Omit k_r=0; its bracket coefficient is zero. The invariant quadratic form q_A(k)=det(k,Ak) satisfies

    q_A(k_r)=q_A(u)+q_A(v)+a mu^r+b mu^(-r),  ab != 0.

To see this, diagonalize A over the real quadratic field. In eigen-coordinates xi,eta, q_A is a nonzero constant times xi*eta. Neither coordinate vanishes on a nonzero integer vector: such a vector would yield a rational eigenvalue, impossible because tr(A)^2-4 is not a square. Expansion proves the formula and ab!=0.

For any fixed value c, the equation q_A(k_r)=c is a nonzero quadratic equation in z=mu^r after multiplying by z. The numbers mu^r are distinct, including when the trace is negative. Thus this equation has at most two indices r. In particular:

**Lemma. For a fixed ordered pair u,v, each oriented A-orbit is visited by k_r at most twice.**

This is an infinite-time statement, not a check up to a chosen cutoff.

## 3. A bounded bilinear synthesis operator

Let kappa_A=sup_(r>=1) lambda^(-r)||A^r||_op, which is finite by diagonalization. For finitely supported scalar sequences x define

    B_(g,f)x = sum_(r>=1) x_r lambda^(-r) J({g,C^r f}/(4 pi)).

**Theorem.** This extends to a bounded operator on l2(N), with

    ||B_(g,f)|| <= sqrt(2)*pi*kappa_A*M1(g)*M1(f).

For each fixed u,v, the corresponding Fourier-pair synthesis has one term in each column and at most two terms in each row, by the lemma. Cauchy--Schwarz in each row gives operator norm at most sqrt(2) times the maximum coefficient. The latter is bounded by kappa_A |u||v| because

    lambda^(-r)|det(u,A^r v)| <= kappa_A |u||v|.

Multiplication by pi and summation over u,v using the triangle inequality for bounded operators proves the claim. Absolute convergence in operator norm justifies exchanging the Fourier sums and the synthesis map.

For S_g=B_(g,g), bilinearity gives the explicit stability estimate

    ||S_g-S_f|| <= sqrt(2)*pi*kappa_A
                   *(M1(g)+M1(f))*M1(g-f).

Consequently G_g=S_g^* S_g is a bounded positive Gram operator and

    ||G_g-G_f|| <= 2*pi^2*kappa_A^2
        *(M1(g)^2+M1(f)^2)*(M1(g)+M1(f))*M1(g-f).

There is no logarithmic weight and no restriction to a finite number of lags. This supplies the uniform completion step needed by the smooth spectral-tail argument. It does not assert a positive lower bound for S_g on every infinite-dimensional lag space.

## 4. Every finite smooth hierarchy is regularized by one fixed harmonic

Fix b=c e_v+conjugate(c)e_(-v), with c!=0 and v!=0. Write G_m(g) for the Gram matrix of the unnormalized vectors J(h_1(g)),...,J(h_m(g)). The one-mode calculation gives

    G_m(b)_(r,s)=4*pi^2*|c|^4*det(v,A^r v)^2 * indicator_(r=s).

All diagonal entries are nonzero. The oriented orbits of v plus or minus A^r v are disjoint for different positive r, as follows from their q_A values q_A(v)*(2 plus or minus tr(A^r)); the absolute traces strictly increase. A vector and its negative lie in different oriented A-orbits.

**Theorem.** For arbitrary real g with M1(g)<infinity,

    D_m(t)=det G_m(g+t b)

is a nonnegative real polynomial of degree exactly 4m, with leading coefficient det G_m(b)>0. Hence at most 4m real coefficients t make the first m resonance classes dependent. Outside a countable set of t, the one perturbation g+t b has independent classes at every finite lag order simultaneously.

Proof: J(h_r(g+t b))=v_r+t w_r+t^2 z_r. Their exterior product is a Hilbert-valued polynomial of degree 2m, with nonzero leading coefficient z_1 wedge ... wedge z_m. The squared norm is D_m(t). This proves its degree and leading coefficient. Taking the countable union of finite exceptional sets finishes the argument.

These are zero-frequency dynamical covariance classes. The statement does not claim a common lower bound as m grows, or simultaneous positivity at every dynamical spectral frequency.

## 5. Explicit small-ball and negative-moment bounds

Set B_m=det G_m(b). Project the exterior product onto its leading coefficient and divide by B_m. In the real Hilbert space of real observables this produces a real monic degree-2m polynomial p_m with

    D_m(t) >= B_m*p_m(t)^2.

If a monic degree-d polynomial p obeys |p(t)|<=delta, at least one of its complex roots is within delta^(1/d) of t. Therefore the real sublevel set has length at most 2d*delta^(1/d). Taking d=2m gives

    Leb{t:D_m(t)<=epsilon*B_m} <= 4m*epsilon^(1/(4m)).

If T has density bounded by M, then

    P(D_m(T)/B_m <= epsilon)
        <= min(1,4m*M*epsilon^(1/(4m))),

and integrating the tail of the inverse variable gives

    E[(D_m(T)/B_m)^(-p)]
        <= (4m*M)^(4m*p)/(1-4m*p),  0<p<1/(4m).

The threshold is sharp uniformly over backgrounds: for g=0 the variable is T^(4m); a density bounded below near zero yields divergence for p>=1/(4m). Conditional versions require only a bound on the conditional density of T given the background.

For each m the positivity locus of G_m is open by the synthesis bound and dense by the one-harmonic theorem. Thus simultaneous finite-order nondegeneracy is residual in the real weighted Wiener space and in C-infinity. This genericity conclusion does not establish random-matrix statistics.
