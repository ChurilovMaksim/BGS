# Literature comparison for the aperture-minimax theorem

## Closest primary sources checked

1. Landon-Cardinal, Govia and Clerk, Quantitative Tomography for Continuous
   Variable Quantum Systems, PRL 120, 090501 (2018),
   DOI 10.1103/PhysRevLett.120.090501; arXiv:1706.07816.
   Interpolation-based continuous-variable reconstruction is prior work.
2. Gandhari, Albert, Gerrits, Taylor and Gullans, Precision Bounds on
   Continuous-Variable State Tomography Using Classical Shadows, PRX Quantum
   5, 010346 (2024), DOI 10.1103/PRXQuantum.5.010346; arXiv:2211.05149.
   The NIST-hosted journal PDF gives exponential heterodyne upper bounds at
   a hard Fock cutoff and explicitly leaves optimal lower bounds open.
3. Becker, Datta, Lami and Rouze, Classical Shadow Tomography for Continuous
   Variables Quantum Systems, IEEE TIT 70(5), 3427-3452 (2024),
   DOI 10.1109/TIT.2024.3357972; arXiv:2211.07578v2.
   Both the arXiv v2 and final published version from the University of
   Amsterdam repository were checked, including the journal page 3431 image.
4. Mele, Mele, Bittel, Eisert, Giovannetti, Lami, Leone and Oliviero,
   Learning quantum states of continuous-variable systems, Nature Physics
   21, 2002-2008 (2025), DOI 10.1038/s41567-025-03086-2;
   arXiv:2405.01431v4. General moment-constrained tomography is prior work;
   measurement-dependent bounds must not be confused with unrestricted ones.

## A narrow source-level conflict, not a blanket retraction

The detailed heterodyne Theorem 4 in the Becker et al. journal version
(Theorem 11 in arXiv v2) retains a cutoff-dependent norm in its finite
sample bound. It must not be treated as uniformly bounded. The overview
Theorem 2 (Theorem 3 in arXiv v2), if read literally as a uniform polynomial
accuracy bound for full trace-distance recovery under one fixed finite
photon moment using ordinary heterodyne, conflicts with the explicit pure
pair in the new manuscript. For n=2k its squared Hellinger distance is at
most 4 sqrt(u(1-u))/sqrt(binomial(2k,k)), while its quantum trace distance
is 2 sqrt(u(1-u)), with u=E/n^beta. The pair also has uniformly bounded
(I+N)^beta moment for every fixed integer beta. An elementary two-point
bound therefore forbids polynomial-copy recovery at the stated uniformity.

This does not invalidate their explicit cutoff-dependent theorem, homodyne
results, or estimation of a fixed finite list of polynomial observables.
No author correspondence, accepted erratum or independent referee assessment
has occurred. The present proofs and this comparison need outside review.

## Remaining priority boundary

Neither abstract matching nor citation validation establishes originality.
The current specific claim is a matching expected trace-distance rate under
one photon-moment condition, uniform across the radius of the recorded
phase-space ball, for the two precisely defined measurement models. Earlier
Wigner pointwise/Sobolev minimax results and unrestricted pure-state minimax
results answer different questions. No absence-of-prior-art theorem is claimed.

Primary versions:
https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=935842
https://pure.uva.nl/ws/files/228864282/Classical_Shadow_Tomography_for_Continuous_Variables_Quantum_Systems.pdf
https://arxiv.org/abs/2405.01431
https://arxiv.org/abs/1706.07816
