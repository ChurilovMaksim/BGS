# Wave 9, task 3 — Lemma Y gap P3′: CLOSED (3-adic digit induction, proved)

**Verdict: P3′ is closed.** Component Lemma Y mod $3^e$ (for $q=3^e\parallel D_m$,
$4\mid m$) is now proved, not merely verified. The proof is below in full.
It does **not** close global Lemma Y: P2 (2-primary) and Pmix (CRT mixing /
carries) remain open, exactly as isolated in wave 8. Repository untouched;
Lean not built; the computations in §8 are verifier artefacts, not part of
the proof.

## 0. What P3′ was, and what replaces it

Wave 8, task 1 proved the mod-3 base case by classification, proved the
odd-prime vanishing lemma ($Y_r\equiv 0\pmod q$ for $p\nmid 24$), refuted
the "Fix mod $q$ is cyclic" route (SNF is $\mathrm{diag}(d_1,d_2)$), and
verified component Lemma Y for all prime powers dividing $D_m$, $m\le 20$.
The remaining 3-adic gap, labelled P3′, was: *reduce component Lemma Y
mod $3^e$ to the mod-3 classification via SNF scaling plus a Hensel digit
argument; the step "multiset mod $3^e$ determines the top digit class-sum
up to $D_t$" was sketched, not written out.*

The completed argument has two steps, neither of which is "digit by digit
on the original exponent" in the naive sense:

1. **Scaling.** Every $\mathrm{Fix}_m\bmod 3^e$ vector is divisible by
   $3^{f_0}$, where $f_0 = 1+v_3(m/4)$ and $e = 2f_0$ (Lemma 4). Dividing
   by $3^{f_0}$ reduces the problem from exponent $e$ to exponent $f_0$.
2. **Top digit at exponent $f_0$.** For a $\mathrm{Fix}_m\bmod 3^{f_0}$
   vector, the class sum $Y'_r$ is divisible by $3^{f_0-1}$, and its top
   digit is exactly $Z'_r = n_0\cdot v_r \pmod 3$, where $v$ is the mod-3
   4-vector of the sequence and $n_0 = (m/4)/3^{f_0-1}\pmod 3$ is a unit
   (Lemma 5). The vector $v$ is determined by the mod-3 multiset up to
   $D_4$ by the 3-type classification (Lemma 6), which is the mod-3 base
   case with the factor $n=m/4$ divided out.

Step 1 is the SNF-balancing statement in disguise: $v_3(d_1)=v_3(d_2)=f_0$
for $M^m-I$. The proof below works directly with the
$\mathbb Z[\sqrt2]$-representation instead of invoking SNF invariance,
which is cleaner; §8 confirms the SNF statement computationally.

## 1. Setup

$H_m = 6I-C-C^T$, $(Hy)_i = 6y_i-y_{i-1}-y_{i+1}$ (indices mod $m$),
$D_m = \det H_m = s_m-2$, $s_n = \alpha^n+\beta^n$,
$\alpha = 3+2\sqrt2$, $\beta = 3-2\sqrt2$, $\alpha\beta = 1$,
$\alpha-\beta = 4\sqrt2$. A recurrence sequence is determined by
$(y_0,y_1)$ via $y_{i+1} = 6y_i-y_{i-1}$; it lies in $\mathrm{Fix}_m\bmod q$
iff it is $m$-periodic mod $q$. Throughout this note $4\mid m$ (otherwise
$3\nmid D_m$ and there is no 3-primary component at all: $s_m\bmod 3$ is
$0$ for $m$ odd and $1$ for $m\equiv 2\pmod 4$, so $D_m\equiv 1,2\pmod 3$;
see wave 8, §2). Write $m = 4n$, $n = m/4$, $t = \gcd(m,4) = 4$,
$O_r = \{i : i\equiv r\pmod 4\}$, $Y_r(y) = \sum_{i\in O_r} y_i$.

**Component Lemma Y mod $3^e$ (target).** Let $q = 3^e\parallel D_m$
($e = v_3(D_m)$). If $y,y'\in\mathrm{Fix}_m\bmod q$ have the same multiset
of entries mod $q$, then $Y(y')\in D_4\cdot Y(y)$ mod $q$, where $D_4$
acts by $r\mapsto r+b$ and $r\mapsto -r+b$ on the coordinates.

## 2. The ring $R = \mathbb Z[\sqrt2]$ at the prime $3$

**Lemma 1.** (a) $(3)$ is a maximal ideal of $R$ and $R/(3)$ is the field
$\mathbf F_9$: $R/(3) \cong \mathbf F_3[t]/(t^2-2)$, and $t^2-2$ is
irreducible over $\mathbf F_3$ (squares mod 3 are $0,1$; $2$ is not a
square). (b) For $x = a+b\sqrt2\in R$, $3\mid N(x) = a^2-2b^2$ implies
$3\mid a$ and $3\mid b$: indeed $a^2\equiv 2b^2\pmod 3$ forces $b\equiv 0$
(otherwise $a^2/b^2\equiv 2\pmod 3$, impossible), then $a\equiv 0$.
(c) Every $x\ne 0$ in $R$ writes uniquely as $x = 3^k x_0$ with
$x_0\notin (3)$ (divide the coefficients $a,b$ by $3$ repeatedly).
Define $v(x) = k$; then $v_3(N(x)) = 2k$, because
$N(x) = 9^k N(x_0)$ and $N(x_0)$ is not divisible by $3$ by (b).
In particular $v(xy) = v(x)+v(y)$, and $x\notin (3)$ iff $v(x)=0$ iff
$N(x)$ is prime to $3$.

*Proof.* (a) and (b) are the computations above. (c) follows from
$N(x_0)\not\equiv 0\pmod 3$: if $x_0\notin (3)$ then at least one of
$a,b$ is not divisible by $3$, and the argument of (b) run backwards
gives $3\nmid a^2-2b^2$. ∎

We use $v$ as "the 3-adic valuation in $R$". Note $v(3) = 1$, and
$v(x)\ge k$ means $3^k\mid x$ in $R$ (coefficient-wise).

**Lemma 2 (representation).** Let $q = 3^e$. Every recurrence sequence
$y_i\bmod q$ has a unique $A\in R/qR$ with
$y_i = A\alpha^i + \bar A\beta^i$ in $R/qR$ (bar = $\sqrt2\mapsto -\sqrt2$),
and $y$ is $m$-periodic mod $q$ iff $(\alpha^m-1)A = 0$ in $R/qR$.

*Proof.* Write $A = a+b\sqrt2$. Then $A+\bar A = 2a$ and
$A\alpha+\bar A\beta = 6a+8b$ (direct expansion: the $\sqrt2$ terms
cancel). Given $y_0,y_1\in\mathbb Z/q$, $2$ and $8$ are units mod $q$
($q$ a power of $3$), so $a = y_0/2$, $b = (y_1-6a)/8$ solve uniquely.
The sequence $\tilde y_i = A\alpha^i+\bar A\beta^i$ lies in $\mathbb Z/q$
(conjugate pair), satisfies the same recurrence (since $\alpha,\beta$
are roots of $t^2-6t+1$), and has the same $(y_0,y_1)$; by induction
(forward, and backward since the recurrence coefficient $-1$ is a unit)
$\tilde y_i = y_i$ for all $i$. Periodicity for all $i$ follows from
periodicity at $i=0,1$ by the same induction. In $A$-terms, $y_m = y_0$
and $y_{m+1} = y_1$ read as the linear system with unknowns
$U = (\alpha^m-1)A$, $V = (\beta^m-1)\bar A$ and matrix
$\begin{pmatrix}1&1\\ \alpha&\beta\end{pmatrix}$, whose determinant
$\beta-\alpha = -4\sqrt2$ has norm $-32$, prime to $3$, hence is a unit
mod $q$; so the system forces $U = V = 0$. ∎

## 3. The valuation of $\alpha^m-1$, and $e = 2f_0$

**Lemma 3.** Let $4\mid m$, $n = m/4$, $f_0 = 1+v_3(n)$. Then
$v(\alpha^m-1) = f_0$, and $v_3(D_m) = 2f_0$.

*Proof.* First, $v(\alpha^4-1) = 1$: $\alpha^4 = 577+408\sqrt2$, so
$\alpha^4-1 = 576+408\sqrt2 = 3\cdot(192+136\sqrt2)$, and
$N(192+136\sqrt2) = 192^2-2\cdot136^2 = -128$, not divisible by $3$,
so the second factor is not in $(3)$; by Lemma 1(c), $v = 1$.

Second, a cubing lemma: if $Z\in R$ with $v(Z-1) = t\ge 1$, then
$v(Z^3-1) = t+1$. Indeed write $Z = 1+\pi$, $v(\pi) = t$; then
$Z^3-1 = 3\pi + 3\pi^2 + \pi^3$, whose three terms have valuations
$1+t$, $1+2t$, $3t$; the minimum is $1+t$, uniquely, since $t\ge 1$
gives $1+t < 1+2t$ and $1+t < 3t$. (Valuation of a sum with a unique
minimum term equals that minimum, by Lemma 1(c) applied to the
coefficients: the lowest-valuation term dominates mod $3^{t+2}$.)

Apply this to $X = \alpha^4 = 1+3u$ ($u = 192+136\sqrt2$, $v(u)=0$).
Iterating the cubing lemma $s$ times, $v(X^{3^s}-1) = s+1$. Write
$n = 3^s n_0$ with $s = v_3(n) = f_0-1$ and $3\nmid n_0$. Let
$W = X^{3^s}$; then $v(W-1) = f_0$ and
$W^{n_0}-1 = (W-1)\sum_{k<n_0} W^k$, where the sum is $\equiv n_0\pmod{(3)}$
(each $W^k\equiv 1\pmod{(3)}$) and $n_0$ is a unit mod $3$, so the sum is
not in $(3)$; hence $v(W^{n_0}-1) = v(W-1) = f_0$. But $W^{n_0} = X^n =
\alpha^{4n} = \alpha^m$. So $v(\alpha^m-1) = f_0$.

Finally, $N(\alpha^m-1) = (\alpha^m-1)(\beta^m-1) = 2-(\alpha^m+\beta^m)
= -D_m$, so $v_3(D_m) = v_3(|N(\alpha^m-1)|) = 2v(\alpha^m-1) = 2f_0$
by Lemma 1(c). ∎

In particular $v_3(D_m) = 2+2v_3(m/4)$ for $4\mid m$ (checked
computationally for $4\mid m\le 100$ in §8), and the SNF statement
$v_3(d_1) = v_3(d_2) = f_0$ for $M^m-I$ is the matrix form of the same
fact: $M^m-I$ corresponds, under the cyclic-module isomorphism
$\mathbb Z^2\cong R$ sending $M$ to multiplication by $\alpha$, to
multiplication by $\alpha^m-1$, whose 3-primary invariant factors are
$3^{f_0},3^{f_0}$.

## 4. Scaling (Lemma 4)

Let $e = 2f_0$, $q = 3^e$.

**Lemma 4 (scaling).** Every $y\in\mathrm{Fix}_m\bmod q$ has all entries
divisible by $3^{f_0}$ in $\mathbb Z/q$. Writing $y_i = 3^{f_0}y^{(1)}_i$
with $y^{(1)}_i\in\mathbb Z/3^{f_0}$, the vector $y^{(1)}$ lies in
$\mathrm{Fix}_m\bmod 3^{f_0}$, and $y\mapsto y^{(1)}$ is a bijection
between $\mathrm{Fix}_m\bmod q$ and $\mathrm{Fix}_m\bmod 3^{f_0}$ that
preserves multisets (division by $3^{f_0}$ is a bijection from the
multiples of $3^{f_0}$ in $\mathbb Z/q$ onto $\mathbb Z/3^{f_0}$).

*Proof.* Let $A\in R/qR$ represent $y$ (Lemma 2), with lift
$\tilde A\in R$. Periodicity says $(\alpha^m-1)\tilde A\equiv 0\pmod{3^e}$
in $R$, i.e. $3^e\mid (\alpha^m-1)\tilde A$ coefficient-wise. Write
$\alpha^m-1 = 3^{f_0}u$ with $u\notin (3)$ (Lemma 3). Then
$3^{e-f_0}\mid u\tilde A$ in $R$; taking norms, $N(u)$ is prime to $3$,
so $9^{e-f_0}\mid N(\tilde A)$ in $\mathbb Z$, i.e. $v(\tilde A)\ge
e-f_0 = f_0$ by Lemma 1(c). Hence $\tilde A = 3^{f_0}\tilde A_1$ in $R$,
and $y_i = 3^{f_0}(A_1\alpha^i+\bar A_1\beta^i)$ with the bracket in
$\mathbb Z/3^{f_0}$; that bracket is $y^{(1)}_i$. It satisfies the
recurrence mod $3^{f_0}$ (divide the recurrence by $3^{f_0}$) and is
$m$-periodic mod $3^{f_0}$ because $(\alpha^m-1)A_1\equiv 0\pmod{3^{f_0}}$
($\alpha^m-1$ itself is divisible by $3^{f_0}$). Conversely, given
$y^{(1)}\in\mathrm{Fix}_m\bmod 3^{f_0}$, $3^{f_0}y^{(1)}$ is in
$\mathrm{Fix}_m\bmod q$: its period condition mod $3^{f_0}$ multiplied
by $3^{f_0}$ gives the period condition mod $3^{2f_0} = 3^e$. Multiset preservation
is entrywise division, which is injective on multiples of $3^{f_0}$. ∎

Note the contrast with the naive SNF parametrisation: for the smaller
exponent $f_0$ the period condition is *automatic* mod $3^{f_0}$
($\alpha^m-1$ is divisible by $3^{f_0}$), so
$\mathrm{Fix}_m\bmod 3^{f_0}$ is *all* recurrence sequences mod $3^{f_0}$,
of size $3^{2f_0}$ — not $3^{f_0}$. This is why the first version of the
check script (§8) undercounted the top-digit test and had to be fixed.

## 5. Top digit at exponent $f_0$ (Lemma 5)

Let now $y'\in\mathrm{Fix}_m\bmod 3^{f_0}$ (any recurrence sequence, by
the remark above), $n = m/4$, $n_0 = n/3^{f_0-1}\pmod 3$ (a unit in
$\mathbf F_3$), and $Y'_r = \sum_{k<n} y'_{r+4k}\pmod{3^{f_0}}$.

**Lemma 5 (top digit).** $Y'_r$ is divisible by $3^{f_0-1}$, and
$Z'_r := Y'_r/3^{f_0-1}\pmod 3$ satisfies $Z' = n_0\cdot v$, where
$v = (y'_0, y'_1, -y'_0, -y'_1)\pmod 3$ is the mod-3 4-vector of $y'$.

*Proof.* Write $X = \alpha^4 = 1+3u$ as in Lemma 3, and
$S = \sum_{k<n} X^k\in R$, so that
$Y'_r = A'\alpha^r S + \bar A'\beta^r\bar S$ in $R/3^{f_0}$, where $A'$
represents $y'$ (Lemma 2, with no periodicity constraint, since it is
automatic mod $3^{f_0}$).

Divisibility: $(\alpha^4-1)Y'_r = A'\alpha^r(\alpha^m-1) +
\bar A'\beta^r(\beta^m-1)\equiv 0\pmod{3^{f_0}}$ (both $\alpha^m-1$ terms
are divisible by $3^{f_0}$). Since $\alpha^4-1 = 3u$ with
$u = 192+136\sqrt2$, this says $3uY'_r\equiv 0\pmod{3^{f_0}}$ in $R$;
looking at the $\sqrt2$-coefficient, $3\cdot136\cdot Y'_r$ is divisible
by $3^{f_0}$ in $\mathbb Z$, and $\gcd(136,3)=1$, so
$3^{f_0-1}\mid Y'_r$ in $\mathbb Z$.

Value of $S$ mod $3^{f_0}$: $(X-1)S = X^n-1$. We claim
$S/3^{f_0-1}\equiv n_0\pmod{(3)}$ in $R/(3)$. Indeed, let
$Y = X^{3^{f_0-1}}$. By the cubing lemma iterated (Lemma 3 proof),
$(Y-1)/3^{f_0}\equiv u\pmod{(3)}$: the base $X-1 = 3u$, and the cubing
step $(1+3^{s+1}w)^3-1 = 3^{s+2}w + 3^{2s+3}w^2 + 3^{3s+3}w^3$ shows the
quotient mod $(3)$ is preserved ($2s+3, 3s+3\ge s+3$). Then
$X^n-1 = Y^{n_0}-1 = n_0(Y-1) + \sum_{j\ge 2}\binom{n_0}{j}(Y-1)^j$;
dividing by $3^{f_0}$, the first term is $\equiv n_0 u\pmod{(3)}$ and
every $j\ge 2$ term is divisible by $3^{f_0}$ (since $v(Y-1) = f_0$,
$v((Y-1)^j)\ge 2f_0\ge f_0+1$). Hence $(X^n-1)/3^{f_0}\equiv n_0 u
\pmod{(3)}$ in $R$. But $(X-1)S = X^n-1$ exactly in $R$, i.e.
$3u\cdot 3^{f_0-1}S_0 = 3^{f_0}W$ where $S = 3^{f_0-1}S_0$ (valuation
$f_0-1$ follows from $(X-1)S = X^n-1$ and $v(X^n-1) = f_0$) and
$W\equiv n_0 u\pmod{(3)}$; cancelling $3^{f_0}$ (R is a domain) gives
$uS_0 = W$ in $R$, so in the field $R/(3)$, $\bar u\cdot\bar S_0 =
n_0\bar u$ with $\bar u\ne 0$, hence $\bar S_0 = n_0$ (in $\mathbf F_3
\subset R/(3)$). The same holds for $\bar S$ (conjugate of $n_0$ is $n_0$).

Therefore, mod $3^{f_0}$,
$Y'_r = 3^{f_0-1}\bigl(A_0\alpha^r n_0 + \bar A_0\beta^r n_0\bigr)$
with $A_0 = A'\bmod{(3)}\in\mathbf F_9$, i.e.
$Z'_r = n_0\cdot T_r$ where $T_r = A_0\alpha^r + \bar A_0\beta^r$ in
$R/(3)$, $\alpha\equiv -\sqrt2$, $\beta\equiv\sqrt2\pmod{(3)}$.
Writing $A_0 = a+b\sqrt2$ ($a,b\in\mathbf F_3$):
$T_0 = 2a$, $T_1 = 2b$, $T_2 = a$, $T_3 = b$ (direct computation:
$(-\sqrt2)^2 = 2$, $(-\sqrt2)^3 = -2\sqrt2$, etc.; e.g.
$T_1 = (a+b\sqrt2)(-\sqrt2) + (a-b\sqrt2)(\sqrt2) = -4b\equiv 2b$).
But the mod-3 sequence of $y'$ is 4-periodic with
$(y'_0,y'_1,y'_2,y'_3) = (2a,2b,a,b)$: indeed $y'_0 = A_0+\bar A_0 = 2a$,
$y'_1 = 2b$ by the same computation, and mod $3$ the recurrence is
$y'_{i+1} = -y'_{i-1}$, so $y'_2 = -y'_0\equiv a$, $y'_3 = -y'_1\equiv b$.
Hence $T = v$ and $Z' = n_0 v$. ∎

## 6. Mod-3 classification (Lemma 6)

**Lemma 6.** Let $v = (a_0,a_1,-a_0,-a_1)\in\mathbf F_3^4$ be a mod-3
4-vector. Its multiset (with each value repeated $n$ times, as in a full
$m$-sequence) determines $v$ up to the $D_4$-orbit, in exactly three
types:

| type | $(a_0,a_1)$ up to $D_4$ | multiset of $v$ | $D_4$-orbit on pairs |
|---|---|---|---|
| all zero | $(0,0)$ | $\{0^4\}$ | singleton |
| one zero | $(0,1)$ | $\{0^2,1,2\}$ | $(0,1)\to(1,0)\to(0,2)\to(2,0)\to(0,1)$ under $(a,b)\mapsto(b,-a)$ |
| both nonzero | $(1,1)$ | $\{1^2,2^2\}$ | $(1,1)\to(1,2)\to(2,2)\to(2,1)\to(1,1)$ under $(a,b)\mapsto(b,-a)$ |

*Proof.* Exhaustive over the $9$ pairs $(a_0,a_1)\in\mathbf F_3^2$:
$v = (a_0,a_1,-a_0,-a_1)$ has multiset $\{0^4\}$ iff $a_0=a_1=0$;
$\{0^2,1,2\}$ iff exactly one of $a_0,a_1$ is $0$ (then the nonzero
entries are $\pm a$, i.e. $\{1,2\}$); $\{1^2,2^2\}$ iff both are nonzero
(entries are $a_0,-a_0,a_1,-a_1$, each of $\pm1$ twice). The rotation
$(a,b)\mapsto(b,-a)$ on pairs corresponds to cyclically rotating $v$,
and reflection $(a,b)\mapsto(a,-b)$ to reversing it; the cycles in the
table show each type is a single $D_4$-orbit. ∎

Note: this is the mod-3 base case of wave 8, §3, with the factor $n$
divided out. In wave 8 the class sum mod $3$ was $n\cdot v$; when
$3\mid n$ (i.e. $f_0>1$) that is $0$ and carries no information — which
is exactly why the top digit, not the mod-3 class sum, is the right
object at higher exponents.

## 7. Theorem: component Lemma Y mod $3^e$

**Theorem.** Let $4\mid m$, $e = v_3(D_m) = 2f_0$, $q = 3^e$. Component
Lemma Y mod $q$ holds: if $y,y'\in\mathrm{Fix}_m\bmod q$ have the same
multiset mod $q$, then $Y(y')\in D_4\cdot Y(y)$ mod $q$.

*Proof.* By Lemma 4, $y = 3^{f_0}y^{(1)}$, $y' = 3^{f_0}y'^{(1)}$ with
$y^{(1)},y'^{(1)}\in\mathrm{Fix}_m\bmod 3^{f_0}$ and the same multiset
mod $3^{f_0}$ (entrywise division). Reducing mod $3$, they have the
same mod-3 multiset, so by Lemma 6 their mod-3 4-vectors $v,v'$ are in
the same $D_4$-orbit: $v' = \pi(v)$ for some $\pi\in D_4$. By Lemma 5,
their top digits are $Z^{(1)} = n_0 v$ and $Z'^{(1)} = n_0 v' = \pi(Z^{(1)})$
(scalar $n_0$ commutes with coordinate permutations). Now
$Y(y) = 3^{f_0}Y^{(1)}$ and $Y^{(1)} = 3^{f_0-1}Z^{(1)}\pmod{3^{f_0}}$,
so $Y(y) = 3^{2f_0-1}Z^{(1)} = 3^{e-1}Z^{(1)}\pmod q$, and similarly
$Y(y') = 3^{e-1}Z'^{(1)} = \pi(Y(y))\pmod q$, since $\pi$ permutes
coordinates and commutes with the scalar $3^{e-1}$. ∎

**Scope.** This closes P3′ only. It does not prove component Lemma Y
for $p=2$ (P2: the 2-primary component, where $\alpha-\beta$ has norm
$-32\equiv 0\pmod{2^e}$ and Lemma 2's representation fails at the first
step), and it does not address Pmix (per-component permutations
$\pi_q$ possibly differing across $q$, and exact-integer carries
$\lfloor Y_r/D\rfloor$). Global Lemma Y therefore remains open, but its
3-primary part is now a theorem, and the remaining gaps are precisely
P2 and Pmix — no longer P3′.

For completeness: the odd primes $p\nmid 24$ are already handled by wave
8, §2 ($Y_r\equiv 0\pmod q$, so component Lemma Y is trivial there);
$p=3$ was the only odd prime with a nontrivial component, and it is the
one closed here.

## 8. Computational verification (not part of the proof)

Script: `methods/wave9_P3prime_check.py`, log:
`methods/wave9_P3prime_check.log` (plus extended runs for $m=48,60,72$).

- $v_3(D_m) = 2f_0$ for all $4\mid m\le 100$ (direct $s_m$ recurrence).
- Component test (SNF parametrisation, valid since $q\parallel D_m$):
  $m = 4,8,12,16,20,24,28,32,36,48,60,72$: SNF $v_3(d_1) = f_0$
  (balanced), every $\mathrm{Fix}\bmod q$ entry divisible by $3^{f_0}$,
  component Lemma Y mod $q$ holds with $0$ bad multisets. Point counts:
  $q = 9$ ($f_0=1$), $81$ ($f_0=2$), $729$ ($f_0=3$, $m=36,72$;
  $17$ multisets at $q=729$).
- Top-digit test (all $\mathrm{Fix}\bmod 3^{f_0}$ points, i.e. all
  $(y_0,y_1)\in(\mathbb Z/3^{f_0})^2$): $Z' = n_0 v$ holds *exactly*
  (not just up to $D_4$) for every point at $m = 4,\dots,72$ step $4$;
  mod-3 multisets number $3$ in every case, with $v$ in a single
  $D_4$-orbit per multiset (bad $=0$).

Correction recorded: the first version of the top-digit test reused the
SNF parametrisation for exponent $f_0 < e$, which enumerates only a
subset of $\mathrm{Fix}\bmod 3^{f_0}$ (the SNF formula assumes
$q\parallel D$). It was fixed to enumerate all $(y_0,y_1)$ pairs; the
final numbers above are from the corrected, complete enumeration.

## 9. Files

- This note: [wave9_lemmaY_P3prime.md](wave9_lemmaY_P3prime.md)
- Check script: [wave9_P3prime_check.py](wave9_P3prime_check.py)
- Check log: `wave9_P3prime_check.log` (not in repository)
- Prior notes: [wave8_lemmaY_proof_attempt.md](wave8_lemmaY_proof_attempt.md),
  [pair_sorted_identity_note.md](pair_sorted_identity_note.md)
