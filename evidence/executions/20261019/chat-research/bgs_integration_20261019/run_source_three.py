import itertools
import json
from fractions import Fraction as F
from pathlib import Path
import subprocess
import sys


def main(target):
    target = Path(target)
    binary = target.parent / 'source_three_prefix'
    p = subprocess.run(['g++', '-O2', '-std=c++20', '-Wall', '-Wextra', 'source_three_prefix.cpp', '-o', str(binary)], capture_output=True, text=True)
    (target.parent / 'compiler_stderr.txt').write_text(p.stderr)
    assert p.returncode == 0, p.stderr
    p = subprocess.run([str(binary.resolve())], capture_output=True, text=True)
    (target.parent / 'engine_stdout.txt').write_text(p.stdout)
    (target.parent / 'engine_stderr.txt').write_text(p.stderr)
    assert p.returncode == 0, p.stderr
    rows = [json.loads(line) for line in p.stdout.splitlines()]
    perms = list(itertools.permutations(range(3)))
    summaries = []
    for prime in (3, 5, 31):
        polys = [dict() for _ in perms]
        for row in rows:
            if row['p'] != prime:
                continue
            for k, count in enumerate(row['boundary_weight24_rotations']):
                if count:
                    polys[k][row['q']] = F(count, 24*3*row['q'])
        central = polys[1] == polys[2] == polys[5] and polys[3] == polys[4]
        summaries.append({'p': prime, 'permutations': perms,
                          'prefix_polynomials': [{str(q):str(a) for q,a in p.items()} for p in polys],
                          'prefix_central': central,
                          'prefix_values_at_one': [str(sum(p.values(), F(0))) for p in polys]})
    fields_equal = all(s['prefix_polynomials'] == summaries[0]['prefix_polynomials'] for s in summaries)
    result = {'status': 'completed_exact_bounded_prefix', 'rows': rows, 'summary': summaries,
              'equal_across_three_tested_fields': fields_equal,
              'scientific_outcome': 'Centrality and prime agreement are observations in q<=9 only; no full source value or universal claim follows.',
              'scope': 'q=3..9, three ports, connected order 3 and defect 3; full support beyond prefix remains uncomputed'}
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status':result['status'], 'equal_fields':fields_equal,
                      'central': [s['prefix_central'] for s in summaries]}))


if __name__ == '__main__':
    main(sys.argv[1])
