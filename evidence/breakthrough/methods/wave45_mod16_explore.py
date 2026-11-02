import numpy as np
from collections import Counter

def analyze(m, p, chunk=65536):
    Q = 8*m*m
    step0 = Q//(8*p)
    assert Q % (8*p) == 0
    mod = Q//step0  # = 8p
    t_all = np.arange(1, mod, 2, dtype=np.int64)  # t odd
    # build full (t,u) grid: u = 11t mod 16, u < mod (flat arrays, small)
    r_all = (11*t_all) % 16
    us = np.arange(0, mod//16, dtype=np.int64)*16  # offsets
    Tall = np.repeat(t_all, mod//16)
    Uall = (np.tile(us, len(t_all)) + np.repeat(r_all, mod//16)) % mod
    stats = Counter()
    examples = {}
    total = 0
    valid = 0
    for c0 in range(0, len(Tall), chunk):
        T = Tall[c0:c0+chunk]
        U = Uall[c0:c0+chunk]
        n = len(T)
        total += n
        y_prev = (step0*T) % Q
        y_curr = (step0*U) % Q
        W = np.zeros((p//4, n), dtype=np.int64)
        snap = {}
        # y_prev=y_0, y_curr=y_1; record w_k = y_{2k+1} for k < p/4,
        # and snapshots y_{p/2}, y_{p/2+1}, y_p, y_{p+1}
        W[0] = y_curr
        for nn in range(1, p+1):
            y_next = (6*y_curr - y_prev) % Q
            y_prev, y_curr = y_curr, y_next
            # now y_curr = y_{nn+1}
            if nn % 2 == 0 and nn//2 < p//4:
                W[nn//2] = y_curr
            if nn+1 in (p//2, p//2+1, p, p+1):
                snap[nn+1] = y_curr.copy()
        # period | p iff (y_p, y_{p+1}) == (y_0, y_1); minimal p iff not (y_{p/2},y_{p/2+1})==(y_0,y_1)
        y0 = (step0*T) % Q
        y1 = (step0*U) % Q
        per_ok = (snap[p] == y0) & (snap[p+1] == y1)
        min_ok = ~((snap[p//2] == y0) & (snap[p//2+1] == y1))
        nu_ok = ((snap[p//2] - y0) % Q == Q//2) & ((snap[p//2+1] - y1) % Q == 0)
        good = per_ok & min_ok & nu_ok
        valid += int(good.sum())
        stats['npoints'] += n
        stats['valid'] += int(good.sum())
        stats['bad_period'] += int((~per_ok).sum())
        stats['bad_min'] += int((per_ok & ~min_ok).sum())
        stats['bad_nu'] += int((per_ok & min_ok & ~nu_ok).sum())
        if not good.any():
            continue
        Wg = W[:, good]
        ng = Wg.shape[1]
        # quarter indices k < p/8 ; pairs j < p/16
        q = p//8
        # epsilon_k
        diff_e = (Wg[q:2*q] - Wg[0:q]) % Q
        stats['eps_non01'] += int(((diff_e % (Q//2) != 0)).sum())
        eps = diff_e // (Q//2)  # (q, ng)
        # phi_j for j < p/16
        pj = p//16
        diff_p = (Wg[pj:pj+pj] - Wg[0:pj]) % Q  # w_{j+pj} - w_j ; pj = p/16 = 2^{j-4} shift
        stats['phi_nondiv'] += int(((diff_p % (Q//4)) != 0).sum())
        phi = (diff_p // (Q//4)) % 4
        # D_j: shift-8 digit, modulus Q/16 at j=9 ; general: Q/2^{j-5} with j = log2(p)
        jj = int(round(np.log2(p)))
        mu = Q // (2**(jj-5)) if jj >= 6 else None
        diff_d = (Wg[8:8+pj] - Wg[0:pj]) % Q
        stats['D_nondiv'] += int(((diff_d % mu) != 0).sum())
        D = (diff_d // mu) % 16
        v = Wg[0:q] % (Q//2)
        ttop = Wg[0:q] // (Q//2)
        # per-point analysis (loop over points in chunk; ng up to 65536, pj up to 64 -> fine)
        for idx in range(ng):
            eps_i = eps[:, idx]
            phi_i = phi[:, idx]
            reps = [j for j in range(pj) if eps_i[j] == 0 and phi_i[j] == 0]
            stats['reps_%d' % len(reps)] += 1
            if len(reps) != 2**(jj-6):
                if 'badrep' not in examples:
                    examples['badrep'] = (m, p, idx, reps)
                continue
            # spacing check
            diffs = [reps[i+1]-reps[i] for i in range(len(reps)-1)]
            if any(d != 4 for d in diffs):
                stats['rep_spacing_bad'] += 1
                if 'spacing' not in examples:
                    examples['spacing'] = (m, p, reps)
                continue
            D_i = D[:, idx]
            # Op mod 8 along reps
            op8 = [int(D_i[j]) % 8 for j in reps]
            stats['op8_' + str(tuple(op8))] += 1
            # classes: group reps by v_j
            v_i = v[:, idx]
            t_i = ttop[:, idx]
            classes = {}
            for j in reps:
                classes.setdefault(int(v_i[j]), []).append(j)
            sizes = tuple(sorted(len(c) for c in classes.values()))
            stats['classsizes_' + str(sizes)] += 1
            contribs = []
            for c, js in classes.items():
                contrib = sum(2*(1-2*int(t_i[j])) for j in js)
                contribs.append(contrib)
            stats['contribs_' + str(tuple(sorted(contribs)))] += 1
            # for each class: D mod 16 tuple and t tuple in k-order
            for c, js in sorted(classes.items()):
                dtup = tuple(int(D_i[j]) for j in js)
                ttup = tuple(int(t_i[j]) for j in js)
                stats['class_len%d_D%s_t%s' % (len(js), dtup, ttup)] += 1
                if len(js) == 4 and 'size4' not in examples:
                    examples['size4'] = (m, p, js, dtup, ttup, contribs)
    return stats, examples

if __name__ == '__main__':
    import sys
    pairs = [(int(sys.argv[1]), int(sys.argv[2]))] if len(sys.argv) > 2 else [(512, 512)]
    for (m, p) in pairs:
        print('=== m=%d p=%d ===' % (m, p))
        st, ex = analyze(m, p)
        for k in sorted(st):
            if k.startswith('op8_') or k.startswith('class_len'):
                continue
            print(k, st[k])
        print('--- examples ---')
        for k, v in ex.items():
            print(k, v)
        for L in (8, 4, 2):
            print('--- class-size-%d detail (top 20) ---' % L)
            items = [(k, v) for k, v in st.items() if k.startswith('class_len%d_' % L)]
            items.sort(key=lambda kv: -kv[1])
            for k, v in items[:20]:
                print(k, v)
