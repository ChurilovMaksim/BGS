# Independent audit: uniform one-step actual charge contraction

## Claim and primary verdict

**Proved as written**, relative to the explicitly inherited actual parametrix,
phase-certificate, and norm-limit/growing-charge inputs identified below.
For the prescribed unchanged odd-dimensional U_N at fixed tau=10^-80, there
exist rho<1 and N0 such that

    sup_(c!=0 mod N) ||B_(N,c)|| <= rho,  odd N>=N0,
    B_(N,c)(j,k)=U_N(j,k) conjugate(U_N(j+c,k+c)).

The charge-pinched adjoint D_N also has an eventual strict one-step norm
bound on the ordinary-HS traceless space, after incorporating the centered
zero-charge block. This is strictly stronger than the earlier finite-power
conclusion. It does not contract the unpinched adjoint, which is unitary.

Reviewed candidate: `onestep_charge_gap.md`, SHA256
`d51de5e8287495514fc431ed9b05e44f3407e46ed923a6e1664df2cca667e97a`.
This is independent internal review, not external referee acceptance or
analytic formalization. The separate global-switch companion is not covered
by this verdict; its review is reported separately.

## 1. Source authority and dependency graph

Canonical `/workspace/shared/BGS` was read only. Its observed HEAD was
`d37c92e563d10d25bb1d6ab85bedffc1f160f773`; other work had already modified
its worktree. Applicable AGENTS, source hierarchy, conventions, research
brief, claim ledger/registry, results and open-question surfaces were checked.
The frozen input copies and exact observed worktree status are recorded in
`source_manifest.json`. No `.mathbox` ledger was found. No canonical files,
claim status, manuscript, commit or publication were changed by this audit.

The load-bearing chain is:

1. Actual raw operator, odd-N modular convention and exact unitarity.
2. Exact four-branch initial identity, HJ evolution and transport gluing.
3. Fixed-time parametrix error, bounded derivatives and alias-safe TT*.
4. Actual two-mode Fourier certificate with a quantitative remainder at
   tau=10^-80, including exact translation of the nonlinear remainder.
5. A2--A5 of the accepted all-translation proof: fixed-c norm convergence and
   uniform small norm for growing c, with simultaneous two cutoffs.
6. Leading transport amplitude positivity and the zero-charge norm limit.
7. Bistochastic normalization from exact quantum unitarity, compact norm
   attainment, and the equality case of the positive-envelope bound.
8. Nonconstant actual branch phase; finite small-c maximum; negative-charge
   conjugacy; direct-sum centered zero-charge bound.

Pins are explicit in the source manifest. In particular the all-translation
source is `c0059f000b4642de174097b3e971d22ba0eac09cdff684289f72ae11db00a7c7`,
its prior review is `7b046dd79bdb000a0d84c150a1949d517fdb2043c3a3c81d6929e8c5e2ae17b4`,
the parametrix is `c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7`,
and FM-021 is `3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09`.
The prior review is provenance, not a replacement for inspecting the raw
proof. The analytic norm-limit and growing-charge arguments were reread,
including alias control, the scaled near-diagonal cutoff and chart gluing.

No step invokes A6--A7, the Koopman identification, FM-018 Egorov, mixing,
Parry--Pollicott, or any conclusion depending on them. The new proof removes
those inputs rather than silently strengthening their conclusion. FM-021 is
used only for its directly proved amplitude estimate and zero-charge gap.
No new specialized external theorem requires an unverified literature leaf.

## 2. Amplitudes, c=0 limit and exact normalization

The leading amplitude solves a real scalar transport equation with initial
value one. Along real characteristics it is the exponential of the integral
of a real coefficient, hence positive. The independent quantitative bound
|a_(r,0)-1|<2*10^-66 also proves nonvanishing without any sign assertion about
the subleading amplitude. Therefore all four b_r=|a_(r,0)|^2/4 are strictly
positive, uniformly on the fixed compact square.

At c=0, the twelve unequal-branch terms have a nonzero actual mixed-phase
Fourier coefficient and the alias-safe upper bound. They vanish in operator
norm by precisely the same TT*/analytic-zero-set argument as in A5. The
four equal-branch terms are N^-1 d(j/N,k/N)+O(N^-2), where d=sum b_r.
The entry error has operator norm O(N^-1). The extended sampled kernel
converges uniformly, hence in Hilbert--Schmidt and operator norm, to K0.
This c=0 extension does not use any statement uniform in c.

With the N^-1 counting measure on the vector space, the step embedding J_N
is an isometry and J_N*1 is exactly the all-one vector. J_N J_N* is only the
step-function projection, but it fixes 1. Consequently both extended P_N
and its adjoint fix 1 exactly. Norm convergence and adjoint norm convergence
give K0 1=K0*1=1. Thus d has both row and column integral one. Continuity
upgrades the almost-everywhere normalization to every point. No invariant
classical measure or unproved density identity is needed.

## 3. The decisive equality case

For fixed nonzero c, the square kernel K_c is Hilbert--Schmidt and compact.
If its norm were one, compact norm attainment gives a unit f with norm-one
image. Pointwise triangle domination by K0|f| and the bistochastic Jensen
bound give a chain with equal endpoint norms. In particular

    integral d(x,y)(|f(y)|-K0|f|(x))^2 dx dy = 0.

Every integrand is nonnegative and d>0 almost everywhere. Fubini therefore
forces |f| to be a single constant almost everywhere. Unit normalization
makes it one; K0|f| is also one almost everywhere. Equality in the first
norm comparison then forces |K_cf(x)|=1 for almost every x.

For those x, K_cf(x) is a probability average over (r,y), with positive
weights b_r(x,y)dy, of the unit complex numbers e(-c L S_r(x,y))f(y).
Equality in the complex average implies agreement almost everywhere.
There are only four branches, so their exceptional sets can be combined.
Canceling the common nonzero f(y) between branches 0 and 1 gives

    e(-c L(S0-S1)(x,y))=1

for almost every (x,y). Continuity extends it to the whole square. The real
continuous function c L(S0-S1) then takes values in the discrete set Z on a
connected square and must be constant. No regularity of f beyond L2 was
silently introduced. Compactness is essential for starting with a maximizer;
a general noncompact contraction can have norm one without attaining it.

## 4. Actual Fourier contradiction

The raw symbol independently reconstructs

    ghat(0,1)=(-3-4i)/1000,  ghat(1,1)=(3+4i)/2000.

Under p=(y-3x)/4 these yield the two frequencies
nu0=(-3/4,1/4), nu1=(1/4,1/4). Multiplication by the mixed derivative and the
HJ factor 1/(2pi) gives first-time coefficient moduli 3pi/1600 and pi/3200.
The inherited C2 remainder is bounded by (10^50/2)tau^2; at literal tau it
is smaller than half the smaller signal. The exact coefficients A_i of
R_(0,xy), not merely their first-time approximations, are therefore nonzero.

The full exact correction satisfies R1(x,y)=R0(x,y+1). Differentiating its
Fourier series gives the coefficient of partial_xy L(S0-S1) at nu_i as

    2pi i (nu_i,x+nu_i,y) A_i (1-i).

The two frequency sums are -1/2 and 1/2. The multiplier divided by pi is
respectively -1-i and 1+i, so neither can vanish. Only analyticity and the
already certified A_i are needed; no numerical C3 remainder estimate is
being inferred from a C2 bound. The initial cat L-difference is the constant
1/2 and contributes zero to this derivative.

Thus L(S0-S1) is not globally constant. The phases are real analytic on the
connected global real chart, so constancy on an open unit square would
force global constancy. This contradicts the equality consequence. The
argument works for every fixed integer c!=0: multiplying by a nonzero c
cannot make a nonconstant continuous function integer-valued. It is not
limited to odd, even, primitive or bounded-order charges.

## 5. Uniformity and centered zero charge

A11 gives C0 and N1 such that all positive c>=C0 with c<N/2 have norm at
most 1/2 once N>=N1. This is a simultaneous two-cutoff statement; pointwise
convergence in c would not suffice. Only finitely many c<C0 remain.
Their compact limiting norms are each strictly below one, so their maximum
rho0 is below one, and norm convergence gives the common eventual bound
(1+rho0)/2. Taking a maximum of finitely many startup thresholds is valid.

The exact identity B_(-c)=T_(-c) conjugate(B_c) T_c preserves the induced
norm. Every nonzero residue at odd N has a positive or negative representative
with 1<=c<N/2. The zero-charge block is the doubly stochastic P_N; its
constant vector is precisely the identity direction. On the remaining
traceless diagonal space, the operator norm is ||P_N-J||<=1/2 eventually
by FM-021. Orthogonality of charge sectors gives the final direct-sum gap.
Here J is the finite constant projection, distinct from the step embedding.

## 6. Obligation matrix

- Actual object and ordinary-HS compression: passed.
- Literal fixed tau, all odd dimensions eventually: passed.
- Leading-amplitude nonvanishing, all four branches: passed.
- Zero-charge norm limit and adjoint normalization: passed.
- Compact norm attainment: passed.
- Jensen equality, Fubini, branch alignment and continuity: passed.
- Exact nonlinear Fourier witness and analytic continuation: passed.
- Every positive/negative nonzero charge: passed.
- Simultaneous growing-charge cutoffs and finite small-charge maximum: passed.
- Centered zero-charge block and traceless direct sum: passed.
- Absence of hidden Egorov/mixing dependence: passed.
- Effective startup or explicit uniform gap value: not claimed.
- Tau-uniformity, tau=0 extension, full undamped offcharge or BGS: out of scope.

## 7. Independent bounded controls and counterexamples

`independent_checks.py` imports no author or repository verifier. Its integer
and rational controls include:

- Every one of 65,536 two-point/two-branch fourth-root phase arrays with
  everywhere-positive bistochastic envelope. Exact 2x2 Gram determinants
  classify 64 norm-one cases. None of 65,280 branch-conflicting arrays has
  norm one; 192 branch-aligned but row-inconsistent cases remain strict.
- Twenty exact weighted variance identities with a positive nonconstant
  bistochastic envelope and four unequal branch weights.
- Explicit failure controls: a zero-weight branch can hide arbitrary phase
  conflict; a positive row-stochastic kernel without column normalization
  has squared norm 5/4; a non-strict envelope permits equality with
  nonconstant modulus.
- 130,815 raw cat phase entries and 125,360 negative-charge identities,
  odd N=3,...,31; 240 exact cyclotomic zero sums proving the square-zero
  control; 120 odd-charge escaping aliases; continuum parity through
  -99<=c<=99.
- Independent reconstruction of the actual symbol modes, G7 multipliers,
  exact rational specified-time remainder comparison, and amplitude lower
  bound.

At tau=0 every finite raw charge block has norm exactly one, although its
square vanishes for nonzero c. The continuum equal-branch kernel is zero
for odd c and rank-one norm-one for nonzero even c. Thus the actual
unequal-branch cancellation, literal-time phase witness and positivity
cannot be replaced by flatness, weak limits or unitarity alone.

Normal and optimized executions passed with identical output. The optimized
injected-failure run exits nonzero, so assertions cannot silently disappear.
The version-2 execution manifests record actual argv, input hashes, scientific
outputs, resource caps, environment and runtime; their skill validator passes.
Finite agreement supports only these bounded algebraic assertions. It does
not prove the analytic limit or resolve an immeasurably small fixed-time gap.

## 8. Exact remaining boundary

No gap remains in the new one-step implication relative to its pinned
analytic inputs. Constants and startup are existential and may deteriorate
without bound as tau tends to zero. The strongest safe conclusion is the
stated uniform strict norm gap for charge compression on traceless operators.
Any occupation mask, varying-charge product or switch-weighted aggregate
requires its own exact bookkeeping. The companion is reviewed separately;
this core result alone does not estimate the full undamped deterministic
signed pair defect, plateau correction, higher factorial hierarchy or BGS.
