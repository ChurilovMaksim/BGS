# Self-referee of the H7* rate note

Read against `proofs/h7_rates.md` and the logs under `logs/` and `logs/parts/`. Each item is a way the argument can be misread or can fail, followed by the check that was actually made.

## 1. The model is not the operator TRACE-223 certified

The failure mode is to read Theorems 6–9 as bounds on \(V_{\beta,a}\) and \(E_{\beta,a}\).

The enclosed operator is the single-disc family \(L_t\) of `lyap.py`: \(\rho = 2.6\), \(K = 40\), letters \(|n|\le 10\), \(C = -1/(\lambda-\lambda^{-1})\). TRACE-223 encloses the multi-disc vertex block of dimension \(1980\) and the edge block, with a counted perturbation about \(2.37\cdot 10^{-10}\). That builder was not rerun. The level-\(7\) self-test puts the model inside the three TRACE-223 discs. That is a calibration at period \(3\). It does not estimate the tail at period \(57\) or \(87\).

Where the note says a conductor exceeds \(T'\), the sentence is about \(L_t\). A tail larger than the gap \(0.03\) could in principle put the multi-disc radius back under \(T'\). The note records the size of the gap and does not convert it into a tail bound. H7* stays open for the multi-disc operator.

Where the note says a conductor lies under \(T'\), the sentence is again about \(L_t\). The same tail could in principle push a model rate of \(1.29\) over \(1.42785\). The margin at \(d = 31\) is \(1.42785 - 1.09240 = 0.335\). The margin at \(d = 49\) and \(d = 217\) is about \(0.14\). Neither margin is a transferred tail bound.

## 2. Sectors 2 and 6 are not the H7* rate

The failure mode is to treat the largest sector, whatever it is, as the growth of \(\mathrm{Lin}_d\).

BGS-TRACE-221 gives \(B = 0\) on sectors \(2\) and \(6\), from \(c^+_a = \overline{c^-_{a+4}} = 1/2\). The identity is the G2 table, cited and not re-proved. The level-\(7\) weight \((12/49)|\cos(k\pi/7)|\) is not used at any other conductor. Theorems 7 and 8 cap the surviving sectors \(0\) and \(4\). Theorem 6 caps all four sectors at \(d = 31\), and the maximum happens to lie on a cancelling sector; the surviving rates are smaller, and the cap covers them anyway.

The three crossings of Theorem 9 are all in sector \(0\). Cancelling sectors \(2\) and \(6\) would not remove them.

## 3. A Newton disc is one eigenvalue

The failure mode is to quote the Newton upper endpoint as a bound on the spectral radius.

Newton–Kantorovich, with Lipschitz constant \(2\) and \(h = 2\beta\eta\le 1/2\), puts one eigenvalue inside the disc of radius \(2\eta\). That lower-bounds the spectral radius. The upper bound used for “below \(T'\)” is the balanced Frobenius cap \(\rho\le \|B^m\|_F^{1/m}\). At the crossings both numbers lie above \(T'\), so the lower bound is what decides them. At \(d = 31\), \(49\) and \(217\) the cap is what decides them.

The constant \(2\) is the infinity-norm Lipschitz constant of \(F(v,\lambda)=(B-\lambda I)v\) with one coordinate of \(v\) fixed. It is not a fitted constant. The radius \(2\eta\) is the crude end of the Kantorovich interval; the sharp radius is at most that.

## 4. A ball solve does not see the ball

The failure mode is to invert the interval Jacobian with `acb_mat.solve` and read the output radius as a bound over every matrix in the product ball.

A direct test with entry radius \(5\cdot 10^{-2}\) returned an output radius of size \(10^{-15}\), and sampled solutions of matrices inside the ball fell outside it. The code therefore inverts the midpoint and inflates by the Neumann factor \(1/(1-\beta_0\delta)\), where \(\delta\) is the infinity norm of the entrywise radius. The residual is formed on the ball. At the crossings, \(\beta_0\delta < 10^{-60}\) and \(\beta\approx 1.44\).

Large eigenvalues are divided by an exact power of two before the Newton step. Without that scaling, the period-\(87\) witness has absolute residual about \(0.2\) and \(h > 1/2\), which is float64’s unit in the last place of an eigenvalue of size \(10^{14}\), not a large true residual. After scaling, the same orbit has \(h \approx 2\cdot 10^{-15}\).

## 5. Balancing is a similarity, and the cap is monotone in the wrong direction for a false pass

Any integer exponents give a valid similarity. The scipy scales are used because they are powers of two and they shrink the norm; the code checks the indexing convention on one entry. A wrong exponent would make the cap larger. A larger cap can fail a true pass. It cannot create a false pass under \(T'\).

The power \(m = 4\) used for the full scans is coarser than the eigenvalue. At level \(7\) the \(m = 4\) cap is \(1.3009359828450457\) against the eigenvalue \(1.283595135666\). The cap is the number in Theorems 6–8, not the eigenvalue.

## 6. Precision

Period \(15\) at \(96\) bits produced a product ball whose relative radius was of order one, and the Newton Jacobian was singular. The working precision is \(128\) up to period \(16\), \(160\) up to period \(24\), and \(8P+64\) after that. The \(d = 31\) certificate is at \(128\). The \(d = 49\) certificate is at \(160\). The crossings are at \(520\) bits (period \(57\)) and \(760\) bits (period \(87\)).

`float(abs_upper)` is an upper bound and `float(abs_lower)` is a lower bound, by the flint test `test_arb_abs_bounds` and by a direct comparison of `arb(float)` against the ball on several intervals. The gaps to \(T'\) in the certificates are at least \(10^{-3}\). A one-ulp accident does not cross \(1.42785\).

## 7. Inheritance is a sublattice

The failure mode is to bound every class at a composite conductor by the level-\(7\) rate.

Lemma 2 copies the parent rate onto \(\beta = e\beta'\) at conductor \(ce\). Coprimeness is not required for the phase identity; the weight formula \(n_e/e^2\) is not used. The self-test checks the identity on \(49\leftarrow 7\), \(217\leftarrow 7\) and \(217\leftarrow 31\). At \(d = 49\) and \(d = 217\) the full surviving-sector scan attains its float maximum on that sublattice. At the three crossings the representative is divisible by no prime factor of the conductor, so the identity does not apply, and the rate is above the level-\(7\) rate.

The equal floating-point rates at \(d = 28073057689\), \(\beta = (-12,-6)\), and at seven times that class on the conductor \(7\) times larger, are a check of the identity. They are not a maximum.

## 8. A sample is not a maximum

The failure mode is to read Section 8 as a certification that those seventeen conductors lie under \(T'\).

The searches are rays and a box. Widening the box from width \(8\) to width \(32\), and lengthening the ray from \(32\) to \(240\), moved several rates by more than the gap that had remained. The conductor \(d = 2735635252619983\) is the example: width \(8\) gave \(1.383552\) at \(\beta = (4,3)\), under \(T'\), and the ray at length \(89\) is certified at \(1.4686852970394264\). Section 8 states the search limits and does not claim a cover of \((\mathbb{Z}/d\mathbb{Z})^2\).

A length-\(500\) continuation that does not raise a maximum is still a ray search. Classes off the rays are open.

## 9. The length bound is not a rate bound

Lemma 5 says that an included divisor has \(\log_\lambda d < 3p/4 - 1/6\). The comparison \(\lambda < 8\) is the elementary step, from \(2\sqrt{2} < 3\). It limits the unwrapped prefix. The spectral radius of the product is a different quantity. The block picture \(\sqrt{\mu^*}\approx 1.384\) lies below the certified rate \(1.5119805994002586\). Quoting Lemma 5 as a uniform discharge of H7* reverses the note.

## 10. What the arithmetic does not touch

The order \(3p\) on the \(23\) conductors is the first return of the integer matrix, checked exactly. TRACE-265’s rank statement for prime factors is cited. The inclusion cutoff \(d^2\le h_p K_p\) is the cutoff of the previous note in this directory, from TRACE-273 as N17b states it. \(L_{\mathrm{fl}}\) may sit above \(\sqrt{h_m}\). This note does not evaluate it, and it does not claim that a divisor above the square-root cutoff is outside H7*.

The earlier floating-point scan that indexed the phase by \((ad+\mathrm{Tr})/(8d)\) instead of \((ad+8\mathrm{Tr})/(8d)\) produced garbage rates above \(1.8\). Those numbers are not in the logs of this note. The self-test rejects a model that misses the level-\(7\) discs.

No row of `record/claims.json` was edited. Theorems 6–9 are not registry claims. Frozen R′, H1, H3, H5, H7* and H8 stay open.
