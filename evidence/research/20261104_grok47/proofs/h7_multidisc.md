# The three crossings on the multi-disc operator

Tags in this file are local to the note. **[P]** is proved here, or is an external theorem with the locator named in the sentence. **[CA]** is a finite enclosure in ball arithmetic, of the object named in the sentence. **[N]** is a floating-point observation. A finite enclosure is not an asymptotic bound. `record/claims.json` was not edited.

The question is whether the three Galerkin crossings of `proofs/h7_rates.md` survive for the multi-disc vertex operator that BGS-TRACE-223 certifies at level \(7\). They do, for the finite section of that operator named in Section 3. The one-step tail from that section to the core operator is proved in Section 4. The passage from that one-step tail to the spectral radius of the untruncated monodromy is not proved, and Section 5 says why the standard norm bound does not close. H7* as an aggregate is not shown false. Section 6 says which reading fails for the finite section, and which re-scoping is untouched.

## 1. The operator

The vertex transfer operator is the one built in `computations/verification/lineJ/code/certG_build_sector.py`. On the disc of radius \(\rho = 1.2\) about an integer centre \(c\), in the monomial basis of \(H^2\), a letter \(n\) contributes the composition with

\[
u \mapsto B + u/\lambda, \qquad B = \bigl((c+n)/\lambda - j\bigr)/\rho, \quad j = \operatorname{round}((c+n)/\lambda),
\]

multiplied by \(\exp(z u)\) with \(z = 2\pi i C n\rho\), and by the weight \(\hat g(n)\,e(C n^2/2)\,e(n t)\). Here \(\lambda = 3+2\sqrt{2}\), \(C = -1/(4\sqrt{2})\), and \(\hat g(n) = i^n J_n(1.8)\). The phase of a twist orbit is the same scalar used in `proofs/h7_rates.md`:

\[
t_j = a/8 + \tau_j, \qquad \tau_j = \operatorname{Tr}(\beta\lambda^j)/d \bmod 1.
\]

The 3-cycle is not tensored into the state. At a general conductor the per-step rate is

\[
r(\beta,a) = \rho\Bigl(\prod_{j<P} L_{t_j}\Bigr)^{1/P},
\]

with the first factor on the right. At level \(7\), \(P = 3\), and this is the rate TRACE-223 bounds. Sectors \(a\in\{2,6\}\) cancel by BGS-TRACE-221, cited and not re-proved. The three orbits below are in sector \(a = 0\). The level-\(7\) weight \((12/49)|\cos(k\pi/7)|\) is not used.

## 2. Inclusion [P, arithmetic, on TRACE-273]

Let \(u_0 = 1\), \(u_1 = 7\), \(u_{n+1} = 6u_n - u_{n-1}\), and \(h_p = u_{(p-1)/2}\). Then \(K_p = 4h_p^2+3\) and \(h_{3p} = h_p K_p\). Integer arithmetic gives

| \(p\) | \(h_p\) | \(K_p\) |
| --- | --- | --- |
| \(19\) | \(9369319\) | \(351136554095047 = 7\cdot 457\cdot 14593\cdot 7521721\) |
| \(29\) | \(63018038201\) | \(15885092554810781265607 = 7\cdot 13921\cdot 5806729\cdot 28073057689\) |

The three conductors and the tests \(d\mid K_p\), \(h_p\nmid d\), \(d^2\le h_p K_p\):

| \(d\) | factorisation | \(p\) | \(\beta\) | \(\lfloor h_m/d^2\rfloor\) |
| --- | --- | --- | --- | --- |
| \(3437426497\) | \(457\cdot 7521721\) | \(19\) | \((-208,0)\) | \(278\) |
| \(24061985479\) | \(7\cdot 457\cdot 7521721\) | \(19\) | \((227,227)\) | \(5\) |
| \(2735635252619983\) | \(7\cdot 13921\cdot 28073057689\) | \(29\) | \((-89,0)\) | \(133\) |

Each divides \(K_p\) exactly, none is divided by \(h_p\), and \(\gcd(\beta_x,\beta_y,d) = 1\). They are \(K_p\)-divisors, not \(h_p\) and not an inherited level \(e\cdot h_p\).

BGS-TRACE-273 (M4b in `mathematics/fixed-map/lineMN_conductor_structure.md`): Line F gives \(|Z_\rho|\ge \tfrac12(1-\lambda^{-m})(\mu_{\mathrm{lo}}^m - 3012.4)\) for \(\rho = (\pm 2,8)\), and with it \(|Z_\rho|^2\ge 4m h_m\) for every odd \(m\ge 15\), so every \(d\mid h_m\) with \(1<d\le\sqrt{h_m}\) is included. The constant \(3012.4\) and the check through \(m = 20001\) are cited, not re-proved. At the three pairs \((m,d) = (57,3437426497)\), \((57,24061985479)\), \((87,2735635252619983)\) the same lower bound was evaluated in arb at precision \(320\): \(|Z|^2 > 4m h_m\) holds, and \(d^2\le h_m\) was checked as an integer comparison. TRACE-273 then includes all three.

\(L_{\mathrm{fl}}\) is not given a numerical value here. N17b puts the idealised gas/Robin crossover at \(p\ge 1386\), and the draft's threshold with rate budgets at \(p\ge 3307\) or \(p\ge 1409\). At \(p = 19\) and \(p = 29\) the gas has not crossed \(I_p\), so the floor absorbs nothing. If H7* is applied at these primes, every included non-inherited level is an obligation. Theorem v5 does not apply H7* at these primes: its implication needs \(p\ge p_{\mathrm{thr}}\).

## 3. The finite section [CA]

The section keeps centres \(|c|\le 3\), monomials of degree \(< 40\), and letters \(|n|\le 16\). The dimension is \(7\cdot 40 = 280\). For every such pair \((c,n)\),

\[
|(c+n)/\lambda|\le 19/\lambda = 19(3-2\sqrt{2}) < 3.26 < 3.5,
\]

so the rounded image is an integer of absolute value at most \(3\). The arb check in `h7_multidisc_cert.py` found no exit and no rounding within \(10^{-8}\) of a half-integer. On this alphabet the core is forward-invariant [P].

The blocks were built in ball arithmetic at precision \(320\). One block, \(n = 1\), \(c = 0\), matches the float builder to \(1.3\cdot 10^{-16}\). The period product is scaled by exact powers of two so that the entries stay of moderate size; the scaling is undone on the eigenvalue. Newton–Kantorovich is the routine of `h7_rates.py`: midpoint Jacobian, Neumann inflation, Lipschitz constant \(2\), success only for \(h\le 1/2\). A returned lower endpoint is a lower bound on the spectral radius of this finite section. The float conversion of an arb endpoint can move by one unit in the last place; every comparison below has more than \(10^{-6}\) of room, and the lower endpoints are quoted after that conversion.

| orbit | \(P\) | \(h\) | lower | upper |
| --- | --- | --- | --- | --- |
| level \(7\), \((2,1)\), sector \(4\) | \(3\) | \(1.18\cdot 10^{-14}\) | \(1.2835951329030868\) | \(1.2835951329030901\) |
| level \(7\), \((1,3)\), sector \(6\) | \(3\) | \(3.11\cdot 10^{-14}\) | \(1.2837142953109737\) | \(1.2837142953109815\) |
| \(d = 3437426497\), \(\beta = (-208,0)\) | \(57\) | \(1.01\cdot 10^{-14}\) | \(1.458772466390154\) | \(1.4587724663901542\) |
| \(d = 24061985479\), \(\beta = (227,227)\) | \(57\) | \(1.79\cdot 10^{-14}\) | \(1.5119805975188876\) | \(1.5119805975188878\) |
| \(d = 2735635252619983\), \(\beta = (-89,0)\) | \(87\) | \(1.37\cdot 10^{-14}\) | \(1.4686852948918232\) | \(1.4686852948918234\) |

Decreasing each printed lower endpoint by \(10^{-12}\) restores a margin for the float conversion of the arb endpoint. All three crossing lower bounds remain above \(1.42785\), by \(0.03092\), \(0.08413\) and \(0.04083\).

The class \((2,1)\) interval sits inside the TRACE-223 disc \([1.2835950326,\ 1.2835952326]\). The class \((1,3)\) value sits under the TRACE-223 cap \(1.2837144\). That is the calibration: the section is the operator TRACE-223 certifies, at a coarser mode cutoff than the dimension-\(1980\) build. It does not reproduce the \(10^{-10}\) perturbation of that build.

The rank-\(40\) single-disc Galerkin rates enclosed in `proofs/h7_rates.md` are \(1.4587724665845072\), \(1.5119805994002586\) and \(1.4686852970394264\). The multi-disc section is a different projection (\(\rho = 1.2\), seven discs, letters through \(16\)). The three differences are \(1.94\cdot 10^{-10}\), \(1.88\cdot 10^{-9}\) and \(2.15\cdot 10^{-9}\). Both certified lower endpoints lie above \(T' = 1.42785\), so both projections cross. That is a comparison of two enclosures, not a tail from one matrix to the other.

## 4. One-step tail [P]

Write \(\theta = 1/(2\rho) + 1/\lambda\). The enclosed value is \(\theta < 0.5882395419204767\). The coefficient \(\ell^1\) norm of the composition of \(u^k\) is at most \(\theta^k\), hence so is the \(H^2\) norm. Multiplication by \(\exp(zu)\) shifts coefficient sequences isometrically, and \(|J_n(1.8)|\le (0.9)^{|n|}/|n|!\).

On one source disc, with letters \(|n|\le 16\):

- **Exit.** A mode \(k<40\) produces output modes \(\ge 40\) only through the tail of \(\exp(zu)\), at most \(\theta^k\sum_{m\ge 40-k}|z|^m/m!\). Summing modes, letters and both signs gives a one-disc bound whose \(\sqrt{7}\)-stacked operator norm is \(< 4.4732051773632864\cdot 10^{-5}\).
- **Return.** A mode \(k\ge 40\) has mass \(\le\theta^k\), and \(\|\exp(zu)\|\le e^{|z|}\), so the whole block from high modes is \(< 2.3227663651960194\cdot 10^{-7}\) after the same stacking.
- **Omitted letters.** \(\sum_{|n|>16}|J_n(1.8)|e^{\alpha|n|}/(1-\theta) < 5.1503393739544364\cdot 10^{-5}\) after stacking, with \(\alpha = \pi\rho/(2\sqrt{2})\). The series tail is \(t^{17}/17!/(1-t/18)\) at \(t = 0.9 e^{\alpha}\), not a subtraction of partial sums.

The stacking \(\sqrt{7}\) is Cauchy–Schwarz on sources that share a target: there are \(7\) sources, and each source column carries one block. The sum of the three pieces is \(< 9.646772214969684\cdot 10^{-5}\). This bounds the operator norm of one step of the difference between the section and the core operator on the same centres, all modes, all letters. It is not a bound on the monodromy.

## 5. Why the monodromy tail is not claimed

Pad the section to the whole space by zero and write one step of the core operator as \(A_j+E_j\) with \(\|E_j\|\le\varepsilon\) and \(\varepsilon < 9.65\cdot 10^{-5}\). The monodromy difference expands as

\[
\Bigl\|\prod(A_j+E_j)-\prod A_j\Bigr\| \le \sum_{k\ge 1}\binom{P}{k}\varepsilon^k M^{P-k},
\]

where \(M\) is a bound on \(\|A_j\|\). The float 2-norm of a section step is about \(12\), and the second singular value is about \(10\) (`h7_multidisc.py` orbits, truncation \(K = 40\)). Taking \(M = 12\) gives a majorant \(P\varepsilon M^{P-1}\) larger than \(10^{50}\) at \(P = 57\), far above the eigenvalue, which is of size \(1.46^{57}\). The bound is true and useless. Elsner's Hölder estimate in dimension \(280\) is the same kind of useless bound. A lower bound on \(\|Qv\|\) lower-bounds the norm of the monodromy, not its spectral radius.

A weighted norm with mode weight \(1.8^k\) brings the float 2-norm down to about \(2.9\), still large enough that \((2.9/1.46)^{57}\varepsilon\) exceeds \(1\). The same weight inflates high modes, so it does not shrink the tail. No common norm that would put \(P(M/r)^P\varepsilon\) under the gap \(1-(T'/r)^P\) was certified.

A first-order excursion along the section orbit, with the exit mass returning through the high-mode bound of Section 4 and then riding the section partial products, is smaller than the crude norm bound by many orders, because the return factor is \(< 2.33\cdot 10^{-7}\). That linearisation was not enclosed. The left factors in the telescoping sum would be section products, and the quadratic re-entry is not bounded. It is not promoted to a bound on \(\rho\).

The edge block was floated at \(\rho = 0.8\), \(K = 20\), half-integer centres, letters \(|n|\le 14\). The five per-step rates are \(0.34739\), \(0.35820\), \(0.34916\), \(0.34911\) and \(0.34340\). TRACE-223 caps every level-\(7\) edge block by \(0.45\). The float numbers sit under that cap and far under \(T'\). They are [N]. They are not a proof that \(\rho(E)<\rho(V)\) at these conductors. The trace formula is \((\operatorname{Tr} V^m-\operatorname{Tr} E^m)/3\). A vertex rate above \(T'\) is the growth of \(\hat Z\) only if the edge is smaller. That comparison is open for the untruncated edge.

## 6. What this does to H7* and to Theorem v5

H7* (BGS-TRACE-305), as a closure condition, asks for \(|\mathrm{Lin}_d|\le\varepsilon_d|Z_\rho|^2/h_p\) with \(\sum\varepsilon_d\le\kappa_0\), over the included levels below \(L_{\mathrm{fl}}\) other than \(h_p\) and \(e\cdot h_p\). The draft's phrase "i.e. cross-correlation growth \(< T' = 1.42785\)" is the sufficient majorant obtained by replacing \(\sum_\beta\kappa\hat Z\) with \((\sum|\kappa|)\max|\hat Z|\) and using \(\sum|\kappa|\lesssim d^2\). One orbit above \(T'\) falsifies that majorant. It does not falsify the sum.

The finite section of Section 3 has, at each of the three included conductors, a sector-\(0\) orbit whose certified per-step rate is above \(T'\). For that section, the sufficient reading is false. The aggregate is not shown false: \(|\mathrm{Lin}_d|\le(2/d^2)|Z|\,|\sum\kappa\hat Z|\), a single orbit contributes one term, and \((r/T')^P\) at the three section rates is \(3.39\), \(26.14\) and \(11.63\). Those are fixed powers at \(m = 57\) and \(m = 87\), not an asymptotic blow-up. An orbit with \(|\kappa|\ll d^2\) is negligible after the factor \(1/d^2\).

Theorem v5 says that frozen R′ fails along \(m = 3p\) for \(p\in\mathcal{P}\), if H0, H1, H6 and H7* hold, \(p\ge p_{\mathrm{thr}}\), and \(\mathcal{P}\) is infinite. The draft's threshold is \(p\ge 3307\) under H1 as stated, and \(p\ge 1409\) if \(C\le 8.8\cdot 10^{-4}\). Both \(19\) and \(29\) lie below either number. A failure of the sufficient reading at these two primes does not fire the implication, and it does not remove H7* from the hypotheses at \(p\ge p_{\mathrm{thr}}\).

The re-scoping that survives is the aggregate bound with the sum over \(\beta\) kept. A uniform cap at the level-\(7\) rate, or at \(T'\), does not survive for this finite section. Restricting the sufficient reading to \(p\ge p_{\mathrm{thr}}\) also survives these three conductors, because they lie below the threshold; that restriction is not a proof for large \(p\).

H7* stays open. Frozen R′ stays open. The claim registry was not edited.
