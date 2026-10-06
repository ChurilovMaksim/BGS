#!/usr/bin/env python3
"""Prespecified bandwidth/edge sensitivity on every original finite design.

Float64, seeds and q sets as in spectral_diagnostics.py. Reuses spectra, not
unfolded levels. The nine settings are descriptive, not selected for GOE fit.
No acceptance threshold and no asymptotic claim. At most 168 spectra, n<=336.
"""
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('sd_sensitivity', ROOT/'computations/analysis/spectral_diagnostics.py')
m = importlib.util.module_from_spec(spec); sys.modules[spec.name] = m; spec.loader.exec_module(m)


def spectra(p,k,a,qs):
    context = m.build_sector_context(p,k,a)
    return [np.linalg.eigvalsh(m.hermitian_matrix(context,q)) for q in qs]


def main():
    settings = [(f,e) for f in [.5,1.,2.] for e in [0.,.05,.1]]
    spacing_rows=[]; inversions=[]
    for p,k,a,qs in [(3571,17,2469,list(range(1,200,5))), (19489,29,4523,list(range(1,300,7)))]:
        xs=spectra(p,k,a,qs)
        inversions.append({'design':f'spacing-{p}', 'spectra':len(xs),
                           'legacy_nonmonotone':sum(bool(np.any(np.diff(m.unfold_polynomial(x))<0)) for x in xs)})
        for f,e in settings:
            gaps=np.concatenate([m.normalized_gaps(x,f,e) for x in xs])
            spacing_rows.append({'N':p,'bandwidth_factor':f,'edge_fraction':e,'gap_count':len(gaps),
                'cdf_sup_distance_to_wigner_surmise':m.empirical_cdf_sup_distance(gaps),
                'minimum_unfolded_gap':min(float(np.diff(m.unfold_monotone(x,f,e)).min()) for x in xs)})
    cat=spectra(19489,29,4523,list(range(1,300,12)))
    rng=np.random.default_rng(20260901);goe=[]
    for _ in range(60):
        g=rng.normal(size=(len(cat[0]),len(cat[0])));goe.append(np.linalg.eigvalsh((g+g.T)/2))
    for name,xs in [('window-catmap',cat),('window-GOE',goe)]:
        inversions.append({'design':name,'spectra':len(xs),
            'legacy_nonmonotone':sum(bool(np.any(np.diff(m.unfold_polynomial(x))<0)) for x in xs)})
    window_rows=[];widths=[1,2,3,5,8,12]
    for f,e in settings:
        samples=[[m.forward_window_count_variance(m.unfold_monotone(x,f,e),widths) for x in xs] for xs in [cat,goe]]
        for w in widths:
            c,g=[np.array([r[w] for r in rows]) for rows in samples]
            window_rows.append({'bandwidth_factor':f,'edge_fraction':e,'L':w,
                'catmap_mean':float(c.mean()),'goe_mean':float(g.mean()),**m.descriptive_difference(c,g)})
    print(json.dumps({'contract':'Nine prespecified settings, no chosen winner; finite descriptive sensitivity only. Edge trimming follows full-spectrum KDE fitting; forward windows remain edge-truncated.',
                     'legacy_inversion_counts':inversions,'spacing':spacing_rows,'windows':window_rows},indent=2,allow_nan=False))
if __name__=='__main__':main()
