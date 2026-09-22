# Independent proof audit: smooth finite-orbit resonance rigidity

Date: 2026-09-22. Review type: independent derivation by a separate agent, not external peer review or formal verification.

## Normalized claim and verdict

**Primary verdict: proved as written.** No mathematical gap was found in Theorem 1, Lemma 2, Lemma 3, or their necessary finite-Fourier dependency after reconstructing the critical arguments below. This verdict concerns the exact stated finite-union-of-signed-orbits theorem. It does not establish priority, a quantitative uniform lower bound, arbitrary analytic support, or microscopic BGS.

Fix any hyperbolic A in SL(2,Z), C f(x)=f(A^T x), and any nonconstant real smooth g with nonzero Fourier support in finitely many signed A-orbits. For every R>=1 and every nonzero a in R^R, the smooth mean-zero function sum a_r {g,C^r g}/(4 pi) has a nonzero oriented-orbit Fourier sum, hence strictly positive orbit variance and is not an L2 C-coboundary. Constants in g are irrelevant. Complex linear independence follows from reality. The argument covers both signs of tr(A), arbitrary phases, and infinite two-sided coefficient sequences on each of the finitely many orbit families.

Authoritative target: `inputs/prior/BGS_research_20260922/repo_overlay/mathematics/finite_orbit_resonance_rigidity.md`, FO.1--FO.17. The dependency `manuscript/unified_sections/temporal_resonance.tex` was fetched directly from GitHub at `39d4e01ae6a6b3eb472ab30266b708ca71a70a16`; the exact labels audited are `lem:temporal-support` and `thm:temporal-independent`. The base repository was not yet present locally during this audit. Overlay AGENTS.md and pinned RESEARCH.md, claim ledger, results index, open questions and generic_wiener_resonance.md were inspected. No main-repository files were edited.

## Dependency graph

1. Hyperbolicity and integrality imply no nonzero integral eigenvector, no periodic nonzero frequency, and exponential growth in both time directions.
2. Smooth Fourier summability implies absolute orbit sums and every exponential moment in the time coefficient sequences.
3. The invariant quadratic form plus actual vector equality prove eventual uniqueness of pair channels for a fixed finite orbit family.
4. Two direct Fourier bracket identities convert zero variance into finite-support difference sequences for both bilinear and Hermitian correlations.
5. Holomorphy on C* and those finite-support differences imply Laurent-polynomial pair products.
6. Algebra over C[z,z^-1], removal of a finite divisor, and two involutions imply a common real zero-free all-pass factor.
7. Weighted absolute convergence gives exact invariance of every orbit sum under that factor.
8. The separately inspected finite-Fourier highest-lag witness excludes zero variance of any nonzero finite temporal combination.

All leaves needed here are elementary algebra/analysis or internal proofs directly inspected; no external research theorem remains as an unverified leaf.

## Obligation matrix

| Obligation | Outcome | Decisive point |
|---|---|---|
| Fourier convention and bracket sign | passed | {e_u,e_v}/(4 pi)=-pi det(u,v)e_(u+v) |
| Signed versus oriented orbits | passed | Signed families only parametrize g; variance and J use oriented orbits |
| Positive and negative trace | passed | B=sign(tr A)A has positive eigenvalues; signs stay in exact vector equations |
| Eventual pair separation, all exponents | passed | Q bounds m-n; expanding covector bounds t; fixed integer vector then vanishes |
| Same-sign channel | passed | Two ordered pairs produce -pi D[S(n-r)-S(n+r)] |
| Opposite-sign channel | passed | Conjugation changes the determinant sign and yields +pi D[K(n-r)-K(n+r)] |
| Negative n and nonzero temporal polynomial | passed | Swap/conjugate symmetries and a real coefficient vector |
| Rational-to-Laurent step | passed | A rational function holomorphic on C* has poles only at 0 and infinity |
| Common factor and real coefficients | passed | Coprime polynomial vector, Bezout, zero divisor removal, both involutions |
| Infinite rearrangements | passed | Every exponential moment dominates bracket growth |
| Finite-Fourier dependency | passed | Lexicographic exposed sum, orbit exclusion, nonzero determinant |
| Bounded invariant range consequence | passed | Product bound plus balanced expanding/contracting coordinates bounds lattice norm |
| Infinite orbit all-members extension | out of scope | Uniform isolation fails; arbitrary smooth extension is actually false |
| Lean, finite regression, external priority | out of scope | None is needed or claimed as proof evidence in this audit |

## Independent channel derivation

Fix n beyond the separation threshold and D=det(v_i,A^n v_j). The orbit of the plus frequency is parametrized by

    k_t=A^t v_i+A^(t+n) v_j.

The first ordered contribution uses frequencies A^t v_i in g and A^(t+n-r) v_j in the untransported second copy of g. Its bracket coefficient is

    -pi D c_(i,t)c_(j,t+n-r).

The reversed ordered contribution uses A^(t+n) v_j and A^(t-r) v_i. Reversing the determinant gives

    +pi D c_(j,t+n)c_(i,t-r).

Sum over t, then replace t by t+r in the second sum. The resulting orbit sum is exactly

    -pi D [S_ij(n-r)-S_ij(n+r)].

For k_t=A^t v_i-A^(t+n) v_j, the same ordered contributions are

    +pi D c_(i,t) conjugate(c_(j,t+n-r)),
    -pi D conjugate(c_(j,t+n)) c_(i,t-r).

Their sum is exactly

    +pi D [K_ij(n-r)-K_ij(n+r)].

No complex conjugate is inserted into S. No extra factor of two occurs even when i=j: the two ordered contributions are already displayed, and n>0 distinguishes their time locations. Additional signed-family representations are excluded by Lemma 2. Nonzero frequencies cannot equal their own negative iterate. These details validate both signs and oriented-orbit multiplicities in FO.10.

For F_X(z)=sum_n X(n)z^(-n), the coefficient of z^(-n) in (z^(-r)-z^r)F_X is X(n-r)-X(n+r), so the generating-function convention also agrees exactly. The symmetries give B^S_ij(-n)=-B^S_ji(n) and B^K_ij(-n)=-conjugate(B^K_ji(n)); reality of a is used in the latter. Thus the right-tail vanishing really yields finite two-sided support.

## Independent large-gap separation check

For Q=xi eta, Q(Az)=Q(z), and for each fixed pair of nonzero integral vectors the leading term of Q(u+epsilon A^n v) is epsilon s^n eta(u)xi(v)lambda^n. Its coefficient cannot vanish. A purported unbounded sequence of nontrivial collisions therefore forces m to infinity and bounds m-n, independently of the outer iterate t. After passing to finitely many index/sign choices and a fixed integer b=m-n, the xi coordinate bounds lambda^t above and below, so t belongs to a finite set. Passing to fixed t yields

    v_i-zeta A^t v_k = A^n(zeta delta A^(b+t)v_l-epsilon v_j).

The vector in parentheses is an integer vector because A is unimodular even for negative powers. A nonzero integer vector has a nonzero expanding component and its A^n image is unbounded. Therefore both sides vanish. Distinct signed representatives force i=k, j=l, and the no-period/no-antiperiod property forces t=b=0, zeta=1, delta=epsilon. This contradicts nontriviality.

The actual vector equation is indispensable: Q equality alone would not establish orbit equivalence. The determinant estimate follows from the same nonvanishing expanding/contracting components. This is a qualitative existence proof of n0, not a numerical cutoff claim.

## Independent factorization check

The ratios P_i/P_1 are rational. Over the PID C[z,z^-1], choose a coprime Laurent-polynomial vector q with P_i=F q_i. Bezout makes F a holomorphic linear combination of the P_i. Every zero of F is a zero of the nonzero Laurent polynomial P_1 P_1*, including multiplicity, hence there are only finitely many. Removing precisely this finite divisor gives holomorphic zero-free F0 and Laurent-polynomial factors.

Both F0(z)F0(1/z) and F0(z)F0*(z) are rational, holomorphic and zero-free on C*. They must be c z^m and d z^n. Inversion symmetry forces m=0. On |z|=1 the second expression equals |F0(z)|^2>0, which forces n=0 and d>0. Since F0(1) is nonzero, normalizing by F0(1) makes both constants one. The two identities then imply R(1/z)=R*(z), equivalently R(w)=conjugate(R(conjugate(w))), so every Laurent coefficient is real.

There is no unjustified boundedness assumption at either puncture: essential singularities are allowed for R itself, while only its products were proved rational. Nonmonomial factors such as exp(a(z-z^-1)), a real, remain admissible. Cauchy bounds on arbitrarily large and small circles give all exponential moments of their Laurent coefficients. This suffices for the smooth operator sum and orbit-sum rearrangement.

## Finite-Fourier dependency reconstructed

For the finite symmetric support V, choose expanding/contracting maxima X,Y and Lambda=lambda^r. The manuscript's linear form L=xi/X+Lambda sigma eta/Y has a trial sum at least 2 Lambda. Lexicographic maximization of (L,xi), separately on V and B^r V, makes the resulting ordered decomposition unique even if L has ties.

The relevant contradictions are:

- An iterate q>=1 landing in any lag j<=r would give L(k)<=Lambda+Lambda/lambda+1+1/lambda<2 Lambda.
- An iterate q<=-1 would give L(k)<=1+Lambda+Lambda/lambda+Lambda/lambda^2<2 Lambda.
- A lower lag j<r at q=0 would give L(k)<=1+Lambda+lambda^j+lambda^(r-j)<=1+Lambda+lambda+lambda^(r-1)<2 Lambda.

For integral trace magnitude >=3, lambda>= (3+sqrt(5))/2. The first two gaps are positive already at r=1, and the third is positive at r=2. The determinant-zero case, with u=c B^r w and R=|c|, is bounded by

    (1+R)[min(Lambda,1/R)+min(1,Lambda/R)]
    <= Lambda+2+1/Lambda < 2 Lambda.

On R<=1/Lambda, 1/Lambda<=R<=Lambda, and R>=Lambda, the expressions are respectively (1+R)(Lambda+1), 2+R+1/R, and (1+1/R)(Lambda+1). Each attains its largest allowed value at the displayed boundary values. Thus determinant zero is impossible. The isolated coefficient is nonzero, and the negative oriented orbit is distinct, proving the finite-Fourier lower bound with factor two. This closes the actual dependency rather than assuming its dashboard status.

## Real gaps and editorial clarifications

No missing implication was identified in the stated finite-orbit theorem. The following remain real boundaries, not defects of that theorem:

1. n0 depends on the entire finite family. Adding new families can create collisions at arbitrarily late gaps. No family-uniform threshold has been proved, and FO.17 explains why that route fails.
2. Strict positivity under finite truncation cannot be passed to a limit without a lower bound surviving truncation.
3. Arbitrary smooth infinite-orbit all-members positivity is false: the pinned temporal_resonance.tex already constructs a nonconstant Gevrey bump with derivative support disjoint from its pullback, giving {g,Cg}=0. A proposed extension must not silently forget this counterexample.
4. The theorem is a classical cohomological statement. It supplies no Heisenberg-time quantum trace comparison.

For exposition alone, explicitly stating that FO.10 sums over k_t=A^t(v_i+/-A^n v_j), and explicitly invoking the Laurent PID in Lemma 3, would reduce reader effort. These are clarifications, not repairs.

## Concrete infinite-orbit perspective

The existing generic_wiener_resonance.md already proves open-dense positivity for lag one; that result must be credited, not rediscovered as new. Its same continuity argument and the now-audited finite-Fourier all-lag theorem immediately extend the generic statement to every fixed number of lags, and then to residual simultaneous independence of all positive lags. No novelty is claimed for this elementary extension.

For a quantitative form, write M1(f)=sum_k |k| |fhat(k)| and let T_g:R^R -> ell2(oriented orbits) have column r equal to J(h_r(g)). For any smooth g,q,

    ||J(h_r(g))-J(h_r(q))||_ell2
    <= pi ||A^r|| M1(g-q)[M1(g)+M1(q)].

Consequently, with

    E_R=pi M1(g-q)[M1(g)+M1(q)](sum_(r=1)^R ||A^r||^2)^(1/2),

one has

    sigma_min(T_g) >= sigma_min(T_q)-E_R.

Every q satisfying sigma_min(T_q)>E_R therefore certifies positivity for every nonzero combination of its first R lags, even if g has infinitely many orbit families. The estimate follows from the Fourier determinant bound and ||Jf||_ell2<=||fhat||_ell1, then the finite-dimensional singular-value perturbation inequality. This supplies a useful certificate for selected infinite-support observables; it does not imply that some truncation q will satisfy the inequality for every analytic g.

The genuinely unresolved all-members analytic question remains nonlinear: can a nonconstant real analytic g have {g,Cg}/(4 pi)=u-Cu with analytic u? To extend the finite-family proof toward that question, one needs a bound on the contributions of *all other families* to selected pair-channel orbit sums that is strictly smaller than a certified surviving core signal. Analytic Fourier decay alone has not been shown here to dominate cancellation of that core signal. This named inequality is the next substantive obligation; further finite collision enumeration cannot replace it.

## Execution and evidence scope

Read commands used cat/rg for the overlay and the exact GitHub raw-file connector for pinned dependencies. The proof was checked by direct derivation, not by trusting previous audit notes. No finite computation was used as universal proof evidence; no Lean or Wolfram build was performed in this subtask. The previous finite regression outputs were not revalidated here. This report intentionally separates proof review from execution verification.
