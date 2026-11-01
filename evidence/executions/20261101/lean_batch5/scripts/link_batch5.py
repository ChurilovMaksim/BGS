"""Integrator script (Lean batch 5, 2026-11-01). Run once from the repository root.

Adds or extends Lean links (`formalization`), the `formalization_scope` sentence and the batch receipt (`evidence`) for the
claims formalized in batch 5, and mirrors the changed rows (boundary, evidence, verifiers, formalization) into the curated
record/claim_verification_inventory.json, following evidence/executions/20261101/lean_batch4/scripts/link_batch4.py.
No claim state is changed. None of the batch-5 claims is a sealed wave-2 row, and none of their boundaries says
"not formalised", so no amendment row and no boundary note is touched."""
import json, hashlib
F = 'formalization/Bgs/'
RECEIPT = 'evidence/executions/20261101/lean_batch5/README.md'
LINKS = {
 'BGS-TRACE-222': ([F + 'LineJSectorConj.lean'],
   'Partial: the letter-weight transformations for w_{C,a,tau}(n) = ghat(n) e(Cn^2/2) e(an/8) e(n tau) with conj ghat(n) = '
   '(-1)^n ghat(n) and ghat(-n) = ghat(n) as hypotheses: K sends (C, a, tau) to (-C, 4 - a, -tau), R sends (C, a, tau) to '
   '(C, -a, -tau), RK sends (C, a, tau) to (-C, a - 4, tau) for every real twist tau; and, for matrices, if V\'_i = U conj(V_i) '
   'U^-1 for every factor then Tr prod V\'_i = conj Tr prod V_i for every finite word. Not formalized: the sector operators on '
   'the disc lattices, the reflection with symmetric rounding, RK as an isometry of the Line F spaces, the trace-class '
   'setting on l^2, and the Galerkin check.'),
 'BGS-TRACE-214': ([F + 'LineIHorocycle.lean'],
   'Partial: for finitely supported kicks and weights f(z_nu) = sum_k c_k e(k nu/M) with sum |c_k| < infinity: (a) '
   'sum_{nu mod M} |Z_nu|^2 f(z_nu) = M sum_k c_k C(k), C(k) = sum_{n,n\'} Phihat(n) conj Phihat(n\') 1[P(n) - P(n\') == k mod '
   'M], and (b) sum_{nu unit} |Z_nu|^2 f(z_nu) = sum_k c_k sum_{n,n\'} Phihat(n) conj Phihat(n\') c_M(k - P(n) + P(n\')), c_M the '
   'Ramanujan sum. Not formalized: summable (infinite-support) kicks; the remarks on the diagonal class and the R\' use.'),
 'BGS-TRACE-213': ([F + 'LineIReduction.lean'],
   'Partial: the exact identity W\'_m = phi^-1 sum_{nu unit, not resonant} (|Z_nu|^2 - RMT_m) + phi^-1 sum_{rho, d incl.} '
   'Dev_d(rho), Dev_d(rho) = sum_{nu in M_d(rho)} (|Z_nu|^2 - |Z_rho|^2/d^2), from the frozen definitions of F_m, Res_m and '
   'W\'_m, assuming that the sets {nu_rho} and M_d(rho) are pairwise disjoint units. Not formalized: that disjointness from '
   'the congruence definition, and the sufficiency (E\'\'), (T\'\'), (D) => R\'.'),
 'BGS-TRACE-317': ([F + 'LineIReduction.lean'],
   'Partial: the bookkeeping W\'_m = NR part + phi^-1 sum Dev_d(rho) (as in BGS-TRACE-213, disjointness assumed), '
   'NR >= -RMT_m when RMT_m >= 0, RMT_m = 4m - m^2/h <= 4m, and the level floor in the form Dev_d(rho) >= -n_d |Z_rho|^2/d^2. '
   'Not formalized: the floor in the form -(h_p/d) S_rho with its constants, and the inclusion threshold m0 = 15 (see '
   'LineMInclusion for the inclusion step of BGS-TRACE-273).'),
 'BGS-TRACE-218': ([F + 'LineIAliasing.lean', F + 'LineIMoebius.lean', F + 'LineISummable.lean', F + 'LineIRegroup.lean',
                    F + 'LineIMoebiusSummable.lean'],
   'Partial: the first identity (1/q) sum_{nu mod q} |Z_m(nu/q)|^2 = sum_{n,n\'} Phihat(n) conj Phihat(n\') 1[q | P(n) - P(n\')] '
   'for every q >= 1, for finite support and for sum |Phihat| < infinity (pair series); the Moebius formula F_m = phi(2h)^-1 '
   'sum_{e | 2h} mu(e) (2h/e) sum_{pairs} 1[(2h/e) | P(n) - P(n\')] for finite support and for sum |Phihat| < infinity (pair '
   'series, LineIMoebiusSummable); for finite support also the regrouping into sum_{j in Z} C_Z(j q) and the Moebius formula '
   'in C_Z form (LineIRegroup). Not formalized: the regrouping of absolutely convergent pair series into sum_j C_Z; the '
   'heuristic assessment is not part of the claim.'),
 'BGS-TRACE-293': ([F + 'LineN3SignConj.lean', F + 'LineN3SignConjComposite.lean'],
   'Partial: at prime levels q, W_{q,beta}(-rho) = conj W_{q,beta}(rho): nu0(-rho) = -nu0(rho) from 8 nu0 = 2 s g, the missing '
   'label t_b = j_b y\' (nu0 + c j_b = 0) changes sign, W(N, -t_b) = conj W(N, t_b) for every N, and the isotropic weights '
   '(q-2)/q^2 agree; at composite levels ce, the symmetry follows from the inheritance W_{ce, e beta\'} = (n_e/e^2) '
   'W_{c, beta\'} with the same real n_e for both signs (LineN3SignConjComposite), with BGS-TRACE-228 as a hypothesis. Not '
   'formalized: the inheritance theorem itself, the comparison with BGS-TRACE-221(ii), and the label covering.'),
}
CP = 'record/claims.json'; raw = open(CP, encoding='utf-8').read(); d = json.loads(raw)
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
by = {c['id']: c for c in d['claims']}
for i, (files, scope) in LINKS.items():
    c = by[i]; assert c['state'] in ('proved', 'conditional'), i
    old = c['formalization']; assert old == files[:len(old)], i
    for f in files: open(f).close()
    c['formalization'] = files
    c['formalization_scope'] = scope
    if RECEIPT not in c['evidence']: c['evidence'].append(RECEIPT)
open(CP, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False) + '\n')
P = 'record/claim_verification_inventory.json'; raw = open(P, encoding='utf-8').read(); v = json.loads(raw)
dump = lambda o: json.dumps(o, indent=1, ensure_ascii=False, separators=(',', ': ')); assert dump(v) == raw
EN = v['method_enumeration']; LF = 'lean_formalization'
seen = set()
for r in v['claims']:
    if r['id'] not in LINKS: continue
    seen.add(r['id']); c = by[r['id']]
    for x in ('boundary', 'evidence', 'verifiers', 'formalization'): r[x] = c[x]
    r['receipt_counts'] = {x: len(c[x]) for x in ('evidence', 'verifiers', 'formalization')}
    meth = set(r['methods']) - {'unevidenced'} | {LF}
    r['methods'] = [x for x in EN if x in meth]
    r['unevidenced'] = c['state'] == 'open' or not any(c[k] for k in ('evidence', 'verifiers', 'formalization'))
assert seen == set(LINKS), set(LINKS) - seen
v['caveats'].append('1 November 2026 (Lean batch 5, evidence/executions/20261101/lean_batch5/README.md): Lean links and '
    'lean_formalization tags added to BGS-TRACE-222, TRACE-214, TRACE-213, TRACE-317, and further Lean files appended to '
    'BGS-TRACE-218 and TRACE-293; all links are partial as stated in formalization_scope. No state changed.')
b = open(CP, 'rb').read(); v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
open(P, 'w', encoding='utf-8').write(dump(v)); print('linked', sorted(LINKS), v['source_blob_sha'])
