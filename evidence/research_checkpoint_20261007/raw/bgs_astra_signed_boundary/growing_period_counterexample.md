# Growing-period residual obstruction with all three coarse gaps

Candidate theorem, 7 October 2026. Changed family, not the literal fixed-tau quantizer. This extension uses the separately supplied dimension-uniform Abel theorem for the exact phase projector, rather than reproducing it. Its source is pinned in inputs/18_uniform_abel_bound.md, SHA256 ecd82a74edfabb89f6cbf46054d76c52dd41e5eb2d5a9790771b16a7c033da3f. The carry method is the separate bilinear_carry_counterexample_v2.md; its exact specialization is given below.

## P1. Construction and conclusions

Let p>=5 run through primes p=2 modulo 3, and N=p^2. For j=x+py, 0<=x,y<p, set f(j)=(x^3,y^3) in F_p^2. Put

    A=[[1,2],[0,1]],
    V_N(j,k)=p^(-1)e_p(f(j)^T A f(k)).                       (P1)

Then V_N is unitary and has the following simultaneous properties:

    |V_N(j,k)|^2=1/N,
    ||Q_N||=N^(-1/2),    Q_N(j,k)=V_N(j,k)conjugate(V_N(k,j)),
    sup_(c!=0 mod N)||B_(N,c)|| ->0,                        (P2)

with the explicit uniform bound B1 of the fixed-period carry note. Charges remain CYCLIC Z/N charges, including p|c.

Its exact period is 2p=2sqrt(N), and for every positive integer m,

    |Tr V_N^m|^2 = N^2       if 2p divides m,
                  N         if m is even and 2p does not divide m,
                  N         if m is odd and p divides m,
                  sqrt(N)   if m is odd and p does not divide m.  (P3)

In particular every fixed nonzero normalized trace tends to zero. More quantitatively,

    sup_(1<=m<2sqrt(N)) |N^(-1)Tr V_N^m| <=N^(-1/2).        (P4)

Nevertheless, for every nonzero nonnegative smooth compact w supported in ANY fixed positive band [a,b], the genuine occupation-mismatched high-Hamming/high-switch residual satisfies

    N^(-2)sum_m w(m/N) residual_(N,m)
       >= (sqrt(N)/2) integral w(t)dt - O_w(1).             (P5)

Here Hamming>floor(.49m), and switches>floor(kappa N/log N) for any fixed kappa>0. Thus the residual diverges despite flat P, decaying reverse Q, vanishing charge blocks, and a growing short-trace window with uniform macroscopic phase law. The switch-regularized endpoint is negligible by the accepted all-switch contraction, so the corresponding T16 boundary integral diverges too.

The known actual fixed-word freeness theorem excludes this family if interpreted as a relation between its specified kick/cat factors; no such factor identification is made. P4 preserves only fixed-power normalized trace information of the single unitary, and is not two-generator freeness, exact quantization, or Anosov Egorov data.

## P2. Exact recurrence and trace table, including odd m and p|m

Before relabeling, let H_A(x,y)=p^(-1)e_p(x^T A y) on F_p^2. Character orthogonality gives unitarity and

    H_A^2(x,y)=1_(y=Cx),
    C=-A^(-1)A^T=[[3,2],[-2,-1]]=I+B,
    B=[[2,2],[-2,-2]],    B^2=0,    rank B=1.               (P6)

For every odd p, B!=0. Hence C^k=I+kB, which is identity exactly when p|k. The row permutation H_A^2 has exact order p. Moreover H_A^p is not identity: its trace computed below is p<N. Thus H_A and V_N have exact order 2p.

For m=2k,

    Tr H_A^(2k)=#{x:C^k x=x}=p^2 if p|k, and p otherwise.   (P7)

For m=2k+1, multiply H_A by the row permutation C^k. Its diagonal phase is x^T A C^(-k)x. Direct multiplication gives

    A C^(-k)=[[1+2k,2+2k],[2k,1+2k]],
    x^T A C^(-k)x=(2k+1)(x1+x2)^2.

There are p pairs (x1,x2) with each fixed sum s, so

    Tr H_A^m = sum_(s in F_p) e_p(m s^2),    m odd.          (P8)

If p|m this is p; otherwise its squared modulus is p by the elementary quadratic Gauss identity. Equations P7 and P8 prove P3 for every positive m, including odd multiples of p and all return multiples. They also prove P4. Negative powers are adjoints, so the fixed nonzero Fourier moments vanish in both directions, giving the uniform macroscopic eigenphase measure.

## P3. Reverse norm and all cyclic charge blocks

Since A-A^T=[[0,2],[-2,0]] is invertible for every odd p, Q_N is 1/p times a unitary finite-group Fourier matrix after the f relabeling. Thus ||Q_N||=1/p exactly.

Use the SAME literal carry formula j+c from B7 of the separate carry proof. The exact row-correlation factorization B8 remains valid, now with

    alpha=A^T a=(a1,2a1+a2),
    beta=A^T b=(b1,2b1+b2).

The complete/incomplete polynomial-sum bounds B5/B6 are unchanged. For c0!=0, the condition that the underlying u-polynomial is constant over F_p still forces alpha1=beta1=0, hence x_l=x_j. There are at most p exceptional partners, independently of carry branch.

For c0=0,c1!=0, the complete v-polynomial being constant forces alpha2=beta2=0. The necessary equation is now

    2x_l^3+y_l^3=2x_j^3+y_j^3.

For each y_l there is exactly one x_l because 2 is invertible and cubing is bijective. Thus the same at-most-p bound holds for every charge divisible by p. Nonconstant polynomials restricted to singleton carry intervals remain covered by completion and are not reclassified as algebraically constant.

The identical Schur estimate therefore gives, uniformly for every c!=0 modulo p^2,

    ||B_(N,c)||^2 <=p^(-1)+2sqrt(2)(2+log p)p^(-1/4).        (P9)

The zero-charge centered block is zero because P=J. This proves every assertion in P2.

## P4. The independently supplied balanced bound

For an arbitrary deterministic unitary W_N, define the exact occupation-balanced trace

    B_N(m)=E_theta |Tr((Z_theta W_N)^m)|^2.

The supplied dimension-uniform Abel theorem proves

    N^(-2)sum_(m>=1)e^(-2sm/N) B_N(m) <=1/(2s)+1/(2N)      (P10)

for every s>0. It uses finite rank-one unitary interlacing and exact phase spectral averaging, and requires no flatness, mixing or model hypotheses. That proof is credited and imported as a source, not independently claimed here.

If w is bounded and supported in [a,b], choose any fixed s>0 and use positivity to get

    N^(-2)sum_m |w(m/N)| B_N(m)
      <=||w||_infinity e^(2sb) [1/(2s)+1/(2N)] = O_w(1).   (P11)

This a priori bound does not identify the balanced CUE limit.

## P5. Growing coherent returns force off-charge divergence

At every multiple of 2p, P3 gives |Tr V_N^m|^2=N^2. All other squared traces are nonnegative. Hence

    N^(-2)sum_m w(m/N)|Tr V_N^m|^2
      >=sum_(r>=1) w(2r/p)
      =(p/2) integral w(t)dt+O_w(1).                       (P12)

Subtract P11. By the exact occupation-projector identity, the result is the full deterministic off-charge trace, so its normalized aggregate diverges as in P5.

The low-Hamming off-charge trace is exactly zero by P=J and the accepted universal Hamming bound. The growing low-switch off-charge trace is exponentially small by P9 and accepted T10–T12, uniformly after any further Hamming restriction, including checksum-zero fibers. For any fixed kappa choose an arbitrarily small fixed rho with -log rho>8kappa/a, then take N sufficiently large. The literal residual therefore has the same lower bound P5.

At z_N=1-A log N/N with A>4/a, eventually rho<=1/2 and accepted T8/T9 makes the damped high-Hamming off-charge aggregate negligible; the low-switch subtraction remains exponentially small. The exact fundamental theorem of calculus T15 identifies the difference with T16. Thus this explicit growing-period family also refutes the signed-boundary closure from all three coarse gaps plus fixed normalized-power data.

## P6. Scope

This is an elementary changed-family counterexample plus an imported independently reviewed universal Abel input. It is not a construction in the frozen raw-Weyl model. It has a coherent period at the growing scale sqrt(N), invisible to every fixed-power normalized moment. No fixed-word theorem has been contradicted. The actual phase relations, exact kick/cat factors and quantitative growing-word exclusions remain possible ways to distinguish the maintained model.
