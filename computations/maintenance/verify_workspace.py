#!/usr/bin/env python3
"""Execute maintained Python/C++ verifiers with source and log hashes.

Execution coverage is not a proof audit. Generated evidence stays below --logs.
Both certificate replays run after their respective producers have completed.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[2]

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build',type=Path,required=True)
    parser.add_argument('--logs',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--workers',type=int,default=2)
    parser.add_argument('--only',action='append',default=[],
                        help='Run only named checks; repeat for a focused verification group.')
    args=parser.parse_args()
    if args.workers<1:parser.error('--workers must be positive')
    args.build=args.build.resolve();args.logs=args.logs.resolve();args.output=args.output.resolve()
    args.logs.mkdir(parents=True,exist_ok=True)
    resonance_certificate=args.logs/'resonance_nondegeneracy_radius8.json'
    extremal_replay=args.logs/'extremal.replay'
    deferred_checker=None
    extremal_producer=False
    items=[]
    temporal={'temporal_soft_modes','temporal_quantum_variance','spectral_module_regression',
              'general_symbol_covariance','quantum_cyclic_module','quantum_phase_completion',
              'cayley_scaling_rigidity'}
    return_checks={'return_local_limits','return_trace_obstruction','analytic_kick_return_gas','even_period_spin_resonance',
                   'fixed_harmonic_return_gas','general_cat_return_laws',
                   'hyperbolic_return_pressure','pell_resonance_lattice',
                   'periodic_point_trace_comparison','phase_space_return_gas'}
    for p in sorted((ROOT/'computations/verification').glob('*.py')):
        if '__main__' not in p.read_text(encoding='utf-8'):continue
        if p.stem=='check_resonance_certificate':
            deferred_checker=p
            continue
        cmd=[sys.executable,str(p)]
        if p.stem=='pell_floquet_regression':
            cmd+=['--cpp',str(args.build/'pell_pair_orthogonality')]
        elif p.stem=='pell_pair_obstruction':
            cmd+=['--output',str(args.logs/'pell_pair_obstruction.json')]
        elif p.stem=='resonance_nondegeneracy_certificate':
            cmd+=['--radius','8','--output',str(resonance_certificate)]
        elif p.stem=='resonance_hessian_obstruction':
            cmd+=['--output',str(args.logs/'resonance_hessian_obstruction.json')]
        elif p.stem=='resonance_quantum_variance':
            cmd+=['--output',str(args.logs/'resonance_quantum_variance.json')]
        elif p.stem=='extremal_resonance':
            extremal_producer=True
            cmd+=['--cases','1000','--max-lag','10','--algebra-cases','20',
                  '--output',str(args.logs/'extremal.json'),'--replay',str(extremal_replay)]
        elif p.stem in return_checks:
            cmd+=['--output',str(args.logs/(p.stem+'.json'))]
        elif p.stem in temporal:
            cmd+=['--output',str(args.logs/(p.stem+'.json'))]
            if p.stem in {'quantum_cyclic_module','cayley_scaling_rigidity'}:
                cmd+=['--prime-limit','251']
            elif p.stem=='quantum_phase_completion':cmd+=['--prime-limit','131']
        items.append((p.stem,cmd,p))
    p=ROOT/'computations/analysis/spectral_diagnostics.py'
    items.append(('spectral_diagnostics_verify',[sys.executable,str(p),'verify'],p))
    for p in sorted((ROOT/'computations/cpp').glob('*.cpp')):
        cmd=[str(args.build/p.stem)]
        if p.stem=='cat_map_order':cmd+=['verify']
        items.append(('cpp_'+p.stem,cmd,p))
    if args.only:
        missing=set(args.only)-{item[0] for item in items}
        if missing:parser.error('Unknown checks: '+', '.join(sorted(missing)))
        items=[item for item in items if item[0] in args.only]
        # The complete run below owns the dependent certificate replays.
        if any(item[0] in {'resonance_nondegeneracy_certificate','extremal_resonance'}
               for item in items):
            parser.error('Dependent certificate producers require a complete run.')
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MPLBACKEND='Agg')
    def check(item):
        name,cmd,source=item;start=time.monotonic();log=args.logs/(name+'.log')
        source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
        with log.open('w') as stream:
            try:
                code=subprocess.run(cmd,cwd=ROOT,env=env,stdout=stream,
                                    stderr=subprocess.STDOUT,timeout=360).returncode
            except subprocess.TimeoutExpired:code=124
            except OSError as exc:
                stream.write(str(exc)+'\n');code=127
        unchanged=source_hash==hashlib.sha256(source.read_bytes()).hexdigest()
        if not unchanged:code=125
        row={'name':name,'source':str(source.relative_to(ROOT)),'sha256':source_hash,
             'source_unchanged':unchanged,'command':cmd,'exit_code':code,
             'seconds':round(time.monotonic()-start,3),
             'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest()}
        print(name,code,flush=True)
        if code:print(log.read_text(errors='replace')[-4000:],flush=True)
        return row
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        rows=list(pool.map(check,items))
    if not args.only and (deferred_checker is None or not extremal_producer):
        raise SystemExit('A required certificate producer/checker is missing.')
    if not args.only:
        cmd=[sys.executable,str(deferred_checker),str(resonance_certificate),
             '--output',str(args.logs/'resonance_certificate_replay.json')]
        rows.append(check(('check_resonance_certificate',cmd,deferred_checker)))
        source=ROOT/'computations/cpp/extremal_resonance_replay.cpp'
        rows.append(check(('extremal_independent_replay',
                           [str(args.build/'extremal_resonance_replay'),str(extremal_replay)],source)))
    data={'producer':'computations/maintenance/verify_workspace.py',
          'scope':'Executable Python/C++ coverage with sequential certificate replays; not a complete proof audit. Lean and TeX are separate.',
          'input_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
          'python':platform.python_version(),'checks':rows,
          'selection':args.only or 'complete Python/C++ surface',
          'passed':sum(r['exit_code']==0 for r in rows),'total':len(rows),
          'repository_mutation_policy':'Generated verifier outputs stay below --logs; committed evidence is not rewritten.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    if data['passed']!=data['total']:raise SystemExit('Verification failed; inspect saved logs.')

if __name__=='__main__':main()
