# Strict Hardy positivity does not identify a limiting excess

**Status:** exact abstract spectral control, author self-review. This is an
addition to the argument in [TRACE-091](hardy_spectral_remainder_20261015.md),
not a counterexample to the prescribed frozen map.

Let V_N contain all (N+1)st roots of unity except 1. Its simple spectrum has
p_N(z)=1+z+...+z^N, and Tr V_N^m=-1 unless (N+1) divides m, when it is N.
For each fixed s>0, summing those two geometric progressions gives

$$
L_N^{\mathrm{del}}(s)=\frac{1}{N^2(e^{2s/N}-1)}
+\left(1-\frac1{N^2}\right)\frac{1}{e^{2s(1+1/N)}-1}.
$$

Taylor expansion at fixed s gives

$$
L_N^{\mathrm{del}}(s)-\frac1{e^{2s}-1}
=\frac1N\left(\frac1{2s}-\frac{s}{2\sinh^2s}\right)+O_s(N^{-2}).
$$

The coefficient is strictly positive because sinh(s)>s. For every finite
N>=2 the Hardy excess is positive, since the spectrum is not an N-clock;
nevertheless it tends to zero. All fixed positive-power traces eventually
equal -1. Thus simplicity, strict positivity and bounded fixed traces do not
give the positive CUE excess required by TRACE-091. In a positive smooth
Fourier band inside (0,1), the complete signed pair defect tends to
-integral t w(t) dt, rather than zero.

The independent geometric-series check is
`computations/verification/imported_finite_controls/verify_final_attempt.py`: 116 exact
rational cases plus explicitly labelled high-precision asymptotic checks.
The source is the imported record, Sections 82-84. Its finite output proves
no assertion about U_N=exp(i*10^-80*N*A_N)M_N.
