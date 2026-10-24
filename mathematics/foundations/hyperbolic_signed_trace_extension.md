# Signed-trace extension: every hyperbolic integer toral automorphism

This addendum completes the trace range in
[the covariance-based spectral theorem](../spectral-obstructions/general_hyperbolic_prime_spectra.md).
It is a project proof, with no assertion of external priority or completed
computer verification. In particular, trace less than -2 is covered without
replacing the classical map by an iterate or by its negative.

## Statement

Let A belong to SL(2,Z), let t=Tr A satisfy |t|>2, put a=|t| and
s=sign(t). Define u_0=0, u_1=1, u_(j+1)=a u_j-u_(j-1). For every odd prime
K>3 not dividing a-2s, let m=(K-1)/2 and set

    N_K=u_(m+1)+s u_m > 0,
    c_K=((a-2s)/K),
    D_K=(N_K-c_K)/2,
    n_K=(N_K-c_K)/(2K).

Parentheses in c_K denote the Legendre symbol. Then N_K is odd. There is a
phase normalization of the unitary Weyl implementer U_(A,N_K) for which the
parity sector

    range((I-c_K R)/2)

has every K-th root of unity with multiplicity exactly n_K. No prime,
squarefree, or split-torus hypothesis on N_K is needed.

With lambda=(a+sqrt(a^2-4))/2,

    N_K=(lambda^(K/2)-s lambda^(-K/2))/sqrt(a-2s).

Consequently K is logarithmic in N_K. Together with the support-separated
fixed-strength construction in the companion note, this gives the all-orders
operator-norm comparison, all polynomial time windows, all fixed factorial
correlations, and random-origin count laws for every such A. The invariant
quadratic refinement q_*(v)=v_1 v_2+v_1+v_2 modulo 2 is part of this general
quantization convention.

## Proof, including the signs

For signed t, let v_0=0, v_1=1, v_(j+1)=t v_j-v_(j-1). One has

    v_j=s^(j-1)u_j,
    v_(m+1)+v_m=s^m N_K.

The exact matrix identity proved in the companion note is therefore

    A^K-I=s^m N_K A^m(A-I).                                 (1)

It follows that A^K=I modulo the positive integer N_K. The polynomial
v_(m+1)+v_m evaluates to K at t=2, so

    gcd(N_K,t-2)=gcd(K,t-2)=1.

The last condition is equivalent to K not dividing a-2s. Thus A-I is a unit
matrix modulo N_K. If A^j fixes a nonzero vector modulo a prime factor of
N_K, 0<j<K, Bezout for j,K and (1) would make A fix it, a contradiction.
The odd order also excludes eigenvalue -1 for every A^j. These are exactly
the hypotheses of the abstract finite spectral theorem.

Parity of N_K follows from the same recurrence modulo 2: the signs of t and
of the consecutive sum do not matter in characteristic two. For even a the
u sequence alternates 0,1. For odd a it has period 0,1,1, and an even
consecutive sum would require K=3 modulo 6, impossible for a prime K>3.

The signed polynomial congruence is

    s^m N_K = ((t-2)/K) modulo K.

Euler's criterion gives s^m=(s/K). Multiplying these two signs gives

    N_K = ((s(t-2))/K) = ((a-2s)/K) modulo K.

This is c_K. The abstract finite theorem now proves the multiplicities and
the sector selection. Its proof uses the full and parity virtual characters,
not a guessed phase of a Gauss sum.

Finally the eigenvalue formula for u_j gives the displayed closed formula
for N_K. It has a plus sign between the two powers when s=-1. Confusing this
sign with the positive-trace case would give the wrong modulus. End of proof.

## A non-squarefree, nonsplit example

Take the original Pell cat with its sign reversed:

    A=-((3,2),(4,3)), t=-6, K=7.

The recurrence at a=6 gives u_3=35 and u_4=204, so

    N_7=204-35=169=13^2,
    c_7=(8/7)=+1,
    D_7=84,
    n_7=12.

Thus the odd sector consists of seven roots, each exactly twelvefold. The
discriminant is t^2-4=32=6 modulo 13. The nonzero squares modulo 13 are
1,3,4,9,10,12, so this component is nonsplit; moreover the modulus is a prime
square. A proof based on a diagonal eigenbasis over Z/169Z would not apply.

For contrast, trace +4 and K=11 give N=989=23*43, c=-1, D=495 and n=45.
Here 12=9^2 modulo 23, but 12^21=-1 modulo 43. This is a mixed split/nonsplit
squarefree example, and its exactly uniform sector is even, not odd.

These arithmetic evaluations are direct consequences of the displayed
integer recurrences. They are not claims of measured spectral data.

## Fixed parity and interpretation

The sign c_K can alternate with K. One fixed sign occurs on an infinite
subsequence by the infinite pigeonhole principle, so a fixed parity statement
is available on an infinite semiclassical subsequence without invoking a
prime-distribution theorem. No assertion that both signs occur infinitely
often is needed here. In cases a-2s is an integer square, the sign is +1 for
all admissible primes and the uniform sector is always odd.

The resulting nonlinear fixed-strength systems remain smoothly conjugate to
an arithmetic toral automorphism. Their non-universal spectra therefore do
not establish, or refute, generic arithmetic-free BGS. What is completed here
is the precise spectral calculation for this explicitly specified class,
including the previously omitted negative traces and non-squarefree moduli.
