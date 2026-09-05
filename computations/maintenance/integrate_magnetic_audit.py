#!/usr/bin/env python3
"""Idempotent integration of named, reviewed research-audit corrections.

All edits are prepared before writing. No historical tree or unreviewed
branch is merged by this command. Analytic proofs are not called formalized.
"""
from __future__ import annotations
import ast
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[2]
CDF='''def empirical_cdf_sup_distance(gaps: np.ndarray) -> float:
    """Supremum against the continuous Wigner-surmise CDF, both jump sides."""
    ordered = np.asarray(gaps, dtype=float)
    if ordered.ndim != 1 or len(ordered) == 0 or not np.all(np.isfinite(ordered)) or np.any(ordered < 0):
        raise ValueError("a nonempty one-dimensional finite nonnegative gap sample is required")
    ordered = np.sort(ordered)
    target = goe_wigner_cdf(ordered)
    right = np.arange(1, len(ordered) + 1) / len(ordered)
    left = np.arange(0, len(ordered)) / len(ordered)
    return float(max(np.max(right - target), np.max(target - left)))
'''
LINK_HELPER='''\ndef _markdown_without_code(text: str) -> str:
    """Remove fenced and inline code before extracting Markdown links."""
    text = re.sub(r"(?ms)^ {0,3}(`{3,}|~{3,})[^\\n]*\\n.*?^ {0,3}\\1[ \\t]*$", "", text)
    return re.sub(r"(`+).*?\\1", "", text, flags=re.S)
\n'''

def link_scanner_patch(source: str) -> str:
    if 'def _markdown_without_code(' in source:
        return source
    tree=ast.parse(source)
    def is_link_pattern(node):
        return isinstance(node,ast.Constant) and isinstance(node.value,str) and '\\[' in node.value and '\\(' in node.value
    compiled=set()
    for node in ast.walk(tree):
        if isinstance(node,ast.Assign) and isinstance(node.value,ast.Call):
            call=node.value
            if isinstance(call.func,ast.Attribute) and call.func.attr=='compile' and call.args and is_link_pattern(call.args[0]):
                compiled.update(t.id for t in node.targets if isinstance(t,ast.Name))
    edits=[];lines=source.splitlines(keepends=True);offset=[0]
    for line in lines:offset.append(offset[-1]+len(line))
    for call in ast.walk(tree):
        if not isinstance(call,ast.Call) or not isinstance(call.func,ast.Attribute):continue
        if call.func.attr not in ('findall','finditer'):continue
        arg=None
        if isinstance(call.func.value,ast.Name) and call.func.value.id in compiled and call.args:arg=call.args[0]
        elif len(call.args)>=2 and is_link_pattern(call.args[0]):arg=call.args[1]
        if arg is None:continue
        a=offset[arg.lineno-1]+arg.col_offset;b=offset[arg.end_lineno-1]+arg.end_col_offset
        edits.append((a,b,'_markdown_without_code('+source[a:b]+')'))
    if not edits:raise RuntimeError('Markdown-link extractor not recognized; no guessed patch applied')
    for a,b,new in sorted(edits,reverse=True):source=source[:a]+new+source[b:]
    first=min(n.lineno for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)))
    lines=source.splitlines(keepends=True);lines.insert(first-1,LINK_HELPER)
    return ''.join(lines)

def main():
    edits={}
    def append_once(path,marker,addition):
        old=(ROOT/path).read_text()
        edits[path]=old if marker in old else old.rstrip()+'\n\n'+addition.rstrip()+'\n'
    append_once('CMakeLists.txt','add_executable(magnetic_word_verifier',
      'add_executable(magnetic_word_verifier computations/cpp/magnetic_word_verifier.cpp)')
    append_once('formalization/Bgs.lean','import Bgs.MagneticTraceSmall','import Bgs.MagneticTraceSmall')
    path='computations/analysis/spectral_diagnostics.py';source=(ROOT/path).read_text();tree=ast.parse(source)
    nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='empirical_cdf_sup_distance']
    if len(nodes)!=1:raise RuntimeError('CDF function is not unique')
    node=nodes[0];lines=source.splitlines(keepends=True)
    edits[path]=''.join(lines[:node.lineno-1])+CDF+''.join(lines[node.end_lineno:])
    path='computations/verification/repository_audit.py';edits[path]=link_scanner_patch((ROOT/path).read_text())
    path='computations/cpp/magnetic_word_verifier.cpp';source=(ROOT/path).read_text()
    source=source.replace('half((p+1)/2),c(p,0){','half((p+1)/2){')
    if 'c.assign(' not in source:
        source=source.replace('  h=mod(h,p);I a=1,work=1;','  c.assign(static_cast<std::size_t>(p),0);\n  h=mod(h,p);I a=1,work=1;')
    edits[path]=source
    path='mathematics/cayley_direct_energy.md';edits[path]=(ROOT/path).read_text().replace('0 notin A','0 in A iff K is even')
    append_once('README.md','## Magnetic-quotient audit (2026-09-05)', '''## Magnetic-quotient audit (2026-09-05)

The [complete derivation](mathematics/magnetic_quotient_semicircle.md) gives an
all-order Weyl trace identity, an explicit antiunitary real gauge, and a
restricted **global** semicircle law for odd compressed observables when
prime subgroup orders satisfy `K -> infinity`, `K=o(log p)`.
This regime is proved impossible for the orders of one fixed hyperbolic cat
map. No microscopic BGS/GOE law or priority claim is asserted.

The [referee audit](record/referee_audit_20260905.md) records independently
reproduced false triple-filter assertions in draft PR #13 and distinguishes
execution coverage from a complete proof audit. The empirical CDF diagnostic
now checks both sides of every jump; its numerical output is regenerated.

Reproduce the new algebra with:

```sh
g++ -std=c++20 -O2 computations/cpp/magnetic_word_verifier.cpp -o /tmp/magnetic_word_verifier
OPENBLAS_NUM_THREADS=1 python computations/verification/magnetic_quotient_regression.py --cpp /tmp/magnetic_word_verifier
python computations/verification/cdf_sup_regression.py
cd formalization && lake build
```

The Lean module contains four finite certificates, not the analytic theorem.
The magnetic publication workflow builds the companion TeX/PDF, exact JSON
certificate and finite global-spectrum illustration from maintained sources.
The source audit explicitly leaves full literature priority open.
''')
    append_once('mathematics/results.md','## Magnetic quotient: restricted global law (2026-09-05)', '''## Magnetic quotient: restricted global law (2026-09-05)

See [the complete proof](magnetic_quotient_semicircle.md). Exact: geometric
antiunitary, orbit-basis equivalence and all-order signed trace histograms.
Derived under explicit hypotheses: quantitative even-moment L2 bounds and
global semicircle convergence for prime K=o(log p). Not derived: fixed-cat-map
or microscopic BGS universality. Equation (21) proves the fixed-map obstruction.
''')
    append_once('record/claim_ledger.md','## Magnetic-quotient claims (2026-09-05)', '''## Magnetic-quotient claims (2026-09-05)

| Claim | Status | Boundary |
|---|---|---|
| Explicit antiunitary and Gauss real gauge | Exact project proof, finite numerical cross-checks | Does not establish GOE universality |
| Signed orbit assembly and all-order Weyl trace identity | Exact project proof; independent Python/C++ histograms | Reference enumeration remains exponential in moment order |
| Reciprocal short-relation rigidity | Proved for prime K, m<K, p^2>m^(K-1) | No polynomial-regime extension asserted |
| Quantitative moment bound and global semicircle law | Complete project derivation, not externally refereed; prime K=o(log p) | Not microscopic BGS; priority not established |
| Fixed-map scope obstruction | Exact growth argument | This regime cannot occur for orders of one fixed hyperbolic integral map |
| Lean magnetic trace checks | Four finite native_decide certificates; compiler execution recorded separately by CI | Not an analytic formalization |
| Triple-resultant filters of draft PR #13 | Necessary divisibility survives; exactness of every triple gcd is false | K=43,p=173 gives 865=5p |

Proof authority for these additions is `mathematics/magnetic_quotient_semicircle.md`.
The earlier ledger remains in force outside these explicitly delimited additions.
''')
    append_once('record/retractions.md','## Empirical CDF and draft triple filters (2026-09-05)', '''## Empirical CDF and draft triple filters (2026-09-05)

The former empirical-CDF supremum omitted left limits at jumps. It could
underestimate the descriptive discrepancy; this is corrected and the spacing
JSON is regenerated. No new spacing-law theorem follows.

Draft PR #13 asserted that each of 96 triple resultant filters equals p.
That is false: K=43,p=173 gives 865=5p. Complete observed sets and the K=29
pair-filter correction are in `referee_audit_20260905.md`. The necessary
p-divisibility argument is not retracted. This does not claim a complete
line-by-line review of that draft's mathematical corpus.
''')
    changed=[]
    for path,new in edits.items():
        target=ROOT/path
        if target.read_text()!=new:target.write_text(new);changed.append(path)
    print('reviewed integration changed:',', '.join(changed) or 'nothing (already integrated)')
if __name__=='__main__':main()
