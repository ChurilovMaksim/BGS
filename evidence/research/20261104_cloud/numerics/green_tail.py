"""Green kernel of the lambda carry and the strict cutoff |e| <= 14.

The recurrence is e_t - 6 e_{t-1} + e_{t-2} = v_t with |v_t| <= 60.
The unique bi-infinite bounded solution is the convolution against

    g_t = - mu^{|t|} / (4 sqrt(2)),   mu = 3 - 2 sqrt(2),

shifted by one index (the stencil produces the delta at the forward site).
||g||_1 = 1/4, so |e| <= 15, and the inequality is strict unless v is the
constant sequence that realises every sign. A finitely supported letter
sequence is not that constant, and an integer strictly inside (-15, 15)
satisfies |e| <= 14.

The tail sum_{|k| > L} |g_k| is geometric with ratio mu. This script
encloses the constants in flint balls. It does not touch the phased
operator.
"""
from __future__ import annotations

import json
import os

from flint import arb, ctx

ctx.prec = 200

LOGS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(LOGS, exist_ok=True)


def ball(x: arb):
    return {"str": str(x), "rad": str(x.rad())}


def main():
    sqrt2 = arb(2).sqrt()
    lam = 3 + 2 * sqrt2
    mu = 3 - 2 * sqrt2
    # identities
    prod = lam * mu
    sm = lam + mu
    diff = lam - mu
    alpha = -1 / (4 * sqrt2)  # signed, so that the even kernel has second difference -1 at the kink site
    # ||g||_1 = |alpha| * (1 + 2 mu / (1-mu))
    l1 = abs(alpha) * (1 + 2 * mu / (1 - mu))
    # closed form 1/4
    quarter = arb(1) / 4
    # geometric tail past lag L: 2 |alpha| mu^{L+1} / (1-mu)
    tails = {}
    for L in range(0, 41):
        tail = 2 * abs(alpha) * (mu ** (L + 1)) / (1 - mu)
        carry = 60 * tail
        tails[str(L)] = {
            "tail_l1": str(tail),
            "times_60": str(carry),
            "below_1": bool(carry < 1),
            "below_1em6": bool(carry < arb("1e-6")),
        }
    # smallest L with 60 * tail < 1 and < 1e-6
    L1 = next(L for L in range(0, 41) if tails[str(L)]["below_1"])
    L6 = next(L for L in range(0, 41) if tails[str(L)]["below_1em6"])
    # mu < 1/5 ?
    out = {
        "lam": ball(lam),
        "mu": ball(mu),
        "lam_mu_minus_1": ball(prod - 1),
        "lam_plus_mu_minus_6": ball(sm - 6),
        "lam_minus_mu_minus_4sqrt2": ball(diff - 4 * sqrt2),
        "alpha": ball(alpha),
        "l1": ball(l1),
        "l1_minus_quarter": ball(l1 - quarter),
        "sixty_l1": ball(60 * l1),
        "sixty_l1_minus_15": ball(60 * l1 - 15),
        "mu_lt_one_fifth": bool(mu < arb(1) / 5),
        "tail_ratio_mu": ball(mu),
        "first_L_60tail_lt_1": L1,
        "first_L_60tail_lt_1e-6": L6,
        "tail_at_L1": tails[str(L1)],
        "tail_at_14": tails["14"],
        "tail_at_30": tails["30"],
        "note": (
            "||g||_1 = 1/4 exactly, so 60||g||_1 = 15. "
            "The tail past lag L is geometric with ratio mu = 3-2*sqrt(2). "
            "Integer carries of a non-constant letter sequence satisfy |e| <= 14."
        ),
    }
    path = os.path.join(LOGS, "green_tail.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print("l1", l1)
    print("l1 - 1/4", l1 - quarter)
    print("60 l1 - 15", 60 * l1 - 15)
    print("mu", mu, "mu<1/5", mu < arb(1) / 5)
    print("first L with 60 tail < 1:", L1, tails[str(L1)]["times_60"])
    print("first L with 60 tail < 1e-6:", L6)
    print("wrote", path)


if __name__ == "__main__":
    main()
