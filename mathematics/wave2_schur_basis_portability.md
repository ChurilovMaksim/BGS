# Why the Wave2 Schur split needs a basis-independent verification

**Status:** exact finite algebraic observation and independently executable
comparison policy. This is a *diagnostic/reproducibility statement*, not an
asymptotic estimate for the frozen quantum map or a proof of BGS.

## The original finite sample

The immutable Wave2 \`rounding\` verifier forms, for \`p=5\` and \`p=11\`,
the matrix indexed by \(x,y\in\mathbb F_p^2\),

\[
V_{x,y}=p^{-1}\exp\left(
  \frac{2\pi i}{p} f(x)^{\mathsf T}A f(y)\right),
\qquad
f(x_1,x_2)=(x_1^3,x_2^3),\quad
A=\begin{pmatrix}1&2\\0&1\end{pmatrix}.
\]

For these primes, \(\gcd(3,p-1)=1\), so \(f\) permutes the
\(p^2\) coordinates. Hence \(V\) is an exactly unitary finite
Fourier matrix (the nonsingular form \(A\) changes only the column
ordering). The original checker computes a complex Schur decomposition,
rounds the known eigenphases to roots of unity, obtains a reconstructed
\(V_{\rm ref}\), and applies *unequal* increments
\(\delta_j=j/p^8\) in that **Schur basis** to produce \(W\).
All original exact- and floating-point checks in that historical program
remain source-hash protected.

When a repeated eigenvalue has multiplicity greater than one, a Schur
algorithm is free to return different orthonormal bases of its eigenspace.
Because the \(\delta_j\) are not all equal, \(W\) itself can change.
It is therefore *incorrect* to require the operator norms computed from
\(W\) to equal one archived floating-point reference to \(10^{-12}\)
for every BLAS kernel, although each \(W\) satisfies the same stated
continuity inequalities. The two machines must not be represented as
having generated identical data.

## Exact reverse-kernel baseline

Define the entrywise reverse product

\[
\mathcal R(X)_{x,y}=X_{x,y}\,\overline{X_{y,x}},
\]

not the matrix product \(XX^*\). Since

\[
A-A^{\mathsf T}=\begin{pmatrix}0&2\\-2&0\end{pmatrix}
\]

is nonsingular modulo either prime, one has the exact expression

\[
\mathcal R(V)_{x,y}
=p^{-2}\exp\left(\frac{2\pi i}{p}
f(x)^{\mathsf T}(A-A^{\mathsf T})f(y)\right).
\]

By orthogonality of additive characters, the rows of this matrix
are orthogonal, with squared row norm \(p^2\cdot p^{-4}=p^{-2}\).
Therefore **exactly**, without a floating Schur basis,

\[
\boxed{\|\mathcal R(V)\|_{\mathrm{op}}=\frac1p.}
\]

For matrices \(X,Y\), the spectral operator norm obeys
\(\|X\circ Y\|_{\mathrm{op}}\le
\|X\|_{\mathrm{op}}\|Y\|_{\mathrm{op}}\): the Hadamard product is a
compression of the tensor product. For unitary \(W,V\), expanding
\(\mathcal R(W)-\mathcal R(V)\) into two Hadamard differences gives

\[
\|\mathcal R(W)-\mathcal R(V)\|_{\mathrm{op}}
\le 2\|W-V\|_{\mathrm{op}}.
\]

The same argument for \(P(X)_{x,y}=|X_{x,y}|^2\) yields
\(\|P(W)-P(V)\|_{\mathrm{op}}\le2\|W-V\|_{\mathrm{op}}\).
Since \(P(V)=J_{p^2}\) and \(V_{\rm ref}\) is the original numerical
root reconstruction, write

\[
\varepsilon=\|W-V_{\rm ref}\|_{\mathrm{op}},
\qquad
\eta=\|V_{\rm ref}-V\|_{\mathrm{op}}.
\]

Consequently the following finite, **Schur-basis-invariant bounds**
hold for *every* such valid \(W\):

\[
\boxed{
\bigl|\|\mathcal R(W)\|_{\mathrm{op}}-p^{-1}\bigr|
\le2(\varepsilon+\eta),
\qquad
\|P(W)-J_{p^2}\|_{\mathrm{op}}
\le2(\varepsilon+\eta).
}
\]

These are bounds independent of the chosen degenerate Schur basis;
they are not statements that the \emph{values} of the perturbed norms
are identical on every machine.

## Precisely scoped portable replay

The [portable successor](../computations/verification/wave2_portable_replay.py)
runs the original eight Wave2 tasks through their unchanged, authenticated
v1 execution adapter. It changes **neither** old source bytes nor old
reference tolerances, raw outputs, hash closures or original numerical
assertions. The new acceptance policy supplements the original strict
inequalities and uses an explicit \(2\cdot10^{-12}\) floating arithmetic
margin on the two boxed structural bounds; the archived
\(\eta<2\cdot10^{-12}\) and \(\|P(W)-J\|\le2\,\text{bound}
+4\cdot10^{-12}\) conditions remain checked verbatim. The other
declared numeric fields still use their exact original 1e-12 reference
tolerance, and nonnumeric fields remain strict typed exact.

Only these four field paths have the new structural acceptance rule:
\`/floating_split_controls/0/reverse_norm\`,
\`/floating_split_controls/0/P_centered_norm\`,
\`/floating_split_controls/1/reverse_norm\`,
and \`/floating_split_controls/1/P_centered_norm\`.
The complete observed and expected raw payloads are retained with hashes,
and the v2 manifest labels the **historical exact-reference equality**
separately (including a negative verdict when it fails). A future change
to the field list, original sample primes, original numeric inequalities
or pinned source hashes fails closed.

The problem originally diagnosed in
[the reproducibility issue](https://github.com/ChurilovMaksim/BGS/issues/27)
was an over-specific, noncanonical numerical equality. This correction
makes the **finite verification criterion**, not the particular Schur
eigenbasis, portable. It does **not** establish signed Heisenberg-scale
spectral cancellation or the microscopic Sine₂ limit.
