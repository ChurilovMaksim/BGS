# Perfect intensity mixing does not determine the microscopic spectrum

**Stable claim:** BGS-TRACE-081. **State:** PROJECT PROOF + INDEPENDENT
INTERNAL RECONSTRUCTION, 14 October 2026. Sections 1--7 are self-contained.
The [review packet](../archive/evidence/executions/20261014/spectrum-coherence/README.md)
binds the frozen input, reconstructed proof and exact finite controls.
This is an abstract-family obstruction, not a BGS counterexample for a
fixed smooth chaotic quantization. No mathematical priority is asserted.

## 1. Exact statement

For a unitary matrix \(U\in U(N)\), put
\[
P(U)_{ij}=|U_{ij}|^2,\qquad
J_N=N^{-1}{\bf1}{\bf1}^*,\qquad
B(U)_{ij}=U_{ij}\overline{U_{ji}}.
\]
All matrix norms below are the Euclidean operator norm. The reversal
matrix \(B(U)\) is the displayed coordinate expression, not a claim of
a complete antiunitary symmetry classification.

Let \(p_k\) be any sequence of odd primes tending to infinity, let
\[
n_k=4^k,\quad N_k=n_kp_k,\quad \epsilon_k=N_k^{-4},\qquad k\ge2.
\]
There is a deterministic choice of unitaries \(U_k\in U(N_k)\) for which
all the following assertions hold.

1. The spectrum is simple, every entry has squared modulus \(1/N_k\),
   and
   \[
   P(U_k)=J_{N_k},\qquad \|P(U_k)-J_{N_k}\|=0,\qquad
   \|B(U_k)\|=2^{-k}.
   \tag{O1}
   \]
2. The empirical eigenphase measure converges weakly to normalized
   Lebesgue measure on the circle. More quantitatively, for each fixed
   positive integer \(q\), eventually
   \[
   \frac{|\operatorname{Tr}U_k^q|}{N_k}
       \le p_k^{-1/2}+q\epsilon_k.
   \tag{O2}
   \]
3. Order the eigenphases around the circle, and include the wrapping
   gap. The empirical distribution of the \(N_k\) unfolded nearest
   spacings \(N_k(\theta_{j+1}-\theta_j)/(2\pi)\) converges weakly
   to \(\delta_0\). At least \(1-6/4^k\) of these spacings are at most
   \(2N_k\epsilon_k/\pi\), for all sufficiently large \(k\).
   \(\tag{O3}\)
4. With an independent uniform origin \(\Theta\) on the circle, put
   \[
   \Xi_k=\sum_{j=1}^{N_k}
      \delta_{\frac{N_k}{2\pi}\operatorname{Arg}
                        (e^{i(\theta_j-\Theta)})}.
   \]
   Then \(\Xi_k\) converges vaguely in probability to the empty point
   measure. In particular, for each fixed \(R>0\),
   \[
   \mathbb P\{\Xi_k([-R,R])>0\}
      \le \frac{12p_k\epsilon_k}{\pi}+
                 \frac{12R}{4^k}\longrightarrow0.
   \tag{O4}
   \]
   Nevertheless \(\mathbb E\Xi_k([-R,R])=2R\) once \(N_k>2R\).
   Counts are not uniformly integrable.
5. The positive integer
   \[
   t_k=6p_k\left\lfloor4^k/6\right\rfloor
       =N_k-4p_k
   \]
   satisfies \(t_k/N_k\to1\), but the normalized form factor obeys
   \[
   \frac{|\operatorname{Tr}U_k^{t_k}|^2}{N_k}
        \ge N_k(1-t_k\epsilon_k)^2\longrightarrow\infty.
   \tag{O5}
   \]
   This is a deterministic sequence of Heisenberg-scale resonances,
   not a claim about a signed smoothing convention.

Simple spectrum in this theorem is obtained by arbitrarily small
column phases, rather than by assuming exact degeneracies count as
different symmetry sectors. The origin-averaged conclusion O4 is stronger
than a prescribed-origin forbidden-interval example.

## 2. A four-dimensional exact core

Define
\[
W=\begin{pmatrix}
1&1&1&1\\
1&-1&-1&1\\
1&1&-1&-1\\
1&-1&1&-1
\end{pmatrix},\qquad H=W/2.
\]
Direct row orthogonality gives \(WW^T=4I\), so \(H\) is real orthogonal
and all its entries have squared modulus \(1/4\). Exact multiplication
gives
\[
H^2=\begin{pmatrix}
1&0&0&0\\0&0&1&0\\0&0&0&1\\0&1&0&0
\end{pmatrix},\qquad H^6=I.
\tag{O6}
\]
The coordinate reversal core is
\[
B(H)=\frac14
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}.
\]
The sign matrix in this display has its product with its transpose
equal to \(4I\). Consequently \(\|B(H)\|=1/2\).
Already \(H^{\otimes k}\) is a perfectly flat orthogonal matrix with
vanishing reversal norm and spectrum supported on six roots of unity.
This simpler example alone has an atomic macroscopic measure.
The next factor removes that macroscopic defect.

## 3. A flat chirp with uniform macroscopic phase law

For an odd prime \(p\), write \(\omega=e^{2\pi i/p}\) and define
\[
(F_p)_{ab}=p^{-1/2}\omega^{ab},\qquad
D_p=\operatorname{diag}(\omega^{b^2})_{b=0}^{p-1},\qquad
V_p=F_p^*D_pF_p.
\]
Fourier orthogonality proves \(F_p\) is unitary. Thus \(V_p\) is
unitary, has eigenvalues \(\omega^{b^2}\), and \(V_p^p=I\).
Its entry formula is
\[
(V_p)_{ij}=\frac1p\sum_{b=0}^{p-1}
                      \omega^{b^2+(j-i)b}.
\tag{O7}
\]
For every \(d\in\mathbb F_p\),
\[
\left|\sum_b\omega^{b^2+db}\right|^2
 =\sum_{b,c}\omega^{(b-c)(b+c+d)}
 =\sum_{a,h}\omega^{ah}=p.
\tag{O8}
\]
The middle substitution is a bijection because 2 is invertible
modulo \(p\). For \(a=0\) the inner sum is \(p\); for \(a\ne0\)
it is zero. This proves exactly \(|(V_p)_{ij}|^2=1/p\).
Replacing \(b\) by \(-b\) in O7 proves \(V_p^T=V_p\), whence
\(B(V_p)=J_p\) and \(\|B(V_p)\|=1\).

If \(p\nmid q\), the same squared-sum argument, with the nonzero
coefficient \(q\), gives
\[
|\operatorname{Tr}V_p^q|
   =\left|\sum_b\omega^{qb^2}\right|=\sqrt p.
\tag{O9}
\]
No evaluation of the phase of a Gauss sum, external exponential-sum
estimate, or random matrix theorem is needed.

## 4. Tensor construction before the simple-spectrum perturbation

Put
\[
A_k=H^{\otimes k}\otimes V_{p_k}.
\]
Tensor multiplication and O6--O9 give
\[
|A_{k,ij}|^2=N_k^{-1},\quad P(A_k)=J_{N_k},\quad
B(A_k)=B(H)^{\otimes k}\otimes J_{p_k},\quad
\|B(A_k)\|=2^{-k},\quad A_k^{6p_k}=I.
\tag{O10}
\]
Its eigenphases therefore belong to at most \(6p_k\) equally spaced
root-of-unity centers. For fixed \(q\), eventually \(p_k\nmid q\).
Since \(H^{\otimes k}\) is unitary,
\[
\frac{|\operatorname{Tr}A_k^q|}{N_k}
 =\frac{|\operatorname{Tr}(H^{\otimes k})^q|}{4^k}
     \frac{|\operatorname{Tr}V_{p_k}^q|}{p_k}
 \le p_k^{-1/2}.
\tag{O11}
\]
Thus every nonconstant Fourier coefficient of the empirical eigenphase
measure tends to zero. Approximation of continuous circle functions
by trigonometric polynomials identifies its limit as normalized
Lebesgue measure.

## 5. Generic column phases give simple spectrum for any invertible core

Here is the algebraic lemma used to remove all exact degeneracies.

**Lemma.** If \(A\) is any invertible complex \(N\)-by-\(N\) matrix,
then \(A\operatorname{diag}(z_1,\ldots,z_N)\) has simple spectrum
for almost every choice of phases \(z_j=e^{i\alpha_j}\) in any
nonempty product of open arcs. In particular, if \(A\) is unitary,
one can choose all \(|\alpha_j|<\epsilon\), for any \(\epsilon>0\),
and retain simple spectrum.

**Proof.** The polynomial
\[
f(\lambda,z)=\det(\lambda I-A\operatorname{diag}z)
\]
is monic in \(\lambda\), has degree at most one in each \(z_j\),
satisfies \(f(\lambda,0)=\lambda^N\), and has constant coefficient
\((-1)^N\det A\prod_jz_j\ne0\) as a polynomial in \(z\).
In the unique factorization ring
\(\mathbb C[\lambda,z_1,\ldots,z_N]\), a repeated irreducible
factor \(g^2\) of \(f\) must be independent of every \(z_j\), since
degrees in each \(z_j\) add and \(\deg_{z_j}f=1\).
Such a \(g\in\mathbb C[\lambda]\) must divide \(f(\lambda,0)=\lambda^N\),
so \(g\) is a scalar multiple of \(\lambda\). But \(\lambda\)
does not divide \(f\), by its nonzero constant coefficient.
Hence \(f\) has no repeated irreducible factor.

Equivalently, \(f\) is square-free as a polynomial in \(\lambda\)
over \(\mathbb C(z_1,\ldots,z_N)\): monicity and the usual
polynomial factorization over a fraction field exclude
coefficient-only factors, and characteristic zero makes each
irreducible factor with positive \(\lambda\)-degree separable.
Its discriminant in \(\lambda\) is therefore a nonzero polynomial
in \(z\).

A nonzero multivariate polynomial cannot vanish identically
on a product of unit-circle arcs: successively fixing all but
one variable reduces this to the univariate polynomial identity
principle. Its zero set on any product of arcs has measure zero,
by induction and Fubini, since a nonzero univariate polynomial
has finitely many zeros; the exceptional parameter slices have
measure zero by the same induction. Outside this zero set the
discriminant is nonzero. This proves the lemma.

Choose such phases for \(A_k\), and put
\[
E_k=\operatorname{diag}(e^{i\alpha_j}),\qquad
U_k=A_kE_k,\qquad |\alpha_j|<\epsilon_k.
\]
The selection can be deterministic. In fact the nonvanishing set
is open and nonempty inside the small phase cube; it contains a
rational phase tuple. Choosing the first suitable tuple in a fixed
enumeration gives a definite mathematical selection. No effective
algorithm for testing a transcendental discriminant is claimed.

We have
\[
\|U_k-A_k\|\le\epsilon_k,\qquad
P(U_k)=P(A_k),\qquad B(U_k)=E_k^*B(A_k)E_k.
\tag{O12}
\]
These identities prove O1, including simple spectrum.
For each positive integer \(q\), telescoping powers of two
unitaries gives
\[
\|U_k^q-A_k^q\|\le q\epsilon_k,\qquad
|\operatorname{Tr}(U_k^q-A_k^q)|\le N_kq\epsilon_k.
\tag{O13}
\]
Combining O11 and O13 proves O2 and the uniform macroscopic law.

## 6. Cluster control, spacings, and a uniform random origin

Every eigenvalue of \(U_k\) is within distance \(\epsilon_k\)
of the spectrum of \(A_k\). Indeed, for a unit eigenvector \(x\)
with \(U_kx=\lambda x\),
\[
(\lambda I-A_k)x=(U_k-A_k)x.
\]
The unitary spectral decomposition of \(A_k\) gives
\(\|(\lambda I-A_k)x\|\ge
 \operatorname{dist}(\lambda,\operatorname{spec}A_k)\).
No matching of individual eigenvalues or eigenvalue derivatives
is used.

For small \(\epsilon_k\), chord distance at most \(\epsilon_k\)
implies angular distance at most \(2\epsilon_k\).
All eigenphases of \(U_k\) lie in at most \(6p_k\) circular
arcs of radius \(2\epsilon_k\) about the old centers.
These arcs are disjoint eventually: their centers are separated
by at least \(2\pi/(6p_k)\), whereas
\(p_k\epsilon_k\to0\).

If a nonempty cluster has \(s\) distinct eigenphases, its \(s-1\)
internal consecutive gaps are at most \(4\epsilon_k\).
Only one cyclic gap per nonempty cluster can join clusters.
There are therefore at least \(N_k-6p_k\) gaps at most
\(4\epsilon_k\). Their unfolded values are at most
\(2N_k\epsilon_k/\pi\to0\). Since \(6p_k/N_k=6/4^k\to0\),
a bounded continuous spacing test converges to its value at zero.
This proves O3. The exact arithmetic mean of the circular
unfolded spacings is still one; weak convergence does not
preserve it without uniform integrability.

For the local process in O4 to put any point in \([-R,R]\),
the uniform origin must fall within angular distance
\(2\epsilon_k+2\pi R/N_k\) of at least one old center.
A union bound over at most \(6p_k\) centers yields O4.
The bound holds whether or not the relevant enlarged arcs overlap.
For each fixed compact window the probability of any point
there tends to zero, proving vague convergence in probability
to the empty point measure. Uniformity of the origin separately
gives expected count \(2R\) exactly. This mean is carried by
events of probability tending to zero with large clustered counts.
This origin-averaged local process cannot have an intensity-one
nonempty limiting point process such as Sine2.

## 7. Heisenberg resonances survive removal of exact degeneracy

Since \(4^k\equiv4\pmod6\), \(t_k=N_k-4p_k\) is a multiple
of \(6p_k\). Thus \(A_k^{t_k}=I\). O13, now with the integer
\(t_k\) rather than a fixed \(q\), implies
\[
|\operatorname{Tr}U_k^{t_k}-N_k|
   \le N_kt_k\epsilon_k.
\]
Here \(t_k\epsilon_k\le N_k^{-3}\to0\), which proves O5.
The same construction gives resonances near any fixed positive
multiple of \(N_k\), but O5 is sufficient for the stated theorem.

## 8. Scope, research consequence, and priority

The construction is an abstract family on the subsequence
\(N_k=4^kp_k\). It is not the repository's unchanged odd-dimensional
fixed-coupling propagator; it is not asserted to quantize one fixed
smooth chaotic map with the required correspondence principle.
It therefore refutes an inference from the displayed algebraic
mixing hypotheses, not the correctly delimited BGS conjecture.

It meets the numerical startup assumptions \(C_0=1\) and
\(\|P-J\|=0\) for the [maintained all-time fresh-phase
feedback theorem](trace-bridge/unconditional_feedback_flatness.md). Thus proving its random-feedback flatness
cannot by itself rule out the clustered initial microscopic law.
Applying any downstream clock theorem also requires that theorem's
precise process, clock, cutoff and independence assumptions.
No clock implication is a premise of this obstruction proof.

Tensor products, Fourier chirps, finite-order unitaries, Gauss
orthogonality, and generic phase splitting are classical mechanisms.
The combination here is a proof of the stated obstruction, with
no world-priority or prize-level claim. Tanner, *Unitary stochastic
matrix ensembles and spectral statistics*, arXiv:nlin/0104014,
formulates an **ensemble-averaged** spectral-statistics conjecture.
Gnutzmann--Altland, *Universal spectral statistics in quantum graphs*,
arXiv:nlin/0402029v1, printed page 2 and equation (1), expressly
uses rationally independent bond lengths to trade the spectral
average for independent phase averaging. Our fixed phase tuples
and small generic phase choices are not that full averaged ensemble.
These references delimit the comparison; neither is used to prove
O1--O5, and neither is alleged to be contradicted.

## 9. Verification boundary

The [maintained exact verifier](../computations/verification/spectrum_coherence_controls.py)
checks finite core, Gauss, tensor and discriminant identities. Separate
[archived JavaScript and independent Python controls](../archive/evidence/executions/20261014/spectrum-coherence/README.md)
retain their actual execution scope. None of these finite checks proves
the all-invertible phase lemma or any asymptotic statement. The mathematical
proof in Sections 1--7 supplies those claims. No analytic Lean certification
or external referee certificate is asserted.
