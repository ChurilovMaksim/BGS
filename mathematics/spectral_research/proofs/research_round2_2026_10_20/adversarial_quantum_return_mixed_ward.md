> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/adversarial_quantum_return_mixed_ward.md`. Embedded SHA256: `53837a219e2a77acc8e2b08921c33ccf5a8eb89d8b6a15f333df360b5593b749`.
> [Thematic guide](../../topics/dephasing.md).

# Mixed quantum return identities and a nonvanishing open contribution

Research continuation, 20 October 2026. Every application below uses the
original matrix $U_N=\exp(i\tau N A_N)M_N$, with the unchanged
$\tau=10^{-80}$. All main identities are finite-dimensional operator
identities. No replacement of quantum returns by classical orbit weights is
made.

The verified input is fermionic_quantum_marker_return.md, SHA-256
31c247eba33f35cdee9123dfbbaf9f711f1a2d47ed257b83e6136bda8793046e.
The proofs below include the return identities they need. The accompanying
classical comparison input
arithmetic_all_marker_domains_and_renewal_barrier.md, SHA-256
dc8bef986cae11bc1917805a02746cd0861ee06f74da1d853bcc82e25ba7deba,
has also been checked; none of its classical endpoint laws is used to
identify a quantum matrix element.

## 1. Main new conclusions

For an arbitrary positive contraction $E$ on $\mathbb C^N$, put
$$
a=(I-E)^{1/2},\quad b=E^{1/2},\quad
A=-a,\quad B=bU,\quad D=aU,\quad F_m=BD^{m-1}b\quad(m\ge1).
\tag{1.1}
$$
Write $\mathcal H_{\rm seen}$ for the smallest reducing subspace of $U$
containing $\operatorname{Ran}b$.

First, the full mixed-time identities are
$$
A^*F_k+\sum_{m=1}^{M}F_m^*F_{m+k}
   =-b(D^*)^M D^{M+k}b\qquad(k\ge1),
\tag{1.2}
$$
and the mixed first moments obey
$$
\boxed{\displaystyle
\sum_{m\ge1}m\,\operatorname{Tr}(F_m^*F_{m+k})
       =\operatorname{Tr}(D^k|_{\mathcal H_{\rm seen}})
       \qquad(k\ge0).}
\tag{1.3}
$$
Thus the weighted mixed returns contain the open-map power traces
themselves.

Second, when $\operatorname{Tr}E\le1/4$, the exact open contribution has
a strictly positive lower bound in the full Abel norm:
$$
\boxed{\displaystyle
\frac1{N^2}\sum_{m\ge1}e^{-m/(2N)}
                    |\operatorname{Tr}D^m|^2>\frac7{10}.}
\tag{1.4}
$$
This holds for every $N$ and every unitary $U$, hence in particular for
the original $U_N$ and the concrete finite Fourier detector in Section 6.
The proof includes the infinite tail. The claim that this open contribution
is $o(1)$ in that normalized Abel functional is therefore false for that
actual detector.

Equation (1.4) does not refute the required statistic for $U_N$.
The exact feedback contribution can interfere with the open contribution.
Sections 5 and 7 identify the mixed coefficients left in that problem.

## 2. Reducing spaces and exact energy bookkeeping

The block matrix
$$
\mathcal V=\begin{pmatrix}A&B\\ b&D\end{pmatrix}
          =\begin{pmatrix}-a&bU\\ b&aU\end{pmatrix}
\tag{2.1}
$$
is unitary, since $a,b$ commute and $a^2+b^2=I$. In particular,
$$
B^*B=I-D^*D,\qquad E=b^2=I-DD^*,\qquad
A^*B=-bD,\qquad ba=DB^* .
\tag{2.2}
$$

The orthogonal complement $\mathcal H_{\rm dark}$ of the seen space is
the largest reducing subspace of $U$ contained in $\ker E$. Both $D$
and $D^*$ preserve this decomposition; on the dark space $D=U$, and
$b$ and $B$ annihilate it. On the seen space the spectral radius of
$D$ is strictly less than one. Indeed, if $Dv=\lambda v$ with
$|\lambda|=1$, contraction equality forces $Uv\in\ker E$, so
$Uv=Dv=\lambda v$ and also $v\in\ker E$. This vector lies in a dark
reducing eigenspace of $U$. Thus no such eigenvector occurs in the seen
space. Finite-dimensional spectral theory completes the assertion.

Let $P_{\rm seen}=I-P_{\rm dark}$, and define
$$
e_M=\|D^M b\|_{\rm HS}^2\quad(M\ge0).
$$
This sequence is nonincreasing. The two defect identities in (2.2) give
$$
e_M=\|D^M\|_{\rm HS}^2-\|D^{M+1}\|_{\rm HS}^2
    =\|BD^M\|_{\rm HS}^2 ,
\tag{2.3}
$$
and therefore
$$
\sum_{M\ge0}e_M=\dim\mathcal H_{\rm seen},\qquad
e_M\le \min\left(\operatorname{Tr}E,
                  \frac{\dim\mathcal H_{\rm seen}}{M+1}\right).
\tag{2.4}
$$
The limits used here follow from geometric decay on the seen space and
unitarity on the dark space.

Similarly,
$$
\|F_m\|_{\rm HS}^2=e_{m-1}-e_m,
$$
so that
$$
\sum_{m\ge1}\|F_m\|_{\rm HS}^2=\operatorname{Tr}E,\qquad
\sum_{m\ge1}m\|F_m\|_{\rm HS}^2=\dim\mathcal H_{\rm seen}.
\tag{2.5}
$$
For the second identity one may first telescope a finite sum and then use
$M e_M\to0$. The latter follows either from finite-dimensional decay, or
from the fact that $e_M$ is a nonincreasing summable sequence.

## 3. Finite, infinite, and Abel mixed-time identities

For $j,k\ge0$ set
$$
H_j^{(k)}=b(D^*)^jD^{j+k}b.
$$
Equation (2.2) gives
$$
F_m^*F_{m+k}=H_{m-1}^{(k)}-H_m^{(k)}.
\tag{3.1}
$$
For $k\ge1$, $A^*F_k=-H_0^{(k)}$; for $k=0$,
$A^*A=I-H_0^{(0)}$. Consequently
$$
\begin{aligned}
A^*F_k+\sum_{m=1}^{M}F_m^*F_{m+k}&=-H_M^{(k)}
                                         &&(k\ge1),\\
A^*A+\sum_{m=1}^{M}F_m^*F_m&=I-H_M^{(0)} .
\end{aligned}
\tag{3.2}
$$
These formulas include $M=0$.

The trace-norm error is bounded by
$$
\|H_M^{(k)}\|_1
\le\|D^M b\|_{\rm HS}\|D^{M+k}b\|_{\rm HS}
\le e_M
\le\frac{\dim\mathcal H_{\rm seen}}{M+1}.
\tag{3.3}
$$
In particular, the infinite mixed sums converge absolutely in trace norm
and have the exact limits specified by (3.2).

The reversed identities also hold:
$$
F_kA^*+\sum_{m=1}^{M}F_{m+k}F_m^*
       =-BD^{M+k}(D^*)^M B^*\quad(k\ge1),
\tag{3.4}
$$
with the diagonal version $I-BD^M(D^*)^M B^*$. To verify them,
use $F_kA^*=-BD^kB^*$, $b^2=I-DD^*$, and telescope.
Their trace-norm errors are again at most $e_M$, by (2.3).

For $0<r<1$, summing the same difference with its actual Abel weight gives
$$
\boxed{\displaystyle
A^*F_k+\sum_{m\ge1}r^{2m}F_m^*F_{m+k}
=-(1-r^2)\sum_{j\ge0}r^{2j}H_j^{(k)}
\quad(k\ge1).}
\tag{3.5}
$$
For $k=0$ replace $A^*F_k$ by $A^*A$ and add $I$ to the
right-hand side. Absolute convergence follows from (2.4). The error in
the infinite, unweighted identity satisfies
$$
\left\|(1-r^2)\sum_{j\ge0}r^{2j}H_j^{(k)}\right\|_1
\le\min\bigl(\operatorname{Tr}E,
                    (1-r^2)\dim\mathcal H_{\rm seen}\bigr).
\tag{3.6}
$$
At $r=e^{-s/N}$, the second bound is $O_s(1)$. It is not an
$o(1)$ estimate. No assertion that this particular matrix error must
remain nonzero is made.

## 4. Weighted mixed returns recover the open power traces

Multiplying (3.1) by $m$ before summing yields the exact matrix identity
$$
\sum_{m=1}^{M}mF_m^*F_{m+k}
  =\sum_{j=0}^{M-1}H_j^{(k)}-M H_M^{(k)}.
\tag{4.1}
$$
Here $k\ge0$. Both infinite sums converge in trace norm:
$$
\sum_{m\ge1}m\|F_m^*F_{m+k}\|_1
\le
\left(\sum_{m\ge1}m\|F_m\|_{\rm HS}^2\right)^{1/2}
\left(\sum_{m\ge1}m\|F_{m+k}\|_{\rm HS}^2\right)^{1/2}
\le\dim\mathcal H_{\rm seen},
\tag{4.2}
$$
and $\sum_j\|H_j^{(k)}\|_1\le\sum_j e_j$.
Since $M e_M\to0$, (4.1) implies
$$
\sum_{m\ge1}mF_m^*F_{m+k}
       =b\sum_{j\ge0}(D^*)^jD^{j+k}b .
\tag{4.3}
$$

Taking the trace, cyclically moving factors, and using $E=b^2$, gives
$$
\operatorname{Tr}H_j^{(k)}
  =\operatorname{Tr}\bigl(D^kD^jE(D^*)^j\bigr).
$$
The other defect telescope is
$$
\sum_{j\ge0}D^jE(D^*)^j=P_{\rm seen}.
\tag{4.4}
$$
Thus (4.3) proves
$$
\sum_{m\ge1}m\operatorname{Tr}(F_m^*F_{m+k})
  =\operatorname{Tr}(D^kP_{\rm seen})
  =\operatorname{Tr}(D^k|_{\mathcal H_{\rm seen}}).
\tag{4.5}
$$
For $k=0$ this recovers the second identity in (2.5). For $k>0$ it is
a genuine mixed-time statement, not a bound on separate return energies.

For reference, the finite traced version is
$$
\sum_{m=1}^{M}m\operatorname{Tr}(F_m^*F_{m+k})
 =\operatorname{Tr}\!\left[
 D^k\{I-D^M(D^*)^M-MD^ME(D^*)^M\}\right].
\tag{4.6}
$$
This is an exact identity; no uniform small remainder at $M\asymp N$
is claimed.

## 5. The first mixed insertion not fixed by the identity Ward relation

Let $X$ be an arbitrary fixed $N$-by-$N$ matrix. Define on the seen
space, and extend by zero on the dark space,
$$
Z_X=\sum_{j\ge0}(D^*)^jB^*XB D^j .
\tag{5.1}
$$
This converges in finite dimension and is the unique such solution of
$$
Z_X-D^*Z_XD=B^*XB.
\tag{5.2}
$$
Uniqueness follows by iteration on the seen space. The map $X\mapsto Z_X$
is completely positive and $Z_I=P_{\rm seen}$. In particular
$\|Z_X\|\le\|X\|$. One may see the last assertion without invoking a
general theorem: apply Cauchy--Schwarz to the sum
$\sum_j\langle BD^jv,XBD^jw\rangle$, and use
$\sum_j(D^*)^j B^*B D^j=P_{\rm seen}$.

Write
$$
\Theta(z)=A+\sum_{m\ge1}z^mF_m.
$$
On the unit circle its apparent dark-space poles are removable, and
$\Theta(e^{it})$ is unitary. This follows from (3.2)--(3.4), or directly
from the unitary colligation (2.1). The nonnegative Fourier coefficients
of $\Theta(e^{it})^*X\Theta(e^{it})$ are exactly
$$
\begin{aligned}
W_0(X)&=A^*XA+bZ_Xb,\\
W_k(X)&=A^*XBD^{k-1}b+bZ_XD^kb\qquad(k\ge1).
\end{aligned}
\tag{5.3}
$$
The negative coefficients are $W_{-k}(X)=W_k(X^*)^*$.
For $X=I$, these collapse to $W_0(I)=I$ and $W_k(I)=0$.
For a nonidentity insertion the actual matrix $Z_X$ remains.

Unitarity still imposes the exact scalar and norm constraints
$$
\operatorname{Tr}W_k(X)=\mathbf1_{\{k=0\}}\operatorname{Tr}X,\qquad
\sum_{k\in\mathbb Z}\|W_k(X)\|_{\rm HS}^2=\|X\|_{\rm HS}^2.
\tag{5.4}
$$
The first follows by cyclicity of trace and the second by Fourier
Parseval. Neither determines the individual mixed coefficients.
Absolute trace-norm convergence also gives
$$
\left\|\sum_{m\ge1}F_m^*XF_{m+k}\right\|_1
       \le\|X\|\operatorname{Tr}E.
\tag{5.5}
$$

There is a useful more explicit formula when $[X,E]=0$. In that case
$$
B^*XB=X-D^*XD+(U^*XU-X).
$$
Consequently, if $W_k^{(M)}(X)$ denotes the finite sum in (5.3),
$$
\boxed{\displaystyle
W_k^{(M)}(X)
 =\mathbf1_{\{k=0\}}X-b(D^*)^M X D^{M+k}b
   +b\sum_{j=0}^{M-1}(D^*)^j(U^*XU-X)D^{j+k}b.}
\tag{5.6}
$$
For $k=0$ its initial term is $A^*XA$, and for $k>0$ it is
$A^*XF_k$. This identity is proved by the same finite telescope; the
initial $bXD^kb$ cancels because $X$ commutes with $a,b$.
The boundary term has trace norm at most $\|X\|e_M$.
The remaining sum is an actual propagated commutator. Replacing it by an
endpoint density or by its separate absolute values would require an
additional estimate.

## 6. Positive open power-trace energy for the actual Fourier detector

### 6.1. A finite-dimensional Poisson inequality

Let $D$ be any invertible contraction of dimension $N$, and put
$$
c_D=-\log|\det D|\ge0.
$$
For every $s>0$,
$$
\boxed{\displaystyle
\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}|\operatorname{Tr}D^m|^2
\ge\frac12\left\{\frac1N
       \coth\!\left(\frac{s+c_D}{N}\right)-1\right\}.}
\tag{6.1}
$$

Proof. List the eigenvalues with algebraic multiplicity as
$\lambda_j=r_je^{i\theta_j}$, where $0<r_j\le1$, and write
$d_j=-\log r_j$. Nonnormality is immaterial: the trace of each power is
the sum of the corresponding eigenvalue powers. Moreover
$\sum_jd_j=c_D$. Set $t=e^{-2s/N}$. Every series below converges
absolutely, since $t<1$ and $|\operatorname{Tr}D^m|\le N$.
The Poisson identity
$$
1+2\sum_{m\ge1}v^m\cos(m\theta)
       =\frac{1-v^2}{|1-ve^{i\theta}|^2}>0\quad(0\le v<1)
$$
gives
$$
N^2+2\sum_{m\ge1}t^m|\operatorname{Tr}D^m|^2
 =\sum_{i,j}
     \frac{1-(tr_ir_j)^2}
          {|1-tr_ir_je^{i(\theta_i-\theta_j)}|^2}
 \ge\sum_j\frac{1+tr_j^2}{1-tr_j^2}
 =\sum_j\coth(s/N+d_j).
\tag{6.2}
$$
Every omitted term is positive. The function $\coth x$ is convex on
$(0,\infty)$, since its second derivative is
$2\operatorname{csch}^2x\,\coth x>0$. Jensen's inequality bounds the
last sum below by $N\coth((s+c_D)/N)$. Rearrangement proves (6.1).

### 6.2. A detector with uniformly bounded logarithmic determinant loss

For (1.1), suppose $\operatorname{Tr}E\le1/4$. Then $\|E\|<1$, so
$D$ is invertible, and
$$
c_D=-\tfrac12\log\det(I-E)
 \le\tfrac12\log(4/3)<\tfrac16.
\tag{6.3}
$$
Indeed, if $e_j$ are the nonnegative eigenvalues of $E$, then induction
using $(1-x)(1-y)\ge1-x-y$ gives
$\prod_j(1-e_j)\ge1-\sum_je_j\ge3/4$. The last strict inequality in
(6.3) follows from $\log(1+x)<x$, with $x=1/3$.

Take $s=1/4$ in (6.1). Since $s+c_D<5/12$ and
$\coth x>1/x$ for $x>0$, its right-hand side is strictly greater than
$$
\tfrac12(12/5-1)=7/10.
$$
This proves (1.4), including its full infinite tail.

For a concrete detector on the original family, choose consecutive
coordinate and frequency windows of equal size
$$
r_N=s_N=\lfloor\sqrt N/2\rfloor
$$
and set
$$
E_N=P_{I_N}\mathcal F_N^*P_{J_N}\mathcal F_NP_{I_N}.
\tag{6.4}
$$
Its trace is exactly $r_Ns_N/N\le1/4$. For all large $N$ both window
sizes are comparable to $\sqrt N$; their centers can be chosen at an
actual fixed point. The effect in (6.4), its square root, and
$D_N=\sqrt{I-E_N}\,U_N$ are exact finite matrices. Thus (1.4) holds for
all sufficiently large odd $N$, without discarding dimensions divisible
by $7$, and without any unproved assertion about a classical marker
quantization.

The inequality is for the Abel functional, not for a prescribed finite
band of times. It does not assert that a specified interval
$[cN,CN]$ alone carries the lower bound.

## 7. Exact feedback coefficients and the remaining interference

The determinant identity from the colligation is
$$
\det(I-zU)=\det(I-zD)\,
          \frac{\det(I-\Theta(z))}{\det(I+a)} .
\tag{7.1}
$$
For completeness, eliminate the lower block of
$$
\begin{pmatrix}I-A&-zB\\-b&I-zD\end{pmatrix}.
$$
Its Schur complement is $I-\Theta(z)$. Eliminating the upper block
instead gives
$$
(I+a)\quad\hbox{and}\quad
I-z\{D+b(I+a)^{-1}B\}=I-zU,
$$
because $a+b^2(I+a)^{-1}=a+(I-a)=I$.
This proves (7.1).

Logarithmic differentiation gives the exact analytic identity
$$
\sum_{m\ge1}z^m\operatorname{Tr}U^m
 =\sum_{m\ge1}z^m\operatorname{Tr}D^m
     +z\operatorname{Tr}\{(I-\Theta(z))^{-1}\Theta'(z)\},
\qquad |z|<1 .
\tag{7.2}
$$
Let $g_m$ be the coefficients of the last term, and put
$R=(I+a)^{-1}$. There is a finite expression for every coefficient:
$$
\boxed{\displaystyle
g_m=m\sum_{j=1}^{m}\frac1j
       \sum_{\substack{n_1,\ldots,n_j\ge1\\n_1+\cdots+n_j=m}}
       \operatorname{Tr}(RF_{n_1}\cdots RF_{n_j}).}
\tag{7.3}
$$
To verify it, write $Q(z)=\sum_{n\ge1}z^nF_n$, so
$I-\Theta=(I+a)(I-RQ)$, and expand
$-\log\det(I-RQ)=\sum_{j\ge1}j^{-1}\operatorname{Tr}(RQ)^j$ near zero.
For a fixed coefficient only $j\le m$ occurs; hence no convergence of
that expansion near the unit circle is assumed.

For the actual detector (6.4), define the positive weighted inner product
$$
\langle v,w\rangle_{s,N}
  =N^{-2}\sum_{m\ge1}e^{-2sm/N}v_m\overline{w_m}.
$$
The sequences in (7.2) belong to this space:
$|\operatorname{Tr}U^m|\le N$, $|\operatorname{Tr}D^m|\le N$, and
$|g_m|\le2N$. Consequently
$$
\|\{\operatorname{Tr}U^m\}\|_{s,N}^2
 =\|\{\operatorname{Tr}D^m\}\|_{s,N}^2+\|g\|_{s,N}^2
       +2\operatorname{Re}
        \langle\{\operatorname{Tr}D^m\},g\rangle_{s,N}.
\tag{7.4}
$$
The first term is $>7/10$ at $s=1/4$. The last two terms and their
interference with the first term have not been estimated to the accuracy
required by the CUE form factor. The mixed Ward relation (3.2) fixes the
identity insertion with one conjugated return; it does not supply the
noncommutative products of all composition lengths in (7.3), or their
correlations across $m$.

Thus this calculation supplies new exact constraints and a rigorous
obstruction to discarding an actual contribution. It proves neither
$H_{\rm diag}$ nor its negation. The first missing quantitative step in
this return formulation is control of the fully summed coefficients
(7.3), together with the mixed inner product in (7.4), on the scale
$m\asymp N$.
