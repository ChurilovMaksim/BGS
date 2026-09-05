---
title: "Gaussian spectral blocks of a fixed cat map along Pell moduli"
author: "WoW research programme"
date: "5 September 2026"
---

# Status and distinction from BGS

This note gives a self-contained project derivation. Priority and independent
referee validation have not been established. It is a **global** spectral law
for compressed observables of one fixed hyperbolic toral automorphism, and a
perturbative global eigenphase-cluster consequence. It is not a microscopic
BGS, GOE, COE, level-repulsion, or fixed-strength perturbation theorem.

Unlike the separate magnetic-quotient semicircle theorem, this result uses a
fixed smooth Fourier observable, deterministic parameters, and generally
composite Pell moduli. No assertion that infinitely many Pell numbers are
prime is needed. The two limiting laws concern different regimes and are not
interchangeable.

# 1. Arithmetic moduli and a fixed classical map

Put
$$
 \alpha=1+\sqrt2,\qquad \lambda=\alpha^2=3+2\sqrt2,\qquad
 T=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$
The integral matrix T has determinant one and eigenvalues lambda and its
reciprocal, so it is one fixed hyperbolic toral automorphism. Also T is the
identity modulo 2, avoiding the usual centered-Weyl parity ambiguity.

Define integers Q_j,P_j by
$$
 \alpha^j=Q_j+P_j\sqrt2,
 \quad Q_0=1,\ P_0=0,\quad
 Q_{j+1}=Q_j+2P_j,\ P_{j+1}=Q_j+P_j.
$$
Let K tend to infinity through odd primes and set
$$
 N=Q_K=\frac{\alpha^K-\alpha^{-K}}2,\qquad F=P_K.
$$
Then
$$
 N^2-2F^2=-1,\qquad N\asymp\lambda^{K/2}.
$$
Every Q_j is odd, and gcd(F,N)=1. In Z/NZ define
$$
 s=F^{-1},\qquad s^2=2,\qquad h=3+2s,\qquad q_0=-F.
$$
The identity (1+s)^K=Q_K+P_Ks=1 gives h^K=1. Moreover h-1=2(1+s)
is a unit, since (1+s)(1-s)=-1. Reducing modulo any prime ell dividing N,
h has order exactly K: its order divides the prime K and is not one.
Consequently every such ell is 1 modulo K. In particular,
$$
 1-h^j\text{ is a unit for }1\leq j<K,
 \qquad 1+h^j\text{ is a unit for every }j. \tag{1}
$$
The latter assertion uses odd K. Thus H=<h> has order K and acts freely on
every nonzero residue, not just on the units. The signed orbits have size 2K,
and
$$
 n=\frac{N-1}{2K}
$$
is an integer. The moduli need not be prime: for example Q_11=8119=23*353.

# 2. Operators and identification with a fixed observable

On C^(Z/NZ), with counting-measure inner product, write
$$
 W(a,b)f(x)=e_N(a(x-b/2))f(x-b),\qquad
 S_u f(x)=f(u^{-1}x),\qquad Rf(x)=f(-x).
$$
Here e_N(t)=exp(2 pi i t/N), and divisions in exponents mean inverses modulo
N. All operators below preserve the odd subspace R=-1. For a character eta
of H, let E_eta be the eta eigenspace of S_h in that odd subspace, and let
P_eta denote its orthogonal projection. Its dimension is n.

Set
$$
 B_q=W(q,1)+W(q,1)^*,\qquad
 A_{q,\eta}=P_\eta B_qP_\eta|_{E_\eta},\qquad
 X_{q,\eta}=\sqrt{K/2}\,A_{q,\eta}. \tag{2}
$$
In the theorem q=q_0 is deterministic and is a unit modulo N.

This is a compression of a fixed Fourier observable of the fixed cat map,
not merely a modulus-dependent choice of an unrelated classical map.
Indeed, over Z/NZ put
$$
 M=\begin{pmatrix}-1/(2s)&1\\-1/2&-s\end{pmatrix},\qquad
 T=M\operatorname{diag}(h,h^{-1})M^{-1}. \tag{3}
$$
The matrix M has determinant one. Define the chirp C_t f(x)=e_N(tx^2/2)f(x)
and the unitary Fourier transform F_N with kernel e_N(xy)/sqrt(N). Direct
substitution gives their Weyl covariance matrices
$$
 C_t:\begin{pmatrix}1&t\\0&1\end{pmatrix},\quad
 S_u:\begin{pmatrix}u^{-1}&0\\0&u\end{pmatrix},\quad
 F_N:\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$
Therefore
$$
 V=C_{s^{-1}}S_{1/2}F_NC_{2s},\qquad U_N(T)=VS_h^{-1}V^* \tag{4}
$$
satisfies the exact finite Egorov identity
$$
 U_N(T)W(v)U_N(T)^*=W(Tv).
$$
These formulas also prove unitarity without invoking a prime-modulus-only
Weil construction. They preserve parity. A global phase convention for the
cat propagator does not affect any compression or relative eigenphase below.

Take the fixed observable
$$
 B=W(1,0)+W(-1,0),\qquad Bf(x)=2\cos(2\pi x/N)f(x). \tag{5}
$$
Under conjugation by V^*, its Weyl index is M^(-1)(1,0)=(-s,1/2).
Conjugating further by S_2, which commutes with S_h, gives index
(-s/2,1)=(-F,1). Thus the compressions of (5) to every odd cat eigenspace are
unitarily equivalent to A_(q_0,eta), with a harmless permutation of sector
labels.

# 3. Main theorem

**Theorem 1 (deterministic global Gaussian blocks).** Let K run through odd
primes, with N,Q_K,F,h,q_0 as above. For every fixed integer m>=1,
$$
 \sup_\eta\left|
 \frac1n\operatorname{Tr}X_{q_0,\eta}^{m}-\gamma_m
 \right|\longrightarrow0,
 \qquad
 \gamma_{2r}=(2r-1)!!,\quad\gamma_{2r+1}=0. \tag{6}
$$
Consequently the empirical spectral measures converge weakly to the standard
normal distribution, uniformly over all K odd-sector cat eigenspaces. There
is no random q in this theorem. For fixed even m the proof gives an
O_m(log K/K) error, apart from an exponentially small polynomial-in-K term.
For fixed odd m the main word contribution is eventually absent.

The name Gaussian here describes the limiting **eigenvalue density**. It does
not assert that the matrices form a Gaussian orthogonal ensemble.

# 4. Exact traces over the composite ring

The finite Weyl product remains
$$
 W(a,b)W(c,d)=e_N((ad-bc)/2)W(a+c,b+d).
$$
In an expansion of (B_q P_eta)^m, let eps_j=+1 or -1 and h_j in H. Starting
with (g,a,b,c)=(1,0,0,0), use
$$
 a'=a+\epsilon/g,\quad b'=b+\epsilon g,\quad
 c'=c+\epsilon(ag-b/g)/2,\quad g'=gh. \tag{7}
$$
The word is e_N(qc)W(qa,b)S_g, with the additional sector weight bar(eta(g)).
For g != 1, (1) gives a unique affine fixed point, so the trace has modulus
one and phase qab(1+g)/(2(1-g)). For g=1, since q is a unit, the trace is
N if a=b=0 and zero otherwise. The parity insertion replaces g by -g and
always has a unique fixed point by (1).

For g=1 write t_1=1 and t_j=h_1...h_(j-1). The remaining labels are arbitrary
in H, and the final h_m is determined. The main term is independent of eta:
$$
 \mu_{m,\eta}(q)=\frac{N}{N-1}
 \frac1{2^{m/2}K^{m/2-1}}
 \sum_{\substack{t_1=1,\ t_2,\ldots,t_m\in H;\ \epsilon\\
                  \sum\epsilon_jt_j=\sum\epsilon_j/t_j=0}}
 e_N(q\Omega)+\mathcal R_{m,\eta}(q), \tag{8}
$$
$$
 \Omega=\frac12\sum_{i<j}\epsilon_i\epsilon_j
                 (t_j/t_i-t_i/t_j),\qquad
 |\mathcal R_{m,\eta}(q)|\leq
 \frac{2^{m/2+1}K^{m/2+1}}{N-1}. \tag{9}
$$
This is an exact identity plus an elementary absolute bound. No field-only
root-counting theorem or random-entry hypothesis is used.

# 5. Lifting reciprocal relations into a quadratic field

A tuple in (8) gives a signed polynomial P(Z)=sum eps_j Z^(e_j), where
 t_j=h^(e_j). Cancel opposite signs at equal labels first. If P is not the
zero polynomial, its support has at most m points on the cyclic group Z/KZ.
Cut at a largest gap and rotate all labels. The resulting polynomial has
coefficient l1 norm at most m and degree
$$
 L\leq K-\lceil K/m\rceil. \tag{10}
$$
Both reciprocal congruences survive this rotation.

Divide P by the monic polynomial Z^2-6Z+1, obtaining remainder aZ+b with
integers a,b. Since P(h)=P(h^(-1))=0 and h-h^(-1)=4s is a unit modulo N,
we have N|a and N|b. Hence, for lambda=3+2sqrt(2),
$$
 N^2\mid \operatorname{Norm}_{\mathbb Q(\sqrt2)/\mathbb Q}P(\lambda).
$$
If this norm is nonzero, its absolute value is at most
$$
 |P(\lambda)P(\lambda^{-1})|\leq m^2\lambda^L. \tag{11}
$$
But N^2 is asymptotic to lambda^K/4, so (10)--(11) are incompatible for all
sufficiently large K at each fixed m. Thus the rotated P satisfies
$$
 P(\lambda)=0. \tag{12}
$$
An elementary sufficient numerical cutoff is lambda^(K/m)>16m^2. A sharper
entirely rational check uses L in (10) and
$$
 m^2(2Q_{2L}+3P_{2L})<2N^2, \tag{13}
$$
since sqrt(2)<3/2. The implementation uses (13), not an uncertified decimal
comparison.

Crucially, (12) does **not** imply coefficientwise balance. The structural
relation h+h^(-1)-6=0 is a non-balanced reciprocal relation of length eight
for every modulus in this family. An exclusion-of-all-relations programme
would therefore be false even here.

# 6. A bounded-cluster lemma and counting, instead of exclusion

**Lemma 2.** Let P be an integral polynomial of coefficient l1 norm <=m with
P(lambda)=0. Split its support at a gap d>2 log_lambda(m). Then the two pieces
vanish separately at lambda.

**Proof.** Write P=P_low+Z^(a+d)P_high, with deg(P_low)<=a. If
P_high(lambda) is nonzero, its algebraic-integer norm is a nonzero integer.
As |P_high(lambda^(-1))|<=m, we have |P_high(lambda)|>=1/m. Cancellation with
the low part would imply lambda^(a+d)/m<=m lambda^a, a contradiction.
Therefore P_high(lambda)=0, and then P_low(lambda)=0. This also covers an
empty low part trivially. Square.

Choose
$$
 B_m=\lceil2\log_\lambda m\rceil+1,\qquad D_m=(m-1)B_m.
$$
Repeatedly applying the lemma partitions a nonzero relation into components
of span at most D_m. Every nonzero component contains at least three signed
occurrences; a two-term relation between positive distinct powers of lambda
is impossible. Reinsert the cancelled opposite-sign pairs as two-occurrence
components of span zero.

If an m-tuple is not coefficientwise balanced, it therefore has at most
floor((m-1)/2) components. For each partition of the m positions, each sign
pattern, and each bounded offset pattern, a component has one translation
parameter in Z/KZ. The component containing t_1=1 has that parameter fixed.
It follows that the number of unbalanced tuples in (8) is at most
$$
 C_m K^{\lfloor(m-1)/2\rfloor-1}, \tag{14}
$$
for a constant depending only on m. For example the coarse constant
C_m=(2m(2D_m+1))^m suffices by overcounting partitions, signs and offsets.
Cyclic rotation introduces no further factor K: the count is directly over
cyclic component translations, with the component containing position 1
pinned.

For even m=2r, (14), divided by the normalization in (8), is O_m(1/K),
uniformly in q and eta. Odd m has an additional simplification. A polynomial
vanishing at lambda is divisible in Z[Z] by Z^2-6Z+1, so P(1) is divisible
by -4. Yet the parity of P(1) equals the parity of the number of signed
occurrences. Consequently odd-m reciprocal tuples do not exist once the
lifting argument applies.

# 7. All pairings survive for the fixed observable

For a balanced 2r-tuple, match equal labels with opposite signs. Distinct
pair labels give a unique matching; repeated labels contribute an
O_r(1/K) normalized overcount. For a matching pi, orient each pair by
sigma_i in {+1,-1}, and let its label be x_i=h^(e_i), with x_1=1. The exact
phase is
$$
 F_{\pi,\sigma}(x)=
 \sum_{\substack{i<j\\\text{pairs }i,j\text{ cross}}}
 \sigma_i\sigma_j(x_j/x_i-x_i/x_j). \tag{15}
$$
Unlike a q-average, the deterministic value q_0 does not suppress crossings.
Let delta be the representative of d modulo K in
[-(K-1)/2,(K-1)/2]. The Pell recurrence gives
$$
 q_0(h^d-h^{-d})\equiv-2P_{2\delta}\pmod N. \tag{16}
$$
For |delta|<=(K-1)/2-L,
$$
 |P_{2\delta}|/N\leq C\lambda^{-L}, \tag{17}
$$
with an absolute constant. A difference of two independent uniform pair
labels is uniform on Z/KZ, including when one label is fixed. Thus, for any
fixed pairing, a union bound shows that only O_r(L/K) assignments have a
crossing difference in the excluded central window. On the other assignments
(15)--(17) make the phase 1+O_r(lambda^(-L)). Taking
L=ceil(log_lambda K) proves
$$
 K^{-(r-1)}\sum_{x_2,\ldots,x_r\in H}
 e_N(q_0 F_{\pi,\sigma}(x))
 =1+O_r(\log K/K). \tag{18}
$$
There are (2r-1)!! matchings, not just the Catalan number of noncrossing
matchings. Equations (8)--(9), (14), and (18) prove (6) and its stated even
moment error. Odd moments follow from the parity argument and (9).

Bounded second moments give tightness, and higher even moments give uniform
integrability. The Gaussian moment sequence is determinate: its even moments
imply a finite exponential-square moment for every exponent below 1/2, by
monotone expansion, and hence determine the characteristic function
exp(-t^2/2). The usual subsequence argument therefore gives weak convergence.
Because all bounds are uniform in eta, selecting a worst sector on any
hypothetically nonconvergent subsequence proves the claimed uniformity.

# 8. An explicit fourth-moment certificate

For m=4, a nonzero polynomial with l1 norm <=4 cannot vanish at lambda>3:
its leading term dominates all lower terms. Thus after (13) holds, all
four-letter reciprocal tuples are balanced. Exact pairing overcount is six,
which gives, uniformly in eta,
$$
 \left|\mu_{4,\eta}-\frac{N}{N-1}
 \left(2+S_K-\frac{3}{2K}\right)\right|
 \leq\frac{8K^3}{N-1}, \tag{19}
$$
$$
 S_K=\frac1K\left(1+2\sum_{d=1}^{(K-1)/2}
                    \cos(4\pi P_{2d}/N)\right). \tag{20}
$$
These are finite-size bounds, not fitted matrix histograms. The companion
certificate computes rational enclosures for the cosines, proves (13) by
integer arithmetic, and includes the entire remainder in (19).

There is also a nontrivial explicit asymptotic correction:
$$
 K(3-\mu_{4,\eta})\longrightarrow
 \frac32+2\sum_{j=0}^\infty
 \left[1-\cos\left((4-2\sqrt2)\pi\lambda^{-j}\right)\right]. \tag{21}
$$
To see this, reindex (20) by d=(K-1)/2-j. Then
P_(K-1-2j)/N tends to alpha^(-1-2j)/sqrt(2). The inequality
1-cos x<=x^2/2 gives a uniform summable geometric majorant. The remainder in
(19), even after multiplication by K, is exponentially small. This proves
(21), uniformly in the sector.

# 9. A finite-perturbation consequence for actual eigenphases

The following elementary comparison explains precisely how far the global
observable theorem transfers to a propagator.

**Lemma 3.** Let U_0 be unitary, let P be its spectral projection at 1, and
let delta>0 be the distance from 1 to the other eigenvalues. Let B=B*,
||B||<=b, and U_e=exp(i e B)U_0. If 0<b|e|<=delta/16, the cluster near 1
has rank rank(P). Write its principal eigenphases as theta_j, and the
eigenvalues of A=PBP on ran(P) as a_j. Their empirical measures satisfy
$$
 W_2\left(\frac1n\sum_j\delta_{\theta_j/e},
          \frac1n\sum_j\delta_{a_j}\right)
 \leq\frac{13\pi b^2|e|}{\delta}. \tag{22}
$$
Here W_2 is quadratic Wasserstein distance between equal-weight real spectra.

**Proof.** Put Delta=U_e-U_0 and d=||Delta||<=b|e|. Resolvent integration on
the circle |z-1|=delta/2 gives ||P_e-P||=eta<=4d/delta<=1/4. The new
projection is orthogonal. Set H=(PP_eP)^(1/2) and J=P_eP H^(-1). Then J is
an isometry onto the perturbed cluster, PJ=H,
||(I-P)J||<=eta, and ||J-P||<=2eta. Let V=J*U_eJ. Spectral inclusion for the
normal matrix U_0 implies ||V-I||<=d: every cluster eigenvalue is within d
of 1, since all other old eigenvalues are farther than delta/2.

Writing Z=(I-P)J and using invariance of the new cluster gives
(U_0-I)Z=Z(V-I)-(I-P)Delta J. Hence
||Z*(U_0-I)Z||<=eta(1+eta)d. Also
||J*Delta J-PDelta P||<=4eta d. Therefore
||V-I-PDelta P||<=24d^2/delta. Taylor's integral remainder for the two
unitary exponentials, and delta<=2, yield
$$
 \|V-e^{i e A}\|\leq26 e^2b^2/\delta. \tag{23}
$$
For two unitary matrices, the squared Frobenius difference is a doubly
stochastic average of squared eigenvalue distances, using the squared
absolute overlaps of their eigenbases. Decomposing that doubly stochastic
matrix into permutation matrices gives a matching whose mean squared chord
distance is at most the squared operator norm in (23). Such a decomposition
follows by repeatedly selecting a positive perfect matching (Hall's
condition follows from the row and column sums), subtracting its smallest
entry, and iterating. All phases here are in a common short arc; for angle
differences <=pi, arc distance is at most pi/2 times chord distance. Dividing
by |e| proves (22). Square.

For the cat propagator, rotate any of its K clusters to 1. Its gap is
$$
 \delta_K=2\sin(\pi/K)\geq4/K,\qquad b=2.
$$
Thus the empirical law of the rescaled relative eigenphases
sqrt(K/2)*theta_j/e differs in W_2 from the corresponding observable block by
at most
$$
 \frac{13\pi}{\sqrt2}|e|K^{3/2}. \tag{24}
$$
**Corollary 4.** For any nonzero perturbation sequence e=e_K satisfying
|e_K|K^(3/2)->0, every odd-sector eigenphase cluster of
exp(i e_K B)U_N(T), rescaled as above, converges globally to the standard
normal distribution, uniformly over the K clusters. The symmetrically kicked
propagator exp(i e_K B/2)U_N(T)exp(i e_K B/2) is isospectral and has the same
conclusion.

This does not exchange the small-perturbation and semiclassical limits
without control: (24) is the control, and its hypothesis is part of the
claim. Fixed nonzero perturbations, microscopic within-cluster correlations,
and full BGS universality are not established.

# 10. What changed in the research route

Absolute cyclotomic exclusion is too restrictive for a fixed map. Here the
quadratic characteristic field retains the structurally forced relations,
and a bounded-cluster argument shows that they have lower-order multiplicity.
For a fixed smooth observable, crossing phases then tend to one rather than
averaging to zero. This explains the Gaussian/semicircle distinction instead
of treating either density as automatic evidence for BGS.

The next microscopic problem requires estimates at orders growing toward the
block Heisenberg scale n, together with unfolding and appropriate joint
correlations. Fixed-moment convergence and a perturbative global transfer do
not supply those estimates. No priority or prize-level claim is made.
