# Independent audit: cyclic-carry counterexample, clarified v2

**Primary verdict: proved as written.** This verdict concerns the changed family with A=[[1,1],[0,1]], and the five assertions B1.1–B1.5 of the pinned v2. It is not an audit of a different matrix, a growing recurrence period, or the actual BGS quantization.

Reviewed source: `bilinear_carry_counterexample_v2.md`, SHA-256
`88408d0241a9346fd16b33117ff3779b8abccb740a3992aa29a631c59f8c49ab`.
The original source is preserved at SHA-256
`e80fc013cbe1a0070174e7941553740dc3c90fc1bf4903a1579d07a7aa86bcbd`.
Only the exceptional-set wording changes in v2. The changed lines now correctly require the two **underlying polynomials over F_p** to be constant, not their restrictions to a potentially singleton interval.

Audit performed on 7 October 2026 by a fresh independent worker. The exact kernel and cyclic-shift objects were reconstructed from definitions. No proposed author implementation was used. BGS instructions and relevant current status/convention sources were consulted. Canonical BGS was read-only throughout; its existing dirty worktree was not changed.

## 1. Normalized claim and dependency closure

For every prime p>=5 with p=2 modulo 3, put N=p² and j=x+p y, with x,y in {0,...,p-1}. Let f(j)=(x³,y³) over F_p and

    V(j,k)=p^-1 exp(2πi f(j)^T A f(k)/p),   A=[[1,1],[0,1]].

The assertions are:

1. V is flat and unitary, V^6=I, and P=|V|²=J.
2. Q(j,k)=V(j,k) conjugate(V(k,j)) has norm 1/p.
3. With every shift interpreted in Z/p², the diagonal charge blocks satisfy

       sup_(c!=0) ||B_c||² <= p^-1 + 2 sqrt(2)(2+log p) p^-1/4.

4. For every nonzero nonnegative smooth w supported in a positive band (a,b), b<1/6, and every fixed κ>0, the literal occupation-mismatched, Hamming>floor(.49m), switches>floor(κN/log N) signed N^-2 aggregate has lower bound

       N ∫ (1/6-t)w(t) dt + o(N).

5. Its value at z_N=1-A_log log N/N tends to zero when A_log>4/a, and the corresponding integrated signed marked-switch boundary expression therefore tends to +∞.

The dependency graph is:

- finite-field character orthogonality + cube bijection → unitary/flat recurrence and reverse norm;
- literal cyclic carry formula + elementary polynomial sums + algebraic exceptional count → uniform charge contraction;
- occupation-gradient/Parseval bound + recurrence + weighted Riemann sums → divergent full off-charge aggregate;
- universal raw off-charge Hamming estimate (pinned input 11, equation (3)) → low-Hamming contribution exactly zero;
- charge contraction + unitarity + exact occupation torus subtraction + switch counting (pinned input 13, T10–T12) → negligible low-switch part, even at zero checksum;
- the universal generating transfer (input 13, T8–T9) → negligible damped endpoint;
- the finite-polynomial fundamental theorem of calculus (input 13, T15) → divergent signed boundary integral.

All leaves are elementary internal arguments or the two inspected, pinned universal algebraic inputs. No Weil estimate, actual-map one-step gap, actual quantization, numerical norm approximation, or external theorem is needed for this changed-family conclusion. The infinitely many admissible primes can, if desired, be supplied by the elementary 3(product of all putative 2 mod 3 primes)-1 argument.

## 2. Obligation matrix

| Obligation | Status | Decisive reason |
|---|---|---|
| Cube bijection and permutation conjugation | Passed | gcd(3,p-1)=1; both kernel indices use the same bijection. |
| Row/ket orientation and recurrence | Passed | Row map C=-A^-1 A^T; ket map C^-1=-A^-T A; both have order 3. |
| P=J and reverse norm | Passed | Flatness; A-A^T is an invertible alternating 2×2 matrix. |
| Cyclic rather than vector-group charge shifts | Passed | Low-digit carry enters the high digit, with outer wrap modulo p. |
| Polynomial degrees and completion constant | Passed | A nonconstant difference is quadratic or cubic; completion remains valid for singleton intervals. |
| Exceptional union over both branches | Passed | A branch-independent necessary equation leaves ≤p row partners. |
| Charges divisible by p | Passed | α₂=β₂=0; in fact there are at most 2 partners. |
| c₁=0 and c₁=-1 | Passed | The zero-displacement v branch is allowed; the same u-polynomial condition bounds its partners. |
| Gram normalization and Schur bound | Passed | Gram scaling is p^-4; exceptional and nonexceptional row contributions have precisely the stated powers. |
| Balanced occupation bound B_m<=mN | Passed | Exact homogeneous polynomial, gradient Parseval, and unitary diagonal bound. |
| Signed lower bound and realness | Passed | Only squared traces and B_m are positive; the residual mask is conjugation symmetric. |
| Hamming and low-switch removals | Passed | Exact raw mask and whole-fiber torus subtraction; no invalid arbitrary-subset inference. |
| Damping and signed boundary | Passed | Centered pinching contraction is uniform under occupation twists; A_log>4/a suffices eventually. |
| Actual BGS conclusion | Out of scope | This is explicitly a changed unitary family with a six-step recurrence. |

## 3. Independent mathematical reconstruction

### 3.1 Row and ket conventions

Write H(x,y)=p^-1 e_p(x^T A y). Summing over the intermediate vector z gives

    H²(x,y)=1_{A^T x+A y=0}.

Thus the unique nonzero column in row x is Cx, where

    C=-A^-1 A^T=[[0,1],[-1,-1]].

Accordingly, the column-vector action is h(x)↦h(Cx), whereas a basis ket labelled y maps to the ket labelled C^-1 y. Direct multiplication gives C³=I. Consequently H^6=I and conjugation by f gives V^6=I. Treating the row and ket maps as equal would be false; the exact controls deliberately record disagreements with that mistaken orientation.

Similarly,

    Q(j,k)=p^-2 e_p(f(j)^T(A-A^T)f(k)).

The matrix p^-1 e_p(x^T(A-A^T)y) is unitary by character orthogonality, since A-A^T=[[0,1],[-1,0]] is invertible. Therefore ||Q||=1/p exactly.

### 3.2 Literal cyclic charge formula and exceptional classification

For c=c₀+p c₁, addition in Z/p² gives

    j+c = (x+c₀ mod p) + p(y+c₁+epsilon(x) mod p),
    epsilon(x)=1_{x+c₀>=p}.

For the Gram entry of rows j,l define a=f(j)-f(l), b=f(j+c)-f(l+c), α=A^T a and β=A^T b. Directly expanding the two kernels, without introducing a vector-group translation, yields the sum over carry branches of

    Σ_(u in I_e) e_p(α₁u³-β₁(u+c₀)³)
       · Σ_(v in F_p) e_p(α₂v³-β₂(v+c₁+e)³).

The Gram entry is p^-4 times this expression. This orientation and normalization agree with the direct cyclic matrix construction in the independent exact controls.

For F(t)=αt³-β(t+d)³, its nonconstant coefficients are

    t³: α-β;   t²: -3βd;   t: -3βd².

If d=0, it is constant iff α=β. If d!=0, it is constant iff α=β=0. There is no nonconstant linear case, because p!=3.

If c₀!=0, a formally constant u polynomial forces α₁=0, hence x_l=x_j by cube injectivity. This necessary condition does not depend on the column branch. Therefore taking a union over the two carry branches still gives at most p exceptional partners. This argument remains valid when c₁=0 or -1 makes one v-displacement zero.

If c₀=0, then c₁!=0 and there is one branch. A constant v polynomial forces

    x_l³+y_l³=x_j³+y_j³,
    x_l³+(y_l+c₁)³=x_j³+(y_j+c₁)³.

The first equation alone gives at most p partners. Subtraction gives the stronger relation

    3c₁(y_j-y_l)(y_j+y_l+c₁)=0,

so there are at most two possible y_l and one x_l for each. This independently resolves the important p|c case and shows that the proposed ≤p bound has ample slack there.

### 3.3 Completion and operator bound

For a quadratic polynomial with nonzero leading coefficient, shift differencing gives the exact complete-sum modulus sqrt(p). For a genuine cubic, each nonzero difference is a genuine quadratic, so

    |Σ_t e_p(F(t))|² <= p+(p-1)sqrt(p) <= 2p^(3/2).

Adding any linear character does not alter the leading coefficient. For a consecutive interval I, Fourier completion therefore costs at most the normalized Fourier l¹ norm of its indicator. The geometric-sum bound gives

    Σ_t |hat(1_I)(t)| <= p[1+H_((p-1)/2)] <= p(2+log p).

Thus every relevant nonconstant incomplete sum is at most sqrt(2)(2+log p)p^(3/4), even if I is a singleton. A formally nonexceptional row partner has such a nonconstant factor on each branch. Bounding the other factor by p and summing at most two branches gives the proposed 2sqrt(2)(2+log p)p^(7/4) bound for its unnormalized Gram sum.

At most p exceptional entries per row each have size at most p^-2. Every remaining entry has size at most 2sqrt(2)(2+log p)p^-9/4. The absolute row sum of the Hermitian Gram matrix is consequently at most

    p^-1+2sqrt(2)(2+log p)p^-1/4.

The spectral norm of that Gram matrix is bounded by this row sum, proving B1 uniformly in every nonzero cyclic charge. The right side tends to zero.

### 3.4 Exact balanced estimate and residual divergence

For any unitary W, let F(θ)=Tr((Z_θW)^m)=Σ_n c_n e^(i n·θ), with nonnegative integer n_j and Σn_j=m. Parseval gives

    Σ_j ||∂_jF||²₂ = Σ_n (Σ_j n_j²)|c_n|² >= m Σ_n |c_n|².

Cyclicity differentiates the actual product exactly:

    ∂_jF = i m ((Z_θW)^m)_(jj).

The sum of squared diagonal moduli of a unitary is at most N. Hence mB_m(W)<=m²N, proving B_m(W)<=mN with no restriction on repeated coordinates.

For V^6=I and w>=0, the full off-charge signed sum is |Tr V^m|²-B_m(V). Keeping the positive trace terms at 6|m and subtracting the upper bound for all B_m gives

    N^-2 Σ_m w(m/N)(|Tr V^m|²-B_m(V))
      >= Σ_(6|m)w(m/N) - N^-1 Σ_m m w(m/N)
      = N ∫(1/6-t)w(t)dt + o(N).

The coefficient is strictly positive because w is nonzero and supported below 1/6.

Pinned input 11, equation (3), bounds the literal off-charge Hamming ball by 2DMt^(m-2r). Here t=||P-J||=0 and m-2floor(.49m)>0, so this contribution is exactly zero. Only this universal off-charge part of the input is used; its Haar-tail and actual-model constants are irrelevant here.

The direct-sum centered charge pinching has norm sup_(c!=0)||B_c||, because its charge-zero centered block vanishes. Thus for any fixed γ>0 it is eventually <=rho=e^-γ. Occupation twists are unitary row phases and preserve these block norms. Orthogonality annihilates the constant vector at the boundaries of zero-charge runs, permitting exact P→P-J replacement. This gives the uniform complete-fiber bound N rho^(m-s(c)), and exact torus subtraction gives the occupation-mismatched fiber bound 2N rho^(m-s(c)). It is valid at zero checksum; no sign estimate on an arbitrary subset is being inferred.

For R=floor(κN/log N), input 13's elementary word count gives an exponentially small sum when γa>8κ. Hamming restriction is a restriction on the entire difference-word fiber, so the same bound applies to the disjoint high-Hamming, low-switch part. Removing this and the zero low-Hamming contribution preserves the lower bound above.

Every selected mask is invariant under swapping x and y. This swap conjugates amplitudes and preserves Hamming/switch counts, so the aggregate and its damping are real. No positivity of individual off-charge fibers or residual summands is needed.

Finally take rho<=1/2 eventually. The centered convex transfer has norm <=1-(1-rho)(1-z), uniformly in occupation and Hamming phases. The coefficient-extracted N^-2 compact-time bound is O(N² exp[-(1-rho)aN(1-z)]). At z=1-A_log log N/N, any A_log>4/a makes this o(1). Subtracting the already negligible low-switch portion gives o(1) for the same damped residual. Exact integration of its finite-polynomial derivative therefore yields the divergent undamped residual minus o(1), proving the claimed signed boundary divergence.

## 4. Original wording issue and why v2 fixes it

The original wording “both factors ... have constant phase on a branch” could be read as constancy after restriction to I_e. That broader reading is false. At p=5, c=21 (c₀=1,c₁=-1) and j=4, the singleton carry branch has **9** restricted-constant partners, larger than p=5. Exhaustive restricted-constancy maxima are 9,21,33 at p=5,11,17, respectively.

This does not contradict the operator estimate. A nonconstant polynomial restricted to a singleton still satisfies the incomplete-sum bound. The needed exceptional set is defined algebraically. The minimal v2 diff makes that definition explicit and leaves the kernel, estimate, and residual conclusion unchanged. No remaining restriction or mathematical correction is needed for v2.

## 5. Independent finite controls

The new `carry_review/check_carry.cpp` constructs exponents directly from j%p, j/p, and literal `(j+c)%N`. Its checks use exact integer residues and complete exponent histograms; there are no floating-point roots or numerical matrix norms. The source uses explicit throwing checks, rather than assertions removable by NDEBUG.

For p=5,11,17 it exhausts:

- cube bijectivity;
- every nonzero charge and every cyclic coordinate carry;
- every ordered row pair for exact unitary, square-permutation, and reverse-kernel Gram histograms;
- every nonzero charge and ordered row pair for complete-F_p polynomial constancy and the exceptional partner bound;
- both nonempty carry branches, including all p|c, c₁=0, and c₁=-1 cases.

For p=5,11 it additionally compares every Gram entry's exponent histogram from the direct cyclic charge kernel against independently convolved u/v phase histograms. This stronger equality is not required by cyclotomic reduction and is tested before evaluating any roots of unity. It is deliberately not run at p=17; the exclusion is explicit in the contract.

Results:

| p | Carry cases | Classified (c,j,l) triples | Exact Gram factorization triples | Max formal exceptional | Max when p|c |
|---|---:|---:|---:|---:|---:|
| 5 | 600 | 15,000 | 15,000 | 5 | 2 |
| 11 | 14,520 | 1,756,920 | 1,756,920 | 11 | 2 |
| 17 | 83,232 | 24,054,048 | Not run | 17 | 2 |

The c₁=0 and c₁=-1 subclasses reach p in every tested prime. The mistaken row/ket interchange is detected in 48,240,576 squared-matrix locations, respectively. A negative control that omits the low-digit carry fails at the exact cyclic carry identity with exit status 2.

The sealed runner output, version-2 manifest, hashes, compiler version, actual runtime and resource caps are in `carry_review/sealed_execution/`. Run reproduction is declared in `carry_review/contract.json` and `carry_review/run_controls.py`. Inputs are pinned before and after execution, including the v2 proof and both mask sources. Finite checks support the dictionaries and case coverage; the universal theorem is supplied by the mathematical argument, not by these finite successes.

## 6. Source and scope record

Pinned universal dependencies:

- `inputs/11_fractional_hamming_cancellation.md`, SHA-256 `10fd5b3e5d14d54c7d2b3ad2ace7b9d474a47f142b5a87e35fcf73b894ecaeb5`, only its exact raw off-charge estimate (3) and proof in Sections 3–5.
- `inputs/13_global_switch_transfer.md`, SHA-256 `4a333b1847eb466ef66326e26562ee63770f6e09ed7f47d7b517e5fbf5e6d0be`, its universal exact transfer, torus projector, zero-run argument, word count, and finite-polynomial boundary identity. Its introductory conditional status concerns an actual-map gap lemma; that gap is replaced here by the independently proved changed-family estimate.

The prior one-dimensional cubic witness is credited by the audited source, and is not re-audited or replaced here. No originality or global literature priority claim is made. No external literature is load-bearing.

Canonical BGS at the audit start reported HEAD `d37c92e563d10d25bb1d6ab85bedffc1f160f773` with substantial pre-existing tracked/untracked changes. This is not a clean-source certification or a canonical promotion. Only the permitted sibling review directory was written.

**Exact remaining gap for the audited claim:** none. The separate actual BGS signed Heisenberg comparison remains open. The strongest safe conclusion is that the conjunction of exact position mixing, vanishing reverse-kernel norm, and uniform one-step cyclic charge contraction cannot by itself force the specified high-Hamming/high-switch signed residual or its localized signed boundary integral to vanish. The explicit period-six changed quantization supplies the counterexample.
