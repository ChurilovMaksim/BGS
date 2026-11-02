import numpy as np

# ---------- Part A: Pell valuations / residues (exact integers) ----------
P = [0, 1]
for n in range(2, 8193):
    P.append(6*P[n-1] - P[n-2])
def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2; c += 1
    return c
print('Part A: r, v2(P), e_r mod16, v2(P+1-1), c_r mod16, v2(P-1+1), f_r mod16')
for r in range(3, 13):
    d = 2**r
    e = P[d]//d; c = (P[d+1]-1)//d; f = (P[d-1]+1)//d
    print(r, v2(P[d]), e % 16, v2(P[d+1]-1), c % 16, v2(P[d-1]+1), f % 16)
    assert (P[d] % d == 0 and (P[d+1]-1) % d == 0 and (P[d-1]+1) % d == 0)
    assert (v2(P[d]) == r and v2(P[d+1]-1) == r and v2(P[d-1]+1) == r)
    assert (e % 16 == 3 and c % 16 == 9 and f % 16 == 9)
print('Part A: all valuations/residues exact (e=3, c=9, f=9 mod 16)')

# ---------- Part B: psi-theorem at real points ----------
def run_case(m, p, n_sample, seed, full=False):
    Q = 8*m*m
    step0 = Q//(8*p)
    mod = 8*p
    rng = np.random.default_rng(seed)
    if full:
        t = np.arange(1, mod, 2)
        t = np.repeat(t, mod//16)
        u = (11*np.tile(np.arange(1, mod, 2), mod//16) + 16*np.tile(np.arange(mod//16), mod//2)) % mod
        # rebuild properly: for each odd t, all u = 11t+16k
        ts = np.arange(1, mod, 2)
        t = np.repeat(ts, mod//16)
        u = (11*t + 16*np.tile(np.arange(mod//16), len(ts))) % mod
    else:
        t = rng.choice(np.arange(1, mod, 2), size=n_sample)
        u = (11*t + 16*rng.integers(0, mod//16, size=n_sample)) % mod
    y_prev = (step0*t) % Q
    y_curr = (step0*u) % Q
    W = np.zeros((p//4, len(t)), dtype=np.int64)
    W[0] = y_curr
    snap = {}
    for nn in range(1, p+1):
        y_next = (6*y_curr - y_prev) % Q
        y_prev, y_curr = y_curr, y_next
        if nn % 2 == 0 and nn//2 < p//4:
            W[nn//2] = y_curr
        if nn+1 in (p//2, p//2+1, p, p+1):
            snap[nn+1] = y_curr.copy()
    y0 = (step0*t) % Q; y1 = (step0*u) % Q
    per_ok = (snap[p] == y0) & (snap[p+1] == y1)
    min_ok = ~((snap[p//2] == y0) & (snap[p//2+1] == y1))
    nu_ok = ((snap[p//2] - y0) % Q == Q//2) & ((snap[p//2+1] - y1) % Q == 0)
    good = per_ok & min_ok & nu_ok
    W = W[:, good]; tg = t[good]; ug = u[good]
    q, pj = p//8, p//16
    j = p.bit_length()-1
    # DIV checks: phi well-defined (s=j-4), eps well-defined (s=j-3)
    dphi = (W[pj:2*pj] - W[0:pj]) % Q
    deps = (W[q:2*q] - W[0:q]) % Q
    div_phi = int(((dphi % (Q//4)) != 0).sum())
    div_eps = int(((deps % (Q//2)) != 0).sum())
    eps = (deps//(Q//2)).astype(np.int64)          # k < q
    phi = ((W[pj:pj+q] - W[0:q]) % Q)//(Q//4) % 4  # k < q
    phij = phi[:pj]
    epsj = eps[:pj]
    # eps alternation
    alt_bad = int(((eps[1:] + eps[:-1]) != 1).sum())
    # phi affine mod 4 over k < q
    dd = (phi[1:] - phi[:-1]) % 4
    aff_bad = int((dd != dd[0]).sum())
    # (ii) phi = eps mod 2
    ii_bad = int(((phij % 2) != epsj).sum())
    # (iii) phi_k + phi_{k+pj} = 2 eps_k mod 4
    iii_bad = int((((phij + phi[pj:2*pj]) % 4) != (2*epsj) % 4).sum())
    # psi alternation on parity classes
    psi = ((phi - eps)//2) % 2
    psi_bad = int(((psi[2:] + psi[:-2]) != 1).sum())
    # reps: count and spacing
    reps_bad = 0; reps_count = set()
    for idx in range(W.shape[1]):
        reps = [jj for jj in range(pj) if epsj[jj, idx] == 0 and phij[jj, idx] == 0]
        reps_count.add(len(reps))
        if len(reps) != 2**(j-6) or any(reps[i+1]-reps[i] != 4 for i in range(len(reps)-1)):
            reps_bad += 1
    # pinning algebra (exact ints) on first 200 valid points
    D = 2**(j-2)
    PD = P[D]; PDm1 = P[D-1]
    e2 = PD//2**(j-2); f = (PDm1+1)//2**(j-2)
    pin_bad = 0
    for idx in range(min(200, W.shape[1])):
        tt = int(tg[idx]); uu = int(ug[idx])
        y2 = 6*uu - tt; y3 = 35*uu - 6*tt; y4 = 204*uu - 35*tt
        L0 = e2*y2 - f*uu; L1 = e2*y4 - f*y3
        if L0 % 16 != 0 or L1 % 16 != 0 or (L1 - L0) % 32 != 16:
            pin_bad += 1; continue
        if (L0//16) % 2 != int(eps[0, idx]) or (L1//16) % 2 != int(eps[1, idx]):
            pin_bad += 1
    print(f'(m={m},p={p}) cand={len(t)} valid={int(good.sum())} '
          f'DIVphi={div_phi} DIVeps={div_eps} alt={alt_bad} aff={aff_bad} '
          f'(ii)={ii_bad} (iii)={iii_bad} psi={psi_bad} reps_bad={reps_bad} '
          f'reps_counts={sorted(reps_count)} pin={pin_bad}')
    assert div_phi == 0 and div_eps == 0 and alt_bad == 0 and aff_bad == 0
    assert ii_bad == 0 and iii_bad == 0 and psi_bad == 0 and reps_bad == 0 and pin_bad == 0

run_case(128, 128, 0, 1, full=True)
run_case(256, 256, 4096, 2)
run_case(512, 512, 4096, 3)
run_case(1024, 1024, 2048, 4)
run_case(2048, 1024, 2048, 5)
run_case(2048, 2048, 1024, 6)
print('ALL CHECKS PASS')
