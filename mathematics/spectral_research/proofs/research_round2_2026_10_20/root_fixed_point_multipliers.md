> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/root_fixed_point_multipliers.md`. Embedded SHA256: `42e52ff202f56182f1ac8314fcca9d668d207c59217738a06eb2f162e9d6824a`.
> [Thematic guide](../../topics/classical_trace.md).

# Exact marked fixed-point multipliers of the specified classical map

## Purpose and scope

This calculation distinguishes the actual prescribed perturbation from a
nonlinear change of coordinates of the unperturbed cat map. Such a change of
coordinates can preserve the entire bad cat spectrum while satisfying
one-step arithmetic-sector mixing. The calculation below rules out that
specific classical explanation for the actual family. It does not prove
quantum trace decorrelation.

We use exactly the corrected ordinary-Weyl symbol

$$
a(q,p)=V(q)+\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha_0),
$$

$$
V(q)=\cos(14\pi q)+r(q)/10+r(q)\sin(2\pi q)/100-1/10,
\quad r(q)=(1-\cos(14\pi q))(1+\cos(2\pi q)).
$$

The classical map in the exact trace construction is

$$
\Psi=\phi_{-a}^{t_*}\circ L,
\quad L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},
\quad t_*=\tau/(2\pi),\quad\tau=10^{-80}.
$$

The Hamiltonian vector field of `-a` is `(-a_p,a_q)`. This convention is
important for the sign of the multiplier shift.

## 1. Two exact equilibrium lines of the kick

At both `q=0` and `q=1/2` one has

$$
r(q)=r'(q)=r(q+1/2)=r'(q+1/2)=0.
$$

Also `sin(14 pi q)=sin(2 pi q)=0`. Differentiating the displayed symbol
therefore gives, for every real `p`,

$$
\nabla a(0,p)=\nabla a(1/2,p)=0.
\tag{1}
$$

Thus the two full vertical lines are fixed pointwise by the Hamiltonian kick
at every time. In particular, the four points

$$
z_{00}=(0,0),\quad z_{01}=(0,1/2),\quad
z_{10}=(1/2,0),\quad z_{11}=(1/2,1/2)
\tag{2}
$$

are fixed by `Psi`, because they are fixed by `L` modulo `Z^2`.

These are all four fixed points of `L`: the equations `(L-I)z in Z^2`
give `2q in Z` and `2p in Z`, and conversely these conditions suffice.
The exact fixed-point count for `Psi` from the earlier strictly concave
sector proof is also four. Exhaustiveness for `Psi` is not needed for the
nonconjugacy argument below.

## 2. Exact Hessians

On either equilibrium line the mixed derivative and the second `p`
derivative vanish. The required elementary values are

$$
r''(0)=392\pi^2,\qquad r''(1/2)=8\pi^2,
$$

$$
V''(0)=-\frac{784}{5}\pi^2,\qquad
V''(1/2)=\frac{984}{5}\pi^2.
\tag{3}
$$

For example, in differentiating `r(q) sin(2 pi q)` at these two points,
all second-derivative terms vanish: the term involving `r''` is multiplied
by the sine, and the other terms contain `r` or `r'`. Also the second
derivative of `cos(14 pi q)` is `-196 pi^2 cos(14 pi q)`.

Since

$$
\cos(-\alpha_0)=-3/5,\qquad
\cos(\pi-\alpha_0)=3/5,
$$

equation (3) gives

$$
D^2a(z)=\frac{\pi^2}{125}
\begin{pmatrix}c_z&0\\0&0\end{pmatrix},
\qquad
\begin{array}{c|rrrr}
z&z_{00}&z_{01}&z_{10}&z_{11}\\ \hline
c_z&-19606&-19594&24306&24894.
\end{array}
\tag{4}
$$

These are exact rational coefficients, not decimal evaluations at a tiny
parameter. The direct differentiation was additionally checked with the
Wolfram Language command below; the derivation (1)--(4) is independent of
that check.

## 3. The derivative of the full map is exact to all orders in tau

At an equilibrium of the kick the linearized flow is the exponential of
the constant derivative of its vector field at that point. By (4) that
matrix is nilpotent of order two:

$$
DX_{-a}(z)=
\begin{pmatrix}0&0\\a_{qq}(z)&0\end{pmatrix}.
$$

Consequently, without a Taylor remainder,

$$
D\phi_{-a}^{t_*}(z)
=\begin{pmatrix}1&0\\t_*a_{qq}(z)&1\end{pmatrix},
$$

$$
D\Psi(z)=
\begin{pmatrix}1&0\\t_*a_{qq}(z)&1\end{pmatrix}
\begin{pmatrix}3&-4\\-2&3\end{pmatrix}.
\tag{5}
$$

In particular `det D Psi(z)=1`, and the four marked traces are

$$
\boxed{\quad
T_z:=\operatorname{Tr}D\Psi(z)
=6-\frac{2\pi\tau}{125}c_z.
\quad}                                                           \tag{6}
$$

They are pairwise different, none equals six, and all are larger than two
at the exact positive parameter of the problem. Their unstable multipliers
are therefore the four different positive numbers

$$
\boxed{\quad
\Lambda_z=\frac{T_z+\sqrt{T_z^2-4}}2.
\quad}                                                           \tag{7}
$$

The strict distinction holds at the full fixed `tau`; no claim relies on
ignoring a term of order `tau^2`.

## 4. Consequences that actually follow

There is no `C^1` diffeomorphism conjugating `Psi` to `L` or to `L^(-1)`.
Indeed, differentiating a `C^1` conjugacy at a fixed point produces similar
derivative matrices. Every fixed point of either linear map has derivative
trace six, contrary to (6). More generally, `Psi` cannot be `C^1` conjugate
to any affine torus map with a constant derivative: the four different
values in (6) would all have to equal that derivative's trace.

Any `C^1` symmetry commuting with `Psi` and permuting its fixed points must
preserve their derivative traces, and hence fixes each of the four points
in (2). With the previously proved four-point count, this applies to every
commuting symmetry. In particular no nonidentity literal torus translation
can commute with `Psi`, because such a translation fixes no point.

This does not classify nonlinear centralizers of the powers `Psi^r`, and
does not rule out a relation in which `Psi^r` intertwines two different
translations. It also gives no estimate for different periodic-orbit action
phases at periods comparable with `N`.

## Symbolic check record

The following finite Wolfram Language computation returned zero gradients
and exactly the four scaled matrices in (4):

```wl
Clear[q,p,r,a];
r[x_]:=(1-Cos[14 Pi x])(1+Cos[2 Pi x]);
a=Cos[14 Pi q]+r[q]/10+r[q]Sin[2 Pi q]/100-1/10
  +r[q+1/2](-3 Cos[2 Pi p]/5+4 Sin[2 Pi p]/5)/100;
grad=D[a,{{q,p},1}]; hes=D[a,{{q,p},2}];
{Table[Simplify[grad/.q->x],{x,{0,1/2}}],
 Table[{x,y,Simplify[125 hes/Pi^2/.{q->x,p->y}]},
       {x,{0,1/2}},{y,{0,1/2}}]}
```

This check concerns only explicit polynomial differentiation; it is not
used as evidence for an asymptotic spectral-statistics theorem.
