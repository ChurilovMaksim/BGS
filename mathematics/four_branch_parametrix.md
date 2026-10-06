# Exact raw metaplectic branches and direct discrete WKB construction

Pinned base: `0ffb20cc152d0ddd2620887e46d21d1120b95fd8`.

Scope: U_N(t)=exp(itN A_N)M_N, odd N, with precisely the ordinary symbol g reproduced in `fixed_map_path_model.md`. This is a direct difference-equation construction, not an appeal to an unspecified FIO theorem. No repository files changed.

Write e(z)=exp(2 pi i z), h=1/N, and g(x,p)=sum c_{k,l} e(kx+lp), where l belongs to {-1,0,1}. The exact ordinary matrix action on a periodic sampled function is
A_N u(x)=sum c_{k,l} e(k(x+hl/2)) u(x+hl).
Indeed (-1)^(kl) e_N(k(x_index+inv2*l))=e(k(x+hl/2)) for odd N. Thus there is no replacement of the raw quantizer.

## 1. Exact initial identity
For every integer j,k and odd N,
M_{jk}= e(3N/8)/(2 sqrt(N)) sum_{r=0}^3 e(N S_r^0(j/N,k/N)),
S_r^0(x,y)=-(3x^2-2x(y+r)+3(y+r)^2)/8.
Proof: put t=j-3k. The sum after removing e(-P/(8N)), P=3j^2-2jk+3k^2, is the Gauss sum
sum_{r mod4} e((-3Nr^2+2tr)/8)=2 e((-3N+3Nt^2)/8).
Complete the square modulo8; an odd number is its own inverse modulo8, and sum_{r mod4}e(ar^2/8)=2e(a/8) for odd a. Since P-3t^2=16jk-24k^2 is divisible by8, multiplying by e(3N/8) gives e(NP/8). If inv8=(1+mN)/8, m=-N modulo8, this equals exactly the missing modular phase e(-mP/8).

## 2. Evolved phases and amplitudes
Solve the real Hamilton-Jacobi equation
S_{r,t}=g(x,S_{r,x})/(2pi), S_r(0)=S_r^0.
For a sufficiently small fixed time interval, the characteristic projection is a diffeomorphism, uniformly in r and (x,y) in bounded fundamental charts. The symbol is a fixed trigonometric polynomial, so phases are real analytic. The classical characteristics are the Hamilton flow of -g/(2pi); no orientation is inferred from the usual opposite-sign Schrodinger convention.

The following phase identities hold by uniqueness:
S_{r+4}(t,x,y)-S_r(t,x,y)=x-3y-3r-6,
S_r(t,x+1,y)-S_{r-3}(t,x,y)=-2r-2y+3.
Their initial identities are polynomial calculations, and their x-derivatives differ by integers or zero, making g unchanged. Similarly S_r(t,x,y+1)=S_{r+1}(t,x,y). Consequently the sum of four branches is exactly periodic on the sampling lattice, including the cyclic x=N-1 to x=0 transition. Individual branches need not be periodic.

Use the following explicit two-amplitude construction (which removes the historical ambiguity in the index L):

V_{jk}(t)=e(3N/8) sqrt(h)/2 sum_{r=0}^3 e(S_r(t,x,y)/h)[a_{r,0}(t,x,y)+h a_{r,1}(t,x,y)].

For a smooth amplitude a, after factoring e(S/h), let P_n a be the coefficient of h^n in

sum_{k,l} c_{kl} e(kx+l S_x)
 exp(2pi i[(S(x+hl)-S(x))/h−l S_x]+pi i k l h) a(x+hl).

The bracket is smooth at h=0 by the integral Taylor formula. Thus P_0 a=g(x,S_x)a and each P_n is an explicitly determined finite differential operator. Set D_n=i P_n for n>=1. Direct expansion gives

D_1 a=(g_p/(2pi))a_x+(g_xp+g_pp S_xx)a/(4pi).

Solve the scalar transport equations

(partial_t−D_1)a_0=0,     a_0(0)=1,
(partial_t−D_1)a_1=D_2 a_0,     a_1(0)=0.

The leading h^-1 term cancels by HJ. The orders h^0 and h^1 cancel by these two equations. The remaining factored residual is O(h²), with all required finite derivatives bounded uniformly on the fixed time interval and enlarged fundamental charts. Including the sqrt(h) kernel prefactor, this is entrywise O(h^(5/2)). These transports preserve the amplitude gluing identities by uniqueness, since all symbol derivatives are periodic in the phase gradient. Thus the finite-shift equation is respected even across lattice wraparound.

The elementary matrix bound ||R||op<=N max|R_jk| gives a residual operator norm O(h^(3/2)). At time zero the exact Gauss identity and initial amplitudes give V_N(0)=M_N. Duhamel and unitarity of E_N(t) therefore give

||U_N(t)−V_N(t)||op=O(h^(3/2)),

uniformly on the fixed time interval. In particular this bounds every error entry. No norm estimate for V_N itself or infinite-dimensional parametrix is required.

Therefore U has four branches of size O(N^-1/2) and an entrywise error O(N^-3/2), with smooth amplitudes having N-uniform derivative bounds. The product Q_jk=U_jk conjugate(U_kj) has 16 terms of size N^-1 and phases S_r(x,y)-S_s(y,x), plus entrywise O(N^-2) and hence operator norm O(N^-1). Constants may depend on the fixed nonzero t, but not on N.

## 3. Distinct norm obligation
A finite branch expansion alone does not prove ||Q||op tends to zero. Every branch-pair mixed derivative must be shown nonidentically zero at t=10^-80, and a lattice oscillatory estimate must handle sampling aliases. Those are separate claims, established in Section 4 and `reversed_path_decay.md`. In particular a first nonzero Taylor coefficient without a quantitative radius/remainder is insufficient at a specified t.

## 4. Quantitative specified-time certificate (reconstructed)
The symbol's nonzero Fourier modes have |(k,l)|<10 and sum |c_kl|<=52 (the constant coefficient vanishes after centering). Thus every coordinate derivative of order m<=4 is bounded by 52*63^m<10^9. Taking B=10^12 safely bounds the sup norm and multilinear derivative operator norms through order3 of the characteristic vector field (-g_p,g_x)/(2pi).

Take T=10^-20. The characteristic flow, parameterized initially by (a,y) with p0=(y+r-3a)/4, has first derivative norm at most exp(BT)<2, second derivative at most 2BT<2*10^-8, and third derivative at most 4BT<4*10^-8. These bounds follow by differentiating its ODE and integrating the variational equations; replacing each coefficient by B leaves the second bound BT exp(3BT) and the third bound BT exp(4BT)(1+3BT exp(2BT)), both below the displayed bounds. The initial linear parameter map has operator norm1 in the max norm. Moreover its x-projection derivative with respect to a differs from1 by at most2BT. The implicit inverse therefore has derivatives through order3 bounded by100, and the resulting p(t,x,y)=S_x has all derivatives of orders1 through3 bounded by10^4. These deliberately loose inverse/composition bounds follow directly from the first three implicit differentiation identities, with denominator X_a>=1-2*10^-8 and every numerator bounded by the flow estimates. The estimates are uniform on real (x,y) because the vector field and its derivatives are periodic and bounded.

Differentiate the HJ equation once in time, with p=S_x:

S_tt=[g_p(x,p)g_x(x,p)+g_p(x,p)^2 p_x]/(4pi²).

Here is a count-independent conservative C² bound. Every derivative of p through order three is at most10⁴. For any derivative H of g of order one, each composite derivative through order two of H(x,p(x,y)) is bounded by 5*10¹⁷: the largest terms have one third derivative of g, bounded10⁹, and two first derivatives of (x,p), each bounded1+10⁴; second-derivative terms are smaller. Hence its weighted C² norm (the sum of absolute coordinate derivatives divided by multi-index factorials, which is submultiplicative) is at most10¹⁹. The corresponding norm of p_x is at most10⁵. The product formula above is therefore bounded by 10³⁸+10⁴³ before division by4pi². In particular10⁵⁰ bounds every C² derivative of S_tt. This bound does not depend on r, x or y.

Taylor's integral remainder now gives

||S(t)−S(0)−t g(x,S_x(0))/(2pi)||C² <= (10⁵⁰/2)t².

The phase correction S_r(t)-S_r(0) is4-periodic separately in x and y: the initial x+4 phase difference has x-derivative -3, and the initial y+4 phase difference has x-derivative1, so the differences remain unchanged by HJ uniqueness. Therefore its antisymmetrized correction has an ordinary Fourier series on [0,4]^2.

For Phi_rs=S_r(t,x,y)-S_s(t,y,x), the coefficient of the first time derivative of mixed derivative Phi_xy at frequency (25/4,1/4) has magnitude pi/128, independent of r,s. Indeed B(q)=r(q+1/2)/100 has coefficient B_7=1/200; the unswapped g term supplies e(r/4-alpha/(2pi))/(800pi), and multiplication by -(2pi)^2*(25/4)*(1/4) gives 25pi/3200=pi/128. No swapped or p-independent term has that frequency. The base Phi_rs(0) is separable.

The normalized Fourier coefficient remainder is bounded by10^50 t^2, so at t=10^-80 it is at most10^-110, while the linear term has magnitude (pi/128)10^-80. Hence Phi_rs,xy is not identically zero for every r,s at the prescribed positive time. This is a quantitative specified-time statement, not merely an unspecified sufficiently-small-time conclusion.

## 5. Uniform upper bound needed by the discrete lemma

At t=0, the mixed derivative of each antisymmetric phase vanishes. The mixed derivative of g(x,(y+r−3x)/4)/(2pi) is a fixed linear combination of g_xp and g_pp with coefficients of magnitude below1, so the antisymmetrized derivative is bounded by2*10⁹. Section4 then gives

sup |Phi_rs,xy(t)| <=2*10⁹ |t|+10⁵⁰t²<1/4 at t=10⁻⁸⁰.

The small upper bound is essential to exclude sampling aliases. Nonzero analytic mixed derivative alone would not give that exclusion at arbitrary fixed phases. All constants used for a local lower bound may depend on this fixed physical tau; no uniform rate as tau tends to zero is claimed.

## Dependency boundary

The finite-shift identity and symbol are reproduced in `fixed_map_path_model.md`. This construction uses analytic ODE existence, a monotone global characteristic projection, finite Taylor expansions and unitary Duhamel; it does not import a continuous FIO theorem. For global existence of the graph at each fixed y, X_a>=1−2*10⁻⁸>0 and X(a,y)−a is bounded. Thus X is strictly increasing and onto the real line; its inverse is globally defined and analytic. Bounds and gluing are then uniform on the finitely many required charts.

## 6. Shared alias-safe discrete norm lemma

Here is the elementary local lemma with the normalization made explicit.
On a rectangle let a_N be a smooth supported amplitude with uniform C²
bounds. Suppose the real smooth phase phi satisfies either
c<=phi_xy<=C<1/4 or −C<=phi_xy<=−c, where c>0. Set

(T_N)_(ij)=N^-1 a_N(i/N,j/N)e(N phi(i/N,j/N)).

Then ||T_N||²<=C_a,phi,c log(2N)/N. The support rectangle may be slightly
enlarged without changing the hypotheses.

Proof. For two supported rows x=i/N, x'=i'/N put d=|x−x'| and
psi(y)=phi(x,y)−phi(x',y). If d>0, psi_y has constant sign and magnitude
between cd and Cd. The discrete phase increments

Delta_j=N[psi((j+1)/N)−psi(j/N)]

have those same bounds. Their magnitude is less than1/2, so they remain
at distance at least cd from every integer. Also their total variation
on the supported column interval is O(d), since psi_yy=O(d).
Discrete summation by parts, applied with reciprocal denominator
(e(Delta_j)−1)^-1, bounds the weighted unnormalized oscillatory sum by
O(1/d): endpoint terms and amplitude variation cost O(1/d), and the
variation of the reciprocal denominator is O(d)/d²=O(1/d).
Thus (TT*)_ii=O(N^-1), whereas for i!=i',

|(TT*)_(ii')| <= C/(N²d)=C/(N|i−i'|).

Schur's row and column estimates give the stated logarithmic bound.
Negative mixed derivative follows by complex conjugation. In particular,
all nonzero integer sampling aliases, not only the zero alias, have been
excluded explicitly.

The same consequence holds for a real-analytic phase with nonidentically-zero mixed derivative and global bound sup|phi_xy|<1/4. Remove an arbitrarily small smooth neighborhood of its area-zero zero set and the chart boundary. The removed N^-1-amplitude kernel is small in **unnormalized** Hilbert–Schmidt norm, whose square is N^-2 sum|a|², and this norm dominates the operator norm. The remaining compact set has a finite smooth rectangular partition, to which the lemma applies. First take N to infinity, then shrink the removed neighborhood. Thus its operator norm is o(1). All constants can depend on the fixed tau and cutoff; no effective decay rate or tau-uniform estimate is asserted.
