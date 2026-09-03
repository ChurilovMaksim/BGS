# M1 note — cross terms in the historical Möbius-fiber assembly

A clean Python implementation and an independent C++20 implementation reproduce the historical fiber assembly and agree on the missing cross energy.

For `N=53,K=13,m=4`:
- diagonal raw energy: `934952569968`;
- cross raw energy: `7805905040`;
- cross/diagonal: `0.0083489851`.

For `N=199,K=11,m=18`:
- diagonal raw energy: approximately `1.1635012135e16`;
- cross raw energy: approximately `3.1752387617e14`;
- cross/diagonal: `0.0272903777`.

A substantial part is trivial/nontrivial coupling; the correction is not confined to nontrivial/nontrivial pairs.  Therefore the historical diagonal-only identity is false for this assembly.

The code/result live at:
- `experiments/m1/cross_term_energy.py`;
- `src/cpp/m1/cross_term_energy.cpp`;
- `results/diagnostics/m1_cross_term_energy.json`.
