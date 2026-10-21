> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round8_2026_10_21/r8_return_audit_three_time_resonance.md`. Embedded SHA256: `792f99160dfbc47714a86da08cb8ac2a480ae7d3a50180afd1359ae8923341e2`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit: signed three-time resonance and exact Weyl recursion

21 October 2026. Reviewer: signed-return branch.

**Verdict: the displayed signed identities, local phase change, and
nontruncated recursion are correct as stated. No mathematical defect
found.** Their time differences remain fixed in the explicit triple
calculation; the source correctly does not call it an estimate for
the required Heisenberg-time spectral statistic.

## 1. Frozen source and independent exact check

The entire source was read:

- `research_round8_2026_10_21/r8_weyl_three_time_resonance_and_exact_recursion.md`.
- SHA-256: `8f6a660d4bb776c769aa7e96e7a4607609c7a44c06addb494764189e3ef1fbf2`.

An independent exact checker was written and run:

- `research_round8_2026_10_21/r8_return_three_time_exact_check.py`.
- SHA-256: `03959edadee28fb26adfffce2385b963f1918cc1b6a4ec61a85a4fc65f0f58a0`.

The checker uses only standard-library integer and rational arithmetic,
with rational complex numbers represented by pairs of fractions. It
expands the original Laurent polynomial in the formal variables
$e^{2\pi iq}$, $e^{2\pi ip}$, rather than entering the
claimed final coefficient list. It then checks all $32^3=32768$
ordered support triples. Separately, it compares every coefficient
of the formal quadratic polynomial on the two sides of the local
Cayley--Hamilton area identity.

Its exact output is:

| First label | Middle label | Last label | Area | Coefficient |
| --- | --- | --- | ---: | --- |
| $(-1,0)$ | $(6,0)$ | $(-1,0)$ | 24 | $-97/1600000-299i/16000000$ |
| $(1,0)$ | $(-6,0)$ | $(1,0)$ | 24 | $-97/1600000+299i/16000000$ |
| $(-1,-1)$ | $(2,0)$ | $(-1,1)$ | 2 | $-i/64000000$ |
| $(1,1)$ | $(-2,0)$ | $(1,-1)$ | 2 | $i/64000000$ |

Thus the sum at area 24 is exactly $-97/800000$, the sum at
area 2 is exactly zero, and there are no other closed integer
triples. The formal quadratic polynomial difference in the area
identity is zero. These finite checks supplement the following
proof audit; they are not numerical evidence for universality.

The checker is reproducible by:

```text
python research_round8_2026_10_21/r8_return_three_time_exact_check.py
```

## 2. Weyl convention and exact transport

For the original modular-half basis, direct multiplication gives the
phase $e_N(\overline2(lk'-kl'))$. This is consistent with the
ordering of the shift and character in $T_N(l,k)$. The triple
phase in source (2.2) follows by applying that multiplication twice.

The displayed covariance matrix
$S=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)$
is verified directly from the kernel, including its constant term.
Subtracting $Q(x,y)$ from the exponent on the left gives
$$
 -\frac14lx+\left(k+\frac34l\right)y
       -\frac12kl-\frac38l^2,
$$
where every fraction in this check denotes its modular inverse.
For $l'=4k+3l$, $k'=3k+2l$, the right exponent has
the same coefficients of $x$ and $y$. Its constant is
$$
 -\frac38(4k+3l)^2+
    \frac12(3k+2l)(4k+3l)
       =-\frac12kl-\frac38l^2.
$$
This is an identity over any ring in which two is invertible, so it
does not impose a prime or squarefree modulus. No residual scalar
phase is left in the transport formula.

## 3. Fourier support and completeness of the four triples

The coefficient formulas follow directly from expanding
$r(q)=(1-\cos(14\pi q))(1+\cos(2\pi q))$. The constant
coefficient cancels after subtracting $1/10$. The pure support is
$\{\pm1,\pm2,\pm5,\pm6,\pm7,\pm8,\pm9\}$, and the
mixed supports at $l=\pm1$ have
$k\in\{0,\pm1,\pm6,\pm7,\pm8\}$. Thus there are 32
labels in total. The listed values
$$
 c_{1,0}=(10-i)/200,\quad
 c_{-6,0}=-c_{1,0}/2,\quad
 c_{-2,0}=i/400,\quad
 \gamma=(-3-4i)/1000
$$
have the correct signs. This calculation uses the modular basis;
an ordinary-half shift is neither needed nor silently inserted.

For $\kappa_0+S\kappa_1+S^2\kappa_2$, the coordinate bounds
are indeed
$$
 9+(3\cdot9+2)+(17\cdot9+12)=203,
$$
and
$$
 1+(4\cdot9+3)+(24\cdot9+17)=273.
$$
Consequently every modularly zero total label is an ordinary zero
for all odd $N\ge275$. This is the only large-modulus step in
the triple enumeration, and it is uniform in all such dimensions.

Eliminating the pure coordinates gives exactly
$$
 4(k_0-k_2)=3l_0+l_1+3l_2,\qquad
 4k_1=-24k_2-l_0-3l_1-17l_2.
$$
The second congruence modulo four and the range
$-3\le l_0-l_1+l_2\le3$ force
$l_1=l_0+l_2$. Substitution yields source (3.2).
The seven possible pairs $(l_0,l_2)$, and every surviving value
of $t=k_2$ in the subsequent support checks, were individually
checked. They give precisely the four rows displayed in the source
and in the independent enumeration above. In particular, no unused
mixed support point can produce another closed triple.

## 4. Signed areas and the commutator limit

For a closed triple $u+v+w=0$, expanding with
$w=-u-v$ makes the sum of the three area terms equal to
$\omega(u,v)$. For the pure positive row,
$$
 u=(1,0),\quad v=(-18,-24),\quad w=(17,24),
$$
so the area is $24$. Negating all vectors leaves this bilinear
area unchanged. Thus both rows carry $e_N(12)$, not conjugate
phases. Their coefficients are conjugates, and their sum is
$$
 -\operatorname{Re}\left((10-i)^3/200^3\right)
    =-970/8000000=-97/800000.
$$
The modular half of 24 is exactly 12 modulo every odd $N$.

For the mixed positive row the transported vectors are
$(1,1),(-6,-8),(5,7)$; their area is $2$, hence the phase
is $e_N(1)$. Its coefficient is
$\gamma\overline\gamma\, i/1600=i/64000000$.
The negative row has the same area and opposite coefficient.
These two terms therefore cancel exactly before taking any modulus.

The normalized trace of a zero-label Weyl operator is one. This
proves the claimed triple trace with no missing dimension factor.
For arbitrary integer $j$, conjugation by $M_N^j$ reduces the
triple to $j=0$, including negative or $N$-dependent indices.

Writing $z=N^{-1}\operatorname{Tr}(A_jA_{j+1}A_{j+2})$,
Hermitian conjugation and cyclicity give the reversed order as
$\overline z$. The normalized commutator expression is
$iN(z-\overline z)$. Since
$z=-(97/800000)e^{24\pi i/N}$, this equals
$$
 \frac{97N}{400000}\sin(24\pi/N),
$$
with positive sign. Its limit is
$97\cdot24\pi/400000=291\pi/50000$, as stated.
The sine is positive for all the allowed $N$.

## 5. Full kick expansion and interaction ordering

The modular Weyl matrices form an orthonormal basis for the
normalized Hilbert--Schmidt inner product by finite-character
orthogonality. Hence expansion (5.1) is finite and exact, and
$\sum|d_N(\eta)|^2=1$ follows from unitarity of the entire
exponential. No Taylor approximation enters.

Expanding $(E_NM_N)^m$ inductively gives the ordered product
$E_0E_1\cdots E_{m-1}M_N^m$, in that order, with
$E_j=M_N^jE_NM_N^{-j}$. Successive Weyl multiplication then
gives the total label and pairwise area in (5.3). Every sum is over
the finite modular phase space. The formula is valid for arbitrary
positive integer $m$, although it supplies no asymptotic estimate
uniform in a growing $m$.

## 6. Cayley--Hamilton move and its complete local phase

The move preserves the total label because
$h-6Sh+S^2h=0$. Let the three transported original vectors be
$x,y,z$, and their changes be $a,b,c$, with $a+b+c=0$.
Every area term with an earlier or later vector cancels by this
zero sum. The exact remaining difference is
$$
 \Delta\mathcal A
  =\omega(a,x+y)-\omega(c,y+z)+\omega(a,b).
$$
For clarity, the linear part is obtained by combining
$\omega(x,b)+\omega(x,c)=\omega(a,x)$, and the quadratic part
$\omega(a,b)+\omega(a,c)+\omega(b,c)$ is $\omega(a,b)$.

Substitute
$a=S^jh$, $b=-6S^{j+1}h$, $c=S^{j+2}h$, then use
$\det S=1$ to preserve $\omega$. The first two terms become
$$
 \omega\bigl(h,\eta_j+(S-S^{-1})\eta_{j+1}-\eta_{j+2}\bigr),
$$
and the last becomes $-6\omega(h,Sh)$. This verifies every
sign in source (6.2). The difference matrix is
$S-S^{-1}=\left(\begin{smallmatrix}0&4\\8&0\end{smallmatrix}\right)$.
For a zero background and $h=(1,0)$,
$-6\omega(h,Sh)=-6(-4)=24$, consistent with the trace triangle.

The exact checker also verified this identity as a polynomial in
all eight scalar coordinates of the three labels and $h$. The
analytic proof makes clear why the phase change stays local only
for three consecutive blocks. The source correctly retains the
simultaneous change of all three kick coefficients and does not
assume invariance of their product.

## 7. Recursion and its precise limitation

In multiplying
$L_m=\sum_\mu v_m(\mu)W_N(\mu)$ on the right by $E_m$,
put $\eta=S^m\eta_0$ for the transported kick label. Since
$\det S=1$, this is a bijection at every modulus. The kick
coefficient becomes $d_N(S^{-m}\eta)$. To produce the output
label $\lambda$, the previous coefficient is
$v_m(\lambda-\eta)$, and the Weyl phase is exactly
$e_N(\overline2\omega(\lambda-\eta,\eta))$. This proves
the stated recursion with its inverse power and multiplication
ordering intact.

Right multiplication by a unitary preserves Hilbert--Schmidt norm,
so the squared coefficient norm stays one. The trace readout in
(7.2) follows by linearity. In fact Parseval for $M_N^m$ gives
$\sum_\lambda|\operatorname{Tr}(W_N(\lambda)M_N^m)|^2=N^2$,
so coefficient Cauchy--Schwarz recovers precisely the elementary
$|\operatorname{Tr}U_N^m|\le N$ bound. It supplies none of
the required weighted cancellations on times of order $N$.

The source consistently distinguishes its completed exact identities
from the original open pair functional and the higher hierarchy.
No correction is required by this audit.
