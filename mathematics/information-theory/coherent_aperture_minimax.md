# Moment-constrained tomography with an observation aperture

Proof authority: `manuscript/unified_sections/coherent_aperture_minimax.tex`
and `heterodyne_aperture_minimax.tex`.

Fix the number of modes s, a photon-moment exponent beta>0, and a moment bound
E>0. There is no state-rank or hard Fock-cutoff assumption. Let

    K_R(T) = T / (1 + max(0, log(T/R^2))).

Uniformly over R>=R0>0, including infinity and radii varying with the budget:

* Sup-norm coherent-probability error delta on the complete ball has optimal
  trace-distance modulus Theta(K_R(log(1/delta))^(-beta/2)).
* B fresh-copy binary coherent-projector tests have minimax expected trace
  distance Theta(K_R(log B)^(-beta/2)), even allowing classical adaptation.
* Ordinary heterodyne detection censored outside the ball, with an outside
  flag and all copies counted, has the same minimax order. R=infinity gives
  uncensored heterodyne.

A finite tensor-Chebyshev reconstruction and positive-part normalization
prove the upper bounds. The cutoff is a regularization parameter, not an
assumption on the unknown state. Pure vacuum/high-number superpositions with
moment exactly E prove the lower bounds, through conditional Hellinger
control for adaptive transcripts and product affinity for heterodyne data.
Constants depend on s,beta,E,R0. Sharp leading constants and mode-uniform
complexity are not claimed. Homodyne, squeezed measurements and collective
quantum measurements are not covered by the lower bounds.

For beta=1, fixed radius gives sqrt(log log B/log B); arbitrary amplitudes or
uncensored heterodyne give 1/sqrt(log B). These are matching orders, not just
an instability example. The earlier fixed-shell theorem remains separate:
the new upper bounds use a ball and do not close its fixed-shell modulus.

Reproduction:

    python computations/verification/coherent_aperture_minimax.py --max-k 16 --expanded --replay build/aperture.txt --output build/aperture.json
    cmake -S . -B build/cmake
    cmake --build build/cmake --target coherent_aperture_bounds
    build/cmake/coherent_aperture_bounds build/aperture.txt

The one-mode high-precision reference implementation is
`computations/analysis/coherent_reconstruction.py`. The proof covers fixed
multimode dimension, whereas the numerical reconstruction code intentionally
implements one mode. Scalar arithmetic checks are not a formal proof of the
analytic or statistical theorems. No BGS result or established priority is
asserted.
