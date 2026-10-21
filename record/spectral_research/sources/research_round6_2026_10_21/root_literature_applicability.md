> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/root_literature_applicability.md`. Embedded SHA256: `c063192b411737eb0823a99913e898d4ca2e551fca647163408425a09c1699a3`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Published inputs and the boundary of the literature comparison

Date checked: 21 October 2026. This note records which external statements
were actually used in round 6, and why the other reviewed papers do not
complete the prescribed deterministic spectral problem. It does not claim
an exhaustive survey or establish the historical novelty of the new lemmas.

## 1. Two exact published inputs used

### 1.1. Matrix bounded differences

Joel A. Tropp, *User-Friendly Tail Bounds for Sums of Random Matrices*,
Foundations of Computational Mathematics **12** (2012), 389–434,
Corollary 7.5, printed page 428.

- DOI: <https://doi.org/10.1007/s10208-011-9099-z>.
- Published PDF personally opened and searched at the theorem:
  <https://link.springer.com/content/pdf/10.1007/s10208-011-9099-z.pdf>.

Application: the self-adjoint dilation of
$R(z)=|U\operatorname{diag}(z)U|^{\circ2}$, a bounded function of
independent uniform coordinate phases. The deterministic coordinate
change is at most $4C/N$. Consequently the squared difference is
bounded by $(4C/N)^2I_{2N}$, the variance parameter is $16C^2/N$,
and the dimension is $2N$. This yields
$$
\Pr(\|R-\mathbb ER\|\ge s)
\le2N\exp[-Ns^2/(128C^2)].
$$
The full application, including the exact original-class coefficient
extraction and the finite band restriction, is proved in the included
phase-concentration source and its audit.

### 1.2. Algebraic exponential independence

Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the Exponentials
of Algebraic Numbers*, ISSAC 2022, Theorem 1.1.

- DOI: <https://doi.org/10.1145/3476446.3536170>.
- Author PDF, version 2 dated 16 May 2022, personally opened at page 1:
  <https://arxiv.org/pdf/2112.05004>.

Only the qualitative Lindemann–Weierstrass statement displayed there is
used. The original finite spectral decomposition has algebraic
coefficients, not all zero, multiplying exponentials of distinct
algebraic numbers $iN\tau\lambda$. The theorem proves every original
matrix entry nonzero. It is not used to infer a quantitative lower bound,
equidistribution, or cancellation of growing sums.

## 2. Why the quantum-graph result does not supply the missing estimate

Z. Pluhař and H. A. Weidenmüller, *Quantum Graphs and Random-Matrix
Theory*, author PDF <https://arxiv.org/pdf/1407.1148>.

The full paper was opened. The relevant definitions, directed-bond
transition matrix, rationally independent bond-length assumption,
uniform spectral-gap hypothesis, and subsequent phase integration were
read. Its graph construction and energy/phase average differ from the
fixed original $U_N$ observable. In particular, replacing this
average by the single prescribed phase value would require a separate
error estimate for the actual target; none has been proved here.

Even a tempting literal star-graph embedding of a general matrix fails
a displayed hypothesis. Such a two-layer construction has stochastic
matrix
$$
\begin{pmatrix}0&P\\ I&0\end{pmatrix}.
$$
It has eigenvalue $-1$, since its constant-mode restriction is
$\begin{pmatrix}0&1\\1&0\end{pmatrix}$. Thus it does not
satisfy a gap that requires every eigenvalue other than $+1$ to have
modulus at most $1-a$. Removing that eigenvalue or invoking a more
general graph theorem requires another argument; it cannot be done by
renaming the matrix. The proof above is the reason this particular
embedding is not used.

S. Gnutzmann and A. Altland, *Spectral correlations of individual quantum
graphs*, <https://arxiv.org/pdf/nlin/0508009>, was also opened at its
phase-average construction. This comparison does not prove or disprove
any assertion of those papers. It identifies the specific unverified
transition needed for the present original matrix sequence.

## 3. Other recent constructions inspected

- *Semiclassical foundation of universality in chaotic quantum circuits*,
  <https://arxiv.org/html/2605.27052v1>.
- *Provable random-matrix spectral ramp in a static, geometrically local
  Hamiltonian*, <https://arxiv.org/html/2606.30635v2>.

Their actual definitions and limiting procedures were inspected. The
first uses a time-window setting and semiclassical/diagonal ingredients;
the second uses its own circuit and Hamiltonian construction with
specified nested limits. Neither is a theorem about the matrix kernel,
fixed kick, all odd dimensions, and full factorial hierarchy of this
problem. No transfer with an $o(1)$ error for the required functional
was found or supplied. They are therefore not dependencies of any
proved result in the current report.

The search date is not a paper's publication date. An older perturbed
cat-map paper returned by a newly crawled search result was not treated
as a new 2026 theorem. Search snippets and titles alone were not used as
evidence that the original-family hypotheses hold.

## 4. Remaining exact obligation

The unproved step remains a quantitative signed trace estimate for the
actual fixed family. No statement about a random-phase ensemble,
generic parameter, restricted time average, prime subsequence, or
different circuit construction has been substituted for it. All
other inputs in round 6 are proved in the included source notes or are
explicitly traced to a full proof already present in the earlier
portion of the same cumulative document.
