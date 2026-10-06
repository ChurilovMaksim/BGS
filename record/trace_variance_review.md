# Independent audit: actual-model one-step trace variance and transcendence

Date: 6 October 2026. Reviewer scope: a fresh, independent internal mathematical
and computational audit. Canonical repository and frozen author overlay were
read-only. This report does not promote a theorem, alter the claim registry,
claim external peer review, or claim formal verification.

## Normalized claim and verdict

**Primary verdict: proved as written.** The phrase refers to the mathematical
statements below, with the explicitly registered external
Lindemann–Weierstrass input. No correction or additional arithmetic exclusion is
needed. The finite calculation is exhaustive because of the proved root-order
bound; the separate finite-dimensional matrix controls are not that proof.

For the unchanged raw modular matrices in
`BGS/mathematics/fixed_model_symmetry_theorem.md`, set

\[
 U_N(t)=e^{itA_N}M_N,\qquad
 H_N=\operatorname{Tr}(M_N)\operatorname{Tr}(A_N^2M_N)
       -\operatorname{Tr}(A_NM_N)^2.
\]

For every odd integer \(N\ge3\), \(H_N\ne0\) if and only if \(N\ne7\).
For every such \(N\ne7\) and every nonzero real algebraic \(t\),
\(|\operatorname{Tr}U_N(t)|^2\) is transcendental. At \(N=7\),
\(A_7=(9/10)I\) and the squared trace is exactly 1 for every real \(t\).
In particular the conclusion applies at \(t=10^{-80}N\).

The newly covered squared-trace family is **one step, odd \(7\mid N\),
\(N>7\)**. It includes all powers of five and seven without an additional
coprimality restriction. Away from seven, FM-008 already supplies this and
stronger nonzero-power conclusions. FM-010 already supplies trace
nonvanishing on the full odd sequence. Neither prior theorem is reclassified
or re-audited in its entirety here.

### Exact review target

- Frozen proof: `bgs_trace_variance_extension/candidate_proof.md`, SHA-256
  `fd44b578a4033c5e57f6d28ecb1b23365a06b7bd0cdb4bc7686e8fc33b83ab9d`.
- Frozen verifier: `bgs_trace_variance_extension/verify_trace_variance.py`, SHA-256
  `7f9cba3553121b7bb381f25729feeadcf81ee3cdde181f89d2ba96041423921f`.
- All 15 entries in its `SHA256SUMS` matched before the audit; they are also
  execution inputs with unchanged before/after hashes in the review manifest.
- Exact canonical raw-model hash:
  `32b2302c2567eebb75ff2231345e3336495ba8719517be6b5ce8734b416920c2`.
- Independent reconstruction: `reconstruct.py`, SHA-256
  `6006441580d08132b5cf243fc629f9cfd85037dc5def5d5626ea3084bcbd8600`.

All load-bearing canonical mathematical, coefficient-source, and external
registry files match the author's recorded hashes. The live
`record/claim_ledger.md` and `record/claims.json` changed after the author's
receipt; their observed hashes and dirty status are retained separately in
`canonical_source_check.json`. Their changed bytes are not silently treated as
the frozen author's snapshot. Neither difference changes this proof's
mathematical dependency closure.

## Dependency graph

1. Canonical raw symbol and raw modular \(T_N,M_N\) definitions
   → independently reconstructed Gaussian-integer coefficients of \(4000A_N\).
2. Direct raw-kernel trace completion and direct Weyl multiplication
   → exact all-odd-N Laurent identity for \(H_N\).
3. Integer polynomial assembly + elementary cyclotomic irreducibility and
   totient bound + complete finite remainder certificate
   → the only odd root orders are 1 and 7
   → \(H_N\ne0\) for odd \(N\ge3\), \(N\ne7\).
4. Hermitian algebraic \(A_N\) + algebraic spectral projectors + this
   nonzero \(H_N\)
   → at least two active spectral-trace coefficients
   → unique nonzero extreme difference coefficient in the squared trace.
5. This coefficient survives subtraction of any algebraic constant +
   EXT-POPESCU-2023, Theorem 3.2
   → squared-trace transcendence at nonzero real algebraic time.
6. Exact raw coefficient aggregation modulo seven + the Gaussian trace norm
   → the exact exceptional answer 1 at \(N=7\).

Neither the common-commutant theorem nor spectral simplicity nor the
p-adic/minor proof of FM-008 is a mathematical dependency of this new proof.
FM-008 and FM-010 are used to identify prior ownership and scope only.

## Obligation matrix

| Obligation | Status | Decisive evidence |
|---|---|---|
| Match the actual raw symbol, centering, mode ordering and coupling | Passed | Rational trigonometric expansion from canonical Section 1; all 32 coefficients agree |
| Weyl cocycle sign and midpoint arithmetic | Passed | Direct algebra below; every raw ordered pair and every row checked in 15 characteristic-zero controls |
| Gaussian trace character for all odd N, including aliases | Passed | Direct square completion and invertible translations; no support-distinctness assumption |
| Nonzero normalizing trace | Passed | \(|\sum e_N(-x^2/2)|^2=N\), using the bijection \((x,y)\mapsto(x-y,x+y)\) |
| Exact integer Laurent polynomial and normalization | Passed | Independent 1,024-pair assembly; every coefficient agrees |
| Universal-to-finite root-order reduction | Passed | Elementary bound \(n\le1894\) derived below |
| Complete necessary mod-2 exclusion | Passed | Different integer-divisor cyclotomic recursion; all 446 eligible orders and all remainders agree |
| Exact root orders and multiplicities | Passed | Independent integer divisions and reconstructed quotient products; orders 1,7, multiplicity 2 each |
| Exact seven-dimensional scalar exception | Passed | Gaussian-integer raw aggregation plus direct characteristic-zero matrix equality |
| Repeated eigenvalues and spectral projector algebraicity | Passed | Projectors indexed by distinct eigenvalues; no simple-spectrum assumption |
| Nonconstant squared trace despite possible frequency collisions | Passed | Unique largest difference among active real frequencies |
| Subtraction of an arbitrary algebraic constant | Passed | Extreme coefficient unaffected; zero-frequency exponent included as needed |
| Registered external theorem and exact application | Passed | Fresh pinned-primary theorem-statement check and explicit mapping; external theorem retained as an input |
| Author execution and fail-closed optimization guard | Passed | Byte-identical author replay; -O and -OO exit before creating outputs |
| Higher powers, simplicity, quantitative estimates, BGS | Out of scope | None follows from the audited argument |

## Independent derivation of the load-bearing identities

Put \(h=2^{-1}\pmod N\). Applying \(T(a,b)T(c,d)\) to a vector at
\(x\) gives phase
\(b(x+ha)+d(x+a+hc)\). Subtracting the phase of
\(T(a+c,b+d)\) leaves \(h(ad-bc)\) modulo \(N\). This gives the
candidate's positive cocycle sign. Every identity is over \(\mathbb Z/N\),
so raw integer labels can be reduced only at the end and aliases cause no
exception.

For the trace, the matrix entry selected by \(T(a,b)\) is \(M_{x+a,x}\).
The actual exponent expands as

\[
b(x+a/2)-(3(x+a)^2-2(x+a)x+3x^2)/8
=-x^2/2+(b-a/2)x+ab/2-3a^2/8.
\]

Completing its square gives
\(-(x-b+a/2)^2/2+(2b^2-a^2)/4\). The translation is a permutation at
every odd modulus. Thus, with \(Q(a,b)=2b^2-a^2\),
\(\operatorname{Tr}(T(v)M)=\operatorname{Tr}(M)e_N(Q(v)/4)\).
The double Gaussian sum becomes an additive-character sum after the
invertible change \((x,y)\mapsto(x-y,x+y)\), giving \(|\operatorname{Tr}M|^2=1\).

Using \(d_v=4000c_v\) now gives, exactly,

\[
4000^2H_N=\operatorname{Tr}(M_N)^2P(e_N(4^{-1})),\quad
P(z)=\sum_{v,w}d_vd_w
 [z^{Q(v+w)+2\omega(v,w)}-z^{Q(v)+Q(w)}].
\]

The normalization is the **complex square** of \(\operatorname{Tr}M\), not
its norm square. Both are nonzero, but replacing one by the other in this
identity would be unjustified. Pairing opposite raw modes makes all
coefficients real integers.

The independent polynomial has 143 terms on exponents -36 through 648,
endpoint coefficients -14 and -50, content 2 and coefficient absolute sum
40,256,624. Thus \(R=z^{36}P/2\) has degree 684 and leading/constant
coefficients -25/-7. Every Laurent coefficient and every coefficient of R
matches the frozen arrays.

If \(P\) vanishes at a primitive odd-order root of order \(n\), its
cyclotomic minimal polynomial divides \(R\) over \(\mathbb Z\). Hence
\(\varphi(n)\le684\). For every odd prime power \(p^a\),
\(\varphi(p^a)^2/p^a=p^{a-2}(p-1)^2\ge1\), so \(n\le684^2\).
Seven distinct odd primes would give
\(n\ge3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19=4,849,845>684^2\).
With at most six distinct odd primes,
\(n/\varphi(n)\le17017/6144\), hence \(n\le1894\).
This reasoning covers all odd n; there is no empirical extrapolation from
the matrix-control dimensions.

The independently implemented recursion divides \(X^n-1\) by
\(\Phi_d\) for **all proper divisors** \(d\mid n\), in integer
coefficient arrays. This differs from the author's prime-step/bit-polynomial
recursion. Degree is compared with a separate gcd-enumerated totient for
every odd \(n\le1894\). Exactly 446 orders satisfy the degree condition;
373 are prime to seven and 73 are divisible by seven. Direct array division
over \(\mathbb F_2\) leaves zero remainder only at 1 and 7. Since
\(R\bmod2\) retains degree 684, monic divisibility over the integers implies
this necessary mod-2 divisibility without any loss of degree or denominator.

Exact integer divisions establish multiplicity two for each survivor, with
nonzero third-division remainders exactly as printed in the candidate.
The independently reconstructed quotient in
\(R=(z^7-1)^2V\) has degree 670 and \(V(1)=2,067,702,784\).
The value \(e_N(4^{-1})\) has exact order N; thus the full H assertion
follows, including every five-adically ramified case.

Finally, let a index the distinct eigenvalues of Hermitian algebraic A, and
write \(c_a=\operatorname{Tr}(P_aM)\). The polynomial projector expression
in the candidate is valid for repeated eigenvalues because products range
over **distinct** values. Thus the eigenvalues and c's are algebraic, and
\(H=(\sum c_a)(\sum a^2c_a)-(\sum ac_a)^2\). At most one nonzero c
would force H=0. When H is nonzero, the extreme active values
\(a_+>a_-\) give a unique contribution to frequency \(a_+-a_-\) in
\(J(t)=\sum c_a\overline{c_b}e^{it(a-b)}\). Its coefficient is nonzero.
Equal intermediate differences may cancel; the extreme one cannot.
Subtracting any algebraic L changes only the zero-frequency coefficient.
After collecting frequencies, Lindemann–Weierstrass applies to the distinct
algebraic exponents \(it\delta\), including zero if its coefficient survives.
This proves \(J(t)\ne L\) at every nonzero real algebraic t.

At seven the exact raw coefficients aggregate to the single residue class
(0,0) with coefficient 3600. The scalar conclusion is therefore an identity
over characteristic zero, not a reduction modulo a prime or a numerical
approximation.

## Computation and independence record

The reviewer saw the frozen claim and proof, then wrote a new implementation
from the canonical raw definitions. The author verifier was read only after
the first independent run completed. No author function or coefficient/screen
module is imported by `reconstruct.py`. Frozen arrays are used only for
comparison with independently constructed objects. Independent reviewer
agreement alone is not the proof; the derivations and coverage reduction above
are essential.

An orthogonal check evaluates the actual tridiagonal/Jacobi entries directly
from the trigonometric symbol in \(\mathbb Q(\zeta_{4N})\). With
\(R_4(x)=(2-\zeta^{7x}-\zeta^{-7x})(2+\zeta^x+\zeta^{-x})=4r(x/N)\),
the scaled diagonal is
\(2000(\zeta^{7x}+\zeta^{-7x})+100R_4(x)-5iR_4(x)(\zeta^x-\zeta^{-x})-400\),
and the two entries are \((-3\mp4i)R_4(x\pm h)\).
This creates B independently of the 32-mode array. Exact quotient-ring
reductions compare B with the raw Weyl matrix row by row and contract
\(\operatorname{Tr}K\), \(\operatorname{Tr}(BK)\), and
\(\operatorname{Tr}(B^2K)\), where \(K=\sqrt N M\).

The 15 checked dimensions are
3, 5, 7, 9, 21, 25, 27, 35, 45, 49, 63, 77, 105, 121, 125.
Every raw character and all 1,024 cocycles at every row are checked.
Direct H is zero only at seven in this bounded list. A corrupted constant
polynomial coefficient is rejected in every dimension. These controls use
characteristic-zero cyclotomic fields, unlike the author's finite-field
specializations; they still remain bounded controls.

`executed/manifest.json` is a validated schema-version-2 computation manifest.
It records input hashes before/after, command arrays, declared result files,
all result/log hashes, Python 3.12.14, runtime, exit statuses and enforced
per-child limits (1 GiB address space, 60 CPU seconds, one CPU affinity,
90-second wall timeout). The standard independent run, optimized independent
run, and author replay passed. Independent non-timing outputs agree under
optimization. All nine regenerated author artifact files are byte-identical
to the frozen evidence. Both author optimization modes fail closed before
writing output.

Reproduction from this directory, preserving the delivered evidence:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -S reconstruct.py reproduced
python3 -S validate_manifest.py executed/manifest.json --root /workspace/shared
sha256sum -c SHA256SUMS
```

The wrapper `run_review.py` was executed once and deliberately refuses to
overwrite `executed/`. Its complete command history is in
`executed/replay_comparison.json`. The manifest hash is
`f96875d5006a1b06627190611d646b094922555845958ad62295a65247cdbf13`.

## External source and precise boundary

The exact primary [Popescu v2 PDF](https://arxiv.org/pdf/2306.14352v2)
was freshly opened on 6 October 2026. Its version header is 17 September
2023; Theorem 3.2 is on printed page 14, with its proof on pages 15–16.
The theorem states independence over the field of all algebraic numbers for
exponentials of distinct algebraic exponents. That is exactly the needed
statement. The translation is \(\alpha_j=it\delta_j\), where the collected
frequencies \(\delta_j\) are distinct real algebraic numbers and \(t\)
is nonzero algebraic. The coefficients after subtracting L are algebraic
and not all zero. No rational independence of frequencies, simple spectrum,
nonzero condition on every exponent, or quantitative version is required.

This is a fresh theorem-statement and application check in addition to the
registered source audit. It is not a new proof or a line-by-line audit of
the external number-theory theorem. That source remains an explicitly
external input. The polynomial and H result do not depend on it.

**Remaining mathematical gap in the stated theorem: none found.** The
strongest accepted statement is exactly the normalized theorem above.
There is no inference to higher powers at seven-divisible dimensions,
generator or propagator spectral simplicity, quantitative trace/gap bounds,
Heisenberg-scale estimates, CUE, or BGS. No additional larger finite-N sweep
is needed for this theorem. Any integration should retain this scope and
these source-bound artifacts; publication and repository promotion are
separate tasks.

## Publication scope

Original bytes and exact source hashes remain bound by
record/spectral_extension_promotion_mapping.json. Execution-machine paths
in this curated copy are source roles, not installed dependencies. Portable
replay packaging does not strengthen the independent mathematical verdict.
