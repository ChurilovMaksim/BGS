# A finite-symbol coherent normal form on prime Pell periods

Self-contained project proof, 2026-09-17; no priority claim. This extends
the mechanism of `mathematics/pell/pell_floquet_normal_form.md` from its single
harmonic to arbitrary fixed finite Fourier support, in full Hilbert–Schmidt
norm. It does not solve the fixed-coupling BGS limit.

Let K>=5 be an odd prime, N+F sqrt(2)=(1+sqrt(2))^K, and
S=[[3,4],[2,3]]. Use modular Weyl operators T_N and a unitary M with
M T(v) M*=T(Sv), normalized by a scalar so M^K=I.
Let

    A_0=f_0 I + sum_(v in Lambda) a_v T(v),
    a_(-v)=conjugate(a_v),
    F_0=sum |a_v|,       F_1=sum |a_v| ||v||_1,

where Lambda is finite and no v is zero modulo N. Gauge signs in a_v
do not affect the estimates. Put A_j=M^j A_0 M^(-j),

    Abar=(1/K)sum_j A_j,
    c_j=(K-1-2j)/(2K),     G=sum_j c_j A_j,
    ||X||_2^2=Tr(X*X)/N.

Then, for every real epsilon, with V=exp(-i epsilon G),

    ||V exp(i epsilon A_0) M V*
              - exp(i epsilon Abar) M||_2
        <=17 pi F_1^2 epsilon^2/sqrt(K).                    (1)

Also

    ||Abar-f_0 I||_2 <= F_0/sqrt(K),                        (2)
    ||exp(-i epsilon K f_0) (exp(i epsilon A_0)M)^K-I||_2
       <=sqrt(K) [F_0 |epsilon|+17 pi F_1^2 epsilon^2].     (3)

## Proof

Covariance and the c_j identity give

    G-MGM*=A_0-Abar.                                       (4)

Every nonzero Weyl label has orbit length K. Its length divides K;
a fixed label would be killed by S-I, whose determinant is -4 and is
a unit modulo the odd N. Primality of K therefore excludes all shorter
nonzero orbits. Consequently, for every nonzero r mod N,

    ||sum_j t_j T(S^j r)||_2^2=sum_j |t_j|^2.               (5)

Let gamma_(v,w,d) be the exact scalar in
[T(v),T(S^d w)]=gamma_(v,w,d) T(v+S^d w). Set lambda=3+2sqrt(2).
Replace d by d-K when d>K/2. Covariance modulo N preserves the
commutator modulus. The elementary bounds

    ||S^d||_(1->1)<=2 lambda^|d|,
    N>lambda^(K/2)/3,
    |gamma_(v,w,d)|<=2 pi |det(v,S^d w)|/N

imply

    |gamma_(v,w,d)|
       <=12 pi ||v||_1 ||w||_1 lambda^(-|d-K/2|).            (6)

The sine estimate in (6) uses an integer representative of the determinant;
modular midpoint signs affect its phase, not its modulus. Since K is odd,

    sum_d lambda^(-|d-K/2|) <=1,
    sum_d (|d-K/2|+1/2)lambda^(-|d-K/2|)<5/4.

These follow by summing twice the half-integer geometric series; the
first infinite sum is exactly 1. Also
|c_d|<=(|d-K/2|+1/2)/K. Expanding commutators, taking the operator
norm and summing (6) proves

    ||[G,A_0]||op <=15 pi F_1^2/K,
    ||[A_0,Abar]||op <=12 pi F_1^2/K.                       (7)

For the remaining commutator retain translation orthogonality:

    [G,Abar]=(1/K)sum_(d,v,w) a_v a_w gamma_(v,w,d)
                       sum_j c_j T(S^j(v+S^d w)).

If v+S^d w=0 mod N, its gamma is zero. Otherwise (5) bounds the
inner norm by sqrt(sum c_j^2)<=sqrt(K)/2. Hence

    ||[G,Abar]||_2 <=6 pi F_1^2/sqrt(K).                    (8)

For Hermitian X,Y and any unitarily invariant norm, unitary Duhamel gives

    ||exp(i t X)exp(i t Y)-exp(i t(X+Y))||
                             <=t^2 ||[X,Y]||/2.            (9)

Use (9) first for -G,A_0 and then for -G+A_0,MGM*. Their sum is Abar,
and the second commutator is [-G+A_0,Abar] by (4). Equations (7)-(8)
bound the resulting error by

    pi F_1^2 epsilon^2 [27/(2K)+3/sqrt(K)]
       <=17 pi F_1^2 epsilon^2/sqrt(K).

This proves (1), with no expansion in epsilon*||G||op. Equation (2)
follows from (5) and the triangle inequality over v. Finally Abar
commutes with M; telescoping K unitary factors in (1) and using
||exp(i H)-I||_2<=||H||_2 proves (3). Scalar f_0 and the projective
phase of M only rotate the spectrum. QED.

## Consequence for occupied spectral arcs

Suppose the right side of (3) is bounded by 0<b<=1/2. At least 3/4
of the eigenvalues satisfy |exp(i K(theta-epsilon f_0))-1|<=2b,
by Markov's inequality for the squared modulus. They lie in K arcs
of angular radius 2 arcsin(b)/K <=3b/K.

Divide these arcs into bins of angular length 2 pi/N. The number of
bins is <=K+3bN/pi<=K+bN. Their populations sum to at least 3N/4.
Cauchy–Schwarz, subtracting at most N diagonal labels, gives

    B_N >= (9/16)/(K/N+b)-1.                               (10)

Thus the entire finite Fourier symbol retains a coherent recurrence
when epsilon sqrt(K) is small, with an explicit nonlinear error.
For the frozen symbol, after subtracting f_0=1/10,

    F_0<=117/100,    F_1<=1483/200,    17 pi F_1^2<3000.

Equation (10) can therefore be applied at large prime indices using
only rational arithmetic and an upper bound on sqrt(K). This is a
coherent full-symbol estimate, not a phase-independent Markov bound.

The first-return and finite normal-form regime still leaves the original
target open: at fixed nonzero tau, epsilon=tau N eventually diverges.
No bound in (1)-(3) is asserted to remain small in that limit.

`finite_symbol_normal_form.py` checks the cohomological identity,
commutators and the direct Duhamel comparison at K=5,7, N=41,239,
for a genuinely two-dimensional, non-even symbol. The displayed
constants are proved above, not fitted to those finite examples.

Continuation, 18 September 2026: `sparse_orbit_theorem.md` removes the
prime-K assumption whenever 12(1+sqrt(2))R<lambda^(K/12), with R the
largest l1 frequency norm. In particular all odd K>=39 are admissible for
the frozen symbol. It also proves a sharper rational commutator certificate.
The fixed-coupling asymptotic limitation stated above is unchanged.
