# The fourth-order drift of a Gaussian coboundary step

**Claim ID: BGS-FLOW-008.** Project derivation, 29 September 2026;
author self-review, not an independent or formal certificate.
All limits in the one-step expansion first fix the matrix dimension.

Use normalized GUE $G$, $B=UGU^*$, and the actual coboundary step

$$
F_\varepsilon(U,G)=e^{i\varepsilon(G-B)}U.
$$

Its spectrum equals that of $W_\varepsilon U$, where
$W_\varepsilon=e^{-i\varepsilon G}e^{i\varepsilon(G-B)}e^{i\varepsilon B}$.
Write $m_j=N^{-1}\operatorname{Tr}U^j$, and put
$H=i[G,B]/\sqrt2$, $X=H-\mathbb EH$, as in
[FLOW-003](../quadratic_coboundary_noise.md).

## 1. Exact fourth-degree logarithm

For anti-Hermitian letters $A=iG$, $D=iB$, formal multiplication gives

$$
\log(e^{-\varepsilon A}e^{\varepsilon(A-D)}e^{\varepsilon D})
=\varepsilon^2L_2+\varepsilon^3L_3+\varepsilon^4L_4+O_G(\varepsilon^5),
$$
$$
L_2=[A,D]/2=iH/\sqrt2,
$$
$$
L_3=(AD^2-A^2D-2DAD+2ADA-DA^2+D^2A)/6,
$$
$$
\begin{split}
24L_4={}&AD^3-A^2D^2-3DAD^2+A^3D+2ADAD+3D^2AD\\
 &-3A^2DA+3ADA^2-DA^3-2DADA+D^2A^2-D^3A. \tag{1}
\end{split}
$$

There is no first-degree term. Formula (1) follows by multiplying the
three exponential polynomials through degree four and subtracting
one half of the square of their degree-two term in the logarithm.
Odd Gaussian parity gives $\mathbb EL_3=0$. Wick contraction yields

$$
\mathbb EL_4=\frac38(m_1U^*-\bar m_1U)
+\frac1{12}\left[m_1^2U^{*2}+m_2\bar m_1U^*
                  -\bar m_1^2U^2-\bar m_2m_1U\right]. \tag{2}
$$

For a check independent of matrix dimension, a word with four letters
$G$ or $UGU^*$ is
$U^{b_1}G U^{b_2-b_1}G U^{b_3-b_2}G U^{b_4-b_3}G U^{-b_4}$,
$b_j\in\{0,1\}$. Use the exact identity

$$
\mathbb E[G A_1G A_2G A_3G]
=\frac{\operatorname{Tr}A_1\operatorname{Tr}A_3}{N^2}A_2
+\frac{A_3A_2A_1}{N^2}
+\frac{\operatorname{Tr}A_2\operatorname{Tr}(A_1A_3)}{N^2}I. \tag{3}
$$

The middle term in each word is $I/N^2$ after the outer powers of $U$;
these terms cancel in (1). Substitution of the other two contractions
gives (2), without an asymptotic Wick approximation.

## 2. Why covariance alone does not give the generator

The leading mean Hermitian field is

$$
J=\mathbb EH/\sqrt2=-\operatorname{Im}(m_1U^*). \tag{4}
$$

For smooth class functions, the mean one-step change starts with
$\varepsilon^2D_J$. Its action on the first normalized trace is

$$
D_Jm_1=-\tfrac12(m_1-\bar m_1m_2),\qquad
D_J|m_1|^2=-|m_1|^2+\operatorname{Re}(\bar m_1^2m_2). \tag{5}
$$

Hence an uncentered matrix process cannot generally have the raw
$L_X$ diffusion as its fourth-time-scale limit: it already has a faster
mean motion. Nor does frozen mean subtraction remove every drift.
For the explicitly modified step
$e^{-i\varepsilon^2J(U)}W_\varepsilon(U,G)U$, the generator at time step
$h=\varepsilon^4/2$ tends, at fixed $N$, to

$$
L_X+D_{B_4},\qquad
B_4=\frac32\operatorname{Im}(m_1U^*)
+\frac13\operatorname{Im}(m_1^2U^{*2}+m_2\bar m_1U^*). \tag{6}
$$

Indeed the centered logarithm has quadratic term $iX/\sqrt2$;
its additional fourth-degree commutator has zero expectation, and
$B_4=2\mathbb EL_4/i$. This is a specified frozen compensation,
not the exact inverse flow of the state-dependent mean field.
Different compensation schemes must not be identified silently.

Equations (4) and (6) are commuting traceless Hermitian fields. Their
operator norms and all derivatives are bounded at fixed $N$. Taylor
expansion on a bounded Gaussian set, followed by Gaussian moment/tail
bounds, justifies the expectation expansion uniformly on compact state
sets. Symmetry under $(\varepsilon,G)\mapsto(-\varepsilon,-G)$ removes
odd expected orders. Smooth test functions have a weak remainder
$O_{N,f}(\varepsilon^6)$. Such constants are not asserted uniform in $N$.

The field $B_4$ differs from the Haar-reversible drift in FLOW-005.
In the bounded fixed-trace regime it adds $3p_1/4$ to the leading
first-trace drift, while its other terms are smaller there. It therefore
cannot simply be dropped even when normalized traces vanish.

## 3. A useful zero set

Both $J$ and $\mathbb EL_4$ vanish identically on $\operatorname{Tr}U=0$.
The faster field (4) moves eigenvalues by

$$
\dot z_j=\tfrac12(\bar m_1z_j^2-m_1). \tag{7}
$$

This is a common infinitesimal disk Möbius transformation of all points.
Consequently it can be removed on the Möbius quotient, rather than
subtracted by an arbitrary matrix drift. The
[Möbius reduction](coboundary_mobius_diffusion.md) makes this observation
quantitative and obtains an iterated-limit local theorem for repeated
uncentered random coboundary steps from a clock.

Neither construction removes noise from a deterministic quantum map.
The original finite step, a frozen-compensated step, the raw quadratic
diffusion and the Haar-reversible diffusion are distinct objects.
