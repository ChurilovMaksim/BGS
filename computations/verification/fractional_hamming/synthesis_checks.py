"""Portable exact bounded replay; scientific logic retained from frozen source.
Every former assert is an explicit conditional raise and survives python -O.
Imports and the no-argument main are silent and do not write files.
"""
from pathlib import Path
import itertools as it, json

def run_checks():
    rows = []
    for N in [2, 3]:
        for m in range(1, 5):
            counts = {}
            words = list(it.product(range(N), repeat=m))
            for x in words:
                for y in words:
                    c = tuple(((b - a) % N for a, b in zip(x, y)))
                    ham = sum((a != b for a, b in zip(x, y)))
                    support = sum((a != 0 for a in c))
                    switches = sum((c[j] != c[(j + 1) % m] for j in range(m)))
                    checksum = sum(c) % N
                    off = any((x.count(a) != y.count(a) for a in range(N)))
                    if not ham == support:
                        raise AssertionError('Exact check failed at original line 14')
                    if not (not checksum or off):
                        raise AssertionError('Exact check failed at original line 14')
                    xr = x[1:] + x[:1]
                    yr = y[1:] + y[:1]
                    cr = c[1:] + c[:1]
                    if not sum((a != b for a, b in zip(xr, yr))) == ham:
                        raise AssertionError('Exact check failed at original line 16')
                    if not sum((cr[j] != cr[(j + 1) % m] for j in range(m))) == switches:
                        raise AssertionError('Exact check failed at original line 17')
                    if not sum(cr) % N == checksum:
                        raise AssertionError('Exact check failed at original line 18')
                    for r in range(m + 1):
                        for R in range(m + 1):
                            first = off and ham <= r
                            second = switches <= R and checksum != 0 and (ham > r)
                            if not not (first and second):
                                raise AssertionError('Exact check failed at original line 22')
                            if not (not second or off):
                                raise AssertionError('Exact check failed at original line 22')
                            key = (r, R)
                            v = counts.setdefault(key, [0, 0, 0])
                            v[0] += first
                            v[1] += second
                            v[2] += first or second
            for (r, R), v in sorted(counts.items()):
                if not v[0] + v[1] == v[2]:
                    raise AssertionError('Exact check failed at original line 25')
                rows.append({'N': N, 'm': m, 'hamming_radius': r, 'switch_radius': R, 'offcharge_low_hamming': v[0], 'nonzero_checksum_low_switch_high_hamming': v[1], 'disjoint_union': v[2]})
    return {'arithmetic': 'exact integers', 'pair_families': [[N, m, N ** (2 * m)] for N in [2, 3] for m in range(1, 5)], 'all_radii': True, 'mask_cases': rows}


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--inject-failure', action='store_true')
    args = parser.parse_args(argv)
    if args.inject_failure:
        raise AssertionError('Deliberate portability failure control')
    if args.output is not None:
        result = run_checks()
        args.output.write_text(json.dumps(result, indent=2, default=str) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
