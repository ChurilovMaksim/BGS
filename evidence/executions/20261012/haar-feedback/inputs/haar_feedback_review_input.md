# Haar feedback, an exact delay law and an entropy-stable clock class

Candidate for independent internal reconstruction, 12 October 2026.
Base: BGS main 6bd6c3129b0b69eeb4ec5243a7e6e2eba75865f7.
No priority, deterministic-map transfer or BGS claim is made. Haar-compatible
Schur projections and the Cauchy/Cayley description are prior: Bourgade,
Najnudel and Nikeghbali, arXiv:1102.2633v1, introduction and Proposition 3.2.
All formulas below are derived internally rather than taken from an abstract.

## 1. Exact finite-dimensional factorization

Let U be Haar on U(N), retain a fixed set R of u labels, and eliminate its
q=N-u complementary labels E with arbitrary fixed unit-modulus feedback
phases. Start the matrix inner function F_N(z)=zU, with incoming delay I.
After reordering R first, absorb those phases into eliminated rows of U:
V=diag(I_u,W_E)U. This is still Haar, also conditional on any independently
chosen complete phase vector and coordinate order. For this paragraph u
and the complete phase/order realization are fixed, not adaptively selected.

Write V in R,E blocks and set

 X(z)=(I_q-zV_EE)^(-1) zV_ER,
 F_u(z)=zV_RR+zV_RE X(z),
 X=X(1), S=F_u(1), T=S*F_u'(1), Q=STS*.

All inverses used here exist almost surely. In particular V has no
eigenvalue 1 almost surely. For a unitary V, a vector fixed by V_EE would
give a vector supported on E fixed by V, so I_q-V_EE is then invertible.
For u=N take X to be the empty matrix and T=I_N.

For 1<=u<N the exact joint law is

 S is Haar on U(u), independent of T;
 T=I_u+X*X, with density of X on C^(q by u)

       c_(q,u) det(I_u+X*X)^(-(N+u)) dX.             (1)

The law of T is invariant under unitary conjugation. Q has the same law
and is also independent of S, although the joint pair (T,Q) need not be
independent of S. None of these statements asserts independence across u.

Proof of the delay identity. On z=e^(i theta), the colligation equation is
zV[I;X(z)]=[F_u(z);X(z)]. Differentiate in theta and multiply on the left
by [F_u(z)*,X(z)*]. The terms X* dot X cancel, giving
-i F_u(z)* dot F_u(z)=I+X(z)*X(z). At theta=0 this is T=I+X*X.

Proof of the density. Define the Hermitian Cayley variable

 C=i(I+V)(I-V)^(-1)=[A B*; B D],
 V=(C-iI)(C+iI)^(-1).

The Haar density in C is proportional to det(I+C^2)^(-N) dC.
This follows directly from the differential: the left translated tangent
is -i V* dV=2(C-iI)^(-1) dC (C+iI)^(-1).
The real Jacobian of Hermitian congruence H -> L H L* in dimension n
is |det L|^(2n). To see this, reduce L to its positive singular values;
each diagonal real coordinate contributes s_j^2 and each off-diagonal
complex coordinate contributes s_j^2 s_k^2. The total is product s_j^(2n).
The harmless factor 2^(N^2) is absorbed into normalization.

The equation V[I;X]=[S;X], multiplied by C+iI, gives

 S=(A-iI)(A+iI)^(-1),  X=B(A+iI)^(-1).              (2)

Put G=I_q+XX* and introduce a Hermitian Y by

 B=X(A+iI),  D=XAX*+G^(1/2) Y G^(1/2).             (3)

This is a globally bijective smooth change of variables (A,X,Y) -> (A,B,D).
Its block triangular real Jacobian is

       det(I_u+A^2)^q det(G)^q.                    (4)

The first factor is the complex rectangular right-multiplication
Jacobian; the second is Hermitian congruence in dimension q.
No derivative of the X-dependent square root adds a determinant factor,
because the full derivative is block triangular in these variables.

The Schur determinant of I+iC is

 det(I+iC)=det(I+iA) det(G+i(D-XAX*))
          =det(I+iA) det(G) det(I+iY).              (5)

Here B(I+iA)^(-1)B*=X(I-iA)X*; no noncommuting
replacement of G+iD by a scalar expression is made.
Combining the conjugate of (5), the original density, and (4) gives

 det(I+A^2)^(-u) det(G)^(-(N+u))
                       det(I+Y^2)^(-N) dA dX dY.  (6)

All three factors have finite positive integrals: their product integrates
to the original finite probability mass, and each integral is positive,
so Tonelli excludes an infinite one. Thus A and X are independent.
The A factor is precisely the Haar Cayley density in dimension u.
Equation (2) proves (1), Haar preservation and the stated independence.
Right invariance of the X density gives conjugation invariance of T;
conditioning on S then proves the assertions about Q.

## 2. Exact inverse-Jacobi spectrum and first moment

Equivalently, let G_0 be q-by-u and Y_0 be 2u-by-u independent standard
complex Gaussian matrices, with entries density exp(-|g|^2)/pi. Then

       X has the law G_0 (Y_0*Y_0)^(-1/2).          (7)

Indeed W=Y_0*Y_0 has density proportional to det(W)^u exp(-Tr W).
Changing G_0=X W^(1/2) contributes det(W)^q. Integrating W gives
det(I+X*X)^(-(2u+q)), exactly (1); the Hermitian congruence Jacobian
supplies the further power u in that gamma integral.

With B_0=G_0*G_0, the eigenvalues of T^(-1) equal those of

       J=(W+B_0)^(-1/2) W (W+B_0)^(-1/2).         (8)

This is a finite Jacobi ratio with independent complex Wishart degrees
2u and q. If q<u, B_0 is singular and J has exactly u-q eigenvalues 1.
The remaining r=min(q,u) eigenvalues y_1,...,y_r in (0,1) have density

       c prod_l y_l^u (1-y_l)^|q-u|
                      prod_(l<k) (y_l-y_k)^2.     (9)

For clarity, one can derive (9) without a nonsingular-B assumption:
the singular values t_l of X*X have density
prod t_l^|q-u| (1+t_l)^(-(N+u)) Delta(t)^2;
the elementary complex rectangular singular-value Jacobian follows by
diagonalizing X*X and keeping its r positive eigenvalues. Setting
y_l=1/(1+t_l) changes the y power to
N+u-|q-u|-2r=u. This covers both sides of q=u.

Thus the exact atom of uT/N at u/N has mass
max(0,(u-q)/u)=max(0,2-N/u) almost surely. This saturates the existing
pathwise lower bound; saturation is asserted here only for the Haar law.
For q>0 and k>0, E Tr(T^k) is finite exactly when k<u+1, as follows
from (9) near a single y=0 with the other eigenvalues bounded away.
The finite-N law is unbounded, although its limiting reference measure
has compact support. No finite-N edge bound follows from the latter.

Finally E W^(-1)=I/u: each diagonal reciprocal is the inverse squared
length of a Gaussian column after projection off the other u-1 columns,
with gamma shape 2u-(u-1)=u+1; unitary invariance kills the off-diagonals.
Consequently

       E T=(1+q/u)I=(N/u)I,  E(uT/N)=I.           (10)

These exact finite-dimensional statements do not require the conditional
clock theorem or an assumption about intensity singular gaps.

## 3. All-time flatness for a Haar initial matrix

Now take the full fresh independent uniform phase and independent uniform
coordinate-order process of the maintained clock theorem. Start U_N Haar,
independent of both. By (1), for each predetermined retained size u the
marginal S_u is Haar in its retained coordinates; in fact this is true
conditional on the entire independent phase vector and coordinate order.

Let ell=log(2N), m=ceil(ell^(1+kappa)), kappa>0 fixed, m<N, and
A_m(K)={max_ij |(S_u)_ij|^2 <= K ell/u for every u>=m}.
For a Haar entry in dimension u>=2,
P(|S_ij|^2>t)=(1-t)^(u-1), 0<=t<1.
This follows from a normalized complex Gaussian column, whose squared
coordinates are Dirichlet(1,...,1). If t>=1 the failure probability is zero.
Therefore, using no independence between sizes,

 P_Haar(A_m(K)^c)
 <= sum_(u=m)^N u^2 exp[-K ell (u-1)/u]
 <= N^3 (2N)^(-K(1-1/m)) =: b_N(K).                (11)

For fixed K>3, b_N(K)=2^(-K) N^(3-K)(1+o(1)), because ell/m -> 0.
For example K=4 gives (1+o(1))/(16N). The statement is valid for the
whole trajectory despite its dependencies and uses neither future-event
conditioning in the clock martingale nor an endpoint-gap premise.

The reviewed conditional clock theorem states, for each fixed L,K,kappa,
an epsilon_N ->0 and an intersection failure probability tending to zero
for every deterministic sequence of initial unitaries. Its latter bound
is uniform over the initial matrix: otherwise choose, at infinitely many
N, deterministic initial matrices with failure probability at least a
fixed positive number, contradicting the theorem for that sequence.
The epsilon_N already depends only on L,K,kappa in its statement.
Integrate this uniform intersection bound over the Haar initial matrix
and add (11). Every fixed clock conclusion in that theorem is now
unconditional in probability, simultaneously for all u>=m:
incoming/outgoing diagonal powers, vanishing off-diagonal powers,
vanishing mixed entries S_u(uT_u/N)^r, and all fixed empirical moments.
The existing compactly determinate full-depth measure mu_(u/N) is the
unconditional empirical weak-law reference. No growing-order, edge or
unrestricted exceptional-event moment bound is inferred from this step.

## 4. An entropy-stable non-Haar class

Let nu_N be any law on U(N), independent of the fresh phase/order process,
with finite relative entropy D_N=D(nu_N || Haar_N). Use the same F_N=zU_N.
Let p_N=P_nu(A_m(K)^c), q_N=P_Haar(A_m(K)^c).
The relative entropy of the full initial-matrix-plus-independent-randomness
law is D_N. Apply Jensen to the density on the event and its complement:

 D_N >= p_N log(p_N/q_N)
      +(1-p_N)log((1-p_N)/(1-q_N))
     >= p_N log(1/q_N)-log 2.

For q_N=0, absolute continuity implies p_N=0. Otherwise (11) yields,
for large N with b_N(K)<1,

       p_N <= (D_N+log 2)/log(1/b_N(K)).            (12)

If D_N=o(log N), fixed K>3 gives high-probability all-time flatness.
More strongly, if D_N=O(log N), ALL fixed clock conclusions above still
hold unconditionally in probability. To prove this last statement, fix
a tolerance eta>0 and L,kappa. For each fixed K>3 the uniform deterministic
intersection estimate integrates over nu_N. Once epsilon_N(K)<eta,
the remaining failure probability is bounded by (12), and hence

 limsup_N P_nu(clock error>eta) <= C/(K-3),
 where C=limsup_N D_N/log N < infinity.             (13)

Now let the fixed comparison constant K tend to infinity after this
limsup. This proves convergence, without substituting an N-dependent K
into a theorem that only allows fixed K. For the O(log N) class, no
high-probability flatness assertion for ONE specified finite K is claimed.
All empirical weak-law consequences use the same moment determinacy and
tail argument as the maintained full-depth measure proof.

## 5. Why entropy stability does not imply microscopic universality

This is a mathematical restriction, not just an absent argument. Fix
0<c<1 and a prescribed microscopic arc I_N of angular length 2pi c/N.
Under Haar U(N), the expected number of eigenangles in I_N is c by
rotation invariance and total count N. Therefore the event E_N of no
eigenangle in I_N has probability at least 1-c.
Take nu_N to be Haar_N conditioned on E_N. Then

       D(nu_N || Haar_N)=-log P_Haar(E_N)
                                      <=-log(1-c). (14)

This family satisfies the entropy hypothesis of Section 4 and hence all
of its clock laws. Nevertheless at the initial retained size u=N its
rescaled local point process has no point in that prescribed arc with
probability one. It cannot have the usual intensity-one Sine_2 law at
that prescribed origin, which has strictly positive expected count c.
This is a counterexample only to an entropy-to-prescribed-origin spectral
implication. It is not a counterexample to BGS, to origin-averaged
statistics, to the Haar spectral law, or to any deterministic quantizer.

A deterministic initial U_N has infinite relative entropy with respect
to continuous Haar measure. Classical dynamical entropy is not the
relative entropy used here. No conclusion here establishes all-time
flatness for the maintained deterministic cat-map family, signed TRACE-005,
the physical TRACE-055 hierarchy, or global BGS.
