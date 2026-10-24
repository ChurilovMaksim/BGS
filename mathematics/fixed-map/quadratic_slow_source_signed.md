# Signed cyclic coefficient of the first nonlinear slow mode

6 October 2026. Separate signed continuation. The parent report and the
nonlinear source/inverse-energy report are frozen and unchanged.

## Exact signed result

Retain the actual operator U_N(t)=exp(itNA_N)M_N, the two-block D, the
quadratic mode Y=X-P_0X and all conventions of `report.md`. For every odd
N>=3, m>=2 and real t, put

    a_N(t)=Tr[D U_N(t) D U_N(t)^*]/Tr(D^2).

Then a_N(t) is real and the actual cyclic vector coefficient is EXACTLY

    f_(N,m)(t)
       :=<Y,R_m K_m(t)Y>/||Y||^2
        =<Y,K_m(t)Y>/||Y||^2
        =[(N^2-1)a_N(t)^2-1]/(N^2-2).                       (S1)

There is no m-dependence. In particular, for the fixed tau=10^-80 and every
odd N>=19, every m>=2 (including m comparable to or larger than N),

    f_(N,m)(tau)=-1/(N^2-2)+delta_N,

    0<=delta_N<= [9pi^4/40000][(N^2-1)/(N^2-2)]
                                      tau^2 N^-3.           (S2)

Thus this coefficient is strictly NEGATIVE at the literal fixed coupling.
This is a signed actual-operator estimate, not an unsigned norm estimate
or the linear Duhamel error for Y. The square in (S1) is essential.

## Proof

For any single-copy unitary U, let C_U denote collective conjugation. Every
pair term D^(r)D^(s) has zero partial traces, as does its image under C_U.
If two pair embeddings differ, their HS inner product is zero even when
they share a slot. Therefore

    <X,C_U X>=binomial(m,2)N^(m-2)[Tr(D U D U^*)]^2.

The Haar-invariant part P_0X is fixed by C_U. Orthogonal projection then gives

    <Y,C_UY>=<X,C_UX>-||P_0X||^2.

Use the exact invariant norm and Y norm from (1)--(2) of `report.md` to
obtain (S1). The trace of the product of the two Hermitian matrices D and
UDU^* is real. Cyclic slot conjugation permutes the unordered slot pairs,
so R_mY=Y, proving the equality of cyclic and ordinary pairings.

To bound a_N at the actual t, put E=exp(itNA). Flatness of M gives
Tr(D M D M^*)=0. Hence

    a_N(t)=Tr[(E^* D E-D) M D M^*]/Tr(D^2).

Hilbert-Schmidt Cauchy-Schwarz and the exact Duhamel bound yield

    |a_N(t)|<=|t|N ||[A,D]||/||D||
       <=(3pi^2/200)|t|N^-3/2,                              (S3)

using the already proved actual middle-edge Rayleigh bound. This is valid
for every real t. Squaring (S3) in (S1) gives (S2). Strict negativity follows
because its nonnegative correction is smaller than 1/(N^2-2); at the literal
tau this holds uniformly for every odd N>=19, without an unspecified startup
constant or a shrinking-coupling substitution.

## What this does and does not settle

This is one normalized vector coefficient of R_mK_m(tau), with its exact
multiplicity normalization retained. It may be viewed as one diagonal
contribution when that vector is included in an orthonormal basis. It is
NOT the full cyclic trace, a uniform estimate for every slow mode, or the
negative plateau correction N-m. Its order is N^-2, whereas the remaining
trace aggregates contain many signed contributions.

The same Y has source norm of order N^-1/2 and an inverse-energy weighted
source norm at least order N^2, as the separately frozen report proves.
Equation (S2) demonstrates why neither unsigned norm determines its signed
cyclic coefficient. No positive-memory or Markov closure follows.

## Executed check

`check_signed.py` independently builds Y in the full tensor space and
compares direct ordinary and cyclic pairings against (S1) at
(N,m)=(3,2),(3,4),(5,3),(19,2), using t=0,.001,.137. All assertions pass
in complex128 arithmetic. The t=0 benchmark is exactly -1/(N^2-2).
The finite nonzero-time checks audit the identity; the literal-tau result
is the all-time proof (S3), not numerical resolution of 10^-80.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_signed.py > signed_checks.json

No canonical or previously frozen file was edited. The signed result is
self-reviewed and requires a fresh independent proof review before promotion.

## Supporting scope

This is a supporting result for TRACE-020, not an extra core theorem or
control of the full balanced/complement trace. Review and original-byte
mappings are in record/collective_promotion_mapping.json. Any full-kernel
identity used by an unregularized corollary retains its separate hypothesis;
the regularized slow-source obstruction does not require identifying Haar
invariants with the entire deterministic kernel.
