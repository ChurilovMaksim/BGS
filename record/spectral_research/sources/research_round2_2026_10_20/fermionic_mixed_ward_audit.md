> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/fermionic_mixed_ward_audit.md`. Embedded SHA256: `48d5eb8c02321dba100ae6224c01944e1771d42fac7d9cf66ead104ef331029d`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the mixed quantum return identities

Research continuation, 20 October 2026.

Audited input:

adversarial_quantum_return_mixed_ward.md

SHA-256:
53837a219e2a77acc8e2b08921c33ccf5a8eb89d8b6a15f333df360b5593b749.

The entire input was read independently. Verdict: **PASS**.
No correction is required. This audit does not claim the original
spectral-statistics problem has been solved.

## 1. The mixed finite telescope

With the input notation, put
$$
H_j^{(k)}=b(D^*)^jD^{j+k}b.
$$
The identity $B^*B=I-D^*D$ gives
$$
F_m^*F_{m+k}=H_{m-1}^{(k)}-H_m^{(k)}.
$$
For $k>0$, $A^*F_k=-H_0^{(k)}$; for $k=0$,
$A^*A=I-H_0^{(0)}$. Thus the distinction at $k=0$ in
the input is essential and correctly retained.

The error estimate uses two Hilbert--Schmidt factors:
$$
\|H_M^{(k)}\|_1
\le\|D^Mb\|_{\rm HS}\|D^{M+k}b\|_{\rm HS}
\le e_M.
$$
The identity $e_M=\|BD^M\|_{\rm HS}^2$, used for the reversed
telescope, also holds: both sides equal
$\|D^M\|_{\rm HS}^2-\|D^{M+1}\|_{\rm HS}^2$.

All unweighted mixed series converge absolutely in trace norm by
Hilbert--Schmidt Cauchy--Schwarz and the exact return energy.
The Abel telescope has coefficient $1-r^2$ and starting index
$j=0$, exactly as in the input. Its Heisenberg-scale error bound
is $O(1)$, without any unsupported $o(1)$ assertion.

## 2. The weighted identity

Finite summation by parts gives
$$
\sum_{m=1}^M mF_m^*F_{m+k}
=\sum_{j=0}^{M-1}H_j^{(k)}-MH_M^{(k)}.
$$
Weighted Cauchy--Schwarz bounds the full trace-norm series by the
dimension of the seen space. Hence the passage to its trace is
legitimate. Cyclicity gives
$$
\operatorname{Tr}H_j^{(k)}
=\operatorname{Tr}\bigl(D^kD^jE(D^*)^j\bigr).
$$
The second defect telescope
$$
\sum_{j\ge0}D^jE(D^*)^j=P_{\rm seen}
$$
therefore proves exactly
$$
\sum_{m\ge1}m\operatorname{Tr}(F_m^*F_{m+k})
=\operatorname{Tr}(D^kP_{\rm seen}).
$$
The formula includes $k=0$. No uniform remainder at $M\asymp N$
is inferred.

## 3. Insertions and the $k=0$ endpoint

The series defining $Z_X$ is zero on the dark space and converges
on the seen space. Its Stein equation and uniqueness follow by
iteration. The contraction estimate applies to non-Hermitian
$X$ as well: the displayed Cauchy--Schwarz proof does not assume
positivity of $X$.

If $[X,E]=0$, then $X$ commutes with $a$ and $b$, so
$$
B^*XB=X-D^*XD+(U^*XU-X).
$$
For $k>0$, the initial term is
$$
A^*XF_k=-bXD^kb,
$$
which cancels the initial term of the telescope. For $k=0$,
$$
A^*XA=aXa=X-bXb;
$$
the telescope restores $bXb$, leaving exactly $X$.
Thus equation (5.6) of the input has the correct endpoint in both
cases. The commutator sum is left unevaluated, as it must be.

The scalar trace identity and the two-sided Hilbert--Schmidt
Parseval identity in (5.4) follow from pointwise unitarity of the
boundary transfer function. Their use does not assert that an
individual inserted Fourier coefficient vanishes.

## 4. The positive open Abel lower bound

For an invertible contraction $D$, let its eigenvalues be
$r_j e^{i\theta_j}$ and $d_j=-\log r_j$.
The full two-sided power sum is a sum of positive Poisson kernels:
$$
N^2+2\sum_{m\ge1}e^{-2sm/N}|\operatorname{Tr}D^m|^2
=\sum_{i,j}P_{e^{-2s/N}r_ir_j}(\theta_i-\theta_j).
$$
Dropping the off-diagonal terms is valid here because each
Poisson kernel is positive, not because the individual power
cross terms have a fixed sign. The diagonal terms are
$\coth(s/N+d_j)$. Convexity of $\coth$ gives the stated
normalization
$$
\frac12\left\{N^{-1}\coth((s+c_D)/N)-1\right\}.
$$

For $\operatorname{Tr}E\le1/4$,
$\det(I-E)\ge1-\operatorname{Tr}E\ge3/4$, so
$$
c_D=-\tfrac12\log\det(I-E)<1/6.
$$
At $s=1/4$, strict $\coth x>1/x$ gives the strict lower bound
$7/10$, for every dimension. The concrete Fourier-window
detector satisfies the trace hypothesis exactly. The proof
controls the entire infinite Abel tail and makes no unjustified
claim about an individual finite time band.

## 5. The determinant and coefficient ordering

Both eliminations of the block determinant in Section 7 give
the same matrix, and
$$
D+b(I+a)^{-1}B=U.
$$
The sign in the logarithmic derivative is consequently correct.
Writing $R=(I+a)^{-1}$ and $Q(z)=\sum_{m\ge1}z^mF_m$,
$$
I-\Theta(z)=(I+a)(I-RQ(z)).
$$
Coefficient extraction from
$-\log\det(I-RQ)=\sum_{j\ge1}\operatorname{Tr}(RQ)^j/j$
gives exactly the ordered products
$$
\frac{m}{j}\operatorname{Tr}(RF_{n_1}\cdots RF_{n_j}).
$$
For a given coefficient the expansion is finite; convergence
near the unit circle is not used.

The final norm identity correctly retains the interference
between the open traces and the feedback coefficients. The
new positive open lower bound does not imply a lower bound for
the original full spectral statistic.
