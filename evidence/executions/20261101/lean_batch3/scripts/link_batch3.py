"""Integrator script (Lean batch 3, 2026-11-01). Run once from the repository root.

Adds or extends Lean links (`formalization`), the `formalization_scope` sentence and the batch receipt (`evidence`) for the
claims formalized in batch 3, appends a dated Lean note to the boundaries of BGS-TRACE-143 and BGS-TRACE-216 (whose
boundaries said "not formalised"), and mirrors the changed rows into the curated record/claim_verification_inventory.json,
following evidence/executions/20261101/lean_batch1/scripts/link_batch1.py. No claim state is changed.

BGS-FM-026 is a sealed wave-2 row (present in evidence/wave2_checked_20261007/raw/provenance/base_navigation/record/claims.json,
with a historical_claim_amendments row): its new link values are admitted through that row (fields `formalization` and
`evidence`, both keys of the sealed row) and no `formalization_scope` key is added; its scope is in the receipt. The other
claims are not sealed."""
import json, hashlib
F = 'formalization/Bgs/'
RECEIPT = 'evidence/executions/20261101/lean_batch3/README.md'
LINKS = {
 'BGS-TRACE-259': ([F + 'LineLLineOrth.lean'],
   'Partial: Lemma A1 in the model O/q = F_q x F_q (q odd split prime, s^2 = 2, frak q = ker(a + b sqrt2 -> a + s b), l(q) its '
   'annihilator under e(Tr(beta x)/q)): sum_{beta in l(q)} |Zhat_beta|^2 = q sum_u |A(u + q)|^2 and |D_q|^2 <= (1 - 1/q) C_q, '
   'C_q = sum_u |A(u + q)|^2 - |Z|^2/q, for A on O/q. The collision form C_q = 1 + sum R(v) - |Z|^2/q (Theorem U) is not formalized.'),
 'BGS-TRACE-267': ([F + 'LineLLineOrth.lean'],
   'Partial: Lemma Q (1/q) sum_{beta in l(q)} F(beta/q) = sum_{gamma in q} c_gamma for absolutely summable c on O = Z x Z, in the '
   'same model, with the line orthogonality and q | Nm(gamma) for gamma in q. The nonvanishing Nm(gamma) != 0 for gamma != 0 and '
   'the block-energy use for F = f_k are not formalized.'),
 'BGS-TRACE-211': ([F + 'LineIPhaseSplit.lean', F + 'LineISummable.lean'],
   'Prop I1 Z_m(nu0 + delta) = Z_m(nu0) sigmahat(delta) for every integer delta and total mass sum_p sigma(p) = 1, for any '
   'modulus M = 2h >= 1, integer phases P(n), real nu0 with Z_m(nu0) != 0, for finitely supported kicks (LineIPhaseSplit, any '
   'complex nu0) and for every kick with sum |Phihat| < infinity (LineISummable). This is the full registered identity; the halo '
   'description is a heuristic and not part of the claim.'),
 'BGS-TRACE-218': ([F + 'LineIAliasing.lean', F + 'LineIMoebius.lean', F + 'LineISummable.lean'],
   'Partial: the first identity (1/q) sum_{nu mod q} |Z_m(nu/q)|^2 = sum_{n,n\'} Phihat(n) conj Phihat(n\') 1[q | P(n) - P(n\')] '
   'for every q >= 1, for finite support and for sum |Phihat| < infinity (pair series); the Moebius formula F_m = phi(2h)^-1 '
   'sum_{e | 2h} mu(e) (2h/e) sum_{pairs} 1[(2h/e) | P(n) - P(n\')] for finite support (LineIMoebius). The regrouping of the pair '
   'sums into sum_j C_Z(j q) and the summable Moebius case are not formalized.'),
 'BGS-TRACE-229': ([F + 'LineJ3PrimeLevel.lean', F + 'LineJ3GaussSquare.lean'],
   'Partial: G_t(beta) = sum_gamma e(-(t Nm gamma + Tr beta gamma)/q) on O/q = F_q x F_q: completing the square G_t(beta) = '
   'e(tbar Nm beta/q) G_t(0), |G_t(0)|^2 = q^2, conj G_t(0) G_t(beta) = q^2 e(Nm(beta) tbar/q), hence q^-4 sum_{t != 0, t_b} '
   'conj G_t(0) G_t(beta) = q^-2(-1 - e(Nm beta tbar_b/q)) with |W| <= 2/q^2 (Nm beta != 0) and (q-2)/q^2 (Nm beta = 0), and '
   '-1/q^2, (q-1)/q^2 without a missing label; 2y\'^2 = 1 => 2 is a square; #{beta != 0 : Nm beta = 0} = 2(q-1). Not formalized: '
   'the label covering (frozen labels cover F_q^* minus exactly one t_b) and the float checks.'),
 'BGS-TRACE-216': ([F + 'LineIMonomial.lean'],
   'Partial: for the 16-state automaton tables of the eight cases (m in {9, 15, 21, 27}, a = +-2) exported from the verifier, '
   'the intertwining relations of all witnesses (X for a = 2, X against (-1)^n conj A_n^(9,2) for a = -2, Y for n -> -n) are '
   'checked by decide, and their matrix form X A = A\' X with X X^H = 1 is proved. Not formalized: the derivation of the tables '
   'from the G2 operators and every infinite-dimensional consequence.'),
 'BGS-TRACE-143': ([F + 'LineCDFTStar.lean'],
   'Partial: the matrix identities of Theorem 1 for odd N: M_N = Delta F_{1/4} Delta, P F_{1/4} P^-1 = F, and (P Delta)(D_theta '
   'M_N) = (D_theta\' F)(P Delta) with P Delta unitary, theta\'_x = theta_{2x} - 2 pi (6 8^-1 (2x)^2)/N. Not formalized: the '
   'measure-preserving property and the eigenvalue law, Remark 1\' (square class), the p = 1 mod 4 sign statement, the numerics.'),
 'BGS-FM-026': ([F + 'Fm026Counts.lean'], None),
 'BGS-TRACE-178': ([F + 'LineBTorsionSplit.lean'],
   'Partial: F = F_gen + F_tor for the Prop C double sum over norm classes mod h with an arbitrary pair weight (so for '
   'mu(q_rr\')/phi(q_rr\')), F_gen the pairs with r, r\' not = 0 mod p. Prop C itself and the numerical values are not formalized.'),
}
BOUNDARY_NOTES = {
 'BGS-TRACE-216': ' Lean note (Lean batch 3, 1 November 2026): the finite intertwining relations of all eight witnesses and of Y, '
   'and their matrix form with X unitary, are now checked in Lean (formalization/Bgs/LineIMonomial.lean) against the automaton '
   'tables exported from the verifier; the derivation of the tables and the infinite-dimensional consequences remain not formalised.',
 'BGS-TRACE-143': ' Lean note (Lean batch 3, 1 November 2026): superseding "Not formalized in Lean" for these identities, the matrix '
   'identities of Theorem 1 (M_N = Delta F_{1/4} Delta, P F_{1/4} P^-1 = F and the unitary conjugacy of D_theta M_N to D_theta\' F) '
   'are formalized in formalization/Bgs/LineCDFTStar.lean; the measure statement, the square-class remark and the numerics are not.',
}
SEALED = ('BGS-FM-026',)
CP = 'record/claims.json'; raw = open(CP, encoding='utf-8').read(); d = json.loads(raw)
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
by = {c['id']: c for c in d['claims']}
for i, (files, scope) in LINKS.items():
    c = by[i]; assert c['state'] in ('proved', 'conditional'), i
    old = c['formalization']; assert old == files[:len(old)], i
    for f in files: open(f).close()
    c['formalization'] = files
    if i not in SEALED: c['formalization_scope'] = scope
    else: assert 'formalization_scope' not in c
    if RECEIPT not in c['evidence']: c['evidence'].append(RECEIPT)
for i, note in BOUNDARY_NOTES.items():
    assert note.strip() not in by[i]['boundary']
    by[i]['boundary'] = by[i]['boundary'].rstrip() + note
open(CP, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False) + '\n')
EP = 'record/claim_integration_epochs.json'; raw = open(EP, encoding='utf-8').read(); e = json.loads(raw)
assert json.dumps(e, indent=2, ensure_ascii=False) + '\n' == raw
am = {r['id']: r for r in e['historical_claim_amendments']}
for i in SEALED:
    r = am[i]; c = by[i]
    r['fields']['formalization'] = c['formalization']; r['fields']['evidence'] = c['evidence']
    r['disposition'] += (' Lean batch 3 (1 November 2026): admit the formalization link ' + ', '.join(c['formalization']) +
        ' and the appended evidence receipt ' + RECEIPT + '; partial Lean coverage of the additive count bookkeeping named in '
        'that receipt only; no state, title, boundary, source or other contract-field change.')
    r['review'] += '; ' + RECEIPT
open(EP, 'w', encoding='utf-8').write(json.dumps(e, indent=2, ensure_ascii=False) + '\n')
P = 'record/claim_verification_inventory.json'; raw = open(P, encoding='utf-8').read(); v = json.loads(raw)
dump = lambda o: json.dumps(o, indent=1, ensure_ascii=False, separators=(',', ': ')); assert dump(v) == raw
EN = v['method_enumeration']; LF = 'lean_formalization'
for r in v['claims']:
    if r['id'] not in LINKS: continue
    c = by[r['id']]
    for x in ('boundary', 'evidence', 'verifiers', 'formalization'): r[x] = c[x]
    r['receipt_counts'] = {x: len(c[x]) for x in ('evidence', 'verifiers', 'formalization')}
    meth = set(r['methods']) - {'unevidenced'} | {LF}
    r['methods'] = [x for x in EN if x in meth]
    r['unevidenced'] = c['state'] == 'open' or not any(c[k] for k in ('evidence', 'verifiers', 'formalization'))
v['caveats'].append('1 November 2026 (Lean batch 3, evidence/executions/20261101/lean_batch3/README.md): Lean links and '
    'lean_formalization tags added to BGS-TRACE-259, TRACE-267, TRACE-216, TRACE-143, FM-026, TRACE-178, and further Lean files '
    'appended to BGS-TRACE-211, TRACE-218, TRACE-229; links are partial except where formalization_scope says otherwise '
    '(BGS-FM-026: scope in the receipt). Dated Lean notes appended to the boundaries of BGS-TRACE-143 and TRACE-216. No state changed.')
b = open(CP, 'rb').read(); v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
open(P, 'w', encoding='utf-8').write(dump(v)); print('linked', sorted(LINKS), v['source_blob_sha'])
