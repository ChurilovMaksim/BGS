#!/usr/bin/env python3
"""Execute maintained Python/C++ verifiers with source and log hashes.

Execution coverage is not a proof audit. Generated evidence stays below --logs.
Both certificate replays run after their respective producers have completed.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.metadata
import json
import os
import shutil
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[2]

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git_status(*, include_untracked: bool=True) -> list[str]:
    mode='all' if include_untracked else 'no'
    result=subprocess.run(
        ['git','status','--porcelain=v1',f'--untracked-files={mode}'],
        cwd=ROOT,text=True,capture_output=True,check=True)
    return [line for line in result.stdout.splitlines() if line]

def source_manifest() -> dict[str,str]:
    raw=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT)
    rels=[item.decode('utf-8') for item in raw.split(b'\0') if item]
    manifest={}
    for rel in sorted(rels):
        path=ROOT/rel
        if not path.is_file():
            raise RuntimeError(f'Tracked path is not a regular file: {rel}')
        manifest[rel]=sha256(path)
    return manifest

def manifest_digest(manifest: dict[str,str]) -> str:
    payload=json.dumps(manifest,sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(payload).hexdigest()

def command_version(command: str) -> str | None:
    exe=shutil.which(command)
    if not exe:return None
    try:
        output=subprocess.check_output([exe,'--version'],text=True,stderr=subprocess.STDOUT,timeout=10)
    except Exception:
        return None
    return output.splitlines()[0] if output else None

def package_versions() -> dict[str,str | None]:
    out={}
    for name in ('numpy','sympy','mpmath','matplotlib','scipy'):
        try:out[name]=importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:out[name]=None
    return out

def boost_version() -> str | None:
    header=Path('/usr/include/boost/version.hpp')
    if not header.is_file():return None
    for line in header.read_text(encoding='utf-8',errors='replace').splitlines():
        if line.startswith('#define BOOST_LIB_VERSION '):
            return line.split(None,2)[-1].strip('"')
    return None

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build',type=Path,required=True)
    parser.add_argument('--logs',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--workers',type=int,default=2)
    parser.add_argument('--allow-dirty',action='store_true',
                        help='Record but do not reject a dirty initial Git worktree.')
    parser.add_argument('--only',action='append',default=[],
                        help='Run only named checks; repeat for a focused verification group.')
    args=parser.parse_args()
    if args.workers<1:parser.error('--workers must be positive')
    initial_status=git_status(include_untracked=True)
    if initial_status and not args.allow_dirty:
        parser.error('Git worktree is not clean; commit/stash changes or pass --allow-dirty')
    source_manifest_before=source_manifest()
    source_tree_sha256_before=manifest_digest(source_manifest_before)
    toolchain={
        'platform':platform.platform(),
        'python':platform.python_version(),
        'python_executable':sys.executable,
        'packages':package_versions(),
        'git':command_version('git'),
        'cmake':command_version('cmake'),
        'cxx':command_version(os.environ.get('CXX','c++')),
        'boost_lib_version':boost_version(),
        'requirements_sha256':sha256(ROOT/'requirements.txt'),
        'cmake_lists_sha256':sha256(ROOT/'CMakeLists.txt'),
        'verify_workspace_sha256':sha256(Path(__file__).resolve()),
    }
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
                   'hyperbolic_return_pressure','pell_resonance_lattice','pell_harmonic_returns',
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
        elif p.stem=='finite_orbit_resonance':
            cmd+=['--output',str(args.logs/'finite_orbit_resonance.json')]
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
        source_hash=sha256(source)
        with log.open('w') as stream:
            try:
                code=subprocess.run(cmd,cwd=ROOT,env=env,stdout=stream,
                                    stderr=subprocess.STDOUT,timeout=360).returncode
            except subprocess.TimeoutExpired:code=124
            except OSError as exc:
                stream.write(str(exc)+'\n');code=127
        unchanged=source_hash==sha256(source)
        if not unchanged:code=125
        row={'name':name,'source':str(source.relative_to(ROOT)),'sha256':source_hash,
             'source_unchanged':unchanged,'command':cmd,'exit_code':code,
             'seconds':round(time.monotonic()-start,3),
             'log_sha256':sha256(log)}
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
    source_manifest_after=source_manifest()
    source_tree_sha256_after=manifest_digest(source_manifest_after)
    source_tree_unchanged=source_tree_sha256_before==source_tree_sha256_after
    final_status=git_status(include_untracked=True)
    data={'producer':'computations/maintenance/verify_workspace.py',
          'scope':'Executable Python/C++ coverage with sequential certificate replays and environment/source fingerprints; not a complete proof audit. Lean and TeX are separate.',
          'input_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
          'git_status_before':initial_status,
          'git_status_after':final_status,
          'allow_dirty':args.allow_dirty,
          'toolchain':toolchain,
          'source_manifest':source_manifest_before,
          'source_tree_sha256_before':source_tree_sha256_before,
          'source_tree_sha256_after':source_tree_sha256_after,
          'source_tree_unchanged':source_tree_unchanged,
          'python':platform.python_version(),'checks':rows,
          'selection':args.only or 'complete Python/C++ surface',
          'passed':sum(r['exit_code']==0 for r in rows),'total':len(rows),
          'repository_mutation_policy':'Generated verifier outputs stay below --logs; committed evidence is not rewritten.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    if not source_tree_unchanged:
        raise SystemExit('Verification mutated a maintained source/dependency file.')
    if not args.allow_dirty and final_status:
        raise SystemExit('Verification left the Git worktree dirty; inspect generated paths.')
    if data['passed']!=data['total']:raise SystemExit('Verification failed; inspect saved logs.')

if __name__=='__main__':main()
