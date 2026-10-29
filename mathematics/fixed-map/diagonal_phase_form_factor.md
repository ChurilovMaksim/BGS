# Diagonal random-phase form factor at times one, two and three

**Claim ID:** `BGS-TRACE-127`.
**Status:** project proof. The path sum is an exact counting argument. Python and C++ recompute it, in floating point, on every odd modulus in the certificate and match the closed forms. They also recompute the integer kernels. A Lean 4.33.1 module decides the matrix factorizations and the integer comparisons. It does not formalize the path count. No external referee.

The identity \(|\operatorname{Tr} M_N^m|^2=\lvert\ker(S^m-I)\rvert\) is the trace-closure lemma of `BGS-TRACE-126`, Section 3. No other statement from that note is used. `BGS-TRACE-005` and `BGS-BGS-001` remain **open**.

## 1. Statements

Let \(N\ge 1\) and let \(M\) be an \(N\times N\) complex matrix with \(\lvert M_{ab}\rvert=N^{-1/2}\) for every row \(a\) and column \(b\). Let \(\varphi_0,\ldots,\varphi_{N-1}\) be independent and uniform on \(\mathbb R/2\pi\mathbb Z\), and let \(D\) be the diagonal unitary \((D\psi)(a)=e^{i\varphi_a}\psi(a)\). Set \(U=DM\). Write \(\mathbb E\) for the normalized Haar integral on this \(N\)-torus.

**Theorem 1 (flat matrices).** For every integer \(m\ge 1\),
\[
\mathbb E\lvert\operatorname{Tr} U^m\rvert^2\le m!.
\]
The first two times are exact:
\[
\mathbb E\lvert\operatorname{Tr} U\rvert^2=1,
\qquad
\mathbb E\lvert\operatorname{Tr} U^2\rvert^2=\frac{2N-1}{N}.
\]
In particular the time-two value is strictly larger than \(1\) for every \(N\ge 2\), and it is at most \(2\).

Let \(N\ge 3\) be odd and let \(M_N\) be the cat-map quantization of `formalization/Bgs/TraceStatement.lean`:
\[
(M_N)_{xy}=N^{-1/2}\,e_N\bigl(-8^{-1}(3x^2-2xy+3y^2)\bigr).
\]
Every entry has modulus \(N^{-1/2}\), so Theorem 1 applies to \(U_N=DM_N\). Let \(S=\begin{pmatrix}3&4\\2&3\end{pmatrix}\).

**Theorem 2 (cat map at time three).** For every odd \(N\ge 3\),
\[
\mathbb E\lvert\operatorname{Tr} U_N^3\rvert^2=\frac{6N^2-9N+4}{N^2}.
\]
The value is strictly larger than \(1\) and strictly smaller than \(6\).

**Theorem 3 (separation from the pure cat map).** For every odd \(N\ge 3\),
\[
\lvert\ker(S^2-I)\rvert=1,
\qquad
\lvert\ker(S^3-I)\rvert=
\begin{cases}
49 & \text{if }7\mid N,\\
1 & \text{otherwise.}
\end{cases}
\]
The trace-closure lemma gives \(\lvert\operatorname{Tr} M_N^m\rvert^2=\lvert\ker(S^m-I)\rvert\). Therefore:

- at time \(2\), the diagonal-phase value \((2N-1)/N\) is strictly larger than the pure value \(1\);
- at time \(3\), if \(7\) does not divide \(N\), the diagonal-phase value is strictly larger than the pure value \(1\);
- at time \(3\), if \(7\) divides \(N\), the pure value is \(49\) and the diagonal-phase value is strictly smaller than \(6\).

**Boundary.** The diagonal phases are independent at the \(N\) sites. They are not the \(16\) mode-pair phases of `BGS-TRACE-126`, and \(U_N\) is not the fixed kick at \(\tau=10^{-80}\). The time-three limit \(6\) is not the CUE value \(3\), and the time-two value tends to \(2\), which is the CUE value at time two and not the COE value \(4\). No symmetry class is identified. The bound \(m!\) lies above \(N^2\) once \(m\) is large, so it does not separate a revival at Heisenberg time. Nothing is claimed for \(m\ge 4\) except the factorial bound. Section 6 records a finite sample of the \(16\)-phase ensemble; that sample is not an evaluation of its expectation and not a limit. `BGS-TRACE-005` and `BGS-BGS-001` remain open.

## 2. Occupation buckets

The entries of \(U\) are \(U_{ab}=e^{i\varphi_a}M_{ab}\). For \(m\ge 1\),
\[
\operatorname{Tr} U^m
=\sum_{x_0,\ldots,x_{m-1}}
\exp\Bigl(i\sum_{t=0}^{m-1}\varphi_{x_t}\Bigr)
\prod_{t=0}^{m-1}M_{x_t x_{t+1}},
\]
with \(x_m=x_0\). A closed word \(x=(x_0,\ldots,x_{m-1})\) has occupation \(n_x(a)=\#\{t:x_t=a\}\). Independence of the phases gives
\[
\mathbb E\exp\Bigl(i\sum_a\bigl(n_x(a)-n_y(a)\bigr)\varphi_a\Bigr)
=1
\]
if \(n_x=n_y\), and equals \(0\) otherwise, because each integral is the integral of a character \(e^{ik\theta}\) over the circle. Therefore
\[
\mathbb E\lvert\operatorname{Tr} U^m\rvert^2
=\sum_n\Bigl\lvert\sum_{x:\,n_x=n}A(x)\Bigr\rvert^2,
\]
where the outer sum runs over occupations of total mass \(m\) and \(A(x)=\prod_t M_{x_t x_{t+1}}\).

Every word has \(\lvert A(x)\rvert=N^{-m/2}\). The words with a fixed occupation are the distinct fillings of that multiset, so there are at most \(m!\) of them. If a bucket contains \(s\) words, the squared modulus of their sum is at most \(s\sum\lvert A\rvert^2\). Summing over buckets and using \(s\le m!\) gives
\[
\mathbb E\lvert\operatorname{Tr} U^m\rvert^2
\le m!\sum_x\lvert A(x)\rvert^2
=m!\,N^m\cdot N^{-m}
=m!.
\]
This is the factorial bound in Theorem 1.

## 3. Times one and two

At time one the words are single sites. The bucket of site \(a\) contains only \((a)\), with amplitude \(M_{aa}\), so
\[
\mathbb E\lvert\operatorname{Tr} U\rvert^2=\sum_a\lvert M_{aa}\rvert^2=\sum_a N^{-1}=1.
\]

At time two a word is a pair \((a,b)\).

If \(a=b\), the bucket contains one word and the contribution is \(\lvert M_{aa}\rvert^4=N^{-2}\). The \(N\) diagonal buckets contribute \(N^{-1}\).

If \(a\neq b\), the bucket of the unordered pair \(\{a,b\}\) contains the two words \((a,b)\) and \((b,a)\). Their amplitudes are \(M_{ab}M_{ba}\) and \(M_{ba}M_{ab}\), which are equal. The sum of the amplitudes has squared modulus \(4\lvert M_{ab}\rvert^2\lvert M_{ba}\rvert^2=4N^{-2}\). There are \(N(N-1)/2\) such buckets, contributing \(2(N-1)/N\).

The total is
\[
\frac{1}{N}+\frac{2(N-1)}{N}=\frac{2N-1}{N}.
\]
For \(N\ge 2\) one has \(N<2N-1\), so the value is strictly larger than \(1\), and \(2N-1\le 2N\), so the value is at most \(2\). The argument uses the common modulus of the entries and the commutativity of the product of two scalars. It does not use the phases of \(M\).

## 4. Time three for the cat map

A word of length three is a triple \((a,b,c)\), with amplitude \(M_{ab}M_{bc}M_{ca}\).

**One site.** The bucket of \((a,a,a)\) contributes \(\lvert M_{aa}\rvert^6=N^{-3}\). The \(N\) buckets contribute \(N^{-2}\).

**Two sites.** Fix \(a\neq b\). The bucket with occupation \(2\) at \(a\) and \(1\) at \(b\) contains the three words \((a,a,b)\), \((a,b,a)\) and \((b,a,a)\). Each product is \(M_{aa}M_{ab}M_{ba}\). The squared modulus of the sum is \(9N^{-3}\). There are \(N(N-1)\) ordered pairs \((a,b)\), contributing \(9(N-1)/N^2\). This step uses only the common modulus.

**Three sites.** Let \(a,b,c\) be distinct. The six words on this set split into the two cyclic orders. The three rotations of \((a,b,c)\) each contribute
\[
P_+=M_{ab}M_{bc}M_{ca},
\]
and the three rotations of \((a,c,b)\) each contribute
\[
P_-=M_{ac}M_{cb}M_{ba}.
\]
Write \(Q(x,y)=3x^2-2xy+3y^2\) and \(\alpha=-8^{-1}\) in \(\mathbb Z/N\mathbb Z\). The exponent of \(M_{xy}\) is \(\alpha Q(x,y)\). As integer polynomials,
\begin{align*}
Q(a,b)+Q(b,c)+Q(c,a)
&=6a^2+6b^2+6c^2-2ab-2bc-2ca,\\
Q(a,c)+Q(c,b)+Q(b,a)
&=6a^2+6b^2+6c^2-2ac-2cb-2ba.
\end{align*}
The cross terms agree, so the two sums of \(Q\) are equal as integers, hence modulo \(N\). Multiplication by \(\alpha\) preserves the equality. The prefactor \(N^{-1/2}\) is the positive square root in the quantization, so \(P_+=P_-\). The six amplitudes therefore sum to \(6P_+\), and the squared modulus is \(36N^{-3}\).

The number of unordered triples is \(N(N-1)(N-2)/6\), contributing \(6(N-1)(N-2)/N^2\).

Adding the three types,
\begin{align*}
\mathbb E\lvert\operatorname{Tr} U_N^3\rvert^2
&=\frac{1+9(N-1)+6(N-1)(N-2)}{N^2}
=\frac{6N^2-9N+4}{N^2}.
\end{align*}
The numerator gap factors as \(5N^2-9N+4=(5N-4)(N-1)\). For \(N\ge 3\) both factors are positive, so the value is strictly larger than \(1\). The same numerator is strictly smaller than \(6N^2\), so the value is strictly smaller than \(6=3!\).

The phase identification uses the quadratic form of this \(M_N\). The counting of one-site and two-site buckets does not. A flat matrix whose two triangle products fail to agree is not covered by the closed form.

## 5. Kernels

A direct product gives \(S^2=\begin{pmatrix}17&24\\12&17\end{pmatrix}\), so
\[
S^2-I=\begin{pmatrix}16&24\\12&16\end{pmatrix},
\qquad
\det(S^2-I)=16\cdot 16-24\cdot 12=-32.
\]
For odd \(N\), \(-32\) is a unit in \(\mathbb Z/N\mathbb Z\). The adjugate then inverts \(S^2-I\) over \((\mathbb Z/N\mathbb Z)^2\), and the kernel has one element.

The same multiplication gives \(S^3=\begin{pmatrix}99&140\\70&99\end{pmatrix}\). With \(A=\begin{pmatrix}7&10\\5&7\end{pmatrix}\),
\[
14A+I=S^3,
\qquad
\det A=49-50=-1.
\]
Thus \(A\in\mathrm{GL}(2,\mathbb Z)\) and \(S^3-I=14A\). On \((\mathbb Z/N\mathbb Z)^2\) the kernel of \(S^3-I\) is the kernel of multiplication by \(14\). Each coordinate contributes \(\gcd(14,N)\) solutions, so the kernel has order \(\gcd(14,N)^2\). Here \(14=2\cdot 7\). For odd \(N\) the factor \(2\) is a unit, and \(14\) contributes only one factor of \(7\), so
\[
\gcd(14,N)=
\begin{cases}
7 & \text{if }7\mid N,\\
1 & \text{otherwise.}
\end{cases}
\]
The kernel therefore has order \(49\) or \(1\). It does not grow with the exponent of \(7\): at \(N=49\) the order is still \(49\), not \(7^4\).

Theorem 3 follows from these orders and the trace-closure lemma. The comparison with the diagonal-phase values is the pair of strict inequalities in Theorem 2. When \(7\) divides \(N\) the pure value is exactly \(49\), which is larger than \(6\).

The direction of the time-three comparison changes according as \(7\) divides \(N\). At \(N=7\) the pure squared trace is \(49\) and the diagonal-phase value is \(235/49\). The same dimension is the scalar identity \(A_7=(9/10)I\) for the \(32\)-mode symbol; that identity is not used here, and the diagonal phases do not fold to a scalar.

## 6. The sixteen-phase ensemble, as a sample

The ensemble of `BGS-TRACE-126` puts one uniform phase on each of the \(16\) mode pairs and keeps those phases fixed along the orbit. Section 1 does not evaluate it. Outside the window \(m B\lvert\eta\rvert\le 1\), a CUE identification \( \mathbb E_\varphi\lvert\operatorname{Tr} U^m\rvert^2=\min(m,N) \) was tested numerically and is not adopted.

The probe builds \(U(\eta,\varphi)=\exp(i\eta A_N(\varphi))M_N\) from the same Weyl symbol as `BGS-TRACE-126`, draws phases from one splitmix generator with seed \(20261029\), and averages \(\lvert\operatorname{Tr} U^m\rvert^2\) by matrix powers. Python and C++ run that generator on the same \(24\) draws at \(\eta=2\), for \(N\in\{3,5,7,11,31\}\) and times \(1\) through \(6\). The printed means agree to twelve digits. Two rows are enough to show why a CUE identification is not made:

- at \(N=7\), time \(3\), the sample mean is \(44.632431403503\), against the pure revival \(49\) and against \(\min(3,7)=3\);
- at \(N=31\), time \(5\), the sample mean is \(47.417022055369\). The same programs compute \(\lvert\ker(S^5-I)\rvert=1\) at this prime, so the spike is not the kernel spike, and it is several times \(\min(5,31)=5\).

A wider Python scan, not repeated entrywise in C++, shows arithmetic revivals of size \(N^2\) falling once \(\eta\) is of order \(1\) or larger, except at dimension \(7\), and it shows other pairs \((N,m,\eta)\) with the same kind of spike. Those rows are properties of the recorded samples. They are not a proved lower bound on the expectation, and they are the reason this note does not identify the sixteen-phase form factor with the CUE or COE ramp.

## 7. Self-audit

The time-two count was checked against the closed form before the time-three count was trusted. Replacing the six triangle words by three would replace the limit \(6\) by a different rational; the enumeration rejects that replacement. The one-site and two-site buckets were not given the cat-map phase identity, because their amplitudes agree for every flat matrix.

The factorial bound counts fillings of a multiset, not primitive orbits. It is attained in the large-\(N\) limit at times one and two, and the time-three value tends to \(6\), but the same limit is not claimed at time four. A separate Monte Carlo at time four, not part of the certificate, increases only slowly with \(N\) and stays far below \(24\). The bound \(m!\) is therefore not presented as sharp for \(m\ge 4\).

Nat subtraction is not used for the gap. The factored form \((5N-4)(N-1)\) is an identity in \(\mathbb Z\), checked in Lean over \(\mathbb Z\). A first draft of the kernel set \(\lvert\ker(S^3-I)\rvert=7^{2v_7(N)}\). That counts every factor of \(7\) in \(N\). The coefficient in \(S^3-I=14A\) has only one factor of \(7\), so the kernel stays of order \(49\) at \(N=49\). The brute-force count in the verifiers caught the draft: at \(N=49\) it returns \(49\), not \(2401\).

The trace-closure input is not re-proved. The verifiers compare the literal squared trace of \(M_N^m\) with the kernel count; that comparison is a finite check of the cited lemma, not a second proof.

Section 6 does not say that the sixteen-phase expectation equals the printed sample mean. It does not say that the expectation tends to \(\min(m,N)\). A single large sample at \(N=31\), \(m=5\), \(\eta=2\) is compatible both with a finite-\(N\) resonance that disappears as \(N\to\infty\) and with a limit that is not CUE. Neither alternative is proved.

No external theorem is used as a lemma. Averages over diagonal unitaries have a graphical calculus in the literature; that calculus is not an input. The Haar form factor of \(U(N)\) is not an input. The Keating–Mezzadri discussion of one shear and of two orthogonal shears is background for why a CUE guess was tested in Section 6. It is not a lemma, and the test did not adopt the guess.

## 8. Certificates

- `computations/verification/diagonal_phase_form_factor.py`
- `computations/cpp/diagonal_phase_form_factor.cpp`
- `formalization/Bgs/DiagonalPhaseFormFactorRational.lean`
- `evidence/executions/20261029/diagonal-phase-form-factor/README.md`

Lean decides \(S^2\), \(S^3\), \(\det(S^2-I)=-32\), the factorization \(S^3-I=14A\) with \(\det A=-1\), the identity \((5N-4)(N-1)=5N^2-9N+4\), the strict gaps at times two and three, and the comparison with \(6\). Python and C++ enumerate the occupation sum at times \(1\), \(2\) and \(3\) for every odd modulus in the receipt, including \(3\), \(5\) and \(7\), and match the closed forms. They recompute both kernels. They recompute one common sixteen-phase sample. A pass does not prove `BGS-TRACE-005` or `BGS-BGS-001`.
