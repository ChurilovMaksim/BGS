# Wave 41, task 3 — Reversal exclusion for general p: PROVED

**Theorem.** Let $y$ be a kernel sequence mod $Q=2^{2j+3}$ ($j\ge3$),
minimal period $p=2^k$ ($k\ge3$), with $\nu=(1,1)$. Then
$E_{\mathrm{alt}}(y):=8A_y/Q\in\{0,\pm2,\pm4,\pm6\}$, where
$A_y=\sum_{i<p}(-1)^i y_i$ (canonical reps). In particular
$|E_{\mathrm{alt}}|\le6<8\le p$.

**Consequence (reversal exclusion, unconditional).** Wave 38 §(a):
a reversal of the odd-flip partner of a $\nu=(1,1)$ point would force
$E_{\mathrm{alt}}=p$. The theorem rules this out for every $p\ge8$,
so the odd-flip partner always lies in a new orbit: $\nu=(1,1)\implies$
split holds **unconditionally**, and wave 38 (a)'s "modulo reversal"
caveat is removed. For split points the bound reads: $|E_{\mathrm{alt}}|
\le6$ unconditionally at $m=32$ (Gap G proved there, wave 40, so Split
Bit is unconditional), and in general modulo Gap G; verified exactly
at $m=32,64,128$ (§3).

## 1. Reduction to a fixed modulus (Lemma R)

$M^n=\bigl(\begin{smallmatrix}U_{n+1}&-U_n\\U_n&-U_{n-1}
\end{smallmatrix}\bigr)$ with $U_n=(\alpha^n-\alpha^{-n})/(4\sqrt2)$,
$\alpha=3+2\sqrt2$. Valuation lemma (in $\mathbf Z[\sqrt2]$):
$v_2(U_n)=v_2(n)$ (LTE: $\alpha^n-\alpha^{-n}=(\alpha^{n/2}-\alpha^{-n/2})
(\alpha^{n/2}+\alpha^{-n/2})$, second factor $=2V_{n/2}$ with $V$ odd);
$v_2(U_{p+1}-1)=k$ for $p=2^k$ (from $U_{p+1}-1=\varepsilon(6+\alpha
\varepsilon)/((1+\varepsilon)4\sqrt2)$, $\varepsilon=\alpha^p-1$,
$v_{\sqrt2}(\varepsilon)=2k+3$, giving $v_{\sqrt2}=2k$); likewise
$v_2(U_{p-1}+1)=k$. Hence $v_2(\gcd$ of entries of $M^p-I)=k$ and
$v_2(\det(M^p-I))=2k+3$ (det $=-(T_k-2)$, $T_k-2=32U_{2^{k-1}}^2$).

So $M^p-I=2^kH_p$ with $\det H_p=\pm2^3\cdot$odd. The kernel condition
$(M^p-I)s\equiv0\pmod{2^{2j+3}}$ then gives, multiplying by
$\mathrm{adj}(H_p)$, $s\equiv0\pmod{2^{2j-k}}$. Thus every
minimal-period-$p$ point is $y=2^{2j-k}z$ with $z$ a kernel sequence
mod $2^{k+3}$ of the same minimal period and $\nu$, and
$E_{\mathrm{alt}}(y)=A_z/2^k$. The theorem reduces to Theorem T below.

## 2. Induction on $k$ (Theorem T)

**T:** $z$ mod $2^{k+3}$, minimal period $2^k$, $\nu=(1,1)$
$\implies A_z/2^k\in\{0,\pm2,\pm4,\pm6\}$.

*Base $k=3$.* Wave 39 §3 classifies the 384 minimal-period-8 reduced
sequences: the split ones are exactly the all-even ones, with
$E_{\mathrm{alt}}\in\{0,\pm2,\pm4,\pm6\}$ (§3(b)); the $\nu=(1,1)$
ones are exactly these 128, since split $\implies\nu=(1,1)$
(Split Bit, unconditional at $m=32$ by wave-40 Gap G) and both sets
have 128 elements (census).

*Step $k\ge4$.* Let $z'=z\bmod 2^{k+2}$.
(i) $z'$ is a kernel sequence mod $2^{k+2}$.
(ii) $z'$ has minimal period exactly $2^{k-1}$: it divides $2^{k-1}$
because the half-defect of $z$ is exactly half the modulus
($z_{i+2^{k-1}}=z_i\pm2^{k+2}$ canonically); it does not divide
$2^{k-2}$, because the quarter-defect is $z_{i+2^{k-2}}\equiv
z_i+2^{k+1}\pmod{2^{k+2}}$ (Lemma 2's proof, valid since $4\mid2^{k-2}$),
nonzero mod $2^{k+2}$.
(iii) $\nu'(z')=(1,1)$: the half-defect of $z'$ is the quarter-defect
of $z$, i.e. $2^{k+1}$ = half of $2^{k+2}$, for both parities
($\nu=(1,1)$ is swap-invariant).
(iv) $A(z)=2A(z')$: write $z_i=z'_i+2^{k+2}t_i$, $t_i\in\{0,1\}$.
Then $A(z)=\sum_{i<2^k}(-1)^iz'_i+2^{k+2}T$ with
$T=\sum(-1)^it_i$. The first sum is $2A(z')$ ($2^{k-1}$ even, and
$z'$ has period $2^{k-1}$). And $T=0$: the canonical half-defect
gives $t_{i+2^{k-1}}=1-t_i$, so the two halves of $T$ cancel
($2^{k-1}$ even $\implies\sum_{i<2^{k-1}}(-1)^i=0$).
Hence $A(z)/2^k=A(z')/2^{k-1}$.
(v) By the induction hypothesis, $A(z')/2^{k-1}\in
\{0,\pm2,\pm4,\pm6\}$. ∎

## 3. Exact verification

- Censuses at $m=32,64,128$ (all kernel points, fibers, dihedral
  orbits): split $\iff\nu=(1,1)$ in all three; $E_{\mathrm{alt}}\in
  \{0,\pm2,\pm4,\pm6\}$ for every $\nu=(1,1)$ point (2,688 at $m=32$;
  10,880 at $m=64$; 43,648 at $m=128$), 0 violations. Nonsplit points
  reach $|E_{\mathrm{alt}}|=15,23,39,55,87$ by period — the bound is
  genuinely a $\nu=(1,1)$ phenomenon.
- Induction step verified on all 512 ($p=16$) and 2048 ($p=32$) points;
  valuations verified for $k=3,\dots,8$.

## Status

Reversal exclusion is **proved for all $p\ge8$** (for $\nu=(1,1)$
points, the operative hypothesis; for split points modulo Gap G).
$T_k=5(k-4)$ now rests on only two named statements: Gap G at
$m\ge64$ (Split Bit Lemma) and the U-lemma. No Lean, repo untouched.
Scripts: `wave41_reversal_census.py`, `wave41_reversal_nu.py`,
`wave41_reversal_explore.py`, `wave41_reversal_induction_check.py`.
