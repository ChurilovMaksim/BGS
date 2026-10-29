# Local antiunitary for a position-diagonal kick

**Claim ID:** `BGS-TRACE-130`.
**Status:** project proof of an antiunitary identity and of two symbol energies. The orthogonal-class name is a heuristic, not a form factor. Python and C++ recompute the symbol energy and check the symmetric conjugate and the momentum sine numerically, including at \(N=3,5,7\). Lean decides the integer energy and the cross-multiplication \((1\cdot 4+1\cdot 4)\cdot 2=1\cdot(4\cdot 4)\) of \(1/4+1/4=1/2\). Equality of rational numbers does not reduce under `decide` here. It does not formalize the antiunitary. No external referee.

`BGS-TRACE-126` supplies the symbol, Egorov, and the symmetry \(M_N^T=M_N\), \(M_N^{-1}=\overline{M_N}\). `BGS-TRACE-005` and `BGS-BGS-001` remain **open**. This note does not prove a COE or CUE form factor.

## 1. Statements

Let \(N\ge 3\) be odd. The operators \(M_N\), \(T_N\) and the phased symbol \(A_N(\varphi)\) are those of `BGS-TRACE-126`. Position conjugation \(K_0\) acts on the position basis by complex conjugation, so \(K_0TK_0=\overline T\) as matrices. The report of 29 October 2026 records numerical form factors; it is not an input.

**Theorem 1 (position-diagonal antiunitary).** Let \(A^{\mathrm{diag}}(\varphi)\) be the sum of the modes with displacement \(\ell=0\). It is a real diagonal matrix. For every real \(\eta\) and every phase vector \(\varphi\), write \(D=\exp(i\eta A^{\mathrm{diag}}(\varphi))\) and \(U=DM_N\). The antiunitary \(\Theta=DK_0\) satisfies
\[
\Theta^2=I,\qquad \Theta U\Theta^{-1}=U^\dagger.
\]
The same identity holds for every real diagonal kick, including one with an extra position sine, because that kick still has a diagonal unitary exponential. The name "orthogonal class" is the heuristic attached to an antiunitary of square \(1\). It is not a theorem that the form factor equals the circular orthogonal formula. It does not exclude a circular unitary form factor: a symmetric unitary can carry that form factor.

**Theorem 2 (momentum row and momentum sine).** The modes with displacement \(\ell=1\) have symbol energy
\[
\sum_k\lvert c_{1,k}\rvert^2=\frac{9}{160000},
\]
and the modes with \(\ell=-1\) have the same energy, hence \(9/80000\) together. The coefficient is \(4000\,c_{1,k}=(-3-4i)\,r(k)\). For the row \(\ell=-1\) the imaginary part changes sign, so \(4000\,c_{-1,k}=(-3+4i)\,r(k)\).

The full symbol fails to be \(K_0\)-even for almost every phase, and it is \(K_0\)-even for some phases. Positive energy does not by itself decide which.

Let \(B_N=(T_N(1,0)-T_N(-1,0))/(2i)\). Then \(B_N\) is Hermitian and \(K_0B_NK_0=-B_N\). Its symbol energy is \(1/2\). For every real \(\varepsilon\ne 0\) and every position-diagonal \(A^{\mathrm{diag}}\), the kick \(A^{\mathrm{diag}}+\varepsilon B_N\) is not a function of position, so the antiunitary argument of Theorem 1 does not apply to \(e^{i\eta(A^{\mathrm{diag}}+\varepsilon B_N)}M_N\). The form factor of that ensemble is not identified.

**Boundary.** Neither theorem evaluates \(\mathbb E\lvert\operatorname{Tr} U^m\rvert^2\) for \(m\ge 2\). The time-one coefficient remains the statement of `BGS-TRACE-129`: it equals \(1+\rho_1\) inside the window of `BGS-TRACE-126`. The samples at \(N=201\) and \(N=203\) are not used. The scale \(\eta^2 N\cdot 9/160000\) is not derived. `BGS-TRACE-005` and `BGS-BGS-001` remain open.

## 2. The antiunitary

A mode \((0,k)\) is multiplication by \(e_N(kx)\). The phased diagonal symbol is a real linear combination of cosines, hence a real diagonal matrix \(A^{\mathrm{diag}}\). Its exponential \(D\) is diagonal and unitary.

`BGS-TRACE-126`, Section 5, records that \(M_N\) is symmetric, so \(\overline{M_N}=M_N^\dagger\). Let \(K_0\) be complex conjugation in the position basis. Then \(K_0DK_0=\overline D=D^{-1}\), and
\[
\Theta^2=D(K_0DK_0)=I.
\]
Since \(\Theta^{-1}=\Theta\),
\[
\Theta(DM_N)\Theta
=D\,K_0(DM_ND)K_0
=\overline{M_N}\,\overline D
=(DM_N)^\dagger.
\]
The same calculation uses only that the kick exponential is a diagonal unitary and that \(M_N\) is symmetric and unitary. An extra position sine keeps the kick real and diagonal, so it keeps the antiunitary.

The symmetric conjugate \(\Sigma_D=D^{1/2}M_ND^{1/2}\) satisfies \(\Sigma_D^T=\Sigma_D\), and \(DM_N=D^{1/2}\Sigma_D D^{-1/2}\). That similarity does not assign a class. Every unitary is unitarily similar to a diagonal matrix, and every matrix is similar to its transpose. Tanner, Journal of Physics A 34 (2001), Section IV.1, reports the orthogonal ensemble for uniform star graphs with a symmetric Fourier matrix. That report is the closest prior heuristic for the antiunitary above. It is not an input of the identity, and it is not a form factor for this cat map.

## 3. The momentum row

The coefficient routine of `BGS-TRACE-126`, as implemented by `computations/verification/sixteen_phase_symmetry.py`, gives, for \(\ell=1\),
\[
4000\,c_{1,k}=(-3-4i)\,r(k),\qquad
\lvert 4000\,c_{1,k}\rvert^2=25\,r(k)^2,
\]
where \(r(0)=4\), \(r(\pm 1)=2\), \(r(\pm 7)=-2\), \(r(\pm 6)=r(\pm 8)=-1\), and \(r(k)=0\) otherwise. The sum of squares is
\[
16+4+4+4+4+1+1+1+1=36,
\]
so \(\sum_k\lvert 4000\,c_{1,k}\rvert^2=25\cdot 36=900\) and
\[
\sum_k\lvert c_{1,k}\rvert^2=900/4000^2=9/160000.
\]
The \(\ell=-1\) formulae replace \(-4i\) by \(+4i\), and the squared moduli agree. A first draft wrote \((-3+4i)\) on the row \(\ell=1\). That sign is the row \(\ell=-1\).

\(K_0T_N(a,b)K_0=T_N(a,-b)\), because conjugation sends the phase \(e_N(b(x+2^{-1}a))\) to its conjugate and replaces \(b\) by \(-b\). Every \(\ell=0\) mode is fixed as a function of position once its phase makes the cosine real, which it does for every phase of a cosine. A mode \((1,k)\) is sent to \((1,-k)\). Whether the full linear combination is fixed depends on the phases. The energy being positive does not forbid a choice of phases that makes \(A_N(\varphi)\) real. The referee audit of 29 October 2026 records one such choice: the phases fixed by \(e^{2i\varphi_0}=\overline c/c\) and by the sums \(\varphi_k+\varphi_{-k}\) for \(k\in\{1,6,7,8\}\) make \(A\) real, with imaginary part at roundoff on \(N=11\), and then \(U^T=MU M^{-1}\). Those constraints do not hold for every phase. The full symbol therefore fails to be \(K_0\)-even for almost every \(\varphi\), and it is \(K_0\)-even for some \(\varphi\).

The matrix \(T_N(1,0)\) is the permutation of the cycle \(x\mapsto x+1\), with every phase equal to \(1\), and \(T_N(-1,0)\) is its transpose. Both are real, so
\[
B_N=\frac{T_N(1,0)-T_N(-1,0)}{2i}
\]
is Hermitian, and \(\overline{B_N}=-B_N\). Thus \(K_0B_NK_0=-B_N\). The symbol of \(B_N\) is the pair of coefficients \(1/(2i)\) and \(-1/(2i)\), with squared moduli \(1/4+1/4=1/2\).

If \(A^{\mathrm{diag}}\) is real diagonal and \(\varepsilon\ne 0\) is real, then \(A^{\mathrm{diag}}+\varepsilon B_N\) is not a multiplication operator in the position basis. Theorem 1 used that the kick was a function of position. That hypothesis fails, and the antiunitary of Theorem 1 is not claimed for this kick.

## 4. Self-audit

An antiunitary of square \(1\) with \(\Theta U\Theta^{-1}=U^\dagger\) is the standard heuristic for orthogonal statistics. It does not imply that the spectral form factor equals the COE formula. The same symmetry does not exclude the CUE form factor. A unitary of the shape \(O^T\Lambda O\), with \(O\) orthogonal and with the eigenvalues of a CUE matrix on the diagonal of \(\Lambda\), is symmetric and has the CUE form factor. Theorem 1 does not exclude that possibility, and it does not prove the orthogonal form factor. The position-diagonal ensemble may still carry arithmetic spikes at times that divide the order of \(S\).

The energy \(9/160000\) is the squared \(\ell^2\) norm of one row of the symbol, not an eigenvalue spacing. The golden-rule scale \(\eta^2 N\cdot 9/160000\) is not derived here. No crossover law is stated.

The time-one value \(1+\rho_1\), rather than \(2\), is `BGS-TRACE-129` inside its perturbative window. It is not re-proved, and it is not extended to large \(\eta\). The asymmetry at \(N=201\) and \(N=203\) is outside this note.

A same-day referee correction deleted the sentence that a CUE form factor is incompatible with similarity to a symmetric unitary, replaced that similarity by the antiunitary \(\Theta=DK_0\), restricted the failure of \(K_0\)-evenness to almost every phase, and corrected the sign of \(c_{1,k}\).

## 5. Certificates

- `computations/verification/sixteen_phase_symmetry.py`
- `computations/cpp/sixteen_phase_symmetry.cpp`
- `formalization/Bgs/SixteenPhaseSymmetryRational.lean`
- `evidence/executions/20261029/sixteen-phase-symmetry/README.md`

The programs check the energy identity, the symmetry of \(D^{1/2}M_ND^{1/2}\) for random real diagonal phases at \(N=3,5,7,11\), and the identities \(\overline{B_N}=-B_N\) and \(B_N^\dagger=B_N\) at those dimensions. A pass does not prove the antiunitary, a COE form factor, a CUE form factor, `BGS-TRACE-005`, or `BGS-BGS-001`.
