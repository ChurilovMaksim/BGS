> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/adversarial_finite_detector_shell_coherence.md`. Embedded SHA256: `76aa1ece063eea6b9e673d5fc592fa23ba72c541fee5c93916314a62da85ee6f`.
> [Thematic guide](../../topics/histories.md).

# Exact finite Fourier detectors: coherence between geometric shells

## Statement and scope

This note proves an exact finite-dimensional counterpart of the geometric-shell calculation. The Hilbert space is the original $\mathbb C^N$, with the ordinary finite Fourier transform and coordinate projections. No approximation to $U_N$, classical return map, or orbit sum is made.

Fix $0<\rho<1$, and write
$$
\ell_\rho=\log(1/\rho).
$$
The application to the previously constructed actual endpoint intervals takes $\rho=\Lambda^{-1}$, where $\Lambda>5$ is the actual unstable multiplier at the chosen fixed point. The theorem below holds for every fixed $\rho$, independently of that application.

For every sufficiently large odd $N$, set
$$
w_N=\left\lfloor\frac{N}{2\sqrt{\log N}}\right\rfloor,\qquad
r_N=2w_N+1,\qquad
s_N=\left\lfloor\frac{N}{\sqrt{\log N}}\right\rfloor,
$$
$$
\sigma_N=\frac{s_N}{N},\qquad
L_N=r_N\sigma_N.
\tag{1.1}
$$
Thus
$$
L_N=\frac{N}{\log N}(1+o(1)),\qquad
\sigma_N\longrightarrow0.
\tag{1.2}
$$

Let $x_0=(N-1)/2$, and let $I_N$ consist of the $r_N$ consecutive coordinate sites centered at $x_0$, interpreted modulo $N$. Let $J_N$ consist of any $s_N$ consecutive Fourier indices. Define
$$
(\mathcal F_N)_{kx}=N^{-1/2}e^{-2\pi i kx/N},\qquad
E_N=P_{I_N}\mathcal F_N^*P_{J_N}\mathcal F_NP_{I_N}.
\tag{1.3}
$$
This is an exact positive contraction and
$$
\operatorname{Tr}E_N=L_N.
\tag{1.4}
$$

Use the integer coordinate $n=x-x_0$, $-w_N\le n\le w_N$. Put
$$
n_j=\lfloor w_N\rho^j\rfloor,\qquad
S_j^+=\{n_{j+1}+1,\ldots,n_j\},\qquad
S_j^-=-S_j^+,\qquad S_j=S_j^+\cup S_j^-.
\tag{1.5}
$$
Empty shells are omitted. Together with $S_*=\{0\}$, these form a finite partition of $I_N$. In particular, the positive and negative shells at the same level belong to the same block. Denote their coordinate projections by $P_j$ and $P_*$, and define the pinching
$$
H_N=P_*E_NP_*+\sum_jP_jE_NP_j.
\tag{1.6}
$$
Then $0\le H_N\le I$ and $\operatorname{Tr}H_N=L_N$.

### Theorem

As $N\to\infty$ through all odd integers,
$$
\boxed{
Q_N:=\operatorname{Tr}E_N^2-\operatorname{Tr}H_N^2
=\|E_N-H_N\|_{\mathrm{HS}}^2
=\frac{(\log L_N)^2}{\pi^2\ell_\rho}
+O_\rho(\log L_N).
}
\tag{1.7}
$$
Moreover,
$$
\operatorname{Tr}E_N^2
=L_N-\frac1{\pi^2}\log L_N+O(1).
\tag{1.8}
$$
Consequently,
$$
\frac{\|E_N-H_N\|_{\mathrm{HS}}}
     {\|E_N\|_{\mathrm{HS}}}\longrightarrow0,
\qquad
e_2(E_N)-e_2(H_N)=-\frac{Q_N}{2}\longrightarrow-\infty.
\tag{1.9}
$$

For each fixed $0<t<1$,
$$
-\frac{t^2Q_N}{2(1-t)^2}
\le
\log\frac{\det(I-tE_N)}{\det(I-tH_N)}
\le
-\frac{t^2Q_N}{2}.
\tag{1.10}
$$
Thus the determinant ratio tends to zero at rate
$\exp[-\Theta_{\rho,t}((\log L_N)^2)]$.

The absolute determinant difference nevertheless tends to zero: both determinants are at most $e^{-tL_N}$. The conclusions concern the second coefficient and the connected logarithm, and cannot be used to deny an absolute $o(1)$ comparison of these two vanishing determinants.

## 2. Exact finite Fourier entries and the modular denominator

If $m,n\in I_N$, let $d=m-n$ be the difference of the chosen integer lifts. A finite geometric sum in (1.3) gives, for $d\ne0$,
$$
|(E_N)_{mn}|^2
=\frac{\sin^2(\pi\sigma_N d)}
       {N^2\sin^2(\pi d/N)}.
\tag{2.1}
$$
For $d=0$, the entry equals $\sigma_N$. The initial Fourier index affects only the phase of an off-diagonal entry.

For $0<|d|\le N/2$,
$$
0\le
\frac1{N^2\sin^2(\pi d/N)}
-\frac1{\pi^2d^2}
\le\frac{C}{N^2}.
\tag{2.2}
$$
Indeed, after putting $u=\pi d/N$, the difference is
$$
\frac1{N^2}
\frac{(u/\sin u)^2-1}{u^2}.
$$
The last factor extends continuously to $u=0$ and is bounded on
$[-\pi/2,\pi/2]$. Nonnegativity follows from $|\sin u|\le |u|$.

Define the nonnegative sequence
$$
f_\sigma(d)=
\begin{cases}
\dfrac{\sin^2(\pi\sigma d)}{\pi^2d^2},&d\ne0,\\[4pt]
\sigma^2,&d=0.
\end{cases}
\tag{2.3}
$$
For all sufficiently large $N$, every lifted difference within $I_N$ satisfies $|d|\le2w_N<N/2$. Therefore replacing the squared matrix entries in any selected sum over ordered coordinate pairs by $f_{\sigma_N}(m-n)$ has absolute error at most
$$
C\frac{r_N^2}{N^2}=O(1/\log N).
\tag{2.4}
$$
This applies both to the whole purity and to the sum restricted to pairs belonging to different shells. No operator norm or semiclassical approximation is involved.

## 3. A uniform discrete adjacent-interval calculation

### Lemma 3.1

Uniformly for integers $a\ge1$ and $0<\sigma\le1/2$,
$$
\sum_{d=1}^a\frac{\sin^2(\pi\sigma d)}d
=\frac12\log^+(a\sigma)+O(1),
\qquad
\log^+x=\max(0,\log x).
\tag{3.1}
$$

If $a\sigma\le1$, the left side is at most
$$
\pi^2\sigma^2\sum_{d=1}^a d=O(1).
$$
Suppose $a\sigma>1$. The identity
$$
\sum_{d=1}^\infty\frac{\cos(2\pi\sigma d)}d
=-\log(2\sin(\pi\sigma))
\tag{3.2}
$$
follows by taking real parts of
$\sum_{d\ge1}z^d/d=-\log(1-z)$ for $|z|<1$, and taking the radial limit. Convergence and the radial limit are also justified directly by summation by parts, since
$$
\left|\sum_{d=A}^B e^{2\pi i\sigma d}\right|
\le \frac1{\sin(\pi\sigma)}.
$$
The tail in (3.2) after $a$ is therefore at most
$C/(a\sin(\pi\sigma))\le C/(a\sigma)$, which is bounded in the present case. Using
$\sin^2u=(1-\cos 2u)/2$,
$\sum_{d\le a}1/d=\log a+O(1)$, and
$\log(2\sin\pi\sigma)=\log\sigma+O(1)$
proves (3.1).

### Lemma 3.2

For positive integers $a,b$, let
$$
\mathcal A_\sigma(a,b)=
\sum_{u=1}^a\sum_{v=1}^b f_\sigma(u+v-1).
\tag{3.3}
$$
Then, uniformly in $a,b,\sigma$,
$$
\mathcal A_\sigma(a,b)
=\frac1{2\pi^2}
  \log^+\!\big(\sigma\min(a,b)\big)+O(1),
\tag{3.4}
$$
and
$$
0\le\mathcal A_\sigma(a,b)\le\sigma^2ab.
\tag{3.5}
$$

To prove (3.4), write $c=\min(a,b)$. The multiplicity of the distance $d=u+v-1$ is exactly $d$ for $1\le d\le c$, and is at most $c$ for $d>c$. Hence the contribution of $d\le c$ is
$$
\frac1{\pi^2}\sum_{d=1}^c\frac{\sin^2(\pi\sigma d)}d.
$$
The remaining contribution is bounded by
$c\pi^{-2}\sum_{d>c}d^{-2}=O(1)$.
Apply Lemma 3.1. Inequality (3.5) follows from $f_\sigma(d)\le\sigma^2$.

These lemmas retain the exact lattice spacing and are uniform when the bandwidth $\sigma=\sigma_N$ shrinks.

## 4. Rounded shells and their accumulated interaction

In this section suppress the subscript $N$ and write
$$
w=w_N,\quad \sigma=\sigma_N,\quad Z=w\sigma,\quad
J=\left\lfloor\frac{\log Z}{\ell_\rho}\right\rfloor.
\tag{4.1}
$$
Then $Z\to\infty$ and
$$
1\le Z\rho^J<\rho^{-1}.
\tag{4.2}
$$
Call $0,\ldots,J$ the resolved shell indices. For these indices,
$$
n_j-n_{j+1}
=(1-\rho)w\rho^j+O(1).
\tag{4.3}
$$
As $\sigma\to0$, all these widths are positive and comparable to $w\rho^j$, uniformly over the resolved indices; the constants depend only on $\rho$.

### 4.1. Adjacent shells give the quadratic logarithm

Two adjacent positive shells $S_j^+,S_{j+1}^+$ have interaction exactly
$$
\mathcal A_\sigma(n_j-n_{j+1},n_{j+1}-n_{j+2}).
\tag{4.4}
$$
For $0\le j<J$, the minimum of the two widths is comparable to $w\rho^j$. Equations (3.4) and (4.2) imply
$$
\mathcal A_\sigma(n_j-n_{j+1},n_{j+1}-n_{j+2})
=\frac1{2\pi^2}(\log Z-j\ell_\rho)+O_\rho(1).
\tag{4.5}
$$
This remains correct at the final few resolved indices: replacing
$\log^+(\sigma\min(a,b))$ by $\log(Z\rho^j)$ incurs only a bounded error depending on $\rho$.

Summing (4.5) gives
$$
\sum_{j=0}^{J-1}
\mathcal A_\sigma(n_j-n_{j+1},n_{j+1}-n_{j+2})
=\frac{(\log Z)^2}{4\pi^2\ell_\rho}
+O_\rho(\log Z).
\tag{4.6}
$$
There are two signs of the coordinate and two ordered directions for each adjacent pair. These interactions all join different blocks in (1.6). Their total is consequently
$$
\frac{(\log Z)^2}{\pi^2\ell_\rho}
+O_\rho(\log Z).
\tag{4.7}
$$

### 4.2. Nonadjacent resolved shells of the same sign

If $0\le j<k-1\le J-1$, the gap between $S_j^+$ and $S_k^+$ is at least
$$
n_{j+1}-n_{j+2}
\ge c_\rho w\rho^j.
$$
Their cardinalities are at most $C_\rho w\rho^j$ and $C_\rho w\rho^k$. Since
$f_\sigma(d)\le(\pi^2d^2)^{-1}$,
their interaction is at most
$$
C_\rho\rho^{k-j}.
\tag{4.8}
$$
Summing this geometric bound over all such pairs gives $O_\rho(J+1)$. The negative coordinate side has the same bound.

### 4.3. Resolved shells on opposite sides

A point in $S_j^+$ and a point in $S_k^-$ are separated by at least
$c_\rho w(\rho^j+\rho^k)$. Their interaction is bounded by
$$
C_\rho
\frac{\rho^{j+k}}{(\rho^j+\rho^k)^2}
\le C_\rho\rho^{|j-k|}.
\tag{4.9}
$$
The sum over $0\le j,k\le J$ is $O_\rho(J+1)$.

Pairs with $j=k$ are retained by the pinching and do not contribute to $Q_N$. Including them in this upper bound only enlarges it. Thus putting both signs in one block changes no leading coefficient.

### 4.4. The unresolved tail and the central site

All shells with $j\ge J+1$, together with the central site, lie in
$$
[-n_{J+1},n_{J+1}],
\qquad n_{J+1}<1/\sigma.
\tag{4.10}
$$
Their total cardinality is $O(1/\sigma)$. All their internal interactions are $O(1)$, because $f_\sigma\le\sigma^2$.

The interaction between shell $J$ and this tail is also $O_\rho(1)$, by the same cardinality bound. For a resolved shell $j<J$, the distance to this tail is at least
$c_\rho w\rho^j$. Hence its interaction with the entire tail is at most
$$
\frac{C_\rho}{\sigma w\rho^j}
=\frac{C_\rho}{Z\rho^j}.
\tag{4.11}
$$
Summing over $j<J$ gives $O_\rho(1)$, by (4.2) and a geometric series.

This accounts for every deep shell, including the finitely many nonempty shells at the final integer scales, and for the singleton at zero. No limiting accumulation of uncounted shell boundaries remains.

### 4.5. Conclusion for the loss of purity

The model loss obtained by replacing squared entries with $f_\sigma$ is a sum of nonnegative interactions between different blocks. Its adjacent contribution is (4.7); all remaining terms have total size $O_\rho(\log Z)$ by Sections 4.2–4.4. Thus
$$
Q_N^{\mathrm{model}}
=\frac{(\log Z)^2}{\pi^2\ell_\rho}
+O_\rho(\log Z).
\tag{4.12}
$$
Now $\log Z=\log L_N+O(1)$, and the exact modular correction is $O(1/\log N)$ by (2.4). This proves (1.7), except for its Hilbert–Schmidt identity. That identity is immediate because coordinate pinching is an orthogonal projection for the Hilbert–Schmidt inner product:
$$
\operatorname{Tr}(E_N-H_N)H_N=0.
$$

## 5. The whole purity and its normalization

For $0<\sigma<1$, the Fourier coefficients of the indicator of any circle interval of length $\sigma$ have squared moduli $f_\sigma(d)$. Parseval gives
$$
\sum_{d\in\mathbb Z}f_\sigma(d)=\sigma.
\tag{5.1}
$$
This can also be proved directly by integrating the finite trigonometric expansions of the indicator and taking their $L^2$ limit.

For $r$ consecutive lattice sites,
$$
\begin{aligned}
\sum_{m,n=1}^{r}f_\sigma(m-n)
&=r\sigma^2+2\sum_{d=1}^{r-1}(r-d)f_\sigma(d)\\
&=r\sigma
 -2\sum_{d=1}^{r-1}d f_\sigma(d)
 -2r\sum_{d\ge r}f_\sigma(d).
\end{aligned}
\tag{5.2}
$$
The final term is $O(1)$, since $f_\sigma(d)\le(\pi^2d^2)^{-1}$. Lemma 3.1 applied to the middle term gives, when $r\sigma\to\infty$,
$$
\sum_{m,n=1}^{r}f_\sigma(m-n)
=r\sigma-\frac1{\pi^2}\log(r\sigma)+O(1).
\tag{5.3}
$$
Taking $r=r_N,\sigma=\sigma_N$ and using (2.4) proves (1.8).

In particular,
$$
\|E_N\|_{\mathrm{HS}}^2\sim L_N,\qquad
\|E_N-H_N\|_{\mathrm{HS}}^2=O_\rho((\log L_N)^2).
$$
This proves the first assertion in (1.9).

For every finite matrix $T$,
$$
e_2(T)=\frac{(\operatorname{Tr}T)^2-\operatorname{Tr}(T^2)}2.
\tag{5.4}
$$
The traces of $E_N$ and $H_N$ agree. Subtraction yields
$$
e_2(E_N)-e_2(H_N)=-\frac{Q_N}{2},
$$
which proves the remaining assertion in (1.9).

## 6. Determinant comparison with the full sign

The following argument applies to any positive contraction $E$ and any orthogonal block pinching $H$. Write
$$
X=E-H,\qquad G_u=H+uX,\quad 0\le u\le1.
$$
Every $G_u$ is a positive contraction. For $0<t<1$, let
$$
F(u)=\log\det(I-tG_u),\qquad R_u=(I-tG_u)^{-1}.
$$
Ordinary finite-dimensional differentiation gives
$$
F'(u)=-t\operatorname{Tr}(R_uX),
$$
$$
F''(u)
=-t^2\operatorname{Tr}(R_uXR_uX)
=-t^2\|R_u^{1/2}XR_u^{1/2}\|_{\mathrm{HS}}^2.
\tag{6.1}
$$
Because $I\le R_u\le(1-t)^{-1}I$,
$$
\|X\|_{\mathrm{HS}}
\le\|R_u^{1/2}XR_u^{1/2}\|_{\mathrm{HS}}
\le(1-t)^{-1}\|X\|_{\mathrm{HS}}.
\tag{6.2}
$$
The lower estimate also holds for indefinite $X$: apply the Hilbert–Schmidt contraction bound to multiplication on both sides by $R_u^{-1/2}$.

Since $R_0$ is block diagonal while all diagonal blocks of $X$ vanish,
$$
F'(0)=0.
\tag{6.3}
$$
Integrating
$$
F(1)-F(0)=\int_0^1(1-u)F''(u)\,du
$$
proves (1.10), using $\|X\|_{\mathrm{HS}}^2=Q_N$.

Finally, for a positive contraction $T$,
$$
\det(I-tT)\le e^{-t\operatorname{Tr}T}.
\tag{6.4}
$$
Both determinants in (1.10) therefore tend to zero. Indeed the sign in (1.10) and (6.4) imply
$$
0\le \det(I-tH_N)-\det(I-tE_N)\le e^{-tL_N}.
\tag{6.5}
$$
The divergent logarithmic correction and degree-two coefficient loss must not be confused with an absolute determinant error.

## 7. What this establishes for the current research

The exact matrices (1.3) are available on the original quantum spaces for every sufficiently large odd $N$. Their windows have coordinate and momentum fractions of order $1/\sqrt{\log N}$, and their trace is of order $N/\log N$. Their pinching by geometric run-length shells has vanishing relative Hilbert–Schmidt error, but discards an explicitly evaluated positive cross-shell contribution of order $(\log N)^2$.

Thus a replacement of a coherent restricted Fourier detector by the incoherent sum of its geometric-shell blocks does not preserve its second elementary symmetric coefficient or its connected determinant logarithm with an $o(1)$ error. The finite modular denominator, all rounding errors, the central accumulation of shells, and the two sides of the coordinate interval have been included in the proof.

This is a statement about the actual finite detector, not a proof of a semiclassical replacement for quantum first-return amplitudes. In particular:

- The detector trace $L_N$ diverges. These coefficients are not the fixed-test coefficients $M^U_{k,N}(b)$ in $H_{\mathrm{diag}}$.
- The pair statistic of $U_N$ is not inferred from detector purity.
- The phases associated with different excursion interiors, including their stationary action constants, have not been estimated by this argument.
- The absolute determinant comparison in (6.5) actually tends to zero, even though the ratio and the degree-two difference exhibit the stated behavior.

The original first missing pair estimate remains the weighted cancellation of
$$
\frac1{N^2}\sum_{m\ge1}
|\widehat b(m/N)|^2
\bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)
$$
for each fixed admissible $b$. No such estimate, and no counterexample to it, is asserted here.

