# Main-branch protection policy

The intended canonical-branch policy is:

- all accepted scientific work ends in `main`;
- theorem/status changes use pull requests;
- force pushes and branch deletion are prohibited;
- the scientific registry audit, structural repository audit, maintained
  verification workflow, Lean build, and manuscript synchronization/build are
  required when GitHub Actions is operational;
- unresolved review objections to theorem/status changes block merge;
- infrastructure non-runs (`runner_id=0`, `steps=[]`) are documented rather
  than relabelled as pass/fail evidence.

The current connector exposes repository-content and PR writes but not GitHub
administration writes for branch-protection/ruleset enforcement. Therefore the
version-controlled target policy is stored in
`.github/main-branch-policy.json`; actual GitHub-side enforcement must be
enabled through an administrative surface when available.

Until then, repository merges follow the same policy procedurally.
