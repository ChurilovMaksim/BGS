# Exact two-step drift and a three-step coherence bound

Candidate, 12 October 2026. This is a one-step theorem for an arbitrary
unitary input. No all-time flatness probability or BGS limit is asserted.

Let S be u-by-u unitary, P=|S|^2, K=P^2, delta=max P<1.
Fix distinct live labels i,j. Pick a coordinate e uniformly among all u,
and an independent uniform w on the circle. If e=i or e=j, freeze K_ij.
Otherwise eliminate e by S'_(kl)=S_kl+q S_ke S_el on survivors,
q=w/(1-S_ee w), and set K'_ij=(|S'|^2)^2_ij.

For e outside {i,j}, k!=e, write
a=S_ee, d=1-|a|^2,
A=S_ie S_ek conj(S_ik), B=P_ie P_ek,
C=S_ke S_ej conj(S_kj), D=P_ke P_ej.
The exact circle moments are E q=E q^2=0,
E|q|^2=1/d, E(q|q|^2)=conj(a)/d^2,
E|q|^4=(1+|a|^2)/d^3.
Thus

E_w[P'_ik P'_kj]
= P_ik P_kj +(P_ik D+P_kj B)/d
 +2 Re(A conj(C))/d
 +2 Re(conj(a)(A D+C B))/d^2
 +(1+|a|^2)BD/d^3.

Summing k!=e and then e outside {i,j}, dividing by u, and subtracting K_ij
gives its exact expected increment. In particular,

u E[K'_ij-K_ij | S]
 <= -(1-c(delta)) K_ij + 2 delta P_ij + dcoef(delta) (P^3)_ij,

c(delta)=2delta/(1-delta)^2+delta(1+delta)/(1-delta)^3,
dcoef(delta)=4/(1-delta)+2delta/(1-delta)^2.

For delta<=1/16, c(delta)<1/2 and dcoef(delta)<5, so

E[K'_ij-K_ij | S]
 <= [-K_ij/2+5(P^3)_ij+2delta P_ij]/u.

Proof of the nontrivial coherence estimate:
A conj(C) = T_(e,k) conj(T_(k,e)),
T_(e,k)=S_ie S_ek S_kj.
The index set D={(e,k):e notin {i,j},k!=e} need not be swap invariant.
Nevertheless each of sum_D |T_(e,k)|^2 and sum_D |T_(k,e)|^2
is at most (P^3)_ij. Weighted Cauchy--Schwarz, using 1/d_e<=1/(1-delta),
therefore bounds the entire weighted coherent sum in absolute value by
(P^3)_ij/(1-delta). This is a bound on the complete coherent sum, not
on each contribution individually.

The base loss sums to -K_ij+P_ii P_ij+P_ij P_jj <=-K_ij+2delta P_ij.
The two positive quadratic terms sum to at most 2(P^3)_ij/(1-delta).
For the nonzero-a cubic phase terms, factor
sqrt(P_ee P_ke)<=delta in |a A D|, then use
sqrt(P_ie P_ek P_ik P_ke)<=[P_ie P_ek+P_ik P_ke]/2.
After summing e,k,
sum_D |a A D| <= delta [K_ij+(P^3)_ij]/2.
Likewise factor sqrt(P_ee P_ek)<=delta in |a C B| and use
sqrt(P_ke P_ej P_kj P_ek)<=[P_ke P_ej+P_kj P_ek]/2.
This gives the same bound for sum_D |a C B|.
The quartic term is bounded by
delta(1+delta)K_ij/(1-delta)^3, since
sum_(k!=e)P_ek P_ke<=(P^2)_ee<=delta.
These prove the displayed inequality with no future conditioning.

The positive companion from the reviewed unitary obstruction is
(P^3)_ij <=1/u+rho(delta-1/u), rho=||P-J_u||op.
Thus the same estimate becomes

E[K'_ij-K_ij | S]
 <= -K_ij/(2u)+5/u^2+5rho(delta-1/u)/u+2delta P_ij/u.

For logarithmic flatness and rho log u bounded, this shows a restoring
mean drift for peaks K_ij much larger than 1/u. It does not give higher
moments, stopped-path concentration, all-time flatness, or prove that
rho log u is bounded for the maintained model.

At the exact witnesses of TRACE-074, P_ij=0,
K_ij=1/b~log u/u and (P^3)_ij=(1+o(1))/u.
The right side is negative for all sufficiently large u: the static
two-step peak has a rigorously restoring one-step mean drift under this
fresh random elimination. This does not imply its probability of decay,
absence of other peaks, or evolution along the maintained initial map.
