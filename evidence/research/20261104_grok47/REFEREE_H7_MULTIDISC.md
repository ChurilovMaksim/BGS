# Self-referee of the multi-disc note

Read against `proofs/h7_multidisc.md` and `logs/h7_multidisc_enclose.json`. Each item is a way the argument can be misread or can fail, followed by the check that was actually made.

## 1. The finite section is not the untruncated monodromy

The failure mode is to read the Newton lower endpoint as a lower bound on the spectral radius of the infinite-mode operator.

The enclosed matrix is the compression onto \(|c|\le 3\), degrees \(< 40\) and letters \(|n|\le 16\), dimension \(280\). Theorem 3 of the note is about that matrix. Section 4 bounds one step of the difference by \(< 9.646772214969684\cdot 10^{-5}\). Section 5 records that the product of \(57\) or \(87\) such steps, estimated by \(P\varepsilon M^{P-1}\) with \(M\approx 12\), is larger than the eigenvalue. That estimate was not replaced by a certified weighted norm. The untruncated rate is not claimed to lie above \(T'\).

A reader who stops at the table in Section 3 has a theorem about the section and does not have a theorem about \(\hat Z\).

## 2. Level 7 calibrates the builder, and does not redo TRACE-223

The failure mode is to replace the TRACE-223 discs by these wider, coarser enclosures.

Class \((2,1)\), sector \(4\), has Newton interval inside \([1.2835950326,\ 1.2835952326]\). Class \((1,3)\), sector \(6\), has lower endpoint \(1.28371429531092\), under the published cap \(1.2837144\). Both are at \(K = 40\), not at the dimension-\(1980\) cutoff, and the one-step tail here is \(10^{-4}\), not \(10^{-10}\). The agreement says the block formulae match. It does not shrink the tail.

## 3. One Newton disc lower-bounds the section radius only

The failure mode is to quote the upper endpoint as a spectral-radius cap, or to forget that Newton sees one eigenvalue.

The routine is `newton_enclose` in `h7_rates.py`. Lipschitz constant \(2\), success only for \(h\le 1/2\), Jacobian inverse on the midpoint, Neumann factor \(1/(1-\beta_0\delta)\). The returned lower endpoint lower-bounds the spectral radius of the matrix that was passed in. The upper endpoint does not. At the crossings the lower endpoint is the quantity compared with \(T'\). No Frobenius cap is used for that comparison.

The product is divided by exact powers of two while it is formed, and the root is multiplied back by \(2^{E/P}\). At level \(7\), class \((2,1)\), the exponent was \(1\) and the corrected root reproduces the unscaled enclosure to the printed digits. A float conversion of an arb endpoint can move by one unit in the last place. The gap from each crossing down to \(1.42785\) is larger than \(10^{-2}\).

## 4. The tail constants are one-step bounds

The failure mode is to multiply the one-step tail by the partial-product constant and call the result a monodromy theorem.

\(\theta < 0.5882395419204767\) is an arb upper bound. The composition estimate \(\|u^k\circ v\|_{H^2}\le\theta^k\) is the \(\ell^1\) norm of the binomial coefficients. The exit bound uses the Taylor tail of \(\exp(zu)\), and the letter bound uses \(|J_n(1.8)|\le (0.9)^{|n|}/|n|!\) with the ratio form \(t^{N+1}/(N+1)!/(1-t/(N+2))\). The factor \(\sqrt{7}\) is Cauchy–Schwarz on at most seven sources into one target. Forward invariance on \(|n|\le 16\) was checked in arb: no image leaves \(|c|\le 3\), and no value falls within \(10^{-8}\) of a half-integer.

No partial-product Frobenius norm was enclosed. Forming the Gram matrix squares the radii and was left out of the product loop for that reason. The linearisation in Section 5 is not a certified constant.

## 5. Inclusion is arithmetic plus a cited threshold

The failure mode is to treat a divisor of \(K_p\) as included without the square-root cutoff, or to invent a value of \(L_{\mathrm{fl}}\) at \(p = 19\).

\(h_p\), \(K_p\) and the three divisions were recomputed with Python integers. \(h_p\) does not divide any of the three conductors. \(d^2\le h_p K_p\) holds, with integer quotients \(278\), \(5\) and \(133\). The TRACE-199 shape with the constant \(3012.4\) from TRACE-273 was evaluated in arb and exceeds \(4mh_m\). The monotonicity check through \(m = 20001\) is cited from TRACE-273, not repeated. N17b's crossover \(p\ge 1386\) is cited to say that the floor absorbs nothing at \(p = 19\) and \(p = 29\). No numerical \(L_{\mathrm{fl}}\) is stated.

## 6. One orbit does not decide the aggregate, and these primes sit below the threshold

The failure mode is to call H7* false, or to say that Theorem v5 has fired.

The closure condition is \(|\mathrm{Lin}_d|\le\varepsilon_d|Z_\rho|^2/h_p\) with \(\sum\varepsilon_d\le\kappa_0\). The sentence "growth \(< T'\)" in the draft is the sufficient majorant. A section rate above \(T'\) falsifies that majorant for the section. It leaves the sum untouched. \((r/T')^P\) is a fixed power at \(m = 57\) and \(m = 87\).

Theorem v5 needs \(p\ge p_{\mathrm{thr}}\), and the draft's values are \(3307\) and, under the smaller H1 constant, \(1409\). Both \(19\) and \(29\) are smaller. The registered primes were not replaced.

## 7. The edge rates are float

The failure mode is to subtract \(\mathrm{Tr}\, E^m\) from the vertex eigenvalue on the strength of a float radius \(0.35\).

`logs/h7_multidisc_edge.json` is float64, \(\rho = 0.8\), \(K = 20\), letters \(|n|\le 14\). The five numbers lie under the level-\(7\) cap \(0.45\) and under \(T'\). No ball enclosure and no edge tail were run. The note marks them [N] and leaves the comparison \(\rho(E)<\rho(V)\) open.
