# Conditional convex resummation of all unmasked pinch words

7 October 2026. **Conditional theorem; author proof and self-review.** This packet makes no repository change and proves no actual-map stationary-phase input. Its new input is the RIGHT-multiplication frame bound stated below. The accepted one-pinch packet uses left multiplication and does not itself supply this input. The original BGS operator, odd-dimensional sequence and normalization are unchanged when the lemma is applied to that sequence.

## 1. Exact hypotheses and notation

Let U=U_N be any N-by-N unitary. Work on H=End(C^N) with ordinary Hilbert--Schmidt norm and ordinary, unnormalized traces. Set

    T=Ad(U),  V_b=Z_b U Z_b*,  D=(1/N) sum_b Ad(V_b),
    T_z=z T+d D,  d=1-z,  0<=z<=1,
    (A_c)_(y+c,y)=U_(y+c,y),  C e_c=A_c*,
    R X=X U.

Here Z_b=diag(exp(2 pi i b j/N)); row-minus-column slices use the accepted packet's explicit c->-c reindexing. Character orthogonality gives D=sum_c Ad(A_c). Assume a uniform number C0>=1 with ||C||^2<=C0. For an integer L>=1 define

    epsilon_(L,N)=max_(1<=r<L) ||C* R^r C||,
    delta_(L,N)=min{C0, C0/L+(1-1/L)epsilon_(L,N)},
    R_(L,N)=(C0-delta_(L,N))(L-1).

The maximum is zero at L=1. In particular 0<=R_(L,N)<=C0(L-1). The conditional asymptotic input is ||C* R^r C||->0 for every FIXED positive integer r. No uniformity in growing r is assumed. Thus delta_(L,N)->C0/L for fixed L.

Define the complete, unmasked, at-least-one-pinch correction

    F_(N,m)(z)=Tr_H(T_z^m)-z^m |Tr(U^m)|^2,  m>=1.

This is not an occupation-subtracted or Hamming-filtered quantity. It is nonnegative: every word in T,D is a convex mixture of Ad(W) with W unitary, and Tr_H Ad(W)=|Tr W|^2>=0. All binary words containing at least one D are included, including adjacent pinches, runs of length zero and the all-D word.

## 2. Exact finite-N theorem

For every integer interval 1<=A<=M and every L>=1,

    (1/N^2) sum_(m=A)^M F_(N,m)(z)
       <= (delta_(L,N)/N) sum_(m=A)^M (1-z^m)
          +(R_(L,N)/N) d [M-A+1+sum_(r=1)^(A-1) z^r].       (1)

In particular the second term is at most R_(L,N)d M/N. For z>0 there is a sharper, separately derived deconvolution estimate:

    (1/N^2) sum_(m=A)^M z^(-m) F_(N,m)(z)
       <= (delta_(L,N)/N) sum_(m=A)^M (z^(-m)-1)
          +(R_(L,N)/N)(z^(-M)-1).                           (2)

These are complete resummations. Their constants have no dependence on the number of insertions and no factorial or binomial entropy factor. For a bounded possibly complex weight w supported in [a,b] contained in (0,infinity), multiply the right side by ||w||_infinity and take A=ceil(aN), M=floor(bN) to bound the absolute value of its weighted sum. Positivity justifies this step; no continuity of w is needed.


Writing u_N=Nd_N, (1) gives, on M<=bN,

    normalized pinched band <= b delta_(L,N)+b C0(L-1)u_N/N. (3)

Consequently it tends to zero for every d_N->0, including u_N=O(log N), by first taking N->infinity with L fixed and then L->infinity. No limit of a growing insertion hierarchy is exchanged with the fixed-lag input. The theorem also applies when u_N->infinity but u_N=o(N).

For 0<=u_N<N, (2) implies

    normalized deconvolved band
       <= [b delta_(L,N)+R_(L,N)/N]
             [exp(b u_N/(1-u_N/N))-1].                     (4)

Thus bounded u_N is safe under the same iterated limit. If u_N=A0 log N, this estimate costs N^(b A0+o(1)); fixed-lag qualitative decay alone supplies no rate that compensates it. A sufficient quantitative condition is a choice L_N for which

    exp(b u_N/(1-u_N/N))
       [C0/L_N+epsilon_(L_N,N)+C0 L_N/N] ->0.                (5)

No such choice in the required large-logarithmic damping window is supplied by the conditional hypothesis.

For the actual BGS family there is a stronger obstruction in that required window: the accepted one-step gap forces the deconvolved COMPLETE positive correction to diverge. See Section 6a. The possible need for quantitative rates in (5) is a statement for the abstract frame lemma; it does not override this actual-family obstruction.

## 3. Proof of the uniform frame estimate

For each fixed unitary B put

    f_B(n)=sum_c |Tr(U^n A_c B)|^2
          =||C* (B U^n)||^2,  n any integer.

The equality follows from cyclicity of the ordinary trace, not from commuting B and U. Since ||B U^n||_HS^2=N, f_B(n)<=N C0. The synthesis operator with blocks R^(-j) C, j=0,...,L-1, has block Gram diagonal norms at most C0 and off-diagonal norms at most epsilon_(L,N). The block row/column norm bound therefore gives

    ||(1/L) sum_(j=0)^(L-1) R^(-j) C C* R^j||
        <= C0/L+(1-1/L)epsilon_(L,N).

The trivial norm bound C0 gives the minimum defining delta. Hence

    sum_(j=0)^(L-1) f_B(n+j)<=N L delta_(L,N)               (6)

for every starting n and every FIXED B. Both the starting point and B may be chosen arbitrarily, but B must be the same within the averaged block. Taking convex mixtures over B preserves (6).

Let f be any such convex mixture. Partition a prefix of length K into L-blocks and a remainder r<L. Then

    sum_(n=s)^(s+K-1) f(n)
       <=N[delta K+(C0-delta)r]
       <=N[delta K+R_(L,N)].                               (7)

For a nonnegative nonincreasing finite weight sequence w_n, summation by parts applied to these prefix bounds proves

    sum_(n=s)^t w_n f(n)
       <=N delta sum_(n=s)^t w_n+N R_(L,N) w_s.             (8)

There is no factor z^(-L) in this weighted estimate. The end term and all short coherent runs are explicitly retained in R_(L,N).

## 4. First-pinch factorization and changing total time

The noncommutative telescoping identity, requiring no commutation, is

    T_z^m-(zT)^m
       =d sum_(n+p=m-1) (zT)^n D T_z^p.                    (9)

It chooses the first D after a fixed linear cut of a rooted word. Every binary word with at least one D occurs exactly once. Expanding T_z^p gives a probability distribution on unitary words B of length p. Averaging the distinguished pinch charge yields

    f_p(n):=Tr_H(T^n D T_z^p)
       =E_B (1/N)sum_b |Tr(U^n V_b B)|^2
       =E_B sum_c |Tr(U^n A_c B)|^2.                        (10)

For each FIXED p, the law of B depends on p and z but is independent of n. It is therefore a legitimate convex mixture in (6)--(8). Nothing is required of coherent gaps within B; zero gaps and arbitrarily many remaining pinches are allowed.

When A<=m<=M, interchange the FINITE sums in (9). For each p=0,...,M-1 the n-interval is

    s_p=max(0,A-1-p),  t_p=M-1-p.

Apply (8) to w_n=z^n. The total scalar weight satisfies

    d sum_p sum_(n=s_p)^(t_p) z^n=sum_(m=A)^M (1-z^m),
    sum_p z^(s_p)=M-A+1+sum_(r=1)^(A-1) z^r.

This proves (1), including z=0 with the usual 0^0=1 convention. At z=1 all pinched corrections vanish identically.

For deconvolution, z^(-m) z^n=z^(-p-1), which is independent of n when p is fixed. Use (7) rather than (8). The total weights are

    d sum_p z^(-p-1)(t_p-s_p+1)
       =sum_(m=A)^M (z^(-m)-1),
    d sum_(p=0)^(M-1) z^(-p-1)=z^(-M)-1.

This proves (2). No post hoc removal of the convex weights was used.

### The essential fixed-time obstruction

At a single fixed m, changing n forces p=m-1-n to change. Consequently B and its distribution change, and (6) cannot be applied across n. Uniformity over fixed B does NOT mean uniformity over sequences B_n. The failure is exact: choose B_n=U^(-(n+1)). Then

    f_(B_n)(n)=sum_c |Tr(A_c U*)|^2
              =sum_c ||A_c||_HS^4>=N,

since sum_c ||A_c||_HS^2=N. Its normalized block average is at least one regardless of the conditional frame estimate for fixed B. For a one-pinch word at fixed m, B_n=U^(m-1-n) likewise makes the trace independent of n by cyclicity. The valid averaging above changes TOTAL TIME and holds p fixed. This is the precise reason it works.

## 5. Binomial insertion counts and cyclic multiplicities

Let W_(m,k) be the sum of Tr_H of all rooted binary length-m words with exactly k copies of D. There are binom(m,k) words. For 1<=k<=m, cyclicity gives the exact identity

    W_(m,k)=(m/k) sum_(l_1+...+l_k=m-k; l_j>=0)
               Tr_H(T^(l_1)D ... T^(l_k)D).                (11)

Proof: mark one of the k pinches in every rooted word. Counting marks at each of the m positions gives the weak compositions in (11). Repeated/periodic words retain all their distinct marks; there is no primitive-necklace quotient and no exceptional cyclic multiplicity. The boundary l_j=0 is retained. This formula is not itself an averaging theorem at fixed total m.

For a fixed k, write

    mu_(p,k-1)=binom(p,k-1)d^(k-1) z^(p-k+1),

zero for p<k-1. The normalized sum of all p-words with k-1 pinches is a convex mixture of unitary words. Calling its function f_(p,k-1), first-pinch decomposition gives

    d^k z^(m-k) W_(m,k)
       =d sum_(n+p=m-1) z^n mu_(p,k-1) f_(p,k-1)(n).       (12)

Applying (8), its band bound has leading term

    (delta/N) sum_(m=A)^M binom(m,k)d^k z^(m-k)

and remainder

    (R/N)d sum_(p=k-1)^(M-1) mu_(p,k-1) z^(s_p).

Sum over all k: sum_(k=1)^(p+1) mu_(p,k-1)=1. This proves (1) again without any k-dependent constant, whether the typical count m d is bounded, logarithmic or larger. The corresponding deconvolved leading mass is sum_m binom(m,k)(d/z)^k; summing k gives z^(-m)-1 and yields (2). Convexity avoids combinatorial growth BEFORE deconvolution. Removing the damping restores the exact total insertion mass z^(-m)-1, so the exponential amplification is real in this bound.

## 6. A noneffective divergent schedule that survives deconvolution

Fix b>0 and define, for N large,

    E_N=min_(1<=L<=floor(sqrt(N)))
            [delta_(L,N)+C0 L/N].

The fixed-lag hypothesis implies E_N->0: first choose fixed large L and then N large. Also E_N>=C0/floor(sqrt(N)), so log(1/E_N)=O(log N). For E_N<1 choose

    u_N=(1/(2b))log(1/E_N),  z_N=1-u_N/N.

For finitely many other N choose u_N=0. Then u_N->infinity, u_N/N->0, and (4) at a minimizing L gives

    deconvolved normalized band
        <=max(b,1) E_N exp(b u_N/(1-u_N/N))
        =O(E_N^(1/2+o(1))) ->0.                            (13)

The schedule depends on unknown frame norms and is noneffective from merely fixed-lag o(1) information. It does not furnish the prescribed u_N=A0 log N with A0>2/(kappa a), or the norm-damping condition kappa a u_N-2 log N->infinity. Indeed this particular safe choice has u_N<=log N/(4b)+O(1), well below that sufficient damping threshold. It therefore cannot close the original marked-switch boundary problem by combining the two displayed estimates.

## 6a. Actual-family logarithmic obstruction: the full positive correction diverges after deconvolution

This corollary uses the separately accepted full traceless one-step gap from `global_switch_transfer.md` T2--T6: D fixes the normalized identity e0, preserves H0=e0^perp and ||D|H0||<=rho<1. With kappa=1-rho in (0,1],

    |Tr_H(T_z^m)-1|<=N^2 exp(-kappa d m).

Set d=A0 log N/N with A0>2/(kappa a). Uniformly for ceil(aN)<=m<=floor(bN),

    Tr_H(T_z^m)=1+o(1),
    z^m |Tr U^m|^2<=N^2 exp(-d m)=o(1).

The second assertion follows because kappa<=1, so a A0>2. Therefore

    F_(N,m)(z)=1+o(1) uniformly on the band.                (14)

Let H=M-A+1. Its positive, deconvolved aggregate is consequently

    (1/N^2)sum_(m=A)^M z^(-m)F_(N,m)(z)
       =(1+o(1)) z^(-M)(1-z^H)/(d N^2)
       =(1+o(1)) N^(b A0-1)/(A0 log N) ->infinity.         (15)

The original, undeconvolved correction is merely (b-a+o(1))/N and thus tends to zero. This is not a lack-of-rate objection: the required large-logarithmic window makes vanishing of the COMPLETE positive deconvolved correction false, using accepted actual-family input.

The scalar 1 cancels exactly in the signed occupation subtraction. It is also removed by the relevant offcharge/high-Hamming projection. Thus (15) does not refute the target T16; it blocks closing T16 by bounding its two complete positive deconvolved corrections separately. Arbitrary occupation twists also preserve e0 and the same centered gap, so their complete pinched corrections have the same leading 1 and the same unsigned divergence. Cancellation has to be kept before an absolute bound.

## 7. Exact scope boundaries

1. **No signed occupation subtraction.** For an occupation phase Z_theta inserted at every step, the coherent unitary becomes Z_theta U and the pinch Kraus slices become Z_theta A_c. The necessary overlaps are C_theta* R_(Z_theta U)^r C_theta. The present R_U hypothesis does not bound them, uniformly or on average in theta. Absorbing all theta factors into B is invalid: they also occur inside the n-step coherent block. If an independent uniform/averaged twisted frame bound were supplied, positivity would bound the signed pinch correction by the sum of the two nonnegative complete corrections; it is not supplied here.

2. **No Hamming/path mask.** The Hamming marker Q_chi need not be a unitary conjugation channel, and extracting a coordinate subset does not preserve positivity of the Kraus trace decomposition. A small full sum cannot bound its signed sub-sums. A separate uniform source estimate or a coefficient-energy estimate is needed. A later Fourier extraction can also cost up to m+1; the current o(1) rate does not absorb that cost.

3. **Deconvolution requires rates or a slow schedule in the abstract lemma, and fails unsigned in the required actual window.** F>=0 and its convex correction is o(1) on bands. Multiplication by z^(-m) costs up to exp(bu_N+o(1)); (2) quantifies it exactly. The noneffective schedule (13) is a valid limited consequence. The accepted actual centered gap makes the COMPLETE positive deconvolved correction diverge at the prescribed large-logarithmic window, as (15) proves. This does not exclude cancellation in the signed, masked correction.

4. **No actual-map proof from this packet.** Echo's separate right-multiplication stationary-phase work is the conditional input. The accepted left-multiplication one-pinch estimate is credited and not duplicated. No claim about balanced microscopic limits, factorial hierarchy or BGS follows from this combinatorial lemma.

For the first scope warning there is even a finite algebraic example: U=diag(1,-1), m=1 gives F(z)=0, whereas the occupation-twisted averaged pinched correction is 2(1-z). Thus positivity of the theta=0 correction alone cannot dominate the occupation projection. This auxiliary example does not satisfy the asymptotic frame hypothesis and is not an actual-map counterexample. For the second warning, the exact control packet contains a rational 2-by-2 unitary with a negative h=1 masked pinch coefficient at m=4, z=1/2, while the complete correction is nonnegative.

## 8. Sources, controls and review status

Source bindings and base revision are in source_bindings.json. The source checkpoint's current acceptance language overrides old candidate headings. The accepted packet's frame identity, block-Gram mechanism and ordinary-HS normalization are prior inputs; this proof adds right-frame conditional resummation, exact weighted estimates, insertion-count closure and the stated deconvolution boundary.

Run `python3 exact_controls.py` in this directory. The controls use exact SymPy rational/algebraic arithmetic on auxiliary N=2,3 unitaries. They test channel identities, every binary word through the recorded finite degree, cyclic weak-composition multiplicities, first-pinch factorization, binomial count resummation, weighted-prefix constants, and both scope warnings. They neither verify the actual frame hypothesis nor prove an asymptotic theorem. This manuscript has received only author self-review; parent-directed independent mathematical review remains available.


## Appendix A. Optional positive-prefix refinement

**Optional sharper remainder.** In (1), (2), and every consequent bound, R_(L,N) may be replaced by

    R_opt=max_(0<=r<L; r integer)
             min{(C0-delta)r, delta(L-r)}.

Indeed a nonnegative remainder of length r has sum at most N min(C0 r,L delta), since extending it to a full L-block can only increase its sum. Thus (7) holds with R_opt. In particular

    R_opt<=L delta(1-delta/C0)<=C0 L/4,
    R_opt<=R_(L,N).

At fixed L under the overlap hypothesis, R_opt->C0(1-1/L), including zero when L=1. The simpler R_(L,N) is retained in the displayed theorem for compatibility with the stated prefix proof; the refinement has the same quantifiers and scope.

