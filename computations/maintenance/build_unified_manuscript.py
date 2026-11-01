#!/usr/bin/env python3
"""Build the authoritative consolidated TeX and record a fail-closed manifest.

The build checks typesetting and immutable inputs, not mathematical truth.
It never edits old manuscript sources. --publish copies only the verified PDF.

Engines: pdflatex (three passes; authoritative, used by CI) is preferred.
When pdflatex is not installed, ``--engine auto`` (the default) falls back to
Tectonic (``$TECTONIC`` or ``tectonic`` on PATH), which reruns internally until
the auxiliary files are stable.  Every gate below (no overfull boxes, no
unresolved references/citations, no duplicate labels/destinations, immutable
inputs, parsed page count) applies unchanged to both engines, and the manifest
records which engine produced the PDF.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time

ROOT=Path(__file__).resolve().parents[2]
MANUSCRIPT=ROOT/'manuscript'

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def _validate_inherited_core(name: str, text: str, source: str) -> None:
    artifacts=(r'\^{}',r'\textgreater',r'\textless',r'\textbar',r'\textsuperscript')
    if any(x in text for x in artifacts):
        raise ValueError(f'Unconverted ASCII mathematics in inherited core {source}')
    required={
        'pell_blocks.tex':(r'H=\langle h\rangle',r'Z^*(U_0-I)Z',r'J^*\Delta J'),
        'floquet.tex':(r'V^*W(1,0)V',r'U_N=VU_0V^*'),
    }
    for token in required.get(name,()):
        if token not in text:
            raise ValueError(f'Missing restored mathematical token {token}: {source}')

def page_count_from_log(text: str) -> int | None:
    # TeX wraps its fixed-width log even inside the page-count digits.
    match = re.search(
        r'Output written on .*?\(\s*(\d(?:\s*\d)*)\s+p\s*a\s*g\s*e\s*s?',
        text, re.S)
    if not match:
        return None
    count = int(re.sub(r'\s+', '', match[1]))
    return count if count > 0 else None

def inputs() -> dict[str,str]:
    master=MANUSCRIPT/'BGS_unified.tex'
    found:set[Path]=set()
    def visit(p:Path)->None:
        p=p.resolve()
        if p in found:return
        if not p.is_relative_to(MANUSCRIPT.resolve()):
            raise ValueError(f'Nonlocal TeX input: {p}')
        if not p.is_file():
            raise ValueError(f'Missing TeX input: {p}')
        found.add(p)
        text=p.read_text(encoding='utf-8')
        if re.search(r'\b(?:sqrt|exp|log|sin|cos|[A-Za-z])\([A-Z]{2}\.[A-Za-z0-9]+\)',text):
            raise ValueError(f'Spurious equation prefix inside a function evaluation: {p}')
        if p.name in ('pell_blocks.tex','floquet.tex'):
            _validate_inherited_core(p.name,text,str(p.relative_to(ROOT)))
        for rel in re.findall(r'\\input\{([^}]+)\}',text):
            q=MANUSCRIPT/rel
            if not q.suffix:q=q.with_suffix('.tex')
            visit(q)
    visit(master)

    # The canonical Floquet core may be split into sequential source parts.
    # Preserve the old fail-closed mathematical token/artifact gate by checking
    # their concatenation, but only for parts actually reachable from the master.
    floquet_parts=sorted(
        (p for p in found if re.fullmatch(r'floquet_part\d+\.tex',p.name)),
        key=lambda p:int(re.search(r'(\d+)',p.name).group(1)),
    )
    if floquet_parts:
        indices=[int(re.search(r'(\d+)',p.name).group(1)) for p in floquet_parts]
        if indices != list(range(1,len(indices)+1)):
            raise ValueError(f'Noncontiguous canonical Floquet parts: {indices}')
        combined=''.join(p.read_text(encoding='utf-8') for p in floquet_parts)
        _validate_inherited_core('floquet.tex',combined,'canonical floquet_partN inputs')

    return {str(p.relative_to(ROOT)):digest(p) for p in sorted(found)}

def select_engine(choice: str) -> tuple[str,str]:
    """Return (kind, executable); fail closed if the requested engine is absent."""
    pdflatex=shutil.which('pdflatex')
    tectonic=os.environ.get('TECTONIC') or shutil.which('tectonic')
    if tectonic and not (Path(tectonic).is_file() and os.access(tectonic,os.X_OK)):
        tectonic=None
    if choice in ('auto','pdflatex') and pdflatex:
        return 'pdflatex',pdflatex
    if choice in ('auto','tectonic') and tectonic:
        return 'tectonic',tectonic
    raise SystemExit(f'No usable TeX engine for --engine {choice} '
                     '(need pdflatex, or Tectonic via $TECTONIC/PATH); no build was performed.')

def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,default=ROOT/'build/unified-paper')
    parser.add_argument('--publish',action='store_true')
    parser.add_argument('--engine',choices=('auto','pdflatex','tectonic'),default='auto',
                        help='auto: pdflatex when installed, otherwise Tectonic')
    args=parser.parse_args()
    kind,engine=select_engine(args.engine)
    out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    if out==MANUSCRIPT.resolve():
        raise SystemExit('Use an out-of-tree build directory, not manuscript/.')
    before=inputs();start=time.monotonic()
    version=subprocess.check_output([engine,'--version'],text=True).splitlines()[0]
    scope=('Three LaTeX passes' if kind=='pdflatex' else
           'One Tectonic compile (internal reruns until auxiliary files are stable)')
    record={'status':'RUNNING','started_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
            'scope':scope+', no horizontal overflow or unresolved references/citations, immutable TeX inputs. Mathematical truth and page-image inspection are separate.',
            'engine_kind':kind,'engine':version,'source_sha256':before,'passes':[]}
    env=dict(os.environ,SOURCE_DATE_EPOCH='1788652800',FORCE_SOURCE_DATE='1',TZ='UTC')
    if kind=='pdflatex':
        runs=[([engine,'-interaction=nonstopmode','-halt-on-error',f'-output-directory={out}','BGS_unified.tex'],90)
              for _ in range(3)]
    else:
        runs=[([engine,'-X','compile','--keep-logs','--keep-intermediates',
                '--outdir',str(out),'BGS_unified.tex'],1800)]
    for number,(command,timeout) in enumerate(runs,1):
        log=out/f'pass-{number}.log'
        with log.open('w') as stream:
            result=subprocess.run(command,cwd=MANUSCRIPT,env=env,stdout=stream,stderr=subprocess.STDOUT,timeout=timeout)
        record['passes'].append({'command':command,'returncode':result.returncode,'log':log.name,'sha256':digest(log)})
        if result.returncode:
            record['status']='FAIL';(out/'build_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
            raise SystemExit(f'LaTeX pass {number} failed; see {log}')
    text=(out/'BGS_unified.log').read_text(errors='replace')
    forbidden=['Overfull \\hbox','undefined references','undefined citations','multiply defined','destination with the same identifier']
    hits=[x for x in forbidden if x in text]
    if re.search(r"LaTeX Warning: (Reference|Citation) .* undefined",text):hits.append('unresolved cross-reference')
    after=inputs()
    record.update(sources_unchanged=before==after,forbidden_warnings=hits)
    if hits or before!=after:
        record['status']='FAIL';(out/'build_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
        raise SystemExit('Build failed its warning/source-hash gate.')
    pdf=out/'BGS_unified.pdf'
    page_count=page_count_from_log(text)
    if page_count is None:
        record['status']='FAIL';(out/'build_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
        raise SystemExit('Build succeeded but PDF page count could not be parsed from the LaTeX log.')
    record.update(status='PASS',runtime_seconds=time.monotonic()-start,
                  page_count=page_count,pdf_sha256=digest(pdf),pdf_bytes=pdf.stat().st_size,
                  latex_log_sha256=digest(out/'BGS_unified.log'))
    if args.publish:
        target=MANUSCRIPT/pdf.name;shutil.copy2(pdf,target)
        record['published_pdf']=str(target.relative_to(ROOT))
    (out/'build_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('status','page_count','pdf_sha256','runtime_seconds')},indent=2))

if __name__=='__main__':main()
