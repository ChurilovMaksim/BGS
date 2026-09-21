# Local jet obstruction to a purely fixed-point proof of resonance nondegeneracy

Date: 21 September 2026.

Status: exact local polynomial construction. It is deliberately not a torus observable and not a counterexample to the global analytic resonance problem.

Let

\[
S(u,z)=(\lambda u,\lambda^{-1}z),\qquad \lambda>1,
\]

and put

\[
a=\sqrt{\frac{\lambda^2+\lambda^{-2}}2},
\]

\[
G(u,z)=\bigl(u^2-z^2+a\,uz\bigr)^2+u^2z^2.
\tag{1}
\]

Then \(G\ge0\), and the origin is a strict isolated minimum. Nevertheless the nonzero local Poisson bracket built from \(G\) and \(G\circ S\) is an analytic polynomial coboundary.

Indeed, direct expansion of the bracket gives a homogeneous polynomial of degree six. For a monomial \(u^rz^s\), the cohomological operator \(V\mapsto V-V\circ S\) multiplies its coefficient by \(1-\lambda^{r-s}\). The only possible resonance at degree six is the \(u^3z^3\) term. Its coefficient cancels exactly because

\[
a^2=\frac{\lambda^2+\lambda^{-2}}2.
\tag{2}
\]

Every remaining monomial has \(r\ne s\), so division by \(1-\lambda^{r-s}\) produces a polynomial transfer \(V\). The bracket is not identically zero: its \(u^6\) coefficient is

\[
8a(\lambda^2-\lambda^4)\ne0.
\tag{3}
\]

For the project eigenvalue \(\lambda=3+2\sqrt2\), one has \(a=\sqrt{17}\).

This construction shows that local Taylor data at a hyperbolic fixed point, even with a strict local minimum and a visibly nonzero bracket, cannot by itself prove the global torus non-coboundary statement. Global Fourier/orbit information is essential. It does not answer whether the periodic analytic equation on \(\mathbb T^2\) has a nonconstant solution.
