# Fixed-map continuation: moment controls, a loop-test falsifier, and growing spectral transfer

**Claim ID:** `BGS-FM-003`

Date: 20--21 September 2026.

Status: exact finite-spectrum identities plus conditional asymptotic consequences. The fixed-\(\tau\) BGS estimate remains open.

## 1. Moment inequalities behind the first mixed levels

At \(w=is/2\), \(v=-is/2\), let \(Z=s_N(w)\), \(P=(Z/i-1)/2\),

\[
L=E|P|^2,\qquad C=E(P^2\bar P),\qquad Q=E|P|^4,\qquad r=\frac1{4s^2}.
\]

For every finite spectrum,

\[
\boxed{LQ\ge L^3+2|C|^2}
\tag{1}
\]

and

\[
\boxed{L+3\Re C\ge2L^2.}
\tag{2}
\]

The first is Bessel positivity after projecting \(|P|^2\) onto the mutually orthogonal functions \(1,P,\bar P\). The second is Cauchy--Schwarz in the positive measure \((\Im Z)\,dP_\alpha\).

If \(e=L+C-r\) and
\(g=\mathcal E_{3,N}(w,v,v)\), the exact low-order algebra gives

\[
Q=(1+2r)L-r+\frac g{16}-2\Re e.
\tag{3}
\]

Under the normalized \(p=2\) and \(p=3\) residual hypotheses used in the fixed-map frontier, Jensen first bounds the moments and then removes the normalization. Every subsequential limit \(\ell\) therefore obeys

\[
\boxed{
\frac{\sqrt{1+s^{-2}}-1}{2}
\le\ell\le
\frac{\sqrt{1+3/(2s^2)}-1}{2}.}
\tag{4}
\]

This strictly improves the earlier two-equation interval but still does not identify CUE.

## 2. An exact counterexample to one-upper tests at one selected height

Fix an integer \(m\ge2\). There is a unique \(x_m>0\) satisfying

\[
\sinh x_m=mx_m,
\qquad s_m=mx_m.
\]

For \(N=mJ\), take every \(J\)-th root of unity with multiplicity \(m\). The cotangent multiplication identity gives an exact resolvent

\[
s_N(w;\alpha)=\cot(-J\alpha/2-w/m).
\]

At \(w=is_m/2\), \(v=-is_m/2\), every residual in the restricted row

\[
\mathcal E_{b+1,N}(w,\underbrace{v,\ldots,v}_{b})
\]

vanishes for every integer \(b\ge1\). Nevertheless

\[
L_N(s_m)
=
\frac{\sqrt{1+s_m^{-2}}-1}{2}
<
\frac{1-e^{-2s_m}}{4s_m^2},
\tag{5}
\]

so the pair statistic is non-CUE.

The opposite third-order orientation detects the same spectra:

\[
\boxed{
\mathcal E_{3,N}(w,w,v)
=
\frac{2(m-\sqrt{1+s_m^2})}{m^2s_m^3}<0.}
\tag{6}
\]

Splitting each repeated root by \(o(1)\) in unfolded units makes every finite spectrum simple, keeps fixed-window local counts uniformly bounded, preserves the one-upper residual limits, and preserves the non-CUE pair limit. Thus simplicity and local-count control do not repair the restricted test.

This is an abstract spectral falsifier, not a realization by the frozen Anosov propagator.

## 3. Growing perturbation transfer

Let \(U\) be unitary of dimension \(N\), \(A=A^*\) centered, \(\|A\|_{\rm op}\le C\), and

\[
V=e^{iaA/N}U,\qquad
A_T=\frac1T\sum_{j=0}^{T-1}U^{-j}AU^j,\qquad
v_N(T)=\|A_T\|_2,
\]

where \(\|B\|_2^2=N^{-1}\operatorname{Tr}B^*B\). There is an eigenphase matching, in mean-spacing units, with RMS displacement \(q_N\) satisfying

\[
\boxed{
q_N
\le
\frac{|a|v_N(T)+a^2C^2(T-1)/N}{2\pi}.}
\tag{7}
\]

The proof follows the eigenphase flow \(U_s=e^{isaA/N}U\), replaces diagonal expectations by the time average in the instantaneous eigenbasis, controls the difference between \(A_{T,s}\) and \(A_T\) by telescoping powers, and integrates the velocity vector.

Hence if \(T_N=\lfloor c\log N\rfloor\) and
\(v_N(T_N)=O((\log N)^{-1/2})\),

\[
q_N=
O\!\left(\frac{|a_N|}{\sqrt{\log N}}
+\frac{a_N^2\log N}{N}\right).
\tag{8}
\]

In particular \(a_N=o(\sqrt{\log N})\) preserves every already-existing randomly rooted local point-process limit under this comparison.

For the retained odd-Pell normal form, \(\|\bar A_N\|_2^2=\sigma^2/K\), with \(\sigma^2=1650797/4000000\). The exact commuting model has RMS displacement

\[
\frac{|a|\sigma}{2\pi\sqrt K},
\]

and the normal-form comparison has an explicit quadratic error. Taking \(a=c\sqrt K\) produces a nonvanishing RMS limit. This shows that the \(o(\sqrt{\log N})\) condition cannot be enlarged to \(O(\sqrt{\log N})\) as a universal vanishing-RMS statement under these inputs.

For the actual frozen kick, \(a=\tau N^2\) in this normalization, far outside (8). Iterating small comparison steps does not create the missing cancellation.

## 4. Research consequence

Any loop-equation route must control varying off-real arguments and multiple distinguished orientations, including \((w,w,v)\); arbitrarily many successful \((w,v,\ldots,v)\) tests at one selected height are insufficient. Any perturbative transfer route must separately justify the model-specific time-average or normal-form estimates at the actual fixed strength.
