# Singular-value contraction under Schur feedback and stopped quantum gaps

**Stable claim:** BGS-TRACE-073. **State:** CONDITIONAL for the stopped gap;
the deterministic singular-value contraction is unconditional under its
displayed invertibility hypothesis. All (C1)--(C7) were independently
reconstructed internally; this is not external refereeing.
The general complex-contraction and reversal extension (C8)--(C9) had a
separate internal reconstruction recorded in Section 7.
**Base:** main `4c2afe539ff6b84be907899b38c8e80f94f547e8`.
The stochastic-complement construction is standard. Priority for the
singular-value comparison is not established. No BGS theorem is asserted.

## 1. Every singular value decreases under classical censoring

Let P be an N-dimensional nonnegative doubly stochastic matrix. Partition
its coordinates into a retained set A of size 1<=a<=N and a deleted set D. Assume
I-P_DD is invertible. The stochastic complement is

$$P^c=P_{AA}+P_{AD}(I-P_{DD})^{-1}P_{DA}.$$

It is nonnegative and doubly stochastic. With J_n=11*/n, let the singular
values on the constant-orthogonal spaces be ordered decreasingly. Then

$$\sigma_j(P^c-J_a)\le\sigma_j(P-J_N),\qquad 1\le j<a.\tag{C1}$$

In particular every Schatten norm, including the operator norm, contracts.
This is a singular-value assertion; no assertion about ordered nonnormal
eigenvalue moduli is needed.

Proof. The inverse has nonnegative entries because the transient
substochastic block has spectral radius less than one. The row and column
sum identities give P^c1=1 and 1*P^c=1*. For x in 1-perp on A, put
t=(I-P_DD)^(-1)P_DA x, z=(x,t), and z0=z-(1*z/N)1. Then
Pz=(P^c x,t), so Pz and z have the same mean. For any 0<=s<=1,

$$\|(P-J_N)z_0\|^2-s^2\|z_0\|^2
=\|(P^c-J_a)x\|^2-s^2\|x\|^2
 +(1-s^2)\left(\|t\|^2-\frac{|1^*t|^2}{N}\right).\tag{C2}$$

The final term is nonnegative, since |1*t|^2<=|D| ||t||^2.
The lift x->z0 is injective: a constant z with a mean-zero retained part
must have retained part zero. If a j-dimensional subspace has
||P^c x||>s||x|| for every nonzero x, its lifted subspace has the same strict
inequality for P-J_N. The positive index of Q*Q-s^2I is the number of
singular values of Q exceeding s. This proves (C1), by varying s. All
singular values are at most one because doubly stochastic matrices contract
Euclidean norm. The case a=1 has no centered singular values.

## 2. Exact mean and a bounded coherent increment

Use the unitary feedback process of
[TRACE-060](delay_bootstrap.md). At a retained size u, order the
eliminated port last and write

$$S=\begin{pmatrix}A&c\\b&a\end{pmatrix},\quad
d=1-|a|^2,\quad q=\frac{w}{1-aw},\quad S'=A+cqb,$$

where w is fresh uniform circle phase, conditional on the past and on the
chosen port. Write delta=max_ij |S_ij|^2<1 and P=|S|^2 entrywise. The
conditional mean of P'=|S'|^2 is precisely the one-port classical complement:

$$\mathbb E_w P'=P_{AA}+\frac{|c|^2|b|^2}{d}=P^c.\tag{C3}$$

For C=diag(c) conjugate(A) diag(b), R=|c|^2|b|^2, and
z=|q|^2-1/d, the entire coherent increment is

$$M=P'-P^c=qC+\bar q\bar C+zR,\qquad \mathbb E_wM=0.\tag{C4}$$

Both row and column sums of M are zero. Unitarity gives
||C||op<=delta and ||R||op<=delta d. Moreover
|q|<=1/(1-sqrt(delta)) and
|z|d<=|q|^2d+1<=2/(1-sqrt(delta)). Consequently

$$\|M\|_{op}\le\frac{4\delta}{1-\sqrt\delta}\le8\delta
\quad\hbox{if }\delta\le\tfrac14.\tag{C5}$$

This estimate includes all rectangular coherences. Averaging the classical
complement and then iterating a deterministic mean matrix would be invalid.

## 3. A self-contained smooth potential

For an even integer p>=2, an arbitrary complex square matrix X, and r>=0,
set F_r(X)=(||X||_p-r)_+^2. It has a real Frechet derivative and

$$F_r(X+H)\le F_r(X)+DF_r(X)[H]+(p-1)\|H\|_p^2.\tag{C6}$$

Here and below the Schatten norm is unnormalized. A proof, rather than an
unverified appeal to a matrix concentration theorem, is useful because the
coordinate spaces change. For Hermitian Y let g(t)=Tr(Y+tZ)^p. Polynomial
differentiation gives p(p-1) trace words in g'', each bounded in absolute
value by ||Y+tZ||_p^(p-2)||Z||_p^2 using Schatten Holder. Differentiating
g^(2/p) and dropping its nonpositive squared-first-derivative term gives
(||Y+tZ||_p^2)''<=2(p-1)||Z||_p^2. The Hermitian dilation
[[0,X],[X*,0]] transfers exactly this bound to complex matrices; its factor
2^(1/p) cancels on both sides.

On intervals where n(t)=||X+tH||_p>r, the second derivative of
(n-r)^2 is 2(n')^2+2(n-r)n'', at most the second derivative of n^2,
because n''>=0 by convexity. The derivative matches zero at n=r. Integrate
the second-derivative bound to obtain (C6); at a zero of n, the homogeneous
quadratic norm has zero first derivative and the same integral bound.
This is the usual uniform smoothness mechanism, reconstructed here.

## 4. All-time stopped gap estimate

Fix K>0, ell=log(2N), an integer m<N with m>=4K ell, and the event

$$\mathcal A_m=\{\max_{ij}|(S_u)_{ij}|^2\le K\ell/u
                  \text{ for every }N\ge u\ge m\}.$$

Initially ||P_N-J_N||op<=rho0. Choose an even p>=2 and a threshold
g>N^(1/p)rho0. Then

$$\mathbb P\left(\mathcal A_m\cap
 \{\max_{N\ge u\ge m}\|P_u-J_u\|_{op}\ge g\}\right)
\le\frac{64N^{2/p}(p-1)K^2\ell^2}
           {m\,(g-N^{1/p}\rho_0)^2}.\tag{C7}$$

This is an intersection-probability estimate, not an estimate conditional
on a future event and not a bound for P(A_m^c).

Proof. Stop at the first flatness or gap crossing, including simultaneous
crossings. Keep the complete centered matrix X_u=P_u-J_u at the crossing,
padded with zeros to dimension N, thereafter. Center before padding; never
subtract J_N from the padded raw P_u. Before a
transition, (C1) gives
||P^c-J_(u-1)||_p<=||P_u-J_u||_p. Choose r=N^(1/p)rho0;
the initial potential F_r is zero. Conditional first on the chosen port,
apply (C6) and (C4); its linear term averages to zero. By (C5),

$$\mathbb E[\Delta F_r\mid\text{past}]
\le64N^{2/p}(p-1)(K\ell/u)^2.$$

The inequality applies to the crossing transition, whose old state is
still admissible. After the stop the increment is zero. Summing through
size m and using sum_(u=m+1)^N u^-2<=1/m bounds the final expectation.
A gap crossing before any flatness failure has F_r>=(g-r)^2. On A_m, every
gap crossing is of this kind, including one simultaneous with a flatness
crossing in the larger event used for the upper bound. Markov's inequality
proves (C7). No future-dependent linear propagator appears in a martingale
inequality; uniform coordinate selection is not required for this gap bound.

Take p=2 ceil(ell). Then N^(1/p)<=sqrt(e). If rho0<g/sqrt(e) is fixed and
m=ceil(ell^(3+kappa)) for any fixed kappa>0, the right side is
O_(K,g,rho0,kappa)(ell^(-kappa)). Thus initial small singular gap propagates
to every retained size down to this scale on the all-time flatness event,
outside the displayed exceptional probability. The maintained map supplies
an eventually much smaller rho0 through FM-021. It does not yet supply the
probability of A_m.

## 5. Why mean-gap contraction alone would be false for the sample

Let S be the normalized 4 by 4 Walsh matrix and eliminate its first port.
It has P=J_4. At w=1, a=1/2 and q=2; the resulting 3 by 3 scattering matrix
is a permutation matrix. Hence its centered intensity norm equals one,
although its conditional mean is J_3 with centered norm zero. This exact
example does not refute (C7): a single phase point has probability zero,
and the example has no growing polylogarithmic cavity. It rejects the
incorrect inference that every quantum realization inherits the gap of
the classical complement.

## 6. Frontier

The theorem removes a separate endpoint-gap premise once all-time entry
flatness is supplied and the initial gap is small. Together with the
conditional delay argument it narrows the physical cavity prerequisites.
It does not establish all-time entry flatness, identify the scalar
microscopic law, remove deterministic noise, close signed TRACE-005, or
prove BGS. Finite energy identities and feedback controls have separate
execution scope; they are not the asymptotic proof.

The preceding review input and the exact internal review scope are retained
in the [cavity continuation](../../archive/record/cavity_continuation_20261011.md).
The all-fixed-moment delay improvement has cutoff ell^(1+kappa); this gap
estimate has cutoff ell^(3+kappa). They are not the same scale.

## 7. General contractions and the reversal channel

The lift argument has a second application that does not remove a Perron
mode. Let C be any complex square matrix with ||C||op<=1, and suppose
I-C_DD is invertible. For its algebraic Schur complement
Cc=C_AA+C_AD(I-C_DD)^(-1)C_DA, every ordered singular value satisfies

$$\sigma_j(C^c)\le\sigma_j(C),\qquad 1\le j\le|A|.\tag{C8}$$

No positivity, stochasticity, normality or reversibility is required.
For arbitrary x on A put t=(I-C_DD)^(-1)C_DA x and z=(x,t). The exact identity

$$\|Cz\|^2-s^2\|z\|^2
 =\|C^c x\|^2-s^2\|x\|^2+(1-s^2)\|t\|^2$$

first proves ||Cc||op<=1 at s=1. For 0<=s<=1 its final term is nonnegative;
the injective lift transfers every strictly positive singular subspace of
Cc above s to C. Positive inertia and varying s prove (C8). Thus every
Schatten-p norm also contracts after zero padding. This argument is distinct
from the centering needed for P-J in Section 1.

For a unitary S define the Hermitian reversal matrix
R(S)_ij=S_ij conjugate(S_ji). Its absolute row sums are at most one:

sum_j |R_ij|=sum_j sqrt(P_ij P_ji)<=sqrt(sum_j P_ij sum_j P_ji)=1.

The same holds for columns, so ||R||op<=1. The pointwise inequality
|R_ij|<=P_ij is generally false and is not used.

Write S=[[A,c],[b,a]], d=1-|a|², q=w/(1-aw),
C0=diag(c) A* diag(b), and v_i=c_i conjugate(b_i). Expanding the reverse
product of S'=A+c q b gives exactly

R(S')=R_AA+q C0+conjugate(q) C0*+|q|² v v*.

Since R_Ae=v, R_eA=v*, R_ee=|a|², the fresh-phase mean is
R_AA+v v*/d=Rc. It therefore contracts the full singular spectrum by (C8).
If delta=max_ij |S_ij|²<=1/4, then ||C0||op<=delta and
||v||²=sum_i |c_i|²|b_i|²<=delta d. The centered Hermitian noise has
mean zero and the same bound as (C5):

||q C0+conjugate(q)C0*+(|q|²-1/d)vv*||op
 <=4delta/(1-sqrt(delta))<=8delta.

Consequently, with the event A_m and other conditions of Section 4, an initial
||R_N||op<=rho_R, even p>=2 and g>N^(1/p)rho_R imply

$$\mathbb P\left(\mathcal A_m\cap
 \{\max_{N\ge u\ge m}\|R_u\|_{op}\ge g\}\right)
 \le\frac{64N^{2/p}(p-1)K^2\ell^2}
 {m\,(g-N^{1/p}\rho_R)^2}.\tag{C9}$$

To prove this, apply the already proved F_r potential with
r=N^(1/p)rho_R to R_u itself, padded with zeros. Do not subtract J.
The conditional mean complement contracts F_r by (C8), the linear fresh
noise has zero mean, and its Schatten-p square is bounded by
64 N^(2/p) delta_u². Sum the same stopped drift, retaining the full first
flatness/reversal-gap crossing, including simultaneous exits. This gives
(C9) by the same nonnegative crossing-potential estimate used in (C7).
Coordinate selection may be adapted to the past; no phase-conditioned future
event is inserted into the martingale argument.

For the maintained fixed-coupling odd-dimensional map,
[FM-022](../reversed_path_decay.md) has precisely this R_N and proves
||R_N||op->0, without an effective startup. Thus p=2ceil(ell),
m=ceil(ell^(3+kappa)) and any fixed g in (0,1), with a fixed sufficiently
small rho_R, give O(ell^(-kappa)) intersection failure. A finite union bound
joins intensity and reversal gap control on the same all-time flatness event.
This is not a complete symmetry classification or a proof of the scalar
cavity law. It does not establish the probability of A_m or deterministic BGS.

The [separate reversal review](../../archive/record/reversal_channel_continuation_20261011.md)
records its analytic reconstruction and finite symbolic execution. No world
priority or analytic Lean formalization is asserted.
