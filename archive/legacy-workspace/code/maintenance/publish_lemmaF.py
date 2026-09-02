"""Append the Lemma F block (run 73.4) to LEDGER.md and THEORY.md.  Idempotent."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BLOCK = r"""
### R73.4 — LEMMA F [PROVEN + certified]: the exact quadratic phase, and the true shape of the barrier

T7 gives only `|Tr(T(v) U^J)| = 1` for `J != 0 mod K`. That modulus-only statement
is the source of the exponential error `C^r/m` in T8 and hence of the whole T18
barrier. It sharpens to an identity.

Write `sigma(m,v) = m_2 v_1 - m_1 v_2`, so `T(m)T(v) = w^{sigma(m,v)/2} T(m+v)`
and `T(m)T(v)T(m)^{-1} = w^{sigma(m,v)} T(v)`; put `B_J = (A^J)^t`.

**Lemma F.** For `J != 0 mod K` let `m(v) = -(B_J^{-1} - I)^{-1} v` (linear in v;
`B_J - I` is invertible). Then

    Tr(T(v) U^J) = Tr(U^J) . w^{Q_J(v)},
    Q_J(v) = sigma(m(v), v) - (1/2) sigma(B_J^{-1} m(v), m(v)),

and `Q_J` is a **homogeneous** quadratic form in v (no linear, no constant term),
with `|Tr(U^J)| = 1`.

*Proof.* Conjugate the trace by `T(m)` and use
`T(m) U^J T(m)^{-1} = w^{-sigma(B_J^{-1}m, m)/2} U^J T((B_J^{-1}-I) m)`; choosing
m with `(B_J^{-1}-I) m = -v` collapses the remaining trace to `Tr(U^J)`. ∎

**Certification** (`src/theorems/lemma_f_quadratic_phase.py`,
`artifacts/r73/lemmaF_quadratic_phase.json`, `artifacts/r73/lemmaF_closed_form.json`):
the quadratic-form structure was *determined* from six samples by linear algebra
over Z/N and then tested out of sample — **5000 checks over 5 (A,N) and J ≤ 5,
zero mismatches**, and every fitted linear and constant coefficient is exactly 0.
The closed form above then reproduces the fitted coefficients under a single
universal sign convention at all 16 triples (A,N,J) tested.

**Corollary (the barrier, named exactly).** The moment error is

    theta_r = (mK)^{-1} sum_{J != 0} lam^{-J} Tr(U^J)
                  . sum_v hat{Vbar^r}(v) w^{Q_J(v)},

with `hat{Vbar^r}` the Weyl coefficient vector of `Vbar^r`. Bounding the inner sum
by its l^1 norm reproduces T8's `C^r/m`. **So the entire obstruction to pushing
the moment method to r ~ log m is cancellation in an explicit theta-like sum
against a homogeneous quadratic phase** — not an abstract "local law". This is the
sharpest formulation of the T18 barrier we can give, and it is where the next
attack belongs: the phases are Gauss-type, the coefficient vector is explicit and
sparse for small r, and the only reason the l^1 bound is still used is that no
structural information about that vector has been exploited.
"""

TH = r"""
### 11.4 Lemma F — the exact quadratic phase (supersedes the modulus-only T7)

For `J != 0 mod K`, with `sigma(m,v) = m_2 v_1 - m_1 v_2`, `B_J = (A^J)^t` and
`m(v) = -(B_J^{-1} - I)^{-1} v`:

    Tr(T(v) U^J) = Tr(U^J) . w^{Q_J(v)},
    Q_J(v) = sigma(m(v), v) - (1/2) sigma(B_J^{-1} m(v), m(v)),

a HOMOGENEOUS quadratic form in v, with `|Tr(U^J)| = 1`. Proof: conjugate by
`T(m)` and choose m with `(B_J^{-1}-I) m = -v`. Certified by determining the form
from six samples over Z/N and testing out of sample: 5000 checks, zero
mismatches, all linear and constant coefficients exactly 0; the closed form
matches at 16 triples (A,N,J) with one universal sign convention.

Consequence: the T8 error term is

    theta_r = (mK)^{-1} sum_{J != 0} lam^{-J} Tr(U^J) sum_v hat{Vbar^r}(v) w^{Q_J(v)},

so the T18 barrier is **exactly** the absence of cancellation in an explicit
theta-like sum against a homogeneous quadratic phase; the `l^1` bound on the inner
sum is what produces `C^r/m`. This is the concrete analytic target replacing
"a local law is needed".
"""


def patch(path, marker, text):
    p = os.path.join(ROOT, path)
    s = open(p, encoding="utf-8", errors="surrogateescape").read()
    if marker in s:
        return f"{path}: already present"
    open(p, "w", encoding="utf-8", errors="surrogateescape").write(
        s.rstrip() + "\n" + text)
    return f"{path}: appended"


print(patch("LEDGER.md", "R73.4 — LEMMA F", BLOCK))
print(patch("THEORY.md", "11.4 Lemma F", TH))
