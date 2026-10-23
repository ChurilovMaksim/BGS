# Fixed-fraction balanced Hamming control by exact torus compression

Author candidate, 7 October 2026. No canonical edits. Independent review is pending. The accepted sparse-marker theorem is credited as the source of the centered-range and support-grading construction; the new step replaces its marker-color count by a positional binomial count without discarding charge balance.

## 1. Exact claim and improvement

Let N>=2, m>=1, W=(C^N)^tensor m, E=End(W), with ordinary unnormalized Hilbert–Schmidt inner product. Let R=Ad(C_m) for one full slot cycle, C_U=Ad(U^tensor m), P_H the full Haar-invariant projector, and Pi the coordinate-occupation balanced projector. Write F_r for the orthogonal projector onto all |x><y| with coordinate Hamming distance at most r, and B_r=ran(Pi F_r). Define

 P_r=Proj[(I-P_H)B_r],  Ptilde_r=Proj[(I-P_H)ran F_r],
 O_r=(I-Pi)F_r.

For 0<=r<=m put

 D=N^2-1, n=m-2r, M=sum_(s=0)^r binom(m,s),
 t=||P_U-J|| on traceless diagonals,
 a_n=E_(V Haar)||P_V-J||^n.

If n>=1 and M a_n<1, then

 |Tr_E(R P_r C_U)| <= D M (t^n+a_n)/(1-M a_n),               (1)
 |Tr_E(R Ptilde_r C_U)| <= D M (t^n+a_n)/(1-M a_n).          (2)

For every n=m-2r>=0, without any Haar smallness requirement,

 |Tr_E(R O_r C_U)| <= 2 D M t^n.                            (3)

At n=0 use t^0=1, including t=0. There is an exact orthogonal identity

 Ptilde_r=P_r+O_r.                                         (4)

The decisive replacement relative to the accepted sparse-marker theorem is

 sum_(s<=r) binom(m,s) b_N(s)  --->  sum_(s<=r) binom(m,s).

No frame sectors are summed after independent orthogonalization. Every projector in (1)–(4) is the true projector onto one specified range. No Weingarten inverse, stable-degree hypothesis, or claim about invariant independence is used.

## 2. Fixed-positive-fraction consequence for the unchanged actual map

Use only the inherited actual bound t_N<=1/2 eventually and, for N>=20,

 a_n<=rho^n+4N^2 exp(-N/160), rho=sqrt(159/160).              (5)

Set lambda=log(1/rho)>0 and h(d)=-d log d-(1-d)log(1-d). Fix 0<a<=b<infinity. Choose any fixed 0<d<1/2 with

 h(d)<(1-2d)lambda,        b h(d)<1/160.                    (6)

Such a positive d exists for every finite b. Put

 gamma_(a,b,d)=min{a[(1-2d)lambda-h(d)], 1/160-b h(d)}>0.    (7)

For every 0<c<gamma_(a,b,d), uniformly for integers aN<=m<=bN and 0<=r<=d m, at sufficiently large odd N,

 |Tr_E(R P_r C_(U_N))|<=exp(-cN),
 |Tr_E(R Ptilde_r C_(U_N))|<=exp(-cN).                      (8)

The genuine new balanced residual Q_r=P_r-P_0 is an orthogonal projector, lies in Pi-P_H-P_ord, and has the same exponential conclusion with any strict c as above. Here P_0=P_ord in the present radius notation, not the scalar projector.

Separately, (3) and t_N<=1/2 give, for every 0<d<1/2 with h(d)<(1-2d)log 2,

 |Tr_E(R O_r C_(U_N))|<=2(N^2-1)exp[-m eta_d],
 eta_d=(1-2d)log 2-h(d)>0,       0<=r<=d m.                (9)

In particular d=1/6 is admissible, since eta_(1/6)=log(5^5/2916)/6>0. Thus an explicit off-charge sector reaching a fixed one-sixth of all coordinates is exponentially negligible for m>=aN. This result does not use an upper Heisenberg band or the Haar tail.

The accepted stronger actual estimate limsup t_N<=10^-64 also permits eventual t_N<=10^-63. Replacing log 2 by 63 log 10 in (9) permits d=49/100: h(49/100)<log 2< (1/50)63 log 10. Thus (3) controls the literal off-charge Hamming ball of radius floor(0.49m), at a non-effective eventual N threshold inherited from FM-021. This stronger fraction does not apply to (8), whose Haar constraints remain (6).

Every compact-weight N^-2 sum over a positive Heisenberg band of a sector in (8) or (9) is exponentially small. The original fixed tau, raw symbol, coordinate basis, common-origin convention and odd-dimensional sequence are unchanged.

## 3. Exact support grading and position blocks

Locally End(C^N)=C e direct-sum V, where e=I/sqrt(N) and V consists of traceless operators. Inside V write V=D0 direct-sum O, where D0 is traceless diagonal and O spans all off-diagonal matrix units. Let p and q be their orthogonal projectors. The raw Hamming projector F_r expands by marking the at-most-r off-diagonal slots; all remaining factors are the full diagonal projector. It preserves every exact traceless-support summand E_S. Pi, C_U and P_H preserve the same summands. Consequently P_r, Ptilde_r and O_r preserve them too. R transports E_S to E_(C_m S). Every proper nonempty S has zero contribution to the cyclic trace, and the empty support is annihilated by Haar removal or by I-Pi. Therefore only V^tensor m contributes.

On that top support, set

 J_S=tensor_i p_(S,i),   p_(S,i)=q if i in S, and p otherwise,
 F=sum_(|S|<=r) J_S.

These J_S are mutually orthogonal tensor-product projections. Let Pi now denote its top-support restriction. Each J_S commutes with Pi, so

 K=Pi F=sum_(|S|<=r) K_S,       K_S=Pi J_S

is an orthogonal block decomposition of the exact balanced raw projector. Some K_S vanish (for example |S|=1), which only improves the count M.

For A_V=Ad(V)|_V, p A_V p restricted to D0 is exactly P_V-J, and every other compressed local transition has norm at most one. Thus, for any S,T of size at most r,

 ||J_S A_V^tensor m J_T||<=||P_V-J||^(m-|S union T|)
                         <=||P_V-J||^n.

Because K_S=Pi J_S and K_T=J_T Pi,

 ||K_S A_V^tensor m K_T||<=||J_S A_V^tensor m J_T||.

After Haar averaging, each block of H=K P_H K has norm at most a_n. The ordinary block Cauchy–Schwarz bound gives

 ||H||<=M a_n.                                             (10)

Exactly the same proof applies to Htilde=F P_H F. Positivity follows from orthogonal Haar compression. Under M a_n<1, both centered top-support inclusions are injective, with exact Gram I-H or I-Htilde. This is a dimension-free block count; the rank N(N-1) of q has not become a multiplicity factor.

## 4. Torus averaging retains the occupation constraint exactly

For z=(z_1,...,z_N) in T^N let Z=diag(z_1,...,z_N), D_z=Ad(Z)|_V, and dz normalized Haar measure. Since E_ab has character z_a conjugate(z_b), while D0 has trivial character,

 Pi=integral_(T^N) D_z^tensor m dz.                         (11)

Equation (11) is the exact projector onto total occupation balance, including every repeated label. It is not an added average of the actual quantizer. The same z is used at every slot in one copy of Pi; different occurrences of Pi in a product have independent integration variables. Every p_(S,i) commutes with D_z, and

 p D_z=p,       D_z p=p.                                   (12)

Equations (11)–(12) are the missing color-summation interface in the sparse-marker estimate.

For k>=1 and unitaries U_1,...,U_k, expand the k copies of K in

 Tr_(V^tensor m)[R K A_(U1)^tensor m ... K A_(Uk)^tensor m].

Choose position sets S_1,...,S_k with |S_l|<=r and torus variables z_1,...,z_k. The summand is

 Tr[R tensor_(i=1)^m (p_(S1,i) D_(z1) A_(U1) ...
                         p_(Sk,i) D_(zk) A_(Uk))].         (13)

The full-cycle tensor trace identity turns (13) into a single ordinary D-dimensional trace, with slot order determined by R. Insert each p_(Sl,i) twice using p^2=p. Each internal stage l<k has compressed transitions between p_(Sl,i) and p_(S(l+1),i). The final stage has transitions between p_(Sk,i) and p_(S1,next(i)); the first position set is shifted at this seam.

For every stage at most 2r of the m transitions have a q endpoint. Each of the at-least-n remaining transitions has p on both ends, so (12) makes its norm exactly bounded by ||P_(Ul)-J||. All other factors have norm at most one. Therefore every (13), uniformly in its torus variables, has absolute value at most

 D product_(l=1)^k ||P_(Ul)-J||^n.

Normalized torus integration adds no constant. Summing M^k choices gives

 |Tr[R K A_(U1)^tensor m ... K A_(Uk)^tensor m]|
 <=D M^k product_(l=1)^k ||P_(Ul)-J||^n.                   (14)

For F in place of K, omit the torus variables; the same bound follows. Crucially, charge balance remains inside (13) until its exact integral is evaluated; no independent per-color bounds are summed.

## 5. Genuine range projectors and the Gram series

On top support, let B=K A_U^tensor m K restricted to ran K. Because R commutes with K and P_H, the exact centered-range formula is

 s_r=Tr_(ran K)[R(I-H)^(-1)(B-H)].                         (15)

This uses A_U^tensor m P_H=P_H=P_H A_U^tensor m. Expand only the convergent inverse in (15). Cyclicity and K^2=K reduce the j-th terms to j+1 copies of K, separated by j independent Haar stages and one actual U stage, or by j+1 independent Haar stages. Applying (14) and integrating Haar factors independently gives

 |Tr(R H^j B)|<=D M^(j+1) a_n^j t^n,
 |Tr(R H^(j+1))|<=D M^(j+1) a_n^(j+1).

The scalar series is absolutely summable under M a_n<1; summing proves (1). The identical argument with F proves (2). No assumption that P_r commutes with C_U is needed.

For (3), the top raw off-charge projector is F-K. Apply (14) with k=1 to each of the two raw traces and subtract. This is a bound on the exact signed trace, not an inference from projector inclusion.

To prove (4), F commutes with Pi and ran P_H is contained in ran Pi. Hence ran F is the orthogonal sum ran K direct-sum ran O_r, and I-P_H maps these pieces into the orthogonal balanced and off-charge spaces, acting identically on the latter. Their true range projectors therefore add exactly. This argument applies before restricting to top support.

## 6. Entropy estimate and remaining boundary

For r<=d m with 0<d<1/2, the elementary binomial estimate gives M<=exp[m h(d)]. To prove it, write x=d/(1-d)<1, use x^s>=x^r for s<=r, and bound

 M<=x^(-r)(1+x)^m<=x^(-dm)(1+x)^m=exp[m h(d)].

Combining this with n>=m(1-2d) and (5),

 M a_n<=exp[-m((1-2d)lambda-h(d))]
          +4N^2 exp[m h(d)-N/160].

Equations (6)–(7) make both exponentially small uniformly on [aN,bN]. Also M t^n is exponentially small at at least the first rate because log 2>lambda. The polynomial prefactors and denominator in (1)–(2) yield every strict exponent c<gamma. Nested raw balls give nested centered balanced ranges, so Q_r=P_r-P_0 is an orthogonal projector and its trace is the difference of the two separately controlled traces. The radius-zero case has a strictly better or equal rate, permitting the same strict c.

This crosses from o(N/log N) markers to a fixed positive fraction of m in the balanced sector, and to 0.49m in the off-charge sector using the stronger actual constant. It does not estimate the whole balanced complement, the off-charge high-Hamming complement, the full signed pair residual, plateau correction, or higher factorial comparison. Generic gap alone still cannot establish CUE statistics. The estimates do not use FM-022 reverse-path suppression and do not purport to absorb all reverse families.

The exact residual is

 I-P_H-Ptilde_r=(Pi-P_H-P_r)+[(I-Pi)-O_r].                  (16)

Both summands are orthogonal projections. Each is still unestimated in general. No equality with a once-counted coordinate-path mask or WKB stationary family is asserted for P_r or Ptilde_r; only O_r is literally the raw off-charge Hamming mask.

## 7. Dependencies and evidence boundary

- Accepted sparse-marker support grading and range-projector algebra: /workspace/shared/bgs_balanced_complement_attack/candidate_v1.md and growth_addendum.md; independent audit /workspace/shared/bgs_balanced_hamming_review/review.md.
- Actual singular bound and stronger 10^-64 limsup: BGS/mathematics/position_chain_mixing.md, Section 1 (FM-021), inherited with its existing analytic-review boundary.
- Haar tail (5): BGS/mathematics/ordered_diagonal_cyclic_trace.md, O5, inherited with its existing source chain.
- New algebra proved here: grouping into p/q position blocks, exact torus integral, shifted-seam contraction, entropy-radius implication, orthogonal off-charge split.
- No external theorem is added. Bounded exact controls are algebra/convention checks only and cannot certify the large-N conclusion.
