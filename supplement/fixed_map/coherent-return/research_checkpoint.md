# Coherent return calculation — unpublished working checkpoint

2026-09-17. Kept only in ignored build/, as requested: no commit or push
before the principal coherent Heisenberg barrier is actually closed.
That barrier is **not closed**. These are finite-dimensional identities,
a falsification example, and a conditional positive estimate. No novelty
or fixed-map BGS claim is made.

## Exact compression and screening

Let U be unitary on C^N, A=Ad_U on Hilbert–Schmidt matrices, P the
orthogonal projection onto diagonal matrices, and Q=I-P. Write

    A = [a b; c d],   a=|U_xy|^2,
    F(z)=z a+z^2 b(I-zd)^(-1)c,
    C(z)=P(I-zA)^(-1)P=(I-F(z))^(-1).

The last equality is the block inverse formula, valid for |z|<1.
The coefficient f_n of F is the amplitude of first return to P:
f_1=a, f_n=b d^(n-2)c for n>=2. This monitored-return construction is
an auxiliary operation on Liouville space, not a claimed physical
measurement of the original N-dimensional system.

Suppose U has simple eigenvalues exp(i theta_j), with normalized columns
v_j, and B_xj=|v_j(x)|^2 is invertible. Its invariant Liouville space
has dimension N, and its compression onto P is D=B B^T>0.
Then 1 is not an eigenvalue of d: a norm-preserving eigenvector of d
at 1 would be an A-fixed vector in Q, contradicting invertibility of B.
Solving the Q component of the invariant-vector equation gives

    F(1)=I,                 b(I-d)^(-1)c=I-a.                 (1)

In particular, a strong stochastic gap does not make the summed quantum
memory small. It instead makes the right side of (1) large on constants'
orthogonal complement. This is an obstruction to treating the entire
memory as a perturbation of a, not an obstruction to BGS itself.

## A phase-blind jet and the first inverse-gap term

For j!=k put w_jk(x)=v_j(x) conjugate(v_k(x)) and
mu_jk=exp(i(theta_j-theta_k)). Expansion at epsilon=1-z gives

    C(z)=D/epsilon + H0 + epsilon H1 + O(epsilon^2),
    H0=sum_(j!=k) w_jk w_jk^*/(1-mu_jk),
    H1=sum_(j!=k) w_jk w_jk^*/|1-mu_jk|^2 >= 0.

Indeed -mu/(1-mu)^2=1/|1-mu|^2 on the unit circle.
Completeness of the compressed spectral projectors gives
H0+H0^*=I-D. Inverting the Laurent expansion, without commuting
matrix factors, proves

    F'(1)=D^(-1),
    (F''(1)+F''(1)^*)/2=D^(-2)-D^(-1),
    H1=D [F''(1) D F''(1)/4 - F'''(1)/6] D.                  (2)

The two terms in the last bracket can be individually very large.
The positivity belongs to their exact difference. Taking their norms
separately destroys relevant cancellation. The anti-Hermitian part of
F'' can already depend on phases; only its Hermitian part is phase-blind.

An independent direct formula, R=(I-d)^(-1), is

    F''(1)=2 b R^3 c,       F'''(1)=6 b d R^4 c.

For N=2 the nonconstant channel has invariant weight t in (0,1),
and c0=cos(theta_1-theta_2). With a0=t+(1-t)c0,
s0=1-t+(1+t)c0, its scalar return function is

    f(z)=z(a0-s0 z+z^2)/(1-s0 z+a0 z^2).

Exactly f(1)=1, f'(1)=1/t, f''(1)=(1-t)/t^2. The third derivative
contains (1-c0)^(-1). Thus even the first two scalar derivatives at
one do not control a closing spectral gap. `two_level.wl` checks this
symbolically; these are algebraic identities, not asymptotic evidence.

## A dimension obstruction to early operator-norm contraction

Every A^j P contains the normalized identity. Therefore

    dim intersection_(j=0)^k A^(-j) Q >= (N-1)(N-k).

On this intersection d^k is isometric, so for 0<=k<=N,

    number of singular values of d^k equal to 1 >= (N-1)(N-k).

In particular ||d^k||=1 for 0<=k<N, regardless of chaos. This is a
finite-rank obstruction. It does not say that all initial states survive
with probability one, or rule out trace cancellation.

If P is cyclic for A, d is strictly stable. Averaging over unit vectors
in P, put p_n=||f_n||_HS^2/N. The survival probabilities are
s_0=1 and s_n=||d^(n-1)c||_HS^2/N for n>=1. Unitarity implies
cc^*=I-dd^*, hence telescoping gives

    sum_(k>=0) d^k cc^* d^(*k)=I_Q,
    sum_(n>=1) p_n=1,       E tau=sum_(n>=0) s_n=N.            (3)

More generally the numerator in the mean is the dimension of the
cyclic subspace. This is the known quantum Kac theorem, not a discovery:
[Bourgain, Grünbaum, Velázquez, Wilkening, Theorem 3.2](https://arxiv.org/abs/1302.7286).
Full cyclicity holds generically: distinct nonzero eigenphase differences,
invertible B, and nonzero w_jk suffice. No such hypothesis has been proved
here for the prescribed nonlinear map at all N.

## A falsification family satisfying the generic assumptions

Let G_N be the unitary discrete Fourier transform. In every neighborhood
of G_N there exist generic unitaries U_N satisfying the preceding full
cyclicity conditions. Choose ||U_N-G_N||<=epsilon_N=N^(-3).
The excluded sets have Haar measure zero, whereas each neighborhood has
positive Haar measure. This gives an existence example; the numerical
random samples are not certificates of exact nonresonance.

Since ||Ad_U-Ad_G||<=2 epsilon_N and |G_xy|^2=1/N,

    || |U_xy|^2-J || <= 2 epsilon_N,       E tau=N.             (4)

Nevertheless G_N^4=I. Spectral stability for normal matrices puts the
eigenvalues of U_N into four arcs of radius O(epsilon_N). Each arc is
microscopically narrower than 1/N. If their populations are n_r, then
the local ordered-pair count is at least

    sum_r n_r(n_r-1) >= N^2/4-N.

Thus the normalized local pair mass is at least N/4-1 and diverges.
Strong mixing and the exact Kac mean do not even imply local pair
tightness. This family is NOT a quantization of the prescribed fixed
nonlinear Anosov map, and is NOT a counterexample to that target.

There is also a sharp warning about interpreting the mean. For G_N,
(Q Ad_G)^2 P=0: its square maps diagonal matrices to diagonal matrices,
while the first-step diagonal part is the invariant constant matrix.
Telescoping the two factors for U_N gives

    Pr(tau>2)<=16 epsilon_N^2.

Combining with (3), for N>2,

    E[tau | tau>2] >= (N-2)/(16 epsilon_N^2),
    E[tau^2] >= (N-2)^2/(16 epsilon_N^2).

The mean N can be carried by an extremely rare and extremely long tail.
Large return-time fluctuations near dark states/degeneracies are already
known; see [Yin et al.](https://arxiv.org/abs/1903.03394).
The present family adapts that warning to the Liouville compression.

## Positive gap criterion, and why it is still missing

Write I_jk=sum_x |v_j(x)|^2 |v_k(x)|^2. If I_jk>=c/N for the pairs with
|theta_j-theta_k|_(circle)<=2 pi R/N, then (2) implies

    pair_mass([-R,R]) <= (4 pi^2 R^2/c) Tr(H1)/N^2.           (5)

Each such pair contributes at least c N/(4 pi^2 R^2) to Tr(H1).
This is a conditional sufficient bound, not a BGS criterion: it gives
tightness only and assumes an overlap lower bound. Neither that bound
nor Tr(H1)=O(N^2) is established here for the fixed map.

For calibration, Haar U has independent Haar eigenvectors and CUE phases.
E I_jk=1/(N+1), while its determinantal two-point density gives

    E sum_(j!=k) |1-mu_jk|^(-2)
      =sum_(m=1)^(N-1) m(N-m)=N(N^2-1)/6.

Thus E Tr(H1)=N(N-1)/6. This follows by integrating
(1-cos m theta)/(2 sin^2(theta/2)), whose circle average is m.
The unregularized observable overweights isolated exceptionally close
pairs. A deterministic uniform bound on it is stronger than the pair
limit we want; do not promote (5) to a necessary condition.

A better bounded-scale target is

    H_s=sum_(j!=k) w_jk w_jk^*/[(s/N)^2+|1-mu_jk|^2], s>0.

Let r in (0,1) solve (1-r)^2/r=(s/N)^2. Exactly

    H_s=[C(r)+C(r)^*-I]/(r^(-1)-r)-D/(s/N)^2.                (6)

Under the same overlap hypothesis,
pair_mass([-R,R]) <= (s^2+4 pi^2 R^2) Tr(H_s)/(c N^2).
The spectral proof of (6) removes all N invariant eigenmatrices, not
just the scalar identity. Without an estimate for this regularized
resolvent, the return reformulation has relocated rather than solved
the Heisenberg problem. Full CUE requires considerably more than this
positive local bound.

## Verification and next discriminating task

`return_memory.py`: direct block inverse, screening, derivative, Kac
Gramian, and exact singular-value multiplicities for N=2,3,5,8;
Fourier perturbation diagnostics N=8,16,32,64. No large-N inference.

`gap_identity.py`: independently generated Cayley unitaries, 80-decimal
arithmetic. Relative errors in (2) are below 9e-73 for N<=8. A preliminary
double-precision random N=8 example lost about five decimal places through
cancellation and failed its tolerance. Raising tolerance was not the fix:
the independent high-precision construction resolves that numerical risk.
`two_level.wl` was evaluated in Wolfram; the identities simplify exactly.

The useful next task is a bound for (6) for the actual fixed quantum map,
or an explicit non-tautological small Wiener insertion after invariant
subtraction. Classical mixing, a Kac mean, the boundary value F(1), and
the phase-blind part of its jet have all been ruled out as substitutes.
No prescribed-map Heisenberg cancellation estimate was obtained.
