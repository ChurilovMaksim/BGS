# One explicit eventual constant for the unchanged actual family

This is a corollary of the global scalar theorem plus the already maintained FM-021 proof, not a new quantum-map estimate. The threshold remains noneffective.

In `/workspace/shared/BGS/mathematics/fixed-map/position_chain_mixing.md`, Section 2, the maintained actual kernel is

U_jk=e(3N/8) N^(-1/2)/2 sum_(r=0)^3 exp(2pi i N S_r) a_r + O(N^(-3/2)),

uniformly in grid indices, with |a_r-1|<2*10^(-66) at tau=10^(-80). Therefore

limsup_(odd N->infinity) N max_jk |U_jk|^2
 <=4(1+2*10^(-66))^2<5.

Consequently C=5 is valid eventually. The same source proves the eventual singular-gap bound rho=1/2. The theorem in report.md can therefore use

K=1+sqrt(5-1)/(1-1/2)=5,
c=1/(2K^2)=1/50.

For every sufficiently large odd N, and every strict centered scalar disk field, the **unchanged actual** bare bosonic action obeys

S_(U_N)(Z)>= (1/50) sum_j -log(1-|z_j|^2).

No numerical value of the startup N_0 follows, no small odd dimension is silently removed from an exact identity, and no full SUSY tail or universality conclusion is inferred. The abstract theorem still applies at any finite dimension where its explicit C,rho bounds are independently verified.
