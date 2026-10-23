"""Exact cycle-core enumeration; mathematical scope is in core_contract.json."""
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


def cycles(n):
    for rest in itertools.permutations(range(1, n)):
        word = (0,) + rest
        tau = [0] * n
        for i, vertex in enumerate(word):
            tau[vertex] = word[(i + 1) % n]
        yield tuple(tau)


def difference(tau):
    n = len(tau)
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        j = (i + 1) % n
        a[i][j] += 1
        a[j][i] -= 1
        j = tau[i]
        a[i][j] -= 1
        a[j][i] += 1
    return a


def support(a, p):
    return tuple(i for i, row in enumerate(a) if any(x % p for x in row))


def is_rank_two(a, p):
    active = support(a, p)
    if not active:
        return False
    i = active[0]
    j = next(j for j in active if a[i][j] % p)
    pivot = a[i][j]
    # The rank-two completion from the invertible principal 2x2 pivot.
    return all((pivot * a[k][l] - a[k][j] * a[i][l]
                + a[k][i] * a[j][l]) % p == 0
               for k in active for l in active)


def collapse_is_zero(a, i, j, p):
    kept = [v for v in range(len(a)) if v != j]
    for u in kept:
        for v in kept:
            value = a[u][v]
            if u == i:
                value += a[j][v]
            if v == i:
                value += a[u][j]
            if u == i and v == i:
                value += a[j][j]
            if value % p:
                return False
    return True


def pair_count(a, p):
    active = support(a, p)
    return sum(collapse_is_zero(a, i, j, p)
               for i, j in itertools.combinations(active, 2))


def direct(n, p, keep_cores=False):
    n2 = d2 = visited = 0
    cores = Counter()
    witnesses = {}
    for tau in cycles(n):
        visited += 1
        a = difference(tau)
        active = support(a, p)
        if len(active) > 8 or not is_rank_two(a, p):
            continue
        collapsed = pair_count(a, p)
        n2 += 1
        d2 += collapsed
        if keep_cores and len(active) == n:
            common = sum(tau[i] == (i + 1) % n for i in range(n))
            key = (n, common, collapsed)
            cores[key] += 1
            witnesses.setdefault(key, tau)
    assert visited == math.factorial(n - 1)
    coefficient = F(n2) - F(math.comb(n, 2) + d2, 2)
    return {"m":n, "p":p, "visited":visited, "rank_two":n2,
            "collapse_pairs_sum":d2, "normalized_first_correction":str(coefficient)}, cores, witnesses


def embed(cores, m):
    count = F(0)
    collapsed = F(0)
    for (q, common, d), multiplicity in cores.items():
        if m < q:
            continue
        if common == 0:
            factor = int(m == q)
        else:
            factor = F(m, q) * math.comb(m - q + common - 1, common - 1)
        count += multiplicity * factor
        collapsed += multiplicity * d * factor
    assert count.denominator == collapsed.denominator == 1
    return int(count), int(collapsed), F(count) - F(math.comb(m, 2) + collapsed, 2)


def main(destination):
    tables = {}
    direct_records = []
    core_records = []
    for p in (3, 5, 7, 11, 13):
        table = Counter()
        for q in range(3, 9):
            row, cores, witnesses = direct(q, p, keep_cores=True)
            direct_records.append(row)
            table.update(cores)
            for key, number in sorted(cores.items()):
                core_records.append({"p":p,"q":key[0],"common_edges":key[1],
                                     "collapse_pairs":key[2],"multiplicity":number,
                                     "example_tau":witnesses[key]})
        tables[p] = table
    for p, m in ((3,9),(13,9),(3,10)):
        row, _, _ = direct(m, p)
        direct_records.append(row)
    for row in direct_records:
        n2, d2, a1 = embed(tables[row['p']], row['m'])
        assert n2 == row['rank_two'] and d2 == row['collapse_pairs_sum']
        assert str(a1) == row['normalized_first_correction']
    predictions = []
    for p, table in tables.items():
        for m in range(3,101):
            n2, d2, a1 = embed(table, m)
            if m <= 12 or a1:
                predictions.append({"p":p,"m":m,"rank_two":n2,
                                    "collapse_pairs_sum":d2,"normalized_first_correction":str(a1)})
    result = {"status":"passed","cores":core_records,"direct_enumeration":direct_records,
              "embedding_predictions":predictions,
              "nonzero_first_corrections":[row for row in predictions if F(row['normalized_first_correction'])],
              "open_cores":[row for row in core_records if row['common_edges']>0],
              "scope":"Finite enumeration plus explicit core-embedding formula; any universal claim needs its separate proof"}
    Path(destination).parent.mkdir(parents=True,exist_ok=True)
    Path(destination).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"status":"passed","direct_cycles":sum(r['visited'] for r in direct_records),
                      "core_types":len(core_records),"nonzero_corrections":result['nonzero_first_corrections'],
                      "open_cores":result['open_cores']}))


if __name__=='__main__':
    main(sys.argv[1])
