# Twisted closure formula and the revival law at the scalar return (diagonal kick)

**Claim IDs:** `BGS-TRACE-133` (twisted closure formula), `BGS-TRACE-134` (pointwise revival bound and its limit on the minimal-period sequence), `BGS-TRACE-135` (half-period parity reduction). Two companion statements are **open**: `BGS-TRACE-136` (free-with-parity revival law, even order) and `BGS-TRACE-137` (exponential revival law at odd order, generic dimensions).

**Status.**
* **Proofs.** The proofs of 133, 134 and 135 are project proofs, given below. An independent internal referee audit (2026-10-29) found the mathematics sound and required write-up corrections, which are incorporated here. There is no external referee.
* **Python.** `computations/verification/revival_closure_law.py` and `revival_half_period_parity.py` check the identities in floating point and the integer facts exactly. They also print Monte Carlo diagnostics for the limit theorem and the open laws.
* **Lean.** `formalization/Bgs/RevivalClosureRational.lean` decides only finite integer facts: orders, \(\kappa\), Cayley–Hamilton, the Pell shape, the phase arithmetic of the closure formula at \(N=7\), two exhaustive norm-lemma boxes, and the half-period at \(61\) and \(101\). It does not formalize the operator identity, the trace or the analytic bound.
* **Scope.** The explicit bound of 134 gives **no information at any computable dimension**: it is below \(1\) only from \(N\approx10^{191}\), at \(\lambda=1/4\). 134 is a limit theorem.
* `BGS-TRACE-005` and `BGS-BGS-001` remain **open**.

Every statement is for the **position-diagonal kick** \(D_\varphi\) (the \(\ell=0\) rows of the sixteen-pair kick of `BGS-TRACE-126`), except the general-kick form of Theorem 1. It is not the full kick \(e^{i\eta A_N}\) and not the fixed kick.

## 1. Setting

* \(N\ge3\) is odd and \(e_N(x)=e^{2\pi i x/N}\).
* \(S=\begin{pmatrix}3&4\\2&3\end{pmatrix}\), with eigenvalue \(\lambda=3+2\sqrt2\). Then \((\lambda-1)^2=4\lambda\) and \(S^2-6S+I=0\).
* \(M_N\), \(T_N(a,b)\) and the Egorov relation \(M_NT_N(v)M_N^{-1}=T_N(Sv)\) are as in `BGS-TRACE-126`. Here \(T(u)T(v)=e_N(2^{-1}\omega(u,v))T(u+v)\), \(\omega(u,v)=u_1v_2-u_2v_1\), and \(\operatorname{Tr}T(v)=N\delta_{v\equiv0}\).
* Pell form: \(S^d=\begin{pmatrix}x_d&4y_d\\2y_d&x_d\end{pmatrix}\) with \(x_d^2-8y_d^2=1\). So \(v_j:=S^je_2=(4y_j,x_j)\) and \(\omega(e_2,S^de_2)=-4y_d\).
* \(t=\operatorname{ord}_N(S)\) and \(\kappa_N=(\operatorname{Tr}S^t-2)/N^2\in\mathbb Z_{\ge1}\). Then \(\lambda^t>N^2\), so \(t>2\log_\lambda N\).
* The kick is \(D_\varphi=\operatorname{diag}\exp(i\eta f_\varphi(q))\), with \(f_\varphi(q)=\sum_r2|c_r|\cos(2\pi k_rq/N+\varphi_r+\alpha_r)\) over the seven diagonal pairs \(k_r\in\{1,2,5,6,7,8,9\}\) (\(K=9\)), and i.i.d. uniform phases.
  * \(\sigma_d=2\sum_r|c_r|^2=13203/32000\).
  * The full-kick energy \(\sigma=66033/160000\) of `BGS-TRACE-126` exceeds it by \(9/80000\): the rows \(\ell=\pm1\), \(9/160000\) each, as in `BGS-TRACE-129`.
* Write \(w_r=2\eta|c_r|\), \(W=\sum_rw_r\), \(J=\prod_rJ_0(w_r)\), \(\rho=e^W-1\), \(\lambda_{\rm rev}=\eta^2t\sigma_d\).
* Fourier coefficients: \(D=\sum_a\hat d(a)T(0,a)\), with \(\hat d(a)=\sum_{n\cdot k\equiv a}c(n)\), \(c(n)=\prod_ri^{n_r}J_{n_r}(w_r)e^{in_r(\varphi_r+\alpha_r)}\) and \(|c(n)|\le\prod_r(w_r/2)^{|n_r|}/|n_r|!\).

## 2. Theorem 1 (BGS-TRACE-133): twisted closure formula

For every odd \(N\), every \(m\ge1\) and every diagonal \(D\), with \(D_j=M_N^jDM_N^{-j}\),
\[
\operatorname{Tr}(D_0D_1\cdots D_{m-1})=N\sum_{a\in\Lambda_m}e_N(\beta(a))\prod_{j<m}\hat d(a_j),
\]
where
* \(\Lambda_m=\{a\in(\mathbb Z/N)^m:\sum_ja_jS^je_2\equiv0\}\) and \(\beta(a)=-2\sum_{i<j}a_ia_jy_{j-i}\);
* \(|\Lambda_m|=N^{m-2}\) for \(m\ge2\), and \(\Lambda_1=\{0\}\).

At a scalar return \(S^m\equiv I\), we have \(M_N^m=cI\) with \(|c|=1\), and \(\operatorname{Tr}U^m=(\operatorname{Tr}M_N^m/N)\operatorname{Tr}(D_0\cdots D_{m-1})\). Deleting \(e_N(\beta)\) gives exactly the classical orbit sum \(N^{-2}\sum_z\prod_jD(q(S^jz))\). The general kick \(K=\sum_u\hat g(u)T(u)\) gives the same formula with \(\Lambda=\{u\in G^m:\sum S^ju_j\equiv0\}\) and phase \(e_N(2^{-1}\sum_{i<j}\omega(S^iu_i,S^ju_j))\).

*Proof.*
1. \(D_j=\sum_a\hat d(a)T(av_j)\).
2. The cocycle gives \(\prod_jT(a_jv_j)=e_N(2^{-1}\sum_{i<j}a_ia_j\omega(v_i,v_j))T(\sum_ja_jv_j)\).
3. Since \(\det S=1\), \(\omega(v_i,v_j)=\omega(e_2,S^{j-i}e_2)=-4y_{j-i}\). So the phase is \(e_N(\beta(a))\), and no inverse of \(2\) survives.
4. Take the trace.
5. Count: for \(m\ge2\), \(a\mapsto\sum a_jv_j\) is onto, because \(v_0=(0,1)\) and \(v_1=(4,3)\) have determinant \(-4\), a unit modulo odd \(N\).
6. Scalar return: \(M^m\) commutes with every \(T(v)\), so Schur's lemma gives \(M^m=cI\). Then \((DM)^m=D_0\cdots D_{m-1}M^m\).
7. Classical sum: \(\sum_ze_N(\sum_ja_j(S^jz)_1)=N^2\delta(\sum_ja_j(S^j)^Te_1\equiv0)\). Since \((S^j)^Te_1=(x_j,4y_j)\) is \(v_j\) with its coordinates swapped, the condition is the same \(\Lambda_m\). ∎

*Algebraic form.* \(a\in\Lambda_m\) iff \(a(S)\equiv0\pmod N\). For odd \(N\) this holds iff \(N\mid a(\lambda)\) in \(\mathbb Z[\sqrt2]\): reduce to \(\alpha+\beta S\), and note \(\alpha+\beta\lambda=(\alpha+3\beta)+2\beta\sqrt2\). Note that \(\mathbb Z[\lambda]=\mathbb Z[2\sqrt2]\) has index \(2\) in \(\mathbb Z[\sqrt2]\); only \(|\mathrm{Nm}\,a(\lambda)|\ge N^2\) is used below.

*Phase average (standard, recorded for this model).* For every unitary \(M\) and every \(m\), Kluyver's average \(\mathbb E\,e^{iw\,\mathrm{Re}(e^{i\varphi}Z)}=J_0(w|Z|)\) applied to the position-basis path sum gives
\[
\mathbb E_\varphi|\operatorname{Tr}(D_\varphi M)^m|^2=\sum_{x,y}K(x)\overline{K(y)}\prod_rJ_0(w_r|V_r(x)-V_r(y)|),
\]
with \(K(x)=\prod_jM(x_j,x_{j+1})\) and \(V_r(x)=\sum_je_N(k_rx_j)\). This is the quantum analogue of the orbit-sum Bessel identity of `BGS-TRACE-129`.

## 3. Norm lemma

**Lemma 1.** If \(\deg p<L\), \(|p_j|\le A\), \(p(S)\equiv0\pmod N\) and \(A^2\lambda^L\le4N^2\), then \(p(\lambda)=0\), i.e. \(x^2-6x+1\mid p\).

*Proof.* If \(p(\lambda)\ne0\), then \(N\mid p(\lambda)\) in \(\mathbb Z[\sqrt2]\) gives \(|\mathrm{Nm}|\ge N^2\). But \(|p(\lambda)|<A\lambda^L/(\lambda-1)\) and \(|p(\bar\lambda)|<A\lambda/(\lambda-1)\), so \(|\mathrm{Nm}|<A^2\lambda^L/4\). ∎

**Lemma 2 (runs).** Let \(p=p_1+x^mp_2\) with \(p(\lambda)=0\), coefficients bounded by \(A\), and a zero gap \(g>G_A:=\lfloor2\log_\lambda(A/2)\rfloor\) between \(p_1\) and \(x^mp_2\). Then \(p_1(\lambda)=p_2(\lambda)=0\). Every non-zero relation has at least three non-zero coefficients.

*Proof.* If \(p_2(\lambda)\ne0\), then \(|p_2(\lambda)|\ge(\lambda-1)/(A\lambda)\), which forces \(\lambda^g<A^2/4\). A two-term relation would make some \(\lambda^k\) rational. ∎

**Dichotomy.** Let \(S^t\equiv I\) and \(a\in\Lambda_t\setminus\{0\}\) with all centred \(|a_j|\le A<N/2\). Then exactly one of the following holds:
* **Case 1.** Some cyclic zero gap \(g\) has \(A^2\lambda^{t-g}\le4N^2\). After a rotation, the integer lift is a relation, and each run is a relation with at least three entries.
* **Case 2.** Every gap is at most \(g^*=\lceil t-\log_\lambda(4N^2/A^2)\rceil-1\), and the support has at least \(s_0=\lceil t/(g^*+1)\rceil\) entries.

## 4. Theorem 2 (BGS-TRACE-134): pointwise bound and the limit on the minimal-period sequence

Let \(S^t\equiv I\pmod N\), \(N>2K=18\) and \(2\le A<N/2\). Then for every \(\varphi\),
\[
\Bigl|\frac{\operatorname{Tr}U^t}{\operatorname{Tr}M_N^t}-\hat d(0)^t\Bigr|\le E_T+E_D+E_R,
\]
where
* \(E_T=t\,\tau_Ae^{W(t-1)}\), with \(\tau_A=\sum_{d>A/K}W^d/d!\);
* \(E_D=\sum_{s\ge s_0}\binom ts\rho^s\);
* \(E_R=(1+w)^t-1\), with \(w=(G_A+1)^2\rho^3/(1-(G_A+1)\rho)\).

Moreover \(|\hat d(0)-J|\le W^3e^W/6\).

*Proof.*
1. By Theorem 1, the difference is the sum over \(\Lambda_t\setminus\{0\}\).
2. Mass bounds:
   * \(\sum_{|n|_1=d}|c(n)|\le W^d/d!\);
   * \(\sum_{a\ne0}|\hat d(a)|\le\rho\) and \(\sum_a|\hat d(a)|\le e^W\);
   * \(\sum_{|a|>A}|\hat d(a)|\le\tau_A\);
   * \(|\hat d(0)|\le1\).
3. Configurations with a large entry give \(E_T\).
4. Case 2 gives \(E_D\).
5. Case 1: by Lemma 2 these are unions of runs, each with \(s\ge3\) entries and \(s-1\) internal gaps in \([0,G_A]\). Their total is at most \(\prod(1+w)-1\).
6. Finally, \(n\cdot k\equiv0\) with \(1\le|n|_1\le2\) is impossible for \(N>18\), because the \(k_r\) are distinct. This gives the estimate for \(\hat d(0)\). ∎

**Corollary.** Suppose \(N\to\infty\) with \(S^t\equiv I\), \(\eta^2t\to\theta\) and \(\log\kappa_N=o(\sqrt t)\), i.e. \(t=2\log_\lambda N+o(\sqrt t)\). Then \(\sup_\varphi|\operatorname{Tr}U^t/\operatorname{Tr}M_N^t-e^{-\theta\sigma_d/2}|\to0\). Hence \(\mathbb E|\operatorname{Tr}U^t|^2/N^2\to e^{-\lambda_{\rm rev}}\).

*Proof.* Take \(A=t^2\). Then:
* \(W\asymp t^{-1/2}\);
* \(E_T\to0\);
* \(g^*=O(\log\kappa+\log t)\), so \(E_D\le\sum(e(g^*+1)\rho)^s\to0\);
* \(tw=O(t^{-1/2}\log^2t)\);
* \(t\log J=-\eta^2t\sigma_d/2+O(\eta^4t)\). ∎

**Scope.** The hypothesis holds along the Bonechi–De Bièvre sequence \(\tilde N_k=\gcd(p_k,p_{k-1}+1)\), where \(S^k=p_kS-p_{k-1}I\) (Commun. Math. Phys. 211 (2000) 659). This is the minimal-period sequence of Faure–Nonnenmacher–De Bièvre (Commun. Math. Phys. 239 (2003), eqs. (102)–(104), Lemma 4):
* odd \(k\): \(N=7,41,239,1393,8119,47321,\dots\), with \(\kappa=4\) and \(t-2\log_\lambda N=0.786\dots\);
* \(k\equiv2\pmod4\): \(N=35,1189,40391,\dots\), with \(\kappa=32\) and \(t-2\log_\lambda N=1.966\dots\).

**Ineffectiveness.** With the sharp \(E_R\), optimised over \(A\):

| \(N\) | \(\lambda_{\rm rev}=1/4\) | \(\lambda_{\rm rev}=1\) |
|---|---|---|
| \(41\) | \(12.6\) | \(\infty\) |
| \(1189\) | \(28.7\) | \(7.9\cdot10^3\) |
| \(N\approx10^{192}\) (\(t=501\)) | \(0.79\) | \(5.4\cdot10^4\) |
| \(N\approx10^{19139}\) | \(0.11\) | \(2.36\) |

Monte Carlo at \(N=41,239,1189,8119\) shows \(\max_\varphi|R-\hat d(0)^t|\) at \(\lambda_{\rm rev}=1\) falling as \(0.035,0.020,0.0065,8\cdot10^{-4}\). This is consistent with the limit theorem, but the explicit bound gives no information there.

**Not claimed.**
* No statement at returns \(kt\) with \(k\ge2\). There the two-term closures \(a_j=-a_{j+t}\) defeat Lemma 1.
* No statement for generic \(N\), and none for the full or the fixed kick.

## 5. Theorem 3 (BGS-TRACE-135): half-period parity reduction

Let \(N\) be an odd prime with \(t\) even. Then \(S^{t/2}\equiv-I\): in \(\mathrm{SL}_2(\mathbb F_p)\) an involution other than \(\pm I\) would have determinant \(-1\). Hence \(M_N^{t/2}=cP\), where \((P\psi)(x)=\psi(-x)\) and \(|c|=1\): \(M^{t/2}P\) commutes with all \(T(v)\), and Schur's lemma applies. That half-periods quantise to the parity is classical (Hannay–Berry 1980; Kurlberg–Rudnick). Consequently, exactly,
\[
\frac{\operatorname{Tr}U^t}{\operatorname{Tr}M_N^t}=N^{-1}\operatorname{Tr}(A\,PAP),\qquad A=D_0\cdots D_{t/2-1},\quad PD_jP=M^j(PDP)M^{-j}.
\]
The same holds for composite \(N\) whenever \(S^{t/2}\equiv-I\), e.g. \(201,401,801\). It fails at \(203\) (\(57I\)), \(205\) (\(124I\)) and \(1001\) (\(274I\)).

## 6. Open: BGS-TRACE-136 and BGS-TRACE-137

**136 (free-with-parity law, conjecture).** Treat \(D_0,\dots,D_{t/2-1}\) as free, with \(PDP\) the only correlated partner. Then at most one crossing pair survives:
\[
F_2=(\mu\mu')^{n-1}[\mu\mu'+n(\tau(DD')-\mu\mu')],\qquad n=t/2,\ \mu=\tau(D),\ \mu'=\tau(PDP).
\]
In the small-\(\eta\) limit this gives \(\mathbb E|R|^2\to e^{-\lambda}(1+0.1204622\,\lambda^2)\), with \(0.1204622=\sum_r|c_r|^4/(2\sigma_d^2)\). The constant is derived, not fitted, but only from the heuristic \(F_2\).

Monte Carlo at the primes \(61\) and \(101\) (1500 draws per row; \(\lambda=1,2,3\)):
* five of six rows are within \(2.2\sigma\) of \(F_2\); the row \(N=61\), \(\lambda=3\) is \(3.4\sigma\) low;
* the naive \(e^{-\lambda}\) is off by up to a factor \(2\);
* the classical-orbit law \(e^{-\lambda}\prod_rI_0(2\lambda|c_r|^2/\sigma_d)\) is rejected by \(4\sigma\) to about \(50\sigma\).

**137 (odd order, conjecture).** For primes with odd \(t\), \(\mathbb E|R|^2\approx e^{-\lambda}\):
* within \(5\%\) at \(N=71,127,151,263\) for \(\lambda\le3\);
* \(18\%\) low at \(N=47\), \(\lambda=3\).

No proof is known. Bounding the sparse closures for generic \(N\), where \(t\gg\log N\) (Kurlberg–Rudnick), would need cancellation in the twisted sums \(\sum e_N(\beta)\prod\hat d\).

## 7. Novelty and references

* Theorem 1 is a new **explicit form**, with the Pell cocycle \(\beta\), of an exact expansion of the type of Boasman–Keating (Proc. R. Soc. A 449 (1995) 629). It specialises the trace-closure lemma of `BGS-TRACE-126` and the scalar return of `BGS-TRACE-129`.
* The phase average is Kluyver/Jacobi–Anger; compare Tanner (nlin/0104014) and Pakoński–Życzkowski–Kuś (nlin/0011050).
* The half-period parity is classical.
* Only Theorem 2 and its corollary, on the minimal-period sequence, and the conjectural law 136 are candidates for novelty. That rests on a literature search, not a guarantee.
