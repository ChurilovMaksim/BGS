# Frozen kick: an exact full-rank obstruction to sparse comparison

Stable claim ID: `BGS-FM-005`. Date: 2026-09-23. Status: elementary deduction for the actual frozen generator; not a BGS proof, not a novelty claim. Derived against the current corpus at `c56c9db3f985872206501e1545678da940dad89c`; the inherited single-chain observation and external source are credited below.

## Target and provenance

The target remains `BGS-TRACE-005`: Heisenberg-scale weighted joint traces for the fixed family

\[
 U_N=e^{i\tau N A_N}M_N,\qquad \tau=10^{-80},\quad N\ge3\text{ odd},
\]

with the exact raw modular Weyl convention and symbol in `mathematics/fixed_map_resolvent_frontier.md`.

The corpus already knows the Jacobi representation and its single cut when `gcd(N,7)=1`: see `supplement/fixed_map/weighted-secular/attempt.md`, section “Independent representation check”, and `supplement/fixed_map/weighted-secular/jacobi_audit.py`. It also knows the Lindemann--Weierstrass scalar-return obstruction. The deduction below combines those existing facts, extends the cut count to all odd dimensions, and states an explicit rank obstruction. It is a small structural result, not a new universality mechanism.

## 1. Exact chain decomposition in every odd dimension

Put

\[
 r(q)=(1-\cos14\pi q)(1+\cos2\pi q),\quad
 e^{i\alpha_0}=(-3+4i)/5,
\]

and write `h=2^{-1} mod N`. Directly from the Weyl formula, the only off-diagonal entries are

\[
 (A_N)_{x,x+1}=\frac{e^{-i\alpha_0}}{200}r((x+h)/N),
 \qquad (A_N)_{x+1,x}=\overline{(A_N)_{x,x+1}},
\]

where residues are reduced modulo N. The diagonal is

\[
 d_x=\cos(14\pi x/N)+r(x/N)/10
       +r(x/N)\sin(2\pi x/N)/100-1/10.
\]

For odd N, `1+cos(2πy/N)` is strictly positive on the grid. Therefore a bond is zero exactly when `7(x+h)=0 mod N`. There are

\[
 d=\gcd(N,7)\in\{1,7\}
\]

such bonds. They are equally spaced, so the cycle separates into d paths, each of length N/d. A diagonal unitary gauge makes all internal bonds real and strictly positive. Thus A_N is unitarily equivalent to a direct sum of d irreducible real Jacobi matrices.

Every eigenvalue of an irreducible Jacobi matrix is simple: its first coordinate cannot vanish (the first row and then the successive rows force every coordinate to vanish); the eigenvector recurrence uniquely determines all remaining coordinates from the first. A Hermitian matrix is diagonalizable, so geometric simplicity is algebraic simplicity. Consequently

\[
 \boxed{\max_{\lambda}\dim\ker(A_N-\lambda I)\le d.}
\tag{1}
\]

In particular A_N has simple spectrum for every odd N not divisible by 7. When N=7 all paths have length one and `A_7=(9/10)I`, so the bound is sharp there. No simplicity of U_N follows.

## 2. The actual exponential is never an exact sparse perturbation

Every entry and every eigenvalue of A_N is algebraic. For any nonzero real algebraic t, distinct eigenvalues λ and μ remain distinct after exponentiation: equality would give

\[
 e^{it(\lambda-\mu)}=1,
\]

contradicting the Hermite--Lindemann theorem, since its exponent is nonzero algebraic. This is the standard theorem already imported in the repository's algebraic-return proof, not a new transcendence result.

For every complex z,

\[
\begin{split}
 \operatorname{rank}(U_N-zM_N)
 &=\operatorname{rank}(e^{i\tau N A_N}-zI)\\
 &\ge N-\gcd(N,7).
\end{split}
\tag{2}
\]

This holds at the literal frozen `τ=10^-80`, for all odd N, with no small-coupling approximation. It also holds for every nonzero real algebraic τ. If `7∤N`, the rank is N except when z is one of the N distinct kick eigenvalues, when it is N−1.

Thus direct exact low-rank perturbation of a scalar multiple of the unperturbed cat factor is unavailable: an exact correction has rank at least N−7. The result does not exclude comparison after an N-dependent conjugacy, an approximate low-rank correction, a local spectral comparison, or a different comparison operator. Exact rank alone says nothing useful about the small singular values.

## 3. A quantitative but pre-wrapping bound for approximate rank

Here `||.||_HS` is unnormalized. For odd N≥19, Fourier orthogonality gives

\[
 \operatorname{Tr}A_N=0,\quad N^{-1}\operatorname{Tr}A_N^2=v_0
       =\frac{66033}{160000}.
\]

For a direct check, write `c_j=cos(2πjq)` and
`h=(9/10)c_7+(1/10)c_1−(1/10)c_7c_1`. Orthogonality gives
`∫h²=33/80`, `∫r² sin²(2πq)=15/16`, and `∫r²=9/4`.
The p-dependent cosine has square mean one half; every cross term vanishes by q parity or p integration. Thus
`v_0=33/80+(15/16)/10000+(9/4)/20000=66033/160000`.
The q support has radius at most 9 and the p support radius 1, so N≥19 excludes every nonzero difference-frequency alias.

This is the unaveraged symbol variance; it is deliberately different from the orbit-averaged constant `1650797/4000000` elsewhere in the corpus. The elementary symbol/operator estimate gives

\[
 \|A_N\|\le B:=79/50.
\]

For example the diagonal part has magnitude at most `1+4/10+4/100+1/10=77/50`, and the sum of the magnitudes of the two off-diagonal entries in a row is at most `4/100=1/25`, giving B by the Hermitian row-sum bound.

Let `t=τN`, assume `|t|B≤π`, and let R have rank at most r. The singular values of `e^{itA_N}−I` are `2|sin(tλ_j/2)|`. In the assumed range they are at least `2|tλ_j|/π`. The best rank-r approximation removes at most r eigen-directions. Since each `λ_j²≤B²`, the Eckart--Young variational bound gives

\[
 \boxed{\frac1{\sqrt N}\|U_N-M_N-R\|_{HS}
 \ge\frac{2|t|}{\pi}
     \sqrt{\max(0,v_0-rB^2/N)}.}
\tag{3}
\]

To see the application to U_N, right-multiply by `M_N*`; rank and Hilbert--Schmidt norm are invariant. The removal argument is valid even if the largest `|sin(tλ/2)|` are ordered differently from the largest `|λ|`: any r removed indices carry at most `rB²` squared generator mass.

Equation (3) gives a relative, order-|t| lower bound against corrections of rank `o(N)` in the pre-wrapping range. It is not a fixed-τ asymptotic estimate as N→∞ because `|τ|NB≤π` eventually fails. Extrapolating it beyond that range would be invalid.

## 4. Missing implication

Neither (1), (2), nor (3) controls the eigenvectors coupling A_N to M_N, the signed principal-minor weights, or mixed traces at m proportional to N. Those are exactly the ingredients needed by the frozen pair/loop criterion. The small result rules out one direct exact sparse-comparison tactic and clarifies its approximate version; it does not establish or refute the fixed-map BGS limit.

## 5. Internal verification

The mathematical proof of (1) is the elementary eigenvector recurrence; (2) imports Hermite--Lindemann; (3) is the singular-value variational inequality. The separately executed `computations/verification/frozen_kick_rank.py` compares the trigonometric chain assembly against the existing Fourier assembly, with the integer modular criterion supplying the exact zero-bond pattern. Its auxiliary exponential parameter is moderate; double precision at `τ=10^-80` would falsely return an identity kick. Numerical output is diagnostic only and is recorded separately.

Executed diagnostics: 12 odd dimensions from 3 through 77; 7 alias-free variance checks; 28 best-rank residual comparisons. All passed. Maximum Fourier/chain assembly entry discrepancy was `7.203e-15`. These data do not certify transcendence or asymptotic spectral statistics.
