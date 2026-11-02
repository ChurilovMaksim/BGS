import numpy as np, math
def fix_pts_np(m,q):
    A,B = np.meshgrid(np.arange(q), np.arange(q), indexing='ij')
    a=A.ravel().astype(np.int64); b=B.ravel().astype(np.int64)
    seqs=[a,b]
    for _ in range(m):
        seqs.append((6*seqs[-1]-seqs[-2])%q)
    ok=(seqs[m]==a)&(seqs[m+1]==b)
    return np.stack([s[ok] for s in seqs[:m]],axis=1), np.stack([a[ok],b[ok]],axis=1)

pts,seeds=fix_pts_np(8,512)
for idx in [0,1,2,10,100]:
    v=pts[idx]
    print("seed",seeds[idx].tolist(),"v",v.tolist())
    print("  v/8", (v//8).tolist(), " v mod 32", (v%32).tolist(), " v mod 64", (v%64).tolist())
# For each point, check: does v_i mod 16 determine i mod 4? i.e. is map class -> set of residues disjoint?
# Look at distribution: for each class r, set of v_i mod 32 values
import collections
for idx in range(0,512,64):
    v=pts[idx]
    print(idx, [sorted(set((v[[j for j in range(8) if j%4==r]]%32).tolist())) for r in range(4)])
