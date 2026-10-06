# Ordered Gaussian Weyl-pair gap: bounded literature check

Checked 6 October 2026. Target: `original_channel_gap.md`, based on BGS commit `fa007c498fe116a814a90aa3215cfd65b1f2a154`. This is an attribution/implication check, not another proof audit or an external referee report. The existing source note was read through GitHub at its pinned commit because its local copy was absent. No repository files were changed.

## Result

**No checked primary theorem immediately supplies the finite-time estimate for this noise law.** Closest overlap is alternating complete diagonal twirls in Fourier-related bases. Their scope already includes composite cyclic dimensions. The basic uncertainty/projection mechanism and Brownian moment formalism are established methods; the potentially distinctive contribution is the uniform low-positive-spectrum count for the particular two-Gaussian sinusoidal law, combined with the exact kernel angle to handle finite noise time. Classification of the checked comparisons: **partial or adjacent results only**. Priority of the exact channel estimate remains unverified; do not claim a first theorem worldwide.

The target is the Hilbert–Schmidt operator-norm estimate

`||exp(-u A_N) exp(-u B_N) Q_N|| <= 1 - (1-exp(-2u lambda_N))/50`,

where `lambda_N = [1024(1+log N)]^-2`, every odd `N >= 3`, `u >= 0`, and `Q_N` removes the identity and swap. Here `A_N = N²/2 sum_{j=1,2} ad(H_j^[2])²`, with `H_1=Re Z`, `H_2=Im Z`; `B_N` uses `Re X, Im X`. The norm is not diamond norm. The physical dimension is `N`, moment order is two, full operator-space dimension is `N^4`, and each total-Weyl block has dimension `N²`.

## Closest primary sources and dictionaries

### 1. Alternating diagonal twirls: most important antecedent

Y. Nakata, C. Hirche, M. Koashi, A. Winter, *Efficient unitary designs with nearly time-independent Hamiltonian dynamics*, PRX 7, 021006 (2017), [arXiv:1609.07021v3](https://arxiv.org/pdf/1609.07021v3), 24 April 2017. PDF pp. 4–5: Definition 7, Lemma 8, Theorem 9, Corollary 10; theorem and hypotheses inspected.

Theorem 9 assumes dimension `d = Omega(t²(t!)²)`, a Fourier-type pair, and **independent uniform phases at every basis vector** in each of three independent diagonal layers `D^E D^F D'^E`. Its moment contraction is `eta=[(1+t²)(t!)²+t²]/d + O(t^4(t!)²/d²)`. Map `d=N`, `t=2`, `E/F=Z/X eigenbases`; the leading bound is `24/N`. Lemma 8 covers cyclic Fourier bases, with no primality restriction. These are full phase-twirl projections. They are not `exp(-uA_N)` and `exp(-uB_N)`: the latter phases share only two Gaussian coefficients per layer. Thus neither the small-time dependence nor the needed quantitative comparison is supplied. **Adjacent, not a corollary for the specified finite Gaussian law.**

Earlier special case: Y. Nakata, C. Hirche, C. Morgan, A. Winter, *Unitary 2-designs from random X- and Z-diagonal unitaries*, [arXiv:1502.07514](https://arxiv.org/html/1502.07514), Theorem 4 and Definition 2 inspected in current primary HTML. It treats `d=2^n`, independent uniform diagonal phases, and `2ell+1` alternating layers, giving diamond error between `(2/d^ell)(1-1/(d-1))` and `(2/d^ell)(1+2/(d-1))`. Its Pauli-Hadamard qubit model is a further mismatch to odd cyclic dimensions. The 2017 theorem is the more relevant comparison. This earlier HTML was not version-pinned; no version-sensitive deduction depends on it.

### 2. Brownian Hamiltonians and moment generators

E. Onorati, O. Buerschaper, M. Kliesch, W. Brown, A. H. Werner, J. Eisert, *Mixing properties of stochastic quantum Hamiltonians*, CMP 355, 905–947 (2017), [arXiv:1606.01914v3](https://arxiv.org/pdf/1606.01914v3), 21 February 2017. PDF Theorem 9 (p. 8), Lemma 15 and (51)–(54) (pp. 15–16), and Section 5.1 inspected.

Lemma 15 identifies the moment semigroup `M_T^k=exp(TG^k)` using the mixed tensor representation. Dictionary: `k=2`, vectorized conjugation is `U^tensor2 tensor conjugate(U)^tensor2`; zero-drift covariance along the four project directions yields `G^2=-(A_N+B_N)` with matching variance normalization. This formalism is prior. Theorem 9 instead assumes the specified locally generated Brownian motion on complete or nearest-neighbor interaction graphs, with covariance over the full local Lie-algebra basis tied to the inverse Killing metric. Its Casimir gap argument does not apply to four selected global directions. Adding an unproved uniform comparison to that Casimir would merely relocate the project’s hard estimate. It also controls a continuous semigroup, not this one ordered finite-time product. **Adjacent.**

Caution: experimental arXiv HTML renumbers the same source's Lemma 15 as Lemma 3. Cite the pinned PDF numbering.

### 3. Uncertainty estimate: standard ingredient

D. L. Donoho, P. B. Stark, *Uncertainty Principles and Signal Recovery*, SIAM J. Appl. Math. 49 (1989), 906–931, DOI [10.1137/0149053](https://doi.org/10.1137/0149053); [author-hosted paper](https://web.stanford.edu/dept/statistics/cgi-bin/donoho/wp-content/uploads/2018/08/UPSR.pdf). The discrete concentration argument surrounding Theorem 3 uses the Frobenius/Hilbert–Schmidt estimate for time and frequency projections. Primary author-uploaded text and author-hosted source identified; not a full-paper audit.

Dictionary: ambient dimension is `D=N²`, not `N`; bases are the project's two partial-Fourier bases. Their cross-entry modulus is `D^-1/2=1/N`, giving `||EF|| <= ||EF||_HS = sqrt(rank E rank F)/N`. This identity is also directly checked by summing squared overlaps, requiring no imported theorem and no prime-dimensional assumption. **The overlap inequality is known after translation.** It supplies neither the model-specific eigenvalue count nor the exact-kernel separation. Claiming the MUB inequality itself as new would be incorrect.

### 4. Detectability/alternating-projection mechanism

A. Anshu, I. Arad, T. Vidick, *A simple proof of the detectability lemma and spectral gap amplification*, PRB 93, 205142 (2016), [primary text](https://arxiv.org/html/1602.01210), Lemma 2 and Corollary 3, current HTML inspected (published DOI [10.1103/PhysRevB.93.205142](https://doi.org/10.1103/PhysRevB.93.205142)). For projectors `Q_i`, `H=sum Q_i`, and at most `g` noncommuting neighbors per projector, the product of complements contracts the excited space by squared norm at most `1/(1+gamma/g²)` when `H` has gap `gamma`.

Dictionary: use two projectors `Q_1=I-Pi_A`, `Q_2=I-Pi_B`, `g=1`. This explains the standard projection-product/coercivity connection **after** the project proves a low-spectral angle. It does not establish that angle, and its factors are projections rather than finite-time heat contractions. The target's elementary three-line loss argument is a soft-contraction counterpart, not a novel general principle. **Adjacent; no stronger prior conclusion for the channel verified.**

### 5. Quantum hypocoercivity

D. Fang, J. Lu, Y. Tong, *Mixing Time of Open Quantum Systems via Hypocoercivity*, PRL 134, 140405 (2025), [arXiv:2404.11503v2](https://arxiv.org/html/2404.11503v2). Main-text Theorem 1 and Conditions 1–4 inspected. It treats `exp[t(Hcal+Dcal)]`, with symmetric dissipation, a positive microscopic gap off `ker Dcal`, skew-adjoint Hamiltonian stirring with a positive macroscopic gap, `P Hcal P=0`, and boundedness constants. It gives a prefactored exponential estimate with constants depending on those hypotheses.

Attempted dictionary: `Dcal=-A_N`, `P=P_A`. But `-B_N` is symmetric dissipative, not skew-adjoint stirring. Setting the Hamiltonian part to zero loses macroscopic coercivity on the large kernel. Moreover the target needs a one-step norm loss with prefactor one, not just eventual decay with a prefactor. A reformulation would require additional quantitative estimates and is not a direct theorem application. **Adjacent framework only.**

## Why the missing bridge matters

This is an independent comparison calculation from the target's own spectral formula. At `k=0`, the first nonaxis mode `y=eta=1` has

`E=8N² sin^4(pi/N) ~ 8pi^4/N²`.

Consequently `||exp(-uA_N)-P_A||` can be at least `exp(-O(u/N²))`. A triangle-inequality perturbation of complete twirls is therefore useless at `u=N^-alpha`. A full-twirl result cannot be converted into the desired finite-time estimate just by saying each Gaussian layer approximates its twirl. The candidate's point is to count the weakly damped modes and prevent their simultaneous concentration in the other basis, rather than demand that each layer mix uniformly on its own.

## Search scope and remaining uncertainty

Two discovery strategies were used: (i) alternating diagonal-design/Brownian/hypocoercivity citation families, including the earlier and later Nakata papers; (ii) the proof mechanism via Fourier concentration, low spectral projections, and detectability. Engines: web search plus Parallel Search; primary verification used arXiv, publisher/author sources. English queries included “alternating random diagonal unitaries approximate unitary 2 designs”, “Donoho Stark uncertainty principle norm projections Fourier sqrt cardinality”, “quantum hypocoercivity spectral gap”, “Brownian unitary designs spectral gap”, “Weyl two-copy gap”, “Gaussian sinusoidal phases unitary designs”, and “alternating dephasing quantum spectral gap”. Horizon: available literature through 6 October 2026. Parallel's exact-model search returned no useful candidate; that is not evidence of absence.

The previous project note's classical randomized-shear sources remain adjacent and were not re-audited, since they do not directly identify this finite quantum operator. No exhaustive MathSciNet/zbMATH search, full forward-citation audit, non-English search, or independent second literature reviewer was completed. The low-mode counting estimate was not found in the checked sources, but its global priority is **unverified**. Safe manuscript positioning: “We prove a quantitative finite-time bound for this specified four-Hamiltonian noise ensemble, using a standard uncertainty/projection method and an explicit uniform spectral count.” Avoid saying the overall design idea, Fourier alternation, composite-dimensional designs, or shared-noise moment semigroups are new.
