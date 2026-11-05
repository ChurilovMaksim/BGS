#!/usr/bin/env python3
"""Lemma S check at the first omega(h_p)=3 prime p=37 (BGS-TRACE-352 extension) [CA].

h_37 = 223 * 37223 * 8761009 ≈ 7.272e13. Exhaustive enumeration of all residue classes is
infeasible. This script:
  * finds every line (8 = 2^3) via CRT choices of sqrt(2) mod each prime factor (flint/sympy);
  * on each cross line, samples N_OUT classes outside the axis sub-line and N_AXIS axis classes;
  * computes a height representative by Lagrange CVP for a^2+2b^2 plus a local polish, with full
    b-exhaust certification whenever G/√2 <= FULL_CERT_LIMIT;
  * checks (G1+G2)^2 >= d_sigma by the exact integer test on A+|a|, B=|b|:
        u = A^2 + 2 B^2 - D, v = 2 A B; holds iff u >= 0 or u^2 <= 2 v^2
    (i.e. (A + B √2)^2 >= D in Q(√2)), and requires a 25% float margin when the pair is not
    fully certified.
Output ../logs/lemmaS_exact_p37.json. Usage: python code/lemmaS_exact_p37.py
"""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import itertools, json, math, pathlib, random, time
from sympy import factorint, sqrt_mod

OUT = pathlib.Path(__file__).resolve().parents[1] / "logs" / "lemmaS_exact_p37.json"
P = 37
N_OUT = 1000
N_AXIS = 500
FULL_CERT_LIMIT = 8000
MARGIN = 1.25
SEED = 0


def h_of(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = a + 2 * b, a + b
    return a


def height_fast(x, r, h, full_cert_limit=FULL_CERT_LIMIT):
    S2 = math.sqrt(2.0)
    x %= h; r %= h
    t = int(x)
    a0 = t if t <= h - t else t - h
    bestG, besta, bestb = float(abs(a0)), a0, 0

    def Q(a, b): return a * a + 2 * b * b
    def Bil(a, b, c, d): return a * c + 2 * b * d

    b1a, b1b = h, 0
    b2a, b2b = -int(r), 1
    for _ in range(64):
        if Q(b2a, b2b) < Q(b1a, b1b):
            b1a, b1b, b2a, b2b = b2a, b2b, b1a, b1b
        denom = Q(b1a, b1b)
        if denom == 0:
            break
        m = int(round(Bil(b2a, b2b, b1a, b1b) / denom))
        b2a, b2b = b2a - m * b1a, b2b - m * b1b
        if Q(b2a, b2b) >= Q(b1a, b1b):
            break
    det = b1a * b2b - b2a * b1b
    if det:
        y1 = ((-x) * b2b) / det
        y2 = (x * b1b) / det
        for e1 in range(-4, 5):
            for e2 in range(-4, 5):
                bb = (int(round(y1)) + e1) * b1b + (int(round(y2)) + e2) * b2b
                t = (x - (bb % h) * r) % h
                a = t if t <= h - t else t - h
                G = abs(a) + S2 * abs(bb)
                if G < bestG:
                    bestG, besta, bestb = G, a, bb
    for db in range(-256, 257):
        bb = bestb + db
        t = (x - (bb % h) * r) % h
        a = t if t <= h - t else t - h
        G = abs(a) + S2 * abs(bb)
        if G < bestG:
            bestG, besta, bestb = G, a, bb
    certified = False
    max_b = int(bestG / S2) + 1
    if max_b <= full_cert_limit:
        for bb in range(1, max_b + 1):
            for sb in (bb, -bb):
                t = (x - (sb % h) * r) % h
                a = t if t <= h - t else t - h
                G = abs(a) + S2 * abs(sb)
                if G < bestG - 1e-15:
                    bestG, besta, bestb = G, a, sb
                    max_b = int(bestG / S2) + 1
        certified = True
    assert (besta + bestb * r - x) % h == 0
    return bestG, besta, bestb, certified


def exact_ge(a1, b1, a2, b2, D):
    A = abs(a1) + abs(a2)
    B = abs(b1) + abs(b2)
    u = A * A + 2 * B * B - D
    v = 2 * A * B
    return u >= 0 or u * u <= 2 * v * v


def main():
    random.seed(SEED)
    h = h_of(P)
    fac = factorint(h)
    qs = sorted(fac)
    assert all(v == 1 for v in fac.values()) and len(qs) >= 3
    results = []
    t_all = time.time()
    for ch in itertools.product(*[[int(sqrt_mod(2, q)), q - int(sqrt_mod(2, q))] for q in qs]):
        r, M = 0, 1
        for q, rq in zip(qs, ch):
            r = r + M * (((rq - r) * pow(M, -1, q)) % q)
            M *= q
        assert (r * r - 2) % h == 0
        e = pow(1 + r, P, h)
        sig = [1 if e % q == 1 else (-1 if e % q == q - 1 else 0) for q in qs]
        assert 0 not in sig
        dp = math.prod(q for q, s in zip(qs, sig) if s == 1)
        dm = h // dp
        kind = "binet" if min(dp, dm) == 1 else "cross"
        row = dict(p=P, signs=sig, dplus=dp, dminus=dm, kind=kind)
        t0 = time.time()
        if kind == "binet":
            G, a, b, c = height_fast(1, r, h)
            assert abs(G - 1.0) < 1e-9 and c
            row.update(Q_at_1=G, certified=c, secs=time.time() - t0)
            results.append(row)
            print(json.dumps(row), flush=True)
            continue
        dsig, dother = (dp, dm) if dp >= dm else (dm, dp)
        ok = fail = cok = 0
        min_ratio = float("inf")
        seen = set()
        while ok + fail < N_OUT:
            x = random.randrange(1, h)
            if x % dother == 0 or x in seen:
                continue
            seen.add(x)
            G1, a1, b1, c1 = height_fast(x, r, h)
            G2, a2, b2, c2 = height_fast((x * e) % h, r, h)
            if c1 and c2:
                cok += 1
            good = exact_ge(a1, b1, a2, b2, dsig)
            need = 1.0 if (c1 and c2) else MARGIN
            marg = (G1 + G2) ** 2 >= dsig * need
            ratio = (G1 + G2) / math.sqrt(dsig)
            min_ratio = min(min_ratio, ratio)
            if good and marg:
                ok += 1
            else:
                fail += 1
                print("FAIL", x, G1, G2, dsig, good, marg, c1, c2, flush=True)
        aok = afail = 0
        amin = float("inf")
        for k in range(1, N_AXIS + 1):
            x = (k * dother) % h
            if x == 0:
                continue
            G1, a1, b1, c1 = height_fast(x, r, h)
            G2, a2, b2, c2 = height_fast((x * e) % h, r, h)
            Dm = min(dp, dm)
            A, B = abs(a1), abs(b1)
            u = A * A + 2 * B * B - Dm
            v = 2 * A * B
            ge = u >= 0 or u * u <= 2 * v * v
            if not c1:
                ge = ge and (G1 * G1 >= Dm * MARGIN)
            sym = abs(G1 - G2) <= 1e-5 * max(1.0, G1)
            if ge and sym:
                aok += 1
                amin = min(amin, G1)
            else:
                afail += 1
                print("AXIS FAIL", x, G1, G2, ge, sym, flush=True)
        assert fail == 0 and afail == 0
        row.update(d_sigma=dsig, d_other=dother, out_ok=ok, out_fail=fail, min_ratio=min_ratio,
                   fully_certified_pairs=cok, axis_ok=aok, axis_fail=afail, axis_minG=amin,
                   sqrt_min=math.sqrt(min(dp, dm)), secs=time.time() - t0)
        results.append(row)
        print(json.dumps(row), flush=True)

    meta = dict(
        p=P, h=h, omega=len(qs), factors={str(k): v for k, v in fac.items()},
        method=("Lagrange CVP + local polish; full b-exhaust when G/√2<=%d; "
                "exact integer (A+B√2)^2>=D; %.0f%% margin when not fully certified; "
                "exhaustive over all h classes infeasible") % (FULL_CERT_LIMIT, (MARGIN - 1) * 100),
        N_OUT=N_OUT, N_AXIS=N_AXIS, FULL_CERT_LIMIT=FULL_CERT_LIMIT, MARGIN=MARGIN,
        rows=results, total_secs=time.time() - t_all,
        total_fails=sum(r.get("out_fail", 0) + r.get("axis_fail", 0) for r in results),
    )
    assert meta["total_fails"] == 0
    OUT.write_text(json.dumps(meta, indent=1) + "\n")
    print("WROTE", OUT, "fails", meta["total_fails"], "secs", meta["total_secs"])


if __name__ == "__main__":
    main()
