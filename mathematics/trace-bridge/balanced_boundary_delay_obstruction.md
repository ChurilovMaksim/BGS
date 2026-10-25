# Infinite boundary-delay variance despite flatness, perfect mixing and reverse decay

Author proof candidate, 7 October 2026. Read-only canonical base: BGS d37c92e563d10d25bb1d6ab85bedffc1f160f773. This is an auxiliary-family obstruction to a possible proof step, not a counterexample to the actual BGS family or to the balanced CUE limit. It specifically rules out obtaining that limit from uniform second-moment bounds on unregularized one-channel boundary delays.

## Theorem

There is an explicit family V_d of odd dimensions N=5^d such that

1. V_d is unitary and |(V_d)_ij|²=1/N, so P_d=J_N exactly;
2. Q_d(i,j)=(V_d)_ij conjugate((V_d)_ji) satisfies ||Q_d||op=q_0^d→0 for a fixed q_0<1;
3. after retaining the first coordinate and closing all other coordinates with independent uniform phases, the scalar inner transfer f(z)=z h(z) has boundary angular delay

   K= f'(1)/f(1) >=0

   defined almost everywhere, but E K²=+infinity for every d>=1.

The expectation in item 3 is over the N−1 internal coordinate phases. All statements refer to literal unitary matrices, no perturbative coupling or numerical limit.

Infinite one-channel delay variance is compatible with unitary random-matrix behavior. Thus this theorem does not refute universality from items 1–2; it refutes a proposed finite-L² boundary-delay premise even under stronger-than-actual initial flatness/mixing inputs.

## 1. The explicit flat seed

Index coordinates by 0,1,2,3,4, write omega=exp(2pi i/5), and let

F_jk=omega^(jk)/sqrt(5),
P be the permutation matrix with column order (0,4,2,3,1),
V=F P,
V_d=V tensor ... tensor V  (d factors).

The first row and column of V are both constant 1/sqrt(5). Every entry has modulus 1/sqrt(5), and V is unitary. Tensoring proves item 1 in every dimension 5^d.

For Q_0(i,j)=V_ij conjugate(V_ji), every entry has modulus 1/5 and its first row and column are both constant 1/5. Therefore ||Q_0||op<=1 by the row/column Schur bound. Equality could hold only if Q_0 has rank-one phases: indeed, equality in

|(Q_0 x)_i| <= (1/5)sum_j |x_j| <= ||x||_2/sqrt(5)

for a norm-attaining unit vector forces equal |x_j| and equality in every row's triangle inequality. The constant first row and column would then force Q_0=J_5. But Q_0(1,2)=omega^(-1)/5, so this is false. Thus q_0=||Q_0||op<1. Tensor products give Q_d=Q_0^tensor(d) and item 2. A floating value q_0≈0.7932895978 is only a diagnostic; the strict inequality above is the proof.

## 2. A simple eigenvalue with a genuinely complex eigenvector

Let

A=sqrt((5+sqrt(5))/10),
B=sqrt((5-sqrt(5))/10),
lambda=B-i A,
v=(0,1,-i,i,-1)^T/2.

Direct Fourier evaluation gives Vv=lambda v. One way to see the whole spectrum is to split into even and odd coordinates under j→−j. On the odd basis (e_1−e_4)/sqrt(2), (e_2−e_3)/sqrt(2), V has matrix

i [[−A, B], [−B, −A]],

with eigenvalues lambda and −lambda^(-1). On the three-dimensional even subspace P acts identically, F²=I, and the trace is 1; the even eigenvalues are 1,1,−1. Hence

spec(V)={1,1,−1,lambda,−lambda^(-1)}.                    (1)

The number lambda is not a root of unity. Indeed x=lambda+lambda^(-1)=2B has degree four and primitive irreducible polynomial

5x^4−20x²+16.

For degree four: x²=2−2/sqrt(5) belongs to Q(sqrt(5)) but is not rational, and x does not belong to that quadratic field. If x=a+b sqrt(5), a,b rational, then ab=−1/5 and a²+5b²=2, giving a²=1±2/sqrt(5), impossible for rational a. The displayed primitive minimal polynomial is not monic, so x is not an algebraic integer. It would be one if lambda were a root of unity.

It follows from (1) that lambda^d is a simple eigenvalue of V_d. An eigenvalue of V_d has the form (−1)^(b+c) lambda^(a−b) with a+b+c+e=d. Equality to lambda^d forces d−a+b=0 because lambda is not a root of unity; hence a=d and b=c=e=0. Its normalized eigenvector is v^tensor(d). Its first coordinate is zero, its coordinates sum to zero, and its nonzero coordinates include two values with a non-real ratio (for example a ratio i).

## 3. A general regular-dark-resonance lemma

Let W be an N by N unitary whose first row and column are constant a=N^(-1/2). Partition

W=[[a,b],[c,d]],  b=a(1,...,1), c=b*.

Then d is normal, since dd*=I−cc* and d*d=I−b*b are equal. Moreover

bd=−a b,   d c=−a c.                                    (2)

Suppose d has a simple unit-modulus eigenvalue lambda_0, with normalized eigenvector u satisfying bu=0, and the coordinates of u are not all real multiples of one complex scalar. Put D(theta)=diag(exp(i theta_k)), and let lambda(theta), u(theta) be a smooth normalized continuation of that eigenpair for d D(theta). Define the leakage

ell(theta)=b D(theta)u(theta).

Unitary norm conservation gives the exact identity

1−|lambda(theta)|²=|ell(theta)|².                        (3)

At theta=0, differentiate the eigenvalue equation and apply b, using (2). The term involving lambda'_k disappears because bu=0, and one obtains

partial_k ell(0) = i lambda_0/(lambda_0+a) b_k u_k.       (4)

By the hypothesis on u, ell has real derivative of rank two. A common phase rotation theta→theta+t(1,...,1) multiplies lambda and ell by exp(it); at ell=0 it leaves the two leakage derivatives zero while changing arg(lambda) at speed one. Therefore the map

theta → (Re ell(theta), Im ell(theta), arg(lambda(theta)/lambda_0))

has rank three at zero. The ordinary inverse function theorem supplies local real coordinates (y_1,y_2,x,t), with a smooth strictly positive measure density, in which

lambda= lambda_0 sqrt(1−|y|²) exp(ix).                   (5)

The remaining coordinates t have dimension N−4. The lemma needs N>=4 and the displayed rank conditions; it does not assert a dark resonance for every flat matrix.

## 4. Scalar transfer and the divergent integral

For fixed internal phases set T=W diag(1,D), d_theta=d D, and

h(z)=a+z b D(I−z d D)^(-1)c,
f(z)=z h(z).

The unitary colligation determinant identity is

h(z)= (−1)^(N−1) det(T) det(zI−d_theta*) / det(I−z d_theta).  (6)

It follows either by block inversion of zI−T* and the unitary reciprocity identity, or by the determinant Schur complement. On a regular boundary point the angular derivative of this finite Blaschke product is

K_theta(z_0)= z_0 f'(z_0)/f(z_0)
   =1+sum_l (1−|lambda_l(theta)|²)/|1−z_0 lambda_l(theta)|²,
   |z_0|=1.                                             (7)

Eigenvalues on the unit circle correspond to cancelled factors; the formula is used almost everywhere. Every term is nonnegative. The exceptional determinant-zero set has phase measure zero because the determinant polynomial has constant coefficient 1.

Take z_0=conjugate(lambda_0). The branch (5) gives a nonnegative contribution

P(y,x)= |y|² / |1−sqrt(1−|y|²) exp(ix)|².

For |x|<=c |y|² and sufficiently small nonzero |y|, P(y,x)>=c'/|y|². Consequently

integral P(y,x)² dx d²y
  >= c'' integral_(0<rho<epsilon) rho^(-4) rho² rho d rho
  = c'' integral_0^epsilon d rho/rho
  =+infinity.                                           (8)

The additional t coordinates range over a fixed positive-volume box and the Jacobian density is bounded below. Formula (7) therefore gives E K_theta(z_0)²=infinity. Uniformity of the internal phases under common rotation implies that this boundary-delay law is independent of z_0, so the same holds at z_0=1.

For W=V_d, its compression d inherits the simple eigenvalue lambda^d and eigenvector obtained by deleting the zero first coordinate of v^tensor(d). Equations (2) hold because W is dephased flat. That eigenvector has genuinely complex coordinate ratios, so (4) has rank two. This verifies every hypothesis and proves item 3.

## 5. Exact consequence for the research strategy

The initial data max|U_ij|²=O(1/N), a singular gap for P, and ||Q||→0 do not imply finite boundary second moments for the scalar Schur delay. A route that takes r↑1, estimates h+r h' in L² there, and then returns to r=e^(−s/N) has an invalid premise in this strong auxiliary control.

The theorem does not exclude estimates retaining r<1 throughout, fractional-moment estimates, cancellations of signed boundary expressions, or the exact positive energy denominator. Nor does it refute CUE, the literal fixed-tau family, or the accepted scalar Schur reduction. The original microscopic radial limit remains open.
