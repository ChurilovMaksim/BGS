# Self-referee of the window-moment note

Read against `proofs/h8_moments.md` and `logs/h8_moments.json`. Each item is a way the argument can be misread or can fail, followed by the check that was actually made.

## 1. The weight \(d\) is not the energy

The failure mode is to read \(E_k(W) \le k!\,|W|^k\) as a factor \(k!/|W|^k\) in front of the amplified weight, and then to declare the loss exponent equal to \(1+\gamma\).

\(E_k(W)\) counts additive \(2k\)-tuples in a window of powers of \(\lambda\). N16b (c2) charges a factor \(d\) because the amplified weight sits outside \(\ell^3 \le \ell^2\). Proposition 10 keeps that factor at exponent \(1\). The formal substitution of \(d\cdot E_k/|W|^{2k}\) for \(d\) is written out and is not a step in the proposition. At the injection upper bound, that formal sum stays under \(0.17973708\) for \(p = 1409\) and under \(0.17322030\) for \(p = 3307\). Both are short of \(0.26223963\). The formal combined exponent stays above \(0.92122088\). Covering the upper end of the gap requires an exponent under \(0.63534092\).

## 2. The liftable length is \(2\log_\lambda d\), not \(\ln d/(2\ln\lambda)\)

The failure mode is to use the length named in the request, \(\ln d/(2\ln\lambda)\), as if it contained \(\ell_0 = p/4\).

That length is \(\theta p/2\). It contains \(p/4\) only for \(\theta \ge 1/2\). The open interval lies under \(1/2\), so the named length does not contain the wrap window anywhere in the interval. The crude bound with both embeddings estimated by \(2k\lambda^l\), compared with the norm \(d^2\), contains \(p/4\) only for \(\theta > 1/4 + \log_\lambda(2k)/p\), which at \(k = 6\) and \(p = 1409\) sits above \(0.25\). Lemma 1 uses \(|\sigma_+| \le 2k\lambda^M\) and \(|\sigma_-| \le 2k\lambda^{-m}\), and compares the product with \(d^2\). The resulting length contains \(p/4\) once \(\theta > 1/8 + \log_\lambda(4k^2)/(2p)\). That threshold lies under \(0.12600049\) for \(k = 6\), \(p = 1409\), and under \(0.12542628\) for \(k = 6\), \(p = 3307\). The slack at the exponent-\(1\) threshold is more than \(200\) nats and more than \(400\) nats respectively.

The norm of \(d\mathcal O\) is \(d^2\). A comparison of the product of the embeddings with \(d\) is a different inequality.

## 3. Near-diagonal energy stops at mass \(6\)

The failure mode is to quote \(E_k \le k!\,|W|^k\) for every \(k\), or to treat a bounded search as the proof that the mass is at least \(7\).

Theorem 4 is the division by \(\lambda^m\) in the \(+\) embedding. The integer comparisons are \(49 < 50\), \(961 < 968\) and \(25 < 32\), together with \(6\lambda^{-1}-1 = \lambda^{-2}\). No coefficient bound and no length bound enter. Theorem 6 classifies mass \(7\): the only equality is \(\lambda^4+6\lambda = 6\lambda^3+1\), up to translation and swapping sides. The two sides are \(595+420\sqrt 2\). On windows of \(4\) to \(10\) consecutive exponents the excess over the permutation count is \(0\) for \(k \le 6\) and \(98(L-4)\) for \(k = 7\). That finite count is not the proof of Theorem 4.

The balanced expansion is Lemmas 3 and 4 of `proofs/span_law.md`, applied to \(\lambda^n\). The label TRACE-337 is not a row of `record/claims.json`, and that file was not edited. Lemma 3 records the single digit of one power. It does not say that a sum of powers has the superimposed word. The integer \(2\) is the witness that multiplicities carry. The mass argument is what controls repeated summands.

## 4. The window is not the subgroup

The failure mode is to export Theorem 7 to \(J_k\) on the whole of \(\langle\lambda\rangle\), of order \(p\) or \(3p\), and to feed that count to TRACE-279 Lemma N1.1.

On the open interval the liftable span is \(< p\). The orbit does not fit in the window. Lemma 1 at \(k = 1\) keeps the powers in one window distinct in \(\mathcal O/d\mathcal O\), which is a statement about the window. The moment in §4 is the moment of that window.

## 5. The character-sum threshold is inside exponent \(1\)

The failure mode is to read the mean bound \(d^{-2}\sum |S|^{2k} \le k!\,|W|^k\) as a bound \(\max|S| \le |W|^{1/2}\) on the gap.

The mean is at most \((k!)^{1/(2k)}|W|^{1/2}\). The maximum pays \(d^{1/k}\) for the number of characters. The resulting estimate drops below \(|W|\) only for \(\theta < 0.00576146\) at \(p = 1409\), \(k = 6\), and for \(\theta < 0.00289289\) at \(p = 3307\), \(k = 6\). The \(k = 7\) row, using \(E_7 \le 2\cdot 7!\,|W|^7\), stays under \(0.00641117\) and \(0.00324273\). All four lie under \(0.16661157\). A factor \(|W|^{O(k)}\) is \(d^{o(1)}\) because \(|W| = O(p)\).

## 6. The diagonal values \(k = 113\) and \(k = 261\) are not a theorem

The failure mode is to optimise \(k\ln|W|-\ln(k!)\) past mass \(7\) and to quote the resulting \(\theta\) as covered.

Those two integers are the first values at which that expression, with \(E_k\) imagined equal to \(k!\,|W|^k\), would push the formal sum of §4 up to \(0.26223963\). Theorem 4 says the imagined bound is false for every \(k \ge 7\). The paragraph that names \(113\) and \(261\) is marked as the arithmetic of a substitution the note does not justify. Lifting still holds at those \(k\), because \(4\cdot 113^2 < \lambda^7\) and \(4\cdot 261^2 < \lambda^8\). The relations are the obstruction, not the height.

## 7. What would make the note false

- A proof that the positivity factor \(d\) is multiplied by \(E_k/|W|^{2k}\).
- An equality of two \(k\)-sums in \(\mathcal O\) with \(k \le 6\) and unequal multisets.
- A second mass-\(7\) relation, not a translate of \(\lambda^4+6\lambda = 6\lambda^3+1\).
- A claim that \(\ell_0 = p/4\) fails to lift on \(\theta \ge 0.16661157\) for \(k \le 7\) at \(p \in \{1409, 3307\}\).
- A claim that the covered wrap range is larger than \(\theta < 0.16661157\).
- A claim that H8, H7*, or v5 is discharged.

None of these is asserted. The script checks are exact integer counts and arb balls at precision \(200\). No floating-point energy is used as a bound.
