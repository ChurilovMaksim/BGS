> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_dual_coherent_fejers.md`. Embedded SHA256: `2c7f66b1a47f0674d81f95016623c10bd51abbc6b519a4e47d331d09b556be42`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit: coherent Weyl participation and finite Fejér averages

Date: 21 October 2026.

## 0. Verdict and frozen input

**Primary verdict: proved as written.** Theorem D, its fixed-label witness, the extraction of a finite time beyond `N`, and the aggregate interference lower bound all follow with the constants stated in the frozen source. No first missing estimate was found.

Primary source:

- `research_round4_2026_10_21/dual_coherent_participation_and_fejers.md`;
- SHA-256 `8a0779ea28cd664bf207e50fa2c71f908479b2dd1f5bacde414a87e3352825d1`.

The full source was read and its hash checked. Its sole substantive family-specific input is the explicit minorization proved in the frozen dual-Weyl source `90cb06de5c56441dfdb17f6fa32a35484b00c7919bbddd899fb8954f950043c1`, independently audited in `audit_dual_weyl_primitivity_quantitative.md`, SHA-256 `fee116da2d8d0611ac624b3815212803c223774edcf4a5ec1997efc058e95dac`.

All new Schur-product, Fejér, rank, and finite-time steps are independently reconstructed below. The conclusion concerns squared Weyl return amplitudes. It does not evaluate the complex adjoint trace appearing in the original pair statistic.

## 1. Dimensions and the commutant participation formula

The source now defines `C` explicitly as the adjoint matrix restricted to the `M=N^2-1` nonzero Weyl labels. This resolves the full-versus-restricted notation issue in the earlier auxiliary discussion. Throughout this audit, `P=|C|^(circ 2)` and `Z_n=|C^n|^(circ 2)` are `M` by `M` matrices.

If the original unitary has distinct eigenvalues `eta` with multiplicities `m_eta`, its full adjoint fixed space has dimension `sum_eta m_eta^2`. Restricting to traceless matrices removes exactly the scalar line, so

$$
r=\dim\ker(C-I)=\sum_\eta m_\eta^2-1\ge N-1.
\tag{1.1}
$$

This holds without spectral simplicity. For a traceless matrix `X`, the orthogonal fixed-space projection is `sum_eta R_eta X R_eta`; this preserves the trace. On a nonzero Weyl mode, its squared normalized Hilbert–Schmidt norm is

$$
q_v=\frac1N\sum_\eta\|R_\eta W(v)R_\eta\|_{\mathrm F}^2
=\frac1N\sum_{j,k:\eta_j=\eta_k}
|\langle\psi_j,W(v)\psi_k\rangle|^2.
\tag{1.2}
$$

The factor `1/N` is correct: `sqrt(N)|psi_j><psi_k|` is orthonormal for the inner product `N^-1 Tr(X*Y)`. No scalar component survives because `Tr W(v)=0`.

Since these numbers are the diagonal entries of an orthogonal projector of rank `r`, they lie in `[0,1]` and sum to `r`. A label maximizing them has `q>=r/M` and can be chosen once for the given `N`, independently of the averaging time.

## 2. Exact Fejér identity and the matrix-order lower bound

Write the distinct spectral decomposition `C=sum_lambda lambda Q_lambda`, with ranks `r_lambda`. For every integer `n`, direct entrywise expansion gives

$$
Z_n=\sum_{\lambda,\mu}(\lambda\overline\mu)^n
Q_\lambda\circ\overline{Q_\mu}.
\tag{2.1}
$$

As `C` is unitary, `C^-n=(C^n)*` and `Z_-n=Z_n^t`. The normalized scalar Fejér kernel obeys

$$
\Phi_T(z)=\frac1T\sum_{|n|<T}(1-|n|/T)z^n
=\left|\frac1T\sum_{j=0}^{T-1}z^j\right|^2\ge0
\tag{2.2}
$$

for `|z|=1`. The factor `1/T` outside the weighted sum is essential and is present. Expanding the squared geometric sum counts `T-|n|` pairs at difference `n`; it also gives `Phi_T(1)=1` and convergence to zero at each fixed `z!=1`.

Each matrix `Q_lambda circ conjugate(Q_mu)` is positive semidefinite. Conjugation preserves positive semidefiniteness, and the entrywise product of two Gram matrices is the Gram matrix of the tensor products of their representing vectors. This proves the needed Schur positivity directly, including unequal eigenvalues.

Substitution into the finite average therefore gives

$$
\mathscr Z_T=\sum_{\lambda,\mu}\Phi_T(\lambda\bar\mu)
Q_\lambda\circ\overline{Q_\mu}
\succeq\mathscr Z_\infty
:=\sum_\lambda Q_\lambda\circ\overline{Q_\lambda}.
\tag{2.3}
$$

The lower bound holds for every positive integer `T`; it does not require a quantitative separation of eigenvalues. The finite sum also proves convergence to the indicated limit. This limit is real, symmetric, positive semidefinite, and doubly stochastic: the column sum of `|Q_lambda|^2` is `(Q_lambda)_(vv)`, and the projectors sum to the identity. Thus the constant vector has eigenvalue one and the orthogonal complement has nonnegative eigenvalues. Consequently `mathscr Z_infty succeq Pi`, as claimed.

## 3. Trace floor and the same label for all times

For each projector, scalar Cauchy–Schwarz gives

$$
\sum_v(Q_\lambda)_{vv}^2\ge r_\lambda^2/M.
$$

The nonzero ranks are positive integers summing to `M`. The rank at one is `r`, so their squared sum is at least `r^2+(M-r)`. Taking traces in (2.3) proves

$$
\operatorname{Tr}\mathscr Z_T
\ge1+\frac{r(r-1)}M
\ge1+\frac{N-2}{N+1}.
\tag{3.1}
$$

This is the asserted `1+gamma_N` bound. Other degeneracies only increase the rank-square lower bound.

The fixed-label assertion is stronger than simply choosing a new large diagonal entry at each `T`, and was checked separately. Let the chosen label maximize the fixed-projector weight `q_v`, so `q>=r/M`. Primitivity implies `r<M`: if `r=M`, then `C=I` and `P=I`, contradicting the positive minorization on dimension `M>1`.

There are at most `M-r` distinct other eigenvalues. Their participation weights at this label sum to `1-q`, so

$$
(\mathscr Z_\infty)_{vv}
\ge q^2+\frac{(1-q)^2}{M-r}.
\tag{3.2}
$$

The right side is increasing for `q>=1/(M-r+1)`. The available lower bound lies in this interval, because

$$
r/M\ge1/(M-r+1)
\quad\Longleftrightarrow\quad(r-1)(M-r)\ge0.
$$

Inserting `q=r/M` into (3.2) gives

$$
(\mathscr Z_T)_{vv}
\ge\frac1M+\frac{r(r-1)}{M^2}
\ge\frac{1+\gamma_N}{M}.
\tag{3.3}
$$

The first inequality uses the diagonal consequence of (2.3). This proves the same witness label works for every `T`.

## 4. The effective Markov estimate

The exact minorization is `P^L=aPi+(1-a)Q`, with `L=6N^2`, `0<a<1`, and doubly stochastic `Q`. Every nonnegative doubly stochastic matrix is a Euclidean contraction: apply weighted Cauchy–Schwarz in each row and then use the column sums. It commutes with `Pi` and acts as the identity on the constant vector.

For `n=jL+s`, `0<=s<L`, expand powers of the minorization to obtain

$$
P^n-\Pi=(1-a)^jP^sQ^j(I-\Pi).
$$

All remaining factors have operator norm at most one, so

$$
\|P^n-\Pi\|_{2\to2}\le(1-a)^{\lfloor n/L\rfloor}.
\tag{4.1}
$$

The same estimate holds after transpose. The Fejér coefficients have total mass one, and `sum_(n>=0)(1-a)^floor(n/L)=L/a`. Therefore

$$
\|\mathscr P_T-\Pi\|_{2\to2}
\le\frac1T\left[1+2\sum_{n=1}^{T-1}
(1-n/T)(1-a)^{\lfloor n/L\rfloor}\right]
\le\frac{2L}{aT}.
\tag{4.2}
$$

It follows that its trace is at most `1+2ML/(aT)` and each diagonal entry is at most `1/M+2L/(aT)`. This does not assume `mathscr P_T-Pi` is positive semidefinite.

For

$$
T_N=\left\lceil\frac{4ML}{a\gamma_N}\right\rceil,
$$

equations (3.1), (3.3), and (4.2) prove, for every `T>=T_N`,

$$
\operatorname{Tr}(\mathscr Z_T-\mathscr P_T)\ge\gamma_N/2,
\qquad
(\mathscr Z_T-\mathscr P_T)_{v_Nv_N}\ge\gamma_N/(2M).
\tag{4.3}
$$

All constants agree with the frozen source.

## 5. Extracting a time in the claimed finite interval

Put `d_n=Tr Z_n-Tr P^n`. Both traces lie in `[0,M]`, hence `|d_n|<=M`. Also `d_0=d_1=0`. At `T=T_N`, the trace difference in (4.3) equals

$$
\frac2{T_N}\sum_{n=1}^{T_N-1}(1-n/T_N)d_n.
\tag{5.1}
$$

The total contribution of `n<N` is at most `2M(N-1)/T_N`. The displayed definition of `T_N` implies this is at most `gamma_N/4`, since `L/a>=6N^2>=2(N-1)`. Hence the sum over `N<=n<T_N` is at least `gamma_N/4`. Its nonnegative weights sum to at most one. At least one such time therefore satisfies

$$
\operatorname{Tr}Z_n-\operatorname{Tr}P^n\ge\gamma_N/4.
\tag{5.2}
$$

The analogous fixed-label argument uses the bound one instead of `M` for the absolute diagonal difference, and yields a possibly different time with diagonal difference at least `gamma_N/(4M)`. No simultaneous choice of those two times is claimed.

The time bound is explicit through the earlier `a_N`, but it can be far larger than `N`. The lower endpoint `N` does not turn this into a result at times proportional to `N`.

## 6. Interference accumulation and its trace-norm consequence

The path expansion is exact:

$$
Z_{n+1}=PZ_n+\mathcal E_n.
$$

Here the error is the sum over unequal intermediate path labels. Both row and column sums vanish because it is the difference of two doubly stochastic matrices; `mathcal E_0=0`. Iteration gives

$$
Z_n-P^n=\sum_{j=1}^{n-1}P^{n-1-j}\mathcal E_j.
\tag{6.1}
$$

Substitution into (4.3) proves the signed aggregate lower bound in source (6.4) with no missing scalar mode, since every matrix in this note is restricted to the same label set.

For its trace-norm consequence, column sums zero give `Pi mathcal E_j=0`. Thus, by (4.1) and the elementary singular-value trace inequality,

$$
|\operatorname{Tr}(P^q\mathcal E_j)|
\le(1-a)^{\lfloor q/L\rfloor}\|\mathcal E_j\|_*.
$$

The Fejér coefficient is at most one. Summing first over `q=n-1-j` bounds the aggregate from above by

$$
\frac{2L}{aT}\sum_{j=1}^{T-2}\|\mathcal E_j\|_*.
$$

Its lower bound `gamma_N/2` therefore yields exactly

$$
\frac1T\sum_{j=1}^{T-2}\|\mathcal E_j\|_*
\ge\frac{a\gamma_N}{4L},\qquad T\ge T_N.
\tag{6.2}
$$

This is an explicit, though very small, lower bound on the omitted coherent errors. The argument does not infer smallness from their zero row and column sums.

## 7. Relation to the requested spectral statistic

The return quantity here is `Tr Z_n=sum_v |(C^n)_(vv)|^2`. The normalized Weyl inner product gives exactly the factor `1/N^2` in its original-matrix formula in source (7.1). The original pair statistic instead uses

$$
\operatorname{Tr}C^n=|\operatorname{Tr}U_N^n|^2-1.
$$

This is a sum of complex amplitudes, rather than the sum of their squared moduli. The source's pair-discrepancy formula correctly subtracts `min(n,N)-1`, so that the scalar modes cancel. Its upper Fourier endpoint may be included because a smooth compactly supported Fourier transform vanishes at its support boundary.

The proved persistent Fejér contribution therefore does not transfer to `H_diag`. It is a rigorous limitation on replacing exact coherent Weyl probabilities by repeated dephasing, with a finite but much too large time window. This is precisely the scope claimed in the frozen manuscript.
