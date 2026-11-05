# Frontier, 4 November 2026

## Twelfth target: \(\gamma^*\) and the sum on one cross line

The eleven targets below are kept as records. The twelfth target is the missing per-line inequality \(|X_{\mathrm{line}}(d)|\le C\min(d, h_p/d)^{-\gamma}\). The proof note is `proofs/h5_xline.md`. The self-referee is `REFEREE_H5_XLINE.md`.

What that note establishes, inside this directory only:

- **[P-arith]** With \(C = 1\), the greedy divisor sum fits both idealised rooms for every \(\gamma\) at least \(0.873735223878\) in the absolute reading, and at least \(0.990856413416\) after multiplication by the gas surplus \(M\). Both thresholds bind at \(p = 3307\). The value \(\gamma = 1\) clears both readings. The value \(\gamma = 1/2\) clears neither tight room. This is not a bound on a line.
- **[P]** For every odd positive integer \(p\) and every \(d\mid h_p\), \(\varepsilon^{2p}\equiv 1\pmod d\) in \(\mathbb Z[\sqrt 2]\), and not \(-1\). For every odd prime \(p\), \(h_p\equiv 1\pmod{2p}\).
- **[P]** The sum of \(\hat Z\) over an ideal of squarefree norm \(h\) equals \(h\) times the sum of the kick weights of those words whose partial orbit lands in the conjugate ideal. The factor \(\min(d, h/d)^{-\gamma}\) does not appear. The group \(\langle\lambda,-1\rangle\) acts freely on the nonzero classes when \(h\mid h_p\) is squarefree.
- **[N]** In the N6 model at \(K = 16\), the cross-line moduli are \(7.958\cdot 10^{-6}\) at \(p = 11\), \(4.760\cdot 10^{-5}\) at \(p = 13\) and \(7.175\cdot 10^{-7}\) at \(p = 17\). Each product with \(\min(d, h/d)\) is below \(1\). There is no counterexample to \(\gamma = 1\) on this set. The pairwise log-log slopes are \(+1.45\) and \(-15.8\). Binet lines were summed at \(p = 11\) and \(13\) only. No line with \(p\ge 23\) was summed.
- **[P, finite]** `python-flint` 0.9.0 factors \(h_p\) for every odd prime \(p\le 199\). Each factorisation is squarefree, and every prime factor is \(1\pmod{2p}\). This is not H6.

\(\gamma^*\) is not achieved. H5(b) stays open. The composite branch of H5 is not discharged. `record/claims.json` was not edited.

## Eleventh target: the cross-line coefficient in H5(b) and H5(c)

The ten targets below are kept as records. The eleventh target is the per-line bound on the \(2^{\omega(h_p)}-2\) cross lines, and the same question for the partially isotropic points. The proof note is `proofs/h5_lines.md`. The self-referee is `REFEREE_H5_LINES.md`.

What that note establishes, inside this directory only:

- **[P]** In the normalisation of N6 §1, N10 and N11b §1, every fully isotropic point enters \(X\) with coefficient \(1\). A cross line is \(h_p-1\) such terms. TRACE-228 multiplies frequencies \(\beta = e\beta'\) with \(e>1\), and a cross-line point is not of that form.
- **[P]** For odd squarefree \(h\), a fully isotropic run of traces within \(1/16\) of \(\mathbb Z\) has length at most the bound \(\lambda^{k-1}\le (6432/25)\varepsilon^2 h\). At \(h = h_p\) this is \(k\le (p+1)/2\). The cap does not see a proper divisor. It is not TRACE-268.
- **[P]** One mixed class has \(\ell^1\) mass of \(Y\)-coefficients \(> (64/161)h_p > h_p/3\) when the non-isotropic prime is at least \(23\). The triangle majorant of one cross line, or of that class, fits either idealised room only if \(\max|\hat Z/Z| < 10^{-540}\) at \(p = 1409\) or \(< 10^{-1267}\) at \(p = 3307\).
- **[C] + [P-arith]** If \(|X_{\mathrm{line}}(d)|\le \min(d, h_p/d)^{-1}\), the greedy sum of primes \(\equiv \pm 1\pmod{2p}\) is \(< 0.00185728\) at \(p = 1409\) and \(< 0.00076450\) at \(p = 3307\). Both lie under the rooms \(0.02011297\) and \(0.00334719\), and so do the products with the gas surplus \(M\). The elementary floors fit absolutely and miss both rooms after multiplication by \(M\). The hypothesis is not proved.

H5(b) and H5(c) are not discharged. The composite branch of H5 is not discharged. The structural ceiling of v5 does not fall. `record/claims.json` was not edited.

## Tenth target: H5 after Lemma W, with H8 parked

The nine targets below are kept as records. H8 is parked in `proofs/h8_park.md`. The self-referee is `REFEREE_H8_PARK.md`. The four routes — the uniform factor of exponent \(1\), the additive energy \(2L^2-L\), the lifted window energies, and the BGK/HBK ranges — leave the amplified wrap at \(\theta < 0.16661157\). The interval up to \(0.26223963\) stays open. H8 is not discharged and not refuted.

The tenth target is the factorisation clause of H5 (BGS-TRACE-303), given Lemma W (BGS-TRACE-342, proved on `main`). The proof note is `proofs/h5_factor.md`. The self-referee is `REFEREE_H5_FACTOR.md`.

What that note establishes, inside this directory only:

- **[P, cited TRACE-342]** For every odd prime \(p\), \(\omega(h_p) \le w_{\max}(p) < p/\ln(p-1)\). At the conditional primes, \(w_{\max}(1409) = 112\) and \(w_{\max}(3307) = 231\).
- **[P]** \(2^{112} > 2e^{1409 R}\) and \(2^{231} > 2e^{3307 R}\), with \(R = 6.234\cdot 10^{-4}\). The same comparison, with coefficient \(1/6\), holds for every integer from \(2000\) to \(e^{170}\). The Lemma W count exceeds the gas main term on that range.
- **[P-arith]** Under the idealisation \(n/h_p := 1\), the room for \(|X_{\mathrm{cross}}|\) is \(< 0.00334719\) at \(p = 3307\), \(\delta = 3.4962\cdot 10^{-4}\), and \(< 0.02011297\) at \(p = 1409\), \(\delta = 7.4115\cdot 10^{-6}\).
- **[P]** \(h_p > (2p-1)(397/250)^p\) at \(p \in \{31, 1409, 3307\}\). The cofactor allowed by \(q_{\min} = 2p-1\) has \(\theta > 0.496\) at both conditional primes, above the sketch cutoff \(1.588^p\).

H5 is not replaced. Infinitude of \(\{h_p \text{ prime}\}\) remains equivalent to the failure of \(R_{\mathrm{NSW}}\) (BGS-TRACE-210). No positive-density theorem is proved. Squarefreeness stays H6. `record/claims.json` was not edited.

## Ninth target: window energies by lifting to \(\mathbb Z[\sqrt 2]\)

The eight targets below are kept as records. The ninth target is the open interval of amplified H8, attacked by higher energies of short windows. The proof note is `proofs/h8_moments.md`. The self-referee is `REFEREE_H8_MOMENTS.md`.

What that note establishes, inside this directory only:

- **[P]** A congruence of two \(k\)-sums of powers of \(\lambda\), with exponents in an interval of span \(l\), is an equality in \(\mathbb Z[\sqrt 2]\) whenever \(4k^2\lambda^l < d^2\). The span is \(l < 2\log_\lambda d - \log_\lambda(4k^2)\). The length \(\ln d/(2\ln\lambda)\) contains \(\ell_0 = p/4\) only for \(\theta \ge 1/2\). The proved length contains \(\ell_0 = p/4\) throughout \(\theta \ge 0.16661157\), for \(k \le 7\) at \(p \in \{1409, 3307\}\).
- **[P]** An equality of two \(k\)-sums in \(\mathbb Z[\sqrt 2]\) with \(k \le 6\) is a permutation of the summands. The ordered energy of a liftable window is then at most \(k!\,|W|^k\). The first non-permutation has mass \(7\), and it is \(\lambda^4+6\lambda = 6\lambda^3+1\) up to translation and swapping sides. The single-digit word of \(\lambda^n\) is Lemmas 3 and 4 of `proofs/span_law.md`.
- **[CA]** The \(2k\)-moment beats \(|S| \le |W|\) only for \(\theta < 0.00576146\) at \(p = 1409\), \(k = 6\), and for \(\theta < 0.00289289\) at \(p = 3307\). The amplified exponent stays \(1\), so the wrap remains \(\theta < 0.16661157\). The formal product of the weight \(d\) with the energy ratio, which is not a theorem, reaches at most \(\theta < 0.17973708\) at \(p = 1409\) and \(\theta < 0.17322030\) at \(p = 3307\). Covering \(0.26223963\) would require an exponent under \(0.63534092\). The formal exponent stays above \(0.92122088\).

H8 is not discharged. The full orbit of length \(p\) or \(3p\) does not fit in the liftable span. `record/claims.json` was not edited.

## Eighth target: the additive energy of \(\langle\lambda\rangle\)

The seven targets below are kept as records. The eighth target is the amplified normalisation of H8 at large \(p\). The aggregate comparisons at \(p = 19\) and \(p = 29\) are parked: both primes lie under the conditional thresholds \(1409\) and \(3307\), so they are not an input the large-\(p\) inequality reads. H7* stays a hypothesis of v5. The proof note is `proofs/h8_energy.md`. The self-referee is `REFEREE_H8_ENERGY.md`.

What that note establishes, inside this directory only:

- **[P]** For a split prime the additive energy of the graph of \(\langle\lambda\rangle\) equals \(2L^2-L\) when the order \(L\) is odd, and \(3L^2-3L\) when \(L\) is even. The odd uniqueness is BGS-TRACE-279; the count is written here. For an odd modulus that has a split prime factor of the same order, the energy is at most \(2L^2-L\). The bound does not depend on the modulus and has no cap at \(\sqrt{h_{3p}}\). The ratio to the trivial energy \(L^3\) is \(< 2/L\).
- **[P]** Bourgain–Glibichuk–Konyagin needs a fixed \(\delta > 0\) with \(|\langle\lambda\rangle| \ge q^\delta\). At the bottom of the gap, \(\delta_{\max}(1409) < 0.02017629\) and \(\delta_{\max}(3307) < 0.00947485\). Heath-Brown–Konyagin applies to the projection throughout the gap at these primes and gives the weaker shape \(L^{5/2}\). Its character-sum form stays above the trivial bound on \(\theta \ge 0.16661157\).
- **[CA]** The \((2,2)\) bound of TRACE-279 beats \(|S| \le L\) only for \(\theta < \ln(L^2/2)/(p\ln\lambda)\). At \(L = 3p\) this is \(< 0.00644413\) for \(p = 1409\) and \(< 0.00303834\) for \(p = 3307\), inside the exponent-\(1\) range. The amplified wrap remains \(\theta < 0.16661157\). The interval up to \(0.26223963\) stays open.

H8 is not discharged. The integers \(49\) and \(343\) have energies \(1617\) and \(122451\), above \(2L^2-L\), because the order grows. `record/claims.json` was not edited.

## Seventh target: the averaged operator for the section aggregate

The six targets below are kept as records. The seventh target is to move \(\sum_\beta\kappa_d(N\beta)\operatorname{Tr} Q_\beta\) inside one operator, using the product formula for \(\kappa_d\) and the character dependence on \(\beta\), and to bound the trace or the spectral radius of that operator at \(d=3437426497\). The proof note is `proofs/h7_average.md`. The self-referee is `REFEREE_H7_AVERAGE.md`.

What that note establishes, inside this directory only:

- **[P]** The sum over all residue classes, including zero, is \(\operatorname{Tr}(MT^P)\) on the section tensored with \(\mathcal O/d\mathcal O\). The Lin sum removes the identity class. The weighted norm of \(T\) is the maximum of \(\|L(k/d)\|_s\), hence at most \(246/100\). The spectral radius of \(T\) lies between the untwisted spectral radius and that norm. The Gauss transform of \(\kappa_q\) is \(q(q-2)\) on \(N=0\) and \(-q(1+e(-t_b N/q))\) off it, for \(q\equiv 1\pmod 8\). It factors across the two primes, and the trace does not.
- **[CA]** The Cauchy–Schwarz majorant is \(7.420040412990621\cdot 10^{48}\), a factor \(1.9142415283101287\cdot 10^{21}\) above the threshold. The Koopman majorant is a factor \(5.608476978097026\cdot 10^{25}\) above the threshold. Both are coarser than the triangle bound of the sixth target. The constant Gauss piece \(d\lvert\operatorname{Tr} Q_0\rvert\) lies under the threshold by \(91.71481675130566\), and the identity-class term by \(92.11798329681781\). A uniform trace cap of \(30788816.98609009\) would put the residue triangle on the threshold.
- **[N]** A scalar model at \(17\cdot 41\) has \(S(d)/(S(17)S(41))\) of modulus \(6.05155913001261\), not \(1\). At the prime \(457\), sector \(0\), a binary64 pass over all \(3665\) orbits puts the twisted remainder at modulus \(64.36874328884288\), against an identity term of modulus \(5.594329091312814\cdot 10^{18}\). The scan's Frobenius column reaches \(10^{47}\) and does not enclose the traces. The remainder does not transfer to the composite.

Aggregate H7* is not shown to hold and not shown to fail. The operator is an operator on the finite section, not on \(\hat Z\). `record/claims.json` was not edited.

## Sixth target: a uniform bound on the section trace

The five targets below are kept as records. The sixth target is a bound \(|\operatorname{Tr} Q|\le C R^P\) for every twist of the finite multi-disc section, with \(R\) below the Frobenius majorant \(M\approx 50.49\), and the comparison of that bound with the \(\eta=1\) threshold at \(d=3437426497\). The proof note is `proofs/h7_uniform.md`. The self-referee is `REFEREE_H7_UNIFORM.md`.

What that note establishes, inside this directory only:

- **[P]** In the weighted norm named by the diagonal in `logs/h7_uniform_weights.json`, a submultiplicative bound on one step is a bound on every twist sequence, sectors included. The residue weight \(\sum_{\beta\not\equiv 0}|\kappa_d(N\beta)|\) factors as a product of local representation sums. For odd \(q\), \(\sum_{k=1}^{q-1}|\cos(\pi k/q)|=\csc(\pi/(2q))-1\).
- **[CA]** Every twisted step has weighted \(2\)-norm at most \(246/100\). The trace of a length-\(P\) product is at most \(280\cdot(246/100)^P\). One eigenvalue of the untwisted step has modulus in \([1.9154732041332492,\ 1.915473204133273]\). The residue weight at \(d=457\cdot 7521721\) is \(1.2589733434762453\cdot 10^{20}\). The section majorant is \(6.768238765003160\cdot 10^{44}\). Against the threshold \(3.8762299862656054\cdot 10^{27}\) the quotient is \(1.7460880259903623\cdot 10^{17}\).
- **[CA]** The rate that would put this triangle bound at the threshold is \(R_*=1.225865206681737\). The certified rate is larger by the factor \(2.006745918386011\). The untwisted section trace alone, times the residue weight, already exceeds the threshold by \(3.9934073393176425\cdot 10^{8}\). No uniform cap can do better than that trace, and \(R_*\) lies below the spectral radius.

Aggregate H7* is not shown to hold and not shown to fail. The bound is a bound on the finite section, not on \(\hat Z\). `record/claims.json` was not edited.

## Fifth target: the aggregate Lin sum at the three crossings

The four targets below are kept as records. The fifth target is the sum \(\sum_{\beta\not\equiv 0}\kappa_d(N\beta)\hat Z(\beta)\) at the three included conductors, compared with \(\varepsilon_d|Z|^2/h_p\). The proof note is `proofs/h7_lin.md`. The scoping sentence is `proofs/h7_scope.md`. The self-referee is `REFEREE_H7_LIN.md`.

What that note establishes, inside this directory only:

- **[P]** For a squarefree product of primes \(q\parallel h_m\), \(\kappa_d\) is the product of the local missing-label sums, with the missing label shifted by the cofactor. The J3-F5 splitting (TRACE-228) applies to the finite-section traces. The exact-conductor term has coefficient \(1\). The conductor-\(457\) term inside \(d=457\cdot 7521721\) has coefficient \(<1.33\cdot 10^{-7}\).
- **[CA]** \(|\kappa|\) on the three crossing frequencies is \(0.20028229612862064\), \(0.352776706753451\) and \(0.8773654889389776\). The sector-\(0\) section trace of each crossing orbit, multiplied by \(\kappa\) and by the orbit length, is \(2.54\cdot 10^{10}\), \(3.45\cdot 10^{11}\) and \(2.54\cdot 10^{16}\). Against the section's own untwisted trace, the three one-orbit shares of \(\eta\) are \(<3.28\cdot 10^{-18}\), \(<9.08\cdot 10^{-19}\) and \(<1.19\cdot 10^{-28}\). Sector \(4\) does not move these digits.
- **[CA]** At the prime \(457\), the complete isotropic part of the section sum has modulus \(7.8450076177326356\) in sector \(0\) and \(39.619988072063016\) in sector \(4\). Against the period-\(57\) untwisted trace, those shares are \(<5.73\cdot 10^{-14}\) and \(<2.90\cdot 10^{-13}\). Carried into the composite by the factor above, they contribute \(<4.61\cdot 10^{-20}\) to \(\eta\).
- **Not enclosed.** The sum over all \(\beta\) at any of the three conductors. A Frobenius bound \(M\le 50.490459330663754\) on one step gives \(M^{57}>10^{90}\), which does not decide \(\varepsilon_d\). The off-isotropic frequencies at \(457\), and the exact-conductor term at each composite, are open.

Aggregate H7* is not shown to hold at these levels, and it is not shown to fail. The sufficient per-orbit reading fails on the finite section at the three included levels, both with \(p<1409\), so Theorem v5 does not fire and H7* stays a hypothesis at \(p\ge p_{\mathrm{thr}}\). `record/claims.json` was not edited.

## Fourth target: the three crossings on the multi-disc operator

The span law, the H7*/H8 obstruction, and the single-disc Galerkin rates below are kept as records. The fourth target is whether those three Galerkin crossings are eigenvalues of the multi-disc vertex operator of TRACE-223. The proof note is `proofs/h7_multidisc.md`. The self-referee is `REFEREE_H7_MULTIDISC.md`.

What that note establishes, inside this directory only:

- **[P, arithmetic]** The three conductors divide \(K_p\), sit at or under \(\sqrt{h_m}\), and are not \(h_p\) or \(e\cdot h_p\). The primes are \(p = 19\), \(p = 19\) and \(p = 29\). TRACE-273, cited, includes them for \(\rho = (\pm 2, 8)\) at odd \(m\ge 15\). The TRACE-199 shape with constant \(3012.4\) was checked in arb at these three pairs and gives \(|Z|^2 > 4mh_m\).
- **[CA]** The finite section with centres \(|c|\le 3\), modes of degree \(< 40\) and letters \(|n|\le 16\), dimension \(280\), has certified per-step rates \(1.458772466390154\), \(1.5119805975188876\) and \(1.4686852948918232\), all above \(T' = 1.42785\). Level \(7\), class \((2,1)\), sector \(4\), falls inside the TRACE-223 disc. Class \((1,3)\), sector \(6\), falls under the cap \(1.2837144\).
- **[P]** One step of the difference between this section and the core operator on the same centres is \(< 9.65\cdot 10^{-5}\) in operator norm, and the core is forward-invariant for the kept letters. The product of \(57\) or \(87\) such steps is not bounded by a useful multiple of that constant. The untruncated monodromy is not claimed to lie above \(T'\).

H7* as the aggregate Lin bound is not shown false. The sufficient reading “every orbit grows slower than \(T'\)” is false for this finite section, at three included levels, both below \(p_{\mathrm{thr}}\). The re-scoping that survives is the aggregate with the sum over \(\beta\) kept. `record/claims.json` was not edited.

## Third target: H7* rates on the included levels

The span law and the H7*/H8 obstruction below are kept as records. The third target is the per-step sector rate on the included \(K_p\)-divisors other than \(7\), against \(T' = 1.42785\). The proof note is `proofs/h7_rates.md`. The self-referee is `REFEREE_H7_RATES.md`.

What that note establishes, inside this directory only, and only for the single-disc Galerkin model that reproduces the three TRACE-223 discs at level \(7\):

- **[CA]** At \(d = 31\), every nonzero class and every sector has rate at most \(1.0923934786042258\).
- **[CA]** At \(d = 49\) and \(d = 217\), every nonzero class in the surviving sectors \(a\in\{0,4\}\) has rate at most \(1.2876123688383678\) and \(1.2892227802420704\) respectively. Both maxima sit on the level-\(7\) survivor, copied by the phase identity.
- **[CA]** Three included conductors have a surviving-sector orbit above \(T'\): \(1.4587724665845072\) at \(d = 3437426497\), \(\beta = (-208,0)\); \(1.5119805994002586\) at \(d = 24061985479\), \(\beta = (227,227)\); \(1.4686852970394264\) at \(d = 2735635252619983\), \(\beta = (-89,0)\). Sector \(0\) is a surviving sector, so the cancellation on sectors \(2\) and \(6\) does not remove them.
- **[P]** No uniform majorant under \(T'\) falls out of \(d\equiv 1\pmod 3\). The untwisted step exceeds \(T'\), inheritance covers only a sublattice, the period is \(3p\), and the length bound \(\log_\lambda d < 3p/4 - 1/6\) does not control the spectral radius. The third crossing lies above \(\sqrt{\mu^*_{\mathrm{model}}}\).

H7* stays open. The seventeen conductors that were only searched along rays are not certified under \(T'\). The model is not the multi-disc operator of TRACE-223. `record/claims.json` was not edited.

Independent note on the open inputs of Theorem R♯-mod v5 (BGS-TRACE-325). The claim registry, `README`, and the hash-pinned sources are unchanged. Status tags in this directory are local to the note: **[P]** proved here, **[P-sketch]** a written argument with a named gap, **[N]** a numerical observation, **[C]** a conjecture. A finite computation is not an asymptotic theorem.

`evidence/breakthrough/` is about the Δ → 0, JBL, Lemma U, and Gap G package. It does not speak to H1 or H3. The governing statement of v5 is `computations/verification/lineN_theorem_draft/THEOREM_DRAFT_v5.md`, with the N20 re-scoping in `evidence/executions/20261101/lineNgas/N20/REPORT_N20_v2.md`.

## Second target: H7* and H8

The span law below is kept as a record of the first target. The second target is H7* (BGS-TRACE-305) and H8 (BGS-TRACE-306). The proof note is `proofs/h7_h8.md`. The self-referee is `REFEREE_H7H8.md`.

What that note proves, inside this directory only:

- **[P]** \(7 \mid K_p\) and \(7 \nmid h_p\) for every prime \(p \ge 5\), by the recurrence modulo \(7\). TRACE-265 had checked the finite range \(p = 5,\ldots,23\). Level \(7\) stays the covered level (TRACE-223). The identity \(h_{3p} = h_p K_p\) is re-proved from the closed form; the rank-\(3p\) statement is cited.
- **[P]** Every prime factor of \(K_p\) is congruent to \(1\) modulo \(3\). This is weaker than N8b’s congruence modulo \(6p\), which is cited and not re-proved.
- **[P, finite]** Complete trial-proved factorisations of \(K_p\) for \(5 \le p \le 31\). On the NSW primes \(p = 5, 7, 19, 29\), H7* inside the inclusion range \(d \le \sqrt{h_m}\) still contains \(K_p\)-divisors other than \(7\). At \(p = 7\) that list contains the prime power \(49\). At \(p = 5\), \(31^2\) divides \(K_5\) and sits above \(\sqrt{h_{15}}\).
- **[P]** A close return at the weakest \(\varepsilon\) allowed by Lemma E (TRACE-268) is shorter than the \(3p\)-factor trace by more than \(p + 7/4\), on every level \(d \le \sqrt{h_m}\). This blocks using one close return as a smallness certificate for the whole product. It does not determine the sign of \(\mathrm{Dev}_d\).
- **[P, arithmetic]** Substituting the caps \(\Lambda \le 1.9656353\) and \(r_2 \le 1.0529012\) produces \(c_{\mathrm{del}} \approx 0.73753152\), and \(\tfrac32 c_{\mathrm{del}} > 1.106\). At \(\ell_0 = p/4\) and \(\bar\rho \le 0.28\), the amplified wrap covers \(\theta < 0.16662\), while the substituted first-moment range still reaches \(\theta > 0.26224\). Covering every divisor forces \(\ell_0/p > 0.75025\). Inserting \(c_{\mathrm{del}}\) as the wrap exponent leaves a length \(\approx 0.55333\, p\).

H7* and H8 stay open. The floor comparison is conditional on an upper shape \(e^{0.05 p}\) for the positive term. The wrap obstruction is the amplified-weight case (N16b (c2)). Unit weights reduce H8 to H1, which this note does not attack. Lemma 2 of N14b stays a sketch.

## What the register already separates

Frozen R′ (BGS-TRACE-206) is open. It is the conjecture W′_m = o(m) for the k₁ kick 0.9 cos(2πq) at η = 2, odd m. Nothing below refutes it or proves it.

Theorem R♯-mod v5 is conditional. If H0, H1, H5–H8 hold and B_p ≥ κ > 0 for infinitely many primes p at least the threshold, then W′_{3p}/m → ∞ and frozen R′ fails along m = 3p. H2 and H4 are met. H3 follows from H1 by Prop. K (BGS-TRACE-332), conditional on H1-shell. The v5 threshold quoted in the draft is p ≥ 3307 when the H1 constant is C ≤ 0.082, and p ≥ 1409 when C ≤ 8.8·10⁻⁴. Those primes are conditional arithmetic. They are not a new official threshold, and this note does not replace them.

| Input | Register status | What is actually proved |
| --- | --- | --- |
| H0 | taken as given | Line F/J package cited by the draft; Prop X′ (TRACE-324) is verification-pending |
| H1 = H1-bad + H1-ali (TRACE-336) | open | Shell law for j ≤ 14, core functional only, C_cert ≤ 4.36·10⁻⁴ (Thm A, TRACE-331). Prop. F (TRACE-329): no unrestricted carry or torus bound can give H1 |
| H2 | met | δ_int^core ≤ 5.14476·10⁻⁷ |
| H3 (TRACE-301) | open as a claim; substance is Prop. K | [P + CA modulo H1-shell]. The span bound ℓ ≤ 2j + g₀ was [P-sketch]. Background interplay and polymer normalisation were [P-sketch] |
| H4 (TRACE-302) | met | δ_true ≤ 5.0313·10⁻⁶ |
| H5 (TRACE-303) | open | c_B = 0.7375 is [P-sketch]; the needed c < 0.387 is open. On the NSW-prime set 𝒫 the mixed-class clause is vacuous, and infinitude of 𝒫 is open |
| H6 (TRACE-304) | open | explicit p₀ for C′ uncomputed; squarefreeness of h_p is Wieferich-type |
| H7* (TRACE-305) | open | signed control of included levels below the floor, including prime powers dividing K_p. Theorem W is non-vacuous only at p far beyond the crossover |
| H8 (TRACE-306) | open | on prime h_p it reduces to H1 [P-sketch]; composite h_p is free only under an extra smallness condition |
| R′ (TRACE-206) | open | not refuted |
| BGS-BGS-001, TRACE-005 | open | untouched |

## The route

The obstruction inside H1 is not a missing length estimate. Prop. F already rules out every bound that uses the unrestricted joint torus mean. The joint collision relation is ε-adic, with carries |e| ≤ 51 and 6145 pair states (Lemma J); the 633-state λ-graph is only the single-window subsystem. A direct Markov certificate on that system, at block size 495⁴, is not a computation this note can close. Scalar letterwise contraction diverges (N14: κ_v up to 38). The cellwise lower bounds N_H ≥ 1 (N13 §4.2) imply that a product of norms cannot decay; the N15 table’s 2048 cell upper bounds are all above 1.04, so they also do not yield a geometric mean below 1.

H5 and H7* are real open estimates, and either one blocks v5 even after H1. They are not the cheapest step that was still marked as a sketch inside an otherwise written implication. That step is the span bound in Prop. K.

The attack is that span bound. The result is a theorem for the length, a sharp pair of constants, and a recomputed tail. H1-bad and H1-ali stay open, so H3 stays conditional and R′ stays open.

## What was proved in this note

**Theorem A [P]** (`proofs/span_law.md`). For α ∈ ℤ[√2] \ {0}, with L = log(|N(α)|/2) / log ε and with span the length of the balanced ε-digit word,

L + 1 < span < L + 3.

The length is constant on the class modulo ±ε^ℤ. The digits lie in {−1, 0, 1}. For every class except the class of √2, span = Kᵣ − Kₗ + 3 exactly, where Kₗ and Kᵣ are the thresholds |θ| ≥ 1/2 and |θ̄| ≥ 1/2. The √2 class has span 2 and Kᵣ − Kₗ + 3 = 3, and still satisfies the strict inequalities (L = 0).

**Corollary C [P].** On shell j, where 2ʲ ≤ |N| < 2ʲ⁺¹,

span < κ j + 3, κ = log 2 / log ε ≈ 0.7864397013573949.

This is the constant N20 wrote as 0.787. It is log 2 / log ε, not log 2 / log λ.

**Corollary D [P].** The cluster length ℓ = span + g₀ used by Prop. K satisfies ℓ < κ j + 3 + g₀. For j ≥ 3 this is stronger than ℓ ≤ 2j + g₀, which is therefore a theorem for those shells. The old label [P-sketch] on the span bound is discharged in this note. It is not discharged in the registry: `record/claims.json` was not edited.

**Sharpness [P].** The constants 1 and 3 cannot be improved by 10⁻³. For α = 116, |N| = 13456, span = 13 and the defect span − L equals 2.99966264991176 within 10⁻⁵⁹. For α = 82√2, |N| = 13448, span = 11 and the defect equals 1.00033740024810 within 10⁻⁵⁹. Both words were computed with integer arithmetic (integer square roots), and the logarithms are arb enclosures. The class 116 has an internal zero run of 9, so it is not a single polymer at g₀ = 4. The bad class α = 118, |N| = 13924, run 3, has defect 2.96087221277804. A uniform bound span ≤ L + 2.96 already fails on a bad class of shell 13.

**Identification [P].** On a fundamental-domain representative the project’s `eps_digits` word is this digit word (Lemmas 7 and 8). Every class with |N| < 2¹⁵ was compared: 20434 words, 0 mismatches. Shell counts match N20 from j = 0 through j = 14, ending at 10225 classes in shell 14.

**Tail arithmetic [P], conditional** (`proofs/propk_tail.md`). Assume H1-shell(C, J₀ = 12) and the cited unweighted finite activity 2Σ|w| ≤ 2.03157·10⁻⁶ (TRACE-321, core functional, j ≤ 12, g₀ = 4). Replace ℓ ≤ 2j + g₀ by ℓ ≤ κ j + 3 + g₀ inside the N20 tail, and solve KP in arb.

At C = 0.082 the activity S₀ falls from ≤ 3.43990·10⁻⁴ to ≤ 3.24088·10⁻⁴. The KP threshold a falls from ≤ 2.63843·10⁻³ to ≤ 1.52670·10⁻³. The gas sees S₀, not a, so the exponent moves by about six percent, not by the forty percent visible in a. The length weight is what moves a; e^{aℓ} with aℓ of size a few thousandths is what moves S₀.

The same program reproduces the registered crossover inputs: δ = 3.4962·10⁻⁴ gives the prime 3307, δ = 5.0313·10⁻⁶ gives 1399, and δ = 7.4115·10⁻⁶ gives 1409. Under the sharp-span majorant at C = 0.082, a sufficient prime is 3067. Under the same program’s 2j-majorant the prime is 3299. The gap 3307 − 3299 is the bookkeeping gap between the published δ and this majorant (the published solver inflates a by 1.02 each iteration). The gap 3299 − 3067 is the span theorem. At C = 8.8·10⁻⁴ either span input leaves the prime at 1409, because the finite part dominates the tail.

These primes are conditional on H1-shell, on H0, H5–H8, on B_p ≥ κ for infinitely many p, and on the additive budgets v5 still treats as idealised. They are not a replacement for 3307 or 1409.

## What remains a sketch or a hypothesis

- H1-bad for shells j > 14, at C ≤ 0.082. Open. The finite-shell margin (about 186× at C_cert ≤ 4.36·10⁻⁴) says nothing about the tail, by Prop. F.
- H1-ali, the near-collision and box constants. Open. A Lipschitz bound on |r|² through the N_H table (Lip_H ≈ 167) is too crude to start a Beurling–Selberg estimate; that route was not pursued.
- Background interplay and polymer normalisation inside Prop. K. Still [P-sketch], exactly as N20 left them. Accepting Theorem A does not make TRACE-332 unconditional.
- H5, in particular c < 0.387 against the sketch c_B = 0.7375; or else infinitude of the NSW-prime set 𝒫.
- H6 (p₀ and squarefree h_p). H7* and H8 stay open. The second note gave the included \(K_p\)-divisors other than \(7\) no rate below \(T'\), and the amplified wrap at \(\ell_0 = p/4\) is outside the range the substituted \(c_B\) covers. The third note gives single-disc Galerkin rates. The fourth note encloses the same three crossings for the multi-disc finite section and does not transfer the one-step tail to the untruncated monodromy. The fifth note encloses one orbit at each of those conductors, and the isotropic orbits at the prime \(457\), and does not enclose the sum over \(\beta\). H8 on prime \(h_p\) still reduces to H1 only as a sketch.
- The passage of A_bad^{KP} into the gas exponent is used here as v5 uses it. The draft header still marks that correction [P-sketch], with lineN22 recording it as correct and necessary.

## Where a proof of H1 would have to go

A bound that can survive Prop. F has to use the bad restriction: digits in {−1, 0, 1}, no internal ε-zero-run of length g₀, and, by Theorem A, word length strictly between L+1 and L+3. That is a description of the support of the sum, not an estimate of Σ |r_A r_B|². The sum is still a joint second moment on the ε-adic carry system. Closing it is the remaining content of H1-bad. This note does not claim a transfer-matrix bound, a sofic presentation, or a value of C.
