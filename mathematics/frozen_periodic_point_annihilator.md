# Exact periodic-point grids and Fourier annihilators for the fixed cat

**Claim ID:** `BGS-FM-012`. **Status:** elementary project derivation,
checked in this integration pass; no novelty or independent-referee claim.

The uploaded `cue_project.zip` suggested an all-time finite-subgroup
averaging statement but supported its threshold with a floating eigenvector
search. Here an exact Pell factorization supplies the missing uniform
argument. Related arithmetic and a special even-time grid already occur in
[the arithmetic trace note](frozen_arithmetic_trace_rigidity.md) and
[the periodic-point trace comparison](periodic_point_trace_comparison.md),
Section 2. This is an explicit all-time specialization of that arithmetic,
not a new universality mechanism.

## 1. Exact statement

Put
$$
 S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
 C=\begin{pmatrix}1&2\\1&1\end{pmatrix},\qquad C^2=S,
 \qquad
 C^m=\begin{pmatrix}x_m&2y_m\\y_m&x_m\end{pmatrix}.
$$
Here $x_0=1,y_0=0$ and
$x_{m+1}=x_m+2y_m$, $y_{m+1}=x_m+y_m$, all in the integers.
For $m\ge1$ let $P_m=\operatorname{Fix}(S^m:\mathbb T^2\to\mathbb T^2)$
and let $L_m$ be its annihilator in the frequency lattice, in $(q,p)$ order.
Then
$$
 L_m=(S^m-I)^T\mathbb Z^2=
 \begin{cases}
   2x_m\mathbb Z\times2x_m\mathbb Z,&m\text{ odd},\\
   2y_m\mathbb Z\times4y_m\mathbb Z,&m\text{ even}.
 \end{cases}                                                    \tag{1}
$$
Consequently
$$
 P_m=
 \begin{cases}
  \{(j/(2x_m),k/(2x_m)):0\le j,k<2x_m\},&m\text{ odd},\\
  \{(j/(2y_m),k/(4y_m)):0\le j<2y_m,\ 0\le k<4y_m\},&m\text{ even},
 \end{cases}                                                    \tag{2}
$$
with counts $4x_m^2$ and $8y_m^2$, respectively. The same sets are
fixed by $S^{-m}$. For $S^T$ the two coordinates in the even case swap;
this distinction matters when comparing frequency-map conventions.

The shortest nonzero annihilator frequency in the infinity norm is exactly
$$
 \ell_m=\begin{cases}2x_m,&m\text{ odd},\\2y_m,&m\text{ even},\end{cases}
 \qquad (\ell_1,\ldots,\ell_6)=(2,4,14,24,82,140).                \tag{3}
$$
In particular $\ell_m\ge14$ for every $m\ge3$.

## 2. Proof, including the lattice and averaging steps

The recurrence gives $x_m^2-2y_m^2=(-1)^m$ and $C^m\in GL(2,\mathbb Z)$.
If $m$ is odd, its inverse is
$\left(\begin{smallmatrix}-x_m&2y_m\\y_m&-x_m\end{smallmatrix}\right)$,
so
$$
 S^m-I=C^m(C^m-C^{-m})=2x_m C^m.
$$
Thus its transpose has image $2x_m\mathbb Z^2$. If $m$ is even, put
$J=\left(\begin{smallmatrix}0&2\\1&0\end{smallmatrix}\right)$; then
$$
 C^m-C^{-m}=2y_m J,
 \qquad (S^m-I)^T=2y_m J^T(C^m)^T.
$$
The last unimodular factor maps $\mathbb Z^2$ onto itself and
$J^T\mathbb Z^2=\mathbb Z\times2\mathbb Z$. This proves (1).

For completeness, for any nonsingular integral $B$, the character
$z\mapsto e^{2\pi i\xi\cdot z}$ is trivial on
$B^{-1}\mathbb Z^2/\mathbb Z^2$ iff
$B^{-T}\xi\in\mathbb Z^2$, or $\xi\in B^T\mathbb Z^2$.
A nontrivial character has zero average: translation by a point where its
value is not one multiplies the average by that value. This proves the
annihilator assertion and (2), without an unproved equidistribution input.
The inverse map has the same fixed points, since
$S^{-m}-I=-S^{-m}(S^m-I)$ and the factor is unimodular.
Equation (3) follows from the rectangular lattice; monotonicity of positive
$x_m,y_m$ and their first values proves the all-$m$ lower bound.

For any Fourier polynomial $f=\sum_\xi\widehat f_\xi e^{2\pi i\xi\cdot z}$,
$$
 \frac1{|P_m|}\sum_{z\in P_m}f(z)-\int_{\mathbb T^2}f
       =\sum_{\xi\in L_m\setminus\{0\}}\widehat f_\xi .         \tag{4}
$$
Hence support in $\|\xi\|_\infty\le K<\ell_m$ implies *exact* equality
with the torus integral. The same formula holds for absolutely summable
Fourier series, by absolute convergence. No bounded-frequency hypothesis
can be silently applied to an exponential of a growing Birkhoff sum.

## 3. Application to the actual ordinary symbol

Use the physical symbol from
[BGS-FM-001](fixed_model_symmetry_theorem.md), not the unshifted raw symbol:
$$
 g(q,p)=v(q)+\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha),
 \quad
 v(q)=\cos14\pi q+\frac{r(q)}{10}
          +\frac{r(q)\sin2\pi q}{100}-\frac1{10},
$$
where $r(q)=(1-\cos14\pi q)(1+\cos2\pi q)$.
Its mean is zero. Its 32 nonzero modes satisfy $|k|\le9,|l|\le1$;
the $k=\pm9$ modes are present, so the upload's bandwidth $8$ is incorrect.
All modes with $l=\pm1$ are killed by every lattice in (1). The surviving
$l=0$ cosine terms are read from
$$
 v(q)=\tfrac9{10}\cos14\pi q+\tfrac1{10}\cos2\pi q
       -\tfrac1{20}\cos12\pi q-\tfrac1{20}\cos16\pi q
       +\text{sine terms}.
$$
Opposite sine coefficients cancel. Equation (4) therefore gives
$$
 \boxed{\frac1{|P_m|}\sum_{z\in P_m}g(z)=
 \begin{cases}-1/10,&m=1,\\-1/20,&m=2,\\0,&m\ge3.\end{cases}}  \tag{5}
$$
The unshifted raw symbol has the same *linear* averages, since the changed
modes all have $l=\pm1$. Their nonlinear orbit weights need not agree.

## 4. Logical boundary and verification

This controls a classical linear average over every fixed-point set.
It does not control $e^{i\lambda\sum_{j<m}g\circ S^j}$, the nonlinear
classical map, a quantum trace remainder, or joint traces at $m\asymp N$.
It supplies no missing implication toward BGS-TRACE-005.

[The maintained verifier](../computations/verification/cue_upload_audit.py)
checks the exact factorizations and membership tests with unbounded Python
integers, brute-enumerates the small fixed-point sets, and assembles the
symbol coefficients with rational real and imaginary parts. Its finite
range is recorded in the output; the all-time assertion is proved above.
The [upload review](../archive/record/cue_upload_review_20260927.md) records the
rejected claims, provenance, and separately scoped numerical checks.
