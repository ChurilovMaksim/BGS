"""Generates INVENTORY.md from record/claims.json at a562e0cf; the class column is a manual planning judgement encoded in A/B."""
import json,collections
import subprocess
d=json.loads(subprocess.run(['git','show','a562e0cf:record/claims.json'],capture_output=True,check=True).stdout);c=d['claims']
pc=[x for x in c if x['state'] in ('proved','conditional')]
A={
'BGS-FM-001':'Fm001Exact: prove the §1 Weyl dictionary and §3 Fourier weight 51451/1000 and 32-mode count stated in Fm001Statement (batch 1)',
'BGS-FM-009':'Fm009TraceObstruction (existing implication kernel) + Fm009CubeArith: S³−I = 14·B, det B = −1, unit mod N (batch 1)',
'BGS-RET-004':'RetTowerGeometry (existing §3 finite certificate, previously unlinked) (batch 1)',
'BGS-FM-036':'PellModuliArith: §4 Pell-moduli arithmetic (N²−2F²=−1, s=2F, h^K=1, ord h = K mod every p | N) (batch 1)',
'BGS-TRACE-248':'LineLCollision: λ²−6λ+1=0, α_v=0 ⇔ (X²−6X+1)|v, carry recursion, k=6 referee check (batch 1)',
'BGS-TRACE-271':'LineM3Const: part (c) constants μ_lo²/λ^{2/3} ≥ 1.13287 and excess ≥ 1.11238 (batch 1)',
'BGS-TRACE-291':'LineN3Order: order of l = λ mod q′ is exactly p (batch 1)',
'BGS-TRACE-178':'finite-sum split F = F_gen + F_tor over norm classes (Finset.sum_filter_add_sum_filter_not) once F is defined',
'BGS-TRACE-273':'explicit inequality |Z|² ≥ 4 m h_m on m ∈ [15, 20001] plus monotonicity: interval/rational bounds on μ_lo^m vs h_m',
'BGS-FM-026':'arithmetic of the counts 612N/625+7, 24N/25+875 (875=840+35) and special values 4333, 107443 given the multiplicity inputs',
'BGS-RES-023':'constant chain B ≤ 2^714 ⇒ 2^(−2B) ≥ 2^(−2^715), π²/41472 factor (given the deposited integer B)',
'BGS-TRACE-216':'finite monomial matrices over 8th roots of unity: X A X⁻¹ = A′ for the 8 cases (needs the deposited automaton data)',
'BGS-TRACE-317':'level bookkeeping inequalities NR ≥ −RMT ≥ −4m and inclusion threshold m0 = 15 (finite arithmetic part)',
}
B={
'BGS-FM-005':'exact low-rank Jacobi decomposition as a matrix identity over ℂ',
'BGS-FM-007':'exact seven-cut generator reduction (finite Weyl-basis algebra)',
'BGS-FM-008':'nonvanishing of metaplectic minors (finite algebraic certificate)',
'BGS-FM-010':'power-trace nonvanishing: algebraic/cyclotomic part',
'BGS-FM-015':'explicit commutator generating action (trigonometric polynomial identity)',
'BGS-FM-024':'scalar joint commutant (finite-dimensional linear algebra over Weyl basis)',
'BGS-FM-025':'simple spectrum of A_{7·5^e} (finite-field/representation algebra)',
'BGS-FM-032':'prime cyclic cohomology identities in a finite cyclic module',
'BGS-RES-006':'adjoint-resolvent representation (finite-dimensional resolvent algebra)',
'BGS-RES-012':'finite quantum cyclic module and variance identity',
'BGS-RES-013':'balanced-phase completion and phase-rank (finite rank computation)',
'BGS-RES-017':'controllability for odd N (finite Lie-algebra generation)',
'BGS-TRACE-002':'exact Fourier trace representation of factorial statistics (finite sums)',
'BGS-TRACE-009':'exact spectral comb for the prime-resonant sector',
'BGS-TRACE-022':'exact balanced-pair Schur energy (finite algebra)',
'BGS-TRACE-026':'hook-cycle cancellation and Eulerian trees (combinatorics)',
'BGS-TRACE-085':'exact root lifting (polynomial algebra)',
'BGS-TRACE-088':'rooted BEST count (combinatorial count; dense-mixing part analytic)',
'BGS-TRACE-109':'inserted trace / commutant projection identities',
'BGS-TRACE-110':'scalar-root comparison lemmas',
'BGS-TRACE-143':'M_N = Δ F_{1/4} Δ and P F_{1/4} P⁻¹ = F (finite DFT/metaplectic identity)',
'BGS-TRACE-184':'exact IFS transfer-operator law at the resonant residue (finite alphabet)',
'BGS-TRACE-204':'dilution identity (Gauss sums over O/d)',
'BGS-TRACE-211':'relative phase split Z(ν0+δ) = Z(ν0) σ̂(δ) (finite Fourier identity)',
'BGS-TRACE-213':'exact reduction identity of Conjecture R′ (bookkeeping identity)',
'BGS-TRACE-214':'Fourier expansion via Ramanujan sums (finite)',
'BGS-TRACE-218':'Möbius aliasing identity (finite Fourier orthogonality + Möbius inversion)',
'BGS-TRACE-222':'sector-level antiunitary map (finite conjugation identity)',
'BGS-TRACE-226':'lifted trace formula on a 2-dim monomial block',
'BGS-TRACE-229':'complete Gauss-sum weights over F_q (finite-field character sums)',
'BGS-TRACE-237':'light-cone identity (finite-field sums)',
'BGS-TRACE-254':'level-h scalar L² unitarity (Parseval on O/h)',
'BGS-TRACE-255':'L2 decomposition D_q, D_iso (finite sums)',
'BGS-TRACE-259':'exact second moment mod q (Parseval on O/q)',
'BGS-TRACE-263':'walk-measure form A = χ B_m (finite Fourier identity)',
'BGS-TRACE-267':'exact line quadrature (orthogonality on l(q))',
'BGS-TRACE-293':'W(−ρ) = conj W(ρ) (finite symmetry of Gauss sums)',
'BGS-TRACE-297':'LineN4Gauge: gauge identities L_τT_σ = T_{λσ}L_{τ−κλσ}, L_τG_ν = G_{ν/λ}L_{τ+ν/λ}, T_σG_ν = e(νσ)G_νT_σ (batch 1)',
'BGS-CAYLEY-007':'three-scalar split support (resultant/ideal algebra)',
'BGS-CAYLEY-008':'scaling rigidity (polynomial algebra)',
'BGS-FM-014':'finite type for translated symbol differences (trigonometric-polynomial algebra)',
'BGS-FM-023':'exclusion of bounded-power translation algebras (finite algebra part)',
}
rows=[];cnt=collections.Counter()
lean_have=[x for x in pc if x['formalization']]
for x in pc:
  if x['formalization']: continue
  i=x['id']
  if i in A: cl,t='a',A[i]
  elif i in B: cl,t='b',B[i]
  else: cl,t='c','out of scope today (analytic, asymptotic, probabilistic, or certified floating/interval numerics needing heavy infrastructure)'
  cnt[cl]+=1
  rows.append((i,x['title'].replace('|','/'),x['state'],cl,t))
L=[]
L.append('# Lean inventory, 1 November 2026\n')
L.append('Base: origin/main a562e0cf (branch lean-batch-1). Source: `record/claims.json` (registry view `record/claim_registry.md`), read at a562e0cf (before the batch-1 links were added) by `make_inventory.py` in this directory (run from the repository root).\n')
L.append(f'* Registry: {len(c)} claims; proved/conditional: {len(pc)}; all non-open (proved, conditional, verification-pending, refuted): {sum(1 for x in c if x["state"]!="open")}.')
L.append(f'* Proved/conditional claims that already linked Lean files before batch 1: {len(lean_have)} (144 non-open claims in total link Lean; 155 modules in `formalization/Bgs`).')
L.append(f'* Proved/conditional claims without Lean before batch 1: {len(rows)}: class (a) {cnt["a"]}, class (b) {cnt["b"]}, class (c) {cnt["c"]}.\n')
L.append('Classes: **(a)** finite or arithmetic statements (exact identities, finite computations, explicit rational/real constant inequalities, combinatorial counts, Pell / finite-field facts), directly formalizable; **(b)** finite-dimensional or algebraic lemmas formalizable with modest effort; **(c)** analytic, asymptotic or probabilistic results (and large certified floating/interval numerics) that need heavy Mathlib infrastructure, out of scope today. Classification is a planning judgement from the registry title, boundary and source; for claims in (a)/(b) it concerns the finite/algebraic **part** named in the target column, not the whole claim unless stated.\n')
L.append('Claims marked "(batch 1)" were formalized (partially) in `evidence/executions/20261101/lean_batch1/`: 7 of class (a) and 1 of class (b) (BGS-TRACE-297). After batch 1, 211 proved/conditional claims have no Lean link: 6 in (a), 41 in (b), 164 in (c).\n')
L.append('## Proved/conditional claims already linking Lean\n')
L.append(', '.join(f'`{x["id"]}`' for x in lean_have)+'\n')
L.append('## Proved/conditional claims without Lean (before batch 1)\n')
L.append('| Claim | Title | State | Class | Planned Lean target |')
L.append('|---|---|---|---|---|')
order={'a':0,'b':1,'c':2}
for r in sorted(rows,key=lambda r:(order[r[3]],r[0])):
  L.append(f'| {r[0]} | {r[1]} | {r[2]} | ({r[3]}) | {r[4]} |')
open('evidence/executions/20261101/lean_inventory/INVENTORY.md','w',encoding='utf-8').write('\n'.join(L)+'\n')
print(cnt,len(rows),len(lean_have))
