# Abel concentration and a Heisenberg-window boundary for clustered spectra

Stable claim ID: `BGS-TRACE-006`. Date: 22 September 2026.

**Status:** exact elementary finite-spectrum inequality and explicit asymptotic
counterexample, independently reconstructed at the level of the formulas below;
external priority has not been established. This note concerns abstract unitary
spectra. Its only application to a quantized map uses the *different, explicitly
compensated* family in
[compensated_heisenberg_trace_control.md](compensated_heisenberg_trace_control.md).
No mixed-resolvent estimate for the prescribed frozen map is proved here.

## Poisson-kernel lower bound

Let a unitary matrix of dimension \(D\geq2\) have eigenphases \(x_j\in\mathbb
R/\mathbb Z\). Suppose their union lies in at most \(K\) circular arcs of radius
\(0\leq\eta<1/2\). For \(s>0\), define

\[
L_D(s)=\frac1{D^2}\sum_{m\geq1}e^{-2sm/D}
\left|\sum_{j=1}^D e^{2\pi imx_j}\right|^2,
\quad J=\max(1,\lceil2D\eta\rceil).
\]

**Proposition 1.** Overlapping arcs, repeated phases, and unequal cluster
occupancies are allowed. The exact bound is

\[
L_D(s)\geq\frac{1}{2KJ}
\frac{\sinh(2s/D)}{\cosh(2s/D)-\cos(2\pi/D)}-\frac12.
\tag{A1}
\]

**Proof.** Assign each phase to one containing arc and subdivide that arc into
at most \(J\) intervals of length at most \(1/D\). If the occupancies of the
at most \(KJ\) intervals are \(b_t\), then
\(\sum_t b_t^2\geq D^2/(KJ)\). For \(q=e^{-2s/D}\), the positive Poisson kernel
satisfies

\[
P_q(2\pi x)=1+2\sum_{m\geq1}q^m\cos(2\pi mx)
=\frac{\sinh(2s/D)}{\cosh(2s/D)-\cos(2\pi x)}.
\]

Expanding the squared traces gives
\(2L_D(s)+1=D^{-2}\sum_{j,k}P_q(2\pi(x_j-x_k))\).
Within one interval the circular distance is at most \(1/D\); hence its
ordered pairs each contribute at least the fraction in (A1). All omitted
pair terms are nonnegative. This proves the assertion. \(\square\)

For each fixed \(s>0\), the fraction in (A1) equals
\(sD/(s^2+\pi^2)(1+O_s(D^{-2}))\). Since \(J\leq1+2D\eta\),

\[
K/D\longrightarrow0,\quad K\eta\longrightarrow0
\quad\Longrightarrow\quad L_D(s)\longrightarrow+\infty.
\tag{A2}
\]

The project bound for the explicitly compensated Pell family gives arcs of
radius \(\eta=\delta_N/4\), with
\(\delta_N=C_g|\epsilon|^3/N^2+D_g\epsilon^2/N^3\),
\(K=O(\log N)\), and dimension \(D=(N-1)/2\) on the inversion-odd sector.
When \(g\) is inversion-even and
\(\epsilon=o(N^{2/3}K^{-1/3})\), the existing separation/homotopy argument
gives the arc containment and (A2) applies. This is a transform consequence
of existing spectral pinning, with vanishing classical action strength.

## A simple-spectrum counterexample to a stronger inference

For integers \(K\geq3\), \(n\geq2\), set \(D=Kn\) and choose
\(0<\eta<1/(2K)\). Define the *distinct* phases

\[
x_{j,r}=\frac jK-\eta+rh,\qquad h=\frac{2\eta}{n-1},
\quad 0\leq j<K,\quad0\leq r<n.
\tag{A3}
\]

**Proposition 2.** Suppose \(K,n\to\infty\), \(K\eta\to0\), and
\(D\eta^2\to\infty\). The globally unfolded nearest-neighbour spacing
distribution converges weakly to \(\delta_0\); each \(L_D(s)\to\infty\)
for fixed \(s>0\); yet, for every fixed \(0<a<b\),

\[
\sup_{aD\leq m\leq bD}\frac{|\operatorname{Tr}U_D^m|^2}{D}
\longrightarrow0.
\tag{A4}
\]

**Proof.** Each of the \(K(n-1)\) internal unfolded gaps is
\(Dh=2K\eta n/(n-1)\to0\), while the remaining \(K\) gaps have vanishing
frequency \(1/n\). The divergence of \(L_D\) follows from (A2).
Geometric summation gives the exact factorization

\[
\operatorname{Tr}U_D^m=e^{-2\pi im\eta}
\left(\sum_{j=0}^{K-1}e^{2\pi imj/K}\right)
\left(\sum_{r=0}^{n-1}e^{2\pi imrh}\right).
\]

For \(K\nmid m\), this is zero. For \(K\mid m\), its magnitude is
\(K|\sin(\pi mnh)/\sin(\pi mh)|\). The assumptions imply
\(bDh=2bK\eta n/(n-1)\to0\). For all large \(D\), every
\(aD\leq m\leq bD\) satisfies \(0<mh\leq1/2\), so
\(\sin(\pi mh)\geq2mh\). Since the numerator is at most one,

\[
\frac{|\operatorname{Tr}U_D^m|^2}{D}
\leq\frac{K^2}{4Dm^2h^2}
\leq\frac{(n-1)^2}{16a^2Dn^2\eta^2}
\leq\frac1{16a^2D\eta^2}\longrightarrow0.
\]

The same bound holds at nonresonant times. For an explicit sequence take
\(n=K^5\), \(D=K^6\), \(\eta=K^{-2}\). \(\square\)

The spectra are also macroscopically uniform: moving every phase to its
closest \(K\)-th root changes it by at most \(\eta\), while the \(K\)-root
measure tends to Haar. Thus even simple eigenvalues, macroscopic uniformity,
spacing collapse and divergent Abel transforms cannot by themselves imply
a positive form-factor lower bound in a window bounded away from zero in
units of \(D\). The stronger hypothesis \(D\delta_N\to0\) used for the
compensated family's window estimate is not replaced by \(K\delta_N\to0\)
through a spectral clustering argument alone. This construction has not
been realized by the fixed-strength quantum map and has no bearing on its
model-specific mixed-loop hypothesis.

## Evidence, comparison and limitations

The algebraic proof is independent of numerical sampling. Finite floating
diagnostics and the exact formulas used are recorded in
[the dated attempt](../../archive/record/abel_window_research_20260922.md). That record
also distinguishes the prior close-pair theorem and the previously proved
\(D\delta_N\)-scale window theorem. These elementary inequalities are
included for their precise inference boundary, without an external novelty
or BGS universality claim.
