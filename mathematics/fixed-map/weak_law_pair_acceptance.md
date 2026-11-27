# Weak Sine₂ and the second moment: acceptance map

This note separates implications and is not a trace estimate for the
kicked map. Here \(X_N\) is the unfolded circular spectrum translated by
one uniform common origin. The discussion applies to deterministic
spectra with multiplicity and does not require a particular coupling.
For the exact weight \(b_*\), the signed defect \(\Delta_{2,N}(b_*)\),
and the all-order sufficient criterion see the
[standalone problem](../../record/remaining_breakthrough_task_20261021.md).
For the identities with the translation-invariant pair measure
\(\gamma_N\), including the diagonal, see
[the pair-implication proof](archive_continuation/pair_implications/README.md).

## Which inference uses what?

| Input | Valid output | What it does not do |
| --- | --- | --- |
| Full factorial comparison at every fixed order with the prescribed test class | Weak Sine₂ by finite inclusion–exclusion and approximation in the Laplace functional; no separately imposed second-moment bound | A single test or a fixed maximal order does not supply the full criterion. |
| Weak Sine₂ alone | Lower semicontinuity for nonnegative pair tests; a strictly negative fixed pair defect along an infinite subsequence refutes it | A positive second-moment excess need not contradict the weak limit. |
| Weak Sine₂ plus the single exact band-two limit \(\Delta_{2,N}(b_*)\to0\) | All continuous pair tests with summable unit-bin suprema; also uniform integrability of squared local counts, as proved below | No higher factorial orders are asserted. |
| Bounded normalized close-pair count at any one fixed positive radius | Bounded local second moments and a uniform pair-measure bound on each unit bin | Boundedness alone does not imply uniform integrability or convergence. |
| Signed residual for all trajectory pairs outside a fixed above-half overlap class | Gives the pair comparison only if the audited high-overlap and short-time inputs hold and the residual tends to \(-\int_1^2(t-1)w(t)\,dt\) | Estimating that residual by \(o(1)\) gives the wrong answer; there is no extra requirement to take the overlap threshold exactly to one half. |

## A precise equivalent condition, conditional on the weak law

Assume \(X_N\Rightarrow \mathrm{Sine}_2\). Write \(X_N(I)\) for
the local count in a fixed bounded interval \(I\). Then
\[
 \Delta_{2,N}(b_*)\longrightarrow0
 \quad\Longleftrightarrow\quad
 \{X_N(I)^2\}_N\text{ is uniformly integrable for every fixed bounded interval }I.
\]
No moment implication here is claimed without the assumed weak law.

*Forward.* The existing [one-test upgrade](archive_continuation/pair_implications/README.md#2-weak-limit-plus-one-exact-pair-test-gives-every-pair-test)
gives convergence of \(\gamma_N\big((|I|-|\cdot|)_+\big)\) to its
Sine₂ value. Stationarity and the overlap length of two translates of
\(I\) identify this integral with \(\mathbb E X_N(I)^2\), including
the diagonal term. The count itself converges in distribution by the
absence of Sine₂ points at deterministic endpoints. A sequence of
nonnegative random variables converging in distribution to an integrable
limit and whose means converge to its mean is uniformly integrable:
apply convergence to \(y\wedge K\), subtract from the means, and use
\(y\,\mathbf1_{y>2K}\le 2(y-K)_+\). Apply this to the squared counts.

*Reverse.* Let \(g\) be continuous and compactly supported; let \(\rho\)
be continuous, nonnegative, compactly supported and have integral one.
The local double integral with kernel \(\rho(x)g(y-x)\) is a continuous
functional of a point measure in the vague topology. Its modulus is
bounded by a constant times \(X_N(I)^2\) for a fixed sufficiently large
\(I\). Uniform integrability gives convergence of its expectation,
which equals \(\gamma_N(g)\). To pass to \(g_{b_*}=b_* *\widetilde b_*\),
bound the mass of every unit interval uniformly, by stationarity and
Cauchy–Schwarz: \((q*\gamma_N)(t)\le \mathbb E X_N([0,1])^2\)
for \(q(u)=(1-|u|)_+\). On \([-1/2,1/2]\), \(q\ge1/2\).
The same bound holds for the limiting pair measure. Since \(g_{b_*}\)
is Schwartz, the truncation tails are uniformly summable. The
finite CUE pair term converges by the Riemann-sum identity in the
existing pair proof, so the signed comparison follows.

## Why a bounded close-pair count is not enough

On the unfolded \(N\)-point clock of period \(N\), collapse
\(r=\lfloor\sqrt N\rfloor\) consecutive labels onto one of their sites.
For a fixed shifted bounded interval of length \(R\), the chance of
seeing any change is at most \(R(r+1)/N\to0\). Thus this sequence has
the same weak limit as the unmodified clock. The number of ordered
distinct-label pairs at circular distance at most one is still \(O(N)\):
pairs not touching the collapse site number \(O(N)\), the cluster
adds \(r(r-1)\), and at most two remaining neighbors add \(O(r)\).
Nevertheless any compact continuous test supported strictly inside
\((-1,1)\), with value one at zero, gains \(r(r-1)/N\to1\) in the
normalized factorial pair measure. This example illustrates the
integrability gap and is not a counterexample for the maintained map.

## What to test next

For the maintained map the unresolved inputs are the actual negative
low-overlap correction at times proportional to \(N\), or an
independent route to the weak local law or its refutation. The
distribution-free implications above do not establish the required
signed comparison, pair-count bound, or local count tails.
