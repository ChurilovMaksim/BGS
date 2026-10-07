# Global switch transfer and exact undamped boundary obligation

Maintained companion prepared 7 October 2026. Independent internal review: proved as written, using the independently accepted one-step gap in [onestep_charge_gap.md](onestep_charge_gap.md). The literal actual-parametrix dependencies remain unchanged. The global switch-damped theorem and checksum-free undamped low-switch theorem have separate scopes; the undamped marked-switch boundary is OPEN.

## T1. Target and decisive new mechanism

Keep the prescribed U_N=exp(i 10^-80 N A_N)M_N, every odd N, and original pair normalization. For rooted cyclic words x,y of length m, define A_U(x)=product_j U_(x_j,x_(j+1)), c=y-x modulo N,

    h(c)=#{j:c_j!=0},   s(c)=#{j:c_j!=c_(j+1)},
    n(x)-n(y)=the integer coordinate-occupation difference.

The full undamped off-charge sum is the sum of A_U(x) conjugate(A_U(y)) over n(x)!=n(y). That theorem remains OPEN. The new mechanism below performs the complete sum over all N^m charge histories before taking a norm. It proves global cancellation with an explicit switch factor z^s, including arbitrary switch density, arbitrary Hamming masks and checksum-zero off-charge pairs. It also removes the checksum restriction from the UNdamped growing low-switch theorem.

The global z=1 boundary is not controlled. A precise counterexample to the proposed interior-to-boundary inference and the exact missing signed estimate appear in T6--T7. No independence of the actual coordinate phases is assumed.

## T2. Exact finite-dimensional generating transfer

Let H=End(C^N) with ordinary Hilbert--Schmidt norm, H_c=span{E_(c,j)=|j><j+c|}, and P_c their orthogonal projections. Put

    T=Ad(U),   D=sum_c P_c T P_c,   e0=I/sqrt(N),
    H0=e0^perp,   J0=|e0><e0|.

The exact charge block from H_d to H_c is

    B_cd(j,k)=U_(j,k) conjugate(U_(j+c,k+d)).                  (T1)

Both T and D fix e0 and preserve H0. T|H0 is unitary. The new one-step lemma gives ||D|H0||<=rho<1 uniformly for sufficiently large actual odd N; enlarge rho to cover the zero-charge centered block.

For Z_theta=diag(e^(i theta_j)), let V_theta=Ad(Z_theta). For |q|=1 define Q_q E_(c,j)=q^(1_(c!=0)) E_(c,j). Both operators are unitary, preserve H0, and fix e0. Define, for real 0<=z<=1,

    M(z,q,theta)=Q_q V_theta [z T+(1-z)D].                   (T2)

No claim is made that this is the original quantum evolution. It is an exactly specified generating transfer on an N^2-dimensional space. Its (c,d) block carries factor z for c!=d and factor 1 for c=d. Its row carries the Hamming marker q and the occupation phase e^(i(theta_j-theta_(j+c))). Therefore the literal matrix trace is exactly

    Tr_H M(z,q,theta)^m
     =sum_(x,y) z^s(c) q^h(c)
       exp(i sum_j[theta_(x_j)-theta_(y_j)])
       A_U(x) conjugate(A_U(y)).                            (T3)

This is rooted, once counted, and includes all repeated coordinates. It follows directly by expanding one cyclic matrix trace; no tensor dimension N^(2m) enters the contraction estimate.

Define the generating off-charge polynomial

    G_(N,m)(z,q)=Tr M(z,q,0)^m
                -integral_(T^N) Tr M(z,q,theta)^m dtheta.   (T4)

The integral is normalized and exact. It kills precisely every nonzero integer occupation difference and retains every balanced pair, including repeated labels. Thus

    G_(N,m)(z,q)=sum_(n(x)!=n(y))
                   z^s(c) q^h(c) A_U(x)conjugate(A_U(y)).    (T5)

The independent theta variables in T4 are a Fourier projector used to express the deterministic mask. They are not inserted into, randomized over, or substituted for the target operator U_N.

## T3. Entropy-free global contraction, including occupation twists

For every theta and |q|=1, the identity direction is reducing and fixed. The triangle inequality on H0 gives

    ||M(z,q,theta)|H0||
      <= z+(1-z)rho = 1-kappa(1-z),  kappa=1-rho>0.          (T6)

This is uniform in all N coordinate phases. It is precisely where a strict ONE-step bound is stronger than a fixed-power bound: multiplication by arbitrary V_theta would not preserve the latter. In particular no coordinate-phase analytic regularity is assumed.

Consequently

    |Tr M(z,q,theta)^m-1|
      <=(N^2-1)[1-kappa(1-z)]^m.

The scalar identity cancels in T4, giving

    |G_(N,m)(z,q)|
      <=2(N^2-1)exp[-kappa(1-z)m].                          (T7)

This bound already sums every charge and switch history, including the dense-switch/high-Hamming family. It has no N^s or binomial entropy factor. The averaging/projection is retained inside the calculation, not bounded color by color.

For an arbitrary set Hset contained in {0,...,m}, let G^Hset be T5 restricted to h(c) in Hset. A finite discrete Fourier extraction at the m+1 roots of unity, or ordinary Fourier coefficient integration on |q|=1, gives

    |G^Hset_(N,m)(z)|
      <=2 |Hset| (N^2-1) exp[-kappa(1-z)m]
      <=2(m+1)(N^2-1) exp[-kappa(1-z)m].                    (T8)

No Hamming cutoff is required for this inequality. In particular Hset={floor(.49m)+1,...,m} controls the entire high-Hamming off-charge polynomial with its switch factor retained, including zero checksum and all switch densities.

For bounded w supported in [a,b], 0<a<b, the original N^-2 aggregate in T8 is at most

    C_(a,b,w) N^2 exp[-kappa a N(1-z)].                      (T9)

Thus, for z_N=1-A log(N)/N and any fixed A>2/(kappa a), the normalized aggregate tends to zero. More generally it does so whenever kappa a N(1-z_N)-2 log N tends to +infinity. This is a genuine Heisenberg-scale statement with vanishing regularization, but it is still a regularized statement.

## T4. Undamped growing low-switch off-charge control without checksum

For a full difference word c, define

    F_theta(c)=sum_x exp(i sum_j[theta_(x_j)-theta_(x_j+c_j)])
                         A_U(x) conjugate(A_U(x+c)).

Its exact block product uses B_cd^theta=V_(theta,c)B_cd. Every switch block has norm at most one. Every nonzero diagonal block has norm at most rho by the new one-step lemma; arbitrary row phases are unitary. The zero diagonal block is still P=|U|^2, since V_(theta,0)=I. Row/column unitarity of Z_theta U implies

    B_(c,0)^theta 1=0 for c!=0,
    1*B_(0,d)^theta=0 for d!=0.

Hence a nonconstant word permits exact replacement of every internal zero-charge run by powers of P-J, just as in the accepted low-switch proof. Runs of length one contain zero internal factors and need no replacement. For a word with r>=1 switches, there are exactly m-r diagonal factors. Therefore

    |F_theta(c)|<=N rho^(m-r)                               (T10)

uniformly in theta, c and the repeated word coordinates. A nonzero constant word has |F_theta(c)|<=N rho^m. The constant zero word is completely balanced, so its off-charge contribution is exactly zero.

The occupation-masked fiber is exactly

    F_off(c)=F_0(c)-integral F_theta(c)dtheta.

Thus for EVERY nonzero difference word, including checksum zero,

    |F_off(c)|<=2N rho^(m-s(c)).                            (T11)

This is a bound on the actual partial fiber, justified by a uniform bound on its exact torus representation. It does not reuse the invalid inference that a signed full-fiber estimate controls arbitrary subsets.

Counting words with r switches by at most binom(m,r)N^r gives

    sum_(s(c)<=R) |F_off(c)|
     <=2N^2 rho^m
       +2N rho^m sum_(r=1)^R binom(m,r)(N/rho)^r.            (T12)

Set gamma=-log rho and R_N=floor(gamma a N/(8 log N)). The same elementary entropy calculation as the accepted low-switch proof, using log(bN^2/rho)<=3 log N eventually, makes T12 at most C exp(-gamma a N/2), uniformly for aN<=m<=bN. Its bounded-weight N^-2 time aggregate is exponentially small. The same estimate permits arbitrary restrictions on the difference word c, including any Hamming set, and weights of modulus at most one depending on c.

This removes the checksum restriction entirely. It includes off-charge portions of translations even when ord(c) divides m, and checksum-zero low-switch partial fibers. It does not imply those partial fibers equal the original full contraction.

## T5. Stronger exact remaining off-charge mask

Relative to the independently accepted .49m raw off-charge Hamming theorem, T12 removes the disjoint high-Hamming low-switch part without any checksum condition. The new remaining literal off-charge set is simply

    n(x)!=n(y),   h(y-x)>floor(.49m),   s(y-x)>R_N.           (T13)

Thus the earlier alternative 'many switches OR zero checksum' can be strengthened to 'many switches', still retaining the high-Hamming condition. The one-step lemma and T4 have separate independent internal acceptance; their exact original source pins and review scopes are retained.

For its z-weighted trace, subtract the low-switch high-Hamming off-charge trace from G^Hset in T8. By T12 the subtracted trace is exponentially small uniformly for 0<=z<=1. Therefore the very same actual dense-switch residual in T13 has a z-weighted normalized aggregate tending to zero under T9, plus an exponentially small error. Every mask is disjoint and literal; no balanced centered-range projector is turned into a coordinate mask.

The separate balanced complement in the accepted synthesis remains untouched. The exact Haar/CUE pair baseline at z=1 remains min(m,N), and the full factorial hierarchy remains open.

## T6. Interior estimates do not determine the undamped boundary

For each m take the scalar polynomial p_m(z)=z^m. It has degree m and satisfies

    |p_m(z)| <= exp[-(1-z)m], 0<=z<=1,

which is even stronger than the exponential shape in T7 for kappa<=1. At z_N=1-A log N/N and m approximately aN it tends to zero polynomially, but p_m(1)=1 exactly. Multiplication by a polynomial prefactor such as N or N^2 gives an order-one or divergent original N^-2 aggregate while retaining the corresponding prefactor in T7. This refutes the inference 'degree<=m and the displayed interior exponential decay imply vanishing at z=1'. It is a counterexample to that analytic closure, NOT to the actual U_N target.

There is also an exact universal operator barrier. On H0, M(1,1,0)=T|H0 is unitary, while T6 strictly contracts for z<1. A telescoping estimate gives, uniformly in theta and |q|=1,

    ||M(1,q,theta)^m-M(z,q,theta)^m||
      <=m(1-z)||T-D|| <=2m(1-z).

After trace and subtraction in T4, this gives

    |G_(N,m)(1,q)-G_(N,m)(z,q)|
      <=4(N^2-1)m(1-z).                                    (T14)

For an arbitrary Hamming set, the coefficient-extraction version costs at most |Hset|. Hence the elementary norm continuity bound makes the high-Hamming normalized aggregate small only if N^3(1-z_N)->0; without a Hamming filter it requires N^2(1-z_N)->0. These are sufficient continuity regimes, not necessary ones. They are incompatible with the exact sufficient damping condition kappa a N(1-z_N)-2 log N -> +infinity, which includes A log N/N with sufficiently large fixed A. No choice of a common z_N closes the original target by these estimates.

The exact Haar off-charge comparator remains zero for EVERY z and Hamming mask, because Haar left-diagonal invariance kills every occupation-mismatched monomial. Thus this reduction preserves that comparator. For the total unmasked trace at z=1, Haar gives min(m,N), not 1. The scalar 1 in the contracted transfer is the one-copy identity contribution, not the full Haar-invariant ramp/plateau. The regularized total transfer can suppress the balanced ramp as well; it must not be substituted into the undamped CUE comparison.

## T7. Exact missing signed implication and executable continuation

Let R_(N,m) denote exactly the mask T13, and define its switch-marked derivative

    H_(N,m)(u)=sum_((x,y) in R_(N,m))
                  s(y-x) u^(s(y-x)-1) A_U(x)conjugate(A_U(y)).

For any 0<z_N<1, the fundamental theorem of calculus for the finite polynomial gives the exact identity

    residual(1)-residual(z_N)=integral_(z_N)^1 H_(N,m)(u) du. (T15)

The residual(z_N) term is proved negligible by T9 and T12. Therefore its complete compact-weight undamped off-charge target is equivalent to

    N^-2 sum_m w(m/N) integral_(z_N)^1 H_(N,m)(u) du ->0.      (T16)

Choose z_N=1-A log N/N with A>2/(kappa a), and use the same masks and original signed normalization. This is a sharp localized missing implication in an explicit shrinking boundary interval, not another definition of the entire old residual. It is a signed marked-switch estimate with one integrated source and a known negligible interior endpoint. Its endpoint cannot be supplied by the norm estimates just proved.

A corresponding full-matrix derivative before coefficient extraction is exactly

    d/dz Tr M(z,q,theta)^m
      =m Tr[M(z,q,theta)^(m-1) Q_q V_theta (T-D)].            (T17)

The noncommuting derivative is valid by cyclicity; it is not a termwise commutation claim. Taking theta=0 minus the normalized theta integral retains the off-charge projector. Subtracting the explicitly controlled low-switch polynomial and extracting high-Hamming coefficients yields H in T15. Thus T16 is an ordinary N^2-dimensional resolvent/marked-transfer boundary problem retaining all nonlinear actual U phases and all switch entropy.

No estimate of T16 is proved here. The cat norm-one control in the companion proof and the p_m boundary polynomial both prevent strengthening the result by deleting its hypotheses or its regularization.

## T8. Prior search and evidence limits

The prior accepted all-translation and low-switch proofs are explicitly credited. The accepted fractional-Hamming and disjoint-synthesis results are frozen in [historical author inputs](../evidence/charge_strengthening_20261007/raw/author/inputs/). Searches in the current mathematical and research-record corpus for switch fugacity, charge pinching, dephasing, global switch transfer and generating-function variants found the exact charge blocks and prior noisy transfer/Abel reductions, but no occurrence of this one-step positive-envelope argument or this occupation-uniform switch transfer. This is a bounded search statement, not a novelty theorem. General quantum-channel convexity, coefficient extraction and Abel boundary obstructions are elementary established mechanisms, not newly invented general theory.

Finite checks use exact Gaussian-integer arithmetic for dense complex rational unitaries. They verify the transfer dictionary, occupation coefficient extraction, Hamming/switch grading, zero-checksum off-charge partial fibers, identity reduction and the matrix derivative; their explicit bounds and source hashes are in the control manifest. The literal tau asymptotic is established only by the companion proof and its accepted analytic inputs, never by these auxiliary matrices.

## Review and reproduction record

The exact original candidate, independent reviews, source pins and bounded computational controls are preserved by [the promotion record](../record/charge_strengthening_promotion.md). No finite computation proves the analytic limit. This prepared overlay is not an integration or publication claim.
