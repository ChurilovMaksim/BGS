#!/usr/bin/env python3
"""Static source/citation index for the single maintained BGS TeX monograph.

A syntactic integrity gate, not a theorem validator, PDF checker or source
novelty audit. The checks are read-only and require no third-party packages.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
INPUT = re.compile(r'\\(?:input|include)\s*\{([^{}]+)\}')
BIB = re.compile(r'\\bibitem(?:\[[^\]]*\])?\s*\{([^{}]+)\}')
CITE = re.compile(
    r'\\(?:cite|citep|citet|citealp|autocite|parencite|textcite)'
    r'\*?(?:\s*\[[^\]]*\]){0,2}\s*\{([^{}]+)\}')
LABEL = re.compile(r'\\label\s*\{([^{}]+)\}')
REF = re.compile(r'\\(?:eqref|ref|autoref|cref|Cref|pageref)\s*\{([^{}]+)\}')
VERBATIM_BEGIN = re.compile(r'\\begin\s*\{(verbatim\*?|Verbatim|lstlisting|minted)\}')
VERBATIM_END = r'\end{{{}}}'


def active_tex(text: str) -> str:
    """Ignore whole-line TeX comments and supported literal environments.

    A percent sign begins a comment only when the immediately preceding
    backslash run is even; escaped percent signs are retained. Whitespace/line numbers are
    preserved only to the extent required by source-index scanning.
    """
    output = []
    verbatim = None
    for line in text.splitlines():
        if verbatim is not None:
            end = VERBATIM_END.format(verbatim)
            if end in line:
                verbatim = None
            continue
        chars = []
        for i, ch in enumerate(line):
            if ch == '%':
                j = i - 1
                while j >= 0 and line[j] == '\\':
                    j -= 1
                if (i - 1 - j) % 2 == 0:
                    break
            chars.append(ch)
        clean = ''.join(chars)
        match = VERBATIM_BEGIN.search(clean)
        if match:
            output.append(clean[:match.start()])
            if VERBATIM_END.format(match.group(1)) not in clean[match.end():]:
                verbatim = match.group(1)
        else:
            output.append(clean)
    return '\n'.join(output)


def audit(repo: Path) -> dict:
    """Read only the TeX include-closure of the maintained article root."""
    base = (repo / 'manuscript').resolve()
    root = base / 'BGS_unified.tex'
    if not root.is_file():
        raise ValueError('Missing manuscript/BGS_unified.tex')
    included = []
    active = []
    cited, bibs, labels, refs = [], [], [], []
    errors = []
    def visit(path: Path):
        path = path.resolve()
        if not path.is_relative_to(base):
            errors.append('TeX include escapes manuscript root: ' + str(path))
            return
        if path in active:
            errors.append('Cyclic TeX include: ' + ' -> '.join(
                p.relative_to(base).as_posix() for p in [*active,path]))
            return
        if path in included:
            errors.append('TeX source included twice: '+path.relative_to(base).as_posix())
            return
        if not path.is_file():
            errors.append('Missing TeX include: ' + path.relative_to(base).as_posix())
            return
        included.append(path)
        active.append(path)
        source = active_tex(path.read_text(encoding='utf-8'))
        cited.extend((item.strip(), path.relative_to(base).as_posix())
                     for m in CITE.finditer(source)
                     for item in m.group(1).split(',') if item.strip())
        bibs.extend((m.group(1).strip(),path.relative_to(base).as_posix())
                    for m in BIB.finditer(source))
        labels.extend((m.group(1).strip(),path.relative_to(base).as_posix())
                      for m in LABEL.finditer(source))
        refs.extend((m.group(1).strip(),path.relative_to(base).as_posix())
                    for m in REF.finditer(source))
        for m in INPUT.finditer(source):
            pathfrag=m.group(1).strip()
            if not pathfrag.endswith('.tex'):
                pathfrag+='.tex'
            child = base / pathfrag
            if not child.is_file():
                child = path.parent / pathfrag
            visit(child)
        active.pop()
    visit(root)
    keys = Counter(key for key,_ in bibs)
    bibnames = set(keys)
    citation_names=set(key for key,_ in cited)
    label_counts=Counter(key for key,_ in labels)
    labelnames=set(label_counts)
    for key in sorted(citation_names-bibnames):
        sources=sorted({source for k,source in cited if k==key})
        errors.append('Unresolved citation '+key+': '+', '.join(sources[:5]))
    for key,count in sorted(keys.items()):
        if count>1:
            errors.append('Duplicate bibliography key '+key+f' ({count} declarations)')
    return {
        'root':'manuscript/BGS_unified.tex',
        'input_files':max(len(included)-1,0),
        'visited_files':len(included),
        'cited_keys':len(citation_names),
        'bibliography_keys':len(keys),
        'labels':len(labelnames),
        'references':len(refs),
        'unresolved_labels':sorted(set(key for key,_ in refs)-labelnames),
        'duplicate_labels':sorted(key for key,n in label_counts.items() if n>1),
        'errors':sorted(errors),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=ROOT)
    parser.add_argument('--check',action='store_true',
                        help='Fail on missing TeX sources or invalid bibliography keys')
    parser.add_argument('--strict-labels',action='store_true',
                        help='Additionally require no unresolved/duplicate LaTeX labels')
    args=parser.parse_args()
    result=audit(args.repo)
    print(json.dumps(result,indent=2,ensure_ascii=False))
    if args.check and result['errors']:
        raise SystemExit('BGS manuscript source/citation audit failed')
    if args.strict_labels and (result['unresolved_labels'] or result['duplicate_labels']):
        raise SystemExit('BGS manuscript label audit failed')


if __name__ == '__main__':
    main()
