# Three-orientation mixed-loop barrier for the pair transform

**Claim ID:** `BGS-FM-004`

Date: 21 September 2026.

Status: conditional theorem for arbitrary unitary spectra. Its residual hypotheses are not proved for the frozen BGS map. The proof is author-checked with exact symbolic and finite numerical checks; there is no Lean certificate or independent referee report.

## 1. Hypotheses and conclusion

For a sequence of \(N\)-dimensional unitary spectra, use the origin-averaged cotangent resolvent \(s_N\) and the \(\beta=2\) loop residual \(\mathcal E_{p,N}\) defined in the fixed-map frontier. At each \(s>0\) set

\[
w=is/2,\qquad v=-is/2,\qquad
Z=s_N(w),\qquad P=(Z/i-1)/2,
\]

\[
L_N(s)=E|P|^2
=N^{-2}\sum_{k\ge1}e^{-2sk/N}|\operatorname{Tr}U_N^k|^2,
\qquad
M_j=E|Z|^j.
\]

Assume, for every fixed \(s>0\),

\[
\frac{|\mathcal E_{2,N}(w,v)|}{1+M_3}\to0,
\quad
\frac{|\mathcal E_{3,N}(w,v,v)|}{1+M_4}\to0,
\quad
\frac{|\mathcal E_{3,N}(w,w,v)|}{1+M_4}\to0.
\tag{H3}
\]

Then

\[
\boxed{
\liminf_{N\to\infty}L_N(s)
\ge
\frac{\sqrt{1+s^{-2}}-1}{2}
+\frac{s^3}{64(1+s^2)^{7/2}}.}
\tag{1}
\]

The earlier upper bound remains

\[
\limsup_{N\to\infty}L_N(s)
\le
\frac{\sqrt{1+3/(2s^2)}-1}{2}.
\tag{2}
\]

The coefficient \(1/64\) is a convenient certified value, not an optimality claim. The interval still has positive width and does not identify the CUE transform.

## 2. Additional exact identity

Write

\[
r=\frac1{4s^2},\quad
C=E(P^2\bar P),\quad
Q=E|P|^4,\quad
R=E(P^3\bar P),
\]

\[
e=L+C-r,\qquad
g=\mathcal E_{3,N}(w,v,v),\qquad
h=\mathcal E_{3,N}(w,w,v).
\]

The first mixed orientation gives

\[
Q=(1+2r)L-r+\frac g{16}-2\Re e.
\tag{3}
\]

The second orientation gives the exact finite identity

\[
\boxed{
R=(1+r)L-r-\frac{L''}{8}-\frac{L'}{4s}
-\frac32e-\frac h{16}.}
\tag{4}
\]

No independence assumption is used.

## 3. Limiting positivity constraint

The second hypothesis in (H3) supplies the same Jensen bootstrap as the lower-order argument, so \(M_2\) and \(M_4\) stay bounded at each fixed \(s\), and all three normalized residuals vanish without normalization. Positivity of the limiting Gram matrix of

\[
(1,\Re P,(\Re P)^2,(\Im P)^2)
\]

gives

\[
\left|R-\frac{C^2}{l}\right|
\le
\sqrt{
\frac12
\left(Q-\frac{C^2}{l}\right)
\left(Q-l^2-\frac{2C^2}{l}\right)}.
\tag{5}
\]

The Laplace-transform representation of \(L_N\) gives compactness in \(C^\infty_{\rm loc}(0,\infty)\), so every subsequence has a further limit \(l\).

Define

\[
K(u)=ru+r-r^2/u,\qquad
J(u)=2ru+r-r^2/u,
\]

\[
F(u)=-u^2+(2r-1)u+3r-2r^2/u.
\]

Equations (3)--(5) imply the scalar differential inequality

\[
l''+\frac{2l'}s
\le
8\left[K(l)+\sqrt{J(l)F(l)/2}\right].
\tag{6}
\]

## 4. Explicit global barrier

Let

\[
l_0(s)=\frac{\sqrt{1+s^{-2}}-1}{2},
\qquad
d(s)=\frac1{64}\frac{s^3}{(1+s^2)^{7/2}},
\qquad
B=l_0+d.
\]

With \(t=s/\sqrt{1+s^2}\) and
\(G_0=(1-t^2)^2/(2t)\), exact differentiation reduces the barrier margin to

\[
1-\frac{15c}{8}-16c-4\sqrt{c(1+8c)},
\qquad c=\frac1{64}.
\]

At this value it equals

\[
\frac{369}{512}-\frac{3}{4\sqrt2}>0.
\tag{7}
\]

If a limiting \(l\) fell below \(B\), \(l-B\) would attain a negative interior minimum. At that point the differential inequality (6), concavity bounds for \(K,J,F\), and (7) imply simultaneously \(Dl\ge DB\) and \(Dl<DB\), a contradiction. Hence \(l\ge B\), proving (1).

At \(s=1\), the previous lower bound \(0.2071067812\ldots\) rises to \(0.2084878491\ldots\), while the CUE value is \(0.2161661792\ldots\).

## 5. Boundary

The result proves that a second mixed orientation couples a fourth moment to derivatives in the smoothing scale and rules out persistence of the old lower-endpoint model across all scales. It still assumes the mixed residual decay. Establishing that decay for

\[
U_N=\exp(i\,10^{-80}N A_N)M_N
\]

or proving the pair transform directly remains the model-specific problem.
