# BGS-TRACE-132 certificate

Occupation sums for the Haar diagonal ensemble and for row inversion, on equal-diagonal and unequal-diagonal hyperbolic matrices. A pass checks the inequalities in `mathematics/fixed-map/hyperbolic_short_time_limit.md`. It does not prove BGS-TRACE-005 or BGS-BGS-001.

Coverage. Matrices \(\begin{pmatrix}3&4\\2&3\end{pmatrix}\), \(\begin{pmatrix}2&1\\1&1\end{pmatrix}\) and \(\begin{pmatrix}5&2\\2&1\end{pmatrix}\), times \(3\) and \(4\), odd moduli \(5\) through \(15\). Inversion on the primes \(5\), \(7\) and \(11\). Times one and two at \(N=5\) and \(N=7\). At \(p=3\) the inversion sum equals the uninverted sum; the time-three value is \(3.444444444444\) in both programs. There are \(48\) inequality rows.

```sh
python3 computations/verification/hyperbolic_short_time_limit.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/hyperbolic_short_time_limit.cpp -o /tmp/hyperbolic_short_time_limit
/tmp/hyperbolic_short_time_limit
```

The aggregate build

```sh
cd formalization && lake exe cache get && lake build Bgs
```

exited 0 (`8792` jobs). The log is [build_bgs.log](build_bgs.log), sha256 `de90e9a410bd3309cfd7a135d8bcee1c8568c7bff3b1bbf053446ef5448c27e0`.
