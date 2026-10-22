# A two-step obstruction inside the unistochastic class

**Claim:** BGS-TRACE-074. **Status:** project proof with independent internal
reconstruction; finite controls have separate scope. The original candidate
was written on 11 October and promoted on 12 October 2026. Priority is not
established. This theorem concerns a static shortcut for entry flatness,
not deterministic BGS or the probability of the Schur good event.

## 1. Statement and quantitative bounds

Let \(J_n\) have every entry equal to \(1/n\). For every sufficiently large
integer \(n\), there is a unitary \(S_n\), with intensity matrix
\(P_{k\ell}=|(S_n)_{k\ell}|^2\), such that, for two fixed distinct labels \(i,j\),

\[
 \delta_n:=\max_{k,\ell}P_{k\ell}\le t_n:=\frac{8\log(2n)}n,\qquad
 \rho_n:=\|P-J_n\|_{\rm op}
 \le\varepsilon_n:=n^{-1/8}+16\sqrt{\frac{\log(2n)}n}\longrightarrow0,
 \tag{1}
\]
\[
 (P^2)_{ij}=\frac1{b_n},\qquad
 b_n=\left\lfloor\frac n{\log(2n)}\right\rfloor,\qquad
 n(P^2)_{ij}\sim\log(2n).
 \tag{2}
\]

Here the norm is a **singular** operator norm. The matrices are genuinely
unistochastic, not merely doubly stochastic. Consequently neither
\((P^2)_{ij}=O(1/n)\) nor a universal inequality

\[
 |((P-J_n)^2)_{ij}|\le C\rho_n\delta_n
 \tag{3}
\]

follows from unitarity, logarithmic entry flatness and a vanishing intensity
singular norm. The construction changes a Haar unitary by rank at most two.

There is also a positive companion: every nonnegative doubly stochastic
matrix \(P\), with \(\delta=\max P_{k\ell}\) and
\(\rho=\|P-J_n\|_{\rm op}\), satisfies, for every integer \(h\ge2\),

\[
 |(P^h)_{ij}-1/n|
 \le \rho^{h-2}
 \sqrt{\left(\sum_kP_{ik}^2-\frac1n\right)
       \left(\sum_kP_{kj}^2-\frac1n\right)}
 \le \rho^{h-2}(\delta-1/n).
 \tag{4}
\]

For \(h=2\), the factor \(\rho^0\) means \(1\), including when \(\rho=0\).
Our sequence has a logarithmic two-step peak while
\(\max_{ij}n|(P^3)_{ij}-1/n|\to0\). The extra singular-norm factor enters
at the third step; it cannot in general be inserted at the second.

## 2. A rank-one unitary correction

For unit vectors \(c,d\in\mathbb C^n\), define

\[
 H(c,d)=I-\frac{(c-d)(c-d)^*}{1-d^*c}\quad(c\ne d),
 \qquad H(c,c)=I.
 \tag{5}
\]

The denominator can vanish only if \(c=d\), by equality in
Cauchy--Schwarz. Write \(v=c-d\) and \(\gamma=1-d^*c\). Then
\(v^*c=\gamma\) and \(\|v\|^2=\gamma+\bar\gamma\), whence
\[
 Hc=d,\qquad
 H^*H=I+vv^*
 \left(-\gamma^{-1}-\bar\gamma^{-1}
       +\frac{\|v\|^2}{|\gamma|^2}\right)=I.
 \tag{6}
\]
Thus \(H\) is unitary and \(\operatorname{rank}(H-I)\le1\).
It fixes the orthogonal complement of the span of \(c,d\).

Fix \(B\subset\{1,\ldots,n\}\setminus\{i,j\}\), with \(|B|=b_n\).
Choose the fixed vectors \(a=\beta=b_n^{-1/2}\mathbf1_B\).
Let \(Z\) be Haar distributed in \(U(n)\), and set
\[
 L=H(Ze_j,\beta),\quad W=LZ,\quad r=W^*e_i,\quad
 R=H(a,r),\quad S=WR.
 \tag{7}
\]
Since \(We_j=\beta\) and \(\beta_i=0\), we have \(r\perp e_j\).
Both \(a\) and \(r\) are orthogonal to \(e_j\), so \(Re_j=e_j\).
It follows that
\[
 Se_j=\beta,\qquad Sa=e_i,\qquad e_i^*S=a^*.
 \tag{8}
\]
These compatible row and column prescriptions imply (2) exactly, on
every outcome:
\[
 (P^2)_{ij}
 =\sum_k |a_k|^2|\beta_k|^2=b_n\cdot b_n^{-2}=1/b_n.
 \tag{9}
\]
Furthermore
\[
 S-Z=(L-I)Z+LZ(R-I),\qquad
 \operatorname{rank}(S-Z)\le2,\qquad
 \|S-Z\|_{\rm HS}\le2\sqrt2.
 \tag{10}
\]
The last inequality uses \(\|S-Z\|_{\rm op}\le2\) for two unitaries.

## 3. The residual completion is Haar: an invariance proof

The corrections are dependent on \(Z\). We do not assume that \(S\) and
\(Z\), or either of their flatness events, are independent.

Consider the compact subgroup
\[
 \mathcal G=\{G\in U(n):G\beta=\beta,\ Ge_i=e_i\}\simeq U(n-2).
 \tag{11}
\]
For \(G\in\mathcal G\), replacing \(Z\) by \(GZ\) leaves its Haar law
unchanged. The identity
\(H(Gc,\beta)=G H(c,\beta)G^*\) shows that \(W\) changes to \(GW\).
The vector \(r=W^*e_i\) is unchanged, as is \(R\), and \(S\) changes to
\(GS\). Thus the joint law of \((r,S)\) is invariant under
\((r,S)\mapsto(r,GS)\).

For almost every \(r\), its regular conditional distribution of \(S\)
is consequently \(\mathcal G\)-invariant. One can first use a countable
dense subgroup and then continuity to make this assertion simultaneous
in \(G\). The group acts freely and transitively on the compact space of
unitary completions of (8): if \(S_1,S_2\) obey (8), then
\(S_2S_1^*\) fixes both \(\beta,e_i\); a group element fixing a completion
is the identity. Uniqueness of normalized Haar measure on this torsor
therefore gives the uniform completion law. In particular,
\[
 S=\beta e_j^*+e_i a^*+V,
 \tag{12}
\]
where \(V\) is a Haar unitary isomorphism from
\(\{e_j,a\}^{\perp}\) to \(\{\beta,e_i\}^{\perp}\), of dimension \(n-2\).
This conditional law is the same for almost every \(r\).

For \(k\ne i,\ell\ne j\), the entry \(S_{k\ell}=V_{k\ell}\).
Projection onto the two complements expresses this entry as a Haar
entry in dimension \(d=n-2\), multiplied by two fixed projection norms
whose product is at most one. For a Haar entry \(U_{11}\) in \(U(d)\),
\(|U_{11}|^2\) has the Beta\((1,d-1)\) law: normalize \(d\) independent
standard complex Gaussians, whose squared moduli are independent
mean-one exponentials. Therefore, for \(0<t<1\),
\[
 \mathbb P(|V_{k\ell}|^2>t)\le(1-t)^{n-3}.
 \tag{13}
\]
All forced row and column entries are at most \(1/b_n\).
For large \(n\), \(1/b_n\le t_n<1\), and the union bound yields
\[
 \mathbb P(\max|S_{k\ell}|^2>t_n)
 \le n^2 e^{-(n-3)t_n},\qquad
 \mathbb P(\max|Z_{k\ell}|^2>t_n)
 \le n^2 e^{-(n-1)t_n}.
 \tag{14}
\]
Both right sides tend to zero.

## 4. An exact centered Haar intensity moment

Write \(P_Z=|Z|^2\) entrywise and \(E_Z=P_Z-J_n\).
Bistochasticity gives
\[
 \|E_Z\|_{S_4}^4=\operatorname{Tr}[(E_ZE_Z^*)^2]
 =\operatorname{Tr}[(P_ZP_Z^*)^2]-1.
 \tag{15}
\]

Let \(\alpha=Z^*e_1\) denote the **random** first-row vector, distinct
from the prescribed fixed vector \(a\) in (7). Its squared moduli
\(p_\ell=|\alpha_\ell|^2\) have the Dirichlet\((1,\ldots,1)\) law.
Normalized complex Gaussians give, for nonnegative integers \(m_\ell\),
\[
 \mathbb E\prod_\ell p_\ell^{m_\ell}
 =\frac{(n-1)!\prod_\ell m_\ell!}
        {(n-1+\sum_\ell m_\ell)!}.
 \tag{16}
\]
Writing \(s_q=\sum_\ell p_\ell^q\), this implies
\[
 \mathbb Es_2=\frac2{n+1},\quad
 \mathbb Es_3=\frac6{(n+1)(n+2)},\quad
 \mathbb Es_2^2=\frac{4(n+5)}{(n+1)(n+2)(n+3)}.
 \tag{17}
\]

Conditional on \(\alpha\), the second row vector \(\xi=Z^*e_2\) is
uniform on the unit sphere of \(\operatorname{Ran}\Pi\), where
\(\Pi=I-\alpha\alpha^*\) has rank \(d=n-1\). For any Hermitian \(D\),
\[
 \mathbb E[(\xi^*D\xi)^2\mid\alpha]
 =\frac{(\operatorname{Tr}D\Pi)^2+\operatorname{Tr}(D\Pi D\Pi)}
        {d(d+1)}.
 \tag{18}
\]
To obtain this identity directly, use a standard complex Gaussian in
\(\operatorname{Ran}\Pi\): its direction and radius are independent;
the fourth Gaussian moment has the two pairings, and the squared
radius has second moment \(d(d+1)\).

For \(D=\operatorname{diag}(p_\ell)\), the two traces in (18) are
\(1-s_2\) and \(s_2-2s_3+s_2^2\). Hence
\[
 \mathbb E\left[\left(\sum_\ell p_\ell|Z_{2\ell}|^2\right)^2
               \mathrel{\big|}\alpha\right]
 =\frac{1-s_2-2s_3+2s_2^2}{n(n-1)}.
 \tag{19}
\]
The \(n\) same-row terms and \(n(n-1)\) distinct-row terms in (15) now give
the exact identity
\[
 \boxed{\mathbb E\|P_Z-J_n\|_{S_4}^4
 =\frac{2(n-1)(n+4)}{(n+1)(n+2)(n+3)}\le\frac2n.}
 \tag{20}
\]
Thus Markov's inequality proves
\[
 \mathbb P(\|P_Z-J_n\|_{\rm op}>n^{-1/8})\le2n^{-1/2}.
 \tag{21}
\]
This elementary rate suffices; no optimal Haar singular-norm rate is claimed.

## 5. Simultaneous witnesses and the failed estimate

On the two flatness events in (14), entrywise
\(\big||S_{k\ell}|^2-|Z_{k\ell}|^2\big|
\le(|S_{k\ell}|+|Z_{k\ell}|)|S_{k\ell}-Z_{k\ell}|\). Consequently
\[
 \|P-P_Z\|_{\rm op}\le\|P-P_Z\|_{\rm HS}
 \le2\sqrt{t_n}\|S-Z\|_{\rm HS}\le4\sqrt{2t_n}.
 \tag{22}
\]
All the conditions needed for (1) hold simultaneously with probability
at least
\[
 1-2n^{-1/2}-n^2e^{-(n-3)t_n}-n^2e^{-(n-1)t_n}\longrightarrow1.
 \tag{23}
\]
No independence is used. This proves existence for each sufficiently
large \(n\); selecting one witness per \(n\) gives the asserted sequence.

Since \(P J_n=J_nP=J_n\),
\(((P-J_n)^2)_{ij}=1/b_n-1/n\). Also
\(n/b_n\ge\log(2n)\). Therefore
\[
 \frac{|((P-J_n)^2)_{ij}|}{\rho_n\delta_n}
 \ge\frac{1-1/\log(2n)}{8\varepsilon_n}\longrightarrow\infty.
 \tag{24}
\]
The denominator is positive: otherwise \(P=J_n\), contradicting (2).
This refutes (3).

## 6. The correct higher-step bound and the Schur variance boundary

For any doubly stochastic \(P\), set \(E=P-J_n\). We have
\(E^h=P^h-J_n\). For \(h\ge2\),
\[
 |(E^h)_{ij}|=|(e_i^*E)E^{h-2}(Ee_j)|
 \le\|e_i^*E\|_2\,\rho^{h-2}\,\|Ee_j\|_2.
 \tag{25}
\]
The squared row and column norms are exactly the two factors in (4),
and \(\sum_kP_{ik}^2,\sum_kP_{kj}^2\le\delta\).
This proves (4). Applied to (1), it gives
\[
 \max_{ij} n|(P^3)_{ij}-1/n|
 \le8\varepsilon_n\log(2n)\longrightarrow0.
 \tag{26}
\]

The [entry-flatness route](../archive/record/entry_flatness_route_20261011.md)
has the exact bracket for one uniformly chosen Schur elimination with a
fresh uniform feedback phase. Define \(\Delta S_{ij}=0\) when the selected
label is \(e\in\{i,j\}\), and
\(\Delta S_{ij}=qS_{ie}S_{ej}\) otherwise, where
\(q=w/(1-S_{ee}w)\). For \(P_{ee}<1\),
\[
 \mathbb E(|\Delta S_{ij}|^2\mid S)
 =\frac1n\sum_{e\notin\{i,j\}}
       \frac{P_{ie}P_{ej}}{1-P_{ee}}.
 \tag{27}
\]
At our constructed states, the prescribed row and column give
\[
 \frac1{nb_n}\le\mathbb E(|\Delta S_{ij}|^2\mid S)
 \le\frac1{nb_n(1-t_n)}\sim\frac{\log(2n)}{n^2}.
 \tag{28}
\]
Thus a universal \(C/n^2\) one-step variance estimate cannot be deduced
from the static hypotheses in (1), even for actual unitary intensities.
The states are admissible inputs to one feedback step; we do **not**
claim that they occur along the maintained random Schur trajectory.
Nor does the uniform three-step law (26) replace the two-step kernel in
the exact bracket (27).

## 7. Dependencies, controls and open conclusion

The proof uses finite unitary algebra, compact-group Haar invariance,
complex Gaussian sphere moments, Cauchy--Schwarz, a union bound and
Markov's inequality. It does not depend on TRACE-060/073's conditional
conclusions or import a spectral-gap theorem. The Haar unistochastic
ensemble is prior work; [the source comparison](../literature/unitary_two_step_sources_20261012.md)
does not establish priority for this obstruction.

The [execution packet](../evidence/executions/20261012/unitary-two-step/README.md)
separates the reviewed original argument, the maintained transcription,
exact rational finite construction checks, and floating diagnostics.
There is no analytic Lean formalization or external referee certification.

The all-time Schur entry-flatness probability is still open. A successful
proof must control the evolving two-step row--column correlations or their
accumulated effect using information beyond the three static properties
in (1). Full TRACE-055, signed TRACE-005 and global deterministic BGS
remain open.
