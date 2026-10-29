"""Deficit-0 classification: ranks of B = A_C - A_H over Q for all Hamiltonian cycles H on [m]
(C = standard cycle), with |C delta H| and Gauss data; lists all rank-2 cases by type."""
import itertools, sys
from collections import Counter
from gauss_exact import diag_Q
def cyc_edges(seq):
    m = len(seq); return frozenset(frozenset((seq[j], seq[(j+1) % m])) for j in range(m))
for m in range(4, int(sys.argv[1])+1):
    C = cyc_edges(list(range(m)))
    seen = set(); cnt = Counter(); r2 = Counter()
    for perm in itertools.permutations(range(1, m)):
        if perm[0] > perm[-1]: continue  # undirected cycles through 0
        seq = (0,)+perm; H = cyc_edges(seq)
        B = [[0]*m for _ in range(m)]
        for e in C:
            a, b = tuple(e); B[a][b] += 1; B[b][a] += 1
        for e in H:
            a, b = tuple(e); B[a][b] -= 1; B[b][a] -= 1
        r, D, bad = diag_Q(B)
        k = len(C - H)
        cnt[(r, k)] += 1
        if r == 2: r2[(k, D)] += 1
    nH = sum(cnt.values())
    print(f'm={m} #H={nH} (r,|C\\H|) counts:', dict(sorted(cnt.items())))
    print(f'   rank-2: (|C\\H|, sqclass of pivot product) -> count', dict(r2),
          f' predicted 2-opt m(m-3)/2={m*(m-3)//2}, swaps m(m-5)/2={max(m*(m-5)//2,0)}')
    sys.stdout.flush()
