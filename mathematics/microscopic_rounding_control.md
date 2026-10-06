# Microscopic rounding with simultaneous low-trace preservation

## Status, ownership and scope

Project proof, independently internally reviewed. This extends the project's
preexisting proposition “First-order Egorov alone cannot force local repulsion”
in `manuscript/unified_sections/spectral_resolution.tex`, already recorded under
“Holomorphic shell rigidity and spectral resolution” in `record/claim_ledger.md`.
Spectral rounding, its first-order Egorov stability, and its simple-spectrum
splitting are prior project work. The refinements here are simultaneous
unnormalized low-trace preservation, a definite stable-band pair witness,
and continuity of the newer position/reversal controls. No external priority
or external referee certification is claimed.

This file is the single canonical proof of this extension. The proposition
concerns an altered operator sequence, not the prescribed frozen quantization.
Deterministic BGS and the actual signed Heisenberg comparison remain open.

## 1. Exact theorem

Fix 0<c<1/2. Let U_N be any sequence of N-dimensional unitary matrices,
and specify a sequence of positive integers K_N=o(N^(1/3)). There exists
a sequence W_N of unitary matrices with simple spectrum satisfying

1. ||W_N-U_N||op=O_c(N^-1).
2. sum_(k=1)^(K_N) |Tr(W_N^k)-Tr(U_N^k)|²=o(1), with ordinary,
   unnormalized traces.
3. There is a fixed nonnegative smooth w compactly supported in (0,1/2),
   with w(c)=1, such that

   J_N,w(W_N)=N^-2 sum_(m>=1) w(m/N)(|Tr(W_N^m)|²-m)

   obeys liminf J_N,w(W_N)>=1-integral_0^(1/2) xi w(xi) dxi>1/2.

Moreover, in any specified coordinate basis, put

P_U(x,y)=|U_xy|²,  Q_U(x,y)=U_xy conjugate(U_yx),  E_N(x,y)=1/N.

Uniform O(N^-1) entry flatness, an eventual P singular contraction on
constants-perpendicular with some fixed gap, Q operator-norm decay, and
fixed-bounded-observable Egorov estimates with O(N^-1) error transfer
from U_N to W_N. More precisely, with epsilon_N=||W_N-U_N||op,

||P_W-P_U||op<=2epsilon_N,  ||Q_W-Q_U||op<=2epsilon_N,

max_xy |W_xy|<=max_xy |U_xy|+epsilon_N,

||W_N* A_N W_N-U_N* A_N U_N||op<=2||A_N||op epsilon_N.

Here * means adjoint. A gap bound rho<1 for U gives any fixed bound
rho' in (rho,1) for W eventually; identical finite-N constants are not
asserted. Any strict margin in a limsup bound is preserved.

The rounding is chosen for the specified K_N. There is no assertion of
one choice optimized simultaneously for every admissible growing window.
The theorem is eventual in N; excluded small dimensions may be assigned
arbitrary simple unitaries. It also applies along odd dimensions alone.
Negative trace indices follow by conjugation; k=0 is unchanged.

## 2. Unbiased rounding and the deterministic choice

For sufficiently large N let M=floor(cN)>=1 and h=2pi/M. In a selected
orthonormal eigenbasis of U_N choose eigenangle representatives

theta_j=h(a_j+t_j),  a_j integer, 0<=t_j<1.

Independently choose B_j in {0,1} with probability P(B_j=1)=t_j.
Let V_N have angles h(a_j+B_j), modulo 2pi, in the same eigenbasis.
Then ||V_N-U_N||op<=h and V_N^M=I for every outcome.

Set d_j=h(B_j-t_j) and

Z_j=exp(ik theta_j)(exp(ik d_j)-1).

E d_j=0 and |d_j|<=h. The inequalities
|exp(ix)-1-ix|<=x²/2 and |exp(ix)-1|<=|x| give

|E Z_j|<=k²h²/2,  Var(Z_j)<=E|Z_j|²<=k²h².

Independence of complex random variables gives

E|sum_j Z_j|²=sum_j Var(Z_j)+|sum_j E Z_j|²
             <=Nk²h²+N²k⁴h⁴/4.

Therefore one outcome satisfies, simultaneously across the whole window,

sum_(k=1)^K |Tr(V_N^k)-Tr(U_N^k)|²
 <=Nh² sum_(k=1)^K k²+(N²h⁴/4) sum_(k=1)^K k⁴.             (1)

Indeed the left side is one nonnegative random variable on a finite
probability space, so some positive-probability outcome is at most its
expectation. Coordinates with t_j=0 cause no difficulty. Bias is included
in the second term, not discarded as if centered traces were automatic.
Since h=O_c(N^-1), (1) is O_c(K³/N+K⁵/N²), hence o(1) at the stated K_N.
No effectiveness or efficient search algorithm is required for this
existence statement.

## 3. Simple spectrum without losing the window

To the selected rounded angle of index j add delta_j=j/N^4 for
j=1,...,N, and call the resulting unitary W_N. Offsets within the same
root are distinct. Distinct roots have circular separation at least h,
whereas every offset difference has magnitude less than N^-3<h
eventually. Thus no collisions occur, including across the circle seam.

The shared eigenbasis gives

||W_N-V_N||op<=N^-3,
|Tr(W_N^k)-Tr(V_N^k)|<=sum_j k delta_j<=k/N².

The l2 norm of the trace error on 1<=k<=K is bounded by
N^-2 (sum k²)^(1/2)=O(K^(3/2)/N²). Combining this with (1) by the
triangle inequality proves conclusion 2; conclusion 1 is immediate.
Degenerate eigenvalues of the original U_N do not obstruct choosing its
orthonormal eigenbasis.

## 4. A fixed stable-band failure

At m=M each unjittered lattice phase equals one, so

N^-1 Tr(W_N^M)=N^-1 sum_j exp(iM delta_j)=1+O_c(N^-2).

Choose a nonnegative smooth bump of height one at c, compactly supported
inside (0,1/2), with integral xi w(xi) dxi<1/2. Such a bump exists by
shrinking its support (one can also require 0<=w<=1).
All squared traces in the defining sum for J are nonnegative. Hence

J_N,w(W_N)
 >=w(M/N)|Tr(W_N^M)|²/N²-N^-2 sum_(m>=1) m w(m/N).

The first term tends to one since M/N tends to c. The second term is a
Riemann sum tending to integral xi w(xi) dxi. This proves conclusion 3.
There is no assumption of cancellation or control of other trace powers.
The normalization and band coincide with the project's necessary CUE
pair test in `heisenberg_pair_heat_formula.md`; its target is J_N,w→0.

## 5. Continuity of coarse coordinate and dynamical controls

For every matrix X, the Hilbert–Schmidt norm obeys

||W X W*-U X U*||HS<=2epsilon_N||X||HS.

Let D:x→diag(x), an isometry from coordinate l2 to Hilbert–Schmidt
matrices. Since P_U=D* Ad_U D with Ad_U(X)=UXU*, compression proves
the asserted P bound without an extra dimension factor.
Both P matrices are doubly stochastic, so constants reduce them and

||P_W-E_N||op<=||P_U-E_N||op+2epsilon_N.

A limsup contraction strictly below one therefore survives. For L>=1,
(P_W-E_N)^L=P_W^L-E_N supplies the corresponding power bound.
If limsup ||P_U-E_N||<=10^-64, as in FM-021, the same limsup bound holds
for W and the eventual bound 2^-L holds after enlarging its startup.

For Q use Q_U=U circ U*, with circ the entrywise product; the adjoint
here is essential, since Q uses the reversed entry. The isometry
T:e_j→e_j tensor e_j gives

T*(A tensor B)T=A circ B, so ||A circ B||op<=||A||op||B||op.

Expanding

Q_W-Q_U=(W-U) circ W*+U circ (W*-U*)

proves the asserted 2epsilon_N bound. Thus ||Q_U||op→0 implies
||Q_W||op→0. Flatness follows from the entrywise inequality in section 1:
sqrt(C/N)+O(N^-1)=O(N^-1/2).

Finally expand W*AW-U*AU as
(W*-U*)AW+U*A(W-U). This proves the conjugation bound. In particular,
if Op_N(a) is uniformly bounded for each fixed smooth symbol a and

||U_N* Op_N(a) U_N-Op_N(a composed with T)||op=O_a(N^-1),

the identical principal classical map and the same order of remainder
hold for W_N, with a possibly changed symbol-dependent constant.
No estimate uniform in growing symbol families or long times is claimed.

## 6. Application and the exact boundary

Apply the theorem to the maintained frozen sequence U_N. Choose a diverging
specified window containing the desired logarithmic range, for example
K_N=ceil(max(1,c_0)log N), where c_0 is the FM-007 time-window constant.
The FM-007 bound |Tr(U_N^k)|<=C N^(39/40) in that range survives with
additive o(1) uniformly across the window. It is not an O(1) logarithmic
bound. The separate FM-013 statement is O_k(1) for each fixed k, with
nonuniform constants and ineffective thresholds; that statement also
survives without becoming uniform for growing k.

FM-021's coarse flatness and P gap, and FM-022's Q decay, survive.
Consequently the generic cyclic, marked and reversed-path conclusions
whose proofs use only these transferred hypotheses and unitarity remain
available. No new semiclassical parametrix for W_N is asserted. Global
spectral equidistribution also transfers, since matched eigenangles move
by O(N^-1), equivalently by testing every fixed normalized trace.

Nevertheless section 4 violates a fixed necessary stable-band pair target.
Thus an implication using only these enumerated quantitative data cannot
establish the actual deterministic microscopic comparison. This is not a
statement that every result known for the actual U_N has been preserved.

The construction changes the quantum operator. It need not preserve the
exact Hamiltonian, Weyl identities, subprincipal symbol, all-order
pseudodifferential or Fourier-integral expansion, arithmetic rigidity,
or membership in a prescribed microlocal quantization class. It is not
a counterexample to BGS for the frozen family, nor a universal statement
about standard local quantization prescriptions. A successful proof may
use that additional exact-quantization information. No external novelty
claim is made.

## Source map

- Prior rounding owner: `manuscript/unified_sections/spectral_resolution.tex`,
  proposition “First-order Egorov alone cannot force local repulsion,” and
  `record/claim_ledger.md`, “Holomorphic shell rigidity and spectral resolution.”
- Inherited FM-007: `mathematics/frozen_seven_cut_reduction.md`, equation (9).
- Inherited FM-013: `mathematics/fixed_time_wavepacket_trace_bound.md`, theorem (1).
- Inherited FM-021: `mathematics/position_chain_mixing.md`, sections 1–4.
- Inherited FM-022: `mathematics/reversed_path_decay.md`, sections 1 and 4.
- Stable-band normalization: `mathematics/heisenberg_pair_heat_formula.md`, section 5.

Sections 1–5 are elementary project proof, not a numerical claim. The
inherited analytic FM theorems are inputs; this extension does not reprove
their full semiclassical dependency chains.
