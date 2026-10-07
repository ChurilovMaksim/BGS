# Actual radial resolvent equivalence at every vanishing switch scale

Addendum candidate to actual_radial_shell.md (SHA256 43319ca5c799fd6e10479fca71e8c8fa5d7783dcd38b7493e48bba11218de37a), 7 October 2026. Its only additional inputs are elementary spectral calculus and the Neumann series. Actual fixed tau, all odd N, no arbitrary occupation-phase uniformity.

On the centered space set T=T_N, D=D_N, z=1-delta_N, L=zT+delta_N D, with 0<delta_N->0. Assuming C1/C6 of the companion:

    sup_(|xi|>=1) delta_N ||D(xi-zT)^(-1)|| ->0,
    sup_(|xi|>=1) delta_N ||(xi-zT)^(-1)D|| ->0.             (R1)

Indeed choose epsilon_N=sqrt(delta_N), and let E be T's spectral projection onto the angular arc of radius epsilon_N about xi/|xi|. On E, the resolvent norm is at most 1/delta_N and ||DE||, ||ED|| tend to zero uniformly by C1 and its adjoint. On I-E, elementary unit-circle geometry bounds the resolvent norm by C/epsilon_N for |xi|>=1 and z>=1/2. Hence each quantity in R1 is at most o(1)+C sqrt(delta_N).

Factor exactly

    xi-L = [I-delta_N D(xi-zT)^(-1)](xi-zT).

The inverse factor exists by R1 for every |xi|>=1 eventually, uniformly. Thus

    sup_(|xi|>=1) delta_N ||(xi-L)^(-1)-(xi-zT)^(-1)|| ->0.  (R2)

This explicitly handles nonnormal L; no spectral-radius-to-resolvent or power-norm inference is made. In fact the stronger relative bound holds pointwise uniformly:

    ||(xi-L)^(-1)-(xi-zT)^(-1)||
       <= o(1) ||(xi-zT)^(-1)||.                           (R3)

The unit-circle worst resolvent scale is consequently sharp:

    delta_N sup_(|xi|=1) ||(xi-L)^(-1)|| ->1,
    inf_(|xi|=1) sigma_min(xi-L) /delta_N ->1.              (R4)

For the upper bound use R2 and ||(xi-zT)^(-1)||<=1/delta_N. For the lower bound choose xi equal to any eigenvalue of T|H_N^0, where the normal resolvent norm is exactly 1/delta_N, and use R2. Centered dimension is nonzero for N>=3. Thus R4 is both a spectral and a pseudospectral boundary-scale obstruction to enhanced-dissipation closure for this particular actual transfer.

## Non-closure remains explicit

R2 is an operator-norm statement. Taking an unnormalized trace costs dimension N^2; at delta=A log N/N the resulting error bound is still too large for T16. The unknown signed occupation subtraction, its high-Hamming extraction, and correlations at scale 1/N are not controlled. R2 is not a proof that the trace defect vanishes, nor a theorem about the actual operator after removing the switch regulator. The scalar radially contracted unitary zT carries the original unknown eigenphase differences exactly, which explains the surviving difficulty.
