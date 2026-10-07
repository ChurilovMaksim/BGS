# Independent audit of the literal-factor extensions

Checked 7 October 2026 against base main `d37c92e563d10d25bb1d6ab85bedffc1f160f773`.
This is an independent internal mathematical review, not external refereeing or analytic formalization. All writes are confined to this review directory. The author's files and canonical/repair checkouts were not edited.

## Verdict and scope

**Primary verdict: proved as written.** This verdict applies separately to the two exact, frozen candidate files below, using the previously independently audited fixed-word theorem and actual-model conventions as inherited inputs. Their new arguments have been checked rather than inferred from the earlier fixed-word verdict.

1. `frozen/growing_word_window.md`, SHA256 `4c497a406e51dd75cc0ca0b3b85100c3713c2013ae2d53b3d15e7ecceaf7222a`: its Q2 uniform normalized-trace conclusion holds for every nonidentity reduced word of length at most floor(log log log N/(4 log 8)), through all odd N, at the literal fixed tau=10^-80. The Q3 constants and Q4 envelope are consistent with the proof. No additional word-count factor is needed.
2. `frozen/strong_freeness_obstruction.md`, SHA256 `8eab771234f702cdf840497e49d7bf43c9fc1ab673818a75f31661bc99273729`: its fixed commutator polynomial has limiting free-group moments, but liminf lambda_max is at least 1-10^-148. Hence the pair is not strongly asymptotically free.

No new conditional mathematical leaf was found. Roy's precise v1 Theorem 1.1 is an external theorem, checked in the primary source; it is not a numerical or conjectural assumption. The inherited fixed-word theorem remains a separate reviewed input. No microscopic CUE, Heisenberg-time, signed factorial, general growing-Pell, spectral-simplicity, or deterministic BGS conclusion follows. Those targets remain open. No assertion of priority is made.

There is no necessary mathematical correction. Helpful local clarifications are listed at the end; none changes a formula, a hypothesis, or the accepted scope.

## Claim cards

The matrices are the unchanged odd-N ordinary-midpoint quantization of the corrected physical finite Fourier symbol g, with A_N=Op_N(g), Q_N=exp(i tau N A_N), and the prescribed cat quantizer M_N. Here tau=10^-80 is fixed; scalar phases in quantizers are allowed only where they cancel. Word length expands integer powers into q, q^-1, m, m^-1 letters. Traces are divided by N; vector norms in the coherent-state argument are ordinary Euclidean norms after unit normalization.

The growing theorem quantifies over every abstract nonidentity word within the stated N-dependent length window. It is stronger than the frozen fixed-word moment theorem but enormously weaker than a logarithmic all-word window. The strong-obstruction polynomial is fixed independently of N:

C=Q M Q* M*, D=M C M*, H=(C+C*+D+D*)/4.

Its free comparison norm is sqrt(3)/2, whereas its actual largest eigenvalue stays asymptotically above 1-10^-148.

## Dependency graph

Growing window:

- Frozen actual symbol, common equilibrium, exact derivatives, and faithful polynomial derivative representation.
- Integer degree/height control -> exact Roy source application -> quantitative derivative separation.
- Fixed Fourier bounds -> common holomorphic strip for all signed words -> bounded scalar embedding difference with one derivative seed.
- Taylor/Cauchy plus three-circle propagation -> uniform finite type at every real point.
- Polarization, derivative stability, divided differences and finite covering -> uniform scalar sublevel estimate.
- Exact integer-label Weyl product and sine remainder, exact cat Egorov -> quantitative word Egorov, with aliases retained.
- Smooth division/cutoff and normalized HS tail bound -> common trace envelope.
- Explicit growth comparison -> the triple-logarithmic window.

Strong obstruction:

- Exact raw-to-midpoint action and finite Fourier g -> sampled-Gaussian second-order residual.
- Exact cat Egorov at powers 0, 1, 2 -> the three residual constants B_j.
- Exact spectral-calculus inequality and phase-free commutator telescoping -> Rayleigh outlier bound.
- Frozen fixed-word freeness plus the explicit free-subgroup basis -> free-group moment limit.
- Internal tree Schur/Rayleigh calculation -> exact free comparison norm.

## Obligation matrix

| Obligation | Status | Decisive check |
| --- | --- | --- |
| Unchanged actual family and odd dimensions | Passed | Midpoint dictionary and cat convention match frozen inputs |
| Derivative polynomial degree and height | Passed | Degree <=L; coefficient l1 <=14^L; scaled integer height <=(14d0)^L |
| Roy exponent field, integrality and complex exponents | Passed | Primary v1 Theorem 1.1; beta=i alpha, degree <=2L, q=abs(a_d) |
| Closest-root conversion | Passed | Segment derivative bounded by e; each root is at least the closest-root distance |
| Signed-word complex domains | Passed | Per-letter width factors <=7 or <2, both <8; all intermediates stay in the original strip |
| Two-variable analytic propagation | Passed | One-dimensional three-circle along complex lines within polydiscs |
| Finite-type directional derivative and patch count | Passed | Polarization loss <=K^K; radius exp(-8K log K); all losses below exp(K^2) |
| H5 Egorov and accumulated word error | Passed | Global cubic sine remainder plus fixed-time Duhamel, then unitary telescoping |
| Aliased N-dependent symbols | Passed | Centered-cell orthogonality plus the omitted Fourier l1 tail, not false global orthogonality |
| Cutoff epsilon powers | Passed | epsilon^-4, epsilon^-3 and epsilon^-3 suffice through third derivatives |
| Growth of K_L and uniform supremum | Passed | log K_L=O_tau(8^L+L^2+L log(L+1)); K at L_N=(log N)^o(1) |
| Gaussian action and normalization | Passed | Exact Weyl action; centered periodization tails exponentially small |
| Exact Q rephasing and commutator cancellation | Passed | No expansion in tau N; scalar phase cancels algebraically |
| Three cat-transformed residuals | Passed | Exact Egorov; Euclidean ||S||<7; j<=2 fixed |
| Outlier arithmetic | Passed | Exact rational loss 146137680000 times 10^-160 |
| Free generators c,d and tree norm | Passed | Triangular free-basis substitution; direct Schur and Rayleigh bounds |
| Original microscopic target | Out of scope/open | Neither extension estimates the signed microscopic hierarchy |

## Growing-window details

### 1. Degree, height, roots, and the exact Roy hypothesis

For length <=L, the polynomial row-sum norm is submultiplicative. The signed S letters have norm <=7, and I+/-uE21 has norm <=2. Subtracting I leaves an entry P with degree <=L and coefficient l1 <=7^L+1<=14^L. Its nonzeroness is provided by the frozen faithful derivative proof; the new effective argument does not infer a lower bound from transcendence alone.

With d0=125*10^80, R(z)=d0^L P(9803z/d0) is integral because every coefficient is p_k*9803^k*d0^(L-k). Since 9803<d0, every coefficient has modulus <=14^L*d0^L=h_L. The degree d may be smaller than L; all later estimates remain in the safe direction.

If the nearest root alpha is within 1 of pi, then alpha is nonzero. Its conjugates are roots of R and have modulus <=1+h_L<=2h_L. For q=abs(a_d), q alpha is integral by the usual scaled-root monic equation; multiplication by i preserves integrality. Each embedding of Q(i alpha) extends to Q(alpha,i), so the conjugates of beta=i alpha also have modulus <=2h_L. Its degree is <=2d<=2L. A single nonzero exponent is rationally linearly independent, exactly as required by Roy.

For the polynomial Z+1, degree and coefficient bounds are both 1. Roy's S is 6 times the exponent-field degree and hence <=12L. Thus c*q*S<=24L*h_L^2 and 18S<=216L. All enlarged bases exceed 1, so the asserted monotone replacement is legitimate. This gives the candidate's exp(-B_L) bound without assuming that h_L beta itself is integral.

On the straight segment from pi to alpha, abs(Im z)<1; consequently abs(exp(i alpha)+1)<=e*abs(alpha-pi). Every root is at least the nearest-root distance away, with multiplicities counted. The leading coefficient is a nonzero integer. Factoring R and dividing by d0^L gives exactly exp[-L(B_L+1+log d0)]. Constant R or distance >=1 cases give an even stronger bound.

### 2. Complex strip and quantitative analytic propagation

The finite Fourier second-moment bound and l1 support bound <=10 justify the numerical strip constants independently of an unpinned qualitative-flow citation. At width 1/100, Fourier magnitudes gain at most exp(pi/5)<2. Vector-field maximum-coordinate norm is at most 2pi*52*exp(pi/5)<1000. For its derivative in maximum-coordinate induced norm, the rank-one frequency contribution has ratio

max_j |v_j|(|v_1|+|v_2|)/|v|^2 <= (1+sqrt(2))/2.

Therefore its bound is below (2pi)^2*52*exp(pi/5)*(1+sqrt(2))/2<5000. The stated constants are valid in the needed maximum norm, not merely in a silently substituted Euclidean norm.

Real solutions remain real. Comparing a complex initial point with its real part and using the derivative bound gives width growth <=exp(5000|kappa|)<2; the displacement bound and initial margin keep the entire comparison flow inside the 1/100 domain. This holds for positive and negative kappa. The two signed cat maps have maximum-coordinate norm <=7. Starting at R_L=1/(1000*8^L), every prefix and intermediate kick trajectory remains within width 1/1000. Holomorphic continuation is therefore legitimate for every word, including inverses.

The sine/cosine embedding coordinates are bounded by 2 on the resulting strip; each difference is bounded by 4. At P the relevant sine derivative is 2pi times an entry of DF-I, so the seed lower bound delta=exp(-D_L) is conservative.

For the propagation lemma, Cauchy gives normalized coefficients <=4. At radius R/2 the low-degree contribution is <=4eta. The tail is at most 16*2^(-K/2) for K>=1000, and the total is <=exp(-K/5). Real centers can be linked in <=ceil(4/R) steps of maximum norm <=R/4. At each new center its R/4 polydisc is contained in the previous R/2 polydisc. Applying three-circle to b(z+t v), with ||v||_infinity=R/2 and radii 1/2, 1, 2, proves the stated sqrt(4a) interpolation. Boundary radii are obtained by limits from within the open strip.

The resulting first derivative bound is 8R^-1 exp[-K/(5*2^J)]. Since K>=100*2^J*(D+log(100/R)+1), this is strictly below exp(-D). Thus Q6 is valid at every real point, without a compactness-only loss.

### 3. Finite type and all covering losses

Q6 gives a partial derivative of order k<=K with modulus >=eta. Polarization of the symmetric real k-linear derivative gives a Euclidean unit direction with k-th derivative at least eta/K^K=beta; the usual sharper factorial gain is simply discarded. A zeroth-order witness is also handled.

The candidate's A=4(K+1)!R^(-(K+1)) bounds every required partial derivative. Since K>=100/R and K>=1000, A<=exp(3K log K). Expansion of a unit directional derivative and one extra gradient contributes at most 2^(K+2), yielding exp(4K log K). On radius r=exp(-8K log K), variation is smaller than beta/2. Choosing the witness at each center of a fixed grid gives <=C r^-2 convex patches covering the torus.

On every positive-order patch, the derivative is real, continuous and bounded away from zero, so it has fixed sign along each interval slice. The divided-difference estimate applies to the full measurable sublevel set, not just one component: select k+1 quantile points with gaps at least a constant times its measure/k, bound their divided difference by the interpolation formula, and apply the repeated mean-value theorem. This gives the displayed 8k(s/beta)^(1/k) bound. For s<=beta/4 and k<=K, replacement of exponent 1/k by 1/K increases the upper bound. The zero-order patches contribute nothing.

The total loss is bounded by C*r^-2*8K*beta^(-1/K), smaller than exp(20K log K). For K>=1000 this is <=exp(K^2). If s>=beta/4, exp(K^2)s^(1/K)>=1, covering the remaining range. This proves Q7 with the actual displayed K, not a hidden larger finite-type order.

### 4. Quantization, aliases and cutoff powers

For integer labels u,v, the ordinary Weyl product phase is exp(pi i sigma(u,v)/N), retaining all aliases. The product error is bounded by C/N times the two first weighted Fourier l1 norms; H3 controls these in dimension two. H2 controls the unweighted Fourier l1 norm.

The commutator's sine remainder is bounded globally by C*N^-2*|u|^3|v|^3 after multiplication by N. The u sum is finite for g; H5 controls the v third weighted l1 norm. Fixed-time Duhamel and bounded H5 composition over the extremely small fixed interval yield Q8. These constants can be bounded uniformly for |tau|<=10^-80 using the finite support and fixed Fourier bounds; no inverse power of tau is hidden. Exact cat Egorov has no error. The prefix embedding symbols have H5 norm <=C R_L^-5 by Cauchy and elementary Sobolev equivalence. Telescoping at most L unitary conjugations therefore gives Q9 without exponential growth of operator errors.

For the HS estimate, retain one centered N-by-N Fourier cell. Its quantizations are exactly orthonormal in normalized HS norm. The retained coefficient l2 norm is bounded by the whole symbol L2 norm. The complementary l1 tail is bounded by H3 times

(sum_{v outside the cell}(1+|v|^2)^(-3))^(1/2) <= C N^-2.

This proves Q10 even when the symbol depends on N. Aliased terms are in the tail and are bounded before combining; no orthogonality of all integer labels is assumed.

Writing B=Op(a composed with F), Egorov implies A W=W B+W E. Cyclicity, the product bound, and ||Op(c)||<=C||c||H2 then give Q11, with the stated R^-3 and L R^-5 losses.

For the cutoff, use smooth fixed scalar functions h(t)=chi(t^2) and f(t)=(1-chi(t^2))/t, extended at zero. Then chi_epsilon=h(b/epsilon) and c_epsilon=epsilon^-1 f(b/epsilon). Derivatives of order at most three produce no worse powers than epsilon^-3 and epsilon^-4 respectively; bounded derivatives of b from Cauchy give bounds stronger than the deliberately loose R^-9 and R^-6 envelopes. This verifies Q12.

Support lies in |b|<=2epsilon. Q7 and the L2 square root give the first term in Q13, with the factor 2 safely inside exp(K^2). When 2epsilon>1 the trivial L2 bound suffices. Multiplying the errors gives R^-12*N^-1*epsilon^-4, L R^-11*N^-2*epsilon^-3, and the HS tail R^-9*N^-2*epsilon^-3, precisely covered by Q13. At epsilon=N^-1/8 the three powers are N^-1/(16K), N^-1/2, and N^-13/8. The fixed prefactor and every L,R loss are bounded by C0 exp(K^3). Small odd N are covered by the trivial unitary trace bound and the minimum in Q4.

### 5. Asymptotic exponent bookkeeping

Taking logarithms of the actual formulas gives log B_L=216L[log(24L)+2L log(14d0)]. Also J_L<=4000*8^L+1. Consequently log K_L=O_tau(8^L+L^2+L log(L+1)), including the ceiling effects. At L_N, 8^L_N<=(log log N)^(1/4) and L_N^2=o(log log N). Thus log K=o(log log N), K=(log N)^o(1), and in particular K^4 log K=o(log N). Both exponents in Q4 tend to negative infinity. The supremum over words uses a common bound and does not require summing over their number.

## Strong-obstruction details

### 1. Gaussian residual and the actual raw phase convention

For all integer labels, the frozen raw-to-midpoint identity gives

(W_N(a,b)psi)(j)=exp(2pi i b(j+a/2)/N) psi(j+a).

Take centered representatives and epsilon=N^-1/2. The normalized periodized vector differs exponentially from epsilon^(1/2) f(epsilon j), f(y)=2^(1/4)exp(-pi y^2). Fixed shifts crossing the cell boundary occur only in exponentially small tails. The exact continuous action is

exp(epsilon L_v)f(y)=exp(2pi i b(epsilon y+epsilon^2 a/2)) f(y+epsilon a),

where L_v=a d/dy+2pi i b y. Taylor expansion through order two is valid in Schwartz seminorms for these fixed labels, so the sampled norm remainder is O(epsilon^3) as well: a polynomial times a Gaussian bounds the remainder uniformly, and its grid sums are uniformly bounded. This supplies a precise justification for the candidate's Gaussian Riemann-sum step; L2 convergence alone is not being used to imply convergence on arbitrary samples.

The constant term cancels using sum c_v=a(P); the first-order term cancels because the two Fourier first moments vanish when da(P)=0. The surviving scaled residual has limiting norm at most one half sum |c_v| ||L_v^2 f||. With z=-a+ib,

L_v^2 f=2pi a z f+4pi^2 z^2 y^2 f,

and ||y^2 f||=sqrt(3)/(4pi). Thus ||L_v^2 f||<=pi(2+sqrt(3))|v|^2<12|v|^2. The constant 6 in S3 is valid.

### 2. Cat powers, phase cancellation and outlier

Exact cat Egorov transports A_N-9/10 on M_N^-j phi_N to Op(g composed with S^j)-9/10 on phi_N. These symbols have the same equilibrium and zero differential. The frequency second moment grows by at most ||S||^(2j), and ||S||_2^2=19+6sqrt(10)<49. Using 6*52 yields exactly B_j=312*7^(2j), for fixed j=0,1,2.

For the rephased Q'=exp(-i tau N*9/10)Q, the spectral-theorem inequality |exp(i t lambda)-1|<=|t lambda| gives S6 for every real t=tau N. This does not require tau N small. It also holds for Q'^*. The commutator C is unchanged by this scalar rephasing, and the displayed telescoping identity for C-I is exact. Applying it to phi_N and M_N^-1 phi_N gives S7 with B0+B1 and B1+B2. D is its exact cat conjugate.

The unitary identity Re<phi,Vphi>=1-||(V-I)phi||^2/2 yields the Rayleigh formula exactly. The constants are B0=312, B1=15288, B2=749112; the total loss is exactly 146137680000*tau^2, strictly smaller than 10^-148. The variational principle proves S2 through all odd N. This argument does not depend on a metaplectic squeeze approximation, its phase convention, or any Ehrenfest-time propagation estimate.

### 3. Free comparison norm and spectral conclusion

The elements q_j=m^j q m^-j for j=0,1,2 freely generate: after adjacent equal j blocks are combined, intervening m powers are nonzero and q blocks cannot cancel. The substitution c=q0 q1^-1, d=q1 q2^-1 has inverse q1=d q2, q0=c d q2. Hence (c,d,q2) is a free basis and c,d freely generate rank two. Restricting the regular representation of the ambient free group to this subgroup is a direct sum of its regular representations, so its polynomial norm is the subgroup norm.

For four-regular-tree adjacency A and f(v)=3^-distance(v,root)/2, Af/f is 2sqrt(3) away from the root and 4/sqrt(3) at the root. Weighted Schur bounds the norm by 2sqrt(3), despite f not belonging to l2; the argument is first applied to finitely supported test vectors. Truncating f at radius R gives norm squared 1+4R/3 and adjacency quadratic form 8R/sqrt(3), proving the reverse bound. Dividing by 4 gives sqrt(3)/2. No external free-norm citation is needed because the note supplies a complete internal proof.

Frozen fixed-word freeness gives convergence of all moments of H_N. Uniform support in [-1,1] gives weak empirical convergence; the outlier variational bound lies above the limiting support. Its mass proportion must vanish, but the proof claims no count or rate. The derived H polynomial is not the single BGS propagator U_N.

## Minimal clarifications and exact remaining boundary

No repair is necessary for promotion of these exact claims. For readability only:

- In Q3 write “a first-order coordinate derivative” rather than “a first coordinate derivative,” to avoid suggesting that only the q derivative is allowed.
- Say once that Sobolev Hs uses a fixed standard torus convention. Equivalent conventions only change fixed constants.
- In S2 mention Schwartz-seminorm Taylor control before sampling, as justified above; this avoids the false general principle that L2 convergence alone controls point samples.
- State that subgroup restriction is a direct sum over cosets when identifying the free polynomial norm.

The strongest safe combined statement is the explicit triple-logarithmic uniform trace law together with failure of strong freeness for this fixed polynomial. None closes the original signed microscopic implication. The cheapest next check is byte-for-byte hash validation when copying these accepted sources and this audit into a checkpoint; no additional mathematical route is needed for this review.
