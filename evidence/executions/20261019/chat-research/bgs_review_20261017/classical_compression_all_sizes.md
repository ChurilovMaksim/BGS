# Classical absorption at every retained size

17 October 2026. Independent reconstruction prompted by CE1 of the attached
two_channel_transmission(4).md. The original attachment is unchanged.
The result below strengthens its small-m regime; it is not a quantum
transmission theorem or a BGS proof. Author proof and self-review only.

## Theorem

Let P be an N-by-N nonnegative doubly stochastic matrix, J_N=11*/N, with

    max P_ij<=C/N, ||P-J_N||op<=epsilon<1, C>=1.

Set B=C+(C-1)/(1-epsilon). For EVERY nonempty subset A, m=|A|,
E=A^c, the stochastic complement

    K=P_AA+P_AE(I-P_EE)^(-1)P_EA

exists, is doubly stochastic, and satisfies, without a restriction on m/N,

    max_(a,b in A)|K_ab-1/m| <=4B/N,
    ||K-J_m||op<=min(1,4Bm/N).                           (1)

For a Markov walk starting at a in A, let L_a be the number of visits in E
before the next return to A. Then

    sum_(a in A) E_a L_a=N-m,
    |E_a L_a-(N-m)/m|<=2B for every a in A.              (2)

The empty E case means K=P and L_a=0. The singleton A case is also included.
This theorem needs no unistochasticity or reversibility.

## Proof

Put R=P-J_N and

    G=(I-P+J_N)^(-1)-J_N=Q_N+M,
    Q_N=I-J_N, M=sum_(h>=1)R^h.

The series converges in operator norm. Since P is doubly stochastic,

    sum_k R_ik^2=sum_k P_ik^2-1/N <=(C-1)/N,

and the same bound holds for every column. For h>=2,

    |(R^h)_ij|<=epsilon^(h-2)(C-1)/N.

For h=1 use |R_ij|<=C/N. Consequently

    max_ij |M_ij|<=B/N.                                (3)

If E is proper, every vector supported in E satisfies

    ||P_EE x||^2<=||Px||^2
       <=[1-(1-epsilon^2)m/N] ||x||^2.

Here Px=J_N x+Rx is an orthogonal decomposition and
||J_N x||^2<=|E| ||x||^2/N. Thus ||P_EE||op<1; its inverse is a
nonnegative geometric series. The block row and column sum equations give
K1_A=1_A and 1_A* K=1_A*.

For completeness, the centered Green compression identity is

    G_K=Q_m G_AA Q_m,
    M_K=Q_m M_AA Q_m,                                  (4)

where G_K is the inverse of I-K on the zero-sum subspace, extended by zero
on constants, and M_K=G_K-Q_m. To prove it, extend a zero-sum b on A by
zero and solve x=G(b,0). The E equation gives
x_E=(I-P_EE)^(-1)P_EA x_A; the A equation becomes (I-K)x_A=b.
Center x_A to obtain G_K b. The inverse exists: a kernel vector of I-K
lifts by the same formula to a kernel vector of I-P, and the latter is
constant because ||R||<1. The identity on constants is immediate.

Since G_K is the two-sided inverse on the zero-sum subspace,

    K-J_m=M_K(I-K)=Q_m M_AA(I-K).                        (5)

In the last equality the right Q_m in (4) disappeared because
1_A*(I-K)=0. Each entry of Q_m M_AA has modulus <=2B/N by (3), whereas
the j-th column of I-K has l1 norm exactly 2(1-K_jj)<=2. Equation (5)
therefore proves the entrywise bound (1). Its operator bound follows from
||K-J_m||<=1 for a doubly stochastic matrix and the entrywise row/column
sum bound. Notice that no Neumann expansion of M_K is needed; this is why
there is no small-m hypothesis.

For (2), let tau_E=(I-P_EE)^(-1)1_E and define h_A=P_AE tau_E.
These are the mean internal visit counts. Column stochasticity gives

    sum_a h_a=1_A*P_AE tau_E
             =1_E*(I-P_EE)tau_E=N-m.

Let r_a=1+h_a on A, extend r by zero to E, and let x_A=0, x_E=tau_E.
Then (I-P)x=1_N-r and sum_a r_a=N. Solving with G gives

    x=-G r+c1_N=-r-Mr+(1+c)1_N.

On A this reads r_a+(M_AA r_A)_a=1+c. All r_a are nonnegative and
their sum is N, so (3) gives |(M_AA r_A)_a|<=B. Subtract its A-average
to get |r_a-N/m|<=2B, exactly (2). The empty-E case follows directly.
This completes the proof.

## Relation to the submitted claims

The attachment's CLASSICAL CE5 and CE17 in the late CE1 appendix are valid,
weaker small-m conclusions. These are CL5 and CL17 in the supplied correction
patch; the attachment reuses CE1--CE6 for unrelated earlier cavity identities.
The centered Green compression mechanism already appears in the project's
TRACE-077 proof. The theorem above is a new combination/reconstruction in
this review, not a priority claim for stochastic complementation or Green
inverses. It uses only the displayed finite-dimensional argument.

For m=2, K_12=1/2+O_C,epsilon(1/N) for every chosen pair, with explicit
constant 4B. Quantum phase-averaged transmission is a different quantity:
the attachment's S_4 example has mean 23/45 over pairs while this classical
quantity is exactly 1/2. Nothing in (1)--(2) suppresses the coherent
occupation-matched path sums needed for quantum universality.
