# Prior scalar concentration mechanism

The scalar exponential argument in TRACE-079/080 is a Bernstein/Freedman
mechanism, not a new concentration inequality.

Primary-source comparison on 13 October 2026:

- Joel A. Tropp, *Freedman's inequality for matrix martingales*, Electronic
  Communications in Probability 16 (2011), 262–270. The author-hosted
  [published PDF](https://tropp.caltech.edu/papers/Tro11-Freedmans-Inequality.pdf)
  was read at Theorem 1.1, printed p.263 (PDF p.2). It states the scalar
  martingale tail in terms of predictable quadratic variation and a
  uniform upper increment bound, with denominator
  `2(sigma²+Rt/3)`. It permits a maximum over times, stronger than the
  fixed-target form needed here.
- David A. Freedman, *On Tail Probabilities for Martingales*, Annals of
  Probability 3(1), 100–118 (February 1975),
  [DOI 10.1214/aop/1176996452](https://projecteuclid.org/journals/annals-of-probability/volume-3/issue-1/On-Tail-Probabilities-for-Martingales/10.1214/aop/1176996452.full).
  Publisher metadata was verified; its complete original theorem text
  was not extracted in this comparison. Tropp identifies its Theorem
  1.6 as the original source.

The new flatness proof reconstructs its finite scalar exponential estimate
from the conditional Taylor series and a variance-compensated
supermartingale. It therefore needs no new external theorem leaf. The
clock corollary separately inherits the existing reviewed TRACE-060
dependency closure, including its scoped Tropp input. The prior source
comparison does not establish priority for the feedback theorem or certify
its full mathematical chain.
