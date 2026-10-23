# Balanced coordinate phases: source contract and exact obstruction checks

6 October 2026. Read-only canonical base: BGS `801de3ab760cab4349e68b9843dcd67955314e62`. All outputs are outside the canonical repository. Author-level audit and elementary deductions; no independent review, canonical edits, publication, or priority claim.

## Verdict

**Incomplete, with the smallest missing implication identified.** None of the primary results checked supplies a rigorous full compact-weight Heisenberg pair theorem for the independent-coordinate-phase ensemble of the prescribed matrix. The most directly relevant unitary-stochastic statement is a conjecture. The closer supersymmetric construction does not provide the necessary nonlinear, all-order, noncompact remainder bound. Even a proved annealed theorem would leave the original deterministic off-charge defect.

The useful additional results of this pass are exact discriminants for a nonlinear coordinate-slice replacement and a repeated-index projector replacement; a precise graph-embedding obstruction; and an elementary rigorous propagator estimate that repairs one local estimate without claiming to repair the full argument.

## 1. Exact target and inherited inputs

Keep every odd dimension and exactly

U_N = exp(i 10^(-80) N A_N) M_N,

with the raw symbol, midpoint convention and normalization in `mathematics/fixed_map_path_model.md`. Let

B_N(m) = E_theta |Tr[(D_theta U_N)^m]|² = sum_{|n|=m} |c_m(n)|².

This equality includes every coordinate occupation multiplicity and every m. It is the prior exact-method report's occupation projection, not a new identity. The original common-origin average does not impose this projection. Define

R_N(m) = |Tr U_N^m|² - B_N(m).

For every w in C_c^infinity((0,infinity)), the full pair target splits exactly into

N^(-2) sum_m w(m/N)[B_N(m)-min(m,N)]
+ N^(-2) sum_m w(m/N) R_N(m) -> 0.

The first summand is the proposed annealed bridge; the second remains original fixed-operator data. Neither is established here.

FM-021 supplies eventual bounds max P_ij <= C/N and ||P-J||_2 <= 1/2, where P=|U|² and J_ij=1/N. Its startup N_0 is not effective. FM-022 supplies ||Q||_2 -> 0 for Q_ij=U_ij conjugate(U_ji), and reverse-cyclic suppression. These are stronger than the eigenvalue-gap assumptions at the quadratic level, but are not estimates of the full nonlinear phase integral. No finite dimension, including N=7, is silently excluded from the exact identities. The asymptotic deductions only assert N>=N_0; they do not claim numerical access to that threshold.

## 2. Primary-source contracts

### Tanner 2001: the direct eigenphase ensemble

Gregor Tanner, *Unitary stochastic matrix ensembles and spectral statistics*, arXiv:nlin/0104014v1 (6 April 2001), J. Phys. A 34 (2001), 8485–8500. Primary PDF: https://arxiv.org/pdf/nlin/0104014v1 . Inspected §§II.B, III.A–B, equations (8)–(20), especially p.7 after (20). The left/right phase orbit of a fixed unitary has the same spectral law as a single independent diagonal phase layer, by diagonal conjugation and multiplication of phases. Thus this is the relevant eigenphase variant, with dimension N directly. The gap criterion is explicitly proposed as a conjecture; the deduction from diagonal approximation to the entire form factor is not proved. No full plateau theorem is available from this source.

### Gnutzmann–Altland 2005

Sven Gnutzmann and Alexander Altland, *Spectral correlations of individual quantum graphs*, arXiv:nlin/0508009v1 (3 August 2005), Phys. Rev. E 72, 056215. https://arxiv.org/pdf/nlin/0508009v1 . Relevant: §II.C–D and (20); §IV.B, (58)–(66); Appendix A, (A1)–(A5). The paper discusses the eigenphase variant explicitly, and uses a phase-average representation. Its massive-mode validity test is quadratic; the classical gap scaling is stricter than Tanner's. Simple-graph locality is used to eliminate off-direction blocks. The statements do not supply a quantitative bound on the complete nonlinear remainder for arbitrary dense U_N. The zero-mode integral captures full RMT correlations formally, but an exact zero-mode evaluation is not itself a bound on the omitted modes.

### Pluhař–Weidenmüller 2015

Z. Pluhař and H. A. Weidenmüller, *Quantum Graphs and Random-Matrix Theory*, arXiv:1407.1148v2 (9 March 2015), J. Phys. A 48, 275102, DOI 10.1088/1751-8113/48/27/275102. https://arxiv.org/pdf/1407.1148v2 . Checked §§2, 2.2, 3.4 and 6; (46), (51)–(56); printed pp.2–6, 14–20, 30–33. The stated all-(P,Q)-correlation claim assumes simple connected graphs, incommensurate bond lengths uniformly bounded above/below, a uniform nontrivial Perron–Frobenius gap, and a uniform bound below one on products of the two endpoint backscattering amplitudes. Its one-step operator acts on 2B directed bonds with paired bond phases. Section 3.4 treats arbitrarily high terms individually; no uniform summed remainder is extracted here. A literal application to the prescribed odd-N ensemble fails before such an extension is imported.

### Weidenmüller 2018/2020: the closest phase action

H. A. Weidenmüller, *Massive Modes for Quantum Graphs*, arXiv:1812.00655v1 (3 December 2018), chapter in *Discrete and Continuous Models in the Theory of Networks* (2020). https://arxiv.org/pdf/1812.00655v1 . Checked §§1–5, especially (3), (22)–(23), (33)–(35), (43)–(47), (49)–(53). It averages independent directed-coordinate phases and uses the dense-entry scale and fixed gap. Thus its phase action is closer to the requested ensemble. But §§4.3–5 explicitly make the massive-mode conclusion conditional on non-rigorous average-based estimates. The author also revisits the nonlinear coset issue left untreated by the earlier papers. This is not an imported rigorous estimate of the entire phase integral. Sections 3 and 4 below give direct algebraic tests of two proposed replacements, without disproving universality.

### Recent rigorous adjacent result

Anna Maltsev and Mohammed Osman, *Mesoscopic Linear Statistics for Two Ensembles of Quantum Graphs*, arXiv:2607.02356v1 (2 July 2026). https://arxiv.org/html/2607.02356v1 . Checked Definitions 2.3–2.4, Theorems 2.1–2.2 and the paragraph following (2.13). One model randomizes a regular graph and edge lengths; the other independently Haar-randomizes vertex matrices on a complete graph. The variance errors are O(eta^(1/2)+(N eta³)^(-1)) and O(eta^(1/2)+(N eta²)^(-1)+phi(N)), respectively. Here N counts vertices, and the second graph has order N² edges. These are mesoscopic variance results, not the fixed deterministic scattering matrix's microscopic independent-phase law or its Heisenberg plateau.

## 3. Exact nonlinear-slice discriminant

Consider just an admissible real bosonic body of the componentwise map in the 2018 source's (33). It is

xi_i = psi_i / sqrt(1+psi_i²).

Take psi=(1/2,1/2,-1,0). Then sum_i psi_i=0, while

sum_i xi_i = 2/sqrt(5) - 1/sqrt(2) > 0.

All |xi_i|<1, so this is within the bosonic coordinate domain. Padding zeros gives every dimension at least four, including all allowed even directed-bond dimensions there; dimension three already suffices algebraically. More generally psi=(a,a,-2a,0) gives a nonzero sum for every a>0. Thus the discrepancy persists in arbitrarily small neighborhoods as well as at order-one coordinates.

Consequently replacing the linear condition sum xi=0 by sum psi=0 is not an exact image of that change of variables. Having the same number of independent coordinates is insufficient to prove equality of the two constrained integrals. A different gauge slice might be valid after a corresponding zero-mode transformation and measure/Jacobian treatment, or the error might be asymptotically negligible. Neither possibility is disproved here. The exact missing implication is that this slice change, its measure, and its source factors alter the microscopic integral by o(1), uniformly on the integration domain. A one-copy spectral gap does not establish that implication.

The perfect-mixing Gaussian diagnostic makes the missing smallness assumption concrete. At P=J, the reduced covariance is I-J. A genuine auxiliary complex Gaussian with this covariance has E[N^(-1) sum_i |psi_i|²]=1-1/N. Hence a fixed maximal gap does not by itself make coordinate fluctuations o(1). This positive Gaussian is only a diagnostic for the quadratic size; it is not a replacement for the supersymmetric integral.

## 4. The repeated-index averaging check, and what can be proved instead

Put A=P-J and H=I-J. Define the reduced propagator

W_r = H(I-P+J)^(-r)H, r>=1.

Under max P_ij<=C/N and ||A||<=rho<1, elementary row/column estimates give

sum_j |A_ij|² <= (C-1)/N,
sum_i |A_ij|² <= (C-1)/N,
|(A^k)_ij| <= (C-1)rho^(k-2)/N for k>=2.

No eigenbasis or normality is needed. The binomial resolvent series consequently yields

|(W_r-I)_ij| <= K_r/N,
K_r = 1+rC+(C-1)[(1-rho)^(-r)-1-r rho]/rho².

For rho=0 the bracketed quotient has its continuous value r(r+1)/2; the bound remains valid. In particular W_1,ii=1+O(1/N), all off-diagonal entries are O(1/N), and both absolute row and column sums of W_r are <=1+K_r. For the actual family one may use rho=1/2 eventually. This supplies a uniform replacement for the source's approximate single-propagator entry estimates.

It also discriminates the pointwise use of its intermediate-projector averaging. In the exact maximally mixing case W=I-J, an n-edge product with every index equal is

(W_ii)^n=(1-1/N)^n.

Replacing each intermediate fixed coordinate projector by I/N instead gives

N^(-(n-1))(W^n)_ii = N^(-(n-1))(1-1/N).

Their ratio is exactly (N-1)^(n-1). Already n=2 has an order-one pointwise discrepancy. For the actual family, W_ii²=1+O(1/N), while N^(-1)(W_2)_ii=O(1/N), so the same failure is inherited from FM-021, not merely a toy example.

This rejects a uniform pointwise replacement over repeated ports. It does **not** reject an appropriately summed asymptotic claim, and it does not refute the source's universality prediction. The source presents this as heuristic averaging; the reason it cannot be imported is the absence of the summed error control required to absorb these exceptional assignments.

### Fixed connected propagator contractions, with all repeated labels

There is a safe elementary bound. Let G be any fixed connected oriented multigraph (loops and parallel edges allowed), with each edge e carrying W_(r_e). Then

sum_(x:V(G)->{1,...,N}) product_(e=(u,v)) |W_(r_e)(x_u,x_v)|
 <= N product_e (1+K_(r_e)).

Choose one spanning tree, bound non-tree edges by their supremum, and sum tree leaves using the absolute row/column bounds. The root costs N. This proof sums every label assignment, including arbitrary coincidences. After N^(-2) normalization it is O_G(N^(-1)).

This is the standard tree-summation mechanism already used in the repository's `mathematics/uniform_cluster_lemma.md` §5, now applied to a different covariance. It is not a new general diagram method, not a bound for diagrams with additional unsimplified U entries, not a proof that every nonzero supersymmetric contraction is connected, and not a bound on the sum over all graphs. K_r and the graph constant grow with complexity. The Taylor coefficients, diagram count, nonlinear domain and remainder still need their own control.

## 5. Why a literal graph embedding does not preserve the contract

For a simple graph let M=2B be the directed-bond dimension, and d_v each vertex degree. A column of its one-step bond-scattering matrix supported at vertex v has at most d_v nonzero entries and squared norm one. If every squared entry were <=C/M with an N-independent C, then d_v>=M/C for every vertex. Summing degrees gives M>=V M/C, hence V<=C. Simplicity gives B<=V(V-1)/2, so B is bounded. Thus no unbounded simple-graph family has this uniform dense scaling in its full directed-bond coordinates. On complete graphs with Fourier vertex scattering, M max|S_ij|²=V, displaying the mismatch explicitly.

This does not make the 2015 graph theorem empty: that theorem does not require this dense-entry bound. It shows why the later dense-matrix heuristic and the actual dense U_N require an arbitrary-unitary extension, rather than a literal simple-graph substitution.

The usual star-return construction also changes the gap. If the return map is V=D_theta U, its one-step dilation may be written

S = [[0,V],[I,0]],  |S|² = [[0,P],[I,0]].

The vector (1,-1) is an exact -1 eigenvector of the latter. Moreover Tr S^(2m)=2 Tr V^m and Tr S^(2m+1)=0. Taking a two-step return recovers V but does not inherit the cited one-step graph hypotheses. Dimension doubling, paired phases and period two must all be accounted for. No graph embedding is asserted to close the bridge.

## 6. First remaining analytic implication and plateau scope

The newly bounded W_r is the inverse of the **classical** reduced channel. The desired statistic is the full quantum phase integral. To transfer the formal method one needs an exact global coordinate/gauge representation plus a signed o(1) error estimate for its complete massive-mode contribution at microscopic spectral sources. This must include the nonlinear constraint change, all bosonic/noncompact regions and boundary terms, and all interaction orders. Pointwise convergence of every fixed diagram does not justify this interchange.

An equivalent concrete annealed target can reuse the project's prior Abel/compact-test bridge (the uniform bounds are valid for every unitary and can be averaged):

N^(-2) sum_(m>=1) exp(-2s m/N) B_N(m)
 -> (1-exp(-2s))/(4s²), for every s>0.

This includes the plateau through all m, without a short-time expansion. Alternatively one can prove the complete compact-weight target in §1 directly. The necessary negative correction above m/N=1 cannot be discarded: the cyclic contribution is asymptotic to m, while the total target is N. A finite small-time expansion supplies no nonperturbative plateau bound.

Even establishing this annealed assertion leaves N^(-2) sum w(m/N)R_N(m)->0 as a separate deterministic theorem. FM-022 removes a reverse-cyclic family; it supplies neither this full off-charge estimate nor the missing global annealed estimate. No full BGS or higher-order conclusion follows.

## 7. Executed checks, provenance and search boundary

`python3 checks.py > checks.json` passed with exact SymPy rational/algebraic arithmetic:

- nonlinear constraint mismatch in dimension 4;
- repeated-index projector ratio for N=3,4,5,7,19,101 and path lengths 2,3,5;
- exact star -1 mode for return dimensions 3,5,7,11;
- W_r identities and entry/row/column bounds at r=1,...,6 for one explicitly printed nonnormal bistochastic rational matrix;
- five fixed connected multigraph sums, with complete label enumeration and repetitions retained;
- complete-graph dense-scaling normalization controls.

The nonnormal matrix is a finite control for the elementary stochastic lemma, not the actual quantum map. These tests certify no asymptotic spectral claim.

Primary PDFs retained in `sources/` were authenticated by their arXiv version headers, with pdftotext extraction and hashes in `sources.json`. The unversioned 2005 download has **v1** in its header; it has been named accordingly, and no nonexistent v2 is used. Auto-generated printed document dates differ from the arXiv submission dates in some older PDFs; the arXiv version identifier governs this audit. Public sources only; no canonical source-cache modification.

Prior ownership was checked against current LOOP-001, `loop_test_reductions.md`, the earlier loop-transfer reports, the exact-method and signed-resummation reports, current massive-covariance/cluster arguments, and repository/source-audit searches for the 2018 identifier and title. The graph references and non-transfer warning were already known; the repository's earlier 2015 source check inspected abstract/bibliography only. No existing 1812.00655 exact-source audit was located in the searched Markdown corpus. Absence of a hit is not an originality theorem.

Searches covered primary-source versions of Tanner, Gnutzmann–Altland, Pluhař–Weidenmüller and the later massive-mode discussion; direct eigenphase/unitary-stochastic/random-diagonal-phase terminology; backward source links; and recent 2024–2026 quantum-graph universality searches through 6 October 2026. The recent mesoscopic paper was inspected as a distinct rigorous alternative. No exhaustive literature absence or global novelty claim is made.
