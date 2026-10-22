# Entire temporal gauges and a regularity obstruction

**Stable claim IDs:** BGS-RES-018.

Status: self-contained project proof. All-pass filters and functional calculus are prior concepts; priority for their application to the complete resonance hierarchy is not established. The preserved data below are zero-frequency cohomological classes, not all dynamical-frequency cross spectra.

## 1. A classified group of smooth unitary filters

Let C be composition with a hyperbolic toral automorphism. Let P be holomorphic on C minus {0}, with real Laurent coefficients p_j, and assume

    |P(exp(i theta))|=1.

Its Laurent coefficients are absolutely summable with every exponential weight. Thus

    T_P g=sum_(j in Z) p_j C^j g

defines a continuous invertible operator on every weighted Fourier space M_s(g)<infinity and on C-infinity. On L2 it is unitary. Its inverse and adjoint are T_(P(1/z)).

**Theorem 1 (entire real all-pass classification).** Such P are exactly

    P(z)=sigma z^n exp(H(z)),
    sigma in {+1,-1}, n in Z,
    H(z)=sum_(k>=1) a_k(z^k-z^(-k)), a_k real,              (1)

where H is holomorphic on the punctured plane.

Proof. Reality and unit modulus on the circle give P(z)P(1/z)=1 by analytic continuation, so P has no zero on the punctured plane. Let n be its winding number and sigma=P(1). The nonvanishing function P(z)/(sigma z^n) has zero winding, hence a global holomorphic logarithm H normalized by H(1)=0. Reality gives H(conjugate(z))=conjugate(H(z)); reciprocity gives H(z)+H(1/z)=0. Comparing Laurent coefficients proves (1). Conversely (1) has all the stated properties.

Cauchy estimates on arbitrarily large and small circles imply sum_j |p_j|R^|j|<infinity for each R>1. Composition by C^j grows at most exponentially in |j| on each fixed smooth seminorm or weighted Fourier norm. This proves continuity on all those spaces. The identities T_P^*=T_(P(1/z)) and P(z)P(1/z)=1 prove unitarity and the inverse formula.

## 2. The entire quadratic resonance hierarchy is preserved

For real g with M1(g)<infinity set h_r(g)={g,C^r g}/(4 pi), for integer r, including h_0=0. Then

    h_r(T_P g)=sum_(i,j) p_i p_j C^i h_(r+j-i)(g).

All sums converge in Fourier l1. In particular, collecting orbit sums gives

    J(h_r(T_P g))=J(h_r(g)) for every r.                    (2)

Indeed the coefficients sum_i p_i p_(i+n) equal delta_(n,0), by P(z)P(1/z)=1. Reordering is legitimate because the Fourier l1 norm of h_s grows at most exponentially in |s| and the p_j have every exponential moment.

There is also an explicit L2 transfer function, not merely equality of orbit sums. Define

    T_i=sum_(l=0)^(i-1) C^l                  for i>0,
    T_0=0,
    T_i=-sum_(l=i)^(-1) C^l                 for i<0.

Then (C-I)T_i=C^i-I, and

    h_r(T_P g)-h_r(g)=(C-I)F_r,
    F_r=sum_(i,j) p_i p_j T_i h_(r+j-i)(g).                 (3)

The series for F_r converges in L2 since ||T_i||<=|i| and the weighted coefficient sums converge. When g is smooth, it converges in every smooth seminorm. Thus the whole quadratic hierarchy is preserved modulo actual L2 coboundaries, and modulo smooth coboundaries for smooth backgrounds.

The linear correlations are preserved as well, since T_P is unitary and commutes with C. The bounded zero-frequency synthesis operator and its entire Gram operator therefore agree before and after this transformation.

## 3. Explicit nontrivial smooth flows

For real a,

    P_a(z)=exp[a(z-z^(-1))],
    T_a=exp[a(C-C^(-1))]

is a nontrivial one-parameter group with all the properties above. More generally one can exponentiate any finite real combination of C^k-C^(-k). This supplies commuting families of arbitrary finite parameter dimension.

These exponentials are continuous on C-infinity. They must be distinguished from the rational all-pass resolvent (C-qI)(I-qC)^(-1), whose geometric coefficient decay does not generally compensate for the growth of arbitrarily high spatial derivatives.

At the two-radius boundary functions used for the resonance tail,

    X_(T_a g)(theta)=exp[2a(lambda-lambda^(-1))cos(theta)] X_g(theta),
    Y_(T_a g)(theta)=exp[-2a(lambda-lambda^(-1))cos(theta)] Y_g(theta).

Their product, and hence the zero-frequency tail symbol, is unchanged. At nonzero dynamical frequency omega the multiplier is instead

    exp[2a(lambda-lambda^(-1))(cos(theta)-cos(omega-theta))],

which is generally not one. The all-frequency invariance claim is therefore explicitly excluded.

## 4. Preserved response does not determine even a cubic observable moment

Take A=(2,1;1,1), v=(1,0), w=Av, z=v+w and

    g_*=B_v+2B_w+B_z, B_u=e_u+e_(-u).

Exact Fourier multiplication gives

    integral g_*^3=24,
    integral g_*^2 Cg_*=4,
    integral g_*(Cg_*)^2=16.

For g_a=T_a g_* all the linear correlations and all classes (2) agree for every a. But

    d/da integral g_a^3 at a=0
       =3 integral g_*^2(C-C^(-1))g_*=-36,

so

    integral g_a^3=24-36a+O(a^2).                           (4)

Thus the continuous gauge family has genuinely different cubic moments.

For physical torus Weyl quantization of each fixed smooth symbol,

    lim_(N->infinity) (1/N)Tr Op_N(g_a)^3=integral g_a^3.

A direct proof expands the trace in Fourier triples. A fixed nonzero total frequency is eventually not a multiple of N; a zero-sum triple has Weyl phase tending to one. Fourier l1 summability bounds the entire triple sum, so dominated convergence applies. Hence sufficiently small nonzero a also changes the large-N observable spectral moments.

This does not show different unfolded microscopic universality classes, and does not identify the eigenphases of a kicked propagator. It proves that the complete quadratic-response data are insufficient to reconstruct all observable spectral moments.

## 5. Nontrivial entire gauges of one harmonic are never finite-Gevrey

Let b_v=e_v+e_(-v), v!=0, and suppose T_P b_v obeyed, for some alpha,c,C>0, the spatial Fourier bound

    |ghat(k)|<=C exp(-c |k|^alpha).                          (5)

Along the hyperbolic orbit this implies

    |p_j|<=C' exp(-c'lambda^(alpha |j|)),

because |A^jv| is bounded below by a positive multiple of lambda^|j|. In particular |p_j|<=C''exp(-c''j^2). Gaussian summation then bounds

    log max_(|z|=rho)|P(z)|=O(1+|log rho|^2)

at both ends rho->infinity and rho->0.

Using the logarithm H from (1) and P(z)P(1/z)=1, these two bounds give

    sup_theta |Re H(rho exp(i theta))|=O(1+|log rho|^2).

For every k>=1 its angular Fourier coefficient is

    a_k(rho^k-rho^(-k))/2.

Letting rho tend to infinity forces a_k=0. Therefore H=0 and P(z)=sigma z^n.

**Theorem 2.** A nontrivial entire real all-pass filter applied to one nonzero harmonic produces a smooth observable which satisfies no bound (5) for any alpha>0. In particular it belongs to no finite Gevrey class. The only gauges of this type retaining such Fourier decay are sign changes and time translations.

This is a statement about the image of a single harmonic under an entire temporal filter. It does not eliminate the finite-polynomial homometric examples, whose transfer ratios are rational rather than entire, and does not prove identifiability of arbitrary analytic observables from quadratic response.
