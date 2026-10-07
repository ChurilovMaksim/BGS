# Flat compact-pinching families need not have negligible signed one-pinch echoes

Research corollary using an existing changed-family witness. This is NOT a
counterexample to the unchanged kicked cat map, FM-029, or BGS.

## Counterexample and exact statement

Reuse the period-six family from the pinned source
`evidence/research_checkpoint_20261007/raw/bgs_astra_signed_boundary/bilinear_carry_counterexample_v2.md`,
B1--B4. For primes p>=5, p=2 mod 3, N=p^2, put

    f(x+p y)=(x^3,y^3) in F_p^2,
    A=[[1,1],[0,1]],
    U_N(j,k)=p^-1 exp(2pi i f(j)^T A f(k)/p).

The source gives elementary complete/incomplete sum and literal cyclic-carry
proofs of all the following; the family is credited there rather than claimed
as a new construction:

    U_N^6=I,  |U_N(j,k)|^2=1/N,  P_N=J_N,
    ||Q_N||=N^-1/2,
    ||D_N-J_H|| <=epsilon_N ->0,
    epsilon_N^2 <=p^-1+2sqrt(2)(2+log p)p^-1/4.

Here Q_N(j,k)=U_N(j,k)conjugate(U_N(k,j)), and J_H is the rank-one identity
projection on End(C^N). The charge projectors are the actual CYCLIC Z/N
coordinate charges, not vector-group translations. Thus D_N has the strongest
possible uniform finite-rank approximation: rank one plus a vanishing
operator-norm error. A fixed centered charge gap follows eventually.

For the SAME one-pinch definition and the SAME full occupation subtraction as
in `one_pinch_averaged_lemma.md`, every nonzero nonnegative
w in C_c^infinity((a,b)), 0<a<b<infinity, satisfies

    liminf_(N=p^2) N^-2 sum_m w(m/N)
       [E_N,m(0)-integral E_N,m(theta)dtheta]
          >=(1/6) integral w(t)dt >0.                    (CEX)

There is no restriction b<1/6 for this first-loop result. It does not claim a
corresponding Hamming/switch-masked one-pinch inequality.

## Exact return identity

For ANY flat unitary U with |U_jk|^2=1/N and U^m=I,

    E_N,m(0)=sum_c |sum_j (U^(m-1))_(j+c,j) U_(j,j+c)|^2
             =sum_c |sum_j |U_(j,j+c)|^2|^2=N.            (R)

This uses U^(m-1)=U*, so every inner sum equals 1 exactly.
For all other m, E_N,m(0)>=0 by the twirl identity. Therefore

    N^-2 sum_m w(m/N) E_N,m(0)
       >=N^-1 sum_(6|m) w(m/N)
       ->(1/6) integral w.

The phase-averaged term is o(1) by the finite-rank/tail lemma, since
D_N=J_H+R_N, ||R_N||<=epsilon_N. More explicitly it is bounded in absolute
value by C_w[N^-1+epsilon_N]. Subtracting this term proves CEX.

## Mechanism and excluded inference

This rejects the specific generic inference

    flatness + reverse decay + strict charge gap + collective compactness
        => signed one-pinch Heisenberg aggregate tends to zero.

The witness even has uniformly small centered D_N. The macroscopic spectral
clusters from period six make the unaveraged Poisson pair kernel much larger
than N^2. Accepted actual fixed-word information excludes this particular
changed family; it does not itself bound the corresponding actual long echo.
A proof for the literal generator must quantitatively control its long-time
spectral/action overlap, rather than invoke those generic coarse inputs.

Finite verification includes exact p=5, N=25 cyclotomic construction,
unitarity, U^6=I, U^5=U*, and E_25,6(0)=25. The asymptotic proof above relies
on the elementary source estimate for all primes, not extrapolation of that
finite test.
