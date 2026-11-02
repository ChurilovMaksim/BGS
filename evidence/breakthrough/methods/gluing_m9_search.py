"""m=9 gluing search, component level, product representation.
Global y = (v4, v49, v39601) with v_q in Fix mod q. v4 is constant, hence
irrelevant to multiset/affine questions, so pairs (v49, v39601) are searched.
For a vector v mod q, A(v) = {p.v : p in Aff, p.v in Fix mod q}.
A candidate y' is built as (w49, w39601), w_q in A(v_q); it is a gluing
counterexample iff sorted pairs of y' == sorted pairs of y (CRT multiset
equality, since CRT is a per-coordinate bijection) and y' is not globally
affine-equivalent to y (different affine canonical form).
Search modes: --random N (seeded), --period3 (all v39601 of period 3),
--asize9 (all v39601 with |A|=9), --all49 (subset interface, not used for
full enumeration).
"""
import sys, random, json, argparse
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/methods')
from gluing_components import fix_mod, aff_perms

m = 9
perms = aff_perms(m)

def A_list(v, fixset):
    out = []
    seen = set()
    for a, b in perms:
        w = tuple(v[(a*j + b) % m] for j in range(m))
        if w in fixset and w not in seen:
            seen.add(w); out.append(w)
    return out

def canon_pairs(pairs):
    # pairs: tuple of 9 pairs; canon = lex min over affine perms of permuted pair-tuple
    best = None
    for a, b in perms:
        t = tuple(pairs[(a*j + b) % m] for j in range(m))
        if best is None or t < best: best = t
    return best

def search_pair(v49, v39601, A49, A39601):
    base = tuple(zip(v49, v39601))
    base_sorted = tuple(sorted(base))
    base_canon = canon_pairs(base)
    for w49 in A49:
        for w39601 in A39601:
            cand = tuple(zip(w49, w39601))
            if tuple(sorted(cand)) != base_sorted: continue
            if canon_pairs(cand) == base_canon: continue
            return {"v49": v49, "v39601": v39601, "w49": w49, "w39601": w39601,
                    "cand": cand, "base": base}
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", required=True)
    ap.add_argument("--n", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    vec49 = fix_mod(m, 49); set49 = set(vec49)
    vec39601 = fix_mod(m, 39601); set39601 = set(vec39601)
    A49 = {v: A_list(v, set49) for v in vec49}
    A39601 = {v: A_list(v, set39601) for v in vec39601}
    if args.mode == "period3":
        targets = [v for v in vec39601 if all(v[j] == v[j % 3] for j in range(m))]
    elif args.mode == "asize9":
        targets = [v for v in vec39601 if len(A39601[v]) == 9]
    elif args.mode == "random":
        rng = random.Random(args.seed)
        targets = [rng.choice(vec39601) for _ in range(args.n)]
    else:
        raise SystemExit("unknown mode")
    print(f"mode={args.mode} targets={len(targets)}")
    tested = 0; combos = 0; hits = []
    if args.mode == "random":
        rng = random.Random(args.seed + 1)
        pairs = [(rng.choice(vec49), t) for t in targets]
    else:
        pairs = [(v49, t) for t in targets for v49 in vec49]
    for v49, v39601 in pairs:
        tested += 1
        combos += len(A49[v49]) * len(A39601[v39601])
        hit = search_pair(v49, v39601, A49[v49], A39601[v39601])
        if hit:
            hits.append(hit); print("HIT", hit); break
    print(f"tested_pairs={tested} combos={combos} hits={len(hits)}")
    json.dump({"mode": args.mode, "tested": tested, "combos": combos,
               "hits": hits}, open(f"/home/hatch/workspace/bgs-breakthrough/methods/gluing_m9_{args.mode}.json", "w"), indent=1)

if __name__ == "__main__":
    main()
