# Egorov overlap rigidity and separation from affine quantizations

**Claim ID: BGS-FM-016. Status: PROJECT PROOF + AUTHOR CHECK.**
4 October 2026. Fixed-time normalized trace vanishing and starting-noise
ellipticity below are independent weaker derivations of consequences already
available from [FM-007](frozen_seven_cut_reduction.md), not new cancellation.
The additional scope is overlap rigidity between different quantized maps
and separation from affine quantizers after fixed classical conjugacy.
The [packet proof](fixed_time_wavepacket_trace_bound.md) now improves the
actual fixed-time input to bounded unnormalized traces. Heisenberg
cancellation remains open.

### Egorov overlap lemma

Let K_N,L_N be unitary quantizations of fixed smooth torus maps F,G.
Use Op_N(1)=I and self-adjoint Op_N(a) for real a.
Assume, for every fixed smooth a, one-step Egorov in operator norm,
K_N^* Op_N(a) K_N=Op_N(a composed with F)+o_op(1), and likewise
for L_N,G. Assume the usual torus Weyl product calculus and HS law:
Op_N(a)Op_N(b)=Op_N(ab)+o_op(1) and
N^{-1}||Op_N(a)||_HS^2 tends to integral |a|^2.
If C={x:F(x)=G(x)} has area zero, then

$$
N^{-1}\operatorname{Tr}(K_N^*L_N)\longrightarrow0,\qquad
\inf_{|\zeta|=1}N^{-1/2}\|K_N-\zeta L_N\|_{HS}
\longrightarrow\sqrt2.                        \tag{8}
$$

**Proof.** Put D_N=K_N^*L_N and t_N(c)=N^{-1}Tr(D_N Op_N(c)).
For u=a composed with F and v=a composed with G, Egorov implies
Op_N(u)D_N-D_N Op_N(v)=o_op(1). Multiply by Op_N(c), take a
cyclic trace and use the product calculus to obtain t_N(c(u-v))=o(1).
Take a_j to be the four real embedding coordinates cos(2 pi q),
sin(2 pi q), cos(2 pi p), sin(2 pi p), and set
f=sum_j(a_j composed with F-a_j composed with G)^2. Its zero set is C.
Choose a smooth chi_epsilon(f) in [0,1], equal to one near zero and
zero for f>=2 epsilon. Smooth division away from zero expresses
1-chi_epsilon(f) as a sum of c_j(a_j composed with F-a_j composed with G).
For each fixed epsilon, t_N(1-chi_epsilon(f)) tends to zero. HS
Cauchy--Schwarz now gives
limsup_N |t_N(1)|<=||chi_epsilon(f)||_L2, which tends to zero with
epsilon because C has area zero. The second assertion follows from
N^{-1}||K_N-zeta L_N||_HS^2
=2-2 Re(zeta N^{-1}Tr(K_N^*L_N)).

If F(x_0)!=G(x_0) at just one point, there is also

$$
\liminf_N\inf_{|\zeta|=1}\|K_N-\zeta L_N\|_{\rm op}\ge\sqrt2.    \tag{9}
$$

Take a torus coherent state psi_N at x_0 (a periodized Gaussian
of width N^{-1/2}) and real smooth a equal to one at F(x_0) and zero
at G(x_0). Localization and Egorov imply
||(Op(a)-I)K_N psi_N||=o(1), ||Op(a)L_N psi_N||=o(1).
Self-adjointness gives <K_N psi_N,L_N psi_N>=o(1). The squared
distance of the two unit vectors, with any relative phase, is therefore
2+o(1), uniformly in that phase. This proves (9).

### Verification for the prescribed odd-N family

Keep the original S_0=[[3,4],[2,3]], tau=10^(-80),
h=(2 pi N)^{-1}, kappa=tau/(2 pi), and the unchanged ordinary
symbol g from FM-001, including r(q+1/2) in its p-dependent term.
Here N is the full odd dimension of the frozen model, not N_p.
The exact matrix identity is A_N=Op_N(g).
Fourier truncation proves the product and HS laws above: fixed finite
sets have no aliasing for large N, Weyl product phases tend to one,
and smooth Fourier tails are bounded in operator norm by their l^1 norms.
The Weyl-product sine expansion also gives, for fixed smooth a,

$$
[\operatorname{Op}_N(a),\operatorname{Op}_N(g)]
=ih\operatorname{Op}_N(\{a,g\})+O_{\rm op}(h^2).
$$

Duhamel's formula for the fixed time kappa yields
Q_N^* Op_N(a) Q_N=Op_N(a composed with Phi_g^{-kappa})+O_op(h),
where Q_N=exp(i kappa Op_N(g)/h). The maintained cat matrix has
exact midpoint Egorov in direction S_0^{-1}. Its raw-to-midpoint
signs agree for odd N because S_0 is the identity modulo two. Hence

$$
U_N^*\operatorname{Op}_N(a)U_N
=\operatorname{Op}_N(a\circ F_\tau)+O_{\rm op}(h),\qquad
F_\tau=\Phi_g^{-\kappa}\circ S_0^{-1}.
$$

Iteration gives Egorov for each fixed integer power. This needs no
regularized plane trace formula or even-N restriction.

The four points {0,1/2}^2 are equilibria of g and fixed by S_0.
Their exact Hessians are diag(b_x,0), with

$$
\frac{b_x}{\pi^2}\in
\left\{-\frac{19606}{125},-\frac{19594}{125},
\frac{24306}{125},\frac{24894}{125}\right\}.
$$

Thus Tr D(S_0 composed with Phi_g^kappa)(x)=6-4 kappa b_x.
These four values are distinct and greater than two at the prescribed
nonzero kappa. For any fixed integer j!=0, the four derivative traces
of F_tau^j remain distinct: t is sent to
2 cosh(|j| arcosh(t/2)), strictly increasing for t>2.
A C^1 conjugacy preserves fixed-point derivative traces, whereas an
affine map has the same derivative everywhere. Therefore F_tau^j
cannot be C^1-conjugate to any affine torus map. Only the four-point
calculation, not the full FM-001 centralizer theorem, is used here.

In particular the analytic map F_tau^j differs from the identity.
Its coincidence set with the identity has area zero, since the
nonzero analytic sum of squared embedding-coordinate differences has
an area-zero zero set. Equation (8), with L_N=I, proves

$$
N^{-1}\operatorname{Tr}U_N^j\longrightarrow0
\quad\hbox{for every fixed integer }j\ne0.      \tag{10}
$$

This implies the standard macroscopic uniform eigenphase law, without
a microscopic conclusion or a rate uniform in j.

For any fixed smooth symplectic H with an Egorov unitary quantizer W_N,
and any fixed affine symplectic L with quantizer M_{L,N}, equation (9)
applies to W_N U_N^j W_N^* and M_{L,N}. If H is analytic, their
distinct analytic maps have an area-zero coincidence set, so the
HS limit (8) holds as well. Arbitrary N-dependent spectral conjugating
matrices are outside these fixed-classical-coordinate statements.

### A closed input for the auxiliary quadratic noise

For the project's centered quadratic noise
X=i[G,U_N G U_N^*]/sqrt(2)-its mean, with normalized GUE G,
the exact FLOW-003 covariance inequality, for traceless Hermitian T, is

$$
\frac{1-|m_2|}{N}\operatorname{Tr}T^2
\le\mathbb E(\operatorname{Tr}XT)^2
\le\frac{2+|m_2|}{N}\operatorname{Tr}T^2,\qquad
m_2=N^{-1}\operatorname{Tr}U_N^2.
$$

Equation (10) therefore proves uniform asymptotic ellipticity for the
actual starting family: covariance condition number <=2+o(1), whitening
operator norm <=1+o(1). A rank-two covariance correction can remain;
this is not complete GUE covariance or deterministic noise removal.

The stronger FM-013 estimate |Tr U_N^j|=O_j(1) is proved in the separate
[packet construction](fixed_time_wavepacket_trace_bound.md). Its historical
Faure action-phase adaptation, stochastic relaxation, deterministic noise
removal and the signed Heisenberg hierarchy remain separate obligations.


## Prior scope and verification boundary

The physical symbol and four Hessians are reused FM-001 inputs. Fixed
integer powers retain distinct derivative traces; only fixed smooth
classical conjugators with Egorov quantizers are covered. The HS assertion
requires an analytic conjugator to control its coincidence set. Arbitrary
N-dependent spectral conjugating matrices are outside the result.
The shared checker replays finite Weyl dictionaries and the four Hessians;
it does not certify the full asymptotic proof. No Lean compilation,
external referee or new priority is asserted.
