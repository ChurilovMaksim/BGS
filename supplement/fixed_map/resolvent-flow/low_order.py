"""Independent quartic-moment check of the first two mixed loop levels."""
import json
from pathlib import Path
import numpy as np
from checks import cot_values, energies, loop_quadrature, frozen_unitary


def run():
    rng = np.random.default_rng(20260921)
    rows = []
    for n in (3, 9, 15):
        spectra = {'clock': 2*np.pi*np.arange(n)/n,
                   'irregular': rng.uniform(-np.pi, np.pi, n),
                   'raw_auxiliary': np.angle(np.linalg.eigvals(frozen_unitary(n, .17)))}
        for name, theta in spectra.items():
            for s in (.6, 1.3, 2.7):
                alpha = np.arange(16384)*2*np.pi/16384
                ss = cot_values(theta, alpha, .5j*s)[0]
                pp = (ss/1j-1)/2
                m2, m4 = np.mean(abs(ss)**2), np.mean(abs(ss)**4)
                q4 = np.mean(abs(pp)**4)
                data = energies(theta, s)
                ell, cc = data['L'], data['C0_real']
                e2 = ell+cc-1/(4*s*s)
                e3 = loop_quadrature(theta, [.5j*s, -.5j*s, -.5j*s])
                errors = [abs(e3-(m4-1-2/s**2*(m2+1))),
                          abs(m4-(1+16*ell+32*cc+16*q4)),
                          abs(q4-((1+1/(2*s*s))*ell-1/(4*s*s)+e3.real/16-2*e2))]
                assert max(errors) < 2e-10
                assert q4+1e-12 >= ell*ell
                polynomial = ell*ell-(1+1/(2*s*s))*ell+1/(4*s*s)
                assert polynomial <= e3.real/16-2*e2+1e-11
                rows.append(dict(N=n, case=name, s=s, L=ell, Q=float(q4),
                    e2=float(e2), e3_real=float(e3.real), e3_imag=float(e3.imag),
                    max_identity_error=float(max(errors))))
    result = dict(status='PASS', rows=rows,
        scope='Finite algebra diagnostics. No vanishing model residual or BGS limit proved.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status':'PASS','cases':len(rows),
                     'maximum_error':max(r['max_identity_error'] for r in rows)}))


if __name__ == '__main__':
    run()
