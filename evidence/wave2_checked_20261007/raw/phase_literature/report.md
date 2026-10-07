# Phase-orbit universality transfer check for the next BGS wave

Checked 7 October 2026. Bounded primary-source pass, not a generic survey or a priority certification.

## Result that changes the next proof step

No checked source supplies a rigorous implication from the actual deterministic dense-unitary P-gap, reverse-Q decay and charge gaps to the complete signed hook covariance at Heisenberg degree. The closest exact ensemble formulation is Tanner's phase-torus ensemble, whose universality statement is explicitly a conjecture. The strongest directly usable convergence theorem is Bourgade–Huang's approximate-loop characterization, already conditionally registered in the checkpoint; its missing mixed-loop input is not implied by these gaps.

There is a useful narrow improvement to the quantum-graph route: the actual flatness plus operator-norm gap rigorously give the centered propagator entry estimates which Weidenmüller 2018 treated by typical-value approximations. A self-contained proof is below. Thus another next-wave proof of fixed-order Gaussian propagator size would not address the hard obstruction. The remaining task is to bound a boundary-completed, correctly centered, full signed nonlinear functional, or the exact phase-Ward overlap contraction, at microscopic absorption. Fixed-order diagram estimates alone cannot do this.

No repository claim status is changed. The inspected current literature qualification already imports no graph universality theorem as a load-bearing leaf. Direct registered Gaussian, matrix, Schur and ordinary-body coercivity results remain independent.

## 1. Exact transfer contract

Read-only input snapshot: /workspace/shared/bgs_checked_checkpoint_validation/source_snapshot; supplied manifest d6d5ade7444d9a2de43be89fd9636554404a275aa6703fa93910e55c1a1826ba.

The target is the unchanged odd-dimensional literal family, tau=10^-80, with V_N=D U_N and independent coordinate-uniform phases. The checkpoint records eventual max_ij |U_ij|^2 <=5/N, ||P_N-J_N|| <=1/2, reverse kernel Q_ij=U_ij conjugate(U_ji) with ||Q_N|| ->0, and the scoped nonzero-charge gaps. These are different kernels from eigenvector overlaps.

For hooks lambda_(m,k)=(m-k,1^k), the exact missing pair identification is

N^-2 sum_(m>=1) exp(-2sm/N) sum_(k,l)(-1)^(k+l)
  [ E_D s_lambda(m,k)(DU_N) conjugate(s_lambda(m,l)(DU_N)) - delta_kl ] ->0

for each fixed s>0. The Fourier degrees that contribute are m comparable to N, with an infinite Abel tail. Fixed-degree character identities, a fixed-flavor analytic source neighborhood and fixed-order regularity do not identify this limit. The particular mixed entry M_(m;0,1) is a discriminator, not a separately sufficient target.

The alternate exact phase-Ward contract is E_D R_(G-G^H) Psi_(N,s) ->0, where G_jk=sum_a |psi_j(a)|^2 |psi_k(a)|^2 and G^H_jk=(1+delta_jk)/(N+1). The Hessian and cotangent-gradient parts stay together. Psi has Heisenberg-scale content. It is not legitimate to substitute P or Q for G, or to infer the needed conditional overlap covariance from Haar eigenvectors without phase stationarity.

Project locators: mathematics/phase_trace_checkpoint.md; mathematics/phase_ward_identity.md, (12)–(15); evidence/research_checkpoint_20261007/raw/bgs_astra_corrected_integral/frontier/exact_identification_target.md, (I1)–(I4).

## 2. Closest quantum-graph sources and precise failures

### W18: conditional massive-mode argument, not a completed transfer theorem

H. A. Weidenmüller, Massive Modes for Quantum Graphs, [arXiv:1812.00655v1](https://arxiv.org/pdf/1812.00655v1), 3 December 2018; later 2020 book chapter. Exact inspected local PDF SHA-256: 51d115ced63d8e673c377b2886681dd5d7dcabdb5eca0566157c9b7499492f0d. Current arXiv history still lists only v1.

In §4.3, printed p.10, the source says: “Postponing a strict treatment to future work”. Equations (44)–(47), pp.11–12, use typical/average propagator and scattering-entry sizes. In §5, pp.14–15, its universality conclusion depends on validity of these approximations. §4.1, (33)–(35), also changes a centering constraint after a nonlinear variable transformation; counting the same number of variables is not the missing exact gauge/Jacobian argument. §4's expansion gives no uniform completed signed remainder at microscopic sources. This is independent of the previously reviewed color-one completion issue. It does not establish invalidity of every invariant superintegral prescription or falsity of graph universality.

Formal dictionary: source dimension 2B corresponds to matrix dimension N; source scattering map B corresponds to U_N; F=|B_ij|^2 corresponds to P_N; its complementary projector corresponds to Pi=I-J_N; its W is Pi(I-P_N+J_N)^-1 Pi. Source increments/source factors are of order B^-1, hence N^-1. Source spectral-gap condition |lambda_i(F)|<=1-a is weaker than the actual singular-norm gap. Actual entry flatness supplies an honest bound replacing its assumed typical |B_ij|=O(N^-1/2). These are formal matrix correspondences, not a literal graph realization: 2B is even, actual N is odd, and graph incidence structure is not supplied.

### PW15: all-correlation claim in a narrower graph setup

Z. Pluhař and H. A. Weidenmüller, Quantum Graphs and Random-Matrix Theory, [arXiv:1407.1148v2](https://arxiv.org/pdf/1407.1148v2), 9 March 2015, J. Phys. A 48 (2015), 275102. Inspected PDF SHA-256: ae8dab788be61436936a6cdc1cd6e4eabf22f547ff97c84a4deb8328bdd77159.

§6, printed pp.30–32, states the generating-function comparison for simple connected graphs with incommensurate bond lengths, fixed finite PF gap, unitary symmetry, and |sigma^(alpha)_(beta,beta) sigma^(beta)_(alpha,alpha)|<=b<1, excluding disconnected single-bond bound states. §4.3, pp.15–20, suppresses fixed terms of a massive-mode expansion; §6 explicitly limits its calculation to individual contributions. A graph's 2B directed-bond matrix and paired bond phases are not arbitrary dense odd-N DU. The proof does not supply the checkpoint's corrected color-one full-integral identification or a resummed signed error estimate for this model. No graph theorem is imported here.

### Tanner: exact phase ensemble, conjectural universal conclusion

Gregor Tanner, Unitary stochastic matrix ensembles and spectral statistics, [arXiv:nlin/0104014v1](https://arxiv.org/pdf/nlin/0104014v1), 6 April 2001, J. Phys. A 34, 8485–8500. §II.B, (8)–(11), pp.4–5, describes D_1 U_tilde D_2 with fixed moduli. Spectral observables reduce to N effective torus phases, matching DU after cyclic similarity. §III.B, (20), p.7, explicitly conjectures universality when its eigen-exponent gap decreases slower than N^-1; the text leaves the all-tau implication open. §IV.A, pp.9–10, numerically studies flat Fourier representatives and expects COE for symmetric U_tilde. The actual P/Q conditions match no proved all-Heisenberg conclusion in this source.

### Eigenvector Gaussian-wave criterion remains insufficient

Gnutzmann, Keating and Piotet, Eigenfunction Statistics on Quantum Graphs, [arXiv:1005.1026v1](https://arxiv.org/pdf/1005.1026v1), 6 May 2010. §7.1, (250)–(253), pp.50–51, uses truncated mean-field plus Gaussian corrections and labels full Gaussian-wave convergence conjectural. §7.2, pp.53–55, discusses regimes and approximation limits. Even an unconditioned fixed-order intensity law is not a theorem controlling the joint angle-overlap contraction in the phase Ward equation. It cannot replace E_D R_(G-G^H) Psi_(N,s).

### Finite color boundary remains mandatory, but is already handled for the pair

The inherited exact audit of Zirnbauer [2109.10272v1](https://arxiv.org/pdf/2109.10272v1), §2.4 (2.55)–(2.58) and Table 1/(4.29)/(4.36)–(4.40), is retained. Independent coordinate phases are separate color-one transforms; physical N is not the color count. The stable square-flavor inequality N_color>=2 n_0 does not apply at color one. The checkpoint's completed pair functional has its specified coherent-section domain, but is not a positive supermeasure or a higher-flavor completed CFT. W18/PW15 cannot be invoked to drop completion or move absolute values through all compact sectors.

## 3. An actual quantitative propagator bridge, proved here

This is an elementary inference from the stated actual hypotheses, not a theorem attributed to W18 and not a new registered asymptotic claim.

Let P be bistochastic, max_ij P_ij <= C/N and ||P-J||<=rho<1. Set A=P-J and Pi=I-J. Since each row/column sums to one,

||e_i^T A||_2^2 <=(C-1)/N,   ||A e_j||_2^2 <=(C-1)/N,
|A_ij|<=C/N.

For every k>=2, exactly A^k=A A^(k-2) A, hence

|(A^k)_ij| <= (C-1) rho^(k-2)/N.                         (P1)

The centered propagator is

W=Pi(I-P+J)^-1 Pi=Pi+sum_(k>=1)A^k.

Consequently

|W_ij-Pi_ij| <= [C+(C-1)/(1-rho)]/N.                    (P2)

More generally, for positive integer n,

W^n=Pi+sum_(k>=1) binom(n+k-1,k) A^k,

and

|(W^n)_ij-Pi_ij| <= K_n/N,
K_n=nC+(C-1)[(1-rho)^(-n)-1-nrho]/rho^2.                (P3)

At rho=0 the bracket quotient is interpreted continuously; in that case A=0 and the conclusion is immediate. For the actual eventual C=5,rho=1/2, K_n=16(2^n-1)-3n and K_1=13. In particular W_ii=1-1/N+O(N^-1), W_ij=O(N^-1) for i!=j, uniformly. This improves average-value guesses to rigorous entries, without eigenvector normality assumptions on P.

Limits: the constants in (P3) grow exponentially with n. Contraction multiplicities, nonlinear centering, compact boundary strata, microscopic source poles and the signed sum of all degrees remain uncontrolled. This propagator theorem does not assert that different summation indices never coincide, does not bound all diagram classes, and does not identify the hook covariance. Even a good fixed-n expansion cannot be interchanged with an infinite nonlinear expansion without a uniform remainder theorem.

Symmetry check: independent phases alone do not force CUE. If U is symmetric, DU is similar to the symmetric unitary D^(1/2) U D^(1/2); the phase-chart real-eigenvector reference is different. The actual reverse Q decay excludes the simplest diagonally gauge-symmetric reverse kernel, but does not evaluate the conditional G covariance. This matches the checkpoint's exact Ward diagnostics.

## 4. Strongest rigorous applicable theorem: conditional loop characterization

Bourgade and Huang, Loop Equations Characterize Random Matrix Statistics, [arXiv:2607.07617v2](https://arxiv.org/pdf/2607.07617v2), 9 September 2026, Theorem 1.9 and (1.4), printed p.6; proof §2.2 pp.13–15. Rational beta>0 is allowed, so beta=2 is covered. Particle-generated random Nevanlinna functions with L^q moments on events of probability 1-o(1) converge vaguely in law to Sine_beta if the full approximate bulk-loop hierarchy holds uniformly on each compact subset of the two half-planes, with residual o(1)(1+E R_N^(p+1)), for every fixed order p.

Dictionary: beta=2; s_N(w)=N^-1 sum_j cot((theta_j-alpha)/2-w/N); poles x_j=N(theta_j-alpha)/2 modulo periodic lifts pi N; each pole has unit mass; limiting intensity is 1/pi. Alpha can be absorbed into the uniform phase law. The supplied complex microscopic source bounds give moment regularity for this s_N, and the event can be the whole phase probability space. The missing premise is the approximate mixed-loop hierarchy itself. Same-half-plane holomorphic averaging does not test it. This is already the registered EXT-BH-2026 conditional leaf; it adds no transfer from P/Q/charge gaps.

For the pair alone the existing exact phase-Ward Poisson equation gives a smaller single-test target than this full hierarchy. If a next-wave prompt uses BH, it must ask for the model-specific signed mixed residual, not reprove normal-family compactness or the characterization theorem.

## 5. Maltsev–Osman 2026: exact scale and randomness mismatch

Anna Maltsev and Mohammed Osman, Mesoscopic Linear Statistics for Two Ensembles of Quantum Graphs, [arXiv:2607.02356v1](https://arxiv.org/pdf/2607.02356v1), 2 July 2026. Definitions 2.3/2.4 and Theorems 2.1/2.2, pp.4–5: Model 1 randomizes a fixed-d regular graph and independent compactly supported edge lengths, with symmetric equi-transmitting vertex matrices. Its variance error is O(eta^(1/2)+1/(N eta^3)); lambda exceeds c_mu sqrt(d-1). Model 2 fixes K_(N+1) but uses independent Haar U(N) vertex matrices; its error is O(eta^(1/2)+1/(N eta^2)+phi(N)), with bounded edge lengths and convergent Cesaro sums. Tests have compact Fourier support.

Model 1 therefore reaches eta>>N^-1/3, while microscopic scale is |E|^-1~N^-1. Model 2 reaches eta>>N^-1/2=|E|^-1/4, whereas microscopic scale is |E|^-1~N^-2. It proves variance, not full local point process/determinant ratios. Neither model is a deterministic dense scattering matrix plus the checkpoint's independent phases. No annealed-to-fixed-U concentration/de-randomization bridge is furnished. Its closed-walk/vertex-Haar contractions are useful as a comparison model, not an estimate of the actual signed hook block.

## 6. Minami-derived complex source bounds: attribution boundary

### Precisely known prior mechanism

Combes, Germinet and Klein, Generalized eigenvalue-counting estimates for the Anderson model, [arXiv:0804.3202v3](https://arxiv.org/pdf/0804.3202v3), 19 March 2009; J. Stat. Phys. 135, 201–216, DOI 10.1007/s10955-009-9731-3. Theorem 2.1/(2.7), p.3, and Theorem 2.3/(2.12)–(2.13), p.4, give nested-interval and all-order falling-factorial bounds by spectral averaging and rank-one resampling. The model is H_0+sum omega_j Pi_j, self-adjoint, with independent atomless single-site laws and concentration function Q_Lambda. No localization assumption is needed for these counting bounds. N corresponds to finite volume |Lambda|; the unitary phase coefficient |arc|/(2pi) must be proved separately.

### Adjacent genuinely unitary source

Mihai Stoiciu, The Statistical Distribution of the Zeros of Random Paraorthogonal Polynomials on the Unit Circle, [arXiv:math-ph/0412025v1](https://arxiv.org/pdf/math-ph/0412025v1), 9 December 2004. Theorem 6.3/(6.23), p.33, gives P(N_arc>=2)<=(b-a)^2/2 on arcs (theta_0+2pi a/N,theta_0+2pi b/N). Theorem 1.1 uses random disk Verblunsky coefficients and one independent uniform boundary coefficient. This is a CMV/paraorthogonal model, not arbitrary dense DU. Its p.18 conditional fractional Caratheodory bound, Lemma 3.9, has exponent in (0,1). It does not state the project’s full complex microscopic p>=2 package.

Hamza, Joye and Stolz, Dynamical Localization for Unitary Anderson Models, [arXiv:0903.0028v1](https://arxiv.org/pdf/0903.0028v1), 28 February 2009, Theorem 3.1/(3.5)–(3.6), p.8 and §4 pp.12–16, gives conditional two-phase resolvent-entry moments for exponent in (0,1). The stated model has band-structured deterministic S. The rank-two averaging algebra uses unitarity, but no literal dense-U theorem is imported without its finite-model adaptation. These fractional-entry bounds do not give all p>=2 normalized trace moments at absorption s/N or finite-flavor determinant-ratio uniform integrability.

### What is and is not supported as an originality statement

The accepted project adaptation proves universal connected/nested-arc factorial bounds for arbitrary finite DU, then centered arc-count moments, a complex Cauchy-kernel integration-by-parts estimate, and determinant log-increment bounds. Its precise conclusions are the O_sigma(p) L^p bound for the normalized complex trace, exponential moments, and a genuine fixed-flavor complex microscopic source neighborhood. The generalized-Minami factorial/resampling step is known machinery, properly credited. The later analytic packaging is not stated in the inspected CGK/Stoiciu/HJS results. No exact predecessor for the whole universal package was verified in this bounded pass, but this is not evidence of global novelty. Recommended wording: a self-contained unitary adaptation and analytic consequence of generalized-Minami resampling; priority of the precise source-bound package unverified.

Do not replace the imaginary Cauchy kernel by its absolute value before using centered counts; that introduces the logarithmic loss the project avoided. Do not infer a two-sided Poisson concentration theorem from one-sided factorial upper bounds. No counting/source bound identifies CUE: diagonal and cyclic U remain universal-bound controls.

## 7. Retained failed candidates and search boundary

- W18/PW15: source-exact conditional/nonlinear-completion and model-realization failures above.
- Tanner: closest exact phase ensemble, but explicitly conjectural universal step.
- GKP10: truncated Gaussian-wave criterion, no conditional microscopic angle-overlap theorem.
- Maltsev–Osman: random graph/Haar vertices, variance only, polynomial mesoscopic scales.
- CGK09/Stoiciu04/HJS09: counting or fractional-moment prior art; not local CUE transfer.
- Broad alphaXiv discovery returned deformed non-Hermitian/critical-edge and hard-edge Girko-ratio candidates, not this phase-orbit law; no applicability inferred. SciSpace broad discovery mostly returned invariant-ensemble/CUE characteristic-polynomial and Haar single-ring work. Neither index supplied an actual deterministic-DU transfer theorem.
- A title query for Poisson eigenvalue statistics for the unitary Anderson model resolved incorrectly to arXiv:2609.33084v1, a self-adjoint long-range Anderson paper. It was excluded rather than cited as the requested unitary result.
- New phase-randomized baker-walk hit 2609.32067 concerns refreshed phases each step and an accumulated unitary walk; it is not the static DU ensemble and was not used.

Two search strategies were used: exact primary-PDF candidate extraction plus local retained primary sources; and web/scientific-index searches across phase-orbit/unistochastic, random diagonal phases, quantum-graph massive modes, Ward overlap, unitary Minami, nested factorial counting, complex resolvent moments and determinant ratios. Date horizon: public indexed sources through 7 October 2026. Scholar Sidekick independently authenticated four records (W18/PW15/CGK/Stoiciu); this checks bibliography, not proofs. No exhaustive forward-citation closure, multilingual literature search or world-priority determination was performed. Failure to find a theorem is scoped to this pass.

Filtered primary-page extracts are retained privately beside this report with hashes in extraction_manifest.json. They are not PDF-byte caches or publication-ready redistribution. Existing W18/PW15 PDF hashes above refer to already retained primary PDFs outside the checked snapshot. No whole-repository edits or publication occurred.

## 8. Suggested narrow Work prompt

Use the unchanged actual family and the completed pair identity. Begin from either (a) the exact signed hook aggregate (I2) or (b) the exact absorbed phase-Ward contraction (13). Preserve complex sources and finite-color boundary completion. The ordinary centered propagator bounds (P1)–(P3) may be used as proved elementary consequences of actual flatness/P-gap, but they do not supply nonlinear gauge or sectorwise positivity. Seek an actual-model estimate of the complete signed covariance, including growth with Heisenberg degree and the Abel tail. A fixed-order Gaussian calculation, a body-only tail, unconditioned eigenvector moments, renewed source regularity, or graph-result transplantation is not the requested closure. If an asymptotic theorem requires an added overlap/loop/remainder hypothesis, state it explicitly and stop short of CUE identification.
