> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_oldspace_audit.md`. Embedded SHA256: `c130a9bc6221b8bca2f2103e14c519f5cda2b540d9b204c51621176b19df1e0e`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).


# Independent audit of canonical-old-space escape

Date: 20 October 2026. Auditor: `/root/all_time_adversarial`.

## Frozen input and verdict

Audited file: `arithmetic_oldspace_escape.md`.

Final SHA256: `596d44605310cc898fa75e23df4aa811189a1764fed21ce8b9f5d07ae734813a`.

The previous hash `541407aa544981ed42aa4f836cff5bf61bb02b4d56adc045bc8d3253b8b0d4d7` was read in full. The sole subsequent change replaced DX,DY by ∇X,∇Y in the derivative bounds, to avoid confusing differentiation with D=X−Y. No mathematical claim changed.

**Verdict: all three old-space theorems and consequence (8.2) are proved as written.** The second-order finite-field simplicity certificates are outside this audit's computational scope; I checked the exponential-polynomial transfer used by the exact old-space minor, but did not rerun those finite-field computations.

The strongest result audited here is the actual fixed-parameter limit, for every fixed odd d≥3 and all odd m→∞, N=d²m:

$$
\frac1N\operatorname{Tr}(P_{d,m}U_N^*P_{d,m}U_N)\longrightarrow d^{-4}.
$$

It is an asymptotic theorem about the original matrices at τ=10^{-80}. It does not replace τ by a shrinking parameter or average over it. Its normalization corresponds to mean retained squared norm d^{-2} on the old subspace of dimension m.

## 1. Exact finite identities and the fixed-parameter minor

The embedding has value d^{-1/2}φ(y mod m) at x=dy and zero elsewhere. Each input coordinate occurs d times, so J*J=I_m.

In M_NJ, write y=d(v+jm), with 0≤v<m, 0≤j<d. The j-dependent quadratic phase reduces to e_d(2 bar8 xj). Since 2 bar8 is a unit modulo d, its sum vanishes unless d divides x. For x=du it equals d, and the remaining phase is the defining M_m phase. The normalization is

$$
d/(\sqrt N\sqrt d)=1/(\sqrt d\sqrt m).
$$

Therefore M_NJ=JM_m exactly, including composite m and m=1. In particular M_N commutes with the orthogonal old-space projector P.

The prescribed modular Weyl quantization gives the exact Jacobi coefficient

$$
(A_N)_{x,x+1}=w_x=e^{-i\alpha_0}r((x+\bar2)/N)/200.
$$

For the selected rows x_u=du−1, only the neighbor x_u+1 belongs to dZ. The other neighbor does not, since d≥3. This also holds at the cyclic seam. Thus RA_NJ is the displayed diagonal matrix.

For y=du−1+bar2, 2y≡−1 mod d, so gcd(y,d)=1. On an odd N-grid, r(y/N)=0 exactly when N divides 7y: the other cosine factor cannot vanish. Such a zero would imply d² divides 7, which is impossible for d≥3. The selected diagonal minor is therefore invertible at first order.

Let F(t)=det(R exp(tA_N)J). Its first nonzero Taylor coefficient is the nonzero product of those diagonal entries, at degree m. The spectral projectors of the algebraic Hermitian matrix A_N are polynomials in A_N with algebraic coefficients. Consequently F is a finite exponential polynomial with algebraic coefficients and algebraic frequencies. After collecting equal frequencies, at least one coefficient is nonzero.

The external theorem required at this point is exactly the Lindemann–Weierstrass assertion that exponentials of distinct algebraic numbers are linearly independent over the algebraic numbers. I opened the published chapter and checked the precise statement in the author's manuscript, Theorem 3.2, printed pages 14–15:

- S. A. Popescu, *A Simple and Self-contained Proof for the Lindemann-Weierstrass Theorem*, published chapter DOI [10.1007/978-3-031-51959-8_16](https://link.springer.com/chapter/10.1007/978-3-031-51959-8_16).
- [Author manuscript, Theorem 3.2](https://arxiv.org/pdf/2306.14352).

At every nonzero algebraic t, the collected exponents βt remain distinct algebraic numbers. The theorem therefore gives F(t)≠0, including t=iNτ. This is a valid transition from a nonzero infinitesimal minor to the specified fixed parameter; no small-time Taylor remainder estimate is used in that transition.

Since RU_N(z)J=R exp(iNzA_N)J M_m is invertible and R vanishes on the old subspace, U_N(z)H_old∩H_old={0}. Lindemann–Weierstrass does not provide a quantitative principal-angle lower bound, and none is asserted.

## 2. The uniform generator estimate includes the exceptional divisor 7

The support neighborhoods of radius one around distinct multiples of d are disjoint for d≥3. The projection back to H_old only averages duplicated centers belonging to the same input column. Thus the Gram matrix of QA_NJ is diagonal, with entries exactly given by the variance-plus-two-escape-terms formula (4.1).

For odd d≠7, the d-point mean of cos(14πq) is zero and its mean square is 1/2. The decomposition

$$
V(q)=0.9\cos(14\pi q)+W(q),\qquad |W|\le6/25
$$

gives the stated lower bound on the diagonal variance after projecting away constants. This uses discrete Fourier orthogonality, which remains valid when N is small enough for some original Fourier modes to alias: the exact sample formula itself is the object being evaluated.

For d=7, the first cosine is constant over the duplicated positions, so this variance argument must be replaced. The audited exact formula is

$$
\mathcal E_7=\frac{81}{16000}(1-C)^2
+\frac3{80000}\big[(1+\cos(t-\delta))^2+(1+\cos(t+\delta))^2\big].
$$

The coefficient 81/16000 comes from the squared orthogonal frequencies 1 and 2 of the diagonal variation. The two off-diagonal terms have mean square 3/2 in their remaining cosine factor. Both modular half shifts are present, giving δ=7π/N rather than zero.

As N≥49, cos δ>0. If C≥0, convexity of the square bounds the bracket below by 2. If C<0, the first term alone is at least 81/16000. Thus every Gram entry is at least 3/40000 and

$$
\|QA_NJ\phi\|\ge\sqrt3\|\phi\|/200.
$$

The finite-time Taylor consequence is valid only for |Nτ| below its stated constant. The source explicitly does not use that finite range as an asymptotic theorem.

## 3. The Egorov convention and its error are correct

The ordinary Weyl matrices use real halves and satisfy

$$
W_N(v)W_N(w)=e^{\pi i\sigma(v,w)/N}W_N(v+w),
\quad \sigma(v,w)=lk'-kl'.
$$

Their relation to the prescribed quantization is T_N(l,k)=(-1)^{kl}W_N(k,l). Thus the ordinary symbol is exactly

$$
a(q,p)=V(q)+r(q+1/2)\cos(2\pi p-\alpha_0)/100.
$$

The shifted mixed term is necessary. With X=(a_p∂_q−a_q∂_p)/(2π), the sine expansion gives

$$
iN[A_N,\operatorname{Op}_N(b)]
=\operatorname{Op}_N(Xb)+O_b(N^{-2}).
$$

The factor N from the generator is included: the commutator's cubic sine remainder is O(N^{-3}) before that factor. Its Fourier sum converges because a has finite support and b is smooth. Duhamel's formula then proves, for fixed s,

$$
E_N(s)\operatorname{Op}_N(b)E_N(s)^*
=\operatorname{Op}_N(b\circ\Phi_s)+O_{b,s}(N^{-2}).
$$

The source consistently uses F Op(b) F*, rather than the opposite conjugation. With that convention, the inside-out composition for F=T_gE* T_hE produces

$$
\kappa_{g,h}=\Phi_\tau\circ t_h\circ\Phi_{-\tau}\circ t_g,
\quad t_g(q,p)=(q+\alpha/d,p-\beta/d).
$$

No change of sign or cyclic conjugation is needed in the final version.

## 4. The normalized trace lemma needs only fixed-time Egorov

For a unitary F_N, put L_N(b)=N^{-1}Tr(Op_N(b)F_N). Hilbert–Schmidt Cauchy–Schwarz gives limsup|L_N(b)|≤||b||_2. Any subsequential limit on a countable dense collection of test polynomials therefore extends to an L² functional with norm at most one.

If F_N Op_N(b)F_N*=Op_N(b∘κ)+o(1), the symbol-product estimate and trace cyclicity imply

$$
L_N(c(b\circ\kappa))=L_N(cb)+o(1)
$$

for every fixed smooth b,c. Thus the limiting L² density is supported on the simultaneous zeros of b∘κ−b. Taking the two coordinate characters identifies that set with Fix κ. If Fix κ has measure zero, every such limit is zero, proving Tr F_N/N→0.

This support argument is valid for a fixed map κ. It is not a long-time Egorov assertion. For a nonidentity real analytic torus map, the fixed set has measure zero by the local analytic-zero-set/Fubini argument included in the source. Both real analyticity and nonidentity are separately verified in the next step.

## 5. Exclusion of a translation relation at the exact small time

If κ_{g,h}=Id, the equivariant lift F of Φ_τ obeys F(z+η)=F(z)−γ+n for a constant integer n. Iterating d times, using dη integral and lift equivariance, gives η+γ integral. Thus the time map commutes with t_h.

It would not suffice simply to differentiate this equality at τ, because equality at one time does not generally imply equality of generators. The source supplies a relative estimate that repairs precisely that problem.

For X and its translate Y, set D=X−Y. The fixed finite Fourier support gives

$$
\|\nabla D\|_\infty\le4000\|D\|_\infty.
$$

This bound is uniform even as the translation tends to zero: each Fourier coefficient is bounded by ||D||∞, and the number and maximum frequency of those coefficients are fixed. Using ||X||,||Y||≤20 and their derivative bounds ≤2000 in the integral equations for the lifted flows yields

$$
\|F_X^s-F_Y^s-sD\|_\infty
\le\tfrac12s^2(80000+2000e^{2000s})\|D\|_\infty.
$$

At s=τ=10^{-80}, the error is strictly smaller than the leading s||D|| term unless D=0. Equal torus time maps have equal lifts here, because both lifts are within 20τ of the identity. Therefore their equality forces X=Y.

Finally, the actual corrected symbol has nonzero coefficients at (1,0) and (0,1): 1/20−i/200 and e^{-iα_0}/200. Neither Fourier mode is killed by taking its Hamiltonian vector field. A translation preserving X must therefore have both coordinates integral. This proves h=0 and then g=0.

This argument uses a property of the actual symbol, not merely hyperbolicity or mixing. Its conclusion is still limited to the one-step relation proved in the source.

## 6. Group average, normalization, and almost-old eigenvectors

The subgroup matrices T_g form an honest representation: their finite Weyl cocycle is trivial because (dm)²=Nm. Their average is exactly P. Averaging modulations forces x to be divisible by d; averaging shifts averages the d duplicated copies.

After commuting M_N past P and using cyclicity,

$$
\frac1N\operatorname{Tr}(P U_N^*P U_N)
=\frac1{d^4}\sum_{g,h}\frac1N\operatorname{Tr}(T_gE_N^*T_hE_N).
$$

For fixed d this contains a fixed finite number of terms. Only g=h=0 has the identity canonical map and contributes 1; the normalized trace lemma makes every other term tend to zero. This proves the d^{-4} normalization and the retained fraction d^{-2}.

For an eigenvector ψ with ||Pψ||²≥1−ε,

$$
\|PUP\psi\|\ge\|P\psi\|-\|Q\psi\|
\ge\sqrt{1-\varepsilon}-\sqrt\varepsilon.
$$

For an orthonormal eigenfamily, the vectors Pψ form a Bessel family. Summing the squares of this inequality is bounded by ||PUP||²_HS. The displayed estimate (8.2) follows. It is an upper bound for an almost-old subfamily, not a uniform escape estimate for every eigenvector.

## Scope retained

No effective N rate, no uniformity as d grows, and no positive minimum principal angle at fixed τ have been established. The overlap is a bounded deterministic one-step observable; its limit does not evaluate the weighted products of power traces at times proportional to N required by H_diag.


---

