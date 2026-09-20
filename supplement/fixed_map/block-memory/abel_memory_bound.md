# Quantitative memory at an Abel Heisenberg scale

This is a continuation of `block_memory_theorem.md`, with the same
model, hypotheses and publication status. The Schur memory identity
and its boundary cancellation already appear in
`../coherent-return/research_checkpoint.md`. The contribution here is
a quantitative application to the actual frozen cat blocks, with an
explicit lower bound on their invariant weight. The identity itself
is not claimed as new. No BGS conclusion is asserted.

## 1. A uniformly visible invariant space

For this note only, use the **ordinary** Hilbert--Schmidt inner product
Tr(X*Y), not the normalized product used for Weyl charge estimates.
Let J:C^K -> Mat_N be the isometry J e_s=P_s/sqrt(d_s), and let
V=Ad_U. Write P=JJ* and R=I-P for projections on this matrix space.
They are distinct from the Hilbert-space cluster projectors P_s,Q_s.
Set

\[
 F=J^*VJ=\operatorname{diag}(d)^{-1/2}T^{\rm cl}
               \operatorname{diag}(d)^{1/2},\quad
 \rho=K|\epsilon|F_0\le1/4,
 \quad c=(1-2\rho^2)^2.
\tag{1}
\]

The normalized Q_s/sqrt(d_s) are orthonormal invariant vectors of V.
The overlap matrix of these vectors with J has entries

\[
 W_{rs}=\frac{\operatorname{Tr}(P_rQ_s)}{\sqrt{d_rd_s}}.
\]

Equal ranks and ||P_s-Q_s||<=rho imply
0<=1-Tr(P_sQ_s)/d_s<=rho^2. The overlaps are nonnegative, and
sum_s Tr(P_rQ_s)=d_r, sum_r Tr(P_rQ_s)=d_s. With positive weights
h_s=sqrt(d_s), the weighted absolute row and column sums of I-W are
therefore at most 2 rho^2 times the corresponding weight. The weighted
Schur test yields

\[
 \|I-W\|\le2\rho^2,\qquad WW^*\succeq cI.
\tag{2}
\]

Let E_1 be the orthogonal projection onto ker(I-V), including the
**entire** invariant matrix space of U. No simplicity assumption on U
is needed. Since the normalized Q_s belong to that space,

\[
 E:=J^*E_1J\succeq WW^*\succeq cI,
 \qquad c\ge49/64.
\tag{3}
\]

Thus every coarse direction, including every nonconstant contrast
between cat blocks, has a large invariant component. This proves a
quantitative statement stronger than the existence of one invariant
identity matrix. It is consistent with exact nonreturn of U itself.

## 2. Resolvent and the memory term

For real 0<z<1 define

\[
\begin{split}
 G(z)&=J^*(I-zV)^{-1}J,\\
 \mathcal K(z)&=J^*VR(I-zRVR)^{-1}RVJ.
\end{split}
\tag{4}
\]

The inverse in the second line is well defined since ||RVR||<=1.
Block elimination on ran(P) plus ran(R) gives exactly

\[
 G(z)^{-1}=I-zF-z^2\mathcal K(z).
\tag{5}
\]

Equivalently, the coefficients of K are J*VR(RVR)^n RVJ for n>=0.
This is the coherent memory of the compression; there is no
measurement or reset in (4)--(5).

For |lambda|=1 and real 0<z<1,

\[
 \operatorname{Re}\frac1{1-z\lambda}
 =\frac{1-z\operatorname{Re}\lambda}{|1-z\lambda|^2}>0.
\]

The spectral theorem for unitary V, separating lambda=1, implies

\[
 \operatorname{Re}G(z)\succeq\frac E{1-z}
 \succeq\frac c{1-z}I.
\]

In particular G is invertible and ||G(z)^-1||<=(1-z)/c. Since F
is a compression of a unitary, ||F||<=1. Rearranging (5) proves

\[
 \boxed{\quad
 \|z^2\mathcal K(z)-(I-F)\|
 \le(1-z)(1+c^{-1})\le\frac{113}{49}(1-z).
 \quad}
\tag{6}
\]

At fixed dimension this implies the Abel limit K(z)->I-F as z->1.
We do **not** assert that I-RVR is invertible at z=1. In this coarse
problem it can have many invariant vectors. The sandwich in (4)
has a controlled Abel limit nonetheless.

## 3. Quantitative comparison to the Markov drift

Let u_s=sqrt(pi_s), ||u||=1, and eta=epsilon^2/300. The Doeblin
decomposition of T^cl gives

\[
 F=\eta uu^*+(1-\eta)F_R,
 \qquad\|F_R\|\le1,\qquad F_Ru=F_R^*u=u.
\]

Here F_R is the diagonal similarity transform of a stationary Markov
matrix; its contraction follows from Jensen's inequality in weighted
L^2. Reversibility is not required. Consequently, on u-perpendicular,

\[
 \|Fx\|\le(1-\eta)\|x\|,
 \qquad \|(I-F)x\|\ge\eta\|x\|.
\tag{7}
\]

Take z_N=1-1/N in (6). Every stationary contrast satisfies

\[
 \|z_N^2\mathcal K(z_N)x\|
 \ge\left[\eta-\frac{1+c^{-1}}N\right]\|x\|.
\tag{8}
\]

This is useful when N eta>1+c^-1. In particular it applies
asymptotically to epsilon=N^-a, 0<a<1/2, along the prime Pell
subsequence. The correction is then o(eta), so the Abel memory is
of at least order epsilon^2 on every contrast. It does not approach
a positive absolute constant as epsilon tends to zero.

The response itself also differs substantially from the memory-free
approximation G_0(z)=(I-zF)^-1. For x perpendicular to u,

\[
 \frac{\operatorname{Re}\langle x,(G(z_N)-G_0(z_N))x\rangle}{N}
 \ge\left[c-\frac1{1+(N-1)\eta}\right]\|x\|^2.
\tag{9}
\]

To see this, use Re G>=cN I and the convergent geometric-series
bound ||G_0|_(u-perp)||<=1/[1-z_N(1-eta)]. Equation (9) controls
a normalized Abel average of the block response, not a spectral
form factor or a microscopic eigenvalue correlation.

For the actual tau=10^-80 and K=199, `exact_certificate.json`
checks by rational arithmetic that

\[
 \frac{1+c^{-1}}{N\eta}<1.5\cdot10^{-65}.
\tag{10}
\]

Thus in this finite instance the memory compensates I-F at z_N to
an error less than 1.5*10^-65 times even the conservative lower bound
eta on its action on contrasts. The exact rational certificate and
its reproducible calculation are in `verify.py`.

## 4. Interpretation and remaining gap

Equations (6)--(10) give the missing term in the attempted Markov
closure a definite quantitative size for the frozen symbol. They do
not prove that memory is concentrated at lags near N: short lags
can also contribute to the same Abel sum. No long-lag tail bound is
inferred from this calculation.

At fixed nonzero tau, epsilon=tau N eventually leaves the smallness
regime. In a general coarse projection the invariant compression
J*E_1J can also become poorly conditioned as N grows. A fixed-N Abel
boundary identity with c=c_N tending to zero does not, by itself,
control z=1-1/N. This is why the boundary identity from the earlier
return calculation did not resolve the Heisenberg barrier.

The earlier result used the full position-diagonal projection and
an invertible eigenvector intensity matrix. Here (3) supplies a
uniform lower bound for the cat-block projection in the stated
regime, without a simple-spectrum hypothesis. This is a scoped
quantitative extension, not a claim to have discovered projection
memory theory or to have established fixed-tau BGS.

The numerical diagnostics evaluate G directly in the eigenmatrix
basis of Ad_U at N=41,239, and check its estimate independently of
any time truncation. They also check the overlap singular values
and agreement of F with the independently assembled transition
matrix. The main proof and this extension received a separate
internal audit. That audit caught a potential normalization mismatch
between ordinary and normalized Hilbert--Schmidt products; the
ordinary convention at the start of this note is essential.
