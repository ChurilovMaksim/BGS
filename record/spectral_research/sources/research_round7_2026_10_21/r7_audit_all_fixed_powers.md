> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_audit_all_fixed_powers.md`. Embedded SHA256: `642e0735bec132681648a07b772a4c48c78231599d4415fc4da3c3af1edb6d5d`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: all fixed physical powers of the original family

21 October 2026. Auditor: r7_physical_audit.

## 1. Verdict and exact audited statement

**Verdict: proved as written, for every fixed positive integer R and all odd N tending to infinity. No mathematical gap was found.**

The audited source is r7_return_all_fixed_powers_phase_separation.md, final SHA-256
46982efaa581d322d4e82d5f5782ccf69f979a5a59adfb863dd40ef292205527.
The fixed original parameter is exactly $\tau=10^{-80}$. I independently reconstructed the proof from the original definitions and the raw mathematical arguments. Author conclusions, other audit conclusions, and author computation scripts were not used as proof inputs.

For $\epsilon=14000\tau$, the source proves that every fixed $R\ge1$ has a positive analytic kernel $k_R$, with both marginals one, such that
$$
 \left\||U_N^R|^{\circ2}
 -\left[N^{-1}k_R(x/N,y/N)\right]_{x,y=0}^{N-1}\right\|_{\rm op}
 \longrightarrow0,
$$
$$
 (1+\epsilon)^{-R}\le k_R\le(1-\epsilon)^{-R},
 \qquad
 \limsup_{N\ {\rm odd}}\||U_N^R|^{\circ2}-J_N\|_{\rm op}
 \le(1-\epsilon)^{-R}-1,
$$
and, eventually for the fixed $R$,
$$
 \max_{x,y}|U_N^R(x,y)|
 \le2\sqrt{b_R}(1-\epsilon)^{-R/2}N^{-1/2}.
$$
The actual diagonal-pair first returns consequently satisfy
$$
 N^{-1}\sum_{r>L}\|F_r(U_N)\|_{\rm HS}^2\longrightarrow1
 \quad\text{for every fixed }L.
$$

There is no claim about a growing $R(N)$, no phase average in these statements, and no conclusion about the trace functional at times proportional to $N$. The proof respects those distinctions. Its new geometric step genuinely removes the former finite cutoff at 49.

| Obligation | Independent finding |
| --- | --- |
| Exact modular quantization and map convention | Corrected symbol, covariance, and physical inverse map agree with the original definition |
| Every intermediate graph | Positive Jacobian follows from the exact partially completed factorization |
| Full nonlinear sheet law | Exact uniqueness and deck identities give the required endpoint lattice |
| No translation intertwiner | Discounted-coordinate proof applies to the corrected symbol and all iterates |
| Separation from endpoint separability | Both integration constants are removed; the induced translations are nontrivial |
| Every sampled alias | Each aliased cycle is nonconstant; the infinitely many distant aliases have a uniform summable bound |
| Wrapped finite-grid WKB | Complete branch sum is exactly periodic; the column and probability errors have the stated powers of N |
| Limiting kernel and marginals | Correct normalization, positivity, and both marginals |
| Fixed-cutoff return mass | Finite-unitary normalization and fixed-power entry bounds suffice without excluding dark states |

## 2. Original symbol, covariance, and signs

The original prescription in round6_main_report.md §1 uses modular inverses of two and eight. For odd $N$, using $2^{-1}=(N+1)/2$ modulo $N$ gives, for raw integer labels,
$$
 e_N(k2^{-1}l)=(-1)^{kl}e^{\pi ikl/N}.
$$
Thus the ordinary Weyl operator is
$$
 W_N(k,l)=(-1)^{kl}T_N(l,k),
 \qquad
 (W_N(k,l)\psi)(x)=e^{2\pi ikx/N+\pi ikl/N}\psi(x+l).
$$
The factor $(-1)^{kl}$ changes the $p$-dependent part of the original symbol by $q\mapsto q+1/2$. Direct Fourier expansion therefore gives exactly
$$
 a(q,p)=\cos14\pi q+\frac{r(q)}{10}
 +\frac{r(q)\sin2\pi q}{100}-\frac1{10}
 +\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha_0).
$$
In particular,
$$
 \widehat a(1,0)=\frac1{20}-\frac{i}{200},
 \qquad
 \widehat a(0,1)=\frac{-3-4i}{1000}
 =\frac{e^{-i\alpha_0}}{200}.
$$
The support has $|k|+|l|\le9$, $|l|\le1$. An independent rational bound obtained by summing absolute real and imaginary parts of all coefficients is $593/500<2$. This confirms the weaker bound used in the proof without relying on numerical Fourier evaluation.

For the original quadratic kernel, the exponents of $M_NT_N(l,k)$ and $T_N(l',k')M_N$, with
$$
 l'=3l+4k,\qquad k'=2l+3k,
$$
agree modulo $N$. This can be checked directly at entries $(x,y)$: the first exponent is the kernel exponent at $(x,y-l)$, plus $k(y-l+2^{-1}l)$; the second is $k'(x+2^{-1}l')$, plus the kernel exponent at $(x+l',y)$. Subtraction gives zero modulo $N$, using the modular inverse of eight.

The parity difference $l'k'-lk=6l^2+16lk+12k^2$ is even. Consequently
$$
 M_N^jQ_N(a)M_N^{-j}=Q_N(a\circ\mathsf S^j)
$$
is an exact identity for ordinary Weyl quantization, including raw labels larger than $N$. It does not assume that an integer frequency has a unique representative modulo $N$.

The generating phase of $M_N$ is
$$
 \Theta(q,s)=-\frac{3q^2-2qs+3s^2}{8}.
$$
With outgoing momentum $\Theta_q$ and incoming momentum $-\Theta_s$, solving for the outgoing variables gives the linear map $\mathsf S^{-1}$. The positive quantum exponential evolves phases by
$$
 \partial_v\Phi=\frac{H(q,\Phi_q)}{2\pi},
 \qquad
 \dot q=-\frac{H_p}{2\pi},\quad
 \dot p=\frac{H_q}{2\pi}.
$$
Therefore, if $\Phi_v$ denotes the flow of $X=(a_p,-a_q)/(2\pi)$, the physical map is
$$
 F=\Phi_{-\tau}\mathsf S^{-1}
 =(\mathsf S\Phi_\tau)^{-1}.
$$
This sign and order are essential. They are consistent throughout the audited proof.

## 3. Positive Jacobians at every quantum stage

Let $C(q,p)=(q,-p)$, $\kappa_v=C\Phi_{-v}C$, and $F_+=CFC$. Since $C\mathsf S^{-1}C=\mathsf S$,
$$
 F_+=\kappa_\tau\mathsf S.
$$
The Fourier support and coefficient bound give $\|X\|\le20$ and $\|DX\|\le2000$, in both norms needed in the source. Reversing momentum and time preserves these bounds. The variational equation implies
$$
 \|D\kappa_v-I\|_\infty\le e^{2000v}-1\le4000\tau
 \quad(0\le v\le\tau).
$$
The last inequality follows, for example, from $e^z\le(1-z)^{-1}$ for $0\le z<1$, since $2000\tau<1/2$.

Every entry of $(D\kappa_v-I)\mathsf S$ has absolute value at most $28000\tau$. The smallest entry of $\mathsf S$ is two. Hence
$$
 (1-\epsilon)\mathsf S
 \le D\kappa_v\,\mathsf S
 \le(1+\epsilon)\mathsf S
 \quad\text{entrywise},\qquad \epsilon=14000\tau.
$$
The product $D\kappa_v\mathsf S$ is positive; positivity of $D\kappa_v$ itself is neither asserted nor needed. Products of positive matrices preserve the entrywise comparisons.

I independently checked the partial-stage identity, since positivity of the final iterate alone would not establish a WKB construction. The exact quantum factorization is
$$
 U_N^R=e^{i\tau NQ(H_0)}\cdots e^{i\tau NQ(H_{R-1})}M_N^R.
$$
In positive coordinates, the classical flow of its $j$-th exponential is
$$
 \mathsf S^j\kappa_v\mathsf S^{-j}.
$$
Starting from $\mathsf S^R$, after $k$ full stages the map is
$$
 \mathsf S^{R-k}F_+^k.
$$
At time $v$ in the next stage, $j=R-k-1$, the map is exactly
$$
 \mathsf S^{R-k-1}\kappa_v\mathsf S F_+^k.
$$
No commuting of different nonlinear factors occurs in this cancellation. Its derivative is bounded between
$$
 (1-\epsilon)^{k+1}\mathsf S^R
 \quad\text{and}\quad
 (1+\epsilon)^{k+1}\mathsf S^R.
$$
These imply the coarser bounds with exponent $R$ at every stage.

All these maps have deck transformation $\mathsf S^R$. If $Q(s,r)$ is their first component, then
$$
 Q(s,r+1)=Q(s,r)+b_R,\qquad
 (1-\epsilon)^Rb_R\le Q_r(s,r)\le(1+\epsilon)^Rb_R.
$$
For each fixed $s$, the map $r\mapsto Q(s,r)$ is thus a global increasing bijection of the real line. Its inverse is analytic. For every fixed finite $R$, compactness modulo the endpoint deck lattice supplies a positive common neighborhood on which the necessary analytic derivatives are bounded.

This reasoning remains valid even when $R\epsilon$ is large or an estimate of the form $\tau\lambda^{2R}\ll1$ fails. Only finiteness of the derivative bounds is subsequently used.

## 4. Initial images and the full nonlinear deck law

Put $(a,b,c)=(a_R,b_R,c_R)$. The exact image sum
$$
 L_N(x,y)=\frac1{\sqrt{bN}}\sum_{m=0}^{b-1}
 \exp\!\left[-\frac{2\pi i}{2bN}
 \{ax^2-2x(y+mN)+a(y+mN)^2\}\right]
$$
has the same two generator intertwinings as $M_N^R$. The polynomial identities in Appendix A are correct; after multiplying by the phase coefficient, their ordinary halves agree with the modular halves because $ab$ and $ac$ are even. Thus $M_N^{-R}L_N$ commutes with both shift and multiplication. Commutation with the latter makes it diagonal, and commutation with the former makes it scalar.

For $g=\gcd(N,b)$, differencing the finite image sum leaves precisely $h=(b/g)j$, $0\le j<g$. Since $N$ and $g$ are odd and $b/g$ is even, the remaining quadratic phase
$$
 e^{-\pi ia(N/g)(b/g)j^2}
$$
equals one. Linear character orthogonality gives
$$
 |L_N(x,y)|^2=\frac gN\,\mathbf1_{\{g\mid x-ay\}}.
$$
Each row has $N/g$ supported columns and norm one. The scalar consequently has modulus one. This proves the image formula without excluding any common divisor of $N$ and $b$.

The initial phases are
$$
 \Theta_m(q,s)=-\frac{aq^2-2q(s+m)+a(s+m)^2}{2b}.
$$
If $u$ is initial output position, the initial positive input momentum is $r=(u-a(s+m))/b$. The Jacobian of the evolving output with respect to $u$ equals $Q_r/b$, so it remains positive at all stages. Characteristic action integration therefore defines global real analytic phases $\Phi_m$, with no change of phase chart or Maslov sign. Its endpoint variations give
$$
 \Phi_q=p_{\rm out},\qquad
 \Phi_s=-p_{\rm in}=r_{\rm in}.
$$
The amplitude is $B_m=J_m^{-1/2}$, where $J_m=Q_r/b$. In particular,
$$
 (1+\epsilon)^{-R}\le B_m^2\le(1-\epsilon)^{-R}.
$$

Writing $S_m=\Phi_m-\Theta_m$, all of the following relations are exact:
$$
 \begin{aligned}
 \Phi_{m+b}&=\Phi_m+q-a(s+m)-ab/2,\\
 \Phi_m(q+1,s)&=\Phi_{m-a}(q,s)-c(s+m)+ac/2,\\
 \Phi_m(q,s+1)&=\Phi_{m+1}(q,s),\\
 S_m(q,s)&=S_0(q,s+m).
 \end{aligned}
$$
Their propagation uses only periodicity of every $H_j$ in $q,p$ and uniqueness of the global characteristic solution. In the first line the momentum changes by one, which preserves the Hamiltonian; in the second, the output position changes by one; additive functions of the parameter $s$ do not change the evolution equation.

Consequently $S=S_0$ has periods $(1,a)$, $(0,b)$, and hence $(b,0)$ and $(a,1)$. The last implication is the exact integer identity
$$
 (a,1)=a(1,a)-c(0,b).
$$
This lattice is present for the complete nonlinear action, not just its first variation.

## 5. No translation intertwiner: all hypotheses verified

I reread the raw discounted-coordinate argument in the cited round-2 source and reconstructed it independently. The new file repeats everything needed; no arithmetic-sector theorem or Egorov estimate from that older file is required here.

Let $\Psi=\mathsf S\Phi_\tau$, $\lambda=3+2\sqrt2$, and $\ell=(1,\sqrt2)/\sqrt3$. Then $\ell\mathsf S=\lambda\ell$. With $\delta=\Phi_\tau-I$, the lift
$$
 v_R(x)=\lambda^{-R}\ell\Psi^R(x)-\ell x
 =\sum_{j=0}^{R-1}\lambda^{-j}\ell\delta(\Psi^jx)
$$
is periodic. This is an exact telescoping identity. Compare it with
$$
 w_R(x)=\tau\sum_{j=0}^{R-1}\lambda^{-j}\ell X(\mathsf S^jx).
$$
The bounds on $X,DX$ give
$$
 \|\delta\|\le20\tau,\qquad
 \|\delta-\tau X\|\le20000\tau^2.
$$
The similarity of $\mathsf S$ to a symmetric matrix yields
$$
 \|\mathsf S^j\|_2\le\sqrt2\lambda^j,\qquad
 \|\Psi^j-\mathsf S^j\|\le50\tau\lambda^j.
$$
The latter estimate uses only the bounded displacement at each kick. Combining its Lipschitz consequence with the bound $\|X\|\le20$ gives
$$
 \|X\circ\Psi^j-X\circ\mathsf S^j\|
 \le\min(10^5\tau\lambda^j,40).
$$
It follows that, uniformly over all positive integers $R$,
$$
 \|v_R-w_R\|
 \le\sum_{j\ge0}
 \left[20000\tau^2\lambda^{-j}
 +\min(10^5\tau^2,40\tau\lambda^{-j})\right]
 <3\cdot10^7\tau^2.
$$
Splitting at $j=200$, using $\lambda>5$, $5^{200}>10^{80}$, and $(1-\lambda^{-1})^{-1}<5/4$, gives the explicit coefficient $20025050<3\cdot10^7$. No limit $\tau\to0$ is taken.

For $j\ge1$,
$$
 \mathsf S^{-Tj}e_1=(a_j,-b_j),\qquad
 \mathsf S^{-Tj}e_2=(-c_j,a_j)
$$
lie outside the symbol strip $|l|\le1$. Thus only the $j=0$ term contributes to the Fourier coefficients of $w_R$ at $e_1,e_2$. The coefficients of the corrected symbol computed above give
$$
 |\ell\widehat X(e_1)|^2=\frac{101}{60000},
 \qquad
 |\ell\widehat X(e_2)|^2=\frac1{120000}.
$$
Both exceed $1/400^2$. Since $3\cdot10^7\tau<1/800$ at the prescribed rational value,
$$
 |\widehat v_R(e_i)|\ge\tau/800>0
 \quad(i=1,2)
$$
for every $R$.

If $\Psi^Rt_h\Psi^{-R}=t_k$ on the torus, connectedness gives a constant integer vector $n$ with
$$
 \Psi^R(x+h)-\Psi^R(x)=k+n.
$$
Iteration in the translation variable yields the same identity with both increments multiplied by any positive integer $L$. The lift of $\Psi^R$ has linear part $\mathsf S^R$ and bounded periodic remainder; division by $L$ therefore forces $k+n=\mathsf S^Rh$. Hence $v_R(x+h)=v_R(x)$.

Its two nonzero Fourier coefficients force $h_1,h_2$ to be integers. Then $k=0$ on the torus as well. This includes irrational input translations and relations with different input and output translations. Reversing the relation proves the same conclusion for $F^R=\Psi^{-R}$.

## 6. Why endpoint separability is impossible

Suppose two distinct sheets modulo $b$ have identically vanishing mixed derivative. Since $\Theta_m-\Theta_n$ is separable and $S_m(q,s)=S(q,s+m)$, translating the input parameter and possibly exchanging the labels gives
$$
 S(q,s+d)-S(q,s)=u(q)+v(s),\qquad 0<d<b,\ d\in\mathbb Z.
$$
The functions are defined on the full real endpoint plane. If vanishing were initially assumed only on the unit square, analytic continuation would first give this global identity.

Let $L=b/\gcd(b,d)$. Summing at $s,s+d,\ldots,s+(L-1)d$ gives zero on the left because $Ld$ is a multiple of the $s$-period $b$. It follows that $u(q)$ is constant. The sheet difference is now independent of $q$, but this alone would not yield the required translation relation.

The second integration constant is removed as follows:
$$
 \overline S(s)=\frac1b\int_0^bS(q,s)\,dq.
$$
The periods $(b,0)$ and $(a,1)$ make this function one-periodic in $s$. Averaging the $q$-independent difference and using the integer $d$ therefore gives
$$
 S(q,s+d)-S(q,s)=\overline S(s+d)-\overline S(s)=0.
$$
This step is valid without any pointwise smallness estimate on $S$.

The remaining phase difference is exactly its initial quadratic difference:
$$
 \Phi_0(q,s+d)-\Phi_0(q,s)
 =\frac{dq-ads-ad^2/2}{b}.
$$
Differentiating gives input momentum increment $ad/b$ and output momentum increment $d/b$. The input position increment $d$ is zero on the torus. The global twist guarantees that the parameters cover every input momentum, so this is a relation between maps on the whole torus:
$$
 F^Rt_{(0,ad/b)}=t_{(0,d/b)}F^R.
$$
Since $a^2-bc=1$, one has $\gcd(a,b)=1$; both translations are nonzero for $0<d<b$. Section 5 excludes this relation. Every distinct pair of full sheet phases consequently has mixed derivative not identically zero.

## 7. The unrestricted sampled fourth-moment lemma

I checked the lattice sum itself, rather than replacing it by an unproved Riemann-sum approximation. For
$$
 A_N(x,y)=N^{-1}a(x/N,y/N)e^{2\pi iN\phi(x/N,y/N)},
$$
the exact fourth Schatten power is an $N^{-4}$-normalized four-variable grid sum with phase
$$
 \mathcal P(x,x',y,y')
 =\phi(x,y)-\phi(x',y)+\phi(x',y')-\phi(x,y').
$$
If $\mathcal P-\xi\cdot z$ were constant for any fixed real $\xi$, then $\mathcal P$ would be affine. An affine function vanishing both on $x=x'$ and on $y=y'$ is identically zero. Differentiating in $x,y$ would give $\phi_{xy}=0$. Thus the mixed-derivative hypothesis rules out a constant phase at every real alias, not only at zero.

A smooth interior cutoff changes the normalized grid sum by at most $C(\delta+N^{-1})$, by counting the grid points in a boundary strip. For fixed cutoff width $\delta$, exact Poisson summation gives
$$
 \sum_{k\in\mathbb Z^4}
 \int \mathcal A_\delta(z)
 e^{2\pi iN(\mathcal P(z)-k\cdot z)}\,dz.
$$
Every fixed summand tends to zero. A nonconstant analytic phase has a critical set of measure zero, since at least one of its first derivatives is a nonzero analytic function. Delete an arbitrarily small neighborhood of this critical set, then integrate by parts with $\nabla f/|\nabla f|^2$ on the remaining compact support. The deleted part is bounded by its volume and the amplitude bound.

The analytic zero-set fact used here has the exact hypotheses of Proposition 0 in Boris Mityagin, [The zero set of a real analytic function, arXiv:1512.07276v1](https://arxiv.org/html/1512.07276v1). I opened and checked that primary source. The audited file also provides the elementary local power-series and Fubini proof, so this is a verified corroboration, not an unverified external hypothesis.

For $|k|>2\sup|\nabla\mathcal P|+2$, the gradient of the aliased phase has norm at least $|k|/2$. In the integration-by-parts operator, its vector coefficient and every required derivative are $O_M(|k|^{-1})$; higher phase derivatives are fixed and bounded on the support. Repetition gives
$$
 \left|\int\mathcal A_\delta e^{2\pi iN(\mathcal P-k\cdot z)}\right|
 \le C_{M,\delta}N^{-M}(1+|k|)^{-M}.
$$
Choosing $M>4$ makes the entire distant-alias tail summable. Only finitely many nearby aliases remain, and each has already been shown to decay. Sending $N$ to infinity before $\delta$ to zero proves the lemma.

There is no lower bound on a particular nonzero gradient, no exclusion of degenerate stationary points, no restriction to a subsequence, and no small-gradient assumption. Analyticity and the fixed-phase quantifier are sufficient. The number and constants of the nearby aliases can grow with $R$; the application requires them only for each fixed $R$.

## 8. Finite-grid WKB and the exact powers of N

The finite Fourier symbols $H_j$, phases, and amplitudes are fixed independently of $N$ once $R$ is fixed. Their derivative bounds may be extremely large, but they are finite. For $h=(2\pi N)^{-1}$, the exact shift length for a label $l$ is $2\pi lh$. Taylor expansion gives
$$
 Q_N(H)(Be^{i\Phi/h})
 =e^{i\Phi/h}
 \left[
 H(q,\Phi_q)B
 -ih\left(H_pB_q+
 \tfrac12(H_{pq}+H_{pp}\Phi_{qq})B\right)
 +O_R(h^2)
 \right].
$$
For a single Fourier label, the first correction is
$$
 h\widehat H(k,l)e^{2\pi i(kq+l\Phi_q)}
 \left(2\pi l B_q+2\pi^2iklB+2\pi^2il^2\Phi_{qq}B\right),
$$
which confirms all signs and factors of $2\pi$.

The evolution equation is $\partial_v\psi=iQ(H)\psi/(2\pi h)$. The Hamilton-Jacobi and transport equations cancel the first two terms. Along a characteristic,
$$
 \dot J=-\frac{H_{pq}+H_{pp}\Phi_{qq}}{2\pi}J,
 \qquad
 \frac{dB}{dv}=\frac{H_{pq}+H_{pp}\Phi_{qq}}{4\pi}B.
$$
Thus $B=J^{-1/2}$, with the same initial normalization used in the source. At stage boundaries the phases and amplitudes match, and the Jacobians multiply by the chain rule.

Individual branches need not be periodic at the finite grid boundary. The complete sum is periodic exactly. The two potentially nontrivial deck-phase increments, after multiplication by $N$, are
$$
 -cy-cNm+acN/2,\qquad
 x-ay-aNm-abN/2.
$$
They are integers for integer $x,y,m$, because $ab,ac$ are even. Reindexing the $b$ branches therefore makes a wrapped finite shift identical to the unwrapped branch extension used in the Taylor expansion. This handles composite odd $N$ as well as prime $N$.

Each residual entry is $O_R(h/\sqrt N)$. A column has $N$ entries, so its residual norm is $O_R(h)$. The initial matrix is the exact Gaussian image sum. Unitary Duhamel evolution through the fixed number of stages gives
$$
 \|(U_N^R-V_{R,N})e_y\|_2=O_R(N^{-1})
 \quad\text{uniformly in }y,
 \qquad
 \|U_N^R-V_{R,N}\|_{\rm HS}=O_R(N^{-1/2}).
$$
The amplitude bounds give $\max|V_{R,N}|\le\sqrt b(1-\epsilon)^{-R/2}N^{-1/2}$. The column error bounds every entry error by $O_R(N^{-1})$, proving the stated entry bound with factor two eventually.

Finally,
$$
 \big\||U_N^R|^{\circ2}-|V_{R,N}|^{\circ2}\big\|_{\rm HS}
 \le(\max|U_N^R|+\max|V_{R,N}|)
       \|U_N^R-V_{R,N}\|_{\rm HS}
 =O_R(N^{-1}).
$$
There is no lost factor of $N$ in this passage.

## 9. The limiting kernel, its marginals, and return normalization

The equal-sheet terms give exactly
$$
 k_R(q,s)=b^{-1}\sum_{m=0}^{b-1}B_m(q,s)^2.
$$
The amplitude deck laws permute this sum under unit changes in either endpoint. It is positive analytic on the ordinary endpoint torus and has the claimed upper and lower bounds.

Each unequal-sheet term has smooth amplitude $B_mB_n/b$ and analytic phase $\Phi_m-\Phi_n$. Section 6 supplies precisely the nonzero mixed derivative required in Section 7. There are $b(b-1)$ terms, a finite number for fixed $R$. Their operator norms tend to zero, and the probability error above also tends to zero.

For the marginals, let $r(q,s)$ invert $Q_R(s,r)$ and let $K=\partial_qr$. Then $B_m^2/b=K(q,s+m)$. The deck law gives
$$
 K(q,s+m)=K(q-am,s),\qquad K(q+b,s)=K(q,s).
$$
Multiplication by $a$ permutes the residues modulo $b$, hence
$$
 k_R(q,s)=\sum_{j=0}^{b-1}K(q+j,s).
$$
Integrating over one period in $q$ gives $r(b,s)-r(0,s)=1$. The same expression is the conditional output-position density for uniform input momentum; area preservation of $F_+^R$ gives the other marginal after integration in $s$.

There is also a purely finite-dimensional cross-check. Unitarity makes $|U_N^R|^{\circ2}$ bistochastic. Apply the proved operator approximation to the normalized constant vector on either side, then use ordinary Riemann sums for the fixed continuous kernel. The squared norm converges to the integral of the squared marginal error, which must vanish. Continuity then gives both marginal identities pointwise.

The entrywise bound on $k_R-1$ is
$$
 |k_R-1|\le(1-\epsilon)^{-R}-1.
$$
The lower deviation is dominated by the upper one because
$(1-\epsilon)^{-R}+(1+\epsilon)^{-R}\ge2$.
The elementary row-column norm bound proves the operator-distance conclusion.

For completeness, the return corollary does not need a dark-space assumption. Write
$$
 W=U\otimes\overline U=
 \begin{pmatrix}P&B\\C&S\end{pmatrix},
 \qquad F_1=P,\quad F_r=BS^{r-2}C.
$$
Unitarity yields
$$
 \sum_{r=1}^{m+1}F_r^*F_r=I-C^*S^{*m}S^mC.
$$
If $a_m=\|S^m\|_{\rm HS}^2$, then $a_m$ is decreasing and bounded below, while $CC^*=I-SS^*$ gives
$$
 \|S^mC\|_{\rm HS}^2=a_m-a_{m+1}\longrightarrow0.
$$
Taking traces proves $\sum_{r\ge1}\|F_r\|_{\rm HS}^2=N$ for every finite unitary, regardless of inaccessible unit-modulus modes in $S$.

With $R_j=|U^j|^{\circ2}$, the renewal identity is
$$
 R_n=\sum_{r=1}^nF_rR_{n-r}.
$$
The normalized diagonal-pair constant vector is fixed by both $W$ and $W^*$. Thus $F_r$ annihilates constants on both sides for $r\ge2$, while $F_1$ is bistochastic. Writing $E_j=R_j-J_N$, rearrangement gives
$$
 F_r=E_r-\sum_{j=1}^{r-1}F_jE_{r-j},
 \qquad
 \|F_r\|_{\rm HS}\le\sum_{j=1}^r\|E_j\|_{\rm HS},
$$
since every $F_j$ is a contraction. The fixed-power entry bounds give
$$
 \|E_j\|_{\rm HS}^2
 =\sum_{x,y}|U_N^j(x,y)|^4-1\le C_j^2-1.
$$
For every fixed cutoff $L$, the total return mass up to $L$ is therefore bounded by a finite constant independent of $N$. Subtracting it from the exact total $N$ proves the corollary.

## 10. Stress checks, limitations, and source provenance

The following potential failure mechanisms were explicitly checked:

- Common divisors of $N$ and $b_R$: retained by the exact image formula and its Gaussian support calculation.
- Uncontrolled caustics at an intermediate exponential: excluded by the exact partial-stage positive Jacobian, not merely the endpoint map.
- Using the uncorrected classical symbol: excluded by rebuilding the original Fourier prescription and checking the two marked coefficients.
- Treating the fixed tiny $\tau$ as a limit: absent; the discounted error is evaluated at the exact rational parameter.
- Confusing separability with equality of sheet corrections: absent; the two separate averaging steps are both necessary and both valid.
- Losing irrational translations in a finite-order argument: absent; the bounded lifted remainder handles arbitrary real translations.
- Discarding nonzero or large sampled aliases: absent; all aliases occur in the exact Poisson formula, with a summable distant tail.
- Replacing grid asymptotics by a continuum oscillatory integral without justification: absent; the cutoff and Poisson steps prove the sampled statement.
- Promoting fixed-R constants to a growing-R conclusion: absent; the proof explicitly permits deterioration in every oscillatory and WKB constant.

The limit at $\tau=0$ would have separable sheet differences and literal translation intertwiners. The proof does not cover that different parameter. For the specified nonzero $\tau$, the nonvanishing Fourier coefficients supply the exact obstruction. The resulting oscillation may require an extremely large $N$; this affects no stated quantifier.

The theorem does not prove uniform bounds for $R(N)$, any estimate at times proportional to $N$, or the original signed trace-pair limit. The fact that normalized first-return mass escapes every fixed cutoff is consistent with those unresolved questions.

The fresh exact checker r7_audit_all_fixed_powers_checks.py passed **353,499 assertions**. Its SHA-256 is
e03e90c4ff8291279eee4671fd89cba9103399fef3bf4b56e4aea0f69a03f0d9.
It uses only integer and rational arithmetic. It checks the rebuilt symbol, full-grid modular covariance for odd dimensions through 41, integer and period-lattice identities through $R=256$, all partial-stage noncommutative words through $R=96$, image and boundary identities, fixed-parameter constants, and rectangular-cycle algebra. The companion check record states the exact finite ranges and limitations. These calculations verify algebraic obligations; the analytic argument above proves the asymptotic assertions.

| Source inspected | Scope | SHA-256 |
| --- | --- | --- |
| research_round7_2026_10_21/r7_return_all_fixed_powers_phase_separation.md | Complete new proof and both appendices | 46982efaa581d322d4e82d5f5782ccf69f979a5a59adfb863dd40ef292205527 |
| research_round6_2026_10_21/round6_main_report.md | Original definitions and conventions, especially §1 | 473b7b5b700a8ff17801eb9ca422c5949be15d0551c252e0b4035997db54b2bf |
| research_round2_2026_10_20/arithmetic_iterated_sector_covariance.md | Raw symbol and complete discounted-coordinate/no-translation proof, §§2–6 | c8e02b81819350ab52e7bc3dd791ffbeb1ae1a2192a9a99f1168c4c56d7123e2 |
| research_round5_2026_10_21/root_oscillatory_matrix_cancellation.md | Earlier sampled lemma, for exact comparison with the new unrestricted version | ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d |
| research_round6_2026_10_21/r6_original_fixed_powers_49.md | Earlier raw physical-power proof, already reconstructed during this independent audit assignment | 3f51c6d7de5b559c28271c72ae62c2f2d331f9c606b24a84cdab80751339d019 |
| research_round6_2026_10_21/r6_original_twostep_physical_mixing.md | Exact metaplectic, branch, and finite-shift formulas | 7d502a881f133743cd3d28afd6ac373351fd4a12f23e8292c59895358f1e747b |
| Spectral_research_master.md | Frozen base identification only; no verdict used as evidence | 3534e4d7aa97c2f8621050248652363c639aeedf723f8b7fe7a971dc01ac2302 |

The initial new-proof revision had SHA-256 ac8b97752b4e3e89cc11417069e66a0ae92b0de8c57b65f9b1d1e3c29fe0c536. During this audit, five carriage-return control bytes before the letter “m” in TeX expressions were restored to literal backslash-r-m commands, producing the final hash above. Reversing only those five repairs reproduces the initial hash exactly. No mathematical content changed.

**Required mathematical corrections: none.** The presentation-only control-byte corrections were applied before the final source was pinned.
