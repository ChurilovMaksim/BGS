> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_classical_symmetry_rigidity.md`. Embedded SHA256: `434e15402b8122051aff0c45e684b53ce07e3ef518642e2b1f7b574b643cd8a3`.
> [Thematic guide](../../topics/symmetry.md).

# Complete C1 symmetry rigidity of the actual classical map

Research continuation, 20 October 2026. This note proves an exact
structural result for the classical map associated with the prescribed
quantization, at the original parameter tau=10^(-80). It is independent
of a random-matrix model and does not prove H_diag.

## 1. Statement

Use the corrected real-half Weyl symbol

$$
\begin{split}
a(q,p)&=V(q)+\frac{R(q)}{100}\cos(2\pi p-\alpha_0),\\
V(q)&=\frac9{10}\cos(14\pi q)
 +\frac1{10}(1-\cos(14\pi q))\cos(2\pi q)
 +\frac{r(q)}{100}\sin(2\pi q),\\
R(q)&=r(q+1/2)=(1+\cos(14\pi q))(1-\cos(2\pi q)).
\end{split}
\tag{1.1}
$$

Let Phi_s be the flow of X=(a_p,-a_q)/(2pi), put

$$
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
\Psi_s=S\Phi_s,\qquad \lambda=3+2\sqrt2.
\tag{1.2}
$$

The inverse convention Phi_(-s) S^(-1) has exactly the same centralizer
and the same reversers, so the conclusions also apply in that convention.

**Theorem.** For every real parameter

$$
0<|s|\le10^{-30},
\tag{1.3}
$$

the centralizer of Psi_s among all C1 diffeomorphisms of the torus is

$$
\boxed{Z_{\mathrm{Diff}^1}(\Psi_s)
       =\{\Psi_s^n:n\in\mathbb Z\}.}
\tag{1.4}
$$

There is no C1 diffeomorphism R of the torus satisfying

$$
\boxed{R\Psi_sR^{-1}=\Psi_s^{-1}.}
\tag{1.5}
$$

The theorem imposes no affine, symplectic, isotopy, or orientation
assumption on the proposed symmetry. In particular it applies at the
exact s=tau=10^(-80). There is no nontrivial C1 root of Psi_s: if
Q^k=Psi_s for an integer |k|>=2 and a C1 diffeomorphism Q, then Q
would commute with Psi_s and (1.4) would imply nk=1 for an integer n.

The result concerns genuine classical diffeomorphisms. It does not
deny the abstract spectral-dependent antiunitary reverser of any finite
unitary matrix, and does not establish quantum spectral correlations.

## 2. Analytic input and its exact remainder

The frozen proof `arithmetic_pressure_analytic_potential.md` establishes
the following facts for the explicit (1.1), with no assumption of a
spatially analytic conjugacy. For |s|<R_*=10^(-16), it constructs a
homeomorphism H_s, close to the identity, and a potential psi_s such that

$$
\Psi_s H_s=H_s S,\qquad
\psi_s\in C^{1/2}(\mathbb T^2;\mathbb C)
\quad\hbox{depends holomorphically on }s,
\tag{2.1}
$$

$$
\psi_0=\log\lambda,\qquad
\|\psi_s-\log\lambda\|_{C^{1/2}}\le10^{11}|s|,
\qquad
\psi'_0=\xi=\frac{a_{pp}-2a_{qq}}{4\pi\sqrt2}.
\tag{2.2}
$$

For real s it also proves the exact coboundary identity

$$
\log J_s^u\circ H_s=\psi_s+u_s\circ S-u_s.
\tag{2.3}
$$

The unstable multiplier is positive, and the stable multiplier is its
reciprocal, since the map preserves area. These assertions follow in the
input from an explicit invariant projective graph over the fixed base S
and the determinant-one derivative matrix. The same construction gives

$$
\|H_s-\mathrm{id}\|_\infty\le4\cdot10^{10}|s|
\tag{2.4}
$$

in the original q,p coordinates. All these properties hold throughout
(1.3); its endpoint is far inside the established disk.

For clarity, the second-order bound needed here follows directly from
(2.2), rather than a theorem about pressure. The Banach-valued function
g_s=(psi_s-psi_0)/s extends holomorphically to zero, satisfies
g_0=xi and has norm at most 10^11 on |s|<R_*. Cauchy's estimates and
the geometric series give, for |s|<=R_*/2,

$$
\boxed{\|\psi_s-\log\lambda-s\xi\|_\infty
                 \le2\cdot10^{27}|s|^2.}
\tag{2.5}
$$

If x is periodic for S, S^k x=x, define

$$
L_s(x;k)=\sum_{j=0}^{k-1}\psi_s(S^j x).
\tag{2.6}
$$

By telescoping (2.3), this is exactly the logarithm of the positive
unstable multiplier of D Psi_s^k at H_s x. It is independent of the
point chosen on that orbit. For two k-periodic points,

$$
\left|L_s(x;k)-L_s(y;k)
       -s\sum_{j=0}^{k-1}[\xi(S^jx)-\xi(S^jy)]\right|
 \le4k\cdot10^{27}|s|^2.
\tag{2.7}
$$

Only k=2 and k=3 are used below.

## 3. The four fixed points determine the allowable lattice actions

For q=0 or 1/2, both derivatives a_p and a_q vanish for every p.
This follows directly from (1.1): R and R' vanish on both lines,
the even terms of V have zero derivative, and its odd term has a
zero of order at least three there. Thus Phi_s fixes both lines
pointwise. The four points

$$
F=\{(0,0),(0,1/2),(1/2,0),(1/2,1/2)\}
\tag{3.1}
$$

are therefore fixed by Psi_s for every s. They are all its fixed
points: S has exactly four, as det(S-I)=-4, and (2.1) is a
homeomorphism conjugacy. One can also solve (S-I)x in Z^2 directly
to obtain precisely (3.1). Since distinct members of F have distance
at least 1/2 in the maximum torus metric, (2.4) implies that H_s
fixes each member of F individually.

At these points the Hessian of a has only the qq entry nonzero.
Direct differentiation of (1.1) gives, in the displayed order of F,

$$
a_{qq}(z)=\frac{\pi^2}{125}c_z,\qquad
(c_z)=(-19606,-19594,24306,24894).
\tag{3.2}
$$

For example, the q-only second derivatives of V at 0,1/2 are
-156.8 pi^2 and 196.8 pi^2. The values R''(0)=8 pi^2 and
R''(1/2)=392 pi^2, multiplied by cos(2pi p-alpha_0)/100,
give the respective additions. At p=0 this cosine is -3/5 and
at p=1/2 it is 3/5. This verifies all four integers in (3.2).

Since these points are equilibria of X, its derivative is the constant
nilpotent matrix [[0,0],[-a_qq/(2pi),0]] along their stationary flow.
Its exponential is exactly the shear

$$
D\Phi_s(z)=\begin{pmatrix}1&0\\-s a_{qq}(z)/(2\pi)&1\end{pmatrix}.
$$

It follows without a Taylor remainder that

$$
\operatorname{Tr}D\Psi_s(z)=6-\frac{2\pi s}{125}c_z.
\tag{3.3}
$$

For s!=0 these four traces are distinct. A C1 commuter of Psi_s
preserves the derivative spectrum at fixed points. A C1 reverser
replaces it by its inverse spectrum. For a two-dimensional
determinant-one matrix the trace of the inverse equals its trace.
Thus either type of C1 symmetry must fix all four points of F
individually.

More generally, either a C1 commuter or a C1 reverser preserves the
unstable multiplier of every periodic orbit that it maps to another
orbit. In the reversing case the derivative is conjugate to the
inverse return map, whose unstable multiplier is the same number
because the two multipliers are reciprocal. In terms of (2.6), all
mapped orbit pairs must have equal L_s.

## 4. Every topological symmetry of S is affine: direct proof

Let R be a homeomorphism of the torus with

$$
R S R^{-1}=S^\epsilon,\qquad \epsilon\in\{1,-1\}.
\tag{4.1}
$$

A lift to the plane has the form R_tilde(x)=B x+r(x), where
B is an invertible integer matrix and r is a bounded periodic
continuous function. Indeed, the lift changes under an integer
translation n by the integer Bn induced by R on the fundamental
group Z^2; subtracting Bx is therefore periodic. The inverse
homeomorphism makes B an element of GL(2,Z).

Comparing lifts in (4.1) gives

$$
BS=S^\epsilon B,\qquad
r(Sx)=S^\epsilon r(x)+k
\tag{4.2}
$$

for one fixed integer vector k. The integer is fixed because the
difference of the two lifts is continuous and integer-valued.
The matrix I-S^epsilon is invertible over R. Choose c with
(I-S^epsilon)c=k. Then v=r-c satisfies

$$
v(Sx)=S^\epsilon v(x).
$$

For every integer n, v(S^n x)=S^(epsilon n)v(x). The left side is
uniformly bounded; the expanding and contracting eigenspaces of S
show that the right side is bounded for both positive and negative
n only when v(x)=0. Hence R is exactly the affine map Bx+c.
This proves the assertion without a centralizer classification theorem.

Now apply this lemma to a C1 symmetry of Psi_s conjugated by H_s.
It becomes a topological symmetry of S. Section 3 and the fact that
H_s fixes F show that its affine representative fixes all of F.
Fixing the origin gives c=0 on the torus; fixing the other two
generators of the half-integer grid gives

$$
B\equiv I\pmod2.
\tag{4.3}
$$

## 5. The integer-matrix calculation leaves only two orbit actions

Put R_0=diag(1,-1), so R_0(q,p)=(q,-p).

In the commuting case, solving BS=SB entry by entry gives

$$
B=\begin{pmatrix}u&2v\\v&u\end{pmatrix}.
\tag{5.1}
$$

In the reversing case, solving BS=S^(-1)B gives

$$
B=\begin{pmatrix}u&2v\\-v&-u\end{pmatrix}.
\tag{5.2}
$$

Condition (4.3) says that u is odd and v is even. In (5.1),
det B=u^2-2v^2 is 1 modulo 8, so det B=1 rather than -1.
In (5.2), det B=2v^2-u^2 is -1 modulo 8, so det B=-1.
In both cases

$$
u^2-2v^2=1.
\tag{5.3}
$$

Here is an elementary complete solution of the needed Pell equation.
The nonzero real number z=u+v sqrt(2) has norm one. Change its sign
if necessary to make z positive. Since lambda=3+2 sqrt(2) and its
inverse have integer coefficients, multiply z by lambda^n for a
suitable integer n to arrange 1<=z'<lambda. Write z'=a+b sqrt(2).
Then

$$
a=(z'+z'^{-1})/2\ge1,\quad
b=(z'-z'^{-1})/(2\sqrt2)\in[0,2).
$$

The integer b is 0 or 1. The latter would give a^2=3 and is
impossible. Thus z'=1, and every solution has
u+v sqrt(2)=plus or minus lambda^n. This proves

$$
\begin{array}{ll}
BS=SB,\ B\equiv I\pmod2 &: B=\pm S^n,\\
BS=S^{-1}B,\ B\equiv I\pmod2 &: B=\pm S^nR_0.
\end{array}
\tag{5.4}
$$

Multiplication by S^n only changes the point on a periodic orbit.
Thus for a reverser there are only two possible actions on orbit
sets: R_0 and -R_0. For a commuter the only additional action
beyond powers of S is -I.

## 6. A period-two orbit excludes the R_0 reversing action

Take the exact S-orbit

$$
x_2=(0,1/8),\qquad Sx_2=(1/2,3/8),\qquad S^2x_2=x_2.
\tag{6.1}
$$

The q-only part of xi is unchanged by R_0. The p-dependent part
of xi on the two critical lines follows from R=0 and their values
of R'':

$$
\xi_{\rm hop}(0,p)=-\frac{\pi}{25\sqrt2}\cos(2\pi p-\alpha_0),
$$

$$
\xi_{\rm hop}(1/2,p)=-\frac{49\pi}{25\sqrt2}
                                  \cos(2\pi p-\alpha_0).
\tag{6.2}
$$

Since sin alpha_0=4/5,

$$
\cos(2\pi p-\alpha_0)-\cos(-2\pi p-\alpha_0)
                      =\frac85\sin(2\pi p).
$$

At p=1/8 and 3/8 both sines equal sqrt(2)/2. Therefore

$$
\boxed{\sum_{j=0}^1
 [\xi(S^jx_2)-\xi(R_0S^jx_2)]= -\frac{8\pi}{5}.}
\tag{6.3}
$$

The set {R_0 S^j x_2} is the S-orbit of R_0 x_2, because R_0
reverses S. By (2.7),

$$
\left|L_s(x_2;2)-L_s(R_0x_2;2)+\frac{8\pi}{5}s\right|
                    \le8\cdot10^{27}|s|^2.
\tag{6.4}
$$

For 0<|s|<=10^(-30), the error divided by |s| is at most .008,
whereas 8pi/5>4.8. Thus these two actual period-two unstable
multipliers differ. No C1 reverser inducing the action R_0 on
periodic orbit sets can exist.

## 7. A period-three orbit excludes both -R_0 and -I

Take

$$
x_3=(1/14,0),\qquad
Sx_3=(3/14,2/14),\qquad
S^2x_3=(3/14,12/14),\qquad S^3x_3=x_3.
\tag{7.1}
$$

Let R_-=-R_0, so R_-(q,p)=(-q,p). The even q-part of V and
the entire hopping term in (1.1) are even in q. Therefore only
V_odd(q)=r(q)sin(2pi q)/100 contributes to
xi(q,p)-xi(-q,p).

At q=j/14 with j odd, put theta=2pi q. Then cos(14pi q)=-1
and sin(14pi q)=0. Differentiating
(1-cos(14pi q))(sin theta+(1/2)sin(2theta)) twice gives exactly

$$
\frac{d^2}{dq^2}[r(q)\sin(2\pi q)]
       =-\pi^2[204\sin\theta+114\sin(2\theta)].
\tag{7.2}
$$

Since xi's q-only contribution is -V''/(2pi sqrt(2)), this proves

$$
\boxed{\xi(q,p)-\xi(-q,p)
 =\frac{\pi}{50\sqrt2}
       [102\sin\theta+57\sin(2\theta)]}
\tag{7.3}
$$

at these q values, independently of p. On the orbit (7.1), theta
is pi/7 once and 3pi/7 twice. Every sine in (7.3) is positive.
Moreover sin t>2t/pi for 0<t<pi/2, by strict concavity of sine
on [0,pi/2]. Hence

$$
\sin(\pi/7)+2\sin(3\pi/7)>2.
$$

It follows that

$$
\boxed{D_3:=\sum_{j=0}^2
 [\xi(S^jx_3)-\xi(R_-S^jx_3)]
       >\frac{102\pi}{25\sqrt2}>8.}
\tag{7.4}
$$

Equation (2.7) gives

$$
|L_s(x_3;3)-L_s(R_-x_3;3)-sD_3|
                         \le12\cdot10^{27}|s|^2.
\tag{7.5}
$$

The error divided by |s| is at most .012 on (1.3). Thus the actual
period-three unstable multipliers differ and exclude every C1
reverser inducing R_- on orbit sets.

The same pair excludes the additional centralizer action -I.
Indeed R_0 fixes x_3, so R_0 maps its S-orbit to itself as a set.
Equivalently the p-coordinates 2/14 and 12/14 in (7.1) are swapped
by R_0. Hence the orbit set (-I)Orb(x_3) equals
(-R_0)Orb(x_3), and its L_s is exactly the comparison value in
(7.5). A C1 commuter inducing -I would have to preserve this
multiplier, a contradiction.

## 8. Completion of the group classification

Suppose a C1 reverser of Psi_s exists. Sections 3--5 show that,
after conjugating by H_s, it has the form plus or minus S^n R_0.
The plus case is excluded by Section 6 and the minus case by
Section 7. This proves (1.5).

Suppose Q is a C1 commuter. Sections 3--5 show that
H_s^(-1) Q H_s equals plus or minus S^n. The negative sign is
excluded by Section 7. With the positive sign, (2.1) gives
Q=H_s S^n H_s^(-1)=Psi_s^n exactly. Conversely every integer
power is a smooth commuter. This proves (1.4).

The map Psi_s has infinite order, since it is homeomorphically
conjugate to S with an eigenvalue lambda>1. The assertion about
roots in Section 1 now follows as stated.

## 9. Provenance, proof status, and quantum boundary

Frozen inputs read without modification:

| File | SHA-256 |
|---|---|
| `arithmetic_pressure_analytic_potential.md` | `44da5eefab7cce7d7eb222fa54f027eec8a1a545b8ca0c4fd3fcf1fc7520637f` |
| `root_fixed_multiplier_nonlattice.md` | `256352cb8b82452d7346345ab0345fd46b795e04935ecf9389940ac920c25e62` |
| `arithmetic_iterated_logarithmic_horizon.md` | `37cae903cc22d77e04ba9848f00fdfd4f19920e9c3a22381de92e965588ce8c6` |

Only the analytic conjugacy and potential properties (2.1)--(2.4)
are imported as load-bearing results; they have complete proofs in
the first file. The fixed-point derivative calculation, affine
classification, Pell reduction, both finite-period discriminators,
and parameter remainder comparison are proved explicitly in this note.
No centralizer theorem, genericity statement, or numerical replacement
of tau is used.

This result excludes all C1 classical symmetries except time iterates,
and all C1 classical reversers, for the actual specified perturbation.
It does not imply that every quantum symmetry admits a C1 classical
limit. In particular no implication from (1.4)--(1.5) to H_diag is
claimed. The required signed quantum trace-product cancellations on
the time scale m proportional to N remain unproved.
