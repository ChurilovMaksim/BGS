"""Integrator script (Lean batch 1, 2026-11-01). Run once from the repository root.

Adds Lean links (`formalization`), a `formalization_scope` sentence and the batch receipt (`evidence`) to the
claims formalized in batch 1, then mirrors the changed rows into the curated record/claim_verification_inventory.json
(formalization, evidence, receipt counts, `lean_formalization` method tag, source_blob_sha), following the procedure of
evidence/executions/20261101/lineNgas/v5_integration/scripts/edit_inv_epochs_v5.py. No claim state is changed.

BGS-FM-001 and BGS-FM-009 are sealed wave-2 rows (wave2/wave3_integration_audit.py): for them the new link values are
admitted through their existing `historical_claim_amendments` rows in record/claim_integration_epochs.json (fields
`formalization` and `evidence`, which exist in the sealed rows), and no `formalization_scope` key is added (the audit admits
no new keys); their scope is recorded in evidence/executions/20261101/lean_batch1/README.md, the linked receipt."""
import json, hashlib
F = 'formalization/Bgs/'
RECEIPT = 'evidence/executions/20261101/lean_batch1/README.md'
LINKS = {
 'BGS-FM-001': ([F + 'Fm001Statement.lean', F + 'Fm001Exact.lean'],
   'Partial: proves the section 1 exact Weyl dictionary (ordinary Weyl quantization of g equals A_N for odd N) and the section 3 '
   'Fourier data (weight 51451/1000, exactly 32 nonzero modes) stated in Fm001Statement. The section 2 dynamical conclusions '
   '(Anosov, centralizer, reversor, affine conjugacy) and the derivative bounds (5) are not formalized.'),
 'BGS-FM-009': ([F + 'Fm009TraceObstruction.lean', F + 'Fm009CubeArith.lean'],
   'Partial: the implication common reversor => Tr([A,M]^3) = 0 for complex matrices, and the integer arithmetic '
   'S^3 - I = 14 [[7,10],[5,7]], det = -196, invertible modulo every N coprime to 14. The nonvanishing Tr[A_N,M_N]^3 != 0 '
   '(Laurent-polynomial certificate, metaplectic character formula, cyclotomic exclusion) is not formalized.'),
 'BGS-RET-004': ([F + 'RetTowerGeometry.lean'],
   'Partial: the section 3 finite exact-rational tower certificate (S^3, 30 separation inequalities, candidate completeness, '
   'j = 1, 2 emptiness, lobe gap 37/528, area 1/288). The bracket nonvanishing {g,Cg} != 0, Gamma_T(g) = 0 and the analytic '
   'RW3/RW7 statements are not formalized.'),
 'BGS-FM-036': ([F + 'PellModuliArith.lean'],
   'Partial: the section 4 Pell-moduli arithmetic only (N^2 - 2F^2 = -1, s = 2F = F^-1 with s^2 = 2, (1+s)^K = 1, h = 3+2s, '
   'h^K = 1, h - 1 = 2(1+s); for K prime, order of h exactly K modulo every prime p | N, 1 - h^j and 1 + h^j units). '
   'The Weyl implementer, the multiplicity count and all spectral conclusions of Theorem C are not formalized.'),
 'BGS-TRACE-248': ([F + 'LineLCollision.lean'],
   'Partial: lambda^2 - 6 lambda + 1 = 0, alpha_v = 0 iff (X^2 - 6X + 1) | v(X) in Z[X], the carry recursion '
   'v_j = e_j - 6e_{j-1} + e_{j-2}, and the referee check (only v = 0 with |v_j| <= 3, k = 6, indices 0..5). '
   'The Green-function carry bound with C0g = 1/(lambda - lambda^-1) and the transfer-matrix reading are not formalized.'),
 'BGS-TRACE-271': ([F + 'LineM3Const.lean', F + 'LineN16Arith.lean'],
   'Partial: part (c) constant arithmetic only: mu_lo^2/lambda^(2/3) >= 1.13287 and mu_lo^2/(lambda^(2/3) * 1.0184224) >= 1.11238 '
   '(real rpow statements). Parts (a), (b), (d), (e), the Prop K2 per-level bound and the Line F certified bound are not formalized.'),
 'BGS-TRACE-291': ([F + 'LineN3Order.lean'],
   'Partial: the order statement only: for odd primes p, q with q | h_p and a square root s of 2 mod q (split q), '
   'l = image of lambda under sqrt2 -> s has order exactly p (lambda^p = 1 + 2 h_p eps^p, N(lambda - 1) = -4). The '
   'twist-sequence description and orbit count are not formalized.'),
 'BGS-TRACE-297': ([F + 'LineN4Gauge.lean'],
   'Partial: the two gauge identities L_tau T_sigma = T_{lambda sigma} L_{tau - kappa lambda sigma} and '
   'L_tau G_nu = G_{nu/lambda} L_{tau + nu/lambda} (arbitrary weights, all functions, tsum form) and T_sigma G_nu = '
   'e(nu sigma) G_nu T_sigma. The geometric-twist product corollary is not formalized.'),
}
SEALED = ('BGS-FM-001', 'BGS-FM-009')
CP = 'record/claims.json'; raw = open(CP, encoding='utf-8').read(); d = json.loads(raw)
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
by = {c['id']: c for c in d['claims']}
for i, (files, scope) in LINKS.items():
    c = by[i]; assert c['state'] in ('proved', 'conditional'), i
    assert not c['formalization'] and 'formalization_scope' not in c, i
    for f in files: open(f.replace('formalization/', 'formalization/', 1)).close()
    c['formalization'] = files
    if i not in SEALED: c['formalization_scope'] = scope
    if RECEIPT not in c['evidence']: c['evidence'].append(RECEIPT)
open(CP, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False) + '\n')
# ---------------- sealed rows: reviewed amendment fields ----------------
EP = 'record/claim_integration_epochs.json'; raw = open(EP, encoding='utf-8').read(); e = json.loads(raw)
assert json.dumps(e, indent=2, ensure_ascii=False) + '\n' == raw
am = {r['id']: r for r in e['historical_claim_amendments']}
for i in SEALED:
    r = am[i]; c = by[i]
    r['fields']['formalization'] = c['formalization']; r['fields']['evidence'] = c['evidence']
    r['disposition'] += (' Lean batch 1 (1 November 2026): admit the formalization links ' + ', '.join(c['formalization']) +
        ' and the appended evidence receipt ' + RECEIPT + '; partial Lean coverage of the finite/algebraic statements named '
        'in that receipt only; no state, title, boundary, source or other contract-field change.')
    r['review'] += '; ' + RECEIPT
open(EP, 'w', encoding='utf-8').write(json.dumps(e, indent=2, ensure_ascii=False) + '\n')
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
v['caveats'].append('1 November 2026 (Lean batch 1, evidence/executions/20261101/lean_batch1/README.md): Lean links and '
    'lean_formalization tags added to BGS-FM-001, FM-009, FM-036, RET-004, TRACE-248, TRACE-271, TRACE-291, TRACE-297; '
    'every link is partial (see formalization_scope in claims.json) and certifies only the finite/algebraic statement named there. '
    'No state changed.')
b = open(CP, 'rb').read(); v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
open(P, 'w', encoding='utf-8').write(dump(v)); print('linked', sorted(LINKS), v['source_blob_sha'])
