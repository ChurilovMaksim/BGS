#!/usr/bin/env python3
"""Finite global illustration; not a microscopic-law test or proof."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'computations/python'))
from bgs.magnetic_quotient import subgroup,orbit_matrix

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,default=ROOT/'assets');args=ap.parse_args()
    p,K,seed=8009,11,20260905
    assert sp.isprime(p) and (p-1)%K==0
    h=pow(int(sp.primitive_root(p)),(p-1)//K,p);H=subgroup(p,K,h)
    q_values=np.random.default_rng(seed).choice(np.arange(1,p),size=32,replace=False)
    spectra=[np.linalg.eigvalsh(np.sqrt(K/2)*orbit_matrix(p,H,int(q))) for q in q_values]
    eigenvalues=np.concatenate(spectra)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    matplotlib.rcParams['svg.hashsalt']='wow-magnetic-20260905'
    fig,ax=plt.subplots(figsize=(8,4.6))
    ax.hist(eigenvalues,bins=64,density=True,histtype='step',linewidth=1.2,label='Finite magnetic quotient spectra')
    x=np.linspace(-2,2,500)
    ax.plot(x,np.sqrt(np.maximum(0,4-x*x))/(2*np.pi),linewidth=1.5,label='Standard semicircle density')
    ax.set_xlabel('Eigenvalue of X = sqrt(K/2) A');ax.set_ylabel('Density')
    ax.set_title('Global spectrum: p=8009, K=11, dimension 364, 32 q values')
    ax.legend();fig.tight_layout()
    fig.savefig(args.output_dir/'magnetic_quotient_global.svg',metadata={'Date':None})
    fig.savefig(args.output_dir/'magnetic_quotient_global.png',dpi=180)
    plt.close(fig)
    report={'producer':'computations/analysis/magnetic_spectrum_figure.py',
      'scope':'Finite global spectral illustration only. No microscopic universality or IID inference.',
      'p':p,'K':K,'dimension':(p-1)//(2*K),'seed':seed,'q_values':[int(q) for q in q_values],
      'reciprocal_cutoff_through_m6':6<K and p*p>6**(K-1),
      'pooled_moments':{str(m):float(np.mean(eigenvalues**m)) for m in range(1,7)},
      'numpy_version':np.__version__,'sympy_version':sp.__version__,'matplotlib_version':matplotlib.__version__}
    out=ROOT/'evidence/numerical/magnetic_quotient_global.json';out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
