#!/usr/bin/env python3
"""Build the authoritative consolidated TeX and record a fail-closed manifest.

The build checks typesetting and immutable inputs, not mathematical truth.
It never edits old manuscript sources. --publish copies only the verified PDF.
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

def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,default=ROOT/'build/unified-paper')
    parser.add_argument('--publish',action='store_true')
    args=parser.parse_args()
    engine=shutil.which('pdflatex')
    if not engine:raise SystemExit('pdflatex is required; no build was performed.')
    out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    if out==MANUSCRIPT.resolve():
        raise SystemExit('Use an out-of-tree build directory, not manuscript/.')
    before=inputs();start=time.monotonic()
    version=subprocess.check_output([engine,'--version'],text=True).splitlines()[0]
    record={'status':'RUNNING','started_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
            'scope':'Three LaTeX passes, no horizontal overflow or unresolved references/citations, immutable TeX inputs. Mathematical truth and page-image inspection are separate.',
            'engine':version,'source_sha256':before,'passes':[]}
    env=dict(os.environ,SOURCE_DATE_EPOCH='1788652800',FORCE_SOURCE_DATE='1',TZ='UTC')
    for number in range(1,4):
        command=[engine,'-interaction=nonstopmode','-halt-on-error',f'-output-directory={out}','BGS_unified.tex']
        log=out/f'pass-{number}.log'
        with log.open('w') as stream:
            result=subprocess.run(command,cwd=MANUSCRIPT,env=env,stdout=stream,stderr=subprocess.STDOUT,timeout=90)
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
    match=re.search(r'Output written on .*?\(\s*(\d+)\s+p\s*a\s*g\s*e\s*s?',text,re.S)
    if not match:
        record['status']='FAIL';(out/'build_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
        raise SystemExit('Build succeeded but PDF page count could not be parsed from the LaTeX log.')
    record.update(status='PASS',runtime_seconds=time.monotonic()-start,
                  page_count=int(match[1]),pdf_sha256=digest(pdf),pdf_bytes=pdf.stat().st_size,
                  latex_log_sha256=digest(out/'BGS_unified.log'))
    if args.publish:
        target=MANUSCRIPT/pdf.name;shutil.copy2(pdf,target)
        record['published_pdf']=str(target.relative_to(ROOT))
    (out/'build_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('status','page_count','pdf_sha256','runtime_seconds')},indent=2))

if __name__=='__main__':main()
