# Round 12: direct spectral-measure route and its actual stopping point

## 0. Status

This branch did **not** obtain a new estimate for the original signed
Heisenberg-time pair functional. It did not prove or refute any instance
of the required `H_diag`. The work below records the attempted direct
spectral-measure route, a short exact test of what its available input
determines, and the point where the original matrix is still
uncontrolled. The auxiliary construction is not a counterexample to
the prescribed family.

The initial approach used Schur/OPUC completion. The root agent supplied
the simpler Fourier construction in Section 2, which makes further
OPUC completion work unnecessary. No novelty claim is made for this
elementary construction.

## 1. Actual input from the original matrices

Throughout this note

\[
 U_N=\exp(i10^{-80}NA_N)M_N,
 \qquad c_{j,N}=\langle e_0,U_N^j e_0\rangle.
\]

The complete raw source
`research_round7_2026_10_21/r7_return_all_fixed_powers_phase_separation.md`
was read, including Appendices A and B. Its needed conclusion is the
following: for each fixed positive integer \(j\), there are finite
constants \(C_j,N_j\) such that, for every odd \(N\ge N_j\),

\[
 \max_{x,y}|U_N^j(x,y)|\le C_jN^{-1/2}.                 \tag{1.1}
\]

In that source the ordinary-half symbol contains
\(r(q+1/2)\cos(2\pi p-\alpha_0)/100\), rather than the unshifted
\(p\)-term. This convention is required for the exact modular Weyl
operators in the question. The proof of (1.1) uses the exact Gaussian
image formula for the metaplectic power, including non-coprime odd
moduli, the positive inverse twist for the fixed classical power, and
the finite-shift Hamilton--Jacobi/transport calculation through its
unitary Duhamel remainder. The latter is \(O_j(N^{-1})\) in each
column and therefore suffices for (1.1). No assertion uniform in a
growing \(j\) is imported here.

Consequently

\[
 c_{j,N}\longrightarrow0\quad\hbox{for every fixed }j\ge1. \tag{1.2}
\]

Define \(m_N=0\) if the following set is empty, and otherwise define

\[
 m_N=\max\left\{2\le m\le\lfloor\sqrt N\rfloor:
       \max_{1\le j\le m}|c_{j,N}|\le m^{-3}\right\}.
                                                               \tag{1.3}
\]

Then \(m_N\to\infty\) along all odd \(N\). Indeed, for any fixed
\(m\ge2\), (1.2) and the finiteness of the indices \(1,\ldots,m\)
make \(m\) an admissible candidate for all sufficiently large odd
\(N\). This is only a diagonal consequence of fixed-power estimates;
it provides no rate comparable to the Heisenberg scale.

## 2. Exact clock completion of these original coordinate moments

The following finite statement needs only Fourier orthogonality.
Suppose \(2m<N\), \(c_{-j}=\overline{c_j}\), and

\[
 2\sum_{j=1}^m|c_j|<1.
\]

Let \(z_l=\exp(2\pi il/N)\), \(0\le l<N\), and set

\[
 w_l=\frac1N\left(1+\sum_{j=1}^m
       [c_jz_l^{-j}+\overline{c_j}z_l^j]\right).
                                                               \tag{2.1}
\]

Each weight is real and strictly positive, since

\[
 \frac{1-2\sum|c_j|}{N}\le w_l
       \le\frac{1+2\sum|c_j|}{N}.                       \tag{2.2}
\]

For every integer \(a\),

\[
 \frac1N\sum_{l=0}^{N-1}z_l^a=\mathbf1_{N\mid a}.       \tag{2.3}
\]

Thus \(\sum_lw_l=1\). For \(1\le k\le m\), expand the product
\(w_lz_l^k\) and use (2.3). The constant term contributes zero,
the term \(c_jz_l^{k-j}\) contributes only for \(j=k\), and
every exponent \(k+j\) lies strictly between \(0\) and \(N\).
Therefore

\[
 \sum_lw_lz_l^k=c_k,\qquad 1\le k\le m.                \tag{2.4}
\]

The negative moments follow by conjugation. In particular there is no
conjugation error in (2.1): the coefficient of \(z_l^{-j}\) is
\(c_j\).

Apply this to the actual numbers \(c_{j,N}\), with \(m=m_N\), once
\(m_N\ge2\). The constraints imply \(2m_N<N\) and

\[
 2\sum_{j=1}^{m_N}|c_{j,N}|\le 2m_N^{-2}\le\tfrac12.
\]

The resulting positive weights satisfy

\[
 \max_l|Nw_{l,N}-1|\le2m_N^{-2}\longrightarrow0.        \tag{2.5}
\]

To realize this as a unitary matrix with a prescribed coordinate,
let \(v_N=(\sqrt{w_{0,N}},\ldots,\sqrt{w_{N-1,N}})^T\). Choose
any unitary \(Q_N\) with \(Q_Ne_0=v_N\), and put

\[
 V_N=Q_N^*\operatorname{diag}(z_0,\ldots,z_{N-1})Q_N.
\]

Then, exactly,

\[
 \langle e_0,V_N^j e_0\rangle
      =\langle e_0,U_N^j e_0\rangle,
       \qquad |j|\le m_N.                             \tag{2.6}
\]

The vector \(e_0\) is cyclic for \(V_N\): all weights are positive,
all eigenvalues are distinct, and the associated Vandermonde matrix
is invertible. Nevertheless the **unweighted** eigenvalues of \(V_N\)
are exactly the clock. A uniformly rotated unfolded clock has law
\(\sum_{n\in\mathbb Z}\delta_{n-\beta}\), with \(\beta\) uniform on
\([0,1)\), for every \(N\). This differs from Sine\(_2\): an interval
of length less than one can contain at most one clock point, whereas
the Sine\(_2\) second factorial integral over any interval of positive
length is positive, because
\(1-[\sin(\pi(x-y))/(\pi(x-y))]^2>0\) whenever \(x\ne y\).

Equation (2.6) concerns a coordinate spectral measure. It does **not**
match the original normalized power traces, and \(V_N\) is not of the
prescribed kicked-metaplectic form. It therefore cannot disprove
`H_diag` or the original local limit. Its sole use in this attempt is
to prevent an invalid inference from the growing initial return data.

## 3. Why the attempted Krylov reconstruction stops here

For a cyclic unitary, monic orthogonal polynomials through degree
\(m\), and hence the corresponding initial Schur parameters, are
determined by the moments \(c_j\), \(|j|\le m\). This finite fact does
not require a spectral universality theorem. The Gram matrix for
\(1,z,\ldots,z^{r-1}\) has entries \(c_{b-a}\); orthogonality of
\(z^r+\sum_{a<r}u_az^a\) is a finite linear system using only
\(c_{-r},\ldots,c_r\).

For the original prefix with \(r\le m_N\), its Gram matrix satisfies

\[
 \|G_r-I\|_{\mathrm{op}}
       \le(r-1)m_N^{-3}<1.
\]

Thus these finite systems are nonsingular. In particular, reconstructing
the initial polynomials from the actual return moments gives exactly
the same prefix for the clock completion in Section 2. The positivity
of the coordinate measure, cyclicity, and closeness of this prefix to
the zero-parameter prefix do not estimate the actual parameters at
indices comparable to \(N\).

The spatial tridiagonal structure of \(A_N\) does not provide such
a tail estimate: the needed Krylov vectors are powers of
\(e^{i10^{-80}NA_N}M_N\), not powers of \(A_N\), and the metaplectic
factor is a full matrix. No identity making its high Krylov
coefficients local in the Jacobi entries was obtained. The proposed
use of a uniform smallness bound for the full Schur tail was abandoned
rather than assumed.

## 4. Follow-up direct approaches examined

The full characteristic determinant can be expanded into exterior
powers, with \(\wedge^r e^{isA}=e^{is\,d\Gamma_r(A)}\). This keeps
the fermionic signs exactly, but estimating each term by its norm
loses the required cancellation. No estimate of the full signed
determinant sum at \(s=N10^{-80}\) was obtained from this identity.

The finite-time path representation was also considered. The fixed
power kernel argument in Section 1 gives controlled individual
branches for each fixed power. At powers proportional to \(N\), it
does not estimate the sum of the phases of the exponentially many
classical branches. Replacing that sum by an independent-phase or
Markov average would introduce a new ensemble; no \(o(1)\) comparison
for the original functional was found. Consequently neither
replacement was used.

The Ward, Haar-basis, scalar first-return, and disagreement-run Schur
identities had already been fully worked out in the nearest Round 11
sources. This branch checked those sources before attempting the
coordinate-measure approach. Their uncontrolled factors are retained;
none is turned into a contraction by taking a norm before the signed
sum.

## 5. The first original estimate remains unchanged

For the fixed test from the target checkpoint, write

\[
 \phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\quad
 I=\int\phi,\quad b_*=\frac{|\mathcal F^{-1}\phi|^2}{2I^2},
 \quad w=|\widehat b_*|^2.
\]

The unresolved estimate is still

\[
 \boxed{
 \frac1{N^2}\sum_{1\le n<2N}w(n/N)
 \left(\left|\operatorname{Tr}
 [(e^{i10^{-80}NA_N}M_N)^n]\right|^2-\min(n,N)\right)
       \longrightarrow0
 }
                                                               \tag{5.1}
\]

along every odd dimension. There is also no proved fixed positive
lower bound for its absolute value along an infinite original
subsequence. The coordinate completion in Section 2 does not change
either statement. Even proving (5.1) alone would not establish the
full hierarchy required in the question.

## 6. Actual read scope and hashes

Hashes below were recomputed from local bytes during this branch.
Reading a source in full means the raw source itself was inspected;
it does not mean all sources mentioned inside it were recursively
reread. The older proof specifically used in Section 1 was read in
full, including its appendices.

| Input | Actual scope | SHA-256 |
|---|---|---|
| `research_history_frozen/master_before_round12.md` | Frozen-base identity and heading searches only; the broad heading output was truncated | `b8b2741c3b15304e82cef77e0db517a6b9db23ffb22f7e49658b22ee5f900185` |
| `research_round12_2026_10_21/round12_target_checkpoint.md` | Full | `b39996f6cc4c86aebbf03b5a0775bf08b1ad250821b1b0bedd6c0c68767a0ec9` |
| `research_round11_2026_10_21/r11_resolvent_ward_diagonal_route.md` | Full | `6868e41398755931045c322ccc18cd3400631d85596aadeaf1c743f34d4efb4f` |
| `research_round11_2026_10_21/r11_coherent_checkpoint.md` | Full | `04d220ec857e51de1aa141504a71d69dee3e84b8329fb72d01f864aa97225770` |
| `research_round10_2026_10_21/root_operator_route_scope.md` | Full | `579b1f4721dfaef4e6da1d914d90cab934b2fc625ebe37ef93b87839b57722a2` |
| `research_round7_2026_10_21/r7_return_all_fixed_powers_phase_separation.md` | Full, including Appendices A and B; needed fixed-power kernel proof inspected | `46982efaa581d322d4e82d5f5782ccf69f979a5a59adfb863dd40ef292205527` |
| `research_round8_2026_10_21/r8_original_uniform_antiunitary_clifford_gap.md` | Full; used only to avoid repeating an already excluded affine/Clifford reversal route | `96a22f2e1ef7b79af6fcbd3768f00adb4dac2bbadfef53545bac2199cf96d3e9` |

Literature scope: selected parts of Barry Simon's primary preprint
`arXiv:math/0606037` were opened for the finite paraorthogonal
construction; the web output was truncated in its middle, so no full
paper read is claimed. That construction was subsequently replaced by
Section 2 and no theorem from the preprint is used here. Further web
searches on deterministic kicked maps and unitary band matrices were
search-result screening only; they produced no imported universality
theorem. No numerical diagonalization at a substituted value of the
physical kick was performed.
