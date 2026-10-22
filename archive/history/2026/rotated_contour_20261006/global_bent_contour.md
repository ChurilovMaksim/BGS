# Global bent contour and summed tail for the actual path integrals

Author candidate, 6 October 2026. Base f285ba510732edd9ee3679b12316df9b12e0dfcb.
This is a new continuation file. No frozen source or canonical repository
file is changed. It depends on the exact Gaussian reciprocity identity,
which is under separate review. This candidate also needs independent review.

## 1. Claimed constructive result and its boundary

Fix a finite WKB order J. In each global Fresnel integral of
exact_gaussian_reciprocity.md (G6-G7), use its UNIQUE actual real stationary
point x*_(r,nu). Define the compact contour box

C_(r,nu)={x*_(r,nu)+(1-i)u : u in [-1,1]^m},

with the product orientation, and retain the FULL nonlinear phase and
finite-J amplitude. Put

S_(N,m,J)= e(3mN/8) N^(m/2)/8^m
 sum_(r in {0,1,2,3}^m) sum_(nu mod B_m)
 integral_(C_(r,nu)) e(N[Phi_r(tau,x)+nu.x]) A_r(x) dx.    (C1)

For every fixed 0<b<8pi/(5 log 7), uniformly for 1<=m<=bN,

|Tr V_(N,J)^m-S_(N,m,J)|
 <=C_(J,b) sqrt(N) exp[-(8pi/5-b log7)N].              (C2)

In particular, for every m<=2N, the right side is at most
C_J sqrt(N) exp(-4N/5). Combining with the separately proved one-step
operator telescoping gives

Tr U_N^m=S_(N,m,J)+O_J(N^(3/2-J))+O_J(sqrt(N)e^(-4N/5))
                                                         (C3)
uniformly for 1<=m<=2N. Negative traces use complex conjugation.

This is a uniform signed representation by EXACT rotated-box integrals,
not by their first-loop approximations. Each box is the one in the local
theorem with scaled radius rho=sqrt(2), after the normalization in section 6.
The local O(N^-1/2) relative first-loop error still cannot be summed absolutely
over exponentially many boxes. No CUE value is established.

## 2. A literal complex-strip certificate at tau=10^-80

The actual symbol has sum |c_(k,l)|<=52, |k|<=9, |l|<=1 and
|k|+|l|<=10. On the complex symbol strip |Im q|,|Im p|<=9/4,

|partial^d g|<=52 exp(45pi) 63^d, d=0,1,2,3.

Using pi<22/7, e<11/4 and 45pi<142 gives the explicit upper bounds

|g|<10^66,  max|partial²g|<10^70,
max|partial³g|<10^72.                                (C4)

Consequently B=10^73 bounds the characteristic vector field
(-g_p,g_q)/(2pi) and its first two induced max-norm derivatives on that
strip. Since B tau=10^-7, its complex flow for 0<=t<=tau moves by at most
2*10^-7, its first derivative differs from identity by at most 2*10^-7,
and its second derivative is bounded by 4*10^-7. These follow from the
integral equation and the first two variational equations, using
exp(3Btau)<2.

For endpoint variables |Im x|,|Im y|<=2, the initial momentum is
(y+r-3a)/4. The characteristic projection x=X_t(a,p_0(a,y)) differs from
a by at most 2*10^-7, and its a-derivative differs from one by at most
2*10^-7. Solving for a by contraction in a 4*10^-7 neighbourhood of x
therefore stays strictly inside the symbol strip of width 9/4. This gives
a holomorphic inverse uniformly over all real translates and r=0,1,2,3.
The first two implicit-derivative formulas bound the resulting momentum's
endpoint derivatives through order two by 100. For example a_y=-X_y/X_a;
second derivatives differentiate this formula, with denominator bounded
below by 1-2*10^-7 and numerators controlled by the flow estimates.

Differentiating S_t=g(x,p)/(2pi) through two endpoint derivatives now gives
max |partial_(x,y)^2 S_t|<=10^76. Hence, on the entire endpoint strip
|Im x|,|Im y|<=2,

max |partial²(S_r(tau)-S_r(0))|<=10^-4.               (C5)

The constant is deliberately loose: each composite second derivative has
at most a fixed handful of terms bounded by 10^70*(1+100)^2 or by a
first derivative of g times 100, all well below 10^76.

Thus the CYCLIC nonlinear phase has a symmetric matrix E of entrywise
Hessian suprema, supported on neighbours, with row sums at most 4*10^-4.
We use the weaker epsilon=1/10 in the contour proof. This includes m=1,2
with repeated derivatives combined correctly.

The leading amplitude solves a scalar transport with coefficient
(g_xp+g_pp S_xx)/(4pi), bounded by 10^73 on these complex characteristics.
Its modulus is at most exp(10^-7)<3/2, and on real points it is positive.
Every fixed finite collection of higher transport amplitudes is holomorphic
and uniformly bounded on a slightly reduced neighbourhood containing the
closed endpoint strip of width 2. This follows inductively from the finite
analytic transport equations, leaving the margin to width 9/4.
Therefore, for each fixed J and all sufficiently large N,

sup_(|Im x|,|Im y|<=2)
 |sum_(ell=0)^J N^-ell a_(r,ell)(tau,x,y)|<=2.         (C6)

No bound uniform in J is asserted. The startup threshold can depend on J.
All these statements are uniform over real translates: the coefficients
and phase corrections have their exact four-periodic gluing.

## 3. A global M-matrix damping inequality

Fix a lifted class and translate its actual stationary point to zero.
The phase can be written

Psi(z)=Psi(0)-(1/2)z^T K_0 z+q(z),
K_0=B_m/4=I+(1/4)L_cycle,
q(0)=0, grad q(0)=0.

Here q is real on real coordinates and holomorphic on |Im z_j|<=2.
Its Hessian entrywise-supremum matrix E is symmetric and has row sums
<=epsilon=1/10, by (C5). Subtracting the stationary affine terms does not
change that Hessian bound.

Let f(u)=clip(u,-1,1) coordinatewise and z(u)=u-i f(u). Since f is
nondecreasing,

u^T K_0 f(u)
 =sum_j u_j f(u_j)+(1/4)sum_edges (u_j-u_k)(f(u_j)-f(u_k))
 >=sum_j min(u_j²,|u_j|).                            (C7)

To bound the nonlinear term, integrate its gradient along the vertical
segment u-i s f(u), and use grad q(0)=0. Symmetry of E and the elementary
rearrangement inequality

(a-b)(min(a,1)-min(b,1))>=0, a,b>=0,

show
sum_ij E_ij |f(u_i)||u_j|<=epsilon sum_j |u_j||f(u_j)|,
and the same estimate holds with |u_j| replaced by |f(u_j)|.
Therefore

|Im q(u-i f(u))|<=2epsilon sum_j min(u_j²,|u_j|).

Together with (C7),

Im(Psi(z(u))-Psi(0)) >=(4/5)sum_j min(u_j²,|u_j|).    (C8)

This is a GLOBAL bound on R^m, not a Taylor estimate on a small real box.
It uses the exact small complex Hessian and the cyclic quadratic M-matrix.
The same inequality with a factor s holds on u-i s f(u), 0<=s<=1.

## 4. Legitimate deformation of the Abel/Fresnel integral

Start with the exact regularization in (G7), with positive Gaussian damping.
Use the holomorphic regulator exp(-pi eta sum_j(z_j+d_j)^2), where d is
the real displacement between the cat center and actual stationary point.
For eta>0, the real integral is absolutely convergent, as are all bounded
imaginary contour translates. Piecewise linear coordinate contours can be
deformed from the real axes by Cauchy's theorem. At finite eta the Gaussian
regulator dominates their at-most-linear growth at real infinity; boundary
faces tend to zero. Equivalently, apply the product-contour argument on
finite boxes and then increase the boxes. Corners have measure zero.

On the final graph z(u)=u-i f(u), (C8) supplies an integrable bound
independent of eta near zero. The regulator has modulus at most
exp(pi eta m), and tends pointwise to one. Thus dominated convergence
removes eta for each finite m,N and identifies the original Abel integral
with the integral on this global bent contour. No compact analytic cutoff
or cancellation of unidentified real-chart side faces is assumed.

The product Jacobian has modulus at most 2^(m/2). Within [-1,1]^m the
contour is exactly x*+(1-i)u, the desired rotated box. Outside it, (C8)
and (C6) give the explicit tail bound in the next section.

## 5. Summing the tail WITH the branch and winding counts

Set c=8pi/5 and define

I_N=integral_R exp[-cN min(u²,|u|)]du
 <=sqrt(5/(8N)) +(5/(4pi N))exp(-cN),
J_N=integral_(|u|>1) exp[-cN |u|]du
 =(5/(4pi N))exp(-cN).

For ONE global class, the absolute contour tail is at most

m *2^m *2^(m/2) J_N I_N^(m-1),                       (C9)

where 2^m is the amplitude bound (C6), and 2^(m/2) is the Jacobian bound.
The exact trace prefactor is N^(m/2)/8^m. There are 4^m branches and
D_m<=6^m winding representatives. Thus the TOTAL trace tail is at most

m N^(m/2) (6 sqrt(2))^m J_N I_N^(m-1).               (C10)

Indeed 4^m*6^m/8^m=3^m, which multiplies the amplitude and Jacobian factors.
Write I_N<=sqrt(5/(8N))(1+eta_N), with
eta_N=O(N^-1/2 exp(-cN)). Formula (C10) becomes

<=C (m/sqrt(N)) (3sqrt(5))^m exp(-cN)(1+eta_N)^m.

For m<=bN, the last factor is bounded. Since 3sqrt(5)<7, this proves (C2).
For m<=2N, pi>3 and log7<2 give c-2log7>4/5, proving the simple bound
stated in section 1. The factor sqrt(N) is retained.

There is no claim for every compact Heisenberg band from this particular
radius-one estimate. The exact reciprocity formula remains valid at all m;
(C2) has the explicit bandwidth restriction shown. A larger certified strip
or a different signed tail argument would be needed to extend this bound.

## 6. Relation to the accepted local theorem and the remaining signed task

On the retained box put y=sqrt(2/h)u. Then
z=(1-i)u=exp(-i pi/4)sqrt(h)y and |y_j|<=sqrt(2)/sqrt(h).
The actual quadratic Hessian is K=-Psi''(0). After factoring the stationary
phase, leading amplitude and FULL Gaussian determinant, the box integral
contains P_G(B_h) Z_(m,h), not merely Z_(m,h), where G=K^-1.

The local theorem applies at this radius using the stronger direct complex
Hessian estimate (C5), rather than relying only on a small-radius Taylor
majorant. The nonlinear phase Hessian differs from its value at the saddle
by at most twice the small bound in (C5); the log-amplitude Hessian contributes
only O(h) after scaling. The finite tilt family therefore still has the
strict diagonal dominance required in the corrected local proof. The
analytic endpoint strip of width 2 contains the complex radius sqrt(2)
needed for its Taylor remainders.

Even with this identification, replacing each exact Z by exp(h ell_1)
has only an algebraic relative error. The exponentially numerous saddle
weights prevent absolute summation of that error at m~N. Therefore (C3)
closes a GLOBAL REPRESENTATION/Tail subproblem, while leaving the complete
signed comparison among these exact local integrals OPEN.

For fixed factorial order and compact Fourier weights whose block sums
satisfy |n_B|<=2N, the trace table in (C3) can be inserted into the exact
Möbius transform. Its operator error is O(N^(k-J-1/2)); its additional tail
error is polynomial times exp(-4N/5). This is a representation reduction,
not a CUE evaluation. Other compact supports retain the all-band exact
Gaussian-operator representation of the earlier note.

## Verification boundary

check_bent_contour_constants.py checks the rational symbol majorants,
B tau, epsilon, and the conservative m<=2N exponential margin. It does not
certify the analytic flow, Cauchy deformation or signed trace law. Those
are the written author arguments above. Independent review is required
before promoting this candidate.
