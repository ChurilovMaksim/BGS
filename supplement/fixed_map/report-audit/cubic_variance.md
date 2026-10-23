# Exact CUE calibration of the cubic Heisenberg test

19 September 2026. Derived during the report audit. This is a reference
calculation with an explicit finite algebra certificate, not a universality
proof for a quantum map and not a claim of novelty. Dimension is N throughout.

## 1. Statistic and theorem

Let T(m)=Tr(V^m), V distributed as CUE_N. Let q_a be nonnegative real
weights, not all zero, supported on integers 2N/3<a<4N/5. Define

\[
Q=\sum_aq_a,\quad r_s=\sum_{a+b=s}q_aq_b,\qquad
Y=\frac{\sum_{a,b}q_aq_bT(a)T(b)T(-a-b)}{NQ^2}.
\]

Then

\[
\mathbb EY=\mu=\frac{2\sum_a a q_a}{NQ}-1,              \tag{1}
\]

and the exact *complex* variance, E|Y-mu|^2, is

\[
\begin{split}
N^2Q^4\operatorname{Var}_{\mathbb C}(Y)
={}&\sum_{s,t}r_sr_t[3N-2\min(s,t)]\\
&+4Q^2\sum_a a(a-N)q_a^2
+N\sum_s(N-s)r_s^2
+2N\left(\sum_a a q_a^2\right)^2.                    \tag{2}
\end{split}
\]

Some summands are negative; only their total is a variance. Treating
the traces as independent Gaussian variables would omit the first three
terms and would also give the wrong mean.

## 2. Cumulants needed for the proof

In the indicated frequency band, the exact finite-N cumulants are

\[
\begin{split}
K_3(a,b,-a-b)&=a+b-N,\\
K_4(b,-a-b,-c,a+c)&=a-N,\\
K_4(a,b,-c,-d)&=N-a-b\quad(a+b=c+d),\\
K_6(a,b,-a-b,-c,-d,c+d)&=3N-2\min(a+b,c+d).           \tag{3}
\end{split}
\]

All small variables a,b,c,d lie in (2N/3,4N/5). K_r denotes the actual
CUE joint cumulant, with its definition and ordered-partition formula in
`cue_reference.md`, equation (4).

The cubic formula was derived there. For K_4(b,-a-b,-c,a+c), the
two-block terms sum to 4N-(a+b+c)-|b-c|. The only surviving three-block
partition contributes 2(N-max(b,c)); the four-block terms all have span
at least one of a+b,a+c, hence exceed N. Adding the one-block term N
gives a-N.

For balanced (a,b,-c,-d), put s=a+b=c+d>N. All four variables are <N.
The two-block contributions consist of the four singleton splits and
the two cross-pair splits; the same-sign split has span s>N. The four
mixed pair/single/single partitions contribute twice
sum of N-max(x,y) over the four positive-negative pairs. Only two cyclic
singleton orders survive; their span is max(a,b,c,d). Combining these
terms gives
N-2s-|a-c|-|a-d|+2max(a,b,c,d)=N-s.
The last equality follows by writing a,b=s/2+/-x and c,d=s/2+/-y.

For K_6 the attached exact finite algebra certificate evaluates every
ordered partition symbolically in each chamber; it does not fit a
formula to sample values. Here is why the finite coverage is complete.

Every difference of two visited partial sums is a sum of a subset of
(a,b,-a-b,-c,-d,c+d). Its coefficients in a,b,c,d lie in {-1,0,1}.
If the coefficient sum is positive, the sign is fixed throughout the
band. If that sum is one, its value is strictly between zero and N;
if it is at least two, its value exceeds N. Explicit worst cases are
2*(4/5)-2/3=14/15<1 and 3*(2/3)-4/5=6/5>1.
For coefficient sum zero, the only possible walls are equality of two
variables or equality of the sums of two disjoint pairs.

After ordering the four variables x_1<x_2<x_3<x_4, the only pair-sum
wall whose sign remains undecided is x_1+x_4=x_2+x_3. Thus 24 orderings
times two sides give exactly 48 chambers. The witnesses with sorted
coordinates (72,73,76,78) and (72,74,76,77), at N=100, visit all of them.
In each chamber the maximizing and minimizing partial sums are fixed
linear forms and so are the active positive parts (N-span)_+.

`cubic_variance.py` computes their *rational coefficient vectors* over
all 203 set partitions and 4683 ordered partitions. All 48 checks yield
(3,-2,-2,0,0) when a+b<c+d and (3,0,0,-2,-2) on the other side, with
coordinates (N,a,b,c,d). This proves the last line of (3) on the open
chambers; continuity proves it on every wall as well. The certificate
and the chamber-coverage argument are both needed. Merely testing 48
numeric values would not prove the formula.

## 3. From cumulants to variance

Equivalently, put A_ab=T(a)T(b)T(-a-b), s=a+b, t=c+d. The covariance
kernel underlying (2) is

\[
\begin{split}
\operatorname{Cov}_{\mathbb C}(A_{ab},A_{cd})={}&3N-2\min(s,t)\\
&+a(a-N)(\delta_{ac}+\delta_{ad})
+b(b-N)(\delta_{bc}+\delta_{bd})\\
&+N(N-s)\delta_{st}
+Nab(\delta_{ac}\delta_{bd}+\delta_{ad}\delta_{bc}).    \tag{3a}
\end{split}
\]

In the sixth moment for |Y|^2, all singleton blocks have zero expectation.
The only two-triple partition with nonzero block sums allowed by rotation
invariance is the original triple and its conjugate; its contribution
is exactly |EY|^2 and cancels on centering. Every other partition that can
survive has block sizes (6), (4,2), or (2,2,2).

The (6) term is the first sum in (2). Among (4,2) partitions, there are
four small positive-negative matches: a=c, a=d, b=c, b=d. Their sum is
4Q^2 sum_a a(a-N)q_a^2, using K_2(a,-a)=a and (3). The large match
a+b=c+d contributes N sum_s(N-s)r_s^2, since s>N and K_2(s,-s)=N.
Finally the two complete pairings contribute
2N(sum_a a q_a^2)^2. This proves (2), including cases of equal frequencies:
partitions concern labeled factors, so those multiplicities must remain.

## 4. Nonzero CUE limit in L2, not just in expectation

For q_a=b(a/N), with nonzero nonnegative smooth b supported inside
(2/3,4/5), put B=int b and c=b*b. Riemann summation in (2) gives

\[
\operatorname{Var}_{\mathbb C}(Y)=\frac{V_b}{N}+o(N^{-1}),
\]

where

\[
\begin{split}
B^4V_b={}&\iint c(s)c(t)[3-2\min(s,t)]\,dsdt\\
&+4B^2\int x(x-1)b(x)^2dx
+\int(1-s)c(s)^2ds
+2\left(\int xb(x)^2dx\right)^2.                     \tag{4}
\end{split}
\]

For b symmetric about 3/4, (1) tends to 1/2, so Y tends to 1/2 in L2.
This conclusively refutes a universal zero target for this connected
cubic Heisenberg test, even as a claim of convergence in probability
for the CUE reference.

The O(1/N) bound also has a proof independent of the exact sixth-cumulant
certificate: the general ordered-partition identity gives |K_r|<=C_r N.
After the two-triple term cancels, there are O(N^4) unrestricted (6)
terms of size O(N), O(N^3) pair-constrained (4,2) terms of size O(N^2),
and O(N^2) full-pairing terms of size O(N^3). Each is O(N^5) in total,
whereas N^2Q^4 is of order N^6. The frequency-band argument above excludes
any additional two-triple contribution. Thus the nonzero limiting target
does not depend on trusting a long symbolic simplification.

## 5. Calibration of the deterministic experiment

For the bump actually used in `monodromy_experiment.py`, supported in
(0.71,0.79) and centered at 0.75, (2) gives CUE root mean square
fluctuations 2.65136, 1.12366 and 0.46543 at N=41,239,1393 respectively.
At N=1393 the deterministic complex cubic values are approximately

| kappa | Y | CUE mean | Distance / CUE RMS |
|---|---|---|---|
| 0.0001 | 0.49041 + 0.74025 i | 0.5 | 1.591 |
| 0.0004 | 0.29316 + 0.23109 i | 0.5 | 0.666 |

These ratios are not p-values and do not prove that the deterministic
model follows CUE. They do show why its visible imaginary cubic part
cannot by itself be treated as evidence of failure: a narrow test still
has substantial finite-N fluctuations in the CUE reference.

Verification also includes the independent CUE-density constant-term
calculation at N=4,q_3=1, yielding mean 1/2 and complex variance 13/4,
and a two-mode exact rational check at N=26,q_19=1,q_20=2 against the
unsimplified general moment formula. The full outputs are in
`cubic_variance.json`. No random-matrix simulation is substituted for
this reference calculation.

A separate focused agent review reconstructed (3a) and the chamber
argument. Its verifier enumerates 1082 cyclic ordered partitions via onto
maps, independently of the author's set-partition generator, and checks
all 49 distinct subset coefficient vectors plus equality-wall cases.
The saved script and output are `independent_variance_review.py` and
`independent_variance_review.json`. This is an additional internal check,
not external peer review or a formal proof-assistant certificate.
