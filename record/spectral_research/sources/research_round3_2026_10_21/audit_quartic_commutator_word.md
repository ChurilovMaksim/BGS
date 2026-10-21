> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round3_2026_10_21/audit_quartic_commutator_word.md`. Embedded SHA256: `ac9afae71b2c9ad15bc00b4a2b98da25473131bcff15072432c605060b4118c6`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Exact quartic commutator estimate at N=d^4

Date: 2026-10-21. Independent reconstruction for the original Hamiltonian.

## 0. Outcome

**The proposed extension survives the exact-operator check.** A uniform
finite-word estimate can be proved without a high-frequency Egorov theorem
or an assumed Fourier-integral-operator amplitude.

Let $d$ be odd, $N=d^4$, $\delta=d^{-1}$,
$h=(2\pi N)^{-1}$, $t=\tau/(2\pi)$, and retain the original
$\tau=10^{-80}$. Write $E_N=e^{i\tau N A_N}$. For the mixed choice
$$
R_N=T_N(N/d,0),\qquad S_N=T_N(0,N/d),
$$
put
$$
C_{0,N}=E_N^*S_NE_N,\qquad
C_{j+1,N}=R_NC_{j,N}R_N^{-1}C_{j,N}^{-1},\quad j=0,1,2.
$$
For the physical Weyl quantization $Q_N$ and corrected actual symbol
$a$ specified below, the following safe constants are valid:
$$
\boxed{
\|C_{3,N}-I-i\tau Q_N(g)\|
\le 10^{18}\tau^2+10^{21}\tau/d,\qquad
g=-\partial_q^3\partial_p a.}
\tag{0.1}
$$

The arithmetic agent's same-direction choice
$$
R_N=S_N=T_N(-N/d,0)
$$
obeys the identical estimate with
$$
\boxed{g=\partial_q^4a.}
\tag{0.2}
$$
The conventions must not be interchanged: their leading symbols differ.

There is also a fixed smooth real $G=G_\tau$, explicitly constructed in
Section 8, such that for either choice
$$
C_{3,N}=Q_N(e^{iG})+O_a(\tau/d),\qquad
G=\tau g+O_{C^r,a}(\tau^2)
\tag{0.3}
$$
for every fixed $r$. The quantitative linear statement (0.1) already
suffices for the oldspace escape application.

For the canonical oldspace projection $\mathsf P_{d,N}$, Section 9 gives
an actual fixed gap for all sufficiently large odd $d$:
$$
\|\mathsf P_{d,N}E_N\mathsf P_{d,N}\|
\le\sqrt{1-(\tau\sigma/32)^2}<1,\qquad
\sigma^2=\int_{\mathbb T^2}g^2>0.
\tag{0.4}
$$
For instance $d\ge10^{24}$ is a safe sufficient threshold with the
displayed deliberately loose constants.

This excludes near-invariance of these canonical oldspaces at
$d=N^{1/4}$. It does not prove the full $H_{\rm diag}$, a pair limit, or
the absence of all arithmetic spectral effects.

## 1. Exact symbol, Weyl conventions, and generators

The exact source is
research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md,
SHA-256
42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b.
Its definitions and descent signs were read directly.

Write $X\psi(q)=q\psi(q)$, $P=-ih\partial_q$, so $[P,X]=-ihI$.
On the line let
$$
W_h(k,l)=e^{2\pi i(kX+lP)},\qquad
Q_h(b)=\sum_{k,l}\widehat b(k,l)W_h(k,l).
$$
Explicitly,
$$
(W_h(k,l)\psi)(q)
=e^{2\pi ik(q+l/(2N))}\psi(q+l/N).
\tag{1.1}
$$
On the specified odd torus fiber,
$$
Q_N(e^{2\pi i(kq+lp)})=(-1)^{kl}T_N(l,k).
\tag{1.2}
$$
The real physical symbol descending exactly to $A_N$ is
$$
\begin{aligned}
a(q,p)&=\cos14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin2\pi q}{100}-\frac1{10}\\
&\quad+\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100},\\
r(q)&=(1-\cos14\pi q)(1+\cos2\pi q).
\end{aligned}
\tag{1.3}
$$
Its support satisfies $|k|+|l|\le9$, and
$$
\|a\|_{\mathcal F}:=\sum|\widehat a(k,l)|\le
1+0.4+0.04+0.1+0.04<2.
\tag{1.4}
$$
Set $A_h=Q_h(a)$ and $E_h=e^{itA_h/h}$. This is the actual bounded
self-adjoint Schrödinger exponential; $t/h=\tau N$.

For the mixed choice, use
$$
H_0=P,\quad L=X,\quad H_1=E_h^*XE_h.
$$
Then $R(u)=e^{iuH_0/h}$, $B(u)=e^{iuH_1/h}
=E_h^*e^{iuX/h}E_h$. At $u=\delta$ these descend to $R_N,C_{0,N}$.

For the same-direction choice, use
$$
H_0=L=-P,\qquad H_1=E_h^*(-P)E_h.
$$
Their exponentials give exactly the negative plus-shift finite matrices
specified in (0.2).

In the parameter argument below, $h$ and $t$ are held fixed while
$u$ runs from zero to $\delta$. The relation $h=\delta^4/(2\pi)$
is substituted only at the final endpoint. No differentiation changes
the Planck constant.

## 2. A uniformly convergent exact Fourier Heisenberg series

For $\kappa=(k,l)$, $\eta=(k',l')$, let
$\omega(\kappa,\eta)=lk'-kl'$. Direct Weyl multiplication gives
$$
W_h(\kappa)W_h(\eta)
=e^{2\pi^2ih\omega(\kappa,\eta)}W_h(\kappa+\eta).
$$
Define the exact symbol operator $\mathcal L_h$ by
$$
Q_h(\mathcal L_h b)=\frac{-i}{h}[A_h,Q_h(b)].
$$
Its Fourier multiplier in each pair of frequencies is
$$
\frac2h\sin(2\pi^2h\omega),\qquad
\left|\frac2h\sin(2\pi^2h\omega)\right|
\le4\pi^2|\omega|.
\tag{2.1}
$$
This bound holds at every $h>0$. No small-$h$ expansion has been made.

For $b=\partial_p a$ or $\partial_q a$,
$$
\operatorname{supp}\widehat b\subset\{|\kappa|_1\le9\},\qquad
\|b\|_{\mathcal F}<120.
$$
After $n$ brackets, support lies in $|\kappa|_1\le9(n+1)$.
At bracket number $j$, the bound in (2.1) costs at most
$4\pi^2\cdot9^2j\|a\|_{\mathcal F}<7000j$. Consequently
$$
\|\mathcal L_h^n b\|_{\mathcal F}\le120\cdot7000^n n!.
\tag{2.2}
$$

For fixed $h$, the ordinary bounded-operator exponential series proves
the Heisenberg identity. Bound (2.2) then makes its Fourier version
absolutely convergent uniformly in $h$ for the fixed tiny physical time.
In particular,
$$
v_h(t)=\sum_{n\ge0}\frac{t^{n+1}}{(n+1)!}\mathcal L_h^n b
\tag{2.3}
$$
is an exact periodic symbol, and
$$
H_1=L-Q_h(v_h(t)).
\tag{2.4}
$$
Here $b=a_p$ in the mixed case and $b=a_q$ in the same-direction case.
The sign follows directly from
$$
\frac{d}{ds}(E_h(s)^*LE_h(s))
=\frac{i}{h}E_h(s)^*[L,A_h]E_h(s)=-E_h(s)^*Q_h(b)E_h(s).
$$

For the weighted Fourier norms
$$
\|c\|_r=\sum_\kappa|\widehat c(\kappa)|(1+|\kappa|_1)^r,
$$
support control and (2.2) give, whenever $|t|\le10^{-12}$,
$$
\|v_h(t)\|_r\le240\,10^r|t|,\qquad 0\le r\le4.
\tag{2.5}
$$
Indeed $7000|t|\le7\cdot10^{-9}$, and the remaining sum
$\sum_{n\ge0}(7000|t|)^n(n+1)^{r-1}$ is less than two.

For the third $q$-derivative of the remainder after its first term,
$$
\begin{aligned}
\|\partial_q^3(v_h(t)-tb)\|_{\mathcal F}
&\le120\cdot60^3|t|
\sum_{n\ge1}(7000|t|)^n(n+1)^2\\
&\le 2\cdot10^{12}t^2.
\end{aligned}
\tag{2.6}
$$
For the last inequality, the sum is at most $5\cdot7000|t|$ on the
stated time interval. The estimate is uniform in $h$.
The same series, with any fixed extra Fourier weight, proves smoothness;
an exponential Fourier weight with a sufficiently small fixed exponent
also converges at this time.

Thus analyticity loss is controlled by an explicit convergent series,
not by an unspecified theorem with a time threshold that might be
smaller than the prescribed $10^{-80}$.

## 3. Uniform mixed scaled commutators

Let $\mathcal D_jF=(i/h)[H_j,F]$, $j=0,1$.
All identities are first made on Schwartz functions, a common invariant
core, and then extended whenever the resulting operator is bounded.

For any Fourier symbol $c$,
$$
\frac{i}{h}[P,Q_h(c)]=Q_h(\partial_qc),\qquad
\frac{i}{h}[X,Q_h(c)]=-Q_h(\partial_pc).
\tag{3.1}
$$
Also the exact Moyal multiplier implies
$$
\left\|\frac{i}{h}[Q_h(b),Q_h(c)]\right\|_r
\le4\pi^2\|b\|_{r+1}\|c\|_{r+1}.
\tag{3.2}
$$
Here the norm denotes the Fourier norm of the displayed commutator
symbol. The inequality
$1+|\kappa+\eta|\le(1+|\kappa|)(1+|\eta|)$ proves the weighted version.

Write $D_h=H_1-L=-Q_h(v_h)$. Equations (2.5), (3.1), and (3.2) show
that, for $r\le3$, either $\mathcal D_j$ applied to a periodic symbol
costs at most $7\|c\|_{r+1}$. The coefficient from $D_h$ is less than
$4\pi^2\cdot10^7|t|<0.001$; the linear-coordinate coefficient is $2\pi$.

In the mixed case the first commutator is
$$
\mathcal D_0H_1=I-Q_h(\partial_qv_h).
$$
Its scalar part vanishes under any further commutator. In the
same-direction case even this scalar part is absent. Therefore every
mixed commutator of depth four obeys
$$
\boxed{
\left\|
\left(\frac{i}{h}\right)^4
\operatorname{ad}_{H_{i_1}}\operatorname{ad}_{H_{i_2}}
\operatorname{ad}_{H_{i_3}}\operatorname{ad}_{H_{i_4}}H_j
\right\|\le10^{12}|t|,
}
\tag{3.3}
$$
for all choices of the five indices in $\{0,1\}$.
For example $7^3(2\pi)\|v_h\|_4<10^{12}|t|$ already suffices.

The first commutators are bounded; depths two through four are
$O(|t|)$. Thus every operator-domain and Taylor-remainder step below
uses bounded operators after the first bracket. Since $A_h$ is a finite
sum of smooth multiplications and translations, its exponential
preserves Schwartz space; (2.4) also shows that $H_1$ is a bounded
perturbation of $L$.

## 4. A finite-word lemma with an operator-norm remainder

For fixed $h,H_0,H_1$, set
$$
W_0(u)=e^{iuH_1/h},\qquad
W_{j+1}(u)=e^{iuH_0/h}W_j(u)e^{-iuH_0/h}W_j(u)^{-1}.
$$
The word $W_3$ has 22 exponential factors, eight of them of type
$e^{\pm iuH_1/h}$.

Put
$$
K_h=\left(\frac{i}{h}\right)^3
\operatorname{ad}_{H_0}^3H_1.
\tag{4.1}
$$
This is bounded and self-adjoint. The left logarithmic generator satisfies
$$
\boxed{
\left\|\frac{h}{i}W_3'(u)W_3(u)^*-4u^3K_h\right\|
\le10^8M_4u^4,\qquad 0\le u\le1,
}
\tag{4.2}
$$
where $M_4$ bounds all mixed scaled commutators of depth four.
No norm bound on the unbounded $H_j$ is required.

Here is a direct proof of the lemma. Differentiate the finite word.
The left generator is a sum of 22 terms, each a signed $H_j$ conjugated
by a prefix of at most 21 factors. For a single conjugation, Duhamel's
formula gives the Taylor expansion with integral remainder
$$
\operatorname{Ad}_{e^{\pm iuH/h}}F
=\sum_{r=0}^{s-1}\frac{(\pm u)^r}{r!}
\left(\frac{i}{h}\operatorname{ad}_H\right)^rF
+\mathcal R_s,\qquad
\|\mathcal R_s\|\le u^sM_s/s!.
$$
It remains valid for $F=H_j$ once its first commutator is bounded.

Expand prefix conjugations from right to left, retaining total degree
at most three. A remainder born after a term of degree $r$ uses
$4-r$ further brackets; hence its total bracket depth is exactly four.
Previously formed remainders pass through the remaining unitary
conjugations without norm amplification. There are fewer than
$22\cdot21\binom{24}{3}<10^8$ possible remainder terms; factorial
coefficients can only reduce this bound. Each contributes at most
$M_4u^4$.

The coefficients through degree three are universal formal Lie
coefficients. They can also be determined without expanding 22 factors:
for formal $X,Y$,
$$
[e^{uX},e^{uY}]=I+u^2[X,Y]+O(u^3),
$$
where the brackets on the left denote group commutators. Commuting once
more with $e^{uX}$ gives
$I+u^3[X,[X,Y]]+O(u^4)$, and a third time gives
$$
W_3(u)=I+u^4[X,[X,[X,Y]]]+O(u^5).
$$
With $X=iH_0/h,Y=iH_1/h$, the left-generator coefficients of degrees
zero, one, and two vanish, and the degree-three coefficient is
$4K_h$. This identifies the finite Taylor polynomial in the already
justified bounded-generator expansion, rather than assuming that an
unbounded exponential series converges in operator norm. It proves (4.2).

Compare $W_3(u)$ to $Z(u)=e^{iu^4K_h/h}$, whose left generator is
exactly $4u^3K_h$. Unitary Duhamel comparison gives
$$
\|W_3(\delta)-e^{i\delta^4K_h/h}\|
\le\frac{10^8M_4}{5h}\delta^5.
\tag{4.3}
$$
This is the required uniform word estimate.

## 5. Applying the word lemma at the critical scale

By (3.3), $M_4\le10^{12}|t|$. Substitute
$h=\delta^4/(2\pi)$ and $t=\tau/(2\pi)$ only now:
$$
\|W_3(\delta)-e^{i2\pi K_h}\|
\le 10^{20}\tau\delta/5
\le10^{21}\tau\delta.
\tag{5.1}
$$

The leading symbol follows exactly from (3.1), with no Egorov remainder:
$$
K_h=
\begin{cases}
-Q_h(\partial_q^3v_h),&H_0=P,\ b=a_p,\\
+Q_h(\partial_q^3v_h),&H_0=-P,\ b=a_q.
\end{cases}
\tag{5.2}
$$
Equation (2.6) therefore gives
$$
\|K_h-tQ_h(g)\|\le2\cdot10^{12}t^2
\tag{5.3}
$$
with the $g$'s in (0.1)–(0.2).
The crude Fourier bound $\|g\|_{\mathcal F}<3\cdot10^7$ yields
$\|K_h\|\le4\cdot10^7|t|$ on the stated time interval.

For bounded self-adjoint $K_h$,
$$
\|e^{i2\pi K_h}-I-i2\pi K_h\|
\le(2\pi\|K_h\|)^2/2.
$$
Together with (5.3), this gives the safe bound
$$
\|e^{i2\pi K_h}-I-i\tau Q_h(g)\|
\le10^{18}\tau^2.
\tag{5.4}
$$
Combining (5.1) and (5.4) proves the line-operator version of (0.1).
The next section supplies the necessary finite-fiber step.

## 6. Exact norm descent: an explicit Zak decomposition

A bound on an $L^2(\mathbb R)$ operator does not by itself imply the
same bound on distributional combs. The missing implication must be
proved; here it is available by an elementary direct integral.

For $\alpha,\beta\in[0,1)$, define
$$
(Z\psi)(\alpha,\beta)_j
=\frac1{\sqrt N}\sum_{n\in\mathbb Z}
e^{-2\pi in\alpha}\psi((j+\beta)/N+n),
\qquad j=0,\ldots,N-1.
\tag{6.1}
$$
Parseval in $n$, followed by partitioning the real line, shows
$$
\int_0^1\int_0^1\sum_j|(Z\psi)(\alpha,\beta)_j|^2\,d\alpha\,d\beta
=\|\psi\|_2^2.
$$
Inverse Fourier series in $\alpha$ reconstruct the values of $\psi$,
so $Z$ is unitary onto the direct integral with fibers $\mathbb C^N$.

For an integer Fourier mode write $j+l=r+Nm$, $0\le r<N$.
Direct substitution in (1.1) gives the fiber action
$$
(W_h(k,l)_{\alpha,\beta}u)_j
=e^{2\pi ik(j+\beta+l/2)/N}e^{2\pi im\alpha}u_r.
\tag{6.2}
$$
It is a continuous unitary matrix in $(\alpha,\beta)$. At
$(0,0)$ it is the real-half matrix in (1.2), including its
$(-1)^{kl}$ factor. The physical corrected symbol (1.3) therefore gives
exactly the specified $A_N$ at that fiber.

The absolutely convergent Fourier symbols $v_h,K_h,g$, and their
bounded exponentials have continuous fiber matrices. The same is true
of $E_h$.

At the endpoint $u=\delta$, $N\delta=d^3$ is an integer.
Thus $e^{i\delta P/h}$ is the Fourier mode $W_h(0,N\delta)$, and
$e^{i\delta X/h}$ is $W_h(N\delta,0)$; both have continuous fibers
of the form (6.2). The negative-shift version is equally exact.
The entire endpoint word $W_3(\delta)$ is consequently decomposable
with continuous finite matrices.

The norm of a decomposable operator is the essential supremum of its
fiber norms. Thus the established line-operator bound holds almost
everywhere in the fiber variables. Continuity extends it to every fiber,
in particular $(0,0)$. This proves (0.1) for the exact finite matrices,
with unchanged constants.

There is no need for intermediate real $u$ to preserve the zero fiber.
Differentiation and Duhamel comparison were performed on the line with
fixed $h$; only their final, decomposable operators are descended.
This resolves the parameter/fiber issue without an illicit
finite-dimensional momentum or position operator.

## 7. Scalar phases and the odd lattice

For the mixed finite translations, direct multiplication gives
$$
R_NS_NR_N^{-1}S_N^{-1}
=e^{2\pi iN\delta^2}I=e^{2\pi id^2}I=I.
\tag{7.1}
$$
On the line at a general $u$, their commutator may have a scalar
$e^{iu^2/h}$, but this scalar cancels in the next group commutator.
Accordingly $W_3(u)=I$ at $\tau=0$ for every real $u$, not merely
at the rational endpoint. This is also reflected by the disappearance
of the central term after the first scaled Lie bracket.

For the same-direction choice the two initial linear translations
already commute for every $u$.

No metaplectic operator occurs in this word. The only odd-Weyl phase
needed is (1.2), which is explicitly retained in (6.2). Thus there is
no arbitrary quantization phase or metaplectic lift to choose. If the
oldspace invariance of $M_N$ is used afterward, it is a separate exact
finite identity and does not alter this commutator calculation.

## 8. Optional stronger symbol form

The actual-word proof also supplies the proposed fixed smooth phase.
Replace the multiplier in (2.1) by $4\pi^2\omega$ to define
$\mathcal L_0 b=\{a,b\}=a_qb_p-a_pb_q$, and set
$$
v_0(t)=\sum_{n\ge0}\frac{t^{n+1}}{(n+1)!}\mathcal L_0^n b,\qquad
G=
\begin{cases}
-2\pi\partial_q^3v_0(t),&\text{mixed},\\
+2\pi\partial_q^3v_0(t),&\text{same direction}.
\end{cases}
\tag{8.1}
$$
The same convergent series proves that $G$ is fixed, smooth, periodic,
real, and $G=\tau g+O_{C^r,a}(\tau^2)$.

For completeness, its replacement of the exact quantum symbol is
controlled. The multiplier difference is bounded by
$$
\left|\frac2h\sin(2\pi^2h\omega)-4\pi^2\omega\right|
\le \frac83\pi^6h^2|\omega|^3.
$$
Telescope the difference of the $n$th iterated brackets. Relative to
(2.2), choosing the exceptional bracket adds only a fixed polynomial
factor in $n$ times $h^2$. Extra fixed Fourier weights add another
polynomial factor. The geometric parameter $7000|t|$ is unchanged.
Therefore, for each fixed $r$,
$$
\|v_h-v_0\|_r\le C_{r,a}h^2t^2.
\tag{8.2}
$$

For smooth Fourier symbols the exact product formula gives
$$
\|Q_h(b)Q_h(c)-Q_h(bc)\|
\le2\pi^2h\|b\|_1\|c\|_1.
$$
Apply Duhamel to $e^{isQ_h(G)}$ and $Q_h(e^{isG})$.
The constant part of $e^{isG}$ has zero product error, so the remainder
is $O_a(h\tau^2)$. Equation (8.2) and (5.1) consequently yield
$$
W_3(\delta)=Q_h(e^{iG})
+O_a(\tau\delta+\tau^2h).
$$
The same continuous-fiber argument descends this identity. Since
$h=\delta^4/(2\pi)$, it proves (0.3).

The proof establishes this statement for the specified actual word.
A generic near-identity canonical map together with an amplitude merely
tending to one would not by itself specify an $O(\delta)$ error:
an amplitude $e^{i\sqrt\delta}$ illustrates the missing rate.
Here the exact generator and norm remainder fix that ambiguity.

## 9. Consequence for the canonical oldspace

Let $\mathsf P=\mathsf P_{d,N}$ project onto the simultaneous fixed
space of $T_N(N/d,0)$ and $T_N(0,N/d)$. The translations commute and
have order $d$, so
$$
\mathsf P=\frac1{d^2}\sum_{u,v=0}^{d-1}R_N^uS_N^v,\qquad
\operatorname{rank}\mathsf P=N/d^2=d^2.
$$
The same space is fixed by the negative $q$-translation used in (0.2).

Conjugating a Fourier mode by these two translations shows
$$
\mathsf P Q_N(e^{2\pi i(kq+lp)})\mathsf P=0
\quad\text{unless }d\mid k\text{ and }d\mid l.
$$
The symbol $g$ has support $|k|+|l|\le9$.
Thus for $d>18$, every nonzero Fourier frequency of the exact product
$Q_N(g)^*Q_N(g)$ is killed by compression. Its constant coefficient is
exactly the Parseval sum, since $W_h(\kappa)^*W_h(\kappa)=I$. Hence
$$
\boxed{\mathsf P Q_N(g)^*Q_N(g)\mathsf P
=\sigma^2\mathsf P,\qquad \sigma^2=\int_{\mathbb T^2}g^2.}
\tag{9.1}
$$

For the mixed symbol an explicit calculation gives
$$
\sigma^2=\frac{3897}{800}(2\pi)^8,\qquad \sigma>2500.
\tag{9.2}
$$
Indeed
$$
r(q+1/2)=1-\cos2\pi q+\cos14\pi q
-\tfrac12\cos16\pi q-\tfrac12\cos12\pi q,
$$
and orthogonality yields the coefficient
$1+343^2+256^2+108^2=194850$.
For the same-direction symbol its pure $\cos14\pi q$ component already
gives
$$
\sigma^2\ge\frac{81}{200}(14\pi)^8,\qquad \sigma>10^6.
\tag{9.3}
$$

If $v\in\operatorname{ran}\mathsf P$ is a unit vector and
$\epsilon=\|(I-\mathsf P)E_Nv\|$, then
$$
\|(C_{0,N}-I)v\|=\|(S_N-I)E_Nv\|\le2\epsilon.
$$
The word $C_{3,N}$ contains eight factors $C_{0,N}^{\pm1}$; its other
factors are $R_N^{\pm1}$, which fix $v$. Telescoping the word on this
single vector gives
$$
\|(C_{3,N}-I)v\|\le16\epsilon.
\tag{9.4}
$$
Equations (0.1) and (9.1) give the opposite bound
$$
\|(C_{3,N}-I)v\|\ge
\tau\sigma-10^{18}\tau^2-10^{21}\tau/d.
$$
For the exact fixed $\tau=10^{-80}$, and for example $d\ge10^{24}$,
the right side is at least $\tau\sigma/2$. Thus
$\epsilon\ge\tau\sigma/32$ for every such unit vector, proving (0.4).

This is a uniform angle estimate at the full time $\tau N$, despite
that time increasing without bound. It does not follow from generator
leakage alone; the quartic group word is the additional argument.

## 10. Audit boundary and provenance

The substantive steps were reconstructed from the exact Weyl matrix and
Hamiltonian definitions. The arithmetic agent independently proposed
the same-direction Lie-word route and supplied a compatible
finite-frequency majorant; the present proof records both conventions,
a complete remainder mechanism, the explicit finite-fiber transfer, and
the mixed-symbol escape constant.

The root's formal word calculation was not used as a norm estimate.
Formal degree-four cancellation alone would not control the remainder
at $h=\delta^4/(2\pi)$; Sections 2–6 supply that control.

The earlier report base remains
Spectral_partial_results_2026-10-20.md,
SHA-256
b8c5e2071d49394270006853ee8316f3900e84f1a7ae9b03e58e5c4eaf29a7cc.
No historical source was modified. This report supplies a new
original-family obstruction to canonical oldspace near-invariance.
It does not close the deterministic spectral-statistics problem.
