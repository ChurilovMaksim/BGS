# The annealed one-pinch term disappears on positive Heisenberg bands

Research theorem candidate, 7 October 2026. Self-review and exact controls are
reported separately. This is a smaller first-loop theorem, not T16 or BGS.

## 1. Target and dependencies

For the unchanged actual odd-N U=exp(i tau N A)M, tau=10^-80, put
T=Ad(U), D=sum_c P_c T P_c, Z_theta=diag(exp(i theta_j)), V_theta=Ad(Z_theta),
A_theta=V_theta T and B_theta=V_theta D. Tr is the N^2-dimensional trace;
tr is the ordinary N-dimensional trace. Define

    E_N,m(theta)=Tr[B_theta A_theta^(m-1)],  m>=1,
    S_N(w)=N^-2 sum_m w(m/N)[E_N,m(0)-integral E_N,m(theta)dtheta].

The torus measure is normalized. It is the exact integer occupation projector;
all repeated occupations remain included. Fix any w in C_c^infinity((a,b)),
0<a<b<infinity. Its powers are m=Theta(N), with no short-word replacement.
There is no Hamming/switch mask on this one-pinch trace: it is the concrete
j=1 echo, not the full masked endpoint. All claims below state this boundary.

Two accepted inputs beyond the FM-027 exact setup are used:

1. FM-028, `mathematics/actual_charge_radial_shell.md`, Section C2, equation (C4):
   under the ordinary-Weyl embeddings, D_N converge in operator norm to a
   compact operator. In particular, for every epsilon>0 there are r_epsilon
   independent of N and operators K_N of rank <=r_epsilon with
   ||D_N-K_N||<=epsilon eventually. One can also choose ||K_N||<=2.
   This invokes only the accepted actual phase/parametrix compactness chain.
   The quasimode, radial/resolvent, Egorov, and classical-mixing parts of
   FM-028 are not inputs to L1--L2. They are used only in the separately
   labeled positive-overlap note when deriving Tr C=o(N).
2. TRACE-023, `mathematics/uniform_phase_pair_abel_bound.md`, theorem (A):
   for every unitary U, every 0<q<1, with W_theta=Z_theta U,

       sum_(k>=1) q^k integral |tr W_theta^k|^2 dtheta
          <= N(1+q)/(2(1-q)).

These inputs are accepted by the maintained `phase_trace_checkpoint.md`; old
candidate headings in the frozen proof copies do not supply a different status.
Neither input is reproved here. The derivation from them is elementary.

## 2. New bounded theorem and its signed consequence

For the actual literal family,

    N^-2 sum_m w(m/N) integral E_N,m(theta)dtheta ->0.       (L1)

Consequently the ORIGINAL occupation-subtracted first-loop functional obeys

    S_N(w)=N^-2 sum_m w(m/N)E_N,m(0)+o(1).                 (L2)

For real nonnegative w this implies liminf S_N(w)>=0. Moreover S_N(w)->0
is equivalent to vanishing of the nonnegative untwisted echo aggregate on
that band. The leading first-loop contribution cannot be canceled by its
balanced occupation subtraction. This equivalence is a reduction, not an
estimate of the remaining untwisted term.

The generic theorem behind L1 only requires uniformly finite-rank
approximation of D_N in operator norm and the exact phase ensemble. It does
not require a uniform compact embedding for V_theta D_N, classical limits
for arbitrary theta, spectral simplicity, or a rate for compactness.

## 3. Exact time-summed spectral kernel

For z on the unit circle put

    f_N(z)=sum_m w(m/N) z^(m-1).

Uniformly in x modulo 2pi, elementary summation by parts twice gives

    |f_N(exp(ix))| <= C_w N/(1+N^2 dist(x,2pi Z)^2).        (L3)

Indeed the trivial sum bound is O_w(N), while
|1-exp(ix)|^2 |f_N(exp(ix))| is at most the l1 norm of the second
difference of the sampled weight, which is O_w(N^-1). Combining the two
bounds gives L3. The weight vanishes near the sample boundaries because
its compact support lies in (a,b).

Let q_N=exp(-1/N), and P_q(x)=(1-q^2)/|1-q exp(ix)|^2.
The inequalities 1-exp(-1/N) comparable to N^-1, and
1-cos x comparable to dist(x,2pi Z)^2 on [-pi,pi], give

    |f_N(exp(ix))| <= C'_w P_(q_N)(x).                    (L4)

If exp(i lambda_alpha(theta)) are the eigenvalues of W_theta, the
adjoint eigenvalues are exp(i(lambda_alpha-lambda_beta)). Hence

    ||f_N(A_theta)||_1
       <= C'_w sum_(alpha,beta) P_(q_N)(lambda_alpha-lambda_beta).

The Poisson Fourier series gives the exact positive expression

    sum_(alpha,beta) P_q(lambda_alpha-lambda_beta)
       =N^2+2 sum_(k>=1) q^k |tr W_theta^k|^2.

After occupation-phase integration, the accepted Abel bound yields

    integral ||f_N(A_theta)||_1 dtheta
       <= C'_w [N^2+N(1+q_N)/(1-q_N)] <= C''_w N^2.       (L5)

No pointwise pair-density estimate is used. The trace norm is taken only
after complete time summation, not termwise in m.

## 4. Finite-rank/tail proof with arbitrary occupation twists retained

The left side of L1 equals

    N^-2 integral Tr[V_theta D_N f_N(A_theta)]dtheta.

Fix epsilon>0 and write D_N=K_N+R_N with rank K_N<=r_epsilon,
||K_N||<=2, and ||R_N||<=epsilon eventually. Multiplication by arbitrary
V_theta is unitary. Thus

    |Tr[V_theta K_N f_N(A_theta)]|
       <=||K_N||_1 ||f_N(A_theta)|| <=2 r_epsilon C_w N,

uniformly in theta. Trace duality and L5 give

    |N^-2 integral Tr[V_theta R_N f_N(A_theta)]dtheta|
       <=epsilon N^-2 integral ||f_N(A_theta)||_1dtheta
       <=C''_w epsilon.

Therefore the limsup of the absolute value in L1 is at most
C''_w epsilon. Let epsilon tend to zero. This proves L1; the exact
occupation identity proves L2. Twirl positivity E_N,m(theta)>=0 proves
its one-sided signed consequence when w>=0.

The identity term can be separated exactly: D_N=J_H+D_N^0,
V_theta J_H=J_H and A_theta J_H=J_H. Its contribution is
N^-2 sum_m w(m/N)=O_w(N^-1), so it causes no exception.

This is not the invalid assertion that V_theta D_N converge in one common
compact embedding uniformly in all theta. Left multiplication only preserves
a fixed finite rank and the operator norm of the remainder, which suffices.

## 5. Fixed additional consecutive pinches

The same argument gives a quantitatively scoped extension. For each fixed
j>=1 define, for m>=j,

    E_N,m^[j](theta)=Tr[B_theta^j A_theta^(m-j)].

Then its phase-averaged N^-2 compact-band aggregate tends to zero. Indeed
replace D_N in the LEFTMOST B_theta by K_N+R_N; the remaining
B_theta^(j-1) has norm <=1. The rank remains <=r_epsilon and the error norm
<=epsilon. The shifted time kernel has the same absolute spectral values
as f_N, apart from a unit-modulus factor. The bound is independent of j
as long as all sampled m>=j; hence also applies to deterministic j_N<=aN
with one block of consecutive pinches. This is NOT an arbitrary separated
j-loop theorem: separated power lengths depend on m and cannot in general
be pulled through the time sum as a fixed contraction. No unjustified
fixed-insertion/fixed-total-word identification is made.

More generally one may insert fixed-in-m contractions on either side of
D_N, even if they depend on theta and N, provided the complete time dependence
is a single adjacent A_theta power. The same proof applies.

## 6. What remains unknown for the literal signed first loop

The missing estimate is now the untwisted positive functional

    N^-2 sum_m w(m/N) (1/N)sum_b
       |tr(U_N^(m-1) Z_b U_N Z_b*)|^2 ->0                 (L6)

for every nonnegative smooth compact positive-band w. The sum includes all
b modulo N, not a fixed set of smooth modulation labels. Exact ordinary-Weyl
sine evolution and its aliases remain the action data specific to the model.

One sufficient added input is an unaveraged local spectral-pair kernel bound

    N^-2 sum_(alpha,beta) P_(exp(-1/N))(lambda_alpha-lambda_beta)=O(1).

With this bound the identical finite-rank/tail proof yields L6. This is a
microscopic local-pair upper bound, not an input supplied by flatness, FM-027,
fixed-word freeness, or the existing radial resolvent theorem. It must not be
silently assumed. The counterexample in `generic_counterexample.md` shows
that the untwisted conclusion is false under those coarse operator bounds,
even when D_N approaches its identity rank-one projection in operator norm.
