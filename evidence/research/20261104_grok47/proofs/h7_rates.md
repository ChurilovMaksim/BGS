# H7* on the included levels: Galerkin rates under and over \(T'\)

Tags in this file are local to the note. **[P]** is proved here, or is an external theorem with the locator named in the sentence. **[CA]** is a finite enclosure in ball arithmetic, of the object named in the sentence. **[N]** is a floating-point observation. **[C]** is not used. A finite enclosure of one conductor is not an asymptotic bound, and an enclosure of the Galerkin model is not an enclosure of the multi-disc operator.

The input under attack is H7* (BGS-TRACE-305), as stated in `computations/verification/lineN_theorem_draft/THEOREM_DRAFT_v5.md`. For an included level \(d \notin \{h_p\}\cup\{e\cdot h_p\}\) with \(d < L_{\mathrm{fl}}\), the cross-correlation growth is required to lie below \(T' = 1.42785\). The draft leaves every \(K_p\)-level other than \(d = 7\) open. Level \(7\) is the covered case: BGS-TRACE-223 gives \(|\mu_{1:3}| \le 1.2837144\).

The conductors asked for are the included \(K_p\)-divisors other than \(7\) at the NSW primes \(p = 5, 7, 19, 29\). They were listed by the trial factorisation in `proofs/h7_h8.md`: \(d = 31\) and \(d = 217\) at \(p = 5\), \(d = 49\) at \(p = 7\), and ten divisors at each of \(p = 19\) and \(p = 29\). This note does not re-factorise \(K_p\). It does not edit the claim registry. It does not discharge H7*, and it does not refute H7* for the multi-disc operator.

The verdict, inside the single-disc model of Section 2, is as follows. At \(d = 31\) every class, in every sector, has per-step rate at most \(1.0923934786042258\). At \(d = 49\) and \(d = 217\) every surviving class has per-step rate at most \(1.2892227802420704\). All three lie below \(T'\). At three included conductors a single surviving orbit has certified per-step rate above \(T'\): \(1.4587724665845072\) at \(d = 3437426497\), \(1.5119805994002586\) at \(d = 24061985479\), and \(1.4686852970394264\) at \(d = 2735635252619983\). No argument that would put every \(K_p\)-divisor \(d \equiv 1 \pmod 3\) under \(T'\) survives those three orbits. The remaining seventeen conductors were not exhausted.

## 1. The rate

Write \(\lambda = 3+2\sqrt{2}\) and \(\beta = b_x + b_y\sqrt{2}\). The twisted phase at step \(j\) is

\[
\tau_j = \frac{\operatorname{Tr}(\beta\lambda^j)}{d} \bmod 1.
\]

BGS-TRACE-221, as recorded in `mathematics/fixed-map/lineJ_d7_twisted_coefficient.md` §2, decomposes the readout into four rank-one sectors \(a \in \{0,2,4,6\}\) of the G2 automaton. The sector coefficients satisfy \(c^+_a = \overline{c^-_{a+4}}\). For \(a \in \{2,6\}\) one has \(c^+_a = \overline{c^-_{a+4}} = 1/2\), so the leading coefficient \(B\) of those sectors vanishes. For \(a \in \{0,4\}\) the same identity makes the sectors survive. The coefficient table is the automaton table. It does not depend on the conductor, and this note does not re-prove it. The level-\(7\) weight \(|W_C| = (12/49)|\cos(k\pi/7)|\) is not used.

The growth rate of one sector is the per-step spectral radius

\[
r(\beta, a) = \rho\Bigl(\prod_{j < P} L_{a/8 + \tau_j}\Bigr)^{1/P},
\]

where \(P\) is the order of \(\lambda\) modulo \(d\), and the product is taken with the first factor on the right. The quantity TRACE-223 bounds at level \(7\) is this rate for the multi-disc vertex and edge operators. The threshold in H7* is \(T' = 1.42785\).

## 2. The model that can actually be enclosed

The operator enclosed here is the single-disc Galerkin family used by `computations/verification/lineJ/J3/code/lyap.py`:

\[
L_t = \sum_{|n|\le 10} \hat g(n)\, e(nt)\, e(Cn^2/2)\, \mathrm{MC}_n
\]

on the monomial basis of \(H^2(D_\rho)\), with \(\rho = 2.6\), mode cutoff \(K = 40\), \(\hat g(n) = i^n J_n(1.8)\), and \(C = -1/(\lambda - \lambda^{-1})\). The phase \(a/8 + \tau_j\) enters as the character \(e(nt)\). In the code the index is \((ad + 8\operatorname{Tr})/(8d)\). The factor \(8\) on the trace is required.

**Lemma 1 [P].** The disc radius \(2.6\) lies above the cutoff \(10/(\lambda - 1)\).

Indeed \(\lambda - 1 = 2(1+\sqrt{2})\), so the inequality \(2.6 > 10/(\lambda-1)\) rearranges to \(\sqrt{2} > 12/13\). Squaring both sides, which preserves the inequality because both sides are positive, gives \(2 > 144/169\), that is \(338 > 144\).

The same family at level \(7\) reproduces the three TRACE-223 classes. The self-test of `code/h7_rates.py` encloses them in the ball arithmetic of Section 3:

| class | sector | model enclosure | TRACE-223 |
| --- | --- | --- | --- |
| \((1,3)\) | \(6\) | \(1.283714293986\) | \(\lvert\mu_{1:3}\rvert \le 1.2837144\) |
| \((2,1)\) | \(4\) | \(1.283595135666\), inside \([1.2835950326,\ 1.2835952326]\) | the certified disc |
| \((0,1)\) | \(0\) | \(1.262430629485\) | \(\lvert\mu_{0:1}\rvert \le 1.2624308\) |

**[CA].** These three model values lie where TRACE-223 puts the multi-disc rates. The comparison is a calibration of the model at period \(3\). It is not a tail bound at period \(3p\).

The multi-disc builder of TRACE-223 (vertex block of dimension \(1980\), edge block, perturbation about \(2.37\cdot 10^{-10}\)) is not rerun. Every rate below is a rate of \(L_t\), not a rate of \(V_{\beta,a}\) or \(E_{\beta,a}\). Where the model rate lies above \(T'\), this machinery cannot certify the level below \(T'\). Where the model rate lies below \(T'\), the gap from the model to the multi-disc operator remains open.

One comparison that does transfer is the untwisted one-step radius. The matrix \(L_0\) has spectral radius

\[
\mu^*_{\mathrm{model}} \in [1.9154732036882485,\ 1.9154732036883702]
\]

**[CA]**, with Kantorovich constant \(h = 7.20\cdot 10^{-13}\). The enclosure is the final Newton routine, including the Neumann inflation; the eigenvalue was already of size one, so no power-of-two scaling was applied. The interval sits inside the TRACE-198 disc \(|\mu^*| \in [1.9154712,\ 1.9154753]\). In particular \(\mu^*_{\mathrm{model}} > T'\). Any upper bound that applies to every phase sequence is at least this large. BGS-TRACE-295 caps the free joint spectral radius by \(\Lambda_{\mathrm{free}} \le 1.9656353\), which is also above \(T'\). A twist-blind majorant cannot land under \(T'\).

## 3. The enclosure

Two computations are used. Both run in flint `acb` balls, at precision \(128\) for period \(15\), \(160\) for period \(21\), and \(8P+64\) bits for a longer period.

**Balanced Frobenius cap [P + CA].** Scipy's diagonal balancing with permutation turned off returns scales that are powers of two. The code checks the convention \(B_{ij} = M_{ij}\cdot\mathrm{scale}[j]/\mathrm{scale}[i]\) on one midpoint entry and then applies the same exponents to the ball. Multiplication by \(2^{e}\) is exact, so \(B\) is a ball for a diagonal similarity of every matrix in the product ball. Eigenvalues are unchanged, and

\[
\rho(B) \le \|B^m\|_F^{1/m}.
\]

The squared Frobenius norm is \(\operatorname{Tr}(B^* B)\), computed in the ball. The reported upper bound is `float` of `abs_upper`, which the flint test `test_arb_abs_bounds` guarantees to lie at or above the upper end of the ball. The per-step cap is that upper bound to the power \(1/(mP)\). This is an upper bound on the spectral radius of the true Galerkin product. It becomes an upper bound under \(T'\) only when the number itself is strictly less than \(1.42785\).

**Newton lower bound [P + CA].** Write \(F(v,\lambda) = (B-\lambda I)v\) with the pivot coordinate of \(v\) fixed at \(1\). The derivative is Lipschitz with constant \(2\) in the infinity norm: the difference of two derivatives, applied to a tangent \((\eta,\tau)\), is \(-\tau\,\delta v - \delta\lambda\,\eta\), whose infinity norm is at most \(2\|(\delta v,\delta\lambda)\|_\infty\). If \(\beta \ge \|F'(y_0)^{-1}\|_\infty\), \(\eta \ge \|F'(y_0)^{-1} F(y_0)\|_\infty\) and \(h = 2\beta\eta \le 1/2\), Newton–Kantorovich puts a root inside the infinity ball of radius \(2\eta\) about the centre. The radius \(2\eta\) is the crude end of the standard interval \([1,2]\eta\).

The centre is a floating-point eigenpair of the midpoint, after dividing by an exact power of two so that the unknown eigenvalue has magnitude in \([1,2)\). The residual is formed with the ball matrix, so its absolute upper bound covers the true matrix inside the product enclosure. The inverse norm is computed on the midpoint and inflated by the Neumann factor \(1/(1-\beta_0\delta)\), where \(\delta\) is the infinity norm of the entrywise radius of \(B\). A ball solve on the interval matrix is not used as an inverse bound: flint's solve encloses rounding of one system, and a direct test with radius \(5\cdot 10^{-2}\) shows that the output radius stays at rounding size. The Neumann step is what puts the radius of \(B\) into \(\beta\).

The resulting disc is a lower bound on the spectral radius, because it contains one eigenvalue. It is an upper bound on the spectral radius only together with the Frobenius cap. A level is certified above \(T'\) when the Newton lower bound exceeds \(1.42785\). A level is certified below \(T'\) when every class in the surviving sectors has Frobenius cap strictly below \(1.42785\).

At the three crossings of Section 7 the inflated condition number \(\beta\) is about \(1.44\), the ball-radius factor \(\beta_0\delta\) is below \(10^{-60}\), and \(h\) is about \(10^{-15}\).

## 4. Phase identity

**Lemma 2 [P].** Let \(d = ce\) and \(\beta = e\beta'\). Then

\[
\frac{\operatorname{Tr}(\beta\lambda^j)}{d} = \frac{\operatorname{Tr}(\beta'\lambda^j)}{c}
\]

as rational numbers. Reducing \(\lambda^j\) modulo \(d\) before the trace does not change the value modulo \(1\), because the added term is a multiple of \(d\) and its trace against \(\beta\) is divisible by \(d\).

The per-step rate depends on the phases only. An inherited class therefore has the same sector rate as its parent, for the true sector operator and for the Galerkin model. Coprimeness is not used. The self-test checks the integer form of the identity on three pairs: \((49,\beta=(7,21))\) against level \(7\), \((217,\beta=(31,93))\) against level \(7\), and \((217,\beta=(7,63))\) against level \(31\).

Consequence for the true operator, by this identity together with TRACE-223: on the sublattice \(\beta \in q\cdot\mathcal{O}\) at a conductor \(7q\), the sector rates equal the level-\(7\) rates, and the surviving one is at most \(1.2837144\). The same copying holds from any parent. It covers no primitive class. At a prime conductor the only inherited class is \(0\).

The crossings in Section 7 are not inherited. At \(d = 3437426497 = 457\cdot 7521721\), the vector \((-208,0)\) is divisible by neither factor. At \(d = 2735635252619983 = 7\cdot 13921\cdot 28073057689\), the vector \((-89,0)\) is divisible by none of those factors.

One numerical check of the copying **[N]**: the ray search finds the same rate \(1.29608327\) at \(\beta = (-12,-6)\) on \(d = 28073057689\) and at \(\beta = 7(-12,-6)\) on \(d = 7\cdot 28073057689\). That is the identity, seen in floating point. It is not the maximum of either level.

## 5. Orders, and a length bound that does not bound the rate

**Lemma 3 [P, finite].** For each of the \(23\) conductors in the list, the first return of \((x,y)\mapsto (3x+4y,\ 2x+3y)\) modulo \(d\) occurs at step \(3p\). Each such \(d\) divides \(K_p\), and \(d^2 \le h_p K_p\). The checks are integer comparisons, recorded in `logs/h7_rates_survey.json`.

TRACE-265 says that every prime factor of \(K_p\) other than \(7\) has rank \(3p\). That order computation is cited, not repeated. Lemma 3 extends the same count to the composite conductors in the list, by the same matrix powering. There is no single matrix, independent of \(p\), whose spectral radius is the rate.

**Lemma 4 [P].** The zero phase sequence occurs only at \(\beta \equiv 0\). If \(\operatorname{Tr}(\beta\lambda^j)\equiv 0\pmod d\) for every \(j\), then \(j = 0\) gives \(d\mid 2b_x\). For odd \(d\) this is \(d\mid b_x\). The step \(j = 1\) then gives \(d\mid 4b_y\), hence \(d\mid b_y\).

**Lemma 5 [P].** If \(d^2 \le h_{3p}\), then \(\log_\lambda d < 3p/4 - 1/6\).

From Lemma 1 of `proofs/h7_h8.md`, \(h_{3p} = (\varepsilon^{3p} - \varepsilon^{-3p})/2 < \varepsilon^{3p}/2\), with \(\varepsilon = 1+\sqrt{2}\) and \(\lambda = \varepsilon^2\). So \(d < \varepsilon^{3p/2}/\sqrt{2}\). The claim \(\log_\lambda d < 3p/4 - 1/6\) is the comparison of this upper bound with \(\lambda^{3p/4 - 1/6} = \varepsilon^{3p/2 - 1/3}\).

The inequality \(d < \varepsilon^{3p/2}/\sqrt{2}\) upgrades to \(d < \varepsilon^{3p/2 - 1/3}\) once \(\varepsilon^{1/3} \le \sqrt{2}\). That is \(\varepsilon^2 \le 8\), that is \(\lambda \le 8\). And \(\lambda = 3+2\sqrt{2} < 6\), because \(2\sqrt{2} < 3\), because \(\sqrt{2} < 3/2\), because \(2 < 9/4\). So \(\lambda < 8\).

The unwrapped prefix of a unit-length vector is shorter than \(3p/4 - 1/6\) steps. Two such ends have total length shorter than \(3p/2 - 1/3\), and the period is \(3p\), so a positive fraction of the period lies outside those ends. This limits how long a phase can track the untwisted orbit. It does not limit the spectral radius. Section 7 gives orbits whose rate exceeds both \(T'\) and \(\sqrt{\mu^*_{\mathrm{model}}}\).

The square root is the formal value of a block estimate that puts spectral radius \(\mu^*\) on half the steps and spectral radius \(1\) on the other half, and then bounds the spectral radius of a product by the product of the spectral radii. The second step is not a theorem. The square root of the upper endpoint is \(1.38400621519138\). The orbit of Section 7 at \(d = 24061985479\) has rate \(1.5119805994002586\), which lies above every value of \(\sqrt{\mu^*_{\mathrm{model}}}\) inside the model interval.

The congruence \(d \equiv 1\pmod 3\) is Lemma 3 of `proofs/h7_h8.md`: it is the quadratic condition for a prime divisor of \(K_p\). It does not determine a rate. Level \(7\) and level \(31\) are both \(1\pmod 3\), and their surviving Galerkin rates are \(1.283595135666\) and \(1.048520846469\).

## 6. Three conductors, every class

The cap below is the maximum, over the stated classes and sectors, of the balanced Frobenius bound at \(m = 4\).

**Theorem 6 [CA].** At \(d = 31\), order \(15\), every one of the \(960\) nonzero classes and every sector \(a\in\{0,2,4,6\}\) has Galerkin per-step rate at most \(1.0923934786042258\). The cap is attained at \(\beta = (7,15)\), sector \(6\), and the ball is \([1.0923934786042 \pm 2.58\cdot 10^{-14}]\). Precision \(128\). In particular the bound is strictly less than \(1.42785\).

Sector \(6\) cancels in the leading coefficient. The largest surviving class in the same scan is \(\beta = (1,9)\), sector \(0\). The final Newton routine encloses its per-step rate in \([1.0485208464672031,\ 1.048520846471151]\), and the balanced cap of that one orbit at power \(16\) is \(1.0490294180164688\). The class \(\beta = (0,10)\), sector \(4\), has cap \(1.021911140698\) at the same power. The level bound does not need these two orbits. The cap of Theorem 6 already covers them.

**Theorem 7 [CA].** At \(d = 49\), order \(21\), every one of the \(2400\) nonzero classes and both surviving sectors \(a\in\{0,4\}\) has Galerkin per-step rate at most \(1.2876123688383678\). The cap is attained at \(\beta = (14,42) = 7(2,6)\), sector \(4\), which is the level-\(7\) survivor carried by Lemma 2. The final Newton routine encloses that orbit in \([1.2835951356658677,\ 1.283595135665885]\), with \(h = 3.76\cdot 10^{-13}\). Precision \(160\) for the cap, and the same working precision for the Newton rerun. The bound is strictly less than \(1.42785\).

Sectors \(2\) and \(6\) were scanned in floating point **[N]**. Their maxima sit on the inherited cancelling classes and equal the level-\(7\) model value \(1.283714293986\). They are not part of the ball cap. They are the sectors whose leading coefficient vanishes.

**Theorem 8 [CA].** At \(d = 217\), order \(15\), the slices \(b_x\in[0,109)\) and \(b_x\in[109,217)\) contain \(23652\) and \(23436\) classes. The union is the \(217^2-1 = 47088\) nonzero classes. Both surviving sectors were capped, at precision \(128\), at Frobenius power \(m = 4\). Both slices return the same cap \(1.2892227802420704\), with ball \([1.289222780242070 \pm 2.8\cdot 10^{-16}]\). One point where it is attained is \(\beta = (62,186) = 31(2,6)\), sector \(4\), the level-\(7\) survivor carried by Lemma 2. The phase sequence of \(\beta = (62,186)\) is a cyclic shift of the phase sequence of \(\beta = (62,31)\), checked by comparing the integer traces, so the two products have the same spectrum. The final Newton routine on \(\beta = (62,31)\) encloses the per-step rate in \([1.2835951356658468,\ 1.2835951356659059]\). The bound is strictly less than \(1.42785\).

## 7. Three conductors where a surviving orbit exceeds \(T'\)

Each row is one orbit. The Newton column is a lower bound on the per-step spectral radius of the Galerkin product. The cap column is the balanced Frobenius upper bound. Both lie above \(1.42785\). The sector is \(a = 0\), which is a surviving sector, so the vanishing of \(B\) on sectors \(2\) and \(6\) does not remove the orbit. The Kantorovich constant satisfies \(h < 10^{-14}\) and \(\beta < 1.45\).

| \(d\) | \(p\) | \(\beta\) | Newton lower bound | cap |
| --- | --- | --- | --- | --- |
| \(3437426497 = 457\cdot 7521721\) | \(19\) | \((-208,\ 0)\) | \(1.4587724665845072\) | \(1.4589707983991738\) |
| \(24061985479 = 7\cdot 457\cdot 7521721\) | \(19\) | \((227,\ 227)\) | \(1.5119805994002586\) | \(1.512186164726419\) |
| \(2735635252619983 = 7\cdot 13921\cdot 28073057689\) | \(29\) | \((-89,\ 0)\) | \(1.4686852970394264\) | \(1.468816118126973\) |

The third conductor is the complement, in \(K_{29} = 7\cdot 13921\cdot 5806729\cdot 28073057689\), of the factor \(5806729\). The second is the complement, in \(K_{19} = 7\cdot 457\cdot 14593\cdot 7521721\), of the factor \(14593\). Both products were checked as integers. Each of the three conductors satisfies \(d\equiv 1\pmod 3\), \(d\mid K_p\) and \(d^2\le h_p K_p\). The representative vectors are divisible by none of the prime factors of their conductors: \(208\) shares no factor with \(457\cdot 7521721\), \(227\) shares none with \(7\cdot 457\cdot 7521721\), and \(89\) shares none with \(7\cdot 13921\cdot 28073057689\). Lemma 2 does not apply to them.

An earlier, shorter ray at the first conductor already crosses: \(\beta = (-27,0)\) has Newton lower bound \(1.4288919795043777\) and cap \(1.428940544221835\). The orbit at \((-208,0)\) is higher, so it is the one quoted in the table. A box of width \(8\) at the third conductor sees only the rate \(1.383552\) at \(\beta = (4,3)\), which is under \(T'\). The crossing sits further out on the same ray, at length \(89\).

**Theorem 9 [CA].** In the Galerkin model, each of these three included conductors has a surviving-sector per-step rate strictly above \(T' = 1.42785\). The machinery that certifies level \(7\) below \(T'\) does not certify these three below \(T'\). The reason is the size of this eigenvalue, not a failure of the enclosure: the enclosure closes, and the number it closes on lies above the threshold.

This is a statement about \(L_t\). It is not a statement that the multi-disc radius of \(V_{\beta,0}\) exceeds \(T'\). The level-\(7\) calibration is smaller than \(10^{-7}\), and the gaps here are \(3\cdot 10^{-2}\), \(8\cdot 10^{-2}\) and \(4\cdot 10^{-2}\). That comparison explains why a tail of level-\(7\) size would not pull these three back under \(T'\). It is not itself a tail estimate, and it is not used as one.

## 8. The other seventeen conductors

No orbit in the searches below has a certified rate above \(T'\), and no search below covers \((\mathbb{Z}/d\mathbb{Z})^2\). These seventeen levels are not certified under \(T'\).

The searches are floating-point location, followed by a ball enclosure of the orbits in Section 7 and of the closest orbit that stayed under the threshold. The location passes were:

- a coordinate box \(|b_x|,|b_y|\le 32\), short rays to length \(96\), and the \(40\) lowest phase-energy samples among \(20000\) random classes (`logs/h7_rates_wide.json`);
- six ray shapes to length \(240\) (`logs/h7_rates_rays_ext.json`);
- seven ray shapes to length \(500\) on the nine conductors whose length-\(240\) maximum exceeded \(1.2\) and had not already crossed (`logs/h7_rates_rays_deep.json`).

Rows already decided by Section 7 are omitted. The length-\(500\) entry is blank when that conductor was under \(1.2\) at length \(240\) and was not searched again. Extending the window from \(240\) to \(500\) left the maximum unchanged except at \(d = 80835474409\) and at \(d = 390805036088569\).

| \(d\) | length \(240\) | length \(500\) | representative | sector |
| --- | --- | --- | --- | --- |
| \(457\) | \(1.00907786\) |  | \((-340,-170)\) | \(4\) |
| \(3199\) | \(1.09756442\) |  | \((-46,-46)\) | \(0\) |
| \(14593\) | \(1.09732229\) |  | \((-16,-16)\) | \(0\) |
| \(102151\) | \(1.16848678\) |  | \((-195,195)\) | \(0\) |
| \(6669001\) | \(1.33286811\) | \(1.33286811\) | \((80,0)\) | \(0\) |
| \(7521721\) | \(1.22847850\) | \(1.22847850\) | \((-197,0)\) | \(0\) |
| \(46683007\) | \(1.31907771\) | \(1.31907771\) | \((-162,-162)\) | \(0\) |
| \(52652047\) | \(1.29867529\) | \(1.29867529\) | \((-6,0)\) | \(0\) |
| \(13921\) | \(1.00344871\) |  | \((-40,-40)\) | \(0\) |
| \(97447\) | \(1.06744389\) |  | \((15,0)\) | \(0\) |
| \(5806729\) | \(1.16072095\) |  | \((-9,0)\) | \(0\) |
| \(40647103\) | \(1.16169064\) |  | \((-73,-73)\) | \(0\) |
| \(28073057689\) | \(1.29608327\) | \(1.29608327\) | \((-12,-6)\) | \(0\) |
| \(80835474409\) | \(1.28388060\) | \(1.28822271\) | \((-456,-456)\) | \(0\) |
| \(196511403823\) | \(1.29608327\) | \(1.29608327\) | \((-84,-42)\) | \(0\) |
| \(565848320863\) | \(1.28784526\) | \(1.28784526\) | \((-108,-54)\) | \(0\) |
| \(390805036088569\) | \(1.40465116\) | \(1.40606361\) | \((0,-321)\) | \(0\) |

The orbit \(\beta = (0,-321)\) at \(d = 390805036088569\), sector \(0\), was enclosed. The Newton value is \(1.4060636053128053\), with \(h < 10^{-15}\), and the balanced cap at power \(16\) is \(1.4061888484607947\). Both lie strictly below \(1.42785\). This is the closest certified orbit in the search that stays under the threshold. It is one orbit of a conductor with \(d^2\) classes.

The representative \((-456,-456)\) at \(d = 80835474409\) was the maximum of a further pass of the shapes \((k,k)\), \((k,0)\) and \((0,k)\) out to length \(2000\) (`logs/h7_rates_climb.json`). The floating-point rate stayed \(1.28822271\). That ray has peaked inside the window. The number is not a cap for the level.

Widening the box from width \(8\) to width \(32\), and then lengthening the ray, raised several of these numbers by more than the gap that remained. The three crossings of Section 7 were found that way: the width-\(8\) sample at \(d = 2735635252619983\) was \(1.383552\) at \(\beta = (4,3)\), under the threshold, and the ray at length \(89\) is certified at \(1.4686852970394264\).

## 9. No uniform bound falls out

A uniform argument would have to cover every divisor \(d\mid K_p\) with \(d\equiv 1\pmod 3\), at every prime \(p\). The following five facts are what that argument has to live with.

1. **[CA]** The untwisted step \(L_0\) has spectral radius above \(T'\). A bound that does not read the phases cannot land under \(T'\).
2. **[P]** The condition \(d\equiv 1\pmod 3\) is the quadratic condition of Lemma 3 in `proofs/h7_h8.md`. Levels \(7\) and \(31\) satisfy it and have different rates.
3. **[P]** Lemma 2 copies a parent rate onto a sublattice. The crossings are not on that sublattice. A prime conductor has no nontrivial parent.
4. **[P]** The period is \(3p\) on every conductor in the list. The matrix depends on \(p\).
5. **[CA]** The length bound of Lemma 5 does not keep the rate under \(T'\), and it does not keep the rate under \(\sqrt{\mu^*_{\mathrm{model}}}\). Theorem 9 is the counterexample inside the model.

The level-\(7\) rate \(1.2837144\) is not an upper envelope. It is the rate of one conductor, copied onto inherited sublattices, and exceeded by primitive rays at larger included conductors.

## 10. Closure

Every computation cited above has closed. The \(d = 217\) slices give Theorem 8. The length-\(500\) search gave the table in Section 8, and the length-\(2000\) continuation at \(d = 80835474409\) stayed at \(1.28822271\). The orbit at \(d = 390805036088569\), \(\beta = (0,-321)\), is the ball enclosure quoted in Section 8.

The Newton intervals quoted for the maximizers at \(d = 31\), \(d = 49\) and \(d = 217\) were recomputed with the final routine, the one that inflates the inverse by the ball radius and scales large eigenvalues. The caps in Theorems 6–8 come from the full scans. A cap does not use the Newton routine. The scan logs also contain an earlier Newton enclosure of the same maximizers; the intervals above are the ones from the final routine, and they contain the level-\(7\) model value.
