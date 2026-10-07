# A residual counterexample with position, reverse and charge gaps

Candidate theorem, 7 October 2026. This is an explicitly CHANGED unitary family, not the frozen quantization. It strengthens the separate one-dimensional cubic witness by also satisfying reverse-kernel decay. The earlier witness and its review are preserved unchanged.

## B1. Exact statement and boundary

There is an explicit family V_N in odd dimensions N=p^2, along primes p=2 modulo 3, for which:

1. V_N is unitary, every |V_N(j,k)|=N^(-1/2), and V_N^6=I.
2. P_N=|V_N|^2=J_N exactly.
3. For the reverse kernel Q_N(j,k)=V_N(j,k)conjugate(V_N(k,j)), ||Q_N||=N^(-1/2).
4. For every nonzero CYCLIC charge c modulo N, the charge block

       B_(N,c)(j,k)=V_N(j,k)conjugate(V_N(j+c,k+c))

   satisfies uniformly

       ||B_(N,c)||^2 <= p^(-1)+2sqrt(2)(2+log p)p^(-1/4).    (B1)

   Thus the full centered charge pinching norm tends to zero.
5. For every nonzero nonnegative smooth w supported in 0<a<b<1/6, the actual occupation-mismatched, Hamming>floor(.49m), switch-count>floor(kappa N/log N) residual, for ANY fixed kappa>0, has normalized signed aggregate at least

       N integral (1/6-t)w(t)dt+o(N),                       (B2)

   and therefore diverges. Its damped value at z_N=1-A log N/N is negligible for sufficiently large fixed A, so its signed marked-switch boundary integral diverges as well.

This refutes a boundary closure from the joint position-chain, reverse-kernel and one-step charge-gap properties together with the exact occupation/switch algebra. It does not preserve the prescribed raw Weyl symbol, fixed nonlinear classical map, exact kick factors, spectral simplicity, or fixed-word freeness. It is NOT a counterexample to the actual BGS target.

## B2. Non-symmetric finite-group Fourier kernel and exact recurrence

Work over F_p^2, with p>=5 prime, p=2 modulo 3. Put

    A=[[1,1],[0,1]],
    H_A(x,y)=p^(-1)e_p(x^T A y),    x,y in F_p^2.

Since A is invertible, character orthogonality proves H_A is unitary. Direct multiplication gives

    (H_A^2)(x,y) = 1_(A^T x+A y=0).                         (B3)

Thus row action sends x to Cx, where

    C=-A^(-1)A^T=[[0,1],[-1,-1]],    C^3=I.

The induced ket-label permutation is C^(-1)=-A^(-T)A, also of order three. Both conventions therefore give H_A^6=I. This explicitly distinguishes row and ket actions rather than reversing A silently.

Label the cyclic coordinate j in {0,...,p^2-1} by its base-p digits

    j=x+p y,   0<=x,y<p,
    f(j)=(x^3,y^3) in F_p^2.

Cubing is a permutation since gcd(3,p-1)=1; hence f is bijective. Define

    V_N(j,k)=p^(-1)e_p(f(j)^T A f(k)),    N=p^2.             (B4)

This is permutation conjugation of H_A, so unitarity, flatness, and V_N^6=I follow exactly. No vector-group translation is substituted for a cyclic charge.

The reverse kernel is

    Q_N(j,k)=p^(-2)e_p(f(j)^T J f(k)),
    J=A-A^T=[[0,1],[-1,0]].

Since J is invertible, p^(-1)e_p(x^T J y) is unitary. Consequently Q_N is a permutation conjugate of p^(-1) times a unitary, giving ||Q_N||=1/p=1/sqrt(N) exactly. This replaces the norm-one reverse kernel of the original symmetric witness.

## B3. Elementary complete and incomplete polynomial sums

For p>=5 and a polynomial F over F_p of degree two with nonzero quadratic coefficient,

    |sum_(u in F_p) e_p(F(u))|=sqrt(p).

Squaring and differencing proves this: the zero shift contributes p, and every nonzero shift is a nonconstant linear character sum and contributes zero.

For degree three with nonzero cubic coefficient, each nonzero difference shift is a quadratic polynomial with nonzero quadratic coefficient. Therefore

    |sum_u e_p(F(u))|^2 <=p+(p-1)sqrt(p)<=2p^(3/2),
    |sum_u e_p(F(u))| <=sqrt(2)p^(3/4).                    (B5)

The same bound holds after any added linear term.

For an interval I of consecutive representatives in {0,...,p-1}, finite Fourier completion gives

    sum_(u in I)e_p(F(u))
       =p^(-1)sum_t hat(1_I)(t) sum_u e_p(F(u)+tu),

up to the harmless Fourier-sign convention. Geometric summation and sin(pi r/p)>=2r/p for 1<=r<=p/2 give

    sum_t |hat(1_I)(t)| <=p(2+log p).

Hence, for every degree-two or degree-three nonconstant F of the displayed type,

    |sum_(u in I)e_p(F(u))|
       <=sqrt(2)(2+log p)p^(3/4).                           (B6)

These are elementary bounds, not an imported Weil theorem. Empty intervals contribute zero. A constant polynomial is estimated trivially and treated as exceptional below.

## B4. Literal cyclic carries

Write a nonzero cyclic charge as

    c=c0+p c1,   0<=c0,c1<p,

with (c0,c1)!=(0,0). For j=x+p y define epsilon(x)=1 if x+c0>=p, and zero otherwise. Then, EXACTLY modulo p^2,

    j+c has digits (x+c0 mod p, y+c1+epsilon(x) mod p).      (B7)

For a column k=u+p v, partition u into at most two nonempty intervals

    I0={0,...,p-c0-1},     I1={p-c0,...,p-1}.

On I_epsilon, the second digit displacement is d_epsilon=c1+epsilon modulo p. If c0=0 only I0 is present. This includes every charge divisible by p, for which c1!=0.

Fix two row labels j,l. Put

    a=f(j)-f(l),       b=f(j+c)-f(l+c),
    alpha=A^T a=(a1,a1+a2),
    beta=A^T b=(b1,b1+b2).

The unnormalized inner product of their charge-block rows is exactly the sum over epsilon of

    [sum_(u in I_epsilon) e_p(alpha1 u^3-beta1(u+c0)^3)]
      *[sum_(v in F_p) e_p(alpha2 v^3-beta2(v+d_epsilon)^3)]. (B8)

The actual entry of B_c B_c* is p^(-4) times this sum. Formula B8 follows directly from B4 and B7 and retains all carry branches.

A polynomial alpha u^3-beta(u+d)^3 is either constant, quadratic or cubic. When d!=0 it is constant precisely when alpha=beta=0; when d=0 it is constant precisely when alpha=beta. Here p!=3 is essential.

Call a row partner l exceptional for fixed j,c if BOTH underlying polynomials in B8 are constant as polynomials over F_p for at least one nonempty branch. A nonconstant polynomial can restrict to a constant on a singleton carry interval; it remains nonexceptional under this algebraic definition and is covered by B6. There are at most p exceptional l, including j:

- If c0!=0, a constant u-polynomial forces alpha1=beta1=0. Since alpha1=a1=x_j^3-x_l^3, cube injectivity forces x_l=x_j. There are exactly p possible second digits, so at most p partners. This necessary condition is independent of the branch, so a union over two branches does not double the count.
- If c0=0, then c1!=0 and only I0 occurs. A constant v-polynomial forces alpha2=beta2=0. The necessary equation alpha2=a1+a2=0 reads x_l^3+y_l^3=x_j^3+y_j^3. For each y_l there is exactly one x_l by cube injectivity, hence at most p partners. This is the decisive p|c case.

For a nonexceptional partner, on each branch at least one factor is a nonconstant quadratic/cubic sum. Apply B5 if that factor is the complete v-sum, and B6 if it is the incomplete u-sum, bounding the other factor by p. Thus B8 has modulus at most

    2sqrt(2)(2+log p)p^(7/4).

For an exceptional partner use the total trivial bound p^2. Every row of B_c B_c* consequently has absolute row sum at most

    p*p^(-2) + p^2*2sqrt(2)(2+log p)p^(-9/4),

which is B1. The matrix is Hermitian, so the column bound agrees, and Schur's inequality proves the stated operator-norm bound. No individual charge or carry case is omitted.

## B5. Independent control of the balanced term

For any N-dimensional unitary W and integer m>=1, set

    B_m(W)=integral_(T^N)|Tr((Z_theta W)^m)|^2 dtheta.

Then B_m(W)<=mN. To see this, write the homogeneous occupation polynomial

    Tr((diag(x)W)^m)=sum_(|n|=m)c_n x^n.

Parseval and sum_j n_j^2>=m give m B_m<=sum_j ||partial_(theta_j)Tr((Z_theta W)^m)||_L2^2. Cyclicity gives the exact derivative i m ((Z_theta W)^m)_(jj), and unitarity bounds the sum of its diagonal squared moduli by N. This proves the bound, with every repeated occupation retained.

Because V_N^6=I, |Tr V_N^m|^2=N^2 for every positive multiple of six, while the other squared traces are nonnegative. Therefore, for the w in B1,

    N^(-2)sum_m w(m/N)[|Tr V_N^m|^2-B_m(V_N)]
       >=sum_(6 divides m)w(m/N)-N^(-1)sum_m m w(m/N)
       =N integral (1/6-t)w(t)dt+o(N).                     (B9)

The coefficient is positive because b<1/6. This proves a statement about the off-charge part itself, independently of what the balanced complement does. It is not an inference from full-pair failure alone.

## B6. Exact residual masks and the damped endpoint

The accepted universal fractional-Hamming estimate gives zero for the low-Hamming off-charge term: ||P-J||=0 and m-2floor(.49m)>0. Since B1 implies the nonzero charge-block norms tend to zero, the complete centered pinching has norm <=rho for every prescribed rho>0 eventually. The charge-zero centered block is zero.

Arbitrary occupation row phases preserve these one-step block norms. The exact zero-run identity and whole-fiber torus subtraction in accepted T10–T12 therefore remove every off-charge word with <=floor(kappa N/log N) switches at exponentially small cost, including checksum zero and with arbitrary further Hamming restrictions. For any fixed kappa choose -log rho>8kappa/a before taking N large. Thus the literal high-Hamming/high-switch residual has the same lower bound B9, proving B2.

Eventually rho<=1/2. At z_N=1-A log N/N, A>4/a, the accepted all-switch transfer bound T8/T9 makes its high-Hamming off-charge aggregate negligible; subtracting the same exponentially small low-switch part gives a negligible damped residual. The exact T15 identity then forces the signed boundary integral T16 to diverge by B2. Positivity is used only for total squared traces and the balanced upper bound; neither the off-charge trace nor its residual is asserted positive term by term.

## B7. Evidence and exact exclusion

The proof uses character orthogonality, elementary Gauss/differencing/completion, the literal cyclic carry formula, and the already accepted universal mask-removal theorems. Bounded finite controls can check these dictionaries; they do not establish the asymptotic by themselves.

All three coarse inputs P=J, ||Q||->0 and sup_(c!=0)||B_c||->0 hold simultaneously. Exact finite-order recurrence, absent in the literal actual map, is the mechanism causing failure. Therefore a future boundary proof must use information that excludes this recurrence/coherence beyond those inputs, such as genuinely quantitative long-word actual phase information. Qualitative fixed-word exclusions alone are not being claimed sufficient either.
