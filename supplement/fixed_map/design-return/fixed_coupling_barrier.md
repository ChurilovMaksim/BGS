# What the strengthened return theorem does and does not reach

18 September 2026. Internal proofs, not an asserted BGS solution.

## 1. A stronger necessary lower bound on the onset dimension

Fix any real finite Fourier symbol with nonconstant Fourier l1 norm F0>0
and finite first moment F1, and the raw modular Pell-cat quantization
specified in the companion notes. Subtracting its scalar mean only rotates
the spectrum. Let tau>0 vary, while for each tau the classical coupling
is held fixed as the dimension varies. Set U_(tau,N)=exp(i tau N A_N) M_N.

Fix a smooth h with 0<=h<=1, h=1 on [-1,1] and support contained in
[-5/4,5/4]. Let N_*(tau), if it exists, be any threshold beyond which the
factorial pair statistic for h differs from its CUE limit by at most 1
at every odd dimension. Then, for sufficiently small tau,

    N_*(tau) >= c_f / [tau sqrt(log(1/tau))],          (1)
    c_f=sqrt(log(1+sqrt(2)))/(384 F0).

This is a necessary lower bound, not a proof that an onset exists, a
matching upper bound, or a formula predicting the actual crossover.

Proof: put L=log(1/tau), a=sqrt(log(beta))/(64 F0), and choose the largest
odd Pell index K with N_K<=a/(tau sqrt(L)). Consecutive sufficiently large
odd Pell dimensions have ratio less than 6. Hence

    a/(6 tau sqrt(L)) < N_K <= a/(tau sqrt(L)),
    K <= L/log(beta)

for small enough tau. The second inequality follows from
N_K=(beta^K-beta^-K)/2. The composite-period theorem applies for large K.
With epsilon=tau N_K and D=17 pi F1^2, its return bound gives

    b <= sqrt(K)(F0 epsilon+D epsilon^2)
      <= 1/64 + D a^2/[sqrt(log(beta)) sqrt(L)] < 1/32.

Also K/N_K<1/32 eventually. The occupied-arc bound in the normal-form
note therefore gives B_(N_K)>8. The h statistic is at least B_(N_K),
while its CUE limit is at most 5/2. Thus this dimension cannot be beyond
N_*(tau), proving (1). QED.

This improves the earlier project bound of order 1/[tau log(1/tau)].
Its mechanism is the square-root K size of the coherent period average,
and removal of the prime-index restriction supplies bounded ratios of
successive admissible dimensions. The asymptotic small-tau threshold in
this conservative proof is not substituted for the separate exact
certificates at tau=10^-80.

## 2. Exact variance and finite certificates for the frozen symbol

Use the explicit position convention

    exp(2 pi i (k q+l p)) -> T(l,k).

The 32 nonconstant coefficients are in (1/4000) Z[i]. Their squared l2
sum is 66033/160000. The only distinct pairs in the same infinite S-orbit
are (-1,1)->(1,1) and their negatives, contributing together -7/1000000
to the orbit variance. Thus

    sigma^2 = 1650797/4000000,
    ||Abar-f0 I||_2^2=sigma^2/K                         (2)

for every odd K>=39.

To justify completeness, for integer v=(a,b) with 0<||v||_1<=9,
(a+sqrt(2)b)(a-sqrt(2)b) is a nonzero integer. If S^d v=w and
||w||_1<=9, this implies lambda^|d|<=2*9^2=162<lambda^3.
Only d=-2,-1,0,1,2 need be checked. Direct coefficient comparison gives
the pairs just listed and no d=2 pair. There is no additional modular
alias for K>=39: balance the two exponents as in the sparse-orbit proof;
the resulting integer vector has norm less than N. If it is zero modulo
N it is zero as an integer vector. Each frequency orbit has length K.
Weyl orthogonality now proves (2).

For the ordinary-midpoint gauge the original coefficients acquire
(-1)^(kl). The integer orbit matches preserve this parity since S=I
modulo 2, so (2) remains true. The rational finite program also checks
both collected norms separately; equality of these norms does not assert
equality of the two quantum spectra.

Combining the exact variance with saturated commutator bounds yields:

| K | N, approximately | HS return error upper bound | B_N lower bound |
|---|---:|---:|---:|
| 199 | 7.43586e75 | 0.00067409 | 1332.17 |
| 201 | 4.33394e76 | 0.00395481 | 226.23 |
| 203 | 2.52600e77 | 0.02337720 | 37.42 |
| 205 | 1.47226e78 | 0.14416142 | 5.15 |

The exact rational computations, with display rounding only at the end,
are in `frozen_sharp_return.py` and its JSON output. At K=205 the h
statistic differs from its CUE limiting value by more than 2.65. This
is one explicitly certified finite dimension, not an infinite-dimensional
counterexample at tau=10^-80.

Independent dense N=41,239 tests assemble the same A_N both from Fourier
modes and from the Jacobi entries, in both midpoint conventions, and
check the homological and Duhamel identities. A separate Wolfram
calculation reproduces the rational variance and Pell matrix identity.
None of these matrix experiments simulates tau=10^-80 at a large dimension.

## 3. A failed way to reach fixed coupling: short Fourier truncations

The sparse-word estimates do not justify truncating the quantum kick at
word lengths of order log N when epsilon=tau N. This is already false
for the one-harmonic kick

    D_N(x,x)=exp(i tau N cos(2 pi x/N)),   0<tau<=1/16.

Let P_Q be the orthogonal projection, in normalized Hilbert--Schmidt norm,
onto diagonal Fourier modes with |n|<=Q. For Q=O(log N),

    ||P_Q D_N||_2^2 -> 0,
    inf_(V in ran P_Q) ||D_N-V||_2 -> 1.               (3)

This holds for a diagonal kick alone. It is an obstruction to the proposed
bounded-bandwidth approximation, not a BGS counterexample and not a proof
that every conceivable resummation fails.

Here is a self-contained estimate. Let epsilon=tau N and

    a_n=(1/(2 pi)) integral_0^(2 pi)
                           exp(i epsilon cos(theta)-i n theta) dtheta.

For epsilon>=16 and |n|<=epsilon/2, split the integral where
|epsilon sin(theta)+n|<=sqrt(epsilon). This set has measure at most
8/sqrt(epsilon): on it |sin(theta)|<=3/4 and |cos(theta)|>1/2.
On the complement split into the four monotonicity intervals of sin and
then at the removed intervals; at most eight intervals remain. Integration
by parts for a monotone derivative of fixed sign bounds each integral by
2/sqrt(epsilon). Consequently

    |a_n| <= 4/sqrt(epsilon).                           (4)

To control finite-lattice aliases, write the Fourier series as the Laurent
series of exp(i epsilon (z+z^-1)/2). Cauchy's estimate on |z|=2 and |z|=1/2
gives |a_n|<=exp(5 epsilon/4) 2^(-|n|). For |n|<=Q<=N/2, the sum of all
nonzero aliases a_(n+lN) has absolute value at most

    4 exp(5 epsilon/4) 2^(Q-N) <= 4 exp(-N/4).          (5)

Discrete Fourier sampling gives the exact aliased coefficient. From
(4)-(5), when Q<=epsilon/2,

    ||P_Q D_N||_2^2
       <=32(2Q+1)/epsilon+32(2Q+1) exp(-N/2).          (6)

Since ||D_N||_2=1, orthogonal projection proves (3). Also any degree-Q
polynomial in cos(2 pi x/N) belongs to this Fourier subspace. Thus a
short polynomial expansion cannot supply the missing approximation either.

`fixed_kick_bandwidth.py` checks this distinct large-epsilon regime by FFT,
without dense matrices. The proof of (3) is the integral argument, not a fit
to the finite data.

## 4. Remaining barrier

At fixed nonzero tau, epsilon=tau N eventually exceeds every fixed power of
log N. Equation (9) of the sparse-orbit note then ceases to be a small
error, and (3) rules out the simplest low-frequency repair. The required
coherent long-time estimate, the pair BGS limit, and the all-k limit all
remain unproved. No commit or push has been made for these intermediate
results, in accordance with the user's publication condition.
