#!/usr/bin/env python3
"""Bounded direct circle intersection checks, independent of root enumerator.
All actual upper labels and norm units at h=5,25,125; root multiplicities
through h=625. Tests the claimed classification, not infinite-depth proof.
"""

def main(argv=None):
    import argparse
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args(argv)
    output_dir = args.output_dir.resolve()
    repository = Path(__file__).resolve().parents[3]
    if output_dir == repository or repository in output_dir.parents:
        raise RuntimeError('Use a scratch output directory outside the proof overlay or repository')
    output_dir.mkdir(parents=True, exist_ok=True)
    import os
    import itertools, json, time
    from pathlib import Path
    start = time.monotonic()
    records = []
    modes = [(1, b) for b in [0, 1, -1, 6, -6, 7, -7, 8, -8]]

    def q(v, h):
        return (2 * v[1] ** 2 - v[0] ** 2) % h

    def S(v, h):
        return ((3 * v[0] + 4 * v[1]) % h, (2 * v[0] + 3 * v[1]) % h)
    for l in range(1, 5):
        h = 5 ** l
        L = 6 * 5 ** (l - 1)
        totals = {'two_root': 0, 'no_root': 0, 'singular': 0, 'singular_points': 0}
        direct = 0
        for c in range(1, h):
            if c % 5 == 0:
                continue
            if l <= 3:
                v = next((v for v in itertools.product(range(h), repeat=2) if q(v, h) == c))
                orbit = []
                for k in range(L):
                    orbit.append(v)
                    v = S(v, h)
                index = {v: k for k, v in enumerate(orbit)}
            for u in modes:
                rhs = (1 - 4 * c * pow(q(u, h), -1, h)) * pow(8, -1, h) % h
                roots = [a for a in range(h) if a * a % h == rhs]
                points = [((-u[0] * pow(2, -1, h) + 2 * a * u[1]) % h, (-u[1] * pow(2, -1, h) + a * u[0]) % h) for a in roots]
                if rhs % 5 in [1, 4]:
                    totals['two_root'] += 1
                    if not (len(roots) == 2 and len({a % 5 for a in roots}) == 2):
                        raise AssertionError('Verification failed: len(roots) == 2 and len({a % 5 for a in roots}) == 2')
                elif rhs % 5 in [2, 3]:
                    totals['no_root'] += 1
                    if not not roots:
                        raise AssertionError('Verification failed: not roots')
                else:
                    totals['singular'] += 1
                    totals['singular_points'] += len(points)
                    for y in points:
                        x = ((y[0] + u[0]) % h, (y[1] + u[1]) % h)
                        if not tuple((z % 5 for z in x)) == tuple((-z % 5 for z in y)):
                            raise AssertionError('Verification failed: tuple((z % 5 for z in x)) == tuple((-z % 5 for z in y))')
                if l <= 3:
                    actual = [y for y in orbit if ((y[0] + u[0]) % h, (y[1] + u[1]) % h) in index]
                    if not set(actual) == set(points):
                        raise AssertionError('Verification failed: set(actual) == set(points)')
                    for y in actual:
                        x = ((y[0] + u[0]) % h, (y[1] + u[1]) % h)
                        if rhs % 5 == 0:
                            if not (index[y] - index[x]) % 6 == 3:
                                raise AssertionError('Verification failed: (index[y] - index[x]) % 6 == 3')
                        elif not (index[y] - index[x]) % 6 in [1, 2, 4, 5]:
                            raise AssertionError('Verification failed: (index[y] - index[x]) % 6 in [1, 2, 4, 5]')
                    direct += 1
        records.append({'l': l, 'h': h, 'root_cases': 9 * 4 * h // 5, 'direct_orbit_cases': direct, **totals})
    out = {'status': 'passed', 'records': records, 'elapsed_seconds': time.monotonic() - start}
    (output_dir / (Path(__file__).stem + '.json')).write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))
if __name__ == '__main__':
    main()
