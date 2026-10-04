# Expansion, tensor memory and fixed-time packet source checks

Checked 4 October 2026 against primary texts. These mappings distinguish
external inputs, reconstructed elementary arguments and corroborating prior
work. They do not establish world-first priority.

| Source and exact locator | Project use | Boundary |
|---|---|---|
| Bourgain--Gamburd, *Uniform expansion bounds for Cayley graphs of SL2(Fp)*, Annals 167 (2008), 625--642, Theorem 1, p.626; [primary PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n2-p07.pdf) | TRACE-013: fixed integral generators S,V; their subgroup contains hyperbolic S,R with disjoint endpoints, hence is non-elementary. Transfer the Cayley gap to each nontrivial irreducible conjugation representation. | A lazy auxiliary random-walk channel gap; no control of the selected word VS or of the frozen propagator. |
| Gross--Audenaert--Eisert, *Evenly distributed unitaries: on the structure of unitary designs*, arXiv:quant-ph/0611002v2, Theorem 2; Section III.B, (20), Theorem 6; Section IV.C; [primary PDF](https://arxiv.org/pdf/quant-ph/0611002) | Prior character/frame-potential identity and Clifford two-design mechanism. The project reconstructs its exact even-sector ranks, full-space orbit compression and gap constant. | Basic frame-potential and Clifford mechanisms are prior mathematics. A two-design average is not a prescribed-word spectral theorem. |
| Popescu, *A simple and self-contained proof for the Lindemann--Weierstrass theorem*, arXiv:2306.14352v2, Corollary 3.2, p.16; [primary PDF](https://arxiv.org/pdf/2306.14352) | Nonzero complex algebraic alpha has transcendental exp(alpha). Distinct spectral labels give a nonzero algebraic exponent; every power trace is a nonzero algebraic-coefficient polynomial evaluated at one transcendental exponential. | Qualitative simplicity, nonvanishing and no exact scalar powers; no quantitative cancellation. Corollary 3.1, about real irrationality, would not suffice. |
| Dirichlet's 1837 theorem, opening paragraph p.1 of the [primary translation](https://arxiv.org/pdf/0808.1408), arXiv:0808.1408v2 (24 November 2014) | Infinite resonant sequence in TRACE-013. The fourth-root/order divisibility is reconstructed over Fp. | No maximal-order assertion or Artin conjecture is used. |
| Guillemin--Uribe--Wang, *Integral representations of isotropic semiclassical functions and applications*, J. Spectr. Theory 12 (2022), 227--258, DOI 10.4171/JST/400, Theorem 1.1, pp.229--230; Section 5.3, pp.256--257; [primary PDF](https://ems.press/content/serial-article-files/33870) | Prior coherent-state covariance under FIOs and fixed-time propagation with uniform estimates on compact time/center sets. FM-013 reconstructs the finite-order finite-Fourier packet recursion, odd-N sampling, overlap bound and exact frame. | Section 5.3 discusses a Schrödinger Hamiltonian; it is background, not a direct theorem about our periodic momentum-dependent symbol or an odd torus trace formula. The direct project construction is load-bearing. |
| Faure, *Semi-classical formula beyond the Ehrenfest time in quantum chaos. (I) Trace formula*, arXiv:nlin/0610004v2, Section 2.2.2; Proposition 4, (36)--(37); Proposition 11, (68)--(69), pp.30--31; [primary PDF](https://arxiv.org/pdf/nlin/0610004) | Historical conditional route to sharper action-phase trace amplitudes. | The even-N theorem is not imported at odd N. The stronger numerical limsup constants and full regularized plane matching retain their conditional boundary. Bounded fixed traces are now proved by a separate frame argument. |

Relevant prior project results: FM-007 already proves normalized trace
vanishing, including a logarithmic window; FM-001 supplies the corrected
symbol, Anosov dynamics and four fixed-point Hessians; FLOW-003 supplies
the exact covariance inequality; fixed_strength_locality.md already gives
nonlinear arithmetic conjugates. None is counted as newly discovered here.

The related 29 September 2026 preprint Jain,
[*Ramanujan quantum expanders from the Weil representation*](https://arxiv.org/abs/2609.38075),
credits earlier classical-to-quantum transfer. It is related work, not a
load-bearing source replacing the checked Bourgain--Gamburd theorem.
