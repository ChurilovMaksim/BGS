# First nonlinear slow mode: actual source and two compressed frames

6 October 2026. Separate continuation; the parent directory's report and
manifest remain byte-for-byte unchanged. Self-reviewed proof with independent
tensor/combinatorial implementations, awaiting a fresh proof review.

## Results

For every odd N>=3 and EVERY replica order m>=2, the quadratic two-block
mode below, after subtracting its full U(N)-invariant projection, has exactly

    source norm squared / input norm squared
        =q_N=(N^2-3N+3)/[3N(N^2-2)],

    compressed energy / input norm squared
        =e_N=16N w_mid/(N^2-2).

Here w_mid is the actual squared Jacobi edge coefficient at the middle cut.
Consequently q_N~1/(3N), while e_N~pi^4/(2500N^5). The multiplicity
binomial(m,2) cancels exactly, so these conclusions apply unchanged at m~N.
The additive mode's exactly zero initial balanced source does NOT extend to
this first nonlinear mode. Its source still tends to zero, but only in norm
as N^-1/2.

At the literal tau=10^-80 the source norm differs from sqrt(q_N) by at most
|tau|N sqrt(e_N)=O(|tau|N^-3/2). This all-time estimate does not discard a
Taylor remainder.

There are two distinct, useful consequences.

* The actual source-weighted regularized inverse-energy norm is at least
  N^2/4 for every odd N>=19, every m>=2, and epsilon=N^-5. Thus the source
  does not cancel the inverse-energy cost in this operator norm.
* The TWO initial compressed frames do lift this particular vector:
  its Rayleigh quotient for L_m+Pi C_m L_m C_m^* Pi is
  3/(20000N)+O(N^-3), rather than order N^-5. This is one explicit vector,
  not a lower bound for that operator on every complementary vector.

Neither conclusion bounds the complete signed memory trace or closes the
plateau. No Markov or positive-semigroup replacement is used.

## 1. Objects and exact invariant subtraction

Retain H_m, Pi, C_m, K_m(t), L_m and P_0 from the frozen parent report:
H_m is commutation by A_tot=sum_r A^(r), C_m is conjugation by M^(tensor m),
K_m(t)=exp(itNH_m)C_m, L_m=Pi H_m^2 Pi, and P_0 is the full U(N)-Haar
invariant projection. In particular P_0 is defined even if 7 divides N,
when it is smaller than ker L_m. All norms are ordinary, unnormalized HS.

Set k=(N-1)/2. In the path ordering from the identically zero edge, take

    D=diag(phi),  phi=1_I-k/N,  |I|=k,
    t2=Tr D^2=(N^2-1)/(4N),  c=t2/(N^2-1)=1/(4N),
    X=sum_(r<s) D^(r)D^(s).

I is an interval in the cyclic coordinate ordering. Twirling D tensor D
gives c(Swap-I/N): the twirl is a linear combination of identity and Swap,
and its traces against those two operators are 0 and t2 respectively.
This two-copy identity, embedded in each pair of slots, proves exactly

    P_0 X=c sum_(r<s)(Swap_rs-I/N),
    Y=X-P_0 X.                                                (1)

Thus Y is balanced and orthogonal to the FULL invariant space, not just to
the identity vector or a chosen finite list of permutations.

Every pair-local term in (1) has both partial traces zero. Consequently
different pair embeddings are HS-orthogonal, including pairs sharing one
slot. For example the shared-slot contraction factors through those zero
partial traces. Therefore, writing b_m=binomial(m,2),

    ||Y||^2=b_m N^(m-2) t2^2 (1-1/(N^2-1))
           =b_m N^(m-2)(N^2-1)(N^2-2)/(16N^2).               (2)

This retains every ordered tensor coordinate and repeated occupation.

## 2. Exact source image and fourth Fourier moment

Put B=M^*DM. Flatness of M and Tr D=0 give B_ii=0. Balanced projection of
the pair B tensor B is precisely

    T=sum_(i!=j)|B_ij|^2 |ij><ji|.                            (3)

There is no diagonal term. Since P_0 is fixed by C_m and Pi,

    W:=Pi C_m^*Y
      =sum_(r<s)[T_rs-c(Swap_rs-I/N)].                        (4)

The bracket in (4) has both partial traces zero. Its squared norm is

    local ||W||^2=t4-t2^2/(N^2-1),
    t4=sum_(i!=j)|B_ij|^4.                                   (5)

Indeed Tr T=0, Tr(T Swap)=t2, and ||T||^2=t4. Thus
||W||^2=b_m N^(m-2) times (5), with no hidden growing-m factor.

The prescribed metaplectic kernel gives, up to a unit complex chirp,

    B_ij=N^-1 sum_l phi_l e_N(4^(-1)l(j-i)).                  (6)

Multiplication of the difference index by the modular inverse of 4 is a
permutation. The interval I has integer additive energy
E(I)=(2k^3+k)/3: its pair-sum counts are 1,2,...,k,...,2,1.
There is no modular wrap in this equality because 2k-2<N. Discrete Parseval,
with the zero Fourier coefficient removed, gives

    t4=E(I)/N^2-k^4/N^3
       =(N^2-1)(N^2+3)/(48N^3).                              (7)

Combining (2),(5),(7) proves the exact, m-independent ratio

    ||W||^2/||Y||^2=q_N=(N^2-3N+3)/[3N(N^2-2)].              (8)

This is positive for every odd N>=3. It disproves only the extension of the
additive zero-source cancellation, not the possibility of other signed
cancellation. In particular q_N itself still tends to zero.

## 3. Actual energy and literal fixed-time source

The invariant part of (1) commutes with A_tot. For one pair,

    [A_tot,D tensor D]=[A,D] tensor D+D tensor [A,D].

These two terms are orthogonal since Tr(D[A,D])=0. Their partial traces
vanish, so different pair embeddings remain orthogonal after commutation.
The two-block step has one nonzero cut along the actual path, giving
||[A,D]||^2=2w_mid. Consequently

    <Y,L_mY>/||Y||^2
       =4w_mid t2/[t2^2(1-1/(N^2-1))]
       =e_N=16N w_mid/(N^2-2).                              (9)

For the actual symbol,

    w_mid=cos^4(7pi/(2N)) sin^4(pi/(2N))/2500.

Thus e_N~pi^4/(2500N^5). For odd N>=19, using pi^4<100,

    0<e_N< (1/20)N^-5.                                      (10)

The formula itself holds also at small and seven-divisible dimensions;
for example e_7=0 because the sampled Jacobi graph has no nonzero edge.

Set T_t=Pi K_m(t)^* restricted to ran Pi. The spectral theorem for H_m
and K_m(t)^*=C_m^* exp(-itNH_m) give the exact all-time bound

    ||T_tY-W||/||Y|| <=|t|N sqrt(e_N).                       (11)

Therefore

    | ||T_tau Y||/||Y||-sqrt(q_N) |
                                      <=|tau|N sqrt(e_N).    (12)

This is uniform in m. At the fixed physical tau it preserves the leading
N^-1/2 source amplitude, with O(|tau|N^-3/2) error. It is an actual U(tau)
statement, not an auxiliary kick-time numerical extrapolation.

## 4. Quantified source-weighted inverse-energy obstruction

On the balanced space, let epsilon=N^-5. Since P_0 commutes with L_m,
testing the operator below on v=(L_m+epsilon)^(1/2)Y gives

    ||T_tau (L_m+epsilon)^(-1/2)(I-P_0)||
       >= [sqrt(q_N)-|tau|N sqrt(e_N)] / sqrt(e_N+epsilon).
                                                                  (13)

For N>=19, q_N>=1/(6N) and (10) holds. At tau=10^-80, (13) yields

    ||T_tau (L_m+N^-5)^(-1/2)(I-P_0)|| >= N^2/4              (14)

for every m>=2 and every odd N>=19, including 7|N. The regularization is
essential to that unrestricted statement. When 7 does not divide N,
ker L_m=ran P_0; the identical test with v=L_m^(1/2)Y gives an at least
cN^2 bound for T_tau times the inverse square root on that complement
(N^2/4 is again a valid conservative constant).

This refutes a uniform or vanishing operator-norm estimate of THIS specified
source-weighted inverse-energy operator. It does not imply that a cyclic
signed trace is large: the tested vector is not the trace functional, and
different signed contributions may still cancel.

## 5. The same vector is lifted by two initial compressed frames

This result concerns C_m at the actual initial metaplectic step. It is not
an assertion about every vector or a finite-time dissipative generator.

By (6), F(d):=|B_(i,i+d)|^2 is independent of i, with F(0)=0. Define

    E_F=sum_(d mod N)[F(d+1)-F(d)]^2.                         (15)

The pair matrix T in (3) is diag(F(i-j)) times Swap. Swap commutes with
A tensor I+I tensor A. Direct matrix-unit contraction therefore gives

    ||[A tensor I+I tensor A,T]||^2
                                      =2||A_off||^2 E_F.     (16)

Both partial traces of this commutator vanish; the invariant correction
in (4) contributes zero. Hence the full m-copy energy is b_m N^(m-2)
times (16). For odd N>=19, ||A_off||^2=9N/80000, so

    ||H_m W||^2/||Y||^2
       =9N^3 E_F/[2500(N^2-1)(N^2-2)].                      (17)

For clarity, the limiting constant in E_F needs no numerical inference.
Let theta=2pi 4^(-1)/N, with the modular inverse represented in {1,...,N-1}.
The triangular interval-overlap sequence gives exactly

    S_k(theta)=sum_(s=-k+1)^(k-1)(k-|s|)^2 e^(is theta)
       =k/sin^2(theta/2)
        -sin(k theta)cos(theta/2)/(2sin^3(theta/2)),

    C_F:=sum_d F(d)F(d+1)
       =S_k(theta)/N^3
        -2k^2 sin^2(k theta/2)/(N^4 sin^2(theta/2)),

    E_F=2t4/N-2C_F=1/24+O(N^-2).                            (18)

The identity for S_k follows by applying the discrete second difference
to (k-|s|)^2. The zero Fourier coefficient of phi is removed in C_F's
second term. Since sin(theta/2)>=1/2 for all odd N>=3,
0<=C_F<=3/N^2, which suffices for the stated error.

Define the two-compressed-frame positive operator

    Q_m=L_m+Pi C_m L_m C_m^* Pi.

Then (9),(17),(18) prove for this exact Y, uniformly in every m>=2,

    <Y,Q_mY>/||Y||^2
       =e_N+9N^3 E_F/[2500(N^2-1)(N^2-2)]
       =3/(20000N)+O(N^-3).                                 (19)

The second frame therefore increases this vector's energy by four powers
of N. This is compatible with (14): a source can have a large inverse-energy
norm for the first frame while its image has greater energy in the second.
Equation (19) does NOT prove a lower spectral gap on all modes, estimate the
oscillatory memory, or justify a Markov closure. Equation (12) controls a
norm difference only; no finite-tau version of (19) is inferred from it.

## 6. Executed checks and limits

`check_nonlinear.py` constructs full m-copy matrices for
(N,m)=(3,2),(3,3),(3,4),(5,2),(5,3),(7,2),(19,2).
It independently checks (1)'s orthogonality against every permutation,
the matrix formula (4), all norm multiplicities, (7)--(9), and (16)--(17).
The seven-dimensional control has zero energy but nonzero source, as its
extra kernel permits. These checks use complex128 arithmetic and do not
constitute an interval certificate.

The interval additive-energy identity is additionally checked in exact
integer arithmetic for every odd N from 3 through 99. The independent
scalar formula (18) is checked through N=1001 in the listed finite sample.
An auxiliary t=.137 check verifies the finite-dimensional Duhamel inequality;
the fixed-tau conclusion is the proof (11), not that auxiliary experiment.

Command:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_nonlinear.py > checks.json

No random inputs, new averaging law, growing-replica cutoff, or change of
the quantum symbol is used. Search of the relevant prior signed-resummation,
occupation, physical-weight and channel-gap notes found no earlier instance
of this exact quadratic source calculation. No literature priority claim
is made. The script, outputs and inherited source hashes are recorded in
the separate manifest. All older report/manifest hashes were verified
unchanged after this run.

## Supporting scope

This is a supporting result for TRACE-020, not an extra core theorem or
control of the full balanced/complement trace. Review and original-byte
mappings are in record/collective_promotion_mapping.json. Any full-kernel
identity used by an unregularized corollary retains its separate hypothesis;
the regularized slow-source obstruction does not require identifying Haar
invariants with the entire deterministic kernel.
