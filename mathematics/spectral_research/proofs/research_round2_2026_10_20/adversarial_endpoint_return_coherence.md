> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/adversarial_endpoint_return_coherence.md`. Embedded SHA256: `e7df95406b8a95cbb62a3da80820db7dcb9634b186267676db657c1991fdb362`.
> [Thematic guide](../../topics/dephasing.md).

# Endpoint cyclicity audit and nonvanishing weighted return coherence

20 October 2026. This is an independent audit of the new endpoint
cyclicity theorem, followed by a consequence for the original quantum
returns. It does not assert the required form factor or $H_{\rm diag}$.

## 1. Frozen inputs

| Input | SHA-256 |
|---|---|
| arithmetic_endpoint_cyclicity.md | 387243de3e23f5df546c999ef2d650a640e6b7c4d4488ea775765e3ae5362868 |
| arithmetic_padic_jacobi_simplicity.md | f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df |
| adversarial_quantum_return_mixed_ward.md | 53837a219e2a77acc8e2b08921c33ccf5a8eb89d8b6a15f333df360b5593b749 |

The first input has been read in full. Its proof passes the checks below.
No modification of any input was needed.

## 2. The additional bordered minors really are nonzero

Use the input's Jacobi order $x_j=(N+1)/2+j\pmod N$, gauge
$\omega=(-3+4i)/5$, real eigenvector matrix $\Phi$, and
$M_0=P^*M_NP$. The hypotheses are $N$ odd and $7\nmid N$.
For eigenvalue sets $|F|=k-1$, $|E|=k$, the bordered determinant is
that of $C_{F,E}$, with endpoint coordinate row adjoined, where
$C=\Phi^TD^{-1}M_0D\Phi$.

Two applications of Cauchy--Binet give
$$
H_{j_*;F,E}
=\epsilon_{j_*,k}
\sum_{\substack{|I|=|J|=k-1\\j_*\notin J}}
\det\Phi_{I,F}\det(M_0)_{I,J}
\det\Phi_{J\cup\{j_*\},E}\,
\omega^{j_*+\sum J-\sum I}.
$$
The cofactor sign is constant, because $j_*$ is an endpoint:
$(-1)^{k+1}$ at $j_*=0$, and $1$ at $j_*=N-1$.
The endpoint phase $\omega^{j_*}$ is included.

At the place with $v_+(\omega)=1$, the first endpoint has unique
extreme pair
$$
I_0=\{N-k+1,\ldots,N-1\},\qquad J_0=\{1,\ldots,k-1\}.
$$
At the conjugate place with $v_-(\omega)=-1$, the last endpoint has
unique extreme pair
$$
I_0=\{0,\ldots,k-2\},\qquad J_0=\{N-k,\ldots,N-2\}.
$$
Both Jacobi factors of each extreme summand are nonzero contiguous
endpoint minors. Its Fourier factor is a nonzero consecutive
Vandermonde. At either place, any other pair has positive integer
exponent gap $g$; the two Jacobi ratios lose at most $g/2$ in
valuation and the Fourier ratio loses nothing. The relative summand
valuation is therefore at least $g/2>0$.

The underlying bounds are valid at both places. The Jacobi coefficients
are integral there, and every nonzero edge has valuation in $[0,1/2]$.
The root-of-unity valuation and balanced-residue minimization used for
the Fourier factor do not distinguish these conjugate places. No
assumption that the endpoint coordinate is a valuation unit is used.
Dividing by the extreme term leaves a unit plus positive-valuation
terms. Thus both bordered determinants are nonzero, including $k=1$.
Passing to an orthonormal eigenbasis only multiplies rows and columns
by nonzero norms, so preserves this assertion.

## 3. Large-time observability and the exact parameter

Order the simple real eigenvalues of $A_N$ as $a_1>\cdots>a_N$.
In its orthonormal eigenbasis, write $B=Q^*M_NQ$ and
$b_k=\det B_{[1:k],[1:k]}\ne0$.
The two leading characteristic terms on scale $e^{ta_k}$ give
$$
\lambda_k(t)e^{-ta_k}\longrightarrow b_k/b_{k-1}\ne0
$$
as $t\to+\infty$; Rouché on a small fixed circle about the displayed
nonzero limit gives a simple root on each of the $N$ separate scales.

For a right eigenvector of $\operatorname{diag}(e^{ta_i})B$, delete
row $k$ and set coordinate $k$ to one. The remaining coefficient
matrix tends to
$$
\begin{pmatrix}B_{I,I}&B_{I,L}\\0&I_L\end{pmatrix},
\quad I=\{1,\ldots,k-1\},\quad L=\{k+1,\ldots,N\}.
$$
This matrix is invertible. Hence the normalization exists uniquely for
large $t$; since the full matrix is singular of rank $N-1$, its
deleted row is automatically satisfied. The vector tends to
$(-B_{I,I}^{-1}B_{I,k},1,0_L)$. Its physical endpoint coordinate is
the bordered minor divided by $b_{k-1}$, and is nonzero by Section 2.
The observable determinant is therefore a nonzero Vandermonde times
the product of these nonzero endpoint coordinates.

The observable determinant at $U_N(z)=e^{izNA_N}M_N$ is a finite
exponential polynomial with algebraic coefficients and frequencies.
Its large-real-time value at $z=-it/N$ shows it is not identically
zero. After equal frequencies have been collected, multiplication by
any nonzero algebraic $z$ leaves distinct algebraic exponents.
Lindemann--Weierstrass therefore forbids its vanishing at such $z$.
The precise version has been independently reopened: S. A. Popescu,
Theorem 3.2, author manuscript arXiv:2306.14352, printed pp. 14--15;
published chapter DOI 10.1007/978-3-031-51959-8_16. It requires
distinct algebraic exponents and algebraic coefficients; both
hypotheses are as just verified. It does not require rational
independence of the frequencies.

Finally,
$$
U_N(z)^*=U_N(\overline z)^{-1}.
$$
Adjoint observability at $\overline z$ gives the cyclic independence
of the inverse powers at $z$; multiplication by $U_N(z)^{N-1}$
and reversal of columns gives cyclicity of the positive powers.
This argument works for complex algebraic $z$, not only real $z$.

The resulting audited conclusion is exactly endpoint observability
and cyclicity at both $x_\pm=(N\pm1)/2$, for $7\nmid N$.
It says nothing about interior coordinate zeros or a quantitative
lower bound on any coordinate.

## 4. A mixed return correlation that cannot disappear

Take the original real parameter $\tau=10^{-80}$. Choose consecutive
coordinate and Fourier windows of equal cardinality
$$
r_N=s_N=\lfloor\sqrt N/2\rfloor,
$$
with the coordinate window centered at $q=1/2$, so that it contains
both endpoints for all sufficiently large odd $N$. Define the exact
effect and return matrices by
$$
E_N=P_{I_N}\mathcal F_N^*P_{J_N}\mathcal F_NP_{I_N},\quad
b_N=E_N^{1/2},\quad
D_N=(I-E_N)^{1/2}U_N,\quad
F_{m,N}=b_NU_ND_N^{m-1}b_N.
$$
The Fourier restriction is a square Vandermonde in distinct roots of
unity, up to nonzero row and column phases. Hence the restriction of
$E_N$ to the coordinate window is positive definite, and its range
is the entire coordinate window. Section 3 implies
$\mathcal H_{{\rm seen},N}=\mathbb C^N$ whenever $7\nmid N$.

The mixed Ward input, which is proved by finite telescoping, now gives
$$
\sum_{m\ge1}m\operatorname{Tr}(F_{m,N}^*F_{m+k,N})
       =\operatorname{Tr}D_N^k\qquad(k\ge0).
\tag{4.1}
$$
The series is absolutely convergent: Hilbert--Schmidt Cauchy--Schwarz
and the exact return sum $\sum_m m\|F_{m,N}\|_{\rm HS}^2=N$ bound its
sum of absolute values by $N$.

Also $\operatorname{Tr}E_N=r_Ns_N/N\le1/4$, so the elementary
Poisson/Jensen inequality of the same input yields
$$
\frac1{N^2}\sum_{k\ge1}e^{-k/(2N)}|\operatorname{Tr}D_N^k|^2
     >\frac7{10}.
$$
Substituting (4.1) proves the actual mixed-return statement
$$
\boxed{\displaystyle
\frac1{N^2}\sum_{k\ge1}e^{-k/(2N)}
\left|\sum_{m\ge1}m\operatorname{Tr}
              (F_{m,N}^*F_{m+k,N})\right|^2>\frac7{10}.}
\tag{4.2}
$$
This holds for every sufficiently large odd $N$ not divisible by
$7$, at the prescribed fixed parameter. The outer series is also
absolutely convergent, since its inner sum equals a contraction power
trace of modulus at most $N$.

Equation (4.2) rigorously rules out an $o(1)$ conclusion for this
specific normalized mixed-return functional. In particular, replacing
the weighted mixed trace by its purely diagonal-in-time counterpart
would discard a nonvanishing amount. The unweighted identity
$A^*F_k+\sum_mF_m^*F_{m+k}=0$ does not justify that replacement:
its time weight is different.

There is no claim that the required $U_N$ form factor is contradicted,
that a fixed finite band of $k$'s carries (4.2), or that all possible
mesoscopic return constructions fail. Nor is (4.2) extended to $7\mid N$:
the open power-trace inequality holds there, but the audited full
visibility assertion used in (4.1) has not been established there.
