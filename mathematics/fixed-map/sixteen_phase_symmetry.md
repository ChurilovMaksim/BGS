# Symmetry class of the sixteen-phase ensemble

**Claim ID:** `BGS-TRACE-130`.
**Status:** project proof. The orthogonal similarity for every position-diagonal realization, and the exact momentum-row energy, are proved below. Python and C++ recompute the symbol energy and check the similarity numerically, including at \(N=3,5,7\). Lean decides the integer energy. It does not sum a form factor. No external referee.

`BGS-TRACE-126` supplies the symbol, Egorov, and the symmetry \(M_N^T=M_N\), \(M_N^{-1}=\overline{M_N}\). `BGS-TRACE-005` and `BGS-BGS-001` remain **open**. This note does not prove a COE or CUE form factor.

## 1. Statements

Let \(N\ge 3\) be odd. The operators \(M_N\), \(T_N\) and the phased symbol \(A_N(\varphi)\) are those of `BGS-TRACE-126`. Position conjugation \(K_0\) acts on the position basis by complex conjugation, so \(K_0TK_0=\overline T\) as matrices. The report of 29 October 2026 records numerical form factors; it is not an input.

**Theorem 1 (position-diagonal ensemble).** Let \(A^{\mathrm{diag}}(\varphi)\) be the sum of the modes with displacement \(\ell=0\). It is a real diagonal matrix. For every real \(\eta\) and every phase vector \(\varphi\), the unitary
\[
U=e^{i\eta A^{\mathrm{diag}}(\varphi)}M_N
\]
is similar to a symmetric unitary. Explicitly, if \(D=e^{i\eta A^{\mathrm{diag}}(\varphi)}\) and \(D^{1/2}=e^{i\eta A^{\mathrm{diag}}(\varphi)/2}\), then
\[
U=D^{1/2}\bigl(D^{1/2}M_ND^{1/2}\bigr)D^{-1/2}
\]
and \(D^{1/2}M_ND^{1/2}\) is symmetric. Every realization lies in the orthogonal class. A CUE form factor is incompatible with this symmetry. A COE form factor is compatible with it and is not proved.

**Theorem 2 (momentum breaking).** The modes with displacement \(\ell=1\) have symbol energy
\[
\sum_k\lvert c_{1,k}\rvert^2=\frac{9}{160000}.
\]
The modes with \(\ell=-1\) have the same energy. Position conjugation fixes every \(\ell=0\) mode and does not fix the pair \(\ell=\pm 1\). Thus the full symbol is not \(K_0\)-even.

Let \(B_N=(T_N(1,0)-T_N(-1,0))/(2i)\). Then \(B_N\) is Hermitian and \(K_0B_NK_0=-B_N\). Its symbol energy is \(1/2\). For every real \(\varepsilon\) and every position-diagonal \(A^{\mathrm{diag}}\), the kick \(A^{\mathrm{diag}}+\varepsilon B_N\) has \(K_0\)-odd part \(\varepsilon B_N\). For \(\varepsilon\ne 0\) this kick is not \(K_0\)-even, so the similarity of Theorem 1 does not apply to \(e^{i\eta(A^{\mathrm{diag}}+\varepsilon B_N)}M_N\). The form factor of that ensemble is not identified with the CUE form factor.

**Boundary.** Theorem 1 is the symmetry reason a position-only kick can stay orthogonal at every \(\eta\). Theorem 2 is the exact weight \(9/160000\) of the modes that break that symmetry in the sixteen-phase symbol, and the effect of an added momentum sine. Neither theorem evaluates \(\mathbb E\lvert\operatorname{Tr} U^m\rvert^2\) for \(m\ge 2\). The time-one coefficient remains the statement of `BGS-TRACE-129`: it vanishes, so the averaged squared trace equals \(1\) plus the remainder of `BGS-TRACE-126` inside that window, rather than the short-time orthogonal value \(2\). The samples at \(N=201\) and \(N=203\) are not used. `BGS-TRACE-005` and `BGS-BGS-001` remain open.

## 2. Position-diagonal similarity

A mode \((0,k)\) is multiplication by \(e_N(kx)\). The phased diagonal symbol is a real linear combination of \(\cos(2\pi kx/N+\varphi)\), hence a real diagonal matrix \(A^{\mathrm{diag}}\). Its exponential \(D\) is diagonal and unitary, and so is \(D^{1/2}\).

`BGS-TRACE-126`, Section 5, records that \(M_N\) is symmetric. Therefore
\[
\bigl(D^{1/2}M_ND^{1/2}\bigr)^T
=D^{1/2}M_N^TD^{1/2}
=D^{1/2}M_ND^{1/2},
\]
where the diagonal square root passes through the transpose. The product \(DM_N\) is the displayed conjugate of this symmetric unitary. A unitary similar to a symmetric unitary is similar to its transpose, which is the orthogonal class in the position basis. The argument uses every real \(\eta\) and every phase; it does not use a small-coupling expansion.

The same similarity applies to any real diagonal kick, including one with an extra position sine. A position sine does not break the orthogonal class.

## 3. The momentum row

The coefficient routine of `BGS-TRACE-126` gives, for \(\ell=1\),
\[
4000\,c_{1,k}=(-3+4i)\,r(k),\qquad
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
The \(\ell=-1\) formulae replace \(4i\) by \(-4i\), and the squared moduli agree.

\(K_0T_N(a,b)K_0=T_N(a,-b)\), because conjugation sends the phase \(e_N(b(x+2^{-1}a))\) to its conjugate and replaces \(b\) by \(-b\). Every \(\ell=0\) mode is fixed. A mode \((1,k)\) is sent to \((1,-k)\), which is not the same mode unless the coefficient satisfies the evenness relation forced by a \(K_0\)-even symbol. The computed energy is positive, so the full symbol is not even.

The matrix \(T_N(1,0)\) is the permutation of the cycle \(x\mapsto x+1\), with every phase equal to \(1\), and \(T_N(-1,0)\) is its transpose. Both are real, so
\[
B_N=\frac{T_N(1,0)-T_N(-1,0)}{2i}
\]
is Hermitian, and \(\overline{B_N}=-B_N\). Thus \(K_0B_NK_0=-B_N\). The symbol of \(B_N\) is the pair of coefficients \(1/(2i)\) and \(-1/(2i)\), with total squared modulus \(1/4+1/4=1/2\).

If \(A^{\mathrm{diag}}\) is \(K_0\)-even and \(\varepsilon\) is real, the odd part of \(A^{\mathrm{diag}}+\varepsilon B_N\) is \(\varepsilon B_N\). It is zero only for \(\varepsilon=0\). Theorem 1 used that the kick was a function of position. A nonzero multiple of \(B_N\) is not a function of position, and the square-root conjugation of that proof does not apply.

## 4. Self-audit

Similarity to a symmetric unitary does not imply that the spectral form factor equals the COE formula. The position-diagonal ensemble may still carry arithmetic spikes at times that divide the order of \(S\). Theorem 1 excludes a CUE identification for that sub-ensemble; it does not prove the orthogonal form factor.

The energy \(9/160000\) is the squared \(\ell^2\) norm of one row of the symbol, not an eigenvalue spacing. The golden-rule scale \(\eta^2 N\cdot 9/160000\) is not derived here. No crossover law is stated.

The time-one value \(1\), rather than \(2\), is `BGS-TRACE-129` inside its perturbative window. It is not re-proved, and it is not extended to large \(\eta\). The asymmetry at \(N=201\) and \(N=203\) is outside this note.

## 5. Certificates

- `computations/verification/sixteen_phase_symmetry.py`
- `computations/cpp/sixteen_phase_symmetry.cpp`
- `formalization/Bgs/SixteenPhaseSymmetryRational.lean`
- `evidence/executions/20261029/sixteen-phase-symmetry/README.md`

The programs check the energy identity, the vanishing of the odd part of every diagonal symbol, the matrix identity \(K_0B_NK_0=-B_N\) at \(N=3,5,7,11\), and the symmetry of \(D^{1/2}M_ND^{1/2}\) for random diagonal phases at those dimensions. A pass does not prove `BGS-TRACE-005` or `BGS-BGS-001`.
