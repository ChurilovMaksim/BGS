# Rare shadowing failures and coherent history selection

Research continuation, 2026-09-16. **Status:** proved symbolic estimates and finite-dimensional obstructions; the geometric periodic-orbit application is conditional on the explicit input (EQ) below. The quantum BGS step remains open. These are internal derivations, not a priority claim.

This continues the user's fixed-map proposal, particularly its TUBE-SAT, QTSB and EXT-FIBER claims. It does not import all of that proposal's [PROVEN] labels. Local working checkpoints 18bb3c7 and e0ada2e were not on remote main when this note was prepared; this note is self-contained. Remote base was 479ce7ef11e554609d44ecb101b7237cef346cdf.

## 1. A uniform filling estimate, with no independence assumption

Let Sigma be a two-sided mixing subshift of finite type on b symbols, with shift sigma. Choose q such that the q-th power of its adjacency matrix is strictly positive. Let psi:Sigma->R be bounded, M=||psi||infinity, and assume summable two-sided variations:

    v_r = sup{|psi(x)-psi(y)| : x_i=y_i for |i|<=r},
    V = sum_(r>=0) v_r < infinity.

Hölder potentials satisfy this. For an m-periodic code x give it probability proportional to exp(S_m psi(x)), counting marked periodic codes. Work with m large enough that the chosen disjoint blocks have a nonempty complement.

Fix an admissible target word of length n. Given any admissible outside configuration, a block of length

    h = n+2q+2

has an admissible filling containing the target word at a prescribed central location: use q-step connecting words at its two ends and absorb harmless extra positions into the bridges. Increasing q once if necessary makes every length >=q admissible between all endpoints. The target word and location are fixed; the bridges may depend on the two outside endpoint symbols.

Compare this filling with any other filling of the same block. Their periodic extensions differ only in that block and its m-periodic copies. Terms of S_m psi inside the block differ by at most 2Mh. For a term outside, agreement extends up to its cyclic distance from the block; at most two terms occur at each such distance. Thus the total outside difference is at most 2V (enlarging this fixed constant is harmless at the nearest endpoints). There are at most b^h possible fillings. Therefore, conditionally on the entire complement,

    Prob(target occurs centrally in the block | outside)
       >= p_h := exp(-2V) exp[-(log b+2M)h].                 (1)

If necessary decrease the prefactor to cover the finitely many shortest lengths. No mixing rate or independence of successive blocks was used.

For J disjoint blocks, let G_j be the corresponding target event. The earlier events G_i^c, i<j, are measurable outside block j. Conditional expectation and (1) give

    Prob(intersection_(j=1)^J G_j^c) <= (1-p_h)^J
                                    <= exp(-J p_h).        (2)

This is a finite-volume inequality, uniform in the period and in all admissible outside configurations.

For an invariant Gibbs measure, the same bound holds with a fixed smaller prefactor in p_h. To see this without assuming conditional independence, first condition on a finite exterior cylinder. Use common infinite continuations for the possible fillings and the Gibbs cylinder bounds. Their ratio is at least G^-2 exp(-2Mh-2V), where G is the Gibbs constant; divide by at most b^h fillings. Pass to conditioning on the full complement by martingale convergence. Then apply the same tower argument.

## 2. Symbolic shadow tubes at Heisenberg periods

Apply Section 1 to a product coding of two copies of the same dynamics. Its alphabet size is B=b^2 and its potential is Psi(x,y)=psi(x)+psi(y). Write

    K = log B+2||Psi||infinity.

Assume the coding map has the standard quantitative property

    codes agree on [-r,r] => distance of coded points <= C theta^r,
    0<theta<1.                                            (3)

For two orbit segments to remain delta-close for times 0,...,ell, it suffices that their codes agree on [-r,ell+r], with C theta^r<=delta. In each block prescribe any one admissible common word in both coordinates over these indices. Product primitivity supplies the bridges, uniformly over the two pairs of exterior endpoints.

Choose

    delta_N=N^-a,
    ell_N=floor(c log N),
    r_N=ceil((a log N+log C)/|log theta|).

The filling length is

    h_N=(c+2a/|log theta|) log N+O(1).

Hence the conditional success probability is at least C_1 N^-kappa, where

    kappa = K(c+2a/|log theta|).

Choose positive a,c small enough that kappa<1. For m in [tau_0 N,tau_1 N], placing J=floor(m/h_N) disjoint blocks yields, in the normalized periodic symbolic Gibbs measure,

    Prob(no delta_N shadow tube of length ell_N anywhere)
       <= exp[-C_2 N^(1-kappa)/log N].                    (4)

The same bound holds for invariant Gibbs histories over a time interval of length comparable to N. In particular the probability is O(N^-A) for every fixed A.

This strengthens the polynomial second-moment estimate in the uploaded TUBE-SAT at the symbolic level. The constants depend on the coding and potential; the numerical exponents a=1/20 and c=1/(80 log 8) from that upload are NOT asserted to satisfy the new budget. Smaller positive exponents may be required.

This is a standard Gibbs filling mechanism applied to this research problem, not a claimed new general hitting-time theory.

## 3. A careful transfer to geometric periodic pairs

Directly identifying all geometric period-m points with period-m codes can fail at Markov boundaries. We do not silently assume a one-to-one periodic coding. The following alternative separates the needed external input.

Let F preserve area, admit the preceding mixing Gibbs coding for its area measure, and have exponential derivative growth. On the product space let mu_2=dx dy. Let P_m^(2) be the normalized stability-weighted periodic-pair measure used in the upload. Assume that for some alpha,gamma>0,

    |P_m^(2)(A)-mu_2(A)|
        <= C exp(-gamma m) ||A||_(C^alpha)                (EQ)

for every Hölder observable A on the product space, with the constant independent of A and m. This is precisely the one-mark, norm-uniform periodic equidistribution input needed here. The upload asserts an appropriate marked theorem, but its exact source-to-model bridge has not been independently completed in this note. Consequently the geometric application here is CONDITIONAL ON (EQ).

Choose kappa<xi<1 and use only the first T_N=floor(N^xi) iterates of a period m comparable to N. Let 0<=chi_delta<=1 equal 1 on distance <=delta and vanish at distance >=2delta, with Hölder norm O(delta^-alpha). Set

    b_N(x,y)=product_(k=0)^ell chi_delta(F^k x,F^k y).

Place the block starts t_j within that initial interval, leaving room for the r_N margins, and define the smooth avoidance majorant

    A_N=product_j (1-b_N composed with (F x,F y)^(t_j)).

On the event of no 2delta shadow tube anywhere, A_N=1. A successful common target word in a block forces its corresponding b_N=1. Thus the invariant Gibbs filling argument gives

    mu_2(A_N) <= exp[-C N^(xi-kappa)/log N].               (5)

Since every factor lies in [0,1], a telescoping product bound gives

    ||A_N||_(C^alpha)
      <= 1+sum_j ||b_N composed with (F x,F y)^(t_j)||_(C^alpha)
      <= exp(C' N^xi+O(log N)).

Using (EQ), uniformly for m in [tau_0 N,tau_1 N],

    P_m^(2)(no 2delta_N shadow tube)
       <= exp[-C N^(xi-kappa)/log N]
          + C'' exp[-gamma tau_0 N+C' N^xi+O(log N)]
       = O_A(N^-A), for every fixed A.                  (6)

Using a sublinear observation interval is essential here: it keeps the Hölder norm subexponential in the full period. It also avoids importing an unproved periodic coding multiplicity statement.

The estimate survives multiplication by any fixed power of N, including time-count and finite-dimensional losses. It does NOT survive an uncontrolled exponential coherent-history factor.

## 4. Rare positive histories can have large coherent traces

Here is an exact obstruction to deducing the quantum conclusion just from (6), Parseval normalization and unitarity.

Take the two-dimensional unitary

    H = (1/sqrt(2)) [[1,1],[1,-1]].

Resolve the identity by the two coordinate projections. A length-R path has amplitude product H_(x_(j+1),x_j). Keep precisely the paths avoiding the transition 1->1. This is a local finite-state condition.

Their coherent sum is exactly B^R, where

    B=(1/sqrt(2)) [[1,1],[1,0]].

Their positive open-history mass, normalized by dimension two, is

    p_R=(1/2) 1^T P^R 1,    P=(1/2)[[1,1],[1,0]].

With phi=(1+sqrt(5))/2,

    p_R=O((phi/2)^R) -> 0,
    ||B^R||op=(phi/sqrt(2))^R -> infinity.

For even R the coherent trace is

    Tr B^R=(phi/sqrt(2))^R+(-1/(phi sqrt(2)))^R,

which also grows, although H^R=I and Tr H^R=2. The complementary paths cancel this growth in the full unitary sum. Restricting both paths in Liouville space gives coherent trace |Tr B^R|^2 while their positive history mass is p_R^2.

At R=12 the positive single-history mass is exactly 305/4096, while the coherent trace is 161/32. This is not a numerical asymptotic claim: the two eigenvalue formulas prove the opposite exponential behaviours for all R.

The exact history isometry and its projected direct-sum norm remain valid. The invalid step would be identifying projection in the recorded-history space with coherent recombination of its selected paths. They are different operations. This example does not refute BGS or the upload's explicitly open QTSB; it refutes a proposed general shortcut to QTSB.

## 5. Which transition masks are universally contractive?

Let M be a finite square zero-one matrix and S_M(X)=M entrywise-multiplied by X. The following elementary finite-dimensional classification is KNOWN Schur-multiplier theory.

S_M contracts the operator norm for every X if and only if its support is a disjoint union of rectangles I_s x J_s, with the I_s mutually disjoint and the J_s mutually disjoint. Equivalently, M has no 2-by-2 submatrix with exactly three ones.

Proof of sufficiency: write S_M(X)=sum_s P_(I_s) X P_(J_s). Orthogonality of the input and output blocks gives

    ||S_M(X)v||^2 <= ||X||^2 sum_s ||P_(J_s)v||^2.

For necessity, absence of a three-one corner says any two row supports are either disjoint or equal, giving the rectangle structure. If a corner exists, compress to it and, after permuting rows and columns, use the unitary

    U_0=(1/sqrt(3)) [[1,sqrt(2)],[sqrt(2),-1]].

Deleting its bottom-right entry gives a symmetric matrix with eigenvalues 2/sqrt(3) and -1/sqrt(3), hence norm 2/sqrt(3)>1. Complete the two-dimensional unitary on the other rows and columns to get the same obstruction in the full matrix. This proves necessity even if testing only unitaries.

Prior work: Rupert H. Levene, *Norms of idempotent Schur multipliers*, New York J. Math. 20 (2014), 325–352, arXiv:1302.4849v2. The primary PDF was checked, including the complete-bipartite characterization used in Section 6. The proof above is included to make this application self-contained; the classification is not claimed as a discovery.
https://arxiv.org/pdf/1302.4849

For the research programme, a geometric history selector must either possess a compatible contractive structure, be shown small for the actual quantum operator, or come with a separate coherent Gram bound. Small classical mass alone supplies none of these.

## 6. What changed and what remains open

The classical rare-set estimate can be made superpolynomial: unconditionally in the specified symbolic Gibbs models, and for geometric stability-weighted periodic pairs under (EQ). This removes the polynomial time-normalization problem from that classical branch.

However, a positive history probability and its coherent contribution can behave in opposite ways. A first-witness projection being contractive on the record space does not prove that its coherent exterior recombination is contractive. The explicit local-mask example locates the issue more sharply than a generic warning about interference.

The next model-specific target is a quantitative coherent envelope for the actual matched/unmatched selector, or an exact contractive localization realizing the desired tube events. The fixed-map pair theorem and the subsequent all-k BGS theorem remain unproved. No Nobel/Fields-level result or novelty is claimed.

## 7. Executed and blocked checks

The local execution environment disconnected before the newly prepared Python verifier could be written or run. No Python mask enumeration is claimed.

An independent connected Wolfram kernel DID execute the companion file computations/verification/history_localization.wl. It returned:
- exact eigenvalues for H, B and P;
- positive masses 5/8, 13/32, 89/512, 305/4096 at R=2,4,8,12;
- coherent traces 3/2, 7/4, 47/16, 161/32;
- the mask witness eigenvalues 2/sqrt(3), -1/sqrt(3);
- all 16 exact rational periodic-Markov avoidance checks passed.

The Markov check uses a positive two-state transition matrix, its product chain, and exact cylinder exclusion matrices. It is a finite regression of the conditional filling inequality, not a proof of the Gibbs theorem or of (EQ). No Lean verification or full repository test run is asserted.
