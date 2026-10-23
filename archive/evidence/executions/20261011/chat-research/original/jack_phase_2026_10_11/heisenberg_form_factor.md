# Form factors on the Heisenberg scale for frozen circular backgrounds

This note adds an unbounded-observable consequence to the point-process
theorem. It proves comparison of the phase-averaged form factor with its
finite circular mean for every trace sequence \(1\le n\le TN\), with any
fixed \(T<\infty\). The scattering background is still sampled from CUE,
COE or CSE and then frozen.

The exact CSE mean and fourth cumulant are known ensemble identities
(Haake–Sommers–Weber, arXiv:chao-dyn/9906024, equations (21)–(22)).
Their direct derivation here checks the conditional argument; it does not
establish novelty of those identities. `exact_cumulants.md` gives the
subsequently derived explicit all-time bounds, replacing the large coarse
constant below. `form_factor_curve.md` proves convergence of the entire
CUE/CSE curve in L² in rescaled time. `critical_cse_gaussian.md` extends
the closed-walk method to every fixed cumulant order.

Define

\[
p_n(Q)=\operatorname{tr}_\beta Q^n,\qquad
K_{N,Q}(n)=\frac1N\mathbb E_D|p_n(DQ)|^2,\qquad
\overline K_{\beta,N}(n)=\frac1N\mathbb E_{\mu_{\beta,N}}|p_n(Q)|^2.
\]

The established variance theorem gives the exact identity/inequality

\[
\mathbb E_Q|K_{N,Q}(n)-\overline K_{\beta,N}(n)|^2
\le\frac{\operatorname{Var}_{\mu_{\beta,N}}|p_n|^2}
{N^2(N+2/\beta)}.
\tag{1}
\]

It remains to bound a fourth trace moment at \(n\asymp N\).
That step does not follow from weak convergence of local point processes.

## 1. COE and CUE: every polynomial degree

Put \(\alpha=2/\beta\). The finite circular Jack norm relative to the
formal symmetric-function norm has the factor

\[
\mathcal N_\lambda^\alpha(N)=
\prod_{(i,j)\in\lambda}
\frac{N+(j-1)\alpha-(i-1)}{N+j\alpha-i},
\qquad \ell(\lambda)\le N.
\tag{2}
\]

This is the standard Jack circular orthogonality formula
(Jiang–Matsumoto, arXiv:1102.4123, Lemma 4.2).
Each factor is positive. When \(\alpha\ge1\), each is at most one,
regardless of the weight of the partition.

Expand the formal power sum \(p_{(n,n)}=p_n^2\) in Jack polynomials.
Finite specialization omits partitions of length greater than \(N\).
The coefficients in the squared norm contribute nonnegative terms.
Equation (2) therefore bounds the finite norm by the formal norm, which is

\[
\langle p_{(n,n)},p_{(n,n)}\rangle_\alpha
=\alpha^2 z_{(n,n)}=2\alpha^2 n^2.
\]

Hence for COE and CUE, for every positive integer \(n\),

\[
\mathbb E|p_n|^4\le2\alpha^2n^2.
\tag{3}
\]

The commonly stated condition \(2n\le N\) is needed for a two-sided
near-Gaussian moment comparison, not for this one-sided inequality.
Thus (1) gives, for \(n\le TN\),

\[
\boxed{\mathbb E_Q|K_{N,Q}(n)-\overline K_{\beta,N}(n)|^2
\le\frac{2\alpha^2T^2}{N+\alpha},\qquad\beta=1,2.}
\tag{4}
\]

For CUE, \(\overline K_{2,N}(n)=\min(n,N)/N\).
Thus its entire ramp and plateau are obtained in probability for every
fixed Heisenberg-scale trace sequence, for almost every typical frozen
background in the probabilistic sense of (4).

## 2. CSE: a direct Pfaffian calculation

A norm-factor maximum is too crude at \(\alpha=1/2\).
We instead control the connected fourth moment directly.

Let

\[
H_N=\{-N+\tfrac12,-N+\tfrac32,\ldots,N-\tfrac12\},
\qquad \phi_k(\theta)=e^{ik\theta}.
\]

The confluent determinant with columns
\((\phi_k(\theta_j),\phi_k'(\theta_j))\) equals
\(i^N|\Delta(e^{i\theta_1},\ldots,e^{i\theta_N})|^4\),
up to a fixed orientation sign. To verify this, subtract
\(i(-N+\tfrac12)\) times the first column of each pair from its derivative
column. Factoring powers of \(z_j=e^{i\theta_j}\) leaves the ordinary
polynomial confluent Vandermonde and the factor
\(i^N\prod_j z_j^{-2N+2}\). On the unit circle,

\[
|\Delta(z)|^4=\Delta(z)^4\prod_j z_j^{-2N+2}.
\]

Expanding the determinant and integrating its paired columns gives
the Pfaffian integral identity. Explicitly, the determinant sum has
\((2N)!\) terms, and pairing the two columns at each integration variable
produces the antisymmetric integrals below. Regrouping over matchings
gives \(N!\operatorname{Pf} A\). The factor \(N!\), orientation sign and
\(i^N\) cancel on dividing by the same expression at zero.

For
\(h(\theta)=u e^{in\theta}+v e^{-in\theta}\), write

\[
Z(u,v)=\mathbb E e^{u p_n+v\overline{p_n}}
=\frac{\operatorname{Pf}A(h)}{\operatorname{Pf}A(0)},\qquad
A(h)_{kl}=i(l-k)\int_0^{2\pi}
e^{i(k+l)\theta+h(\theta)}\frac{d\theta}{2\pi}.
\tag{5}
\]

Half-integer individual functions cause no periodicity problem:
\(k+l\) is an integer, and the determinant and all paired integrals
are periodic.

Let \((A_s)_{kl}=i(l-k)\mathbf1_{k+l+s=0}\), with an integer \(s\), and
\(B_s=A_0^{-1}A_s\).
Since \((A_0^{-1})_{k,-k}=1/(2ik)\),

\[
(B_s)_{kl}=\frac{2k-s}{2k}\,
\mathbf1_{l=k-s\in H_N},\qquad B_0=I.
\tag{6}
\]

These are finite weighted shifts, with no zero denominator.
The Taylor germ at \(u=v=0\) satisfies

\[
\log Z=
\frac12\operatorname{Tr}\log\left(
I+\sum_{a+b\ge1}\frac{u^av^b}{a!b!}B_{(a-b)n}\right).
\tag{7}
\]

Equation (7) uses \(\operatorname{Pf}(A)^2=\det A\) and the analytic
branch normalized by \(Z(0,0)=1\). It may also be interpreted purely as
a formal series of finite matrices, so no large-parameter convergence
assumption is involved.

## 3. The exact CSE mean and its singularity

Taking the coefficient of \(uv\) in (7) gives

\[
m_2:=\mathbb E|p_n|^2=N-\tfrac12\operatorname{Tr}(B_nB_{-n}).
\]

For \(1\le n<2N\), the active coordinates are
\(k\in H_N\) with \(k-n\in H_N\), a set of size \(2N-n\).
The product at a coordinate is

\[
\frac{(2k-n)^2}{4k(k-n)}
=1+\frac{n^2}{4k(k-n)}.
\]

Partial fractions, followed by reflection of the active interval, yield

\[
\boxed{
m_2=
\begin{cases}
\displaystyle\frac n2+\frac n4
\sum_{j=|N-n|}^{N-1}\frac1{j+\frac12},&1\le n\le2N,\\
N,&n\ge2N.
\end{cases}}
\tag{8}
\]

The sum is empty at \(n=2N\). In particular the \(n=1\) case gives
\(N/(2N-1)\), in agreement with the independent sharp-mode calculation.

The half-integer harmonic sum is at most \(2+\log(2N-1)\).
Therefore, for every \(n\ge1\),

\[
m_2\le n\left(1+\tfrac14\log(2N-1)\right).
\tag{9}
\]

At \(n=N\), the normalized mean in (8) grows like
\(\tfrac14\log N\). A finite limiting form-factor value must not be
claimed there.

## 4. A closed-walk bound for the fourth cumulant

Denote the complex mixed cumulant by

\[
\kappa_{2,2}=2!2!\,[u^2v^2]\log Z.
\]

In (7) it is a finite sum of traces of products of at most four \(B_s\).
Every shift is an integer multiple of \(n\), with \(|s|\le4n\).
A contributing trace has total shift zero.

Remove all zero shifts, since \(B_0=I\).
A nonempty contributing closed walk then has between two and four
nonzero steps. Its visited coordinates have the form \(k+t_jn\),
where the \(t_j\) are integers. Any one coordinate occurs at most twice:
three visits in a four-step cyclic walk would force a zero step.
Distinct centers are separated by at least \(n\).

For each starting coordinate \(k\), take a nearest distinct center.
Put \(d=\min_j|k+t_jn|\ge1/2\).
All other distinct denominator coordinates have absolute value at least
\(n/2\). By (6), their individual factors have absolute value at most five.
The nearest denominator can occur at most twice. Thus

\[
|\text{walk product}|
\le 5^4(1+2n/d)^2
\le625(2+8n^2/d^2).
\]

There are at most four distinct centers. Extending each half-integer sum
to the full lattice gives

\[
\sum_{k\in H_N}d^{-2}
\le4\sum_{q\in\mathbb Z+1/2}q^{-2}=4\pi^2.
\]

Consequently each such trace, including the all-zero case, obeys

\[
|\operatorname{Tr}(\text{product})|
\le2500N+20000\pi^2n^2
\le200000(N+n^2).
\tag{10}
\]

The constants are deliberately loose; only the order matters.

The sum of absolute scalar coefficient weights in (7) is

\[
\sum_{r=1}^4\frac1{2r}
 [u^2v^2](e^{u+v}-1)^r=\frac{13}{4}.
\]

For \(r=1,2,3,4\), the bracketed coefficients are respectively
\(1/4,7/2,9,6\). Differentiation contributes a further factor four.
Thus

\[
|\kappa_{2,2}|\le2\,600\,000(N+n^2).
\tag{11}
\]

Global rotation gives \(\mathbb Ep_n=\mathbb Ep_n^2=0\).
The moment-cumulant relation is exactly

\[
\mathbb E|p_n|^4=2m_2^2+\kappa_{2,2}.
\]

Combining (9) and (11), for \(n\le TN\),

\[
\mathbb E|p_n|^4
\le C_T N^2(1+\log N)^2.
\tag{12}
\]

This proves the needed uniform integrability bound by a finite-dimensional
calculation, including \(n=N\).

## 5. All positive CSE times, including the high-frequency tail

There is a sharper high-frequency conclusion. The matrix \(A_s\) vanishes
when \(|s|\ge2N-1\). At equality its only candidate entry has \(k=l\)
and hence is zero. Thus for \(n\ge2N-1\),

\[
Z(u,v)=\left(\sum_{a\ge0}\frac{(uv)^a}{(a!)^2}\right)^N,
\qquad m_2=N,\quad \kappa_{2,2}=-N,\quad m_4=2N^2-N.
\tag{12a}
\]

Equivalently, the labelled powered eigenangles become independent uniform
angles: the Laurent density \(|\Delta|^4\) has each coordinate exponent
bounded by \(2N-2\), and averaging its preimages under multiplication by
\(n\ge2N-1\) kills all nonconstant Fourier coefficients.

For \(n<2N-1\), (12) applies with \(T=2\); for larger \(n\), (12a)
applies. Consequently the bound below is absolute and uniform over all
positive trace orders.

## 6. CSE conditional form factor

Substituting (12) into (1) gives

\[
\boxed{
\mathbb E_Q|K_{N,Q}(n)-\overline K_{4,N}(n)|^2
\le C\frac{(1+\log N)^2}{N},
\qquad n\ge1.
}
\tag{13}
\]

This controls absolute fluctuations around the finite mean even at
\(n=N\), where that mean diverges logarithmically.
In the convention counting N distinct CSE eigenvalues, this singular point
is at half the Heisenberg time in the terminology of the 1999 source;
the plateau begins at n≈2N. The scale n proportional to N includes both.

From (8), if \(n/N\to\tau>0\) with \(\tau\ne1\), the deterministic mean
converges to

\[
K_4(\tau)=
\begin{cases}
\displaystyle\frac{\tau}{2}
-\frac{\tau}{4}\log|1-\tau|,&0<\tau<2,\ \tau\ne1,\\
1,&\tau\ge2.
\end{cases}
\tag{14}
\]

Equations (13)–(14) give this same pointwise limit in probability for
the frozen CSE background. At sequences approaching \(\tau=1\), (13)
still compares with the exact finite-size expression (8).

For CUE, the same Fourier-support argument gives independent powered
angles at \(n\ge N\), since \(|\Delta|^2\) has coordinate degree \(N-1\).
Together with (3) for \(n<N\), this yields
\(\sup_{n\ge1}\mathbb E|p_n|^4\le2N^2\), and hence a uniform
all-positive-time CUE comparison bound \(2/(N+1)\).
The exact fourth-cumulant calculation in `exact_cumulants.md` improves
this bound to (1−1/N)/(N+1), and supplies a moderate explicit constant
for the CSE bound (13).
The COE estimate (4) covers every prescribed finite \(T\).

The bounds are uniform for the indicated individual times; they do not claim that
the maximum over all O(N) times converges. Chebyshev plus a union bound
does give simultaneous comparison over any prescribed o(N/log^2 N)
CSE times, or o(N) COE/CUE times at a fixed error threshold.
It also gives convergence of the mean squared error averaged over
all \(1\le n\le TN\), by linearity of expectation. No independence
between different times is assumed.

## Scope and status

The algebraic argument is nonperturbative and reaches the Heisenberg scale
for these frozen random backgrounds. Its dependence on the circular
background has not been removed. Scientific priority is unestablished.
Finite computations and an independent audit are separate evidence and
are not substituted for the derivation above.

