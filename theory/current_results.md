# Current mathematical state

This file is authoritative for theorem status.

## Exact finite-field layer

Let `N` be an odd prime, `H <= F_N^*` have order `K`, `m=(N-1)/K`, and `S=H^perp`.
For admissible ordered pairs `x,y notin {0,1}` put

`u=x/y`, `v=(x-1)/(y-1)`, `d=x-y`.

Off the diagonal this is a bijection onto
`u,v in F_N^*\{1}`, `u!=v`, with

`y=(1-v)/(u-v)`, `x=u(1-v)/(u-v)`,
`d(u,v)=(u-1)(v-1)/(v-u)`.

The diagonal collapses to the single key `(1,1)` with multiplicity `N-2` and difference zero.

The exact constrained `k=2` off-diagonal count is

`(K-1)(K-2)`.

For a collapsed key record `r=(u_r,v_r,d_r,n_r)`, define

`B(t)=sum_{r,s} n_r n_s 1_H(u_r u_s) 1_H(v_r v_s) 1_{d_r+d_s=t}`.

Then

`sum_t B(t)=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K`.

If

`A_{chi,psi}(d)=sum_{r:d_r=d} n_r chi(u_r) psi(v_r)`, `chi,psi in S`,

character orthogonality gives exactly

`sum_{chi,psi}(A_{chi,psi}*A_{chi,psi})(t)=m^2 B(t)`.

For the twisted Jacobi sums used in the matrix-element model this is

`sum_{chi,psi in S}|J(chi,psi;q)|^4=m^2 Sigma4(q)`,
`Sigma4(q)=sum_t B(t)e_N(qt)`.

Writing `V=sum_t B(t)` and `Z=B(0)`, finite Fourier orthogonality gives

`E_{q!=0} Sigma4(q)=(N Z-V)/(N-1)`,
`Var_{q!=0} Sigma4(q)=N Var_{t!=0} B(t)`.

These are exact finite identities; no random-matrix or asymptotic assumption enters them.

## Mixed layer

There is an exact decomposition

`B(t)=O(t)+2(N-2)C_H(t)+(N-2)^2 1_{t=0}`.

With the Cayley map

`c(h)=(h+1)/(h-1)`

one has

`d(u,v)=2/(c(u)-c(v))`.

Thus `C_H` is a relabelled nonzero difference-representation function of
`A=c(H\{1})`. Since `c(h^-1)=-c(h)`, for odd `K` the set is centrally symmetric and `0 notin A`.

For odd prime `K`, an exact characteristic-zero classification of the sparse cyclotomic collision equation leaves only the identity and inversion-swap families. Reduction modulo `N` can create additional collisions. For fixed `K` these are controlled by a finite set `E_K` obtained from the relevant cyclotomic resultants.

The active exact gate fully enumerates only

`E_11={23,67,89}`,
`E_13={53,79,131,157,313}`.

If `N notin E_K`, then

`sum_t C_H(t)^2=(K-1)(2K-5)`

and the mixed M1 layer has standard deviation `O(K sqrt(N))`.

This is a fixed-`K` theorem, not a useful uniform exclusion when `K` grows. A fresh independent exact reconstruction gives the negative control

`N=461, K=23: sum_t C_H(t)^2=1190`,

where the forced baseline is `902`; hence this level is exceptional for `K=23`.

## Off/off elliptic family

The pure off/off term `O(t)` admits a plane-cubic/elliptic-family organization in Cayley coordinates. Current symbolic work supports a nonconstant generic `j`-invariant, bounded bad-fiber complexity, an involutive same-`j` symmetry, and reducible fibers at Cayley-difference parameters already visible in the mixed layer.

This structure is useful, but the repository does **not** currently promote the resulting M1 variance estimate to an unconditional theorem. Two load-bearing obligations remain:

1. a publication-grade algebraic certificate for the projective family, discriminant/`j` map, exceptional parameters, twists and the required no-isogeny/non-isomorphism statement after reduction;
2. a source-exact uniform trace-sheaf correlation lemma with purity, irreducibility/monodromy, conductor, ramification, dual/twist and deleted-point hypotheses checked for the actual family.

Conditionally on these obligations, the expected estimate is

`Var_{t!=0} O(t) << K^2 N + K^4 sqrt(N) + K^4`,

which gives the target M1 scale in the preliminary regime `K=o(N^(1/4))` outside the relevant fixed-`K` exceptional reductions.

## Spectral status

Finite parity-reduced spacing and number-variance experiments are GOE-like at the tested designs. They are numerical evidence only.

Even an unconditional restricted M1 theorem would not prove a microscopic BGS law. A separate argument must control the structured arithmetic dependencies strongly enough to reach a resolvent/local-statistics theorem.

## Retracted from the active argument

The following historical claims are not current results:

- the old Mobius-fiber object proves M1;
- the old H-coupling chain proves a general rank-1 or rank-2 local law;
- moment/Catalan data plus an ESY citation automatically give BGS;
- the old Sp4 numerical flatness closes a theorem for `Sp(2g)`;
- finite GOE fits are proof of a limiting spacing distribution.

Git history preserves those routes as research archaeology. They are intentionally absent from the active tree.