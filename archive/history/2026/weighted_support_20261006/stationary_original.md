# A once-counted stationary-label residual on the pair normalization

6 October 2026. Supporting decomposition, not a new core claim. FM-021
(position_chain_mixing.md) ALREADY proves a cyclic ramp for position-index
paths of U_N. The family here consists of stationary labels of the fixed-J
V_(N,J) representation; no dictionary identifying the two families is asserted.
The accepted physical/quantum/EQ inputs and the combined selected-coefficient
assembly are the dependencies. The assembly itself awaits interface review.

## 1. Exact positive cyclic family

For z,z' in G_m put

 T(z,z')=D_m^-1 e(N[Q_m(z')-Q_m(z)]) alpha(z')conjugate(alpha(z)).

The sum over all ordered pairs is |Tr V_(N,J)^m|². Let p_m(z) be the least
period of z under S, and define the ONCE-COUNTED set

 C_m={(z,z'):z'=S^jz for some integer j}.

Cyclic relabelling gives alpha(Sz)=alpha(z) and Q_m(Sz)=Q_m(z) modulo one.
There are exactly p_m(z) distinct choices of z' for each z. Therefore

 sum_(C_m) T(z,z')=D_m^-1 sum_z p_m(z)|alpha(z)|².                    (R1)

For exact boxes, w_0²=D_m rho_m and the imaginary first-loop theorem gives
P_z²|Z_z|²=1+O_J(N^-1/2) uniformly on fixed m/N bands. Consequently R1 equals

 sum_z p_m(z)rho_m(z)+O_J(mN^-1/2 Z_m^cl).                          (R2)

EQ gives Z_m^cl=1+O(e^-cm). Proper-period points cause only an exponential
correction. If p_m(z)<m then p_m(z) divides m and is at most m/2. There are
at most C m lambda^(m/2) such points, since #Fix F^ell=#Fix S^ell.
The actual entrywise derivative lower bound in frozen_seven_cut_reduction.md
has unstable factor lambda_-=(5+sqrt(21))/2>sqrt(lambda), so uniformly
rho_m(z)<=C lambda_-^-m. It follows that

 0<=m Z_m^cl-sum_z p_m(z)rho_m(z)
                         <=C m²(sqrt(lambda)/lambda_-)^m.           (R3)

The global-versus-box normalized l2 comparison from the combined theorem,
with the multiplier p_m bounded by m, costs at most
C_J m sqrt(N)e^(-4N/5). Thus, for fixed J and m<=2N,

 sum_(C_m)T=m+O_J(mN^-1/2+m²e^-cm+m sqrt(N)e^(-4N/5)).              (R4)

Only m~N is used in the normalized conclusion. This is an alternative
coordinate-specific ramp derivation, not a new claim that a ramp alone gives
CUE or BGS.

## 2. Exact disjointness from the selected homoclinic family

Let O_m be the DISTINCT union of the cyclic orbit of d_m and its negative,
as in S9, and set

 H_m={(z,z+d):z in G_m, d in O_m}.

These ordered pairs are all distinct because O_m is a set. Moreover

 C_m intersect H_m is empty, for every m.                            (R5)

To prove it, take k0=(1/2,0) mod1. Then Sk0=k0 and k0 belongs to every G_m.
For a cyclic-pair displacement d=(S^j-I)z, pairing invariance gives

 b_m(k0,d)=b_m((S^(-j)-I)k0,z)=0 mod1.

For d=±S^j d_m, the same invariance and b_m(k0,d_m)=(k0)_q give
b_m(k0,d)=±1/2=1/2 mod1. This contradiction proves R5 without a generic-period
assumption or an approximate intersection estimate. In particular the
homoclinic coefficients controlled in S9 were not double-counting pieces of
the positive stationary cyclic family.

## 3. The remaining signed sum, exactly once counted

Define

 R_(N,m,J)=sum_((z,z') notin C_m union H_m) T(z,z').

Then the exact pair decomposition and R4/S9 imply, for w smooth and compactly
supported in (0,1/2), fixed J>=2,

 N^-2 sum_m w(m/N)(|Tr U_N^m|²-m)
       =N^-2 sum_m w(m/N) R_(N,m,J)+O_(J,w)(N^-1/2).                 (R6)

Transfer to U is only the accepted AGGREGATE norm/trace estimate; R is a
stationary-label sum for V, not an intrinsic spectral component of U.
The N-torsion sectors and nearly all noncyclic stationary pairs remain inside
this signed residual. No estimate making its right side vanish is proved.

For bands above m/N=1, the CUE pair benchmark is min(m,N), not m. The cyclic
ramp R4 persists, so the remaining signed pairs must also supply the negative
plateau correction N-m. Neither the decomposition nor the removed family
addresses that correction. Higher factorial orders remain separate.
