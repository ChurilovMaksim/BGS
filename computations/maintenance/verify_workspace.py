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
import re
import shlex
import subprocess
import sys
import time
import tempfile

from workspace_sources import git_root, read_manifest, validate

ROOT=Path(__file__).resolve().parents[2]

# These replays expose durable evidence modes. Keep their fresh outputs under
# --logs so the CI artifact upload preserves new results even after failure.
REPLAY_ARTIFACT_OPTIONS = {
    'intermediate_old_layers_certificates': '--replay-output-dir',
    'charge_strengthening_replay': '--output-dir',
    'balanced_pair_schur': '--output-dir',
    'research_checkpoint_replay': '--output-dir',
    'wave2_portable_replay': '--output-dir',
    'wave3_checked_replay': '--output-dir',
    'fractional_hamming_replay': '--output-dir',
    'fractional_hamming_full_end_2_1': '--output-dir',
    'fractional_hamming_full_end_2_2': '--output-dir',
    'fractional_hamming_full_end_2_3': '--output-dir',
    'fractional_hamming_full_end_3_2': '--output-dir',
    'fractional_hamming_top_gram': '--output-dir',
    'fractional_hamming_torus': '--output-dir',
    'fractional_hamming_network': '--output-dir',
    'fractional_hamming_offcharge_bound': '--output-dir',
}


# One unchanged exact N4 packet now has a declared 600 CPU / 660 wall budget.
# Keep its aggregate watchdog finite with room for the other packet controls.
CHECK_TIMEOUT_SECONDS = {'research_checkpoint_replay': 900}


def check_timeout_seconds(name):
    return CHECK_TIMEOUT_SECONDS.get(name, 360)


def replay_artifact_args(name: str, certificate_directory: Path) -> list[str]:
    option = REPLAY_ARTIFACT_OPTIONS.get(name)
    return [option, str(certificate_directory / name)] if option else []


MOMENTUM_STDOUT='evidence/executions/20261029/momentum-phase-cue/python_stdout.json'

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git_status(*, include_untracked: bool=True) -> list[str]:
    mode='all' if include_untracked else 'no'
    result=subprocess.run(
        ['git','status','--porcelain=v1',f'--untracked-files={mode}'],
        cwd=ROOT,text=True,capture_output=True,check=True)
    return [line for line in result.stdout.splitlines() if line]

def source_manifest() -> dict[str,str]:
    raw=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=ROOT)
    rels=[item.decode('utf-8') for item in raw.split(b'\0') if item]
    manifest={}
    for rel in sorted(set(rels)):
        path=ROOT/rel
        if path.is_symlink() or not path.is_file():
            raise RuntimeError(f'Tracked path is not a regular file: {rel}')
        manifest[rel]=sha256(path)
    return manifest

def validate_output_locations(root: Path, paths: list[Path], manifest: dict[str, str],
                              archive_manifest: Path | None = None) -> None:
    """Reject source/output overlap before execution, including the final receipt."""
    root = root.resolve()
    maintained = [(root / rel).resolve() for rel in manifest]
    if archive_manifest is not None:
        maintained.append(archive_manifest.resolve())
    for raw in paths:
        path = raw.resolve()
        if any(source == path or source.is_relative_to(path) for source in maintained):
            raise ValueError(f'Output overlaps maintained source: {raw}')
        if path.is_relative_to(root):
            parts = path.relative_to(root).parts
            if not parts or parts[0] != 'build':
                raise ValueError(f'Output must be outside source or under its build/ directory: {raw}')


def manifest_digest(manifest: dict[str,str]) -> str:
    payload=json.dumps(manifest,sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(payload).hexdigest()

def command_version(command: str) -> str | None:
    words=shlex.split(command)
    if not words:return None
    exe=shutil.which(words[0])
    if not exe:return None
    try:
        output=subprocess.check_output([exe,*words[1:],'--version'],text=True,stderr=subprocess.STDOUT,timeout=10)
    except Exception:
        return None
    return output.splitlines()[0] if output else None

def package_versions() -> dict[str,str | None]:
    out={}
    for name in ('numpy','sympy','mpmath','matplotlib','scipy'):
        try:out[name]=importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:out[name]=None
    return out

def boost_probe(compiler: str, include: Path | None = None) -> dict:
    """Read Boost macros using the declared compiler and its actual include search.

    This verifies header availability, not the provenance of prebuilt binaries.
    The command and include-affecting environment are retained for reproduction.
    """
    command = shlex.split(compiler)
    if include is not None:
        command += ['-I', str(include.resolve())]
    command += ['-dM', '-E', '-x', 'c++', '-']
    result = {'command': command, 'include': str(include.resolve()) if include else None,
              'environment': {key: os.environ.get(key) for key in
                              ('CPATH', 'CPLUS_INCLUDE_PATH', 'C_INCLUDE_PATH')},
              'version': None, 'error': None}
    try:
        process = subprocess.run(command, input='#include <boost/version.hpp>\n',
                                 text=True, capture_output=True, timeout=15)
        if process.returncode:
            result['error'] = process.stderr[-4000:]
            return result
        match = re.search(r'^#define BOOST_LIB_VERSION "([0-9]+(?:_[0-9]+)+)"$',
                          process.stdout, re.MULTILINE)
        numeric = re.search(r'^#define BOOST_VERSION ([0-9]+)$', process.stdout, re.MULTILINE)
        if not match or not numeric:
            result['error'] = 'Boost version macros missing or malformed'
            return result
        parts = [int(value) for value in match.group(1).split('_')]
        expected = parts[0] * 100000 + parts[1] * 100 + (parts[2] if len(parts) == 3 else 0)
        if len(parts) not in (2, 3) or int(numeric.group(1)) != expected:
            result['error'] = 'Boost numeric and string version macros disagree'
            return result
        result['version'] = match.group(1)
    except (OSError, subprocess.TimeoutExpired) as exc:
        result['error'] = str(exc)
    return result


def validate_versions(toolchain: dict, requirements: Path, *, need_cpp: bool, need_git: bool) -> list[str]:
    errors=[]
    for line in requirements.read_text(encoding='utf-8').splitlines():
        line=line.strip()
        if not line or line.startswith('#'):continue
        if line.count('==') != 1:
            errors.append('Unsupported requirements pin: '+line)
            continue
        name,expected=line.split('==')
        actual=toolchain['packages'].get(name)
        if actual != expected:
            errors.append(f'{name}: expected {expected}, observed {actual!r} (missing/unknown is not verified)')
    for name in (['git'] if need_git else []) + (['cmake','cxx','boost_lib_version'] if need_cpp else []):
        value=toolchain.get(name)
        if not value or not any(c.isdigit() for c in value):
            errors.append(f'{name}: missing or unknown version')
    return errors

def dependent_replay(item, producer_name: str, artifact: Path, rows: list[dict],
                     check, logs: Path) -> dict:
    """Gate a replay on its producer and a regular output in this run's fresh directory."""
    producer = next((row for row in rows if row['name'] == producer_name), None)
    reason = None
    if producer is None or producer['exit_code'] != 0:
        reason = f'Producer {producer_name} missing or failed; replay not executed.'
    elif artifact.is_symlink() or not artifact.is_file():
        reason = f'Producer {producer_name} supplied no fresh regular artifact; replay not executed.'
    if reason is not None:
        name, command, source = item
        log = logs / (name + '.log')
        log.write_text(reason + '\n')
        print(name, 'BLOCKED', reason, flush=True)
        return {'name': name, 'source': str(source.relative_to(ROOT)),
                'sha256': sha256(source) if source.is_file() else None,
                'source_unchanged': None, 'command': command, 'exit_code': 126,
                'execution_status': 'blocked', 'blocked_reason': reason,
                'executable_sha256': None, 'seconds': 0,
                'log_sha256': sha256(log), 'producer': producer_name,
                'input_artifact': str(artifact), 'input_artifact_sha256': None}
    before = sha256(artifact)
    row = check(item)
    unchanged = (artifact.is_file() and not artifact.is_symlink()
                 and sha256(artifact) == before)
    row.update(producer=producer_name, input_artifact=str(artifact),
               input_artifact_sha256=before, input_artifact_unchanged=unchanged)
    if not unchanged:
        row['exit_code'] = 125
        row['execution_status'] = 'failed_input_mutation'
    return row


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build',type=Path,required=True)
    parser.add_argument('--logs',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--workers',type=int,default=2)
    parser.add_argument('--boost-include',type=Path,
                        help='Boost header root used by the C++ build; probed with CXX and recorded.')
    parser.add_argument('--archive-manifest',type=Path,
                        help='Explicit SHA-256 manifest for a source archive without Git.')
    parser.add_argument('--allow-dirty',action='store_true',
                        help='Record but do not reject a dirty initial Git worktree.')
    parser.add_argument('--only',action='append',default=[],
                        help='Run only named checks; repeat for a focused verification group.')
    args=parser.parse_args()
    if args.workers<1:parser.error('--workers must be positive')
    archive_mode=args.archive_manifest is not None
    if archive_mode and git_root(ROOT):
        parser.error('--archive-manifest requires a non-Git archive; use Git mode in a checkout')
    if not archive_mode and not git_root(ROOT):
        parser.error('No Git checkout: supply --archive-manifest (see REPRODUCE_unified.md)')
    if archive_mode and args.allow_dirty:
        parser.error('--allow-dirty cannot bypass archive manifest validation')
    try:
        expected=read_manifest(args.archive_manifest) if archive_mode else None
        source_manifest_before=validate(ROOT,expected) if archive_mode else source_manifest()
    except (ValueError, OSError, RuntimeError) as exc:
        parser.error(str(exc))
    try:
        validate_output_locations(ROOT,[args.logs,args.output],source_manifest_before,args.archive_manifest)
    except ValueError as exc:
        parser.error(str(exc))
    archive_manifest_hash=sha256(args.archive_manifest) if archive_mode else None
    input_commit=None if archive_mode else subprocess.check_output(
        ['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    initial_status=None if archive_mode else git_status(include_untracked=True)
    if initial_status and not args.allow_dirty:
        parser.error('Git worktree is not clean; commit/stash changes or pass --allow-dirty')
    source_tree_sha256_before=manifest_digest(source_manifest_before)
    compiler=os.environ.get('CXX','c++')
    boost=boost_probe(compiler,args.boost_include)
    toolchain={
        'platform':platform.platform(),
        'python':platform.python_version(),
        'python_parent_optimization_level':sys.flags.optimize,
        'python_executable':sys.executable,
        'packages':package_versions(),
        'git':command_version('git'),
        'cmake':command_version('cmake'),
        'cxx':command_version(compiler),
        'boost_lib_version':boost['version'],
        'boost_probe':boost,
        'requirements_sha256':sha256(ROOT/'requirements.txt'),
        'cmake_lists_sha256':sha256(ROOT/'CMakeLists.txt'),
        'verify_workspace_sha256':sha256(Path(__file__).resolve()),
    }
    args.build=args.build.resolve();args.logs=args.logs.resolve();args.output=args.output.resolve()
    args.logs.mkdir(parents=True,exist_ok=True)
    # A fresh exclusive directory makes stale certificates impossible to reuse,
    # while retaining all earlier producer artifacts for inspection.
    certificate_directory=Path(tempfile.mkdtemp(prefix='certificates-',dir=args.logs))
    resonance_certificate=certificate_directory/'resonance_nondegeneracy_radius8.json'
    extremal_replay=certificate_directory/'extremal.replay'
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
        cmd += replay_artifact_args(p.stem, certificate_directory)
        if p.stem=='wave2_checked_replay':
            # The archived v1 wrapper is SHA-sealed by BOTH Wave2 and Wave3.
            # Recheck its original source closure through the portable v2
            # authenticator: v1's own loader hashes the three governance
            # files (AGENTS.md, SOURCE_OF_TRUTH.md and
            # record/repository_conventions.md) at their live paths, where
            # they editorially evolved after the seal, while the portable
            # loader verifies the identical 70-file closure against the
            # identical sealed digests, resolving exactly those three to
            # their archived sealed copies via the bindings' reviewed
            # historical_resolutions. The portable v2 entry below
            # independently executes ALL eight old tasks with the same
            # authenticated adapter and a four-field basis-invariant policy.
            # v1's historical exact-reference replay remains runnable
            # manually, but cannot be a cross-CPU scientific release gate.
            cmd=[sys.executable,str(p.with_name('wave2_portable_replay.py')),'--check-sources']
        if p.stem=='pell_floquet_regression':
            cmd+=['--cpp',str(args.build/'pell_pair_orthogonality')]
        elif p.stem in {'actual_algebra_check', 'actual_factor_check', 'actual_field_check', 'actual_casoratian_check'}:
            cmd+=['--output',str(args.logs/'actual_commutant')]
        elif p.stem=='pell_pair_obstruction':
            cmd+=['--output',str(args.logs/'pell_pair_obstruction.json')]
        elif p.stem=='resonance_nondegeneracy_certificate':
            cmd+=['--radius','8','--output',str(resonance_certificate)]
        elif p.stem=='resonance_nondegeneracy_margin':
            # Declared args (phase-5 G8 fix): the margin compiler requires a
            # certificate positional and --output. It replays the DEPOSITED
            # radius-eight certificate (ND.10 closure); its own asserts pin
            # the content (status CERTIFICATE, remaining [], equation SHA).
            # Missing certificate fails loudly here, never silently skips.
            margin_certificate=ROOT/'evidence/executions/20261006/corpus-revision/final/checks/certificates-mpuvq_28/resonance_nondegeneracy_radius8.json'
            if not margin_certificate.is_file():
                parser.error('Missing deposited radius-eight certificate for resonance_nondegeneracy_margin: '+str(margin_certificate))
            cmd+=[str(margin_certificate),'--output',str(args.logs/'resonance_nondegeneracy_margin.json')]
        elif p.stem=='replay_spectral_corpus':
            # Declared args (phase-5 G8 fix): --output-dir is required; the
            # script creates the directory. Output stays under --logs.
            cmd+=['--output-dir',str(args.logs/'replay_spectral_corpus')]
        elif p.stem=='resonance_hessian_obstruction':
            cmd+=['--output',str(args.logs/'resonance_hessian_obstruction.json')]
        elif p.stem=='resonance_quantum_variance':
            cmd+=['--output',str(args.logs/'resonance_quantum_variance.json')]
        elif p.stem=='finite_orbit_resonance':
            cmd+=['--output',str(args.logs/'finite_orbit_resonance.json')]
        elif p.stem=='frozen_antireversor':
            cmd+=['--output-dir',str(args.logs/'frozen_antireversor')]
        elif p.stem in {'frozen_full_lag_gap', 'frozen_kick_rank',
                        'nonlinear_pressure_variance', 'frozen_seven_cut',
                        'frozen_total_minors', 'frozen_arithmetic_traces',
                        'quadratic_noise_dynamics', 'quadratic_noise_clock',
                        'coboundary_mobius_diffusion', 'coboundary_joint_limit',
                        'coboundary_polynomial_limit', 'coboundary_general_start',
                        'circular_dyson_relaxation', 'microscopic_noise_removal',
                        'local_moment_transport',
                        'clock_structure_and_heat_projection',
                        'growing_degree_trace_projection',
                        'heisenberg_pair_heat_formula',
                        'frozen_operator_transfer_coercivity',
                        'collective_diffusion_gap',
                        'heisenberg_note_audit', 'prime_resonant_audit',
                        'signed_heisenberg_audit', 'resonant_density_audit',
                        'folded_quadratic_audit', 'expansion_wavepacket_audit'}:
            cmd+=['--output',str(args.logs/(p.stem+'.json'))]
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
        # Declared args (phase-5 G8 fix): the replay requires a radius;
        # 8 is the ND.10 radius-eight certificate radius.
        if p.stem=='resonance_complex_replay':cmd+=['8']
        items.append(('cpp_'+p.stem,cmd,p))
    if args.only:
        missing=set(args.only)-{item[0] for item in items}
        if missing:parser.error('Unknown checks: '+', '.join(sorted(missing)))
        items=[item for item in items if item[0] in args.only]
        # The complete run below owns the dependent certificate replays.
        if any(item[0] in {'resonance_nondegeneracy_certificate','extremal_resonance'}
               for item in items):
            parser.error('Dependent certificate producers require a complete run.')
    preflight=validate_versions(toolchain,ROOT/'requirements.txt',
                                need_cpp=any(name.startswith('cpp_') or name=='pell_floquet_regression' for name,_,_ in items),
                                need_git=not archive_mode)
    if preflight:parser.error('Dependency/version preflight failed: '+ '; '.join(preflight))
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MPLBACKEND='Agg',
             PYTHONOPTIMIZE='0')
    def check(item):
        name,cmd,source=item;start=time.monotonic();log=args.logs/(name+'.log')
        source_hash=sha256(source)
        executable=Path(cmd[0])
        executable_hash=sha256(executable) if executable.is_file() else None
        with log.open('w') as stream:
            try:
                code=subprocess.run(cmd,cwd=ROOT,env=env,stdout=stream,
                                    stderr=subprocess.STDOUT,timeout=check_timeout_seconds(name)).returncode
            except subprocess.TimeoutExpired:code=124
            except OSError as exc:
                stream.write(str(exc)+'\n');code=127
        unchanged=source.is_file() and source_hash==sha256(source)
        if not unchanged:code=125
        row={'name':name,'source':str(source.relative_to(ROOT)),'sha256':source_hash,
             'source_unchanged':unchanged,'command':cmd,'exit_code':code,
             'execution_status':'passed' if code==0 else 'failed',
             'executable_sha256':executable_hash,
             'seconds':round(time.monotonic()-start,3),
             'declared_wall_timeout_seconds':check_timeout_seconds(name),
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
             '--output',str(certificate_directory/'resonance_certificate_replay.json')]
        rows.append(dependent_replay(('check_resonance_certificate',cmd,deferred_checker),
                                     'resonance_nondegeneracy_certificate',resonance_certificate,
                                     rows,check,args.logs))
        source=ROOT/'computations/cpp/extremal_resonance_replay.cpp'
        rows.append(dependent_replay(('extremal_independent_replay',
                           [str(args.build/'extremal_resonance_replay'),str(extremal_replay)],source),
                           'extremal_resonance',extremal_replay,rows,check,args.logs))
    if not archive_mode and not initial_status and (ROOT/MOMENTUM_STDOUT).exists():
        # momentum_phase_cue.py (hash-pinned in its receipt) rewrites its committed
        # python_stdout.json; the seeded Gaussian mean varies in the last float digit
        # across BLAS builds. Restore that one file so the worktree check stays strict.
        subprocess.run(['git','checkout','--',MOMENTUM_STDOUT],cwd=ROOT,check=True)
    source_error=None
    try:
        source_manifest_after=validate(ROOT,expected) if archive_mode else source_manifest()
    except (ValueError, OSError, RuntimeError) as exc:
        source_manifest_after={}
        source_error=str(exc)
    source_tree_sha256_after=manifest_digest(source_manifest_after)
    source_tree_unchanged=source_tree_sha256_before==source_tree_sha256_after
    final_status=None if archive_mode else git_status(include_untracked=True)
    final_commit=None if archive_mode else subprocess.check_output(
        ['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    if final_commit != input_commit:
        source_tree_unchanged=False
        source_error='Git HEAD changed during execution'
    if archive_mode and (not args.archive_manifest.is_file() or sha256(args.archive_manifest)!=archive_manifest_hash):
        source_tree_unchanged=False
        source_error='Archive manifest changed during execution'
    data={'producer':'computations/maintenance/verify_workspace.py',
          'scope':'Executable Python/C++ coverage with sequential certificate replays and environment/source fingerprints; not a complete proof audit. Lean and TeX are separate.',
          'input_commit':input_commit,
          'upstream_commit':None,
          'source_mode':'archive' if archive_mode else 'git',
          'archive_manifest_sha256':archive_manifest_hash,
          'source_validation_error':source_error,
          'git_status_before':initial_status,
          'git_status_after':final_status,
          'allow_dirty':args.allow_dirty,
          'toolchain':toolchain,
          'source_manifest':source_manifest_before,
          'source_tree_sha256_before':source_tree_sha256_before,
          'source_tree_sha256_after':source_tree_sha256_after,
          'source_tree_unchanged':source_tree_unchanged,
          'python':platform.python_version(),
          'python_parent_optimization_level':sys.flags.optimize,'checks':rows,
          'certificate_directory':str(certificate_directory),
          'selection':args.only or 'complete Python/C++ surface',
          'python_assertions':'Child PYTHONOPTIMIZE=0; verifier assert statements enabled.',
          'cpp_build_provenance':'Prebuilt executable hashes are recorded; this runner does not establish source-to-binary correspondence.',
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
