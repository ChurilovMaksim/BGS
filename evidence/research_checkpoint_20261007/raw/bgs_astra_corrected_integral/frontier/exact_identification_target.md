# Exact remaining identification term after the source bounds

7 October 2026. Author derivation and finite diagnostic; this note is not part of the independent acceptance of the three analytic source files. The literal BGS family is unchanged, with tau=10^-80 and odd N. No generic-gap universality conclusion is made.

## 1. The hook covariance that must still be estimated

Let lambda_(m,k)=(m-k,1^k), with 0<=k<=min(m-1,N-1), and put

M_(m;k,l)(U)=E_D[s_lambda(m,k)(DU) conjugate(s_lambda(m,l)(DU))].

The elementary Newton/hook character identity gives the exact formula

B_N(m)=sum_(k,l) (-1)^(k+l) M_(m;k,l)(U).                       (I1)

For Haar unitary matrices the hook characters are orthonormal, so M is the identity and the sum is min(m,N). For the phase orbit of the actual U_N, the remaining Abel identification is exactly

N^-2 sum_(m>=1) exp(-2sm/N)
  sum_(k,l) (-1)^(k+l)[M_(m;k,l)(U_N)-delta_kl] -> 0,            (I2)

for each s>0, equivalently with the existing complete compact-test bridge. The new uniform source estimates bound the complete expression and supply normal-family compactness. They do not establish (I2).

Here is an explicit first mixed representation entry whose Heisenberg-scale aggregate has no bound supplied by the actual P/Q/charge gaps:

M_(m;0,1)=E_D[h_m(DU) conjugate(h_(m-1)(DU) Tr(DU)-h_m(DU))],    (I3)

for m>=2. It mixes the symmetric-power sector with the next hook and retains all torus-weight multiplicities. There is no assertion that this entry alone has to vanish, or that bounding it alone would suffice: the required quantity is the full signed double sum (I2). Classical P and reverse Q determine selected path contractions, and the accepted charge/Hamming results remove other specific projectors; none is an estimate of this complete growing-degree cross-hook covariance or its remaining signed combination. Replacing the weight-block trace product by a Hilbert-Schmidt norm loses these terms.

## 2. Cheap exact discriminator

Take the auxiliary flat unitary, not the BGS operator,

U_ij=5^(-1/2) zeta_5^(sigma(i)j),  sigma=(0,1,3,2,4), i,j=0,...,4.

It has P=J exactly. Direct exact cyclotomic computation gives

Re M_(4;0,1)=3 sqrt(5)/625 !=0,
B_5(4)=(2365+48 sqrt(5))/625.

Thus a perfect classical gap does not make the mixed hook block vanish identically. This is a finite algebraic discriminator, not an asymptotic counterexample to the actual phase law. The independently printed floating reverse norm is about 0.79329 at this one dimension; no asymptotic reverse-gap theorem is inferred from it.

check_hook_covariance.py uses exact arithmetic in Z[zeta_5], divided by 5^m only at scalar-product time. It computes complete source coefficients through m=6 from principal minors and the complete-symmetric recurrence. check_frontier_direct.py separately checks m=2,3,4 by enumerating all rooted closed words and all repeated-index permanents. Those direct checks pass and distinguish an implementation error from a nonzero mixed representation term.

## 3. A mandatory large compact sector and why absolute-sector estimation fails

There is an especially concrete obstruction to controlling the completed integral sector by sector. Choose the circle w_i wbar_i coefficient at every one of the N sites in the compact functional. The fermionic body determinant contributes its top coefficient (cd)^N |det U|^2=(cd)^N. Therefore this single compact sector, after the matched-source operation ab partial_c partial_d at q=ab=cd, is

T_top,N(q)=N^2 q^N Z_B,U(q),
Z_B,U(q)=E_D |det(I-sqrt(q) DU)|^-2.                            (I4)

The pure-boson compact identity identifies the same Z_B as the circle integral of det(I-q U Z U* Z*)^-1. Formula (I4) is exact at every finite N and 0<q<1.

Even in the Haar comparison itself, character orthogonality gives E_Haar Z_B,U(q)=1/(1-q). Hence at q=exp(-2s/N),

E_Haar T_top,N(q) ~ N^3 exp(-2s)/(2s),

whereas the complete Haar pair observable is

q(1-q^N)/(1-q)^2 ~ N^2(1-exp(-2s))/(4s^2).

Thus the top compact sector is not an o(N^2) error even in the target comparison ensemble. Its N^3 scale has to cancel with other numerator/fermion sectors before taking an absolute value. This is an obstruction to that absolute-sector method, not a universality obstruction. The independently proved full-source bounds control the already-completed sum and do not assign a bound to Z_B at zero numerator source.

The exact Ward factorization G_U=1+(a-c)(b-d)H_U, coming from one-sided holomorphic phase averaging, removes the artificial large derivative factors before reorganizing source coefficients. Its hook expansion returns (I1)-(I3); it does not make the mixed covariance disappear. This is the finite-N cancellation location at which actual model-specific information must enter.

## 4. Stopping condition for this checkpoint

The exact corrected finite-N identity, complete microscopic source regularity, and uniform integrability have passed independent internal review. The signed high-degree identification (I2) has not. No step from actual P/Q/charge gaps to (I2) is asserted. The compact centering candidate is separately labeled and is not a prerequisite for the accepted checkpoint. Further exploratory branches are deferred under the user's latest instruction to finish the checked checkpoint before the next work wave.
