# Direct attempt at the fixed-coupling spectral-statistics barrier

20 September 2026. Base git revision
`e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7`; parent checkpoint
`block-memory-20260919-frozen-symbol-doeblin-and-coherent-retention`.

**Outcome: the principal estimate was not proved. No breakthrough is
claimed.** This record preserves the executed calculations and the exact
points at which three proposed routes fail to close. It is not a new
article or a replacement of the original goal by auxiliary identities.
No tracked edit, commit or push.

## Target held fixed

Keep the prescribed U_N=exp(i tau N A_N)M_N, tau=10^-80. Scalar centering
of A_N does not change the target. Before all-k correlations, even the
following pair statement is missing: for every w in C_c^infinity(R),

\[
 R_N(w)=\frac1{N^2}\sum_{m\ne0}w(m/N)
  \bigl(|\operatorname{Tr}U_N^m|^2-\min(|m|,N)\bigr)\longrightarrow0.
\tag{1}
\]

The omitted m=0 terms agree exactly, both being N^2. This is the
weighted CUE trace comparison from the maintained Fourier bridge.
Neither strict positivity, absence of exact returns, nor a change of
quantization proves (1). No parameter or phase averaging is part of (1).

## Route 1: exact determinant resummation

Diagonalize the centered Hermitian A=Q diag(a_1,...,a_N)Q*, and put
B=Q*M Q. For a subset I define a_I=sum_(j in I) a_j and b_I=det B_(I,I).
The diagonalization need not be unique; the following identities hold
for every choice. The exact coefficients of det(I-z exp(i epsilon A)M)
are

\[
 c_k(\epsilon)=(-1)^k\sum_{|I|=k}b_Ie^{i\epsilon a_I},
 \qquad 0\le k\le N.
\tag{2}
\]

This follows by expansion into principal minors in the eigenbasis of A;
no stationary-phase approximation or growing-time remainder enters.
For real epsilon, unitarity gives exactly

\[
 c_{N-k}=c_N\overline{c_k},\qquad
 k c_k=-\sum_{j=1}^k c_{k-j}\operatorname{Tr}U^j.
\tag{3}
\]

Thus resummation reduces the independent secular data to k<=floor(N/2),
plus the determinant. It does not reduce the needed time scale to log N.
The products of coefficients still involve coherent weighted sums

\[
 |c_k(\epsilon)|^2
 =\sum_{|I|=|J|=k}b_I\overline{b_J}
     e^{i\epsilon(a_I-a_J)}.
\tag{4}
\]

**Attempted decisive step:** use (3) to cancel the I!=J contribution
at epsilon=tau N without estimating every term separately. No such
weighted cancellation was established. Absolute values destroy the
phases of the minors; replacing their products by independent random
variables changes the model.

This is consistent with the precise scope of Braun--Haake,
[*Chaotic maps and flows: Exact Riemann-Siegel lookalike for spectral
fluctuations*](https://arxiv.org/html/1206.4222v1), sections 2, 4 and 6:
the finite-unitary determinant identity is exact, but the spectral
evaluation uses periodic-orbit and diagonal-approximation arguments.
Their half-Heisenberg truncation is not a logarithmic-time estimate.
No uniform error bound for the fixed model was extracted from that work.

One cannot impose |c_k|^2 -> 1 for the single fixed operator as a
substitute: 1 is a CUE **expectation**, not a concentration statement.
Najnudel--Paquette--Simm, [Theorem 1.2](https://arxiv.org/pdf/2011.01823),
in fact prove that the middle CUE coefficient tends to zero in
probability, despite its unit second moment. The code's reference
value is labelled as a mean only. No individual secular-coefficient
limit is promoted to a necessary or sufficient BGS criterion here.

## Route 2: replace the fixed phases by independent phases

For independent uniform t_j on the circle, (2) gives

\[
 \mathbb E_{\mathbf t}\left|\sum_{|I|=k}b_I
                       e^{i\sum_{j\in I}t_j}\right|^2
 =\sum_{|I|=k}|b_I|^2.
\tag{5}
\]

This average is exact but is a different model. Averaging the actual
single parameter epsilon over [epsilon_0-L,epsilon_0+L] instead gives

\[
 \sum_{I,J}b_I\overline{b_J}
 e^{i\epsilon_0(a_I-a_J)}
 \operatorname{sinc}\bigl(L(a_I-a_J)\bigr),
 \quad\operatorname{sinc}(x)=\sin(x)/x.
\tag{6}
\]

In particular, a fixed-N qualitative equidistribution argument cannot
silently replace (6) by (5) uniformly at k proportional to N.

Here is a direct scale check. Since ||A||<=F_0=593/500, all binomial(N,k)
subset energies a_I lie in [-kF_0,kF_0]. Pigeonholing, with exact
coincidences allowed, gives distinct I,J with

\[
 |a_I-a_J|\le\frac{2kF_0}{\binom Nk-1}.
\tag{7}
\]

For k=floor(N/2), the bound is O(N^(3/2)2^-N). Consequently, for
every fixed polynomial horizon L=N^b, there is a nontrivial subset
character whose actual interval-average modulus tends to one, while
its independent-phase average is zero. Use
sinc(x)>=1-x^2/6 to make this an explicit bound.

This disproves a proposed **uniform characterwise** phase replacement,
not a weighted determinant comparison: the associated minors could
have very small weights, or other terms could cancel. That remaining
weighted sum is exactly what was not estimated. Equation (7) is an
elementary pigeonhole observation, not a new small-divisor theorem.

There is a second scale mismatch. A classical-parameter window of
radius delta_N changes U in operator norm by at most F_0 N delta_N.
The direct eigenangle-path bound gives unfolded displacements at most
F_0 N^2 delta_N/(2 pi). If N^2 delta_N -> 0, every subset-difference
phase in (4), for k<=N/2, also changes by o(1) across the window.
Such a window preserves the spectrum by this sufficient norm criterion
but cannot create independent phases. This does not rule out every
possible use of structured parameter averaging; it rejects this
particular direct combination of bounds.

For context, Kieler--Fritzsch--Baecker,
[*Semiclassical foundation of universality in chaotic quantum circuits*](https://arxiv.org/pdf/2605.27052v1),
equations (2)--(9), use a spectral/time average and periodic-orbit
phase statistics in a multipartite model. Those inputs are not a
proved weighted estimate for (4) at the specified single tau.
That source therefore does not complete this transfer.

## Route 3: long-time prequantum trace formula

Faure--Tsujii's published monograph,
[*Prequantum transfer operator for symplectic Anosov diffeomorphism*](https://www.researchgate.net/profile/Frederic-Faure/publication/225091014_Prequantum_transfer_operator_for_symplectic_Anosov_diffeomorphism/links/58da9fa745851578dfc44c9b/Prequantum-transfer-operator-for-symplectic-Anosov-diffeomorphism.pdf),
provides a promising long-time trace construction. But Theorem 10.3.2,
printed pp.190--191, compares its quantum operator with a corrected
Toeplitz operator only to O(hbar^epsilon), epsilon>0 unspecified. The
comparison includes a conjugation and symbols in S_delta. Remark
10.3.5 describes almost unitarity, not exact unitarity. The arXiv v2
numbering is different: Theorems 1.38 and 1.69. No O(1/N) smooth
unitary-generator comparison with our frozen propagator was found.

The attempted transfer therefore cannot invoke
`../ergodic-transfer/ergodic_spectral_transfer.md`: that result requires
a factor exp(i Op(a)/N) with the specified fixed-symbol ergodic controls.
Even for two unitaries, an unspecified O(N^-epsilon) operator error
does not imply o(1) unfolded displacement; the direct estimate is
O(N^(1-epsilon)). Almost-unitary outer-band operators require an
additional justification as well. The required comparison was not
proved here. This is a failed import, not a defect asserted in the
source theorem.

## Executed checks and status

`exact_structure_checks.py` independently assembles the frozen A,M at
N=5,9 and checks (2)--(3) against direct characteristic polynomials and
matrix traces, with auxiliary epsilon=0.17,2.4. Maximum residual is
below 1.2e-14. It also verifies (5) by a complete two-point grid in all
independent phases; differences of 0/1 subset characters make that
grid exact algebraically. The near-zero original-tau rows are flagged
as below floating resolution and are not evidence of a resolved kick.

The scale comparisons from (7) use exact rational arithmetic through
N=10001. Decimal scientific strings preserve tiny positive values
instead of reporting floating underflow as an exact zero. None of
these checks establishes spectral universality at growing dimension.

The three routes were executed through their first load-bearing
implications. The decisive weighted phase estimate was not obtained;
no available result checked here supplies it. The next substantive
advance would need control of the weighted coherent sums, or a
different mechanism proving (1), not another characterwise estimate,
small-perturbation certificate, or unproved random-phase substitution.
The principal task is still open. Review in this attempt is self-review;
no new independent-agent or Lean certification is claimed.
