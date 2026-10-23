# Executed source-transfer checkpoint: exact occupation projection and extensive repeats

6 October 2026. Read-only canonical base d4132ccee82849b644520d88c953cb9b33382a59. Author-level result, not independently reviewed. No canonical edits. TRACE-005 remains OPEN.

## Result

One recent mechanism was selected for an actual transfer test: Kumar–Prosen–Roy's phase-projected permutation diagrams. The source's repeated-state bookkeeping is not an all-multiplicity resummation. For the actual fixed map, a direct lemma proved below shows that triple repeated coordinates are extensive under the positive cyclic path measure at Heisenberg time: T/N tends to c^3/6 in L2 when m/N tends to c>0. This does **not** prove that a signed omitted diagram sum is large. It identifies why the source's double-repetition truncation cannot be justified here by rarity.

The usable transfer is an exact occupation-polynomial replacement that includes every repetition and works for the entire pair/cubic leaf. It exposes a signed charge-zero term and a signed nonzero-charge remainder; no estimate for the latter is currently established. Origin averaging removes neither. This is a narrowly executed method checkpoint, not a theorem proving universality, nor a generic spectral-rounding control.

## Primary source contract (194 words or fewer)

Vijay Kumar, Tomaž Prosen, Dibyendu Roy, *Leading and beyond leading-order spectral form factor in chaotic quantum many-body systems across all Dyson symmetry classes*, [arXiv:2502.04152v1](https://arxiv.org/html/2502.04152v1), 6 February 2025; primary record lists Phys. Rev. X 16, 031019 (2026), DOI 10.1103/kwh6-hncn. Checked 6 October 2026. Version v1 is the only arXiv version listed.

Relevant locators: §II (10)–(29), Theorems 2–3, §IX.1 (66), §X.2 (75)–(78). The phase average requires independent uniform phases (with the stated Kramers exception). For the symmetry class without time reversal, its transition matrices are formed from the kick in the unperturbed eigenbasis. Equation (21) subtracts the first repeated-state overcount. The paragraph following (29) explicitly restricts the calculation to double repetitions; higher repetitions require further corrections. Theorem 3 pairs reduced diagrams using column orthogonality. A local pairing is not a globally bijective, all-multiplicity signed cancellation theorem. Their reported spectral calculation is through second order, not the full microscopic mixed hierarchy.

Authentication and these local source statements were checked; the whole paper was not independently audited. No local source-byte hash is asserted.

## 1. Dictionary and the first hypothesis that does not transfer

In the physical factorization U=exp(i tau N A)M, taking the source's W=M requires expressing V=exp(i tau N A) in an eigenbasis of M. The source's Markov matrix is then |V|^2 in that basis. It is not the project's coordinate matrix P=|U|^2. Thus one cannot simply cite FM-021 for that source matrix.

There is a mathematically exact diagnostic ensemble which *does* retain P: set U(phi)=D(phi)U, D(phi)=diag(exp(i phi_j)). Traces are cyclic, so this has the same spectra as U D(phi). This changes the operator for phi not equal to zero; it is not a proposal to replace the frozen map. Independent phase integration is an exact projection available for comparison. The actual origin rotation is phi_j=alpha for every j, which is a one-dimensional subgroup of this N-dimensional torus. The distinction below is algebraic and requires no semiclassical approximation.

For m>=1, let

c_m(n)=sum over words x=(x_1,...,x_m) with occupancy n of product_r U[x_r,x_(r+1)], x_(m+1)=x_1.

Here n is a nonnegative integer N-vector with |n|=m. Every rooted coordinate word occurs once. Then exactly

p_m(phi)=sum_(|n|=m) c_m(n) exp(i n dot phi).

Consequently the independent-phase pair and cubic averages are

B_m=sum_n |c_m(n)|^2,
H_(a,b)=sum_(|n|=a,|k|=b) conjugate(c_a(n)c_b(k)) c_(a+b)(n+k).

These formulas include all repeated coordinates and the cubic coefficient is signed/complex. The corresponding fixed values at phi=0 contain, respectively, every n,n' and every n,k,l. Independent phase averaging keeps n=n' or l=n+k. Common origin averaging keeps **all** of them because total degree is neutral. For example exp(i(phi_i-phi_j)) has origin average 1 and torus average 0 for i≠j. This is an exact failed source hypothesis for the authorized origin probability space, not a claim that aggregate fixed-map errors cannot vanish asymptotically.

For any neutral product of traces, the same construction imposes equality of the sum of positive occupancies and the sum of negative occupancies. Thus it provides exact bookkeeping at every fixed factorial order (before applying the project's distinct-eigenvalue partition transform). It supplies no cancellation estimate.

## 2. Executed application to the long resolvent leaf

Retain q=exp(-2s/N), K=floor(c_0 log N), and the exact F_K from the reviewed loop report. Define

L_0=N^-2 sum_(m>K) q^m B_m,
C_0=N^-3 sum_(a,b>K) q^(a+b) H_(a,b),
R=N^-2 sum_(m>K) q^m (|p_m|^2-B_m)
 + N^-3 sum_(a,b>K) q^(a+b) (p_(-a)p_(-b)p_(a+b)-H_(a,b)).

Then the actual leaf numerator is exactly

L_0+C_0+R-1/(4s^2).

This identity concerns the fixed actual U and an explicitly defined diagnostic average. Fubini is legitimate: |p_m(phi)|<=N, so the pair and cubic series converge absolutely uniformly in phi for each N,q<1. Individual expanded occupation coefficients can be large, but each finite-degree polynomial is finite; take degree sums after the torus integral rather than claiming absolute convergence of an unrestricted coefficient-by-coefficient rearrangement.

The source's diagrams live in the zero-charge sector L_0 (and only a bounded time expansion thereof). They supply neither the cubic H nor the complete signed R. Vanishing of R relative to the loop denominator would still be a new fixed-operator theorem. This checkpoint does not assert that L_0+C_0 already has the required limit.

## 3. Actual-map lemma: triple visits are extensive

Let m/N→c∈(0,infinity), along odd N for which the inherited FM-021 bounds hold. Use the probability measure on rooted cyclic words

mu(x)=product_(r=1)^m P[x_r,x_(r+1)] / Z_m, Z_m=Tr(P^m).

P=|U_N|^2 is the **actual** position chain. FM-021 gives P_ij<=C/N and ||P^l-J||<=2^-l. Consequently every positive power has entries <=C/N, and Z_m=1+O(N 2^-m). Define

T(x)=sum_(1<=i<j<k<=m) 1{x_i=x_j=x_k}.

Then

E_mu T = binom(m,3)/N^2 + O(log N),
Var_mu T = O(N log N),
T/N → c^3/6 in L2(mu).

Constants may depend on a compact positive range of m/N and the inherited flatness constant; no effective startup is claimed.

### Proof of expectation

For a specified triple, the cyclic gaps a,b,d are positive and total m. The unnormalized coincidence mass is

sum_x (P^a)_xx (P^b)_xx (P^d)_xx.

Choose L=ceil(4 log_2 N). If all gaps are >=L, each factor is N^-1+O(N^-4), so the mass is N^-2(1+O(N^-3)). There are binom(m,3)+O(m^2 L) such triples. For the remaining O(m^2 L) triples, the mass is bounded by C^3/N^2. Division by Z_m proves the expectation estimate (the long-gap error is smaller than O(log N)).

### Proof of second moment and variance

Expand T^2 over ordered pairs of triples. Group by r, the size of their union.

For disjoint triples r=6. There are binom(m,3)^2+O(m^5) pairs. If all six cyclic gaps are >=L, the equality constraints leave two independent labels. Summing those labels, the joint mass is N^-4(1+O(N^-3)). The number of pairs with at least one short gap is O(m^5 L); each has mass <=C^6/N^4, using the entry bound for every gap. Their total is O(N L).

If the triples share exactly one time, r=5, their equality constraints leave one label and each mass is at most C^5/N^4. There are O(m^5) such pairs, giving O(N). If they share two times, r=4 and one label gives mass <=C^4/N^3; O(m^4) pairs again contribute O(N). Identical triples have r=3, mass <=C^3/N^2 and O(m^3) pairs, again O(N).

Therefore E T^2=binom(m,3)^2/N^4+O(N log N). The expectation estimate gives (E T)^2=binom(m,3)^2/N^4+O(N log N); subtraction proves the variance bound. Normalization Z_m changes these estimates exponentially little. Dividing by N^2 proves the L2 assertion.

This establishes that a mu-typical actual cyclic word has order N triple visits. It does not identify the size of a signed noncyclic contribution. In particular, a successful complete resummation may cancel extensive repetition terms; it cannot discard them on a rare-collision premise.

## 4. Cheapest exact multiplicity test

For the length-three word with all labels equal, the full unrestricted permutation sum has multiplicity 3!=6. Subtracting only the three pair coincidences, each with 3!/2!=3 representatives, leaves 6-9=-3. Its true once-counted multiplicity is 1. The missing correction is 4. This checks the precise combinatorial issue, rather than appealing vaguely to growing diagram counts. It is not a criticism of a source which explicitly retains an ellipsis and restricts its calculation to two orders.

The occupation coefficient avoids this issue by grouping each word once from the outset. It does not itself prove a globally cancellable path expansion.

## 5. Executed computation and boundaries

Command: python3 /workspace/shared/bgs_exact_method_search/check_transfer.py > checks.json.

Exact rational arithmetic on one explicitly displayed 3x3 rational orthogonal unitary. Checked pair m=2 and cubic (a,b)=(1,1),(1,2),(2,2),(2,3),(3,3) against a separate modular-exponent zero-selector, with modulus 13 exceeding all relevant component degrees. Checked triple-visit expectations by complete word enumeration at (N,m)=(3,3),(3,5),(5,6). All passed. The script also records the length-three multiplicity mismatch. The calculation is finite algebra verification, not an actual-map numerical experiment or proof of the analytic lemma; the latter has the direct proof above.

Read canonical AGENTS, SOURCE_OF_TRUTH, conventions, RESEARCH, current claim records, results/open questions, exact frozen symbol, relevant literature entries, reviewed loop report and its independent review, and reviewed rounding control. Prior project ownership: cyclic path measure and its mixing bounds are FM-021; raw-symbol/operator conventions are unchanged. Occupation grouping is elementary polynomial bookkeeping, not claimed novel. The new reported checkpoint is its source-specific transfer and the stated extensive-triple calculation under the actual inherited bounds.

Search boundary: primary-web queries for 2024–2026 deterministic chaotic maps, Anosov quantization, spectral determinants and spectral universality; one Parallel Search call; repository literature grep. The semiclassical-circuit and Riemann–Siegel mechanisms were already source-reviewed in the repo and were not relabeled new. Unrelated eigenfunction, open-map, and quantum-information-supermap papers were discarded. Only one mechanism was selected for detailed execution; no comprehensive literature or originality claim is made. No new source was found supplying the full signed fixed-map hierarchy.

## Next decisive question

An all-multiplicity signed resummation must handle the extensive repeated-port sector and the nonzero occupation charges simultaneously, or prove a separate cancellation theorem for the latter. A natural reusable exact algebra object is the multivariate determinant det(I-z D(phi)U_N), whose logarithm generates c_m; its coefficients retain the exact frozen U. Merely inserting independent phi averages discards the unestimated R. No further resummation estimate is claimed here.

## 6. All fixed multiplicities: the same proof closes

The triple lemma is not special. For each **fixed** integer r>=2, define

T_r(x)=sum_(I subset {1,...,m}, |I|=r) 1{all x_i, i in I, are equal}.

Under exactly the same actual cyclic measure, if m/N→c∈(0,infinity),

E T_r=binom(m,r)/N^(r-1)+O_r(log N),
Var T_r=O_r(N log N),
T_r/N→c^r/r! in L2.

For the expectation, r long cyclic gaps give one free label, hence mass N^(1-r)(1+O_r(N^-3)); O_r(m^(r-1)L) short-gap choices have mass <=C^r/N^(r-1), contributing O_r(L). For the second moment, disjoint r-tuples have 2r visits and two free labels, hence mass N^(2-2r); their short-gap exceptions number O_r(m^(2r-1)L), contributing O_r(NL). If the r-tuples overlap in h>=1 visits, their union has 2r-h visits, all with one common label. Its mass is <=C^(2r-h)/N^(2r-h-1), and there are O_r(m^(2r-h)) choices, giving O_r(N) for each h. Long-gap relative errors and the circular partition function are controlled exactly as in §3. This proves the formulas.

This is an all-fixed-r statement, with constants depending on r, not a growing-r uniform estimate. T_r counts r-element subsets of equal visits, not the number of sites visited exactly r times. The proof does not claim a Poisson occupancy law. It shows that at every fixed multiplicity, the actual positive cyclic measure contains extensive repeated visits. The target remains the full signed trace-pair/mixed hierarchy, not this positive measure.
