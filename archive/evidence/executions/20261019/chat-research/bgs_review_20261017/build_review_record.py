#!/usr/bin/env python3
"""Build external research records; read BGS and the original attachment only."""
from pathlib import Path
from collections import Counter
import hashlib,json,shutil


ROOT=Path(__file__).resolve().parent
WORK=ROOT.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,value):(ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')


def main():
    original=WORK/'upload/two_channel_transmission(4).md'
    inventory=json.loads((ROOT/'attachment_inventory.json').read_text())
    assert sha(original)==inventory['sha256']
    inventory['review_policy']={
      'mathematical_arguments':'Arguments were read and critically scoped; this is not a formal line-by-line certificate.',
      'external_theorems':'Only sources explicitly listed in review_and_progress.md were independently checked for the stated application.',
      'numeric_tables':'Original large Monte Carlo tables were not rerun and remain diagnostic.',
      'new_results':'Author working proofs and exact finite controls; conditional hypotheses remain explicit.'}
    administrative={1,2,23,59,65,73}
    diagnostic={18,64,66,74,75}
    external={25,29,30,32,54,55,56,57,58}
    relevant={
      12:('accepted_sufficient_criterion','L2 contraction accepted with an explicit density hypothesis; no density bound derived from G.'),
      13:('accepted_conditional_G','Rank and absolute continuity reconstructed; strengthened to TV compactness in a separate proof.'),
      24:('accepted_and_reused','The linear-k tail was already proved here; it is restored in QC7.'),
      31:('scope_checked','Involution and support claims checked algebraically; displayed numerical table not rerun.'),
      33:('accepted_finite_identity','One-step positive variance and signed reverse-direction correction checked; no global recursion closure.'),
      34:('accepted_model_result','Poisson optical class explicitly assumes an independent Haar ingredient; not inferred for deterministic input.'),
      38:('accepted_with_exact_controls','Harmonic formulas checked using 268 exact branching cases; all-weight proof remains analytic.'),
      39:('partly_recomputed','Degree-two covariance table independently rebuilt at N=4,5,7,10; DR14--DR16 not separately fully recomputed.'),
      41:('accepted_finite_reduction','Positive clock-weighted Ward identities accepted; conditional isotropy remains unproved.'),
      42:('accepted_scope_barrier','Conditional finite-probe G is not a growing-index cavity CLT; the stated countermodels remain outside the original class.'),
      43:('accepted_auxiliary','Haar reverse coupling and marked-column support are exact; they do not construct an arbitrary coherent counterexample.'),
      44:('accepted_scope_barrier','Flat algebraic families and exact global trace anomaly accepted; a global trace anomaly is not a local BGS or transmission counterexample.'),
      45:('accepted_scope_barrier','All tensor moment singular spectra can lose orientation information; finite anomaly does not settle an asymptotic sequence.'),
      46:('accepted_finite_regularity','Nonzero transverse symplectic Jacobian is a finite AC result, not a uniform density estimate.'),
      47:('accepted_and_extended','Marked-column consistency and first-clock limits reused; TV and weighted-measure passage strengthened separately.'),
      48:('accepted_with_external_representation','Finite marked decoupling retains its exchangeable-representation input; inverse-Wishart Haar law is a benchmark, not an assumption on the actual model.'),
      49:('accepted_necessary_constraints','Root-frequency measure constraints and Haar target checked; the common measure is not identified from G.'),
      50:('accepted_scope_barrier','One-sided Cauchy substitutions checked; mixed-signature information is not supplied.'),
      51:('accepted_scope_barrier','All positive-source probes after external mixing are still automatic under global phase invariance.'),
      52:('accepted_nonuniqueness_control','Exact Gram-positive nonuniform laws only refute a weakened criterion; no full coherent G family constructed.'),
      53:('accepted_auxiliary','Two-step contractions are for specified reduced channels/classical chain, not the full unitary adjoint.'),
      60:('accepted_finite_identity','Conditional holomorphic evaluation and mixed determinant wedge do not identify the unweighted balanced T moments.'),
      61:('accepted_finite_regularity','Shortest-path argument gives generic coupling and complete escape under irreducibility.'),
      62:('accepted_and_reused','Exact Kac/controllability identity reused in linear scalar and tensor clocks.'),
      63:('accepted_with_exact_controls','Length-two signed cooperon identity checked against coherent word enumeration.'),
      67:('accepted_finite_identity','Rank-one source spectral averaging keeps the source weight and all cavity phases.'),
      68:('accepted_finite_identity','Fractional transform has bounded continuous endpoint extension for 0<s<1.'),
      69:('accepted_equivalent_criterion','Complete bounded fractional-overlap criterion incorporated; its target value remains unproved.'),
      70:('accepted_finite_identity','Matrix controllability identity does not equipartition the output Gramian.'),
      71:('accepted_finite_identity','Determinantal and Mahler identities checked; no logarithmic asymptotic inferred from positive moments.'),
      72:('accepted_scope_barrier','Sharp deterministic exceptional scar is at exceptional phases; not a typical probabilistic counterexample.'),
      76:('accepted_finite_identity','Hardy coordinate orthonormality retained under stability/generic escape.'),
      77:('accepted_finite_identity','Model-space and phase-speed identities retained with their exact normalization.'),
      78:('accepted_benchmark','Complex Student field is a Haar benchmark with a shared Gamma denominator.'),
      79:('accepted_scope_barrier','Higher unregularized cavity moments may diverge; numerical benchmark not rerun.'),
      80:('accepted_candidate_family','Cubic circulant algebra checked; no anomalous asymptotic T established.'),
      81:('accepted_candidate_family','Classical spectral gap follows from a nondegenerate quadratic Gauss sum.'),
      82:('accepted_with_external_Weil','Cubic additive Weil bound conditions checked in Kowalski Theorem 3.2; numerical tables not rerun.'),
      83:('strengthened_and_labels_corrected','Classical CE1--CE17 renamed CL1--CL17 in proposed patch; new 4B/N bound covers every retained size.'),
      84:('accepted_and_reused','Matched occupations and the first signed correction reused; individual absolute path pairs must not be summed.'),
      85:('accepted_window_bound','Kac/short-degree localization accepted; central O(N)-length coefficients remain unknown.'),
      86:('accepted_scope_boundary','Classical and quantum complements distinguished; no equipartition conclusion accepted.'),
      87:('independently_recomputed_finite','All 12 ordered pairs give exact mean 23/45; not an asymptotic counterexample.'),
      88:('sharpened_in_proposed_patch','QC35--QC37 restored to linear k by rational-degree/area argument; simultaneous k=o(log N).')}
    for index,section in enumerate(inventory['sections'],1):
        section['section_number']=index
        if index in relevant:status,note=relevant[index]
        elif index in diagnostic:status,note='diagnostic_or_code_only','Code inspected structurally; large original numerical run not repeated. All 12 embedded Python blocks separately pass AST parsing.'
        elif index in administrative:status,note='scope_or_summary_reviewed','Administrative, literature-scope or summary material; not a separate mathematical proof certificate.'
        elif index in external:status,note='argument_reviewed_external_input_retained','Internal argument read and scoped; representation/classification/analytic source dependencies retained, not independently certified in full.'
        else:status,note='argument_and_scope_reviewed','Finite/internal argument read and checked for stated scope; no automatic promotion to two-channel universality.'
        section['audit_status']=status;section['audit_note']=note
    inventory['structural_corrections']='attachment_corrections.patch; see structure_audit.json'
    write('attachment_inventory.json',inventory)

    baseline_path=WORK/'bgs_focus_20261016/repo_before.json'
    baseline=json.loads(baseline_path.read_text());repo=WORK/'BGS'
    current={str(p.relative_to(repo)):sha(p) for p in repo.rglob('*') if p.is_file()}
    integrity={'baseline_sha256':sha(baseline_path),'expected_files':len(baseline),
       'actual_files':len(current),'changed':[p for p in baseline if p in current and baseline[p]!=current[p]],
       'missing':sorted(set(baseline)-set(current)),'added':sorted(set(current)-set(baseline)),
       'git_mutations_performed':False}
    integrity['all_unchanged']=not integrity['changed'] and not integrity['missing'] and not integrity['added']
    assert integrity['all_unchanged'] and len(current)==716
    write('repo_integrity.json',integrity)

    previous=json.loads((WORK/'bgs_focus_20261017/proof_inputs.json').read_text())
    inputs=[{'workspace_relative_path':str(original.relative_to(WORK)),'sha256':sha(original),
             'library_file_id':'libfile_998a498fb36c8191b76d16e599c40165','role':'user attachment, immutable'}]
    for item in previous['inputs']:
        p=WORK/item['workspace_relative_path'];assert sha(p)==item['sha256']
        inputs.append(item)
    copies={
     'dimension_uniform_feedback_20261017.md':WORK/'bgs_focus_20261017/dimension_uniform_feedback.md',
     'prior_self_review_20261017.md':WORK/'bgs_focus_20261017/self_review.md',
     'deep_feedback_gaussian_20261016.md':WORK/'bgs_focus_20261016/deep_feedback_gaussian.md',
     'transmission_spectral_averaging_20261017.md':WORK/'bgs_focus_20261017/transmission_spectral_averaging.md'}
    (ROOT/'inputs').mkdir(exist_ok=True)
    for name,source in copies.items():
        destination=ROOT/'inputs'/name
        if destination.exists():assert destination.read_bytes()==source.read_bytes()
        else:shutil.copyfile(source,destination)
        inputs.append({'workspace_relative_path':str(source.relative_to(WORK)),
                       'archive_copy':str(destination.relative_to(ROOT)),'sha256':sha(source),
                       'role':'previous working input; no new certification of its named project dependencies'})
    write('proof_inputs.json',{'checkpoint':'BGS-REVIEW-20261017','inputs':inputs})

    evidence=[]
    for manifest in sorted(ROOT.glob('*_run/manifest.json')):
        x=json.loads(manifest.read_text());r=json.loads((manifest.parent/'result.json').read_text())
        assert x['run']['exit_status']==0 and r['status']=='passed'
        for item in x['input_artifacts']:
            assert sha(ROOT/item['path'])==item['sha256']==item['sha256_after']
        for item in x['outputs']:assert sha(ROOT/item['path'])==item['sha256']
        evidence.append({'run':str(manifest.parent.relative_to(ROOT)),'claim_id':x['claim_id'],
                         'status':r['status'],'manifest_sha256':sha(manifest),
                         'runtime_seconds':x['run']['runtime_seconds'],'pinned_hashes_current':True})
    assert len(evidence)==7
    write('evidence_summary.json',{'status':'passed','exact_mathematical_runs':evidence,
         'structure_audit':'structure_audit.json','original_numeric_tables_rerun':False,
         'boundary':'Finite controls are not a formal proof of the analytic all-N theorems.'})

    claims=[
      {'id':'REVIEW-CLASSICAL-COMPRESSION-ALL-SIZES-20261017','state':'working_proof_self_reviewed','source':'classical_compression_all_sizes.md','conditional_on_G':False,'boundary':'Classical only; no equality with quantum phase average.'},
      {'id':'REVIEW-LINEAR-K-WINDOW-20261017','state':'existing_result_reconstructed_and_consolidated','source':'positive_clock_and_moment_window.md','conditional_on_G':False,'boundary':'Already in attachment lines 1202--1266; no priority claim.'},
      {'id':'REVIEW-FIXED-CHANNEL-TV-COMPACTNESS-20261017','state':'conditional_working_proof_self_reviewed','source':'fixed_channel_total_variation_compactness.md','conditional_on_G':True,'boundary':'Full G for arbitrary diverging u=o(N), or stated rank condition R; no Haar identification.'},
      {'id':'REVIEW-POSITIVE-BERNSTEIN-PATH-LAW-20261017','state':'working_proof_self_reviewed','source':'positive_bernstein_path_law.md','conditional_on_G':False,'boundary':'W1 approximation of entire law with finite positive coefficients; their asymptotic masses uncomputed.'},
      {'id':'REVIEW-BETA-SMOOTHED-PATH-LAW-20261017','state':'conditional_working_proof_self_reviewed','source':'positive_bernstein_path_law.md','conditional_on_G':True,'boundary':'TV approximation after specified beta smoothing; no quantitative TV rate and no proof that the density tends to one.'},
      {'id':'REVIEW-TRANSMISSION-APPENDIX-EXACT-20261017','state':'exact_finite_controls_passed','source':'appendix_run/result.json','conditional_on_G':False,'boundary':'S4 mean 23/45 is finite-size only.'},
      {'id':'BGS-TWO-CHANNEL-ORIGINAL-THREE-CONDITIONS','state':'open','source':'review_and_progress.md','boundary':'Even the full-general mean limit is not established.'},
      {'id':'BGS-ALL-CHAOTIC-SYSTEMS','state':'open','source':'review_and_progress.md','boundary':'No reduction from every chaotic Hamiltonian system to the studied phase model has been proved.'}]
    write('research_checkpoint.json',{'date':'2026-10-17','user_request':'Critically review attachment, incorporate useful results and continue the breakthrough search without touching BGS.',
        'repo_integrity':'repo_integrity.json','claims':claims,
        'accepted_attachment_tools':['AP complete escape and quantum Kac','SA source spectral averaging','FM bounded fractional criterion','UC/HS exact controllability and Hardy structure','L2/entropy sufficient transfer criteria','QC coherent occupation coefficients','CE classical complement','MC marked-column/Haar inverse-Wishart benchmark','MR/BG/SG necessary constraints with explicit nonuniqueness boundaries'],
        'proposed_corrections':['CE1--CE6 collisions resolved by CL1--CL17 in late classical appendix','Historical structural counts separated from current 597 tags and 12 code blocks','QC7 tail strengthened from k^2 to existing linear k'],
        'research_branches':[
          {'route':'Classical complement -> quantum equipartition','outcome':'blocked by exact finite interference; classical theorem strengthened independently'},
          {'route':'Full G -> finite-channel regularity','outcome':'TV compactness and marked-clock UI proved conditionally'},
          {'route':'Positive occupation coefficients -> full transmission law','outcome':'finite positive Bernstein approximation with an explicit W1 error'},
          {'route':'TV compactness + beta smoothing','outcome':'conditional positive polynomial-density approximation in TV'},
          {'route':'Regularity/normalization -> Haar identification','outcome':'open; compactness and total clock do not evaluate the positive path density'}],
        'remaining_obligation':'Control coherent occupation-class masses at O(N) internal lengths; under G prove integral_0^1 |h_N(t)-1| dt -> 0, or use the complete bounded fractional-overlap criterion.',
        'unperformed':['No BGS modifications, commit or push.','No new subagents.','No claim of a full Lean formalization.','No rerun of the attachment\u2019s large Monte Carlo tables.','No global priority or prize-level claim.']})
    print(json.dumps({'status':'passed','inventory_sections':len(inventory['sections']),
       'BGS_files_unchanged':len(current),'exact_runs':len(evidence),'open_main_claims':2}))


if __name__=='__main__':main()
