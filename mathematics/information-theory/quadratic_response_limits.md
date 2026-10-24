# Exact limits of quadratic-response data

Status: explicit algebraic consequences and counterexamples. This note does not claim a counterexample to microscopic universality after unfolding.

## 1. The preserved data

Let A=(2,1;1,1), C f=f composed with A^T, v=(1,0), w=Av, and z=v+w. Put B_u=e_u+e_(-u) and

    a=B_v+2 B_w+B_z,
    P(Z)=1-Z/2, Q(Z)=Z-1/2,
    f=P(C)a, h=Q(C)a.

The identity P(Z)P(Z^(-1))=Q(Z)Q(Z^(-1)) gives equality of all ordinary two-point temporal correlations of f and h. The finite-filter cancellation theorem also gives, for every r>=1,

    J({f,C^r f}/(4 pi))=J({h,C^r h}/(4 pi)),

where J is the vector of oriented Fourier-orbit sums. Therefore their entire bounded normalized resonance synthesis operators, and not just finitely many covariance matrices, agree.

Their high-lag Gram tails are coercive. The seed a has a constant orbit filter on the orbit of z, which is different from the orbit of v because det(z,Az)=5 and det(v,Av)=1. The exact tail symbol from phase_regularized_resonance.md gives

    F_a(theta)>=4 pi^2*25/(3^2-4)=20 pi^2.

Filtering by P multiplies this symbol by

    |P(lambda exp(i theta))P(lambda^(-1) exp(i theta))|^2,
    lambda=(3+sqrt(5))/2.

Both factors attain their minimum at theta=0. Their product squared there is

    (1-3/2+1/4)^2=1/16.

Hence the common tail symbol of f,h obeys F_f=F_h>=5 pi^2/4. Equality of the quadratic response data is therefore not caused by an uncontrolled soft tail.

## 2. A third moment not determined by those data

Exact Fourier multiplication gives

    integral a^3=24,
    integral a^2 C a=4,
    integral a (C a)^2=16.

Expanding the two cubes yields

    integral f^3=27, integral h^3=0.

For the physical integer Weyl convention Q_N(u)Q_N(v)=exp(pi i det(u,v)/N)Q_N(u+v), this becomes an exact finite-dimensional distinction. Both filtered symbols have max-norm frequency at most seven, so N>=22 excludes every nonzero three-term alias. Their closed-triangle phase histograms are respectively

    { -1:27/2, +1:27/2 } and the empty histogram.

Consequently

    (1/N)Tr Op_N(f)^3=27 cos(pi/N),
    (1/N)Tr Op_N(h)^3=0,                                  (1)

for every integer N>=22. The Hermitian observable spectra differ, although the ordinary two-point correlations and the entire zero-frequency Poisson-bracket response hierarchy agree.

This proves incompleteness for reconstructing all spectral moments. It does NOT prove that f and h have different unfolded microscopic universality classes, and does NOT identify the eigenphase law of exp(i epsilon Op_N(f))U_A. Such stronger conclusions would require new arguments.

## 3. What all-pass filtering does not preserve

The identity of zero-frequency classes is not an identity of every dynamical-frequency matrix. Already for the single seed b=B_v, q=1/2, and b_r={b,C^r b}/(4 pi), direct bilinearity gives

    h_r(P(C)b)=(1+q^2 C)b_r-q(C b_(r-1)+b_(r+1)),
    h_r(Q(C)b)=(C+q^2)b_r-q(C b_(r-1)+b_(r+1)).

Their difference is (1-q^2)(C-I)b_r. The single-mode dynamical spectra are orthogonal with weights 4 pi^2 det(v,A^r v)^2. At dynamical frequency pi, the cross-spectral entries between r=1 and r=2 are -12 pi^2 and +12 pi^2, respectively. Thus the stronger all-frequency claim, and an asserted identity obtained by multiplying the brackets by (1-qC)^2 and (C-q)^2, are false. They are not used in the corrected analysis.

The standard unitary all-pass operator (C-qI)(I-qC)^(-1) preserves L2 correlations, but need not preserve smoothness: its geometric expansion contains spatial derivatives growing exponentially under C^j. Smooth examples should use P(C)a,Q(C)a with a smooth seed, rather than silently assuming that the resolvent maps C-infinity to itself.

## 4. A separate cyclic-quantum transfer obstruction

Suppose a quantum map U_N has U_N^(K_N) scalar, and define

    H_(r,N)=(iN/2)[G_N,U_N^r G_N U_N^(-r)].

Then H_(r+K_N,N)=H_(r,N) and H_(K_N,N)=0, exactly. Any Gram matrix of more than K_N-1 such lag observables is singular, whatever positive Hilbert-space inner product is used; multiplying its columns by nonzero normalizations does not change this rank obstruction.

If a corresponding classical normalized resonance tail has lower bound c>0, as in the phase-regularization theorem, no singular quantum Gram block of the same size can approximate it in operator norm by an error below c: test a unit vector in the quantum kernel. This is a precise obstruction to uniformly transporting classical lag coercivity through an unperturbed cyclic quantum map at and beyond its return scale.

It is conditional on an exact scalar quantum return. It is not a theorem about a genuinely perturbed propagator whose period has been destroyed. In particular, it identifies a failed transfer mechanism, not a proof or disproof of generic BGS universality.
