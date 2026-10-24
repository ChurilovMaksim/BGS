# An observed first-return pulse despite perfect intensity mixing

**Stable claim:** BGS-TRACE-083. **State:** PROJECT PROOF + INDEPENDENT
INTERNAL RECONSTRUCTION, 14 October 2026. The complete R1--R5 proof
uses TRACE-081's explicit family and TRACE-082's block recurrence.
This is an abstract-family theorem, not a BGS theorem. Mathematical
priority is not established; no analytic formal certification is claimed.

Inputs: the explicit \(A_k,U_k,\epsilon_k\) of TRACE-081 and the
Hilbert--Schmidt block definitions of TRACE-082. All first-return
arguments below are given explicitly; no external recurrence theorem
is a proof dependency.

Let \(n=4^k\), \(N=np\), \(k\ge2\), \(p\) an odd prime,
\(\epsilon=N^{-4}\). Write \(K=H^2\) for TRACE-081's three-cycle
permutation and \(S=K^{\otimes k}\). Thus \(S^3=I\).
Put \(J_n=n^{-1}{\bf1}{\bf1}^*\), \(J_p=p^{-1}{\bf1}{\bf1}^*\),
\(\Pi_n=I-J_n\), \(\Pi_p=I-J_p\), and
\(A=H^{\otimes k}\otimes V_p\).
Choose the simple-spectrum \(U=AE\) of TRACE-081 with
\(\|U-A\|\le\epsilon\). Its exact flat intensity and reversal norm
are unchanged.

On Hilbert--Schmidt matrices let \(\mathcal D\) be diagonal projection,
\(\mathcal Q=I-\mathcal D\), and \(\mathcal T_U(X)=UXU^*\).
Identify diagonal matrices with their diagonal vectors. Define
\[
 F_t(U)=\mathcal D\mathcal T_U
          (\mathcal Q\mathcal T_U)^{t-1}\mathcal D,\qquad t\ge1.
\]
For \(t\ge2\) this equals
\(\mathcal L_U\mathcal E_U^{t-2}\mathcal C_U\) in TRACE-082 notation;
\(F_1(U)=P(U)\). These are first-return amplitudes for an orthogonal
projection protocol on Hilbert--Schmidt space. They are not being
identified with literal physical measurement probabilities for
density matrices.

## R1. Exact finite-support first-return kernel

The complete amplitudes on the diagonal space are
\[
\begin{aligned}
 F_1(A)&=J_n\otimes J_p,\\
 F_2(A)&=(S-J_n)\otimes J_p,\\
 F_p(A)&=J_n\otimes\Pi_p,\\
 F_{2p}(A)&=(S^p-J_n)\otimes\Pi_p.
\end{aligned}
\]
For every other positive integer \(t\), \(F_t(A)=0\).
The four displayed times are distinct since \(p\ge3\) is odd.

**Proof.** Set \(R_m=\mathcal D\mathcal T_A^m\mathcal D=P(A^m)\),
with \(R_0=I\). Core periodicity and the chirp Gauss identity give
\[
R_m=
 \begin{cases}S^{m/2},&m\ \text{even},\\J_n,&m\ \text{odd}\end{cases}
 \ \otimes\
 \begin{cases}I_p,&p\mid m,\\J_p,&p\nmid m.\end{cases}
\]
For even \(m\), \(H^m=K^{m/2}\); for odd \(m\), \(H^m\) is
a permutation times \(H\), hence flat. These statements tensorize.
If \(p\nmid m\), the nonzero-coefficient Gauss argument in TRACE-081
makes \(V_p^m\) flat; otherwise \(V_p^m=I\).

The exact renewal identity, from TRACE-082's block recurrence, is
\[
 R_m=\sum_{t=1}^m F_t R_{m-t}.
\]
It determines the \(F_t\) uniquely by induction; multiplication order
has not been interchanged. Split diagonal space into the four
orthogonal sectors
\[
 {\bf1}_n\otimes{\bf1}_p,\quad
 {\bf1}_n^\perp\otimes{\bf1}_p,\quad
 {\bf1}_n\otimes{\bf1}_p^\perp,\quad
 {\bf1}_n^\perp\otimes{\bf1}_p^\perp.
\]
In these sectors \(R_m\) equals, respectively: the identity at every
time; \(S^{m/2}\) at even times and zero otherwise; the identity at
multiples of \(p\) and zero otherwise; \(S^{m/2}\) at multiples of
\(2p\) and zero otherwise. Thus each sector has one first amplitude,
at \(1,2,p,2p\), and subsequent returns are its powers. Substitution
into the renewal identity proves all four formulas and all zero
coefficients, including times beyond a period.

## R2. One observed coefficient is almost an isometry

Let
\[
 W=\operatorname{Ran}(\Pi_n\otimes\Pi_p),\quad
 d_W=(n-1)(p-1).
\]
It lies in the centered diagonal space \(D_0\), of dimension \(N-1\).
For \(t=2p\), every \(x\in W\) satisfies
\[
 \|F_t(U)x\|_2\ge(1-4p\epsilon)\|x\|_2.
\]
At least \(d_W\) singular values of \(F_t(U)|_{D_0}\) are
at least \(1-4p\epsilon\), and
\[
 1\ \ge\
 \frac{\|F_t(U)|_{D_0}\|_{\rm HS}^2}{N-1}
 \ \ge\
 \frac{(n-1)(p-1)}{np-1}(1-4p\epsilon)^2
 \longrightarrow1
\]
as \(k\to\infty\), \(p\to\infty\).
Here the Hilbert--Schmidt norm is that of an operator on diagonal
vectors; it is distinct from the ambient matrix operator norm.

**Proof.** The identity
\[
 (\mathcal T_U-\mathcal T_A)X
   =(U-A)XU^*+AX(U^*-A^*)
\]
gives \(\|\mathcal T_U-\mathcal T_A\|_{\rm HS\to HS}\le2\epsilon\).
Each intervening projection and unitary is a contraction.
Telescoping the \(t\) unitary superoperator factors in \(F_t\) gives
\[
 \|F_t(U)-F_t(A)\|_{2\to2}\le2t\epsilon.
\]
At \(t=2p\), R1 restricts \(F_t(A)\) to \(S^p\otimes I\) on \(W\),
an isometry. The reverse triangle inequality yields the lower bound.
The min-max principle applied to \(F_t^*F_t\) proves the singular-value
statement. Alternatively, summing the squared lower bound on an
orthonormal basis of \(W\) directly proves the Hilbert--Schmidt bound.
Trace preservation ensures that all these maps preserve \(D_0\).
Contractivity supplies the upper bound \(N-1\).
Finally \(4p\epsilon\le4N^{-3}\to0\) and
\((n-1)(p-1)/(np-1)\to1\).

## R3. Later than every fixed power below N

Choose odd primes \(p_k\ge4^{k^2}\). Their existence needs only
unboundedness of primes, not a prime-gap estimate. For \(t_k=2p_k\),
\[
 \frac{t_k}{N_k}=\frac2{4^k}
      =2\|B(U_k)\|^2\longrightarrow0,
 \qquad
 \frac{t_k}{N_k^\alpha}
     =\frac{2p_k^{1-\alpha}}{4^{\alpha k}}
         \longrightarrow\infty
 \quad(0<\alpha<1\ \text{fixed}).
\]
The same family retains exact \(P=J\), vanishing reversal norm, simple
spectrum, the uniform macroscopic phase measure and TRACE-081's
non-BGS local statistics. Therefore those algebraic conditions cannot
imply that every observed memory coefficient decays at all times
beyond any fixed sublinear power of \(N\). Failure holds even for
the centered Hilbert--Schmidt average over diagonal source directions,
not just an unreachable norm witness in the off-diagonal block.

## R4. Low unconjugated traces cancel; cyclic compositions survive

Assume \(p\ne3\), and put \(M_A=F_{2p}(A)|_{D_0}\),
\(M_U=F_{2p}(U)|_{D_0}\), \(\delta=4p\epsilon\).
For every positive integer \(q\),
\[
 \left|
 \frac{\operatorname{Tr}_{D_0}M_U^q}{N-1}
 -\frac{(n-1)(p-1)}{np-1}\,{\bf1}_{3\mid q}
 \right|\le q\delta.
\]
In particular, for each fixed \(q\), the normalized trace converges
to \({\bf1}_{3\mid q}\). The first two unconjugated traces tend to
zero, while the normalized cubic trace tends to one.

**Proof.** \(K\) and \(K^2\) have exactly one fixed coordinate, hence
\(\operatorname{Tr}S=\operatorname{Tr}S^2=1\), whereas \(S^3=I_n\).
As \(S\) commutes with \(J_n\) and \(SJ_n=J_n\),
\[
 M_A^q=(S^{pq}-J_n)\otimes\Pi_p.
\]
If \(3\nmid q\), then \(3\nmid pq\) and this trace is zero.
If \(3\mid q\), the trace is \((n-1)(p-1)\).
R2 gives \(\|M_U-M_A\|\le\delta\); both maps are contractions.
Telescoping powers and the dimension bound on the trace yield
\[
 \|M_U^q-M_A^q\|\le q\delta,\qquad
 |\operatorname{Tr}_{D_0}(M_U^q-M_A^q)|
       \le(N-1)q\delta.
\]
This proves the inequality for every integer \(q\ge1\), and its limit
for fixed \(q\). No growing-\(q\) limit is claimed without keeping the
explicit \(q\delta\) error.

This is not cancellation of a conjugated covariance:
\(\operatorname{Tr}(M_UM_U^*)/(N-1)\to1\) by R2.
The statement concerns compositions of a specified observed memory
operator, not the spectral traces of the frozen BGS propagator.
It shows explicitly why low unconjugated scalar cancellations do
not propagate automatically to all cyclic compositions.

## R5. Small all-source energy tails do not remove short-pulse recycling

Put \(\delta=4p\epsilon\), with no additional assumption \(p\ne3\).
For every diagonal vector \(x\),
\[
 \sum_{t>2p}\|F_t(U)x\|_2^2\le\delta^2\|x\|_2^2.
\]
In particular the centered diagonal operator tail satisfies
\[
 \frac1{N-1}\sum_{t>2p}\|F_t(U)|_{D_0}\|_{\rm HS}^2
       \le\delta^2\le16N^{-6}.
\]

**Proof.** Define \(Y_s(U)=(\mathcal Q\mathcal T_U)^s\mathcal D\).
Orthogonality of \(\mathcal D,\mathcal Q\) and unitarity of
\(\mathcal T_U\) give the exact energy identity
\[
 \|Y_{t-1}(U)x\|_{\rm HS}^2-\|Y_t(U)x\|_{\rm HS}^2
       =\|F_t(U)x\|_2^2.
\]
For \(A\), the four operators \(F_t(A)^*F_t(A)\) in R1 are exactly
the four orthogonal sector projections, whose sum is the identity.
All four first returns have occurred by time \(2p\). Telescoping the
energy identity therefore gives \(Y_{2p}(A)=0\).
Telescoping the \(2p\) unitary-superoperator factors, as in R2, yields
\(\|Y_{2p}(U)-Y_{2p}(A)\|\le4p\epsilon=\delta\).
For every finite \(T>2p\), the remaining energy identity bounds the
sum from \(2p+1\) to \(T\) by \(\|Y_{2p}(U)x\|^2\).
Taking increasing partial sums proves the infinite upper bound.
Summing it over an orthonormal basis of \(D_0\) gives the operator
Hilbert--Schmidt assertion. Finally \(p\le N\) and
\(\epsilon=N^{-4}\) give \(\delta^2\le16N^{-6}\).

No equality of eventual return probabilities or weighted return-time
bound is imported. This is an amplitude-energy bound on the specified
Hilbert--Schmidt projection protocol. It coexists with R2's large
single coefficient and R4's recurring cyclic compositions: repeated
short returns can carry coherence even when the monitored tail is
tiny. The powers \(M_U^q\) compose data from separate completed excursions;
they are not \(F_{2pq}(U)\). For example \(F_{6p}(A)=0\), whereas
\(R_{6p}(A)|_W=M_A^3|_W=I_W\).
No conclusion about the actual physical cavity source or its
signed trace hierarchy follows from this abstract example.

## Boundary

Abstract \(N_k=4^k p_k\) family only. No unchanged odd-\(N\) map,
fixed smooth chaotic quantization, specified physical cavity source,
phase-averaged ensemble contradiction or BGS conclusion is supplied.
This concerns one coefficient \(\mathcal L\mathcal E^{t-2}\mathcal C\),
strengthening TRACE-082's full-return comparison for this family.
First-return renewal theory is prior mathematics; priority of this
application is not established.

## Verification and prior mechanism

[TRACE-081](flat_spectrum_obstruction.md) supplies the family;
[TRACE-082](coherence_memory_plateau.md) supplies the return-block
notation. The [independent reconstruction and exact finite packet](../../archive/evidence/executions/20261014/first-return/README.md)
bind the frozen R1--R5 text, independent controls and root executions.
The full mathematical proof is separate from every finite replay.
No new Lean operator theorem is asserted.

The first-return/renewal mechanism is prior mathematics:
[primary-source dictionary](../../literature/coherence_first_return_context_20261014.md).
The exact finite-support family, perturbation bounds and cyclic trace
conclusions above are the project result, without an established
world-priority claim.
