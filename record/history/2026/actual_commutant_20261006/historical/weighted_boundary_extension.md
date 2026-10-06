# Weighted leading-boundary compatibility in characteristic zero

Extension of interior_transfer_algebra.md. The earlier file is frozen for independent review. Same canonical base d4132ccee82849b644520d88c953cb9b33382a59; no canonical writes. This extension is self-reviewed and needs its own independent audit.

## Result and exact boundary

For every odd N divisible by49, let L=N/7, let B be the matrix retaining only the actual upper Jacobi bonds of 1000 A_N along its seven paths, and let G=sqrt(N) M_N be the actual metaplectic kernel. Then the complex common commutant of B and G is scalar.

Equivalently, let D normalize those upper bonds so D^(-1) B D=J_L tensor I_7. The complex common commutant of J_L tensor I_7 and D^(-1) G D is scalar. **Both matrices are transformed.** This closes the upper-bond-weighted Jordan surrogate, not the actual pair (A_N,M_N). The actual diagonal and lower bonds have not been discarded in the target; they are absent only in this explicitly named surrogate. No 5-adic residue or lifting conclusion follows merely from this characteristic-zero result.

## 1. Leading coefficient from the last seven boundary equations

Write a commuter with J as upper block-Toeplitz, with blocks C_0,...,C_(L-1). In the last depth row, the first seven column equations read

[C_0, Etilde_s] = sum_(d=1)^s Etilde_(s-d) C_d,  s=0,...,6.

Here Etilde_s=D_(L-1)^(-1) E_(0,s) D_s is a nonzero scalar multiple of u_s v_s^T, where

u_s=D_(L-1)^(-1) f_(4+2s),
v_s^T=f_(s+3)^T D_s,
f_b(j)=w^(bj), w=exp(2 pi i/7).

The seven u_s are a basis. Apply its s-th dual row to the displayed equation. All terms on the right are annihilated, since they have column factors u_0,...,u_(s-1). It follows that

v_s^T C_0=lambda_s v_s^T.

At s=0, commuting with the rank-one u_0 v_0^T also implies C_0 u_0=lambda_0 u_0. Thus if v_s^T u_0 is nonzero for every s, all lambda_s equal lambda_0. The actual-weight Casoratian lemma in the frozen note proves that the seven v_s are independent. Therefore C_0 is scalar.

This argument makes no assumption that C_0 already commutes with each rank-one block. It uses the coupled equations to produce the left eigenvectors.

## 2. Uniform overlap nonvanishing for L>=21

The actual upper bond at depth u-1 on chain j is

b_(u,j)=(-3-4i) r((u+jL)/N),
r(q)=(1-cos(14 pi q))(1+cos(2 pi q)).

By the definition D_(t+1,j)=D_(t,j)/b_(t+1,j), with D_(0,j)=1,

D_(s,j)/D_(L-1,j)=product_(u=s+1)^(L-1) b_(u,j).

The (-3-4i) factors and the factors 1-cos(14 pi u/N) are independent of j and nonzero in this range. Consequently v_s^T u_0 is a nonzero chain-independent factor times

sum_(j=0)^6 w^(sj) W_j,
W_j=product_(u=s+1)^(L-1) [1+cos(2 pi(j/7+u/N))].

Every W_j is strictly positive. Put m=L-1-s. For every x in (0,1/7), elementary trigonometry gives

cos²(pi(1/7+x))/cos²(pi x) <= a=cos²(pi/7),
cos²(pi(5/7+x))/cos²(pi(6/7+x)) <= a,

and for j=2,3,4,

cos²(pi(j/7+x)) <= b min{cos²(pi x),cos²(pi(6/7+x))},
b=cos²(2pi/7)/cos²(pi/7).

The first ratio decreases with x; the second follows by x ->1/7-x. For the middle three, the numerator is at most cos²(2pi/7), while both denominator candidates are at least cos²(pi/7). Multiplying the inequalities over the m factors yields

W_1<=a^m W_0, W_5<=a^m W_6,
W_j<=b^m min(W_0,W_6), j=2,3,4.

Hence the five remaining terms have total absolute value at most

[a^m+(3/2)b^m](W_0+W_6).

The two leading terms satisfy

|W_0+w^(6s)W_6| >= cos(3pi/7)(W_0+W_6) > (W_0+W_6)/5.

Indeed their smaller angular separation is at most6pi/7; for nonnegative A,B, |A+e^(i theta)B| >= cos(theta/2)(A+B) when 0<=theta<=pi.

Use the explicit rational bounds

a<5/6, b<1/2, cos(3pi/7)>1/5.

Since L>=21 and s<=6, m>=14, and

(5/6)^14 + 3/2^15 < 1/5.

Thus the five-term remainder is strictly smaller than the leading pair, proving v_s^T u_0 nonzero for all s=0,...,6.

For completeness, the trig bounds need no decimal computation. Since pi>31/10 and cos x<=1-x²/2+x^4/24 for x in [0,1],

cos²(pi/7) < [1-(31/70)²/2+(31/70)^4/24]² < 9/11 <5/6.

For a>=1/2, b=(2a-1)²/a=4a-4+1/a is increasing, so

b<4(9/11)-4+11/9=49/99<1/2.

Finally cos(3pi/7)=sin(pi/14)>sin(3/14)>=3/14-(3/14)^3/6>1/5. Every displayed rational comparison is checked with fractions in weighted_boundary_bounds.py.

## 3. Higher tails and finite base

Once C_0 is scalar, the frozen note's minimal-tail argument applies to the gauge-normalized kernel. For the smallest nonzero C_d, either d<=L-7, when the proven seven-row weighted Casoratian isolates and kills C_d, or d>=7, when seven consecutive bottom rows have independent Fourier right factors at depth zero and kill it. These cases cover every d when L>=13. The allowed L>7 are odd multiples of7, so L>=21.

At L=7, N49, weighted_surrogate_base.py uses the actual b_(u,j) and G to form D^(-1) G D over F_197 with primitive49th root16. The full 343-dimensional Toeplitz centralizer map X -> [X,D^(-1) G D] has rank342. Its nonzero minor lifts through the cyclotomic reduction (all internal b_(u,j) are nonzero in this field). The scalar identity gives the remaining dimension. Therefore the N49 complex common commutant is scalar too. This is an exact finite base, not a conjectured extrapolation.

The larger-N overlap proof cannot include N49 unchanged: three overlap factors vanish exactly there, as recorded in the frozen note. The finite base explicitly handles that exception. Factors of5 and arbitrarily high powers of7 cause no omission in the characteristic-zero proof.

## 4. Remaining actual-model implication

The upper-bond truncation theorem does not imply scalar common commutant of A_N and M_N. A commuting operator for A_N need not commute separately with its upper, diagonal, and lower pieces. One must prove a simultaneous filtered degeneration statement, with the actual G gauge and all correction terms controlled, or find a different way of separating those pieces inside the generated algebra.

The independent review's new 5-adic Casoratian-unit check, once verified, would strengthen only that row-independence leaf. The positive-weight overlap argument here is archimedean and does not prove its overlaps are units at5. Neither the scalar characteristic-zero truncated commutant nor a nonzero complex overlap can silently be used as the needed residue statement. The actual all-N target and BGS remain open.
