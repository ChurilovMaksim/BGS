> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round9_2026_10_21/r9_sector_deleted_clock_independent_audit.md`. Embedded SHA256: `26d8fb35fcb86d0a6fe3cc2c0e3be7a7b5a518e22bb669994954ef26779c6cfe`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Independent audit of the deleted-clock determinant obstruction

21 October 2026. Auditor: `/root/r9_sector_coherence`.

## Audited artifact and outcome

The complete raw proof in
`research_round9_2026_10_21/r9_determinant_exact_cue_detdet_counterexample.md`
was read. Its actual SHA-256 at review was
`22da436148c61eea76077aa0546a709ac30c64a16bfb5550db0ae2755a23419c`.

**Accepted in its stated scope.** The construction gives an auxiliary
unitary family with exactly the full CUE determinant autocorrelation,
but with lattice local statistics and a nonvanishing fixed pair defect.
It does not concern the spectrum of the prescribed kicked cat matrices.
No conclusion about their unresolved full weighted pair sum follows.

## Load-bearing checks

1. For the $(N+1)$-st roots of unity with the root $1$ removed,
   
   $$
   D_N(z)=\prod_{j=1}^N(1-ze^{2\pi ij/(N+1)})
         =\sum_{r=0}^Nz^r.
   $$

   Thus angular averaging gives exactly
   $\sum_{r=0}^N(z\overline w)^r$, with no asymptotic error.

2. The alternant identity for $e_k\Delta$ uses the exponent set
   $\{0,\dots,N\}\setminus\{N-k\}$. Character orthogonality
   makes distinct such exponent sets orthogonal and gives norm one
   after division by the CUE normalization $N!$. This proves the
   claimed CUE comparison, including the cases $k=0,N$.

3. The complete-symmetric-function alternant uses
   $\{0,\dots,N-2,N-1+m\}$. These sets are distinct for different
   $m\ge0$, and the claimed inverse-determinant second moment
   $1/(1-r^2)$ follows. Absolute convergence for $r<1$ permits
   termwise integration.

4. For $0<m<N+1$, the deleted-clock trace is $-1$. The prescribed
   auxiliary test has Fourier support in $[-1/2,1/2]$, so every
   nonzero pair-sum frequency is in this range. Consequently
   
   $$
   \Delta_{2,N}(b)
   =N^{-2}\sum_{1\le m<N/2}|\widehat b(m/N)|^2(1-m)
   \longrightarrow-\int_0^{1/2}u|\widehat b(u)|^2\,du<0.
   $$

   The bump construction does satisfy every requested admissibility
   condition. This is a fixed test and all sufficiently large odd
   dimensions, for the auxiliary family.

5. Restoring the missing point gives a randomly shifted lattice of
   spacing $N/(N+1)$. Removing the missing root changes any fixed
   bounded observation window with probability at most its length
   divided by $N$. The local weak limit is therefore the randomly
   shifted unit lattice.

6. The asserted strict Laplace separation does not hide a moment
   convergence assumption. For finitely many $h_j\in[0,1]$, set
   $E=\prod_j(1-h_j)-1+\sum_jh_j$. Adding a new factor of size
   $h$ increases $E$ by $h(1-\prod_j(1-h_j))\ge0$.
   If two factors are at least $h_0>0$, then $E\ge h_0^2$.
   The Sine-kernel factorial second moment on a nonempty interval is
   strictly positive, hence the event of two such points has positive
   probability. This establishes strict separation by a bounded
   Laplace observable.

7. The inverse deleted-clock determinant has coefficients $+1$ at
   exponents $q(N+1)$ and $-1$ at $q(N+1)+1$, with disjoint
   supports. Parseval gives
   
   $$
   \int|D_N(re^{i\alpha})|^{-2}\frac{d\alpha}{2\pi}
   =\frac{1+r^2}{1-r^{2(N+1)}}.
   $$

   Its bounded microscopic-radius limit and the linearly diverging
   CUE comparison are both correct.

## Consequence and limitation

The argument decisively rejects the implication from full direct
determinant autocorrelation to mixed inverse-determinant statistics.
Differentiating direct determinant products cannot insert the missing
denominators. Every use of the example must retain the word
**auxiliary**: it is not the prescribed $U_N$, and it proves neither
failure nor validity of that family's $H_{\rm diag}$.

No change to the audited file or the master document was made.
