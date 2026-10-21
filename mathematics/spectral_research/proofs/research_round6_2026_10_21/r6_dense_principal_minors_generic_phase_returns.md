> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/r6_dense_principal_minors_generic_phase_returns.md`. Embedded SHA256: `2f5d4896e461fe33cf6f8ed25c71d994a4d2842206f48f5fba7bf75189f9d0f8`.
> [Thematic guide](../../topics/algebra.md).

# Nonzero original principal minors and generic auxiliary phases with no dark return sector

21 October 2026. This note proves a further property of the exact
prescribed family for every odd N, followed by its consequences for
auxiliary coordinate phases.

For the original matrix U_N, every initial principal minor on
$\{0,\ldots,k-1\}$, $1\le k\le N$, is nonzero.
For almost every auxiliary row-phase vector z, the eigenangle map
of $\operatorname{diag}(z)U_N$ has invertible Jacobian, its
eigenvectors have no zero coordinates, and its nonzero ordered
eigenangle differences are distinct. Its doubled transfer
therefore has no dark reducing subspace outside the diagonal
pair states. The exact weighted first-return energy is $N^2$.

These are qualitative statements. None supplies a quantitative
bound at the fixed original phase vector $z=(1,\ldots,1)$.
No assertion about spectral simplicity, distinct differences, or
absence of dark states at that specified vector is made here.
There is no claim of H_diag or of a local spectral limit.

## 1. Arithmetic input, stated precisely

We use the following published form of Lindemann--Weierstrass:
a linear combination of exponentials of distinct algebraic
numbers, with nonzero algebraic coefficients, cannot vanish.

The exact source is Cheng-Chao Huang, *Explicit Bounds for Linear
Forms in the Exponentials of Algebraic Numbers*, Proceedings of
ISSAC 2022, Theorem 1.1, DOI
https://doi.org/10.1145/3476446.3536170 .
The author version https://arxiv.org/pdf/2112.05004, page 1,
displays that theorem and the publication metadata. Its precise
statement was independently opened on 21 October 2026.
Only this qualitative statement, not a claimed effective lower
bound, is used below.

Every entry of A_N and M_N is algebraic. Indeed the finite Fourier
coefficients use rational numbers, i, and
$\exp(i\alpha_0)=(-3+4i)/5$; the modular phases are roots of
unity; and $N^{-1/2}$ is algebraic. The Hermitian matrix A_N has
algebraic eigenvalues. Its distinct-eigenvalue projectors are
algebraic because
$$
 P_\lambda=\prod_{\substack{\mu\in\operatorname{spec}(A_N)\\
                           \mu\ne\lambda}}
                   \frac{A_N-\mu I}{\lambda-\mu},
$$
where the product is over distinct eigenvalues.

More generally, let H be a finite Hermitian matrix with algebraic
entries, and let v,w be algebraic vectors. Then
$$
 \langle v,e^{iN\tau H}w\rangle
   =\sum_\mu \langle v,P_\mu w\rangle e^{iN\tau\mu}.
                                                               \tag{1.1}
$$
If the same expression at $\tau=0$ is nonzero, at least one
coefficient in (1.1) is nonzero. Discard zero coefficients.
At every fixed nonzero algebraic $\tau$, the remaining
exponents $iN\tau\mu$ are distinct algebraic numbers.
Lindemann--Weierstrass therefore makes (1.1) nonzero.

Here $\tau=10^{-80}$ is the exact rational parameter in U_N.
The alternative rescaled time $\tau/(2\pi)$ is not used in
this arithmetic argument.

## 2. Every initial principal minor of the original matrix is nonzero

Let $\zeta=e^{2\pi i/N}$ and let $\gamma=4^{-1}\bmod N$.
The given Gaussian kernel factors as
$$
 (M_N)_{xy}=N^{-1/2}\,\eta_x\,\zeta^{\gamma xy}\,\eta_y,
 \qquad
 \eta_x=e_N(-3\cdot8^{-1}x^2).                    \tag{2.1}
$$
For $S_k=\{0,\ldots,k-1\}$, $1\le k\le N$, this gives
$$
 \det M_N[S_k,S_k]
 =N^{-k/2}\left(\prod_{x=0}^{k-1}\eta_x^2\right)
       \prod_{0\le a<b<k}
             (\zeta^{\gamma b}-\zeta^{\gamma a}).   \tag{2.2}
$$
It is the ordinary Vandermonde determinant with row exponents
$0,\ldots,k-1$. Since $\gamma$ is invertible modulo every
odd N, the bases $\zeta^{\gamma a}$, $0\le a<N$, are distinct.
Every factor in (2.2) is therefore nonzero.

Let $A_N^{[k]}$ denote the additive exterior generator: the
restriction of
$$
 A_N\otimes I\otimes\cdots\otimes I+\cdots+
 I\otimes\cdots\otimes I\otimes A_N
$$
to $\bigwedge^k\mathbb C^N$.
It is Hermitian with algebraic entries, and
$$
 \bigwedge\nolimits^k U_N
 =e^{iN\tau A_N^{[k]}}\bigwedge\nolimits^k M_N.     \tag{2.3}
$$
In the standard algebraic wedge basis,
$$
 \det U_N[S_k,S_k]
 =\left\langle e_{S_k},
      e^{iN\tau A_N^{[k]}}
         (\bigwedge\nolimits^kM_N)e_{S_k}\right\rangle.
                                                               \tag{2.4}
$$
Its value at zero parameter is (2.2), which is nonzero.
Equation (1.1) applies to (2.4), including all coincidences among
sums of eigenvalues by grouping them into the distinct spectral
values of the additive exterior generator. We obtain
$$
 \boxed{\quad
 \Delta_k(U_N):=\det U_N[S_k,S_k]\ne0
       \quad(1\le k\le N),\quad N\ge3\text{ odd}.
 \quad}                                                        \tag{2.5}
$$

For later use, every individual entry of U_N is also nonzero.
The same argument with H=A_N, $v=e_x$, $w=M_Ne_y$
has value $(M_N)_{xy}\ne0$ at zero parameter. Hence
$$
 \boxed{(U_N)_{xy}\ne0\quad\text{for every }x,y.}    \tag{2.6}
$$
This entry result was independently proved already in the
occupation rational-inner note; it is reproduced here to make
the present implication self-contained. Formula (2.5) asserts a
specified complete chain of principal minors, not nonvanishing
of every possible principal minor.

## 3. A nonzero coefficient Jacobian

Fix an N by N unitary U whose initial principal minors
$\Delta_k(U)$ are nonzero. For
$Z=\operatorname{diag}(z_0,\ldots,z_{N-1})$, write
$$
 p(\lambda,z)=\det(\lambda I-ZU)
   =\lambda^N+\sum_{k=1}^N c_k(z)\lambda^{N-k}.
$$
The principal-minor formula gives
$$
 c_k(z)=(-1)^k\sum_{|S|=k}\det U[S,S]\prod_{a\in S}z_a.
                                                               \tag{3.1}
$$
Consider the logarithmic coefficient Jacobian
$$
 {\cal J}(z)=
 \det\left[z_a\frac{\partial c_k}{\partial z_a}\right]
 _{\substack{1\le k\le N\\0\le a<N}}.             \tag{3.2}
$$
Use lexicographic monomial order $z_0>z_1>\cdots>z_{N-1}$.
The leading monomial of c_k is
$$
 (-1)^k\Delta_k(U)\,z_0z_1\cdots z_{k-1}.
$$
In row k of (3.2), this monomial appears with the same coefficient
in precisely the columns $a<k$. Every other monomial in that
row is strictly smaller. Multiplicativity of the monomial order
shows that the coefficient of the product of all these leading
monomials is the determinant of the lower-triangular indicator
matrix $[{\bf1}_{\{a<k\}}]$, times their coefficients.
That determinant is one. Consequently
$$
 \boxed{\quad
 [z_0^Nz_1^{N-1}\cdots z_{N-1}]\,{\cal J}(z)
   =(-1)^{N(N+1)/2}\prod_{k=1}^N\Delta_k(U)\ne0.
 \quad}                                                        \tag{3.3}
$$
No smaller monomial choices can cancel this coefficient.
Thus ${\cal J}$ is a nonzero polynomial.
By (2.5), this conclusion applies to every original U_N.

## 4. Generic simplicity and full support of eigenvectors

We give an elementary algebraic proof using only the nonzero
entries in (2.6). Suppose U is any invertible matrix with
$U_{ab}U_{ba}\ne0$ for every $a\ne b$. Define
$$
 D(w)=\det(\operatorname{diag}(w_0,\ldots,w_{N-1})-U).
$$
This polynomial is irreducible over $\mathbb C$.
Indeed it is of degree one in each variable and has leading
monomial $\prod_aw_a$ with coefficient one. In a nontrivial
factorization D=FG, each variable belongs to exactly one of
the factors: its degrees in the two factors are nonnegative
integers with sum one. Thus there is a nonempty partition I,J
of the variables, with F depending only on I and G only on J.
Normalize their full monomial coefficients to one.
For $a\in I,b\in J$, the coefficients missing a and missing b
from the full monomial are $-U_{aa}$ and $-U_{bb}$.
Their factorization forces the coefficient missing both to be
$U_{aa}U_{bb}$. Its actual value is
$$
 \det U[\{a,b\},\{a,b\}]
      =U_{aa}U_{bb}-U_{ab}U_{ba},
$$
a contradiction. This proves the irreducibility.

The constant coefficient of D is $(-1)^N\det U\ne0$.
Thus D stays irreducible after inverting its variables, since
it is not a variable factor or a monomial. Adjoin and invert
one further variable $\lambda$. The Laurent change of variables
$w_a=\lambda/z_a$ gives
$$
 p(\lambda,z)=\left(\prod_a z_a\right)D(\lambda/z).
                                                               \tag{4.1}
$$
It follows that p is irreducible in the Laurent ring in
$\lambda,z$. Its constant coefficient as a polynomial in
$\lambda$ is the nonzero Laurent monomial
$(-1)^N\det U\prod_a z_a$. A factorization in the polynomial
ring in $\lambda$ cannot therefore acquire a nonconstant
factor $\lambda^m$ that becomes a Laurent unit.
Since p is monic, Gauss's lemma now makes it irreducible in
$\mathbb C(z_0,\ldots,z_{N-1})[\lambda]$.

Let $p_a(\lambda,z)$ be the characteristic polynomial of the
matrix obtained from ZU by deleting row and column a.
It has degree $N-1$. Irreducibility and characteristic zero
give the nonzero Laurent polynomials
$$
 \operatorname{Res}_\lambda(p,\partial_\lambda p)\ne0,
 \qquad
 \operatorname{Res}_\lambda(p,p_a)\ne0
       \quad(0\le a<N).                          \tag{4.2}
$$
Here the elementary resultant criterion says that the determinant
of the Sylvester matrix is zero exactly when two polynomials have
a common factor over the coefficient field. The degree of
$p_a$ and of $\partial_\lambda p$ is smaller than that of p,
so such a factor is impossible.

A nonzero Laurent polynomial has zero set of measure zero on
the unit torus. To see this, induct on the number of variables,
viewing it as a polynomial in the last variable after clearing
monomial denominators. Outside the null set where all its
coefficient polynomials vanish, it has finitely many zeros
in that last circle. Fubini completes the induction.

Therefore for almost every unit phase vector z, ZU has distinct
eigenvalues, and none of these eigenvalues is an eigenvalue
of any deleted principal matrix. If ZU is unitary, for a
normalized eigenvector v_j with simple eigenvalue $\lambda_j$,
$$
 p_a(\lambda_j,z)=
       (\partial_\lambda p)(\lambda_j,z)\,|v_j(a)|^2.             \tag{4.3}
$$
For example, (4.3) follows by evaluating the aa entry of
$$
 \operatorname{adj}(\lambda I-ZU)
   =p(\lambda,z)(\lambda I-ZU)^{-1}
$$
using its spectral resolution. Equations (4.2)--(4.3) imply
$$
 v_j(a)\ne0\quad\text{for all }a,j
$$
outside a null set of phases. All hypotheses hold for every
original U_N by (2.6).

## 5. Eigenangle Jacobian and distinct nonzero differences

On a neighborhood with simple eigenvalues, the implicit function
theorem applied to p gives smooth local eigenvalue branches.
For unit phases $z_a=e^{i\phi_a}$, write
$\lambda_j=e^{i\theta_j}$ in local real angle coordinates.
Differentiating the eigenvalue equation of the normal matrix ZU
gives
$$
 \frac{\partial\lambda_j}{\partial\phi_a}
   =v_j^*(iE_{aa}ZU)v_j
   =i\lambda_j|v_j(a)|^2,
 \qquad
 \frac{\partial\theta_j}{\partial\phi_a}=|v_j(a)|^2.
                                                               \tag{5.1}
$$
The Jacobian from the eigenvalues to the coefficients
$c_1,\ldots,c_N$ is invertible when the eigenvalues are distinct.
One direct proof is that the polynomials
$-\prod_{\ell\ne j}(\lambda-\lambda_\ell)$, their derivatives
with respect to the individual roots, are linearly independent:
evaluating at $\lambda=\lambda_j$ isolates each coefficient.

Since
$$
 \frac{\partial c_k}{\partial\phi_a}
      =i z_a\frac{\partial c_k}{\partial z_a},
$$
the chain rule and (3.2) show that the real matrix in (5.1) is
invertible wherever the spectrum is simple and ${\cal J}(z)\ne0$.
The exceptional set has measure zero by (3.3), (4.2), and the
torus zero-set argument. Thus
$$
 \boxed{\quad
 \det\bigl[|v_j(a)|^2\bigr]_{j,a}\ne0
       \quad\text{for almost every phase vector }z.
 \quad}                                                        \tag{5.2}
$$

The inverse function theorem now makes the eigenangle map a
local diffeomorphism on this full-measure set. In particular
the auxiliary eigenangle law is absolutely continuous in local
angle coordinates: on each inverse chart this is the ordinary
change-of-variables formula, and a countable chart cover suffices.
No bound on its density or on the inverse Jacobian is asserted.

For distinct ordered pairs $(j,k)\ne(\ell,m)$, with
$j\ne k$ and $\ell\ne m$, the equality
$$
 \lambda_j\overline{\lambda_k}
       =\lambda_\ell\overline{\lambda_m}
$$
is equivalent on each angle chart to
$$
 \theta_j-\theta_k-\theta_\ell+\theta_m\in2\pi\mathbb Z.
                                                               \tag{5.3}
$$
This is a nonzero linear form in the angle coordinates; its
coefficients could all vanish only if the ordered pairs agreed.
The countable union of hyperplanes in (5.3) has Lebesgue
measure zero. Its inverse image under the local diffeomorphisms
therefore has measure zero. Taking the finite union over the
ordered pairs proves that all nonzero ordered eigenangle
differences are distinct for almost every auxiliary phase vector.
Simplicity also excludes any such difference from being zero.

## 6. No dark subspace and exact weighted return energy

Set $V=ZU_N$ and $W=V\otimes\overline V$.
Let M project onto the diagonal pair states and $O=I-M$;
write
$$
 W=\begin{pmatrix}P&B\\C&S\end{pmatrix},\qquad S=OWO.
$$
A unitary reducing subspace of S inside O is also reducing for W.
Indeed unitarity of W gives
$$
 B^*B+S^*S=I_O,\qquad CC^*+SS^*=I_O.
$$
On the unitary subspace of S, both B and $C^*$ vanish.
These identities show directly that W and $W^*$ preserve
the same subspace.

For a phase vector satisfying §§4--5, the eigenvectors of W are
the matrix units $|v_j\rangle\langle v_k|$.
For $j\ne k$, each eigenvalue
$\lambda_j\overline{\lambda_k}$ is simple. Its eigenvector
has diagonal entries $v_j(a)\overline{v_k(a)}$, all nonzero
by §4. Hence this eigenspace has no vector in O.

The eigenvalue one has exactly the N-dimensional eigenspace
$$
 \operatorname{span}\{|v_j\rangle\langle v_j|:1\le j\le N\}.
$$
Its diagonal projection is the map
$$
 (t_1,\ldots,t_N)\longmapsto
          \left(\sum_j t_j|v_j(a)|^2\right)_{a=0}^{N-1},
$$
which is injective by (5.2). This eigenspace also has zero
intersection with O. Every nonzero reducing subspace of a finite
unitary contains an eigenvector. We have therefore proved
$$
 \boxed{\quad
 \mathcal H_{\rm dark}(z)=\{0\}
       \quad\text{for almost every auxiliary phase vector }z.
 \quad}                                                        \tag{6.1}
$$

For the exact first returns
$$
 F_1=P,\qquad F_r=BS^{r-2}C\quad(r\ge2),
$$
the finite-dimensional identities proved in the frozen renewal
note are
$$
 \sum_{r\ge1}\|F_r(z)\|_{\rm HS}^2=N,\qquad
 \sum_{r\ge1}r\|F_r(z)\|_{\rm HS}^2
                =N^2-\dim\mathcal H_{\rm dark}(z).
$$
They follow by telescoping
$$
 \|S^mC\|_{\rm HS}^2
   =\|S^m\|_{\rm HS}^2-\|S^{m+1}\|_{\rm HS}^2
$$
and splitting a finite contraction into its unitary part and its
strictly stable part. All details, including completeness in
the presence of dark states, are contained in the cited proof.

Combining with (6.1) yields for every odd original dimension N,
$$
 \boxed{\quad
 \sum_{r\ge1}r\|F_r(z)\|_{\rm HS}^2=N^2
       \quad\text{for almost every }z,\qquad
 \sum_{r\ge1}r\,\mathbb E_z\|F_r(z)\|_{\rm HS}^2=N^2.
 \quad}                                                        \tag{6.2}
$$
The averaged equality uses Tonelli and the universal upper
bound $N^2$. Equivalently,
$$
 \nu_N(r)=N^{-1}\mathbb E_z\|F_r(z)\|_{\rm HS}^2
$$
is a probability distribution on the positive integers with
exact mean N. In particular its normalized return-time laws
have the elementary tail bound
$$
 \nu_N(r\ge BN)\le1/B\qquad(B>0).
$$
No limiting distribution or concentration around the mean is
inferred from this identity.

## 7. Precise limitations

The conclusions (2.5)--(2.6) are properties of the actual U_N
at its specified exact parameter and hold for every odd N.
The conclusions about full eigenvector support, invertible
eigenangle Jacobian, distinct nonzero differences, and zero dark
subspace hold almost everywhere in the auxiliary phase torus.
A specified point such as $z=(1,\ldots,1)$ can belong to the
exceptional null set. The proof does not exclude that possibility.

There is also no uniform lower bound for the Jacobian or a
spectral gap for S as N grows. In fact the exact isometric
subspace theorem still gives $\|S^m\|_{\rm op}=1$ for
$1\le m<N$, for every phase vector; this is compatible with
eventual decay for each fixed generic finite-dimensional S.
Neither genericity nor the exact mean return time supplies the
missing signed cancellation for the original long traces.

## Proof dependencies

- The sole external theorem is the precise published
  Lindemann--Weierstrass statement identified and checked in §1.
  Its distinct-exponent and algebraic-coefficient hypotheses are
  verified explicitly in (1.1)--(2.4).
- The weighted first-return identity and all finite-dimensional
  recurrence details are proved in
  research_round6_2026_10_21/r6_dense_renewal_long_return_obstruction.md,
  SHA256 95ea7e37c46b840854853c934eebecbd51ac1cb305d0200a283e68b9f7c3d0b2.
- The previously established all-entry nonvanishing is in
  research_round6_2026_10_21/r6_occupation_rational_inner_kac.md,
  §7. Its proof is repeated here, so no additional assumption
  is imported from that note.

No numerical spectral experiment or unproved genericity
assumption enters these statements.

