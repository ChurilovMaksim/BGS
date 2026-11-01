"""Integrator script (Lean batch 4, 2026-11-01). Run once from the repository root.

Adds or extends Lean links (`formalization`), the `formalization_scope` sentence and the batch receipt (`evidence`) for the
claims formalized in batch 4, and mirrors the changed rows (boundary, evidence, verifiers, formalization) into the curated
record/claim_verification_inventory.json, following evidence/executions/20261101/lean_batch3/scripts/link_batch3.py.
No claim state is changed. None of the batch-4 claims is a sealed wave-2 row, and none of their boundaries says
"not formalised", so no amendment row and no boundary note is touched."""
import json, hashlib
F = 'formalization/Bgs/'
RECEIPT = 'evidence/executions/20261101/lean_batch4/README.md'
LINKS = {
 'BGS-TRACE-204': ([F + 'LineGDilution.lean'],
   'Partial: on O/d = Z/d x Z/d for every modulus d (prime or composite) and every unit t mod d: the completed square '
   't Nm gamma + Tr(beta gamma) = t Nm(gamma + tbar conj beta) - tbar Nm beta, hence G_t(beta) = e(tbar Nm beta/d) G_d(t), and '
   'the dilution identity d^-2 sum_beta Zhat(beta) G_t(beta) = (G_d(t)/d^2) sum_beta e(tbar Nm beta/d) Zhat(beta) for any '
   'Zhat. Prop I2\' (BGS-TRACE-212) is the input and not re-proved; |G_d(t)| = d is formalized at primes only; the main-term '
   'remarks and the brute-force checks are not formalized.'),
 'BGS-TRACE-293': ([F + 'LineN3SignConj.lean'],
   'Partial: at prime levels q, W_{q,beta}(-rho) = conj W_{q,beta}(rho): nu0(-rho) = -nu0(rho) from 8 nu0 = 2 s g, the missing '
   'label t_b = j_b y\' (nu0 + c j_b = 0) changes sign, W(N, -t_b) = conj W(N, t_b) for every N, and the isotropic weights '
   '(q-2)/q^2 agree. Not formalized: the composite levels via inheritance (BGS-TRACE-228), the comparison with BGS-TRACE-221(ii), '
   'and the label covering (taken from the frozen definition).'),
 'BGS-TRACE-267': ([F + 'LineLLineOrth.lean', F + 'LineL3Quadrature.lean'],
   'Partial: Lemma Q (1/q) sum_{beta in l(q)} F(beta/q) = sum_{gamma in q} c_gamma for absolutely summable c on O = Z x Z '
   '(model O/q = F_q x F_q, s^2 = 2), q | Nm(gamma) for gamma in q, Nm(gamma) = a^2 - 2b^2 != 0 for gamma != 0 (irrationality '
   'of sqrt 2), hence |Nm gamma| >= q on q minus 0, and the average is exactly c_0 when c_gamma = 0 for every gamma != 0 with '
   '|Nm gamma| >= q. The block-energy use for F = f_k (the band [I_k - T_k(q), I_k + T_k(q)]) is not formalized.'),
 'BGS-TRACE-254': ([F + 'LineLCollisionForm.lean'],
   'Partial: for finitely supported w with R(v) = sum_n w(n) conj w(n - v) and any additive alpha: the collision form '
   'sum_u |A(u)|^2 = sum_{v in s - s, alpha_v = 0} R(v) (at any level); if R vanishes at every collision v != 0 (exact or mod h) '
   'then sum_x |A(x)|^2 = sum_n |w(n)|^2; Parseval on O/h = (Z/h)^2 for odd h, sum_beta |Zhat_beta|^2 = h^2 sum_x |A(x)|^2; '
   'hence, with sum |w|^2 = 1, sum_x |A(x)|^2 = 1 and sum_beta |Zhat(beta/h)|^2 = h^2. Theorem U itself (Lemma U1 and the '
   'Bessel/Neumann vanishing of R, sum J_n(1.8)^2 = 1) is not formalized and enters as hypotheses.'),
 'BGS-TRACE-259': ([F + 'LineLLineOrth.lean', F + 'LineLCollisionForm.lean'],
   'Partial: Lemma A1 in the model O/q = F_q x F_q (q odd split prime, s^2 = 2, frak q = ker(a + b sqrt2 -> a + s b), l(q) its '
   'annihilator under e(Tr(beta x)/q)): sum_{beta in l(q)} |Zhat_beta|^2 = q sum_u |A(u + q)|^2 and |D_q|^2 <= (1 - 1/q) C_q, '
   'C_q = sum_u |A(u + q)|^2 - |Z|^2/q, for A on O/q; and the collision form for finitely supported w (LineLCollisionForm): '
   'sum_u |A(u + q)|^2 = sum|w|^2 + sum_{v != 0, alpha_v in q} R(v), so that, when the exact collisions alpha_v = 0, v != 0 '
   'have R(v) = 0 and sum|w|^2 = 1, C_q = 1 + sum_{alpha_v in q minus 0} R(v) - |Z|^2/q. Theorem U (the vanishing of R at exact '
   'collisions, sum|w|^2 = 1) is a hypothesis, not formalized.'),
 'BGS-TRACE-255': ([F + 'LineL2Decomp.lean'],
   'Partial: in the model O/q = F_q x F_q (q odd, frak q = ker phi_s, frak qbar = ker phi_{-s}, s != 0), for any A on O/q: '
   'A(frak q) = q^-1 sum_{beta in l(q)} Zhat_beta, A(qO) = q^-2 sum_beta Zhat_beta, D_q = q^-1 sum_{beta in l(q) minus 0} '
   'Zhat_beta, A(qO) - A_tot/q^2 = q^-2 sum_{beta != 0} Zhat_beta, q cap qbar = qO, and D_iso := A(q cup qbar) - ((2q-1)/q^2) '
   'A_tot = D_q + D_qbar - (A(qO) - A_tot/q^2). The use with Theorem K1 (BGS-TRACE-237) is not formalized.'),
 'BGS-TRACE-218': ([F + 'LineIAliasing.lean', F + 'LineIMoebius.lean', F + 'LineISummable.lean', F + 'LineIRegroup.lean'],
   'Partial: the first identity (1/q) sum_{nu mod q} |Z_m(nu/q)|^2 = sum_{n,n\'} Phihat(n) conj Phihat(n\') 1[q | P(n) - P(n\')] '
   'for every q >= 1, for finite support and for sum |Phihat| < infinity (pair series); for finite support also the regrouping '
   'into sum_{j in Z} C_Z(j q) and the Moebius formula F_m = phi(2h)^-1 sum_{e | 2h} mu(e) (2h/e) sum_j C_Z(j 2h/e) '
   '(LineIRegroup), i.e. both displayed identities for finitely supported kicks. The summable Moebius case and the regrouping '
   'of absolutely convergent pair series are not formalized; the heuristic assessment is not part of the claim.'),
 'BGS-TRACE-273': ([F + 'LineMInclusion.lean'],
   'Partial: only the inclusion step: |Z_rho|^2 >= 4 m h implies |Z_rho|^2/d^2 >= 4m for every d | h with 1 < d <= sqrt h. '
   'The certified Line F F3 lower bound, the interval check for odd m in [15, 20001], the monotonicity argument and the '
   'm = 9, 11, 13 remarks are not formalized.'),
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
v['caveats'].append('1 November 2026 (Lean batch 4, evidence/executions/20261101/lean_batch4/README.md): Lean links and '
    'lean_formalization tags added to BGS-TRACE-204, TRACE-293, TRACE-254, TRACE-255, TRACE-273, and further Lean files '
    'appended to BGS-TRACE-267, TRACE-259, TRACE-218; all links are partial as stated in formalization_scope. No state changed.')
b = open(CP, 'rb').read(); v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
open(P, 'w', encoding='utf-8').write(dump(v)); print('linked', sorted(LINKS), v['source_blob_sha'])
