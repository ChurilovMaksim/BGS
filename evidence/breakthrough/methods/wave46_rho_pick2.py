import pickle, json
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    for _ in range(n): r = mul(r, a, M)
    return r
AP8 = [pw(ALPHA, i, 8192) for i in range(32)]
AP17 = [pw(ALPHA, i, 17) for i in range(32)]
def seq_fast(B, AP, M):
    return tuple((2*((B[0]*a[0]+2*B[1]*a[1]) % M)) % M for a in AP)
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1,-1) for b in range(4)]
data = pickle.load(open("wave46_rho_groups.pkl", "rb"))
groups = data["groups"]
# Phase 1: score mixed members (cheap)
scored = []
for glob, mem in groups.items():
    if len(mem) < 2: continue
    for (B2, Bq, mf) in mem:
        if not mf: continue
        p = seq_fast(B2, AP8, 8192); a = seq_fast(Bq, AP17, 17)
        pd, ad = len(set(p)), len(set(a))
        scored.append((min(pd, ad), pd, ad, B2, Bq, glob))
scored.sort(reverse=True)
print("top scores:", [(s[0], s[1], s[2], s[3], s[4]) for s in scored[:10]], flush=True)
# Phase 2: partners only for top 12 distinct (B2,Bq)
seen = set(); cands = []
for (score, pd, ad, B2, Bq, glob) in scored:
    if (B2, Bq) in seen: continue
    seen.add((B2, Bq))
    mem = groups[glob]
    p = seq_fast(B2, AP8, 8192); a = seq_fast(Bq, AP17, 17)
    J = joints(p, a)
    psets = []
    for (B2b, Bqb, _) in mem:
        if (B2b, Bqb) == (B2, Bq): continue
        pb = seq_fast(B2b, AP8, 8192); ab = seq_fast(Bqb, AP17, 17)
        Jb = joints(pb, ab)
        pis = [pi for pi in perms if all(Jb[r] == J[pi[r]] for r in range(4))]
        psets.append(((B2b, Bqb), pis))
    has_single_nonid = any(len(pis) == 1 and pis[0] != (0,1,2,3) for _, pis in psets)
    has_nonid = any(any(pi != (0,1,2,3) for pi in pis) for _, pis in psets)
    cands.append({"A": [B2, Bq], "pd": pd, "ad": ad, "nmem": len(mem),
                  "single_nonid": has_single_nonid, "nonid": has_nonid,
                  "partners": [[[x[0][0], x[0][1]], x[1]] for x in psets[:6]]})
    print("CAND:", B2, Bq, "pd:", pd, "ad:", ad, "nmem:", len(mem),
          "single_nonid:", has_single_nonid, "nonid:", has_nonid, flush=True)
    print("   partners:", cands[-1]["partners"][:3], flush=True)
    if len(cands) >= 12: break
json.dump(cands, open("wave46_rho_best.json", "w"))
print("saved wave46_rho_best.json")
