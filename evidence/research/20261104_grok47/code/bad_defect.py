#!/usr/bin/env python3
"""Defect span - log(|N|/2)/log(eps) among classes whose internal zero-run is < g0.

These are exactly the single-polymer (bad) classes at that g0, model types included.
Complete for |N| < 2^{J+1}. Exact digits; arb enclosures of the defect.
"""
from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

from flint import arb, ctx

ctx.prec = 200
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("span_audit", HERE / "span_audit.py")
sa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sa)

OUT = HERE.parent / "logs" / "bad_defect.json"
logeps = math.log(1 + math.sqrt(2))
eps = 1 + arb(2).sqrt()
log_eps = eps.log()


def max_run(word):
    best = cur = 0
    for x in word:
        if x == 0:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best


def main():
    J = 14
    classes = sa.enumerate_classes(J)
    rows = {}
    witnesses = {"near_hi": None, "near_lo": None}
    for g0 in (4, 6):
        hi = arb("-10")
        lo = arb("10")
        n = 0
        wh = wl = None
        for a, b, Nabs in classes:
            Kl, Kr, _ = sa.support_bounds(a, b)
            E = sa.digits_of(a, b, Kl - 4, Kr + 6)
            span, first, last, word = sa.span_from_E(E)
            if not word:
                continue
            if max_run(word) >= g0:
                continue
            n += 1
            j = Nabs.bit_length() - 1
            d = arb(span) - (arb(Nabs) / 2).log() / log_eps
            if d > hi:
                hi = d
                wh = {"a": a, "b": b, "N": Nabs, "j": j, "span": span, "run": max_run(word), "word": word}
            if d < lo:
                lo = d
                wl = {"a": a, "b": b, "N": Nabs, "j": j, "span": span, "run": max_run(word), "word": word}
        rows[str(g0)] = {
            "n_bad_including_models": n,
            "defect_lower_enclosure_lower": str(lo.lower()),
            "defect_upper_enclosure_upper": str(hi.upper()),
            "witness_hi": wh,
            "witness_lo": wl,
        }
        print("g0", g0, "n", n, "lo", lo.lower(), "hi", hi.upper())
    # sharpness witnesses from the full (not necessarily bad) set, arb-certified
    witnesses_all = []
    for a, b, span, Nabs in ((116, 0, 13, 13456), (0, 82, 11, 13448)):
        d = arb(span) - (arb(Nabs) / 2).log() / log_eps
        # recompute span exactly and check
        Kl, Kr, N2 = sa.support_bounds(a, b)
        assert N2 == Nabs
        E = sa.digits_of(a, b, Kl - 4, Kr + 6)
        sp, _, _, word = sa.span_from_E(E)
        assert sp == span
        witnesses_all.append({
            "a": a, "b": b, "N": Nabs, "span": sp, "word": word,
            "defect_lower": str(d.lower()), "defect_upper": str(d.upper()),
            "run": max_run(word),
        })
    OUT.write_text(json.dumps({"J": J, "by_g0": rows, "sharpness_witnesses": witnesses_all}, indent=1))


if __name__ == "__main__":
    main()
