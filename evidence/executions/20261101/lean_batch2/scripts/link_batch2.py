"""Integrator script (Lean batch 2, 2026-11-01). Run once from the repository root.

Adds Lean links (`formalization`), a `formalization_scope` sentence and the batch receipt (`evidence`) to the
claims formalized in batch 2, then mirrors the changed rows into the curated record/claim_verification_inventory.json
(formalization, evidence, receipt counts, `lean_formalization` method tag, source_blob_sha), following
evidence/executions/20261101/lean_batch1/scripts/link_batch1.py. No claim state is changed. None of the batch-2 claims
is a sealed wave-2 row (none is in evidence/wave2_checked_20261007/raw/provenance/base_navigation/record/claims.json and
none has a historical_claim_amendments row), so record/claim_integration_epochs.json is not touched.

BGS-TRACE-297 already links formalization/Bgs/LineN4Gauge.lean (batch 1); the new corollary file is appended and the
scope sentence is replaced by the updated one."""
import json, hashlib
F = 'formalization/Bgs/'
RECEIPT = 'evidence/executions/20261101/lean_batch2/README.md'
LINKS = {
 'BGS-TRACE-297': ([F + 'LineN4Gauge.lean', F + 'LineN4GaugeTwist.lean'],
   'Partial: the two gauge identities L_tau T_sigma = T_{lambda sigma} L_{tau - kappa lambda sigma} and '
   'L_tau G_nu = G_{nu/lambda} L_{tau + nu/lambda} and T_sigma G_nu = e(nu sigma) G_nu T_sigma (LineN4Gauge), and the '
   'geometric-twist corollary prod_{i<n} L_{tau_i} = T_{-lambda sigma_{n-1}} G_{-b lambda^{1-n}} L_{t0}^n G_{lambda b} T_{sigma_0} '
   'by induction (LineN4GaugeTwist; scalar exactly 1 in this ordering, hence unimodular), for arbitrary weights, complex '
   'a, b, t0, kappa != 0, lambda != 0 and all functions C -> C (tsum form). The disc-space (small-gauge) reading is not formalized.'),
 'BGS-TRACE-211': ([F + 'LineIPhaseSplit.lean'],
   'Partial: Prop I1 Z_m(nu0 + delta) = Z_m(nu0) sigmahat(delta) for every integer delta, and total mass sum_p sigma(p) = 1, '
   'for any modulus M = 2h >= 1, any phases P(n) in Z and any complex nu0 with Z_m(nu0) != 0, for a finitely supported kick. '
   'The absolutely summable (infinitely supported k1) case and the halo heuristic are not formalized.'),
 'BGS-TRACE-218': ([F + 'LineIAliasing.lean'],
   'Partial: the first identity (1/q) sum_{nu mod q} |Z_m(nu/q)|^2 = sum_{n,n\'} Phihat(n) conj Phihat(n\') 1[q | P(n) - P(n\')] '
   '(= sum_j C_Z(jq), regrouped by j) for every q >= 1 and a finitely supported kick, with the character orthogonality '
   'sum_{nu<q} e(-nu k/q) = q 1[q | k]. The Moebius formula for F_m and the absolutely summable case are not formalized.'),
 'BGS-TRACE-229': ([F + 'LineJ3PrimeLevel.lean'],
   'Partial: the complete character-sum step over F_q (q prime): W = q^-2 sum_{t in F_q^*, t != t_b} e(N tbar/q) equals '
   'q^-2(-1 - e(N tbar_b/q)) with |W| <= 2/q^2 for N != 0, (q-2)/q^2 for N = 0, and without a missing label -1/q^2 resp. '
   '(q-1)/q^2. The completing-the-square identity conj G_t(0) G_t(beta) = q^2 e(N(beta) tbar/q), the label covering '
   '(F_q^* minus exactly one t_b), the count 2(q-1) of isotropic beta and the float checks are not formalized.'),
 'BGS-RES-023': ([F + 'ResonanceMarginConst.lean'],
   'Partial: the final arithmetic step only: the deposited integer B (verbatim from resonance_nondegeneracy_margin.json) '
   'satisfies 2^711 <= B < 2^712 (712 binary digits) and B <= 2^714, and Gamma >= (pi^2/41472) 2^(-2B) X with X >= 0 implies '
   'Gamma >= (pi^2/41472) 2^(-2^715) X, the printed (ND.10). The radius-eight certificate replay and the compilation of B '
   'from it are not formalized.'),
}
CP = 'record/claims.json'; raw = open(CP, encoding='utf-8').read(); d = json.loads(raw)
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
by = {c['id']: c for c in d['claims']}
for i, (files, scope) in LINKS.items():
    c = by[i]; assert c['state'] in ('proved', 'conditional'), i
    if i == 'BGS-TRACE-297':
        assert c['formalization'] == files[:1] and 'formalization_scope' in c, i
    else:
        assert not c['formalization'] and 'formalization_scope' not in c, i
    for f in files: open(f).close()
    c['formalization'] = files
    c['formalization_scope'] = scope
    if RECEIPT not in c['evidence']: c['evidence'].append(RECEIPT)
open(CP, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False) + '\n')
# ---------------- inventory mirror ----------------
P = 'record/claim_verification_inventory.json'; raw = open(P, encoding='utf-8').read(); v = json.loads(raw)
dump = lambda o: json.dumps(o, indent=1, ensure_ascii=False, separators=(',', ': ')); assert dump(v) == raw
EN = v['method_enumeration']; LF = 'lean_formalization'
for r in v['claims']:
    if r['id'] not in LINKS: continue
    c = by[r['id']]
    for x in ('evidence', 'verifiers', 'formalization'): r[x] = c[x]
    r['receipt_counts'] = {x: len(c[x]) for x in ('evidence', 'verifiers', 'formalization')}
    meth = set(r['methods']) - {'unevidenced'} | {LF}
    r['methods'] = [x for x in EN if x in meth]
    r['unevidenced'] = c['state'] == 'open' or not any(c[k] for k in ('evidence', 'verifiers', 'formalization'))
v['caveats'].append('1 November 2026 (Lean batch 2, evidence/executions/20261101/lean_batch2/README.md): Lean links and '
    'lean_formalization tags added to BGS-TRACE-211, TRACE-218, TRACE-229, RES-023, and the twist corollary file appended to '
    'BGS-TRACE-297; every link is partial (see formalization_scope in claims.json) and certifies only the statement named there. '
    'No state changed.')
b = open(CP, 'rb').read(); v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
open(P, 'w', encoding='utf-8').write(dump(v)); print('linked', sorted(LINKS), v['source_blob_sha'])
