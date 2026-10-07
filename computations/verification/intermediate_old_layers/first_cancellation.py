"""Bounded reviewed arithmetic. All executable work is inside run(root); outputs stay in scratch. Original assertions are explicit RuntimeError checks, including under python -O. Original __debug__ preconditions are obsolete after this conversion."""

def run(scratch_root):
    __file__ = str(scratch_root / 'replay_coordinate_cancellation.py')
    "No project imports. Edge phases reconstructed from raw coordinate kernel;\nscalar vanishing tested directly modulo Phi_(6m), without factoring a sixth\nroot or using the author's coefficient-balancing implementation or period.\nEVERY wild label is visited at depths 1..5.\n"
    from collections import defaultdict, Counter
    from pathlib import Path
    import json, time, math
    phi = [1, 1, 0, -1, -1, -1, 0, 1, 1]
    remainders = []
    for degree in range(30):
        a = [0] * max(9, degree + 1)
        a[degree] = 1
        for d in range(len(a) - 1, 7, -1):
            q = a[d]
            if q:
                for k in range(9):
                    a[d - 8 + k] -= q * phi[k]
        remainders.append(tuple(((i, c) for i, c in enumerate(a[:8]) if c)))

    def normal(exponents, n):
        step = n // 5
        out = defaultdict(int)
        for e in exponents:
            d, r = divmod(e % (6 * n), step)
            for i, c in remainders[d]:
                out[r + i * step] += c
        return {i: c for i, c in out.items() if c}

    def run(l):
        h = 5 ** l
        n = h * h
        L = 6 * h // 5
        half = pow(2, -1, n)
        eighth = pow(8, -1, n)
        b = -pow(2, -1, h) % h
        roots = defaultdict(list)
        for a in range(h):
            roots[a * a % h].append(a)
        records = []
        summary = Counter()
        for c in range(3, h, 5):
            rs = roots[(pow(2, -1, h) - c) % h]
            if not rs:
                summary['no_intersections_circles'] += 1
                continue
            v = (rs[0], b)
            start = v
            orbit = []
            E = [0]
            for k in range(L):
                orbit.append(v)
                a, d = v
                A = (3 * a + 4 * d) % h
                B = (2 * a + 3 * d) % h
                edge = (-eighth * (3 * A * A - 2 * A * a + 3 * a * a) - half * a * d + half * A * B) % n
                if not edge % h == 0:
                    raise RuntimeError('replay_coordinate_cancellation.py:41: edge % h == 0')
                E.append((E[-1] + edge) % n)
                v = (A, B)
            if not (v == start and len(set(orbit)) == L):
                raise RuntimeError('replay_coordinate_cancellation.py:43: v == start and len(set(orbit)) == L')
            ix = {v: k for k, v in enumerate(orbit)}
            terms = []
            for a in rs:
                ky = ix[a, b]
                B = (b + 1) % h
                kx = ix[a, B]
                translation = (-a + half * a * (B - b)) % n
                terms.append(((translation + E[ky] - E[kx]) % n, kx - ky))
            if not len({d % 6 for _, d in terms}) == 1:
                raise RuntimeError('replay_coordinate_cancellation.py:50: len({d % 6 for _, d in terms}) == 1')
            if not len({ix[a, b] % 3 for a in rs}) == 1:
                raise RuntimeError('replay_coordinate_cancellation.py:51: len({ix[a, b] % 3 for a in rs}) == 1')
            if not len({ix[a, (b + 1) % h] % 3 for a in rs}) == 1:
                raise RuntimeError('replay_coordinate_cancellation.py:52: len({ix[a, (b + 1) % h] % 3 for a in rs}) == 1')
            if not ix[rs[0], b] % 3 == ix[rs[0], (b + 1) % h] % 3:
                raise RuntimeError('replay_coordinate_cancellation.py:53: ix[rs[0], b] % 3 == ix[rs[0], (b + 1) % h] % 3')
            shift = 5 * (E[-1] // h)
            zs = []
            details = []
            for j in range(L):
                alpha = (shift + 5 * h * j) % (6 * n)
                if not (alpha * L - 6 * E[-1]) % (6 * n) == 0:
                    raise RuntimeError('replay_coordinate_cancellation.py:57: (alpha * L - 6 * E[-1]) % (6 * n) == 0')
                exps = [(6 * f + alpha * d) % (6 * n) for f, d in terms]
                zero = not normal(exps, n)
                if zero:
                    zs.append(j)
                if l <= 2:
                    details.append({'j': j, 'exponents': exps, 'remainder': normal(exps, n), 'zero': zero})
            summary['surviving_circles'] += 1
            summary['zero_blocks'] += len(zs)
            summary['simple_rank6_blocks'] += L - len(zs)
            rec = {'c': c, 'D': (pow(2, -1, h) - c) % h, 'roots': rs, 'base': start, 'EL': E[-1], 'L': L, 'zero_labels': zs, 'zero_blocks': len(zs), 'nonzero_blocks': L - len(zs)}
            if l <= 2:
                rec.update(terms=terms, details=details)
            records.append(rec)
        return dict(l=l, h=h, summary=dict(summary), records=records)
    t = time.monotonic()
    data = [run(l) for l in range(1, 6)]
    original = json.loads((scratch_root / 'author/exact_singular_sums.json').read_text())
    for own, old in zip(data, original):
        if not own['summary'] == old['summary']:
            raise RuntimeError("replay_coordinate_cancellation.py:72: own['summary'] == old['summary']")
        for rec in own['records']:
            oldrec = next((r for r in old['records'] if r['c'] == rec['c']))
            period = oldrec['zero_test_label_period']
            if not rec['zero_labels'] == [j for j in range(rec['L']) if j % period in oldrec['zero_label_classes']]:
                raise RuntimeError("replay_coordinate_cancellation.py:75: rec['zero_labels'] == [j for j in range(rec['L']) if j % period in oldrec['zero_label_classes']]")
    r = next((r for r in data[1]['records'] if r['c'] == 13))
    n = 625
    expected = [[(0, 3), (750, 1), (3000, 1)], [(1875, 3), (3375, 1), (4125, 1)], [(0, 1), (750, 2), (3000, 2)], [(1875, 1), (2625, 1), (3375, 1), (4125, 1), (4875, 1)], [(0, 1), (1500, 2), (2250, 2)]]
    for detail, poly in zip(r['details'][:5], expected):
        if not normal(detail['exponents'], n) == normal([e for e, mult in poly for _ in range(mult)], n):
            raise RuntimeError("replay_coordinate_cancellation.py:80: normal(detail['exponents'], n) == normal([e for e, mult in poly for _ in range(mult)], n)")
    out = {'method': 'raw-coordinate phases and direct Phi_(6m) division, no label-period reduction', 'depths': data, 'all_source_counts_and_label_sets_match': True, 'l2_expressions_match': True, 'elapsed_seconds': time.monotonic() - t}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'depths'}))
    print(json.dumps([{'l': r['l'], **r['summary']} for r in data]))
