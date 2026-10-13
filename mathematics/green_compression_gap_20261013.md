# Green compression and shrinking stopped intensity gaps

**Stable claim:** BGS-TRACE-077. **State:** PROJECT PROOF + INDEPENDENT
INTERNAL RECONSTRUCTION, 13 October 2026. The probability statement below
is unconditional for a stopped prefix. It does not estimate the probability
of reaching that prefix without an entry exit, or prove BGS.

Dependencies: TRACE-073 C3--C6 only (fresh-phase noise and Schatten
smoothness); TRACE-074 for the higher-step singular comparison. FM-021
is used only for the actual-map initial conditions, not for the abstract
unitary theorem. No reversal conclusion from TRACE-073 is inherited.
[Independent reconstruction and finite execution](../evidence/executions/20261013/green-compression/README.md).

## 1. Exact classical identity

For a doubly stochastic P of size n let Q_n=I_n-J_n, J_n=11*/n.
Assume I-P is invertible on the constant-orthogonal space and define
G(P)=(I-P+J_n)^(-1)-J_n and M(P)=G(P)-Q_n.
If rho=||P-J_n||op<1 then M=sum_{h>=1}(P-J_n)^h.

For a retained set A of size u and deleted set D, assume I-P_DD
invertible and define P^c=P_AA+P_AD(I-P_DD)^(-1)P_DA. Then

G(P^c)=Q_u G(P)_AA Q_u,
M(P^c)=Q_u M(P)_AA Q_u.                                      (G1)

For b on A with sum b=0, set full b=(b,0). The full solution
x=G(P)full b obeys (I-P)x=full b and has mean zero.
Its D row gives x_D=(I-P_DD)^(-1)P_DA x_A. Its A row therefore
gives (I-P^c)x_A=b. Center x_A to obtain G(P^c)b. This proves
the first identity on the zero-sum space and on constants.
Existence of the reduced inverse is part of the conclusion: a vector
in the kernel of I-P^c lifts to a vector in the kernel of I-P by
y_D=(I-P_DD)^(-1)P_DA y_A. The latter kernel consists of constants.
Thus I-P^c is invertible on its zero-sum space. For a nonnegative
substochastic block P_DD, invertibility implies spectral radius less
than one by Perron theory, so its geometric inverse is nonnegative.
The block row/column equations give both stochastic sums of P^c.
The second identity follows because Q_u(Q_n)_AA Q_u=Q_u.
No symmetry, normality or commuting blocks have been used.

On original N coordinates, let H_A be the vectors supported in A
whose coordinate sum is zero, and let Q_A be its orthogonal projection.
For nested retained sets, Q_A Q_B=Q_A if A is a subset of B.
Embedding all zero-sum operators by zero padding turns (G1) into
M(P^c)=Q_A M(P) Q_A.

## 2. Initial entry control

Let S_N be any deterministic unitary, P_N=|S_N|^2,
max P_N<=C0/N with fixed C0>=1, and
rho_N=||P_N-J_N||op<=1/5. Then ||M_N||op<=1/4.
For h>=2 the doubly stochastic singular bound is

|(P_N^h-J_N)_ij|
 <=rho_N^(h-2)
 sqrt[(sum_k P_ik^2-1/N)(sum_k P_kj^2-1/N)]
 <=rho_N^(h-2)(C0-1)/N.

Indeed (P^h-J)=(P-J)(P-J)^(h-2)(P-J) and the outer row/column
Euclidean norms give the first inequality. The h=1 entries have
absolute value at most C0/N. Thus

max_ij |(M_N)_ij|<=B/N,
B=C0+(C0-1)/(1-rho_N).                                      (G2)

Every centered retained compression has operator norm at most
min(1/4,Bu/N), by the submatrix row/column sum bound and orthogonal
projection contraction.

## 3. Quantum increment in Green coordinates

At size v remove a port chosen predictably from the past and use a
fresh independent uniform circle phase. For S=[[A,c],[b,a]],
d=1-|a|^2, q=w/(1-aw), the effective scattering matrix is A+c q b.
The new intensity P' is doubly stochastic and

P'=P^c+Xi, E(Xi|past,chosen port)=0,
Xi 1=0, 1*Xi=0, ||Xi||op<=8 delta_v,                         (G3)

where delta_v=max P_v and delta_v<=1/4.
These follow by expanding the intensity:
Xi=q C+conjugate(q)conjugate(C)
 +(abs(q)^2-1/d)|c|^2|b|^2,
C=diag(c)conjugate(A)diag(b).
Unitarity gives ||C||<=delta_v,
|| |c|^2|b|^2 ||<=delta_v d,
|q|<=1/(1-sqrt(delta_v)), and
|abs(q)^2-1/d|d<=2/(1-sqrt(delta_v)).

Put ell=log(2N), fix K>0 and an integer m<N with m>=32K ell
and C0<=K ell. Stop at the first entry crossing
delta_u>K ell/u or Green crossing ||M_u||op>1/2,
including simultaneous crossings and their full new states.
Before a transition ||G^c||op<=3/2 by (G1).
Since delta_v<=1/32, Neumann on the zero-sum space guarantees the
new Green inverse exists even at this first crossing and ||G'||op<=3.
The exact noncommuting inverse expansion is

G'=G^c+G^c Xi G^c+G^c Xi G^c Xi G'.                         (G4)

Write L_v=G^c Xi G^c and D_v=G^c Xi G^c Xi G'.
Then E L_v=0, ||L_v||op<=18 delta_v,
and ||D_v||op<=432 delta_v^2.
Embed them in the original N coordinate space, setting both increments
to zero after the stop. The L_v are adapted martingale differences, with predictable
coefficients and stop mask; D_v are bounded adapted remainders.
Neither increment is assumed predictable. A randomized choice of port
is revealed before the fresh phase and included in the conditioning
sigma-algebra. Failure of the Green inverse may be included in the
Green stopping rule; the preceding Neumann argument excludes a first
such failure before or at the entry exit.

Up to and including the crossing, nested projections telescope:

M_u=Q_u M_N Q_u+Q_u Z_u Q_u+Q_u B_u Q_u,
Z_u=sum_{v>u} L_v, B_u=sum_{v>u} D_v.                       (G5)

Z_u is an ordinary N by N matrix martingale in chronological
elimination time. Future projections do not occur inside its summands.
The projection Q_u is applied only afterward in the pathwise bound
||Q_u Z_u Q_u||op<=||Z_u||op.
This remains valid for adapted coordinate choices: retained zero-sum
spaces are nested along each path and the chosen port is predictable.
There is no averaging of iterated nonlinear conditional means.

## 4. Quantitative prefix theorem

For even p>=2 the unnormalized Schatten norm has the smoothness bound

||X+Y||_p^2<=||X||_p^2+D(||X||_p^2)[Y]+(p-1)||Y||_p^2.       (G6)

It is the internally derived r=0 case of C6 in the maintained
Schur censoring proof. For completeness, on Hermitian matrices
differentiate Tr(X+tY)^p twice, bound each trace word by Schatten
Holder, differentiate its 2/p power and drop the nonpositive squared
first derivative. The second derivative is at most
2(p-1)||Y||_p^2. Hermitian dilation transfers the bound to arbitrary
complex matrices; integrating gives (G6).

Applying (G6) and the conditional mean-zero property yields

E||Z_m||_p^2
 <=324 N^(2/p)(p-1)K^2 ell^2/m.

The norm of a martingale is a nonnegative scalar submartingale.
Doob's L2 inequality and ||Z||op<=||Z||_p give

P(max_{N>=u>=m}||Z_u||op>eta)
 <=1296 N^(2/p)(p-1)K^2 ell^2/(m eta^2).                    (G7)

The complete remainder has norm at most

beta=432K^2 ell^2/m,                                       (G8)

using sum_{v=m+1}^N v^(-2)<=1/m.
If eta+beta<1/4, the complementary event of (G7) prevents a
Green crossing before, or simultaneously with, an entry crossing:
at any proposed first such state (G5) has norm at most
1/4+eta+beta<1/2, a contradiction.

Let tau_delta be the first entry crossing, or infinity if none occurs
before m. Outside the exceptional probability in (G7), every state
through that first entry crossing has a well-defined Green matrix and

||M_u||op<=min(1/4,Bu/N)+eta+beta.                           (G9)

If h_u=Bu/N+eta+beta<1, then R_u=P_u-J_u
=M_u(I+M_u)^(-1) on the zero-sum space, so

rho_u<=h_u/(1-h_u).                                        (G10)

This is an unconditional probability statement about a stopped prefix.
It is not P(all-time flatness), not a probability conditioned on a
future flatness event, and not a claim about later states after the stop.

## 5. Shrinking gap and the third-step forcing

Fix kappa>0. Set p=2ceil ell, m=ceil ell^(7+kappa),
eta=ell^(-2), and b_N=floor(N/ell^2). For sufficiently large N the
hypotheses above hold and the exceptional probability is O_K(ell^(-kappa)).
Simultaneously at all pre-entry-crossing sizes m<=u<=b_N,

rho_u=O_{C0,K}(ell^(-2)), rho_u ell->0.

At these old, admissible states, the correct higher-step bound gives

(P_u^3)_ij<=1/u+rho_u(delta_u-1/u)
          <=[1+O_{C0,K}(ell^(-1))]/u.                        (G11)

The last conclusion is not asserted at the entry-crossing state if its
entry condition already fails. The actual maintained fixed-coupling map
has max P_N=O(1/N) and eventually rho_N<=1/5 by FM-021.
Thus its randomized fresh-phase feedback has this stopped estimate.
It does not supply the probability of reaching b_N without an entry
crossing, sustained two-step concentration, a scalar microscopic law,
signed TRACE-005 or BGS.

## 6. Prior structures and verification boundary

Group inverses of finite Markov chains and stochastic complementation
are classical; see the limited [primary-source comparison](../literature/green_compression_prior_structures_20261013.md). The centered block
identity is proved here rather than attributed to an unread theorem.
Schatten smoothness is also a standard mathematical structure. No priority verdict is asserted.
The proposed mechanism is their combination into a genuinely adapted
Green martingale with a depth-decaying initial term.

Four exact rational nonnormal compressions (including singleton and no
deletion), one ordered resolvent check, two rejected algebraic mutations
and four complex-double adaptive unitary steps are reproducible via
`computations/verification/green_compression.py`. They are finite controls,
not proofs of the analytic asymptotic bounds. No new Lean kernel, C++
certificate or external referee certification is asserted. The frozen
reviewed candidate and report are preserved; the maintained proof corrects
the martingale terminology and makes the reduced inverse argument explicit.
