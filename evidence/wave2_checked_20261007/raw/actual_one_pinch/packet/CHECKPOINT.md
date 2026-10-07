# Resumed one-pinch checkpoint

7 October 2026. Task resumed from the verified 3930-file snapshot. No rematerialization, broad literature search, or new subagents. The root workspace and canonical source checkout are unchanged.

**Outcome:** a complete author candidate proof of the model-specific estimate

    ||C_N* L_(U_N)^r C_N|| = O_r(sqrt(log(2N)/N))

for each fixed r>=1, where C_N synthesizes adjoints of the displacement slices of the literal U_N. The proof is in `actual_fixed_lag_overlap.md`; it remains subject to independent review.

The decisive step is the direct r-variable cyclic phase built from the actual one-step parametrix. Its internal Hessian is a uniformly negative perturbation of -(3/2)I+(P+P*)/4, and every Poisson alias has reduced charge mixed derivative in [1/10,1/3]. Discrete stationary phase and alias-safe TT* prove the overlap estimate. The short-block Gram argument then yields

    N^-2 sum_m |w(m/N)| E_(N,m)(0) ->0

on each fixed positive compact Heisenberg band. Combined with the parent's supplied reviewed annealed theorem, this gives the occupation-subtracted ONE-PINCH aggregate. The native packet's manifest is recorded, but that packet was not received or re-audited here.

**Verification:** 129 exact bounded controls pass in both normal and optimized Python. They cover indexing, cyclic Hessians and constant slack, not the analytic limit. `self_audit.md` gives the separate author audit and precise independent-review questions. `source_bindings.json` pins the actual inputs to the verified snapshot.

**Remaining implication:** T16 still requires separated-insertion control with the occupation, high-Hamming and high-switch masks, a growing insertion tail, and adequate rates for boundary deconvolution. This proof estimates none of those masked traces. Balanced identification, complete deterministic offcharge comparison and higher factorial TRACE-005 remain open.

**Next concrete action:** independently audit the frozen proof, especially sampled gluing, the phase Hessian/Schur complement, and the finite-alias stationary-phase remainder. Do not rerun setup or expand the worker portfolio. No accepted-status or novelty claim is made before that review.

Reproduce finite controls using the existing activated environment:

    source /workspace/.setup/activate.sh
    python /workspace/bgs_echo_task_20261007/overlap_resume/check_overlap.py
    python -O /workspace/bgs_echo_task_20261007/overlap_resume/check_overlap.py
