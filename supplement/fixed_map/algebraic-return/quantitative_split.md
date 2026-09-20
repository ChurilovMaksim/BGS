# From exact certificates to a quantitative splitting bound

Continuation of `exact_return_theorem.md`. These are self-reviewed
finite-dimensional deductions. They do not give a uniform microscopic
law, and no independent review of the new constants is asserted.

## 1. A weaker modular hypothesis suffices for normal matrices

Suppose B is normal over the complex numbers, with entries in a number
field, integral at a prime where reduction is defined. If its reduction
has a cyclic vector, B has simple spectrum in characteristic zero.
Indeed, lift the finite-field cyclic vector arbitrarily to the coefficient
ring. The determinant of its Krylov matrix is nonzero after reduction,
hence nonzero before reduction. Thus B is cyclic. A complex normal
matrix is diagonalizable, so a degree-N minimal polynomial forces N
distinct eigenvalues.

The rational-resolvent certificate in the companion note certifies this
cyclicity already through its degree-N denominator and coprime numerator.
Squarefreeness after reduction is an additional sufficient condition,
not a necessary one for a normal lift. The recorded programs intentionally
retain their stronger squarefree check, so none of their conclusions
depends on accepting a broader class of certificates.

For a control, the real symmetric matrix `[[1,2],[2,-1]]` has characteristic
polynomial x^2-5. Modulo 5 it is nonzero nilpotent, and the vector (1,0)
is cyclic (Krylov determinant 2). The reduction is not semisimple, but
the original eigenvalues are the distinct numbers plus/minus sqrt(5).

This observation does not supply cyclic vectors for the frozen model in
all dimensions. That is a remaining algebraic obligation.

The nonscalar-average witness from the companion note cannot replace that
obligation, even if A itself has simple spectrum. For example take
A=diag(0,3,1,2,4) and let M swap the first two and the next two coordinates,
fixing the fifth. Its average is diag(3/2,3/2,3/2,3/2,4), which is nonscalar.
But U(z) has both eigenvalues plus/minus exp(3iz/2) twice each, for every z,
and the fifth eigenvalue exp(4iz). Thus the general return-exclusion theorem
does not imply simplicity, even with an additional simple-A hypothesis.
This is an exact control, not an example in the frozen symbol family.

## 2. An elementary separation estimate from an algebraic certificate

Let B have N distinct eigenvalues and let H=DB have algebraic-integer
entries in a number field K of degree d. Suppose every complex embedding
sigma of K satisfies ||sigma(H)||op <= H0, with 2H0>=1. The characteristic
discriminant Delta of H is a nonzero algebraic integer. Consequently
its field norm is a nonzero integer, of absolute value at least one.
Each conjugate discriminant has absolute value at most
(2H0)^[N(N-1)]. Isolating the identity embedding gives

    |Delta| >= (2H0)^[-N(N-1)(d-1)].

If delta_H is the smallest eigenvalue distance of H, isolate its squared
factor in the product defining Delta and bound the other factors by
2H0. This proves

    min_gap(B) >= D^(-1) (2H0)^[1-d*N*(N-1)/2].             (1)

All algebraic conjugates are needed here. A norm bound in just the
chosen complex embedding would not justify (1).

For the certified frozen matrices B=G+tE, G=sqrt(N) M and
E=(1/R)sum_(r<R)Ad_M^r(A), take

    K=Q(zeta_(4N)),  d=phi(4N),  D=4000 R,
    C=643/500,
    H0=D [ceil(sqrt(N))+|t| C].                            (2)

The independent rational coefficient calculation gives ||A||op<=C by
the sum of absolute real and imaginary parts, including the scalar mean.
Every cyclotomic embedding commutes with complex conjugation; it preserves
Hermiticity and replaces roots of unity by roots of unity. Each conjugate
of G has norm sqrt(N), by the same quadratic character orthogonality
as G itself. The conjugates of E are unitary conjugation averages of
the corresponding conjugates of A, so their norms are at most C.
This proves (2) in every embedding. D clears every coefficient denominator.

With L defined by

    L=digits(D)+(d*N*(N-1)/2-1)*digits(2H0),

where digits is the number of decimal digits of a positive integer,
(1) implies min_gap(B)>=10^(-L). On a single M eigenspace, G is scalar;
thus the minimum separation in the corresponding compression of A is
at least delta=10^(-L)/|t|. Singleton blocks need no internal separation
condition. This bound is explicit but extremely small.

## 3. A quantitative first-order splitting theorem

Let M be unitary, with distinct eigenvalues separated by at least g,
0<g<=2. Let A be Hermitian, ||A||op<=C. Suppose each compression
A_j=P_j A P_j has simple spectrum, and within each block its eigenvalue
separation is at least delta, where 0<delta<=2C. For real epsilon with

    0<|epsilon| <= g*delta/(18 C^2),                        (3)

the matrix U=exp(i epsilon A)M has simple spectrum and

    min_gap(U) >= |epsilon|*delta/3.                       (4)

Here gaps are chordal distances on the unit circle, not unfolded gaps.

Proof: fix a block P with eigenvalue mu, and one eigenvalue a of PAP.
Use lambda=mu(1+i epsilon y) on the circle |y-a|=delta/3. On and inside
this circle, |y|<2C. In the complementary block Q, the inverse of
Q(lambda-U)Q exists and has norm at most 2/g, since

    |lambda-mu|<=2|epsilon|C,
    ||U-M||<=|epsilon|C,
    |epsilon|C<=g/9.

In the P Schur complement, division by i mu epsilon leaves
yI-PAP plus an analytic error bounded in operator norm by

    |epsilon| C^2 (1/2+2/g)
       <=3|epsilon| C^2/g <=delta/6.

The first term uses the real-unitary Taylor remainder
||exp(i epsilon A)-I-i epsilon A||<=epsilon^2 C^2/2.
The other term bounds the product of the two off-diagonal blocks
and the complementary inverse. On the y-circle the resolvent of PAP
has norm at most 3/delta. A linear homotopy in the Schur error never
has a zero determinant on the boundary. The argument principle therefore
gives exactly one eigenvalue, with algebraic multiplicity, in this disk.

Doing this for every a in every block counts all N eigenvalues. Within
a block, disk centers are separated by |epsilon|delta and disk radii
are |epsilon|delta/3, giving (4). Between different original blocks the
separation is at least g-4|epsilon|C>=5g/9, larger than the bound in (4).
The argument uses |epsilon| and works for both signs. QED.

For the cat matrix, if its projective period is R>=2, one may take
g=4/R: any two distinct projective R-th roots are separated by at least
2 sin(pi/R)>=4/R. Combining this with the modular certificate and (1)
gives an entirely explicit, but very small, interval (3).

## 4. What the quantitative attempt actually reaches

`quantitative_bounds.py` evaluates L and tests (3) against the prescribed
epsilon=N/10^80 using exact rational arithmetic. It never constructs
10^L when L is enormous. For N=3 the bound already covers this epsilon.
For the other recorded dimensions the conservative certified interval
is too small to cover it. The algebraic-specialization simplicity theorem
continues to apply at those dimensions; this particular quantitative
bound is insufficient. No estimate of the actual gap is inferred from
that failure.

An effective Lindemann--Weierstrass route was also checked at the primary
source: Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the
Exponentials of Algebraic Numbers*, ISSAC 2022,
[Theorem 1.2](https://arxiv.org/pdf/2112.05004v2). It provides a lower bound
depending on the number of exponential terms and the algebraic degrees
and heights. Applying it uniformly here would require estimates for the
eigenvalues and spectral projectors of A_N, collected frequencies and
coefficients of powers whose length grows with N. No useful Heisenberg
estimate follows from the qualitative specialization argument, and this
source is not being cited as supplying one.

Even a lower bound on the minimum gap is not by itself a CUE correlation
law. What remains is control of the distribution and coherent sum of
near-resonances at the correct N-dependent scale. The original target is
unchanged and unproved.
