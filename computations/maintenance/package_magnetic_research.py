#!/usr/bin/env python3
"""Package the focused magnetic research without claiming a full-repository audit.

The source tree is never rewritten. Optional verification records failures as
failures; local Python execution is not represented as Lean compilation.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile

ROOT=Path(__file__).resolve().parents[2]
FILES=(
 'mathematics/magnetic_quotient_semicircle.md',
 'manuscript/magnetic_quotient_semicircle.tex',
 'manuscript/magnetic_quotient_semicircle.pdf',
 'computations/cpp/magnetic_word_verifier.cpp',
 'computations/verification/magnetic_quotient_regression.py',
 'computations/verification/magnetic_scalar_certificate.py',
 'computations/verification/cdf_sup_regression.py',
 'computations/analysis/spectral_diagnostics.py',
 'computations/analysis/magnetic_spectrum_figure.py',
 'computations/maintenance/package_magnetic_research.py',
 'evidence/certificates/magnetic_quotient_audit.json',
 'evidence/numerical/magnetic_quotient_global.json',
 'assets/magnetic_quotient_global.svg',
 'assets/magnetic_quotient_global.png',
 'literature/magnetic_quotient_sources_20260905.md',
 'record/referee_audit_20260905.md',
 'requirements.txt',
)


def run_check(name: str, command: list[str], cwd: Path, logs: Path,
              env: dict[str,str], timeout: int=300) -> dict:
    log=logs/(name+'.log')
    try:
        with log.open('w') as stream:
            result=subprocess.run(command,cwd=cwd,env=env,stdout=stream,
                                  stderr=subprocess.STDOUT,timeout=timeout)
        code=result.returncode
        status='pass' if code==0 else 'fail'
    except subprocess.TimeoutExpired:
        code=None;status='timeout'
    except OSError as exc:
        log.write_text(str(exc)+'\n');code=None;status='unavailable'
    return {'name':name,'command':command,'status':status,'exit_code':code,
            'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest()}


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True,help='ZIP destination outside the source tree')
    parser.add_argument('--verify',action='store_true',help='compile C++ and run the focused Python checks')
    parser.add_argument('--check-lean',action='store_true',help='also build the copied formalization with lake')
    args=parser.parse_args()
    destination=args.output.expanduser().resolve()
    if destination==ROOT or ROOT in destination.parents:
        raise ValueError('the archive destination must be outside the source tree')
    if destination.suffix.lower()!='.zip':raise ValueError('output must have a .zip suffix')
    destination.parent.mkdir(parents=True,exist_ok=True)
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='wow-magnetic-package-') as temp:
        work=Path(temp);package=work/'WoW_magnetic_research';package.mkdir()
        missing=[]
        for relative in FILES:
            source=ROOT/relative
            if not source.is_file():missing.append(relative);continue
            target=package/relative;target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(source,target)
        for relative in ('computations/python/bgs','formalization'):
            shutil.copytree(ROOT/relative,package/relative,
                ignore=shutil.ignore_patterns('.lake','__pycache__','*.pyc','build'))
        logs=package/'verification_logs';logs.mkdir()
        checks=[]
        if args.verify:
            compiler=shutil.which('g++') or shutil.which('c++') or 'g++'
            binary=work/'magnetic_word_verifier'
            checks.append(run_check('cpp_build',[compiler,'-std=c++20','-O2',
                'computations/cpp/magnetic_word_verifier.cpp','-o',str(binary)],package,logs,env))
            if checks[-1]['status']=='pass':
                (package/'evidence/certificates').mkdir(parents=True,exist_ok=True)
                checks.append(run_check('magnetic_regression',['python',
                    'computations/verification/magnetic_quotient_regression.py',
                    '--cpp',str(binary),'--output','evidence/certificates/magnetic_quotient_audit.json'],package,logs,env))
            for name,path in [('scalar_certificate','magnetic_scalar_certificate.py'),
                              ('cdf_regression','cdf_sup_regression.py')]:
                checks.append(run_check(name,['python','computations/verification/'+path],package,logs,env))
        if args.check_lean:
            checks.append(run_check('lean_build',['lake','build'],package/'formalization',logs,env,600))
        status={'producer':'computations/maintenance/package_magnetic_research.py',
          'scope':'Focused research package, not a complete proof audit or microscopic BGS theorem.',
          'checks':checks,'missing_optional_files':missing,
          'lean_requested':args.check_lean,'verification_requested':args.verify,
          'priority':'Not established; no externally refereed priority claim is made.',
          'remote_sync':'The archive does not assert the status of any GitHub publication job.'}
        try:
            status['base_commit']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
            status['working_tree_clean']=not subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True).strip()
        except (OSError,subprocess.CalledProcessError):
            status['base_commit']=None;status['working_tree_clean']=None
        (package/'VERIFICATION_STATUS.json').write_text(json.dumps(status,indent=2)+'\n')
        (package/'requirements-research.txt').write_text('-r requirements.txt\nmatplotlib==3.10.0\n')
        (package/'README.md').write_text('''# Focused magnetic-quotient research package

The proof is in `mathematics/magnetic_quotient_semicircle.md`. Its global
semicircle law assumes prime K=o(log p); this is not microscopic BGS.
The proof also establishes the obstruction to that regime for orders of one
fixed hyperbolic integral cat map. Exact operator identities have wider scope.

Consult `VERIFICATION_STATUS.json` and `verification_logs` for actual requested
checks and their outcomes. A clean compiler run is not inferred from the
presence of Lean source. Four finite trace identities are not a formalization
of the analytic limiting theorem. Source SHA256 hashes identify the packaged
files even when the source working tree was not clean.

```sh
python -m pip install -r requirements-research.txt
g++ -std=c++20 -O2 computations/cpp/magnetic_word_verifier.cpp -o /tmp/magnetic_word_verifier
OPENBLAS_NUM_THREADS=1 python computations/verification/magnetic_quotient_regression.py --cpp /tmp/magnetic_word_verifier
python computations/verification/magnetic_scalar_certificate.py
python computations/verification/cdf_sup_regression.py
(cd formalization && lake build)
```
''')
        def included(path: Path) -> bool:
            return path.is_file() and not any(part in ('.lake','__pycache__') for part in path.relative_to(package).parts)
        files=sorted(path for path in package.rglob('*') if included(path))
        manifest='\n'.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(package).as_posix() for p in files)+'\n'
        (package/'SHA256SUMS').write_text(manifest)
        with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(package.rglob('*')):
                if included(path):archive.write(path,package.name+'/'+path.relative_to(package).as_posix())
        print(json.dumps(status,indent=2));print('Archive:',destination)
        return 1 if any(c['status']!='pass' for c in checks) else 0

if __name__=='__main__':raise SystemExit(main())
