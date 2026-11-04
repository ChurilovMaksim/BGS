# The aggregate Lin sum at the three included crossings

Tags in this file are local to the note. **[P]** is proved here, or is an external theorem with the locator named in the sentence. **[CA]** is a finite enclosure in ball arithmetic. **[N]** is a floating-point observation. A finite enclosure is not an asymptotic bound, and it is not an enclosure of a sum that was not computed. `record/claims.json` was not edited.

The question is whether
\[
\mathrm{Lin}_d(\rho)=\frac{2}{d^2}\operatorname{Re}\Bigl(\overline{Z_\rho}\sum_{\beta\not\equiv 0}\kappa_d(N\beta)\,\hat Z(\beta)\Bigr)
\]
satisfies \(|\mathrm{Lin}_d|\le\varepsilon_d|Z_\rho|^2/h_p\) at the three included conductors of `proofs/h7_multidisc.md`, for an \(\varepsilon_d\) small enough to sit in the H7* budget \(\sum\varepsilon_d\le\kappa_0\). It does not get decided. The sum over \(\beta\) was not enclosed. The pieces that were enclosed are one \(\lambda\)-orbit at each conductor, and, at the prime \(457\), the isotropic orbits. Each one-orbit piece is negligible next to \(|Z|^2/h_p\). Negligible pieces do not bound the sum.

The scoping sentence is `proofs/h7_scope.md`.

## 1. Weights [P]

Let \(u_0=1\), \(u_1=7\), \(u_{n+1}=6u_n-u_{n-1}\), \(h_p=u_{(p-1)/2}\), \(K_p=4h_p^2+3\), \(h_m=h_p K_p\) at \(m=3p\). The three conductors, their factorisations, and the tests \(d\mid K_p\), \(d^2\le h_m\) are the integer statements in `proofs/h7_multidisc.md` §2. Each prime factor below is \(1\bmod 8\), hence \(\bigl(\frac{2}{q}\bigr)=1\), and each divides \(h_m\) to the first power only. Trial division in `h7_lin_cert.py` rechecked primality.

The member labels at an exact level \(d\mid h_m\) are \(t=jy'\bmod d\), where \(j\in(\mathbb Z/d\mathbb Z)^\times\) and \(\nu=\nu_0+(2h_m/d)j\) is coprime to \(2h_m\). Here \(\nu_0\equiv\pm 4^{-1}\pmod{h_m}\) is the odd representative, so \(\nu_0\) is a unit modulo \(h_m\), and \(y'\) is a unit modulo \(h_m\) because \(h_m^2+1=2y'^2\). Write \(\kappa_d(u)=\sum_{t\in S_d}e(\bar t\, u/d)\).

**Lemma 1.** Let \(d=\prod q\) be a product of distinct primes \(q\parallel h_m\). For each such \(q\) let \(t_b(q)\) be the missing label at the prime level, and set \(t_c(q)\equiv t_b(q)\cdot(d/q)\pmod q\). Then \(S_d\) is the Chinese-remainder product of the sets \(\mathbb F_q^\times\setminus\{t_c(q)\}\), and
\[
\kappa_d(u)=\prod_q\kappa_q^{(t_c(q))}\bigl(u\cdot(d/q)^{-1}\bmod q\bigr),
\]
where \(\kappa_q^{(t)}(0)=q-2\) and \(\kappa_q^{(t)}(v)=-1-e(\bar t\, v/q)\) for \(v\not\equiv 0\).

*Proof.* For a prime \(\ell\mid h_m\) with \(\ell\nmid d\), one has \(2h_m/d\equiv 0\pmod\ell\), so \(\nu\equiv\nu_0\not\equiv 0\pmod\ell\). The condition \(\gcd(\nu,2h_m)=1\) therefore cuts only at the primes \(q\mid d\). At such a \(q\), \(2h_m/d\) is a unit modulo \(q\): \(q\) divides \(h_m\) once, \(d/q\) is coprime to \(q\), and \(q\) is odd. Hence \(\nu\equiv 0\pmod q\) is one linear condition \(j\equiv j_c\pmod q\). The prime-level condition is \((2h_m/q)j_b\equiv-\nu_0\pmod q\), and \(2h_m/q=(2h_m/d)\cdot(d/q)\), so \(j_c\equiv j_b\cdot(d/q)\pmod q\). In particular \(j_c\not\equiv 0\). The allowed \(j\) are the Chinese-remainder product of \(\mathbb F_q\setminus\{0,j_c\}\). Multiplication by the unit \(y'\) preserves the product shape and sends \(j_c\) to \(t_c(q)\).

For the sum, Bézout gives \(1/d=\sum_q\bigl((d/q)^{-1}\bmod q\bigr)/q\) as rational numbers. If \(t\equiv t_q\pmod q\), then
\[
\frac{\bar t\, u}{d}\equiv\sum_q\frac{u\cdot(d/q)^{-1}\cdot t_q^{-1}}{q}\pmod 1.
\]
The character sum over a product set is the product of the local sums. The local sum over \(\mathbb F_q^\times\setminus\{t_c\}\) is the stated formula, because the complete sum over \(\mathbb F_q^\times\) equals \(-1\) off zero and \(q-1\) at zero. ∎

The same algebra is the prime-level formula of J3 §3 (BGS-TRACE-229) when \(d=q\). It does not use \(\bigl(\frac{2}{q}\bigr)=1\). That Legendre symbol is the hypothesis of Theorem K1 (BGS-TRACE-237), which evaluates a different sum and is not invoked here.

**Check [N].** At \(m=15\), \(d=7\cdot 41=287\), the member enumeration has \(195=(7-2)(41-2)\) labels. On \(42\) arguments the product formula and the direct sum differ by at most \(8.56\cdot 10^{-14}\) (`logs/h7_lin_kappa_check.json`, precision \(320\) on the product side, float64 on the direct sum).

**Corollary 2 [CA].** For the three crossing frequencies, \(N(\beta)\) is a unit at every prime factor, and ball arithmetic at precision \(320\) encloses \(\kappa_d(N\beta)\):

| \(d\) | \(\beta\) | \(N(\beta)\) | \(|\kappa|\) |
| --- | --- | --- | --- |
| \(3437426497\) | \((-208,0)\) | \(43264\) | \(0.20028229612862064\) |
| \(24061985479\) | \((227,227)\) | \(-51529\) | \(0.352776706753451\) |
| \(2735635252619983\) | \((-89,0)\) | \(7921\) | \(0.8773654889389776\) |

Each modulus ball has width below \(10^{-12}\) after the float conversion of an endpoint; the two printed endpoints in `logs/h7_lin_traces.json` agree to the digits shown. These are smaller than the trivial cap \(2^{\omega(d)}\).

## 2. What the conductor decomposition does not remove [P]

J3-F5, recorded as BGS-TRACE-228, says that for coprime odd \(c,e\) with \(ce\mid h_m\) and \(\beta=e\beta'\),
\[
\hat Z^{(d)}_{e\beta'}=\hat Z^{(c)}_{\beta'},\qquad W_{d,e\beta'}=\frac{n_e}{e^2}W_{c,\beta'},
\]
with \(n_q=q-2\) when \(q\parallel h_m\). The phase identity \(\operatorname{Tr}(e\beta'\,\lambda^j)/d=\operatorname{Tr}(\beta'\,\lambda^j)/c\) is the definition of the twist. It holds for the finite-section monodromy of Section 4 for the same reason: the section letter depends on \(\beta\) only through that phase. So the splitting
\[
\mathrm{Lin}_d=\sum_{c\mid d}\frac{n_e}{e^2}\Lambda_c,\qquad
\Lambda_c=\frac{2}{c^2}\operatorname{Re}\Bigl(\overline{Z}\sum_{\beta\text{ exact conductor }c}\kappa_c(N\beta)\,\hat Z(\beta)\Bigr),
\]
is an identity of the section traces as well as of the untruncated traces. This is the bookkeeping in N7b §1, cited, with the section phase check added here.

At \(d=457\cdot 7521721\) the divisors are \(1\), \(457\), \(7521721\) and \(d\). The term of exact conductor \(d\) has coefficient \(n_1/1^2=1\). The term of conductor \(457\) is carried with coefficient
\[
\frac{7521721-2}{7521721^2}=\frac{7521719}{56576286801841}<1.33\cdot 10^{-7}.
\]
An enclosure of every orbit at the prime \(457\) would control that \(10^{-7}\) piece and would not control \(\mathrm{Lin}_d\). The same arithmetic at the other two conductors leaves a coefficient-\(1\) primitive term. The primitive term is the aggregate this note does not enclose.

## 3. Why the sum was not enclosed

On \((\mathbb Z/d\mathbb Z)^2\) the map \(\beta\mapsto\lambda\beta\) has order \(P\), with \(P=57\) at the first two conductors and \(P=87\) at the third (`h7_lin_cert.py` returns that order before the product). A unit \(\beta\), meaning \(N(\beta)\) coprime to \(d\), has orbit length \(P\): \(\lambda^k\beta=\beta\) implies \(\lambda^k=1\) after multiplying by the inverse \(\bar\beta/N(\beta)\). The number of residue classes is \(d^2\). At \(d=3437426497\), \(d^2=11815900922277691009\). Since \(d^2\equiv 1\pmod{57}\), \((d^2-1)/57=207296507408380544\). That is the number of length-\(57\) orbits there would be if every nonzero class had orbit length \(57\). Classes fixed by a proper power of \(\lambda\) make the orbit count larger, not smaller. Either way the count is about \(2\cdot 10^{17}\). Each orbit is one \(280\times 280\) product of length \(57\) in the section of Section 4. They were not enumerated.

The Gauss form of the same sum is a propagation on the dual grid \((\mathbb Z/d\mathbb Z)^2\), with the same cardinality, contracted against the kernel of Lemma 1. At the prime \(q=457\) the grid has \(457^2=208849\) fibres and the section has dimension \(280\). One fibre-vector is a complex array of about \(0.94\cdot 10^9\) bytes. A full trace is \(280\) such vectors. Column-sequential timing of one \((457^2,40)\times(40,40)\) product was about \(0.06\) s, and a step applies about \(7\times 33\) such products, so one vector of length \(57\) is about a quarter of an hour and the trace is about sixty hours. That run was not started. A four-probe Hutchinson estimator would be a float average, not an enclosure; it was not used.

A Frobenius bound does not replace the sum. The blocks of one untwisted step satisfy \(\|L\|_F\le 50.490459330663754\) for every unimodular letter phase, because the Frobenius norm of a sum is at most the sum of the Frobenius norms (`logs/h7_lin_traces.json`, precision \(320\)). Then \(\|Q\|_F\le M^P\) with this \(M\). At \(P=57\), \(M^P\) is larger than \(10^{90}\). Multiplied by \(d^2\) it sits many orders above the threshold of Section 5. The bound is true and does not decide \(\varepsilon_d\).

The same obstruction, with a larger grid, applies at \(d=24061985479\) and at \(d=2735635252619983\). No aggregate enclosure is claimed at either conductor.

## 4. The finite-section traces that were enclosed [CA]

The section is the one in `proofs/h7_multidisc.md` §3: centres \(|c|\le 3\), \(40\) modes, letters \(|n|\le 16\), dimension \(280\), disc radius \(1.2\), precision \(320\). The core is forward-invariant on this alphabet (the builder reports no exit). Sectors \(a\in\{2,6\}\) cancel in the \(\pm\rho\) sum by BGS-TRACE-221, cited and not re-proved. Sectors \(a=0\) and \(a=4\) are the ones that survive. The edge operator is not in this section.

The twist of \(\lambda\beta\) is the cyclic shift of the twist of \(\beta\), because \(\operatorname{Tr}(\lambda\beta\,\lambda^j)=\operatorname{Tr}(\beta\lambda^{j+1})\) and \(\lambda^P\equiv 1\pmod d\). The trace of a product is invariant under a cyclic permutation of the factors. \(N(\lambda\beta)=N(\beta)\), so \(\kappa\) is constant on the orbit. An orbit of length \(P\) therefore contributes \(P\cdot\kappa_d(N\beta)\cdot\operatorname{Tr}(Q_{\beta,a})\) to the sector-\(a\) section sum
\[
S_a=\sum_{\beta\not\equiv 0}\kappa_d(N\beta)\,\operatorname{Tr}(Q_{\beta,a}).
\]
This \(S_a\) is not \(\sum\kappa\hat Z\). The trace formula of Line J is
\[
\hat Z_\rho(\beta)=c_m\sum_a c_a\cdot\frac13\bigl(\operatorname{Tr} V_{\beta,a}^m-\operatorname{Tr} E_{\beta,a}^m\bigr),
\]
with \(c_m=1-\lambda^{-m}\) and \(|c_a|=1/2\). The section trace encloses \(\operatorname{Tr} V\) of the truncated vertex, not \(\operatorname{Tr} V-\operatorname{Tr} E\), and not the untruncated operator. The coefficient of one sector is at most \(1/6\) in modulus.

Each product was scaled by an exact power of two and the trace was multiplied back by that power. The flint real and imaginary strings in `logs/h7_lin_traces.json` are the enclosure. A float endpoint below is the converted ball; every comparison has more than three correct leading digits of room.

### 4.1. Untwisted section, \(\beta=0\)

| period | sector | \(|\operatorname{Tr}|\) |
| --- | --- | --- |
| \(57\) | \(0\) | \(1.2295228772115986\cdot 10^{16}\) |
| \(57\) | \(4\) | \(1.8544532173567326\cdot 10^{-14}\) |
| \(87\) | \(0\) | \(3.614257095031031\cdot 10^{24}\) |
| \(87\) | \(4\) | \(1.0989073615162788\cdot 10^{-21}\) |

Sector \(4\) is smaller than sector \(0\) by more than \(10^{29}\). In this section the untwisted mass sits in sector \(0\).

### 4.2. The three crossing orbits

| \(d\) | sector | \(|\operatorname{Tr}|\) |
| --- | --- | --- |
| \(3437426497\) | \(0\) | \(2224799020.4343753\) |
| \(3437426497\) | \(4\) | \(2.737488085506396\cdot 10^{-13}\) |
| \(24061985479\) | \(0\) | \(17144879331.749458\) |
| \(24061985479\) | \(4\) | \(5.692851229494173\cdot 10^{-13}\) |
| \(2735635252619983\) | \(0\) | \(333273628480233.94\) |
| \(2735635252619983\) | \(4\) | \(1.5655338498675646\cdot 10^{-19}\) |

Every one of these balls has relative accuracy above \(100\) bits, and the two float endpoints of the modulus agree to the digits printed. Sector \(4\) is again negligible next to sector \(0\). The orbit contribution to the sector-\(0\) section sum is \(P\kappa\operatorname{Tr}\):

| \(d\) | \(\lvert P\kappa\operatorname{Tr}\rvert\) |
| --- | --- |
| \(3437426497\) | \(2.5398507805526253\cdot 10^{10}\) |
| \(24061985479\) | \(3.447539018953732\cdot 10^{11}\) |
| \(2735635252619983\) | \(2.5439041860176404\cdot 10^{16}\) |

### 4.3. Isotropic orbits at \(q=457\) [CA]

There are two isotropic lines, \(w\equiv 80\pmod{457}\) a square root of \(2\). On each, \(\lambda\) acts by multiplication by a unit of order \(57\), and the nonzero points split into \(8\) orbits of length \(57\). On every nonzero isotropic frequency, \(\kappa_q=q-2=455\). The \(16\) representatives were enclosed in sectors \(0\) and \(4\) (`logs/h7_lin_iso_s0.json`, `logs/h7_lin_iso_s4.json`). Summing the trace balls and multiplying by \(455\cdot 57\) gives the complete isotropic part of the section sum (`logs/h7_lin_iso_sum.json`):

| sector | \(\lvert S_{\mathrm{iso}}\rvert\) |
| --- | --- |
| \(0\) | \(7.8450076177326356\) |
| \(4\) | \(39.619988072063016\) |

Both modulus balls have width below \(10^{-4}\) before these digits; the float endpoints agree. This is not \(\mathrm{Lin}_{457}\): the off-isotropic frequencies, where \(|\kappa|\le 2\), were not enclosed. By Section 2 the carry of this piece into \(\mathrm{Lin}_d\) at \(d=457\cdot 7521721\) has the extra factor \(<1.33\cdot 10^{-7}\).

## 5. Comparison with \(\varepsilon_d|Z|^2/h_p\)

Write \(\eta(S)=| \tfrac{2}{d^2}\overline{Z} S |\, h_p/|Z|^2\), so that the closure inequality at this single level is \(\eta\le\varepsilon_d\) for some budget with room for every other level. Two denominators are used, and they are not interchangeable.

- **Section ratio.** Take \(Z\) and \(\hat Z\) to be section traces in one sector, so the sector coefficient cancels. Then
  \[
  \eta_a\le \frac{2 h_p}{d^2}\cdot\frac{|P\kappa\operatorname{Tr}(Q_{\beta,a})|}{|\operatorname{Tr}(Q_{0,a})|}
  \]
  is an upper bound on the share of this one orbit. It is a statement about the section.
- **Scale of the true \(Z\).** BGS-TRACE-273 gives \(|Z_\rho|\ge z_{\mathrm{lo}}=\tfrac12(1-\lambda^{-m})(\mu_{\mathrm{lo}}^m-3012.4)\) with \(\mu_{\mathrm{lo}}=1.9154712\). The constant \(3012.4\) is cited. Using \(z_{\mathrm{lo}}\) in the denominator and a section trace in the numerator is a mixed comparison. It upper-bounds the orbit's contribution to the true \(\eta\) only if the section trace upper-bounds the true \(|\hat Z|\). Section 5 of `proofs/h7_multidisc.md` records that this transfer was not proved. The mixed number is reported as a scale, not as a value of \(\varepsilon_d\).

The threshold at which a sum \(S\) can force \(\eta\ge 1\), granted \(|Z|\ge z_{\mathrm{lo}}\) and \(|\mathrm{Lin}|\le(2/d^2)|Z|\,|S|\), is \(|S|\ge z_{\mathrm{lo}}\, d^2/(2h_p)\). The certificate's lower endpoints of that threshold are \(3.876\cdot 10^{27}\), \(1.899\cdot 10^{29}\) and \(1.073\cdot 10^{44}\). A one-orbit \(|P\kappa\operatorname{Tr}|\) many orders smaller than that threshold does not put the full sum under the threshold: Section 3 counts the residue classes, and no uniform upper bound better than the Frobenius majorant was proved.

Using the sector-\(0\) section trace at \(\beta=0\) as the denominator, the one-orbit shares are
\[
\eta_0<3.28\cdot 10^{-18},\qquad
\eta_0<9.08\cdot 10^{-19},\qquad
\eta_0<1.19\cdot 10^{-28}
\]
at the three conductors in the order of Section 4.2. Replacing the denominator by \(z_{\mathrm{lo}}\) instead of the section trace multiplies these by less than \(2.1\). Inflating each numerator by a relative \(10^{-12}\) does not change the inequalities. The sector-\(4\) traces are too small to move any of them. These are shares of one orbit. They are not \(\varepsilon_d\).

At the prime \(q=457\), against the same period-\(57\) sector-\(0\) untwisted trace, the isotropic pieces satisfy
\[
\eta(S_{\mathrm{iso},0})<5.73\cdot 10^{-14},\qquad
\eta(S_{\mathrm{iso},4})<2.90\cdot 10^{-13}.
\]
Their sum is \(<3.47\cdot 10^{-13}\). Carried into \(d=457\cdot 7521721\) by the factor of Section 2, the same pieces contribute less than \(4.61\cdot 10^{-20}\) to \(\eta\). Replacing the section trace by \(z_{\mathrm{lo}}\) multiplies these by less than \(2.1\). This is the isotropic part only. The off-isotropic sum at \(q=457\), and the exact-conductor sum at each composite, stay unenclosed.

**Decision.** At each of the three conductors, the aggregate closure condition of H7* is not shown to hold and not shown to fail. The sufficient per-orbit reading is already false for the finite section, by `proofs/h7_scope.md`. Theorem v5 does not apply H7* at \(p=19\) or \(p=29\), both of which are \(<1409\).

## 6. Tags

- **[P]** Lemma 1, the conductor splitting for section traces, the orbit-length count, and the cyclicity of the section trace.
- **[CA]** The three values of \(\kappa\), the section traces named in the logs, the isotropic sums \(|S_{\mathrm{iso}}|<7.846\) and \(<39.620\), and the Frobenius step bound \(50.490459330663754\).
- **[N]** The member-sum check at \(d=287\). The grid-versus-\(\beta\) check of the Gauss kernel at \(q=41\), \(m=15\), truncation \(K=20\), absolute error \(1.33\cdot 10^{-10}\) (`logs/h7_lin_validate.json`). That check tests the propagator used to debug the kernel. It is not an enclosure at \(q=457\) or at the composite conductors, and those propagations were not run as certificates.
- **Not claimed.** An enclosure of \(\sum_\beta\kappa\hat Z\) at any of the three conductors. A value of \(\varepsilon_d\). A sign for \(\mathrm{Lin}_d\). A bound on the edge, or a transfer of the one-step tail to the untruncated monodromy. A discharge or a refutation of H7*, H8, H1, H3, or frozen R′.
