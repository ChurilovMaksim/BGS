"""Portable integer format for the separately implemented C++ verifier."""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import json
from pathlib import Path
from exact_coefficients import frozen_coefficients

folder = Path(__file__).resolve().parent
coeff = frozen_coefficients()
certs = json.loads((folder/'certificates.json').read_text())['certificates']
lines = [f'{len(coeff)} 4000']
for (a, b), (re, im) in sorted(coeff.items()):
    assert (4000*re).denominator == (4000*im).denominator == 1
    lines.append(f'{a} {b} {int(4000*re)} {int(4000*im)}')
lines.append(str(len(certs)))
for c in certs:
    lines.append(' '.join(str(c[k]) if k != 'ordinary_midpoint' else str(int(c[k]))
                          for k in ('N', 'p', 'period', 'ordinary_midpoint', 'weight',
                                    'zeta_N', 'image_of_i')))
    for key in ('u', 'v', 'recurrence_descending'):
        lines.append(' '.join(map(str, c[key])))
(folder/'certificates.txt').write_text('\n'.join(lines)+'\n')
