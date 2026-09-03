# Current results and research boundary

This is the concise active mathematical summary. `record/claim_ledger.md`
contains the broader disposition of older results.

## 1. Finite-field pair geometry

Let `N` be an odd prime, `H <= F_N^*` a subgroup of order `K`,
`m=(N-1)/K`, and `S=H^perp`. For admissible ordered pairs
`x,y notin {0,1}` put

`u=x/y`, `v=(x-1)/(y-1)`, `d=x-y`.

Off the diagonal this is a bijection onto
`u,v in F_N^*\{1}`, `u!=v`, with inverse

`y=(1-v)/(u-v)`, `x=u(1-v)/(u-v)`

and

`d(u,v)=(u-1)(v-1)/(v-u)`.

The diagonal collapses to `(u,v,d)=(1,1,0)` with multiplicity `N-2`.

## 2. Exact second and fourth moment reductions

The constrained `k=2` off-diagonal count is `(K-1)(K-2)`.

For a collapsed key record `r=(u_r,v_r,d_r,n_r)`, define

`B(t)=sum_{r,s} n_r n_s 1_H(u_r u_s)1_H(v_r v_s)1_{d_r+d_s=t}`.

Then exactly

`sum_t B(t)=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K`.

For `chi,psi in S` define

`A_{chi,psi}(d)=sum_{r:d_r=d} n_r chi(u_r)psi(v_r)`.

Character orthogonality gives

`sum_{chi,psi}(A_{chi,psi}*A_{chi,psi})(t)=m^2 B(t)`,

and for the twisted Jacobi sums used in the matrix-element model,

`sum_{chi,psi in S}|J(chi,psi;q)|^4=m^2 Sigma4(q)`,

`Sigma4(q)=sum_t B(t)e_N(qt)`.

Writing `V=sum_t B(t)` and `Z=B(0)`,

`E_{q!=0} Sigma4(q)=(NZ-V)/(N-1)`,

`Var_{q!=0} Sigma4(q)=N Var_{t!=0}B(t)`.

These are exact finite identities.

## 3. Mixed Cayley layer

Exactly,

`B(t)=O(t)+2(N-2)C_H(t)+(N-2)^2 1_{t=0}`.

For `c(h)=(h+1)/(h-1)`,

`d(u,v)=2/(c(u)-c(v))`.

Thus `C_H` is a relabelled nonzero difference-representation function of
`A=c(H\{1})`. Since `c(h^-1)=-c(h)`, the forced energy for odd `K` is
`(K-1)(2K-5)`.

For odd prime `K`, a computer-assisted exact classification of all `6!`
matching systems leaves only identity and inversion-swap collisions in
characteristic zero. Reduction modulo `N` can create extra collisions. For
fixed `K` they are detected by explicit cyclotomic resultants.

Audited exact sets:

`E_11={23,67,89}`,

`E_13={53,79,131,157,313}`.

For `N notin E_K`,

`sum_t C_H(t)^2=(K-1)(2K-5)`.

The fresh negative control

`N=461, K=23: sum_t C_H(t)^2=1190`

shows why the fixed-`K` exceptional qualification is load-bearing: the forced
baseline there is only `902`.

## 4. Off/off elliptic family

In Cayley coordinates the pure off/off term is organized by a bounded-degree
family of plane cubics. Current algebra identifies a nonconstant generic
`j`-map, special parameter strata, an exact same-`j` involution and reducible
fibers at the Cayley-difference parameters already seen by `C_H`.

The earlier broad reconstruction also contains a degree-12 `j`-map/cusp-width
no-isogeny route and affine-boundary bookkeeping. These are retained in the
research notes and record, but they are **not promoted here beyond theorem
draft** until the projective model, exceptional parameters, twists,
inseparable cases and the exact trace-sheaf theorem hypotheses have been
audited line by line.

Conditionally on those obligations the intended bound is

`Var O(t) << K^2 N + K^4 sqrt(N) + K^4`,

leading in the first regime `K=o(N^(1/4))` to

`Var_{t!=0}B(t)=O(K^2 N)` and `std Sigma4=O(NK)`.

## 5. Earlier foundations that remain scientifically relevant

The historical workspace contains a substantial rank-1 foundation preceding
the present M1 repair: symmetry-class arguments, quadratic trace identities,
shape/moment decompositions, torus level sets and twisted-Jacobi formulas.
They were incorrectly almost erased from the visible tree during the compact
rebuild.

The present repository preserves them but does not silently reuse every old
`PROVEN` label. The pieces currently re-certified most directly are:

- finite torus level-set/orbit statements at `N=199` (Lean);
- finite scale-law statement at `N=199` (Lean);
- finite `k=2` and `k=4` counting certificates (Lean);
- selected twisted-Jacobi scalar and moment regressions;
- the current pair-key/Cayley exact layer.

The remaining symmetry/Catalan/arcsine statements are retained as
historical-unreviewed until a dedicated fresh proof audit is completed.

## 6. Numerical spectral evidence

Parity-reduced spacing and number-variance data at the retained designs are
GOE-like. They are finite numerical evidence only. A historical `N=95419`
test using a mismatched statistic is quarantined.

## 7. Open endpoint

General microscopic BGS/local eigenphase statistics are unproved. A completed
restricted M1 theorem would still require a separate mechanism controlling the
structured arithmetic dependence at the local resolvent/eigenvalue scale.
