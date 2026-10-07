# Independent audit: growing-period three-gap counterexample

**Primary verdict: proved as written.** Every new claim and implication in the pinned growing-period companion is proved by this audit. The dimension-uniform Abel bound is imported from its separately accepted and source-matched independent review. No proof of that input is duplicated here. The recurrence, trace, reverse-kernel and charge-block algebraic assertions do not depend on it.

Audited source: `growing_period_counterexample.md`, SHA-256
`c5e2f39ba99145072a51bc10429978367a694294e666bcdda70125592990edf5`.

Imported Abel source: `inputs/18_uniform_abel_bound.md`, SHA-256
`ecd82a74edfabb89f6cbf46054d76c52dd41e5eb2d5a9790771b16a7c033da3f`.

Imported acceptance receipt: `/workspace/shared/bgs_compact_phase_bound_review/review_first_pair.md`, SHA-256
`fd2f0d76ff4326fb4a80e6c84bff69b264ee7b0665448105c59c8cd2128d27b1`. Its “Uniform Abel bound” verdict exactly identifies the author source hash above and accepts the all-N deterministic-unitary theorem. The review and its version-1 execution manifest were read and their hashes verified; the manifest validation passed with its explicitly reported legacy provenance limitations. The Abel part is a mathematical proof audit, not an extrapolation from those finite computations. Local frozen copies are `imported_abel_review.md` and `imported_abel_manifest.json`. The unrelated compact-projector result in the same receipt is not an input to this companion.

Prior fixed-period carry seal remains unchanged: `carry_review/review_v2.md`, SHA-256
`5d0cbaf1b444073c8b19f24e3024a9cc4670d450eb995e45e6f304f084b39c4a`.

This is a fresh derivation for A=[[1,2],[0,1]], not an inference that the fixed-period matrix's conclusion transfers without checking. The parent requested this continuation explicitly. All writes are confined to a separate subdirectory of the permitted review directory. No canonical BGS edits, publication, external agent communication, or further delegation took place.

## 1. Exact claim and dependencies

For p>=5 prime, p=2 modulo 3, let N=p², f(x+p y)=(x³,y³), and

    V(j,k)=p^-1 e_p(f(j)^T A f(k)),  A=[[1,2],[0,1]].

Claims checked:

- unitarity and |V(j,k)|²=1/N;
- exact period 2p;
- the complete even/odd trace table P3, including odd multiples of p;
- sup_(1<=m<2p)|Tr(V^m)/N|<=1/p and weak convergence of the normalized eigenphase measure to Haar;
- reverse-kernel norm 1/p;
- uniform contraction of every nonzero **cyclic Z/p²** charge block, with the same explicit squared bound as the fixed-period note;
- the implication from the pinned Abel theorem to a compact weighted balanced bound O_w(1);
- the return count (p/2)∫w+O_w(1), and therefore the high-Hamming/high-switch residual lower bound (p/2)∫w-O_w(1);
- the negligible damped endpoint and divergent signed marked-switch boundary integral.

Dependency graph:

1. Cube bijection + finite-field Fourier orthogonality → unitarity and row permutation V².
2. The explicit nilpotent matrix B with C=I+B → even traces and growing recurrence.
3. The correctly oriented odd-power diagonal quadratic → odd traces, exact order, and normalized short-trace bounds.
4. Invertibility of A-A^T → reverse norm.
5. Literal cyclic carry identity + the new α₂=2a₁+a₂ classification + elementary sum bounds → uniform charge contraction.
6. Imported Abel bound + positivity → compact weighted balanced O_w(1).
7. Positive return trace terms + weighted lattice Riemann sum − balanced bound → full off-charge divergence.
8. Previously pinned universal raw Hamming and whole-fiber low-switch identities → the exact residual.
9. Centered generating-transfer contraction + polynomial differentiation → damped endpoint and boundary divergence.

No actual-map theorem, fixed kick/cat factorization, spectral simplicity, or two-generator freeness is required or established. The supplied Abel source is the sole new imported analytic leaf.

## 2. Obligation matrix

| Obligation | Status | Evidence |
|---|---|---|
| New A and cube relabeling | Passed | Direct Fourier orthogonality, bijective common permutation. |
| Row/ket orientation | Passed | H² has row x, column Cx; odd diagonal uses A C^-k. |
| Nilpotence and exact recurrence | Passed | B²=0, B!=0, C order p; Tr(H^p)=p!=p². |
| Even trace table | Passed | rank(kB)=1 when p does not divide k. |
| Odd trace table, including p|m | Passed | Exact one-dimensional quadratic Gauss sum. |
| Growing uniform normalized window | Passed | Every nonreturn squared trace below 2p is at most p²=N. |
| Reverse norm | Passed | A-A^T=[[0,2],[-2,0]] invertible for odd p. |
| New carry coefficients | Passed | α=(a₁,2a₁+a₂), β=(b₁,2b₁+b₂). |
| p|c exceptional classification | Passed | 2x_l³+y_l³ constant; at most p, in fact at most 2 partners. |
| c₁=0,-1 and singleton branches | Passed | Underlying-polynomial classification retained. |
| Abel theorem itself | Passed as imported input | Pinned source matches the separately accepted independent review exactly. |
| Abel-to-compact-weight implication | Passed | Positivity and exponential comparison on the support. |
| Weighted return count | Passed | Lattice spacing 2/p; total-variation error O_w(1). |
| Exact residual and boundary | Passed | The accepted Abel theorem and independently verified universal mask/transfer inputs apply. |
| Actual BGS inference | Out of scope | Explicit changed quantization. |

## 3. Fresh recurrence and trace derivation

Let H(x,y)=p^-1 e_p(x^T A y) on F_p². Direct multiplication gives

    H²(x,y)=1_{y=Cx},
    C=-A^-1 A^T=[[3,2],[-2,-1]]=I+B,
    B=[[2,2],[-2,-2]].

Since p is odd, B has rank one and is nonzero; B²=0. Thus C^k=I+kB. Its order is exactly p. The corresponding matrix sends a function h(x) to h(Cx), and a ket labelled y to a ket labelled C^-1 y. The two orientations are not interchangeable.

For even powers m=2k, H^(2k) is the row permutation x↦C^k x. Its trace counts the fixed space:

    Tr H^(2k)=p²  if p|k,
                p   otherwise.

For odd m=2k+1, using H H^(2k), the diagonal is

    H^(2k+1)(x,x)=p^-1 e_p(x^T A C^-k x).

The exact matrix multiplication is

    A C^-k=[[1+2k,2+2k],[2k,1+2k]],
    x^T A C^-k x=(2k+1)(x₁+x₂)².

For each s=x₁+x₂ there are p ordered vectors x, cancelling the prefactor p^-1. Hence

    Tr H^m=Σ_(s in F_p)e_p(m s²),  m odd.

At p|m this trace is p exactly. Otherwise its squared modulus is p. This proves every branch of P3, with no omitted odd-multiple case.

H^(2p)=I follows from C^p=I. Since H² has exact order p, the order of H is either p or 2p. The just-proved value Tr H^p=p differs from N=p², excluding H^p=I and establishing exact order 2p.

For 1<=m<2p the squared trace is at most p². Therefore

    |Tr H^m|/N <= p/p²=1/p=N^-1/2.

For each fixed positive m this tends to zero; negative moments are conjugates. Every probability measure limit on the circle has the Haar Fourier coefficients, and trigonometric polynomial approximation proves convergence to Haar. This is a single-unitary macroscopic moment conclusion only.

## 4. Fresh cyclic-charge specialization

The new phase is

    f(j)^T A f(k)=x_j³x_k³+2x_j³y_k³+y_j³y_k³.

Its reverse-kernel skew matrix is A-A^T=[[0,2],[-2,0]], invertible modulo every admitted p. Orthogonality therefore gives ||Q||=1/p exactly.

Write c=c₀+p c₁ and retain the carry epsilon(x)=1_{x+c₀>=p}. The shift j+c is taken modulo p², not componentwise modulo p. For rows j,l the exact branch factorization uses

    α=(a₁,2a₁+a₂),  β=(b₁,2b₁+b₂),
    a=f(j)-f(l),  b=f(j+c)-f(l+c).

The u polynomial is unchanged in form. If c₀!=0, its algebraic constancy forces a₁=b₁=0 and therefore x_l=x_j. This same necessary condition applies to both carry branches, so their exceptional-set union has at most p elements.

If c₀=0 and c₁!=0, the complete v polynomial is constant only if α₂=β₂=0. In particular

    2x_l³+y_l³=2x_j³+y_j³.

For each y_l this determines one x_l, since 2 and the cube map are invertible. Thus the necessary count is at most p. The second equation sharpens it: subtracting the two relations gives

    3c₁(y_j-y_l)(y_j+y_l+c₁)=0.

There are at most two y_l and therefore at most two partners. This directly checks the troublesome p-divisible-charge case for the changed coefficient 2, rather than borrowing the old coefficient-1 equation.

When c₁=0 or -1, a branch can have zero v-displacement; the constant-polynomial criterion then becomes α₂=β₂. This does not affect the necessary u condition. Singleton u intervals are treated by completion even when their restricted values happen to be constant. They are not reclassified as algebraically constant.

The complete/incomplete bounds and p^-4 Gram normalization are unchanged. At most p exceptional partners have Gram magnitude <=p^-2. Every nonexceptional partner has magnitude <=2sqrt(2)(2+log p)p^-9/4. Schur's bound gives exactly

    ||B_c||²<=p^-1+2sqrt(2)(2+log p)p^-1/4

uniformly over all nonzero cyclic c. Its right side tends to zero. The zero-charge centered block vanishes because P=J.

## 5. Imported Abel bound: exact interface checked

The separate source theorem, in the exact needed notation, is

    B_N(m)=E_θ |Tr((Z_θW_N)^m)|²,
    N^-2 Σ_(m>=1)e^(-2sm/N)B_N(m) <= 1/(2s)+1/(2N)

for every deterministic unitary W_N and every s>0. This is the exact occupation-balanced quantity required here. No independence assumption is imposed on the entries of W_N; the torus variables implement the balanced projector.

Let w be bounded and supported in [a,b], with 0<a<=b<∞. Positivity of B_N(m) and

    |w(t)|<=||w||∞ e^(2sb)e^(-2st),   t in the support,

give

    N^-2 Σ_m |w(m/N)|B_N(m)
       <=||w||∞ e^(2sb)[1/(2s)+1/(2N)].

Choose any fixed s>0. The right side is O_w(1), independent of the growing period or p. This implication is fully checked and does not require a CUE limit, derivative convergence, normal-family identification, or phase-density estimate. The underlying Abel theorem is imported with its source hash and independent review, rather than reproduced or claimed as a new proof here.

## 6. Exact return count and signed residual

For m=2pr, the squared trace is N². Keeping just these nonnegative terms gives

    N^-2 Σ_m w(m/N)|Tr V^m|² >= Σ_(r>=1) w(2r/p).

The lattice spacing is h=2/p. A cellwise fundamental-theorem-of-calculus estimate yields

    |Σ_(r>=1)w(hr)-h^-1∫_0^∞w(t)dt| <= ∫_0^∞|w'(t)|dt.

Thus the lower bound is (p/2)∫w-O_w(1), with an explicit error independent of p. Subtracting the imported compact balanced bound leaves

    N^-2 Σ_m w(m/N)(|Tr V^m|²-B_N(m))
       >= (p/2)∫w-O_w(1).

Because w is nonzero and nonnegative, the integral is positive. Unlike the fixed-period argument, no restriction b<1/6 is needed.

The universal Hamming estimate from pinned input 11 is exactly zero for r=floor(.49m), since ||P-J||=0 and m-2r>0. Uniform charge contraction allows an arbitrarily small fixed rho eventually. For a given κ and a, choose -log rho>8κ/a. The exact whole-fiber torus subtraction and zero-run identities in pinned input 13, T10–T12, then remove the disjoint high-Hamming low-switch portion at exponentially small aggregate cost, including zero-checksum fibers. Therefore the literal residual has the same lower bound.

The swap (x,y)↦(y,x) conjugates amplitudes and preserves each mask; hence the signed aggregate is real, although no individual off-charge term is assumed positive.

For the damped endpoint, eventually rho<=1/2. Input 13, T8–T9, gives O(N² exp[-aN(1-z)/2]) after arbitrary Hamming extraction. At z_N=1-A_log log N/N with A_log>4/a this is o(1). Low-switch subtraction is uniformly exponentially small for 0<=z<=1. The exact finite-polynomial T15 identity therefore makes the integrated signed marked-switch boundary expression equal to the divergent undamped residual minus o(1).

## 7. Independent exact finite checks and provenance

`check_growing.cpp` was created separately from the earlier sealed fixed-period source. It directly constructs the new exponent from base-p digits and the term 2x_j³y_k³. The new α₂ and β₂ formulas and necessary p|c equations are explicitly changed and checked.

All mathematical checks use exact signed integer residues and exponent histograms over F_p; no floating-point Gauss sums, eigenvalues, or operator norms are used.

For p=5,11,17, respectively:

- all 600, 14,520, 83,232 nonzero-charge carry cases pass;
- all 15,000, 1,756,920, 24,054,048 charge/row-pair classifications pass;
- exceptional counts reach p, while the p|c maximum is 2;
- every unitarity, square-permutation, and reverse-kernel Gram histogram passes;
- direct repeated matrix multiplication checks C^k=I+kB for every 0<=k<2p;
- 10,22,34 even traces and the same number of odd traces are checked, covering 0<=m<4p and odd m=p,3p;
- odd trace quadratic exponent histograms and their Gauss squared-modulus histograms pass;
- the first full return is exactly m=2p and the normalized bound below it passes;
- exact direct-vs-factorized Gram histograms pass all 1,771,920 cases at p=5,11. This extra comparison is explicitly not run at p=17.

The deliberately incorrect row/ket convention disagrees at 40,220,544 square-matrix entries, respectively. A deliberately omitted carry fails immediately with exit status 2. These controls show that the test harness detects the principal convention and carry defects.

A version-2 execution manifest and scientific result are in `sealed_execution/`. The runner completed successfully under a 120-second wall cap, 90-second per-process CPU cap, 2 GiB address-space cap, and one-core affinity. Its manifest pins all input hashes before/after and was successfully validated against the project root. Full run time, compiler version, exact command and result hashes are retained there.

Finite success validates the implemented finite assertions; it does not establish a universal theorem or the imported Abel bound. The uniform conclusions come from the mathematical derivation above.

## 8. Boundary and remaining obligation

The new kernel, period, full trace table, vanishing normalized short-trace window, reverse norm, and cyclic-charge bound have no remaining gap. The implication from the supplied Abel theorem to the compact balanced bound and residual divergence is complete.

The independently finalized Abel review receipt has now been read, matched to the exact source hash, and admitted as an accepted input. The earlier conditional draft is retained separately as `review_conditional_draft.md`; it is superseded by this sealed report. There is no remaining mathematical gap or additional restriction for the growing-period companion in its stated changed-family scope.

The actual BGS signed comparison, fixed quantization, kick/cat freeness, and quantitative growing-word exclusions remain outside this counterexample. The strongest safe conclusion is that all three coarse gaps together with uniformly vanishing normalized traces on 1<=m<2sqrt(N), and hence every fixed normalized-power limit, still do not force the specified signed residual to vanish.
