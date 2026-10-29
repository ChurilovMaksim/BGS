# Unitary short-time form factor for a momentum-phase cat map

**Claim IDs:** `BGS-TRACE-140`, `BGS-TRACE-141`, `BGS-TRACE-142`.
**Status:** project proof of `BGS-TRACE-140` and `BGS-TRACE-141`. `BGS-TRACE-142` is verification-pending: the rotation and reflection main terms are evaluated, and the non-injective Gaussian remainder is not bounded. Python and C++ recompute the exact Haar bucket sums on the odd primes \(5,7,11\) at times two and three. A Lean module decides the odd-symbol energy, the constants \(468\) and \(20\), and the residues \(27\bmod 5,7,11,13\). It does not sum the form factor. No external referee.

The comparison values \(2m\) and \(m\) are the short-time orthogonal and unitary counts of `BGS-TRACE-128`. The present note does not quote that error term: the expansion is rederived for a momentum-diagonal factor. `BGS-TRACE-005` and `BGS-BGS-001` remain **open**. This is not a theorem about the fixed kick at \(\tau=10^{-80}\).

## 1. Statements

Let \(p\) be an odd prime and let
\[
S=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}\in\mathrm{SL}(2,\mathbb Z)
\]
with \(t=\alpha+\delta\) and \(|t|\ge 3\). Assume \(p\) does not divide \(\beta\delta\). Set \(\kappa\equiv-(2\beta)^{-1}\pmod p\) and
\[
(M)_{xy}=p^{-1/2}\,e_p\bigl(\kappa(\delta x^2-2xy+\alpha y^2)\bigr),
\]
where \(e_p(r)=\exp(2\pi i r/p)\). The hypothesis \(p\nmid\delta\) is the Gauss-sum condition: if \(p\) divides \(\delta\), the quadratic coefficient in the column vanishes, the momentum index is slaved to the target, and the momentum phases collapse to position phases. Let \(\lambda\equiv\delta^{-1}\pmod p\). Theorems 1 and 2 assume only
\[
\lambda\not\equiv -1\pmod p,
\]
that is \(\delta\not\equiv -1\pmod p\). The stronger condition \(\lambda^t\not\equiv 1\) for \(1\le t\le m\) implies this when \(m\ge 2\), but it is not needed for those two theorems: the matrix identity of Section 5 uses only \(\lambda\not\equiv -1\). In particular \(\lambda\equiv 1\), as for Arnold's map \(\begin{pmatrix}2&1\\1&1\end{pmatrix}\), is allowed. Write \(P(p,m)=p(p-1)\cdots(p-m+1)\).

Let \(D\) and \(E\) be independent Haar diagonal unitaries, and let \(F\) be the unitary Fourier matrix \(F_{jp}=p^{-1/2}e_p(-jp)\). Set \(R=F^{\dagger}EF\) and \(U=DRM\). Write \(\mathbb E\) for the product Haar measure.

**Theorem 1 (Haar momentum phases, unitary value).** For \(m=1\), \(\mathbb E\lvert\operatorname{Tr} U\rvert^2=1\). For \(m=2\) assume \(\lambda\not\equiv -1\pmod p\), that is \(\delta\not\equiv-1\). Then the reversal is the nontrivial rotation, and
\[
\bigl\lvert\mathbb E\lvert\operatorname{Tr} U^2\rvert^2-2\bigr\rvert\le\frac{20}{p}.
\]
For every integer \(m\ge 3\),
\[
\Bigl\lvert\mathbb E\lvert\operatorname{Tr} U^m\rvert^2-m\,\frac{P(p,m)}{p^m}\Bigr\rvert
\le\frac{(m!)^2\bigl(1+2m(m-1)\bigr)}{p}.
\]
In particular, for each fixed \(m\ge 1\),
\[
\lim_{\substack{p\to\infty\\ p\text{ admissible}}}\mathbb E\lvert\operatorname{Tr} U^m\rvert^2=m
\]
for \(m\ge 3\), and the limits at times one and two are \(1\) and \(2\). If \(m(p)\ge 3\), if \((m!)^2 m^2=o(p)\), and if \(m^2=o(p)\), the ratio of the expectation to \(m\) tends to \(1\). Every sequence \(m\le c\log p/\log\log p\) with a fixed \(c<1/2\) lies in this range for all large admissible \(p\). The estimate does not reach \(m\le p^{\alpha}\).

Position conjugation reverses the momentum factor \(R\) if and only if \(\xi_j=\xi_{-j}\) for every frequency \(j\). That locus has Haar measure zero. The reflection contribution, which the antiunitary \(\Theta'=DE_qK_0\) of `BGS-TRACE-131` (equal to \(DK_0\) when \(\alpha\equiv\delta\pmod p\)) doubles for a position-diagonal kick, is \(o(1)\) for Haar momentum phases.

**Theorem 2 (joint moments).** Fix an integer \(k\ge 1\). For \(m\ge 3\), under the same hypothesis \(\lambda\not\equiv -1\),
\[
\Bigl\lvert\mathbb E\lvert\operatorname{Tr} U^m\rvert^{2k}-k!\,m^k\,\frac{P(p,km)}{p^{km}}\Bigr\rvert
\le\frac{\bigl((km)!\bigr)^2\bigl(1+2km(km-1)\bigr)}{p}.
\]
For each fixed \(k\) and \(m\ge 3\), the expectation tends to \(k!\,m^k\). If \(k\) is fixed and \(m\le c\log p/\log\log p\) with \(c<1/(2k)\), the ratio to \(k!\,m^k\) tends to \(1\).

**Theorem 3 (Gaussian crossover, verification-pending).** Let \(v\ge 0\) and let \(g_j\), \(j\in\mathbb F_p\), be independent standard real Gaussians, independent of \(D\). Set \(\xi_j=\exp(i\sqrt{v}\,g_j)\), let \(E=\mathrm{diag}(\xi)\), and keep \(U=DRM\). The rotation, reflection and non-dihedral main terms are evaluated in Sections 3–5, where the inverse of \(A=I-\lambda C\) is used and therefore \(\lambda^t\not\equiv 1\) for \(1\le t\le m\). Theorems 1 and 2 do not use that inverse: their hypothesis is only \(\lambda\not\equiv -1\). The contribution of non-injective position words is not bounded here: the occupation count of Section 6 uses the Haar momentum constraint and does not apply to Gaussian weights. The limit \(m(1+e^{-vm})\) is therefore stated as verification-pending. Exact finite-\(p\) values approach it with a gap of about \(4/p\) at \(m=3\), \(v=0.4\). With \(\tau=m/p\) and \(\Lambda=vp\), the proposed limit is
\[
m\bigl(1+e^{-vm}\bigr)=p\cdot\tau\bigl(1+e^{-\Lambda\tau}\bigr).
\]
This is the diagonal approximation of the Pandey–Mehta form factor. Saito and Nagao, arXiv:nlin/0505055, equation (7), identify their parameter \(\mu\) with \(bT\). The primary source of that crossover form factor is Bohigas, Giannoni, Ozorio de Almeida and Schmit, Nonlinearity 8 (1995), 203–221.

**Corollary (odd energy of the maintained symbol).** The modes with displacement \(\ell=\pm 1\) have total energy \(9/80000\). The part odd under \(p\mapsto -p\) has energy
\[
\frac{16}{25}\cdot\frac{9}{80000}=\frac{9}{125000}=7.2\times 10^{-5}.
\]
If that energy is used as the Gaussian variance per step, \(v=\sigma_{\mathrm{odd}}\eta^2\), the crossover parameter of Theorem 3 is
\[
\Lambda=\sigma_{\mathrm{odd}}\eta^2\,p=\frac{9}{125000}\,\eta^2\,p.
\]
The value \(7.2\times10^{-5}\) is close to the numerical scale \(\approx7.3\times10^{-5}\eta^2N\). The choice \(v=\sigma_{\mathrm{odd}}\eta^2\) is a convention: matching the phase variance of time-reversed partners, \(2\eta\sum V_{\mathrm{odd}}\), would give \(v=2\sigma_{\mathrm{odd}}\eta^2\). Neither identification is derived. The corollary computes the symbol energy. It does not identify the sixteen-phase propagator with the Gaussian ensemble.

**Boundary.** The ensemble is not the fixed kick, not the sixteen-phase ensemble of `BGS-TRACE-126`, and not Haar measure on \(U(p)\). The value \(m\) is the short-time unitary count, not the sine-kernel pair correlation. Times of order \(p\) are not reached. The factor \(e^{-vm}\) is the diagonal approximation: the Sieber–Richter corrections of order \(\tau^2\) are not proved. At time two a reversal is a rotation, so the formula \(m(1+e^{-vm})\) is not stated for \(m<3\). If \(\delta\equiv -1\pmod p\) the reflections survive the Haar momentum average and the limits are \(4\) at time two and \(2m\) for \(m\ge3\). For example \(S=\begin{pmatrix}-3&1\\2&-1\end{pmatrix}\) has \(\mathbb E\lvert\operatorname{Tr}U^2\rvert^2=3.698\) at \(p=13\) and \(3.828\) at \(p=23\), tending to \(4\). The values \(m\) and \(m(1+e^{-vm})\) are classical diagonal counts; only the finite-\(p\) error bounds of Theorems 1 and 2 are new. `BGS-TRACE-005` and `BGS-BGS-001` remain open.

## 2. The reduced phase

Let \(a=\kappa\delta\) and \(\gamma=(4a)^{-1}\). Both are units. The Fourier inversion \(R_{xz}=p^{-1}\sum_j\xi_j e_p(j(x-z))\) and the quadratic Gauss sum
\[
G(a)=\sum_{z\in\mathbb F_p}e_p(az^2),\qquad\lvert G(a)\rvert=\sqrt p,
\]
give, after completing the square,
\[
(RM)_{xy}=\mu\,e_p(\nu y^2)\,p^{-1}\sum_j\xi_j\,e_p\bigl(-\gamma j^2+j(x-\lambda y)\bigr),
\]
with \(\lvert\mu\rvert=1\) and \(\nu\in\mathbb F_p\). The identity \(\lvert G(a)\rvert^2=p\) is the change of variables \((x,y)\mapsto(x-y,x+y)\), bijective because \(p\) is odd, followed by the geometric sum. The coefficient of \(y\) is \(\lambda\) because \(4\gamma\kappa=\delta^{-1}\).

A column phase \(e_p(\nu y^2)\) and the quadratic \(-\gamma j^2\) depend on a word only through \(\sum y_t^2\) and \(\sum j_t^2\). Inside a fixed occupation they are constant. For the Haar case they cancel in \(A(x)\overline{A(y)}\) whenever the occupations of the two words agree. For the Gaussian case they cancel on the stationary families of Section 4, where the square sums are proved equal. The global factor \(\mu\) has modulus one. Therefore, writing \(\Phi(x,s)=\sum_{t=0}^{m-1}s_t(x_t-\lambda x_{t+1})\),

\[
\mathbb E_D\lvert\operatorname{Tr}(DRM)^m\rvert^2
=p^{-2m}\sum_{x,y,\,s,r}
W(s,r)\,e_p\bigl(\Phi(x,s)-\Phi(y,r)\bigr),
\]
the sum being restricted to pairs of position words with the same occupation, and \(W\) the momentum weight. For Haar momentum phases, \(W=1\) when \(s\) and \(r\) have the same occupation and \(W=0\) otherwise. For the Gaussian weight,
\[
W(s,r)=\exp\Bigl(-\frac v2\sum_{j\in\mathbb F_p}c_j(s,r)^2\Bigr),
\]
where \(c_j\) is the multiplicity of \(j\) in \(s\) minus its multiplicity in \(r\). Indeed \(\mathbb E\exp(i\sqrt{v}\,c g)=\exp(-vc^2/2)\).

## 3. Rotations and the cycle automorphism group

Let \(\rho\in S_m\) act by \((x\circ\rho)_t=x_{\rho(t)}\). If \(x\) is injective and \(y\) has the same image, there is a unique such \(\rho\). The same holds for momenta. Summing over all words and dividing by the stabilizer is estimated at the end of this section; the injective sum is the one that enters the error.

The coefficient of \(x_j\) in \(\Phi(x,s)-\Phi(x\circ\rho,r)\) is
\[
s_j-\lambda s_{j-1}-r_{\alpha(j)}+\lambda r_{\alpha(j)-1},
\]
where \(\alpha=\rho^{-1}\) and indices are read in \(\mathbb Z/m\mathbb Z\). In operator form this is \(As=P_{\alpha}Ar\), with
\[
(As)_j=s_j-\lambda s_{j-1}
\]
and \((P_{\alpha}v)_j=v_{\alpha(j)}\). The matrix of \(A\) is \(I-\lambda C\), where \(C\) is the cycle shift \((Cs)_j=s_{j-1}\). Since \(\lambda^m\neq 1\) and \(C^m=I\),
\[
A^{-1}=\frac1{1-\lambda^m}\sum_{k=0}^{m-1}\lambda^k C^k.
\]
Every coefficient \(\lambda^k/(1-\lambda^m)\) is nonzero, so every entry of \(A^{-1}\) is nonzero. The solution is \(s=A^{-1}P_{\alpha}Ar\), one momentum word for each parameter word, for every \(\rho\).

The quadratic form \(Q(s)=\sum_j s_j^2\) satisfies \(Q(s)=Q(r)\) for every \(r\) if and only if \(L=A^{-1}P_{\alpha}A\) is orthogonal. Equivalently \(P_{\alpha}\) commutes with \(AA^{T}\) by conjugation. A direct expansion gives
\[
AA^{T}=(1+\lambda^2)I-\lambda(C+C^{-1}).
\]
The coefficient of \(C+C^{-1}\) is \(-\lambda\neq 0\). Conjugation by \(P_{\alpha}\) replaces the cycle by the permuted cycle. For \(m\ge 3\) the automorphism group of the cycle graph is the dihedral group of order \(2m\): the maps \(j\mapsto j+b\) and \(j\mapsto -j+b\). Thus \(Q(s)-Q(r)\) vanishes for every \(r\) if and only if \(\alpha\) is dihedral.

On a rotation, \(L\) itself is that rotation, occupations agree, and the Gaussian weight equals \(1\). There are \(m\) rotations. On a reflection the same square identity holds, by the auxiliary relation \(RAR=A^{T}\) for the standard reversal \(R\) and by normality of the circulant \(A\): every circulant commutes with its transpose, so
\[
A^{-1}RA=R(A^{T})^{-1}A
\]
is orthogonal. The \(m\) reflections are disjoint from the \(m\) rotations when \(m\ge 3\). A \(2\)-cycle is equal to its reversal, which is why \(m=2\) is excluded from the factor \(1+e^{-vm}\).

For the Haar weight only occupation-matched momenta survive. A reflection does not preserve occupation for a positive-density set of momenta: \(L\) is not a permutation matrix. A permutation matrix would be orthogonal, hence \(\alpha\) would be dihedral, and the reflection case is not a coordinate permutation when \(\lambda\not\equiv\pm 1\). The Haar main term is therefore only the \(m\) rotations.

## 4. Square sums and charges on the dihedral families

On rotations, \(s\) is a coordinate permutation of \(r\), so \(Q(s)=Q(r)\) and every charge \(c_j\) vanishes. The Gaussian weight is \(1\). Summing over all position words and all momentum parameters gives \(p^{2m}\) pairs, and the quotient by \(p^{2m}\) is \(1\). The \(m\) rotations contribute \(m\), up to the symmetry overcount of Section 6.

On a reflection, \(Q(s)=Q(r)\) as well, so the quadratic phase is identically \(1\). The parameter \(r\) runs through \(\mathbb F_p^m\). The coordinate functions of \(s=Lr\) are the rows of \(L\). Invertibility of \(L\) forces the rows to be pairwise distinct, so \(s_i-s_j\) is a nonzero linear form. No row is a standard basis vector. Indeed, under the hypothesis \(\lambda^t\not\equiv 1\) for \(1\le t\le m-1\), the entry
\[
(Le_j)_a=\frac{\lambda^{a-\alpha(j)}}{1-\lambda^m}\bigl(1-\lambda^{1-(\alpha(j+1)-\alpha(j))}\bigr)
\]
vanishes if and only if \(\alpha(j+1)=\alpha(j)+1\). If a row vanished at all but one column, the step \(\alpha(j+1)-\alpha(j)\) would equal \(1\) at all but one index. Summing the steps around the cycle forces the remaining step to be \(1\) as well, so \(\alpha\) would be a rotation. Reflections and non-dihedral permutations are not rotations, so every row has at least two nonzero entries. Consequently \(s_i-r_j\) is a nonzero linear form for every \(i,j\).

A nonzero linear form on \(\mathbb F_p^m\) vanishes on exactly \(p^{m-1}\) points. There are \(\binom{2m}{2}\) pairs among the \(2m\) coordinate forms. Off that union, all \(2m\) values are distinct, every charge is \(\pm 1\), and
\[
\sum_j c_j^2=2m,\qquad W=\exp(-vm).
\]
The proportion of the union is at most \(\binom{2m}{2}/p\). Therefore the average of \(W\) over the reflection family differs from \(e^{-vm}\) by at most \(m(2m-1)/p\). The \(m\) reflections contribute \(m e^{-vm}\) in the limit, with the same explicit gap.

## 5. Non-dihedral permutations

Let \(\alpha\) lie outside the dihedral group. Section 3 shows that \(Q(s)-Q(r)\) is not the zero function. Over a field of odd characteristic a nonzero quadratic form has rank \(r\ge 1\) and may be diagonalized: there are coordinates in which \(Q=\sum_{i=1}^{r}a_i y_i^2\) with each \(a_i\neq 0\). Diagonalization is the usual completion: if some diagonal entry of the polar bilinear form is nonzero, complete the square; if every diagonal entry vanishes and an off-diagonal entry \(b_{ij}\) is nonzero, the substitution \(y_i=u+w\), \(y_j=u-w\) produces a nonzero square because \(2\neq 0\). The exponential sum then factors, and
\[
\Bigl\lvert\sum_{y\in\mathbb F_p}e_p(a y^2)\Bigr\rvert=\sqrt p
\]
for \(a\neq 0\). Hence
\[
\Bigl\lvert\sum_{q\in\mathbb F_p^m}e_p\bigl(Q(Lq)-Q(q)\bigr)\Bigr\rvert=p^{m-r/2}\le p^{m-1/2}.
\]

The Gaussian weight equals \(e^{-vm}\) off the collision union of Section 4, and the same row argument shows that no coordinate is forced into collision: otherwise a row of \(L\) would be a basis vector, which Section 4 excludes for non-rotations, or two rows would coincide, which invertibility excludes. The symmetric difference between the weighted sum and \(e^{-vm}\) times the pure quadratic sum is supported on at most \(\binom{2m}{2}p^{m-1}\) points. Dividing by \(p^m\), the contribution of one non-dihedral \(\alpha\) is at most
\[
p^{-1/2}+\frac{m(2m-1)}{p}.
\]
At most \(m!\) permutations \(\alpha\) exist. Only \(\lambda\not\equiv-1\) is used for Theorems 1 and 2. The condition \(\lambda^t\not\equiv 1\) for \(1\le t\le m\) is used in Sections 3–5, for the Gaussian main terms of Theorem 3, because those sections invert \(A\).

## 6. The Haar count

Write \(w(x)=1/\lvert\operatorname{Stab} x\rvert\), where the stabilizer is the set of permutations that fix the word \(x\). The exact identity is
\[
\mathbb E\lvert\operatorname{Tr} U^m\rvert^2
=p^{-2m}\sum_{\rho,\sigma\in S_m}\sum_{x,r\in\mathbb F_p^m}
w(x)\,w(r)\,e_p\bigl(\langle x,\,B_{\rho,\sigma} r\rangle\bigr),
\]
with \(B_{\rho,\sigma}=AP_\sigma-P_{\rho^{-1}}A\). Replacing \(w\) by \(1\) makes the sum over \(x\) equal to \(p^m\) times the indicator that \(Br=0\). That part of the sum equals \(\sum p^{\dim\ker B-m}\).

The matrix identity
\[
B_{\rho,\sigma}=0\iff P_\sigma-P_{\rho^{-1}}=\lambda\bigl(CP_\sigma-P_{\rho^{-1}}C\bigr)
\]
has entries in \(\{0,\pm 1\}\) on the left and in \(\lambda\{0,\pm 1\}\) on the right. If \(\lambda\not\equiv\pm 1\), both sides vanish, so \(\sigma=\rho^{-1}\) is a rotation. Checking \(\lambda\equiv 1\) directly among sums of permutation matrices leaves only the rotations. Checking \(\lambda\equiv -1\) leaves the rotations and the \(m\) reflections. Thus, when \(\lambda\not\equiv -1\), one has \(B=0\) only for the \(m\) rotations. Every other pair has \(\dim\ker B\le m-1\), and this part of the sum lies in
\[
\bigl[m,\,m+\bigl((m!)^2-m\bigr)/p\bigr].
\]
The weight correction is at most \((m!)^2\bigl(1-(P/p^m)^2\bigr)\le (m!)^2 m(m-1)/p\). Together,
\[
\bigl\lvert\mathbb E\lvert\operatorname{Tr} U^m\rvert^2-m\bigr\rvert
\le\frac{(m!)^2\bigl(1+m(m-1)\bigr)-m}{p}.
\]
Since \(m-mP/p^m\le m^2(m-1)/(2p)\), this implies the bound of Theorem 1 for every \(m\ge 2\). At time two the same estimate gives \(10/p\), which is at most \(20/p\). At time one the only word is a site and the expectation equals \(1\).

For Theorem 2 the same argument applies to \(k\) blocks, with \(A\) block diagonal. The centraliser of \(k\) disjoint \(m\)-cycles is the wreath product \(\mathbb Z_m\wr S_k\), of order \(k!\,m^k\). The constant \(\bigl((km)!\bigr)^2\bigl(1+2km(km-1)\bigr)/p\) follows in the same way. Stirling’s bound \(m!\le m^m\) gives the windows \(c<1/2\) and \(c<1/(2k)\).

For the Gaussian weight the momentum sum is not restricted to occupation-matched pairs, so the count of this section does not bound non-injective position words. That is the gap recorded in Theorem 3. The rotation and reflection main terms of Sections 3 and 4, and the non-dihedral quadratic sums of Section 5, are not that missing estimate.

## 7. Where the diagonal antiunitary fails

The matrix of \(R\) in the position basis is \(R_{xz}=p^{-1}\sum_j\xi_j e_p(j(x-z))\). Complex conjugation of the entries replaces \(\xi_j\) by \(\overline{\xi_{-j}}\), after the substitution \(k=-j\). The adjoint \(R^{\dagger}\) is the same circulant with eigenvalues \(\overline{\xi_j}\). Therefore \(K_0RK_0=R^{\dagger}\) if and only if \(\xi_j=\xi_{-j}\) for every \(j\). For \(p>2\) the frequencies \(1\) and \(-1\) are distinct, and the Haar measure of the set \(\xi_1=\xi_{-1}\) is zero.

For a position-diagonal ensemble the antiunitary \(\Theta'=DE_qK_0\) of `BGS-TRACE-131` doubles each reflection family, which is why the short-time value is \(2m\). In the present ensemble those families are still present as pairings, but Section 6 shows that their Haar weight is \(o(1)\). The doubling is not the weight that enters the form factor. For \(\alpha\not\equiv\delta\) the statement \(K_0RK_0=R^\dagger\iff\xi_j=\xi_{-j}\) concerns \(K_0\) only. The argument does not classify an antiunitary that is not diagonal in the position basis.

## 8. The odd symbol energy

The maintained symbol has momentum coefficient proportional to \(r(q)\cos(2\pi p-\alpha_0)\), with \(e^{i\alpha_0}=(-3+4i)/5\). Thus \(\cos\alpha_0=-3/5\) and \(\sin\alpha_0=4/5\), and
\[
\cos(\theta-\alpha_0)=-\frac35\cos\theta+\frac45\sin\theta.
\]
The two summands are orthogonal in \(L^2\) of the momentum circle and have equal norms. The odd summand carries the fraction \(16/25\) of the energy of the modes \(\ell=\pm 1\). That energy is \(9/80000\), so the odd energy is \(9/125000\). The count \(25\cdot 36=900\) and the denominator \(4000^2\) are the same integer identity as in `BGS-TRACE-130`; the factor \(16/25\) is new. The choice \(v=\sigma_{\mathrm{odd}}\eta^2\) is a convention. Matching the phase variance of time-reversed partners, \(2\eta\sum V_{\mathrm{odd}}\), would give \(v=2\sigma_{\mathrm{odd}}\eta^2\). Neither identification is derived, and neither evaluates the sixteen-phase propagator.

## 9. Self-audit

The main term was checked against an exact bucket sum before the error constant was trusted. At time three the bucket values are \(2.8816\) at \(p=5\), \(2.9542\) at \(p=7\), and \(2.9876\) at \(p=11\), against \(m=3\). These primes satisfy \(\lambda\not\equiv -1\). The bound of Theorem 1 is an upper bound and is not sharp.

The factor \(e^{-vm}\) is not claimed at time two. The reflection family is equal to the rotation family when \(m=2\). The recorded seeded sample (`python_stdout.json`) at \(p=29\), \(m=3\), \(v=0.4\), of \(600\) draws, has mean \(3.709\) against the limit \(3.904\). An independent exact evaluation gives \(3.7555\) at \(p=29\) and \(3.7182\) at \(p=23\), a finite-\(p\) gap of about \(4.2/p\). The sample does not test the constant in the exponent. Richardson extrapolations from \(p=23\) and \(p=29\) give \(3.8985\) against \(3.9036\) at \(v=0.4\), and \(3.144\) against \(3.149\) at \(v=1\).

The quadratic-sum bound uses diagonalization over an odd finite field. It is not a Weil bound on a curve. The constant \(p^{-1/2}\) is the rank-one case and is not sharp for a form of higher rank.

Tanner, Journal of Physics A 34 (2001), 8485–8500, and Pakoński–Życzkowski–Kuś, Journal of Physics A 34 (2001), 9303–9317, remain the references for the occupation constraint, as in `BGS-TRACE-127`. Diaconis and Shahshahani, Journal of Applied Probability 31A (1994), 49–62, give \(k!\,m^k\) for Haar \(U(N)\) when \(N\ge km\). The argument here is the same moment count for a different measure. Saito and Nagao, arXiv:nlin/0505055, equation (7), identify \(\tau(1+e^{-bT})\) with the Pandey–Mehta diagonal term. Their \(\mu=bT\) is \(\Lambda\tau\) in the proposed limit of Theorem 3. The values \(m\) and \(m(1+e^{-vm})\) are Berry's diagonal approximation and its GOE–GUE crossover (Bohigas, Giannoni, Ozorio de Almeida, Schmit, Nonlinearity 8 (1995) 203–221, the source of Saito–Nagao eq. (7)); unitary-class short-time counts for random-phase ensembles are those of Tanner and of Pakoński–Życzkowski–Kuś, and CUE statistics for cat maps with both position and momentum shears are known numerically (de Carvalho–Keating–Robbins, J. Phys. A 31 (1998) 5631; Keating–Mezzadri, Nonlinearity 13 (2000) 747). The new content is the finite-\(p\) error bound for this ensemble. The higher-order encounter corrections are not proved here.

Row inversion, proved in `BGS-TRACE-128` to have limit \(m\), is a different matrix. It is not a momentum phase. A second position diagonal remains inside the orthogonal count, by the conjugation recorded there.

## 10. Certificates

- `computations/verification/momentum_phase_cue.py`
- `computations/cpp/momentum_phase_cue.cpp`
- `formalization/Bgs/MomentumPhaseCue.lean`
- `evidence/executions/20261029/momentum-phase-cue/README.md`

The programs recompute the bucket sums and the integer energy. Lean decides the cross-multiplication of \(9/125000\), the constants \(468\) and \(20\), and the residues \(27\bmod 5,7,11,13\) (so \(3^3\not\equiv 1\) at \(5,7,11\) and \(3^3\equiv 1\) at \(13\); the conditions \(t=1,2\) are not formalized). A pass does not prove `BGS-TRACE-005` or `BGS-BGS-001`.
