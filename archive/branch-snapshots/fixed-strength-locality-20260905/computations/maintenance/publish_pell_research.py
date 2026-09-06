#!/usr/bin/env python3
"""Idempotent integration of reviewed Pell/Floquet source changes.

This changes source and documentation only. Execution and publication are
separate guarded CI steps; this script never declares that a test passed.
"""
from __future__ import annotations
import ast
from pathlib import Path
import re
import subprocess
import sys
import mpmath as mp

ROOT=Path(__file__).resolve().parents[2]

MARKDOWN_HELPER=r'''
def _floquet_markdown_prose(text: str) -> str:
    import re
    lines=[]
    fence_char=None
    fence_length=0
    for line in text.splitlines(keepends=True):
        match=re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$",line.rstrip("\n"))
        if fence_char is not None:
            if match and match.group(1)[0]==fence_char and len(match.group(1))>=fence_length and not match.group(2).strip():
                fence_char=None
            lines.append("\n")
            continue
        if match and not (match.group(1)[0]=="`" and "`" in match.group(2)):
            fence_char,fence_length=match.group(1)[0],len(match.group(1))
            lines.append("\n")
        else:
            lines.append(line)
    return re.sub(r"(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)"," ","".join(lines),flags=re.S)

'''


def append_once(name: str, marker: str, text: str) -> None:
    path=ROOT/name
    old=path.read_text(encoding='utf-8')
    if marker not in old:
        path.write_text(old.rstrip()+'\n\n'+text.strip()+'\n',encoding='utf-8')


def repair_markdown_audit() -> None:
    path=ROOT/'computations/verification/repository_audit.py'
    source=path.read_text(encoding='utf-8')
    tree=ast.parse(source)
    constants={}
    for node in ast.walk(tree):
        if isinstance(node,ast.Assign) and isinstance(node.value,ast.Constant) and isinstance(node.value.value,str):
            for target in node.targets:
                if isinstance(target,ast.Name): constants[target.id]=node.value.value
    def string_value(node):
        if isinstance(node,ast.Constant) and isinstance(node.value,str): return node.value
        if isinstance(node,ast.Name): return constants.get(node.id,'')
        return ''
    def link_pattern(node):
        pattern=string_value(node)
        return '\\[' in pattern and '\\(' in pattern
    compiled=set()
    for node in ast.walk(tree):
        if isinstance(node,ast.Assign) and isinstance(node.value,ast.Call):
            call=node.value
            if isinstance(call.func,ast.Attribute) and call.func.attr=='compile' and call.args and link_pattern(call.args[0]):
                compiled.update(t.id for t in node.targets if isinstance(t,ast.Name))
    lines=source.splitlines(keepends=True)
    offsets=[0]
    for line in lines: offsets.append(offsets[-1]+len(line))
    def offset(lineno,col):
        # Python AST columns are UTF-8 byte offsets, not Unicode character offsets.
        return offsets[lineno-1]+len(lines[lineno-1].encode('utf-8')[:col].decode('utf-8'))
    patches=[]
    for node in ast.walk(tree):
        if not isinstance(node,ast.Call) or not isinstance(node.func,ast.Attribute): continue
        if node.func.attr not in ('findall','finditer','search'): continue
        arg=None
        if isinstance(node.func.value,ast.Name) and node.func.value.id=='re' and len(node.args)>=2 and link_pattern(node.args[0]):
            arg=node.args[1]
        elif isinstance(node.func.value,ast.Name) and node.func.value.id in compiled and node.args:
            arg=node.args[0]
        if arg is None: continue
        if isinstance(arg,ast.Call) and isinstance(arg.func,ast.Name) and arg.func.id=='_floquet_markdown_prose': continue
        a=offset(arg.lineno,arg.col_offset)
        b=offset(arg.end_lineno,arg.end_col_offset)
        patches.append((a,b,'_floquet_markdown_prose('+source[a:b]+')'))
    if not patches and '_floquet_markdown_prose(' not in source:
        raise RuntimeError('No Markdown-link regex call recognized; refusing a guessed source rewrite')
    for a,b,replacement in sorted(patches,reverse=True): source=source[:a]+replacement+source[b:]
    if 'def _floquet_markdown_prose(' not in source:
        parsed=ast.parse(source)
        first=next(n for n in parsed.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)))
        insert=sum(len(line) for line in source.splitlines(keepends=True)[:first.lineno-1])
        source=source[:insert]+MARKDOWN_HELPER+source[insert:]
    ast.parse(source)
    path.write_text(source,encoding='utf-8')
    namespace={}
    exec(MARKDOWN_HELPER,namespace)
    prose=namespace['_floquet_markdown_prose']
    pattern=r'!?\[[^\]]*\]\(([^)]+)\)'
    assert re.findall(pattern,prose('`Z[T](w_e,w_f)` [real](README.md)\n```\n[x](bad)\n```'))==['README.md']
    assert re.findall(pattern,prose('[broken](missing.md)'))==['missing.md']


def main() -> None:
    subprocess.run([sys.executable,str(ROOT/'computations/maintenance/integrate_magnetic_audit.py')],cwd=ROOT,check=True)
    repair_markdown_audit()
    # Recompute the decimal from the defining absolutely convergent series.
    # This is high-precision arithmetic plus a separate tail estimate, not an
    # interval certificate for floating-point rounding.
    mp.mp.dps=70
    lam=3+2*mp.sqrt(2)
    a=4*mp.pi/(mp.sqrt(2)*(1+mp.sqrt(2)))
    gamma=mp.mpf(3)/2+2*sum(1-mp.cos(a*lam**(-j)) for j in range(40))
    decimal=mp.nstr(gamma,17)
    assert abs(gamma-mp.mpf('5.6121412249647')) > mp.mpf('0.001')
    for name in ('README.md','record/claim_ledger.md','mathematics/results.md',
                 'mathematics/pell_phase_rate.md','mathematics/pell_cat_map_gaussian_blocks.md',
                 'manuscript/pell_gaussian_section.tex'):
        path=ROOT/name
        text=path.read_text(encoding='utf-8')
        text=re.sub(r'5\.612141\d*(?:\.\.\.)?',decimal+'...',text)
        text=text.replace('All operators below preserve the odd subspace R=-1.',
            'The symmetrized observables and spectral projectors preserve the odd subspace R=-1; individual Weyl translations need not.')
        text=text.replace('All operators below preserve the odd subspace f(-x)=-f(x).',
            'The symmetrized observables and spectral projectors preserve the odd subspace f(-x)=-f(x); individual Weyl translations need not.')
        text=re.sub(r'The companion\s+certificate computes rational enclosures for the cosines, proves \(13\) by\s+integer arithmetic, and includes the entire remainder in \(19\)\.',
            'The maintained numerical companion reports high-precision evaluation with a separate analytic tail estimate. It does not certify every floating-point matrix calculation by rational intervals.',text)
        path.write_text(text,encoding='utf-8')
    cmake=ROOT/'CMakeLists.txt'
    text=cmake.read_text(encoding='utf-8')
    for target in ('pell_floquet_pair_verifier','spectral_lattice_clustering'):
        if not re.search(r'add_executable\s*\(\s*'+target+r'\b',text):
            text+='\nadd_executable('+target+' computations/cpp/'+target+'.cpp)\n'
            text+='target_include_directories('+target+' PRIVATE ${Boost_INCLUDE_DIRS})\n'
    cmake.write_text(text,encoding='utf-8')
    cpp=ROOT/'computations/cpp/spectral_lattice_clustering.cpp'
    text=cpp.read_text(encoding='utf-8')
    if '#include <cstdlib>' not in text:
        text=text.replace('#include <cstdint>','#include <cstdint>\n#include <cstdlib>')
    cpp.write_text(text,encoding='utf-8')
    paper=ROOT/'manuscript/arithmetic_cat_map_moments.tex'
    text=paper.read_text(encoding='utf-8')
    anchor=r'\begin{thebibliography}'
    if text.count(anchor)!=1: raise RuntimeError('unexpected bibliography structure')
    for stem in ('pell_gaussian_section','pell_floquet_section'):
        direct=r'\input{'+stem+'.tex}'
        include=r'\IfFileExists{manuscript/'+stem+r'.tex}{\input{manuscript/'+stem+r'.tex}}{'+direct+'}'
        if include not in text:
            text=text.replace(direct+'\n','').replace(direct,'')
            text=text.replace(anchor,include+'\n\n'+anchor)
    if r'\usepackage{graphicx}' not in text:
        package=r'\usepackage{booktabs}'
        if text.count(package)!=1: raise RuntimeError('unexpected package anchor')
        text=text.replace(package,package+'\n'+r'\usepackage{graphicx}')
    graphics=r'\graphicspath{{assets/figures/}{../assets/figures/}{assets/}{../assets/}}'
    if graphics not in text: text=text.replace(r'\begin{document}',graphics+'\n'+r'\begin{document}')
    def wrap_chain(match):
        body=match.group(1)
        if body.count(r'\longrightarrow')<2: return match.group(0)
        body=body.replace('\n'+r'\longrightarrow'+'\n','\n'+r'\\ \downarrow \\'+'\n')
        return '\\[\n'+r'\begin{gathered}'+'\n'+body+'\n'+r'\end{gathered}'+'\n\\]'
    text=re.sub(r'\\\[\n(\\boxed\{.*?)(?:\n\\\])',wrap_chain,text,flags=re.S)
    paper.write_text(text,encoding='utf-8')
    section=ROOT/'manuscript/pell_gaussian_section.tex'
    section.write_text(section.read_text(encoding='utf-8').replace('../assets/figures/',''),encoding='utf-8')
    append_once('README.md','## Floquet resonance and microscopic clustering',r'''
## Floquet resonance and microscopic clustering

The [finite Floquet normal form](mathematics/pell_floquet_normal_form.md) controls the actual kicked propagator in normalized Hilbert--Schmidt norm by `12 epsilon^2/sqrt(K)`. At `epsilon=tau/sqrt(2K)`, its K-th-power spectrum has a wrapped-normal limit. The [resonance-comb theorem](mathematics/pell_resonance_comb.md) proves uniform off-resonant trace decay throughout every bounded window `|t|<=CK`.

The [microscopic concentration theorem](mathematics/pell_microscopic_clustering.md) gives a distinct negative result: if `epsilon_K sqrt(K)->0`, globally unfolded nearest-neighbour spacings of the original odd propagator converge to a point mass at zero, and each fixed microscopic close-pair count diverges. This uses no folded phase assignment and no Gaussian moment limit.

These are project proofs, not priority claims or complete Lean formalizations. The kick's classical strength tends to zero. Positive BGS for fixed classical strength and properly resolved symmetries remains unproved here.

Reproduce the independent finite checks with `python computations/verification/pell_floquet_regression.py --cpp build/pell_floquet_pair_verifier` and `python computations/verification/spectral_lattice_clustering.py --cpp build/spectral_lattice_clustering`. Add `--extended --probes 32` to the former for reproducible FFT trace estimates; their probe RMS bound is not a deterministic confidence interval.
''')
    append_once('record/claim_ledger.md','## Floquet continuation and microscopic concentration, 2026-09-05',r'''
## Floquet continuation and microscopic concentration, 2026-09-05

PROJECT PROOFS: the finite Pell Floquet normal form; the critical wrapped-normal return spectrum; uniform off-resonant decay for bounded t/K; the two-scale one-eigenvalue product limit; the general circle-concentration inequalities; and subcritical globally unfolded spacing collapse with divergent microscopic ordered pair counts. Detailed statements, proofs and exclusions are in the three maintained Floquet/concentration notes.

VERIFICATION SCOPE: finite pair-cardinality tests in different coordinate representations; exact rational/integer concentration checks; dense-versus-FFT operator comparisons; numerical trace diagnostics. Actual execution status is recorded by the workflow manifest, not inferred from the presence of source. Existing Lean checks do not formalize the new analytic limits.

OPEN: fixed nonzero classical perturbation strength, correctly desymmetrized Heisenberg-scale joint trace estimates, local critical-regime universality, and full BGS. A two-scale observation of one eigenvalue is not a two-eigenvalue correlation law.
''')
    append_once('mathematics/results.md','## Floquet continuation: return spectra and local obstruction',r'''
## Floquet continuation: return spectra and local obstruction

- [Finite arithmetic Floquet normal form and wrapped-normal critical law](pell_floquet_normal_form.md).
- [Uniform resonance comb and two-scale one-eigenvalue limit](pell_resonance_comb.md).
- [General spectral concentration criterion and microscopic subcritical clustering](pell_microscopic_clustering.md).

The last result is a negative local-statistics theorem with global mean-spacing normalization; it is not a positive BGS universality theorem. All limits retain their shrinking-kick hypotheses.
''')
    append_once('record/retractions.md','## Pell decimal and publication correction, 2026-09-05',
        '## Pell decimal and publication correction, 2026-09-05\n\n'
        'The previously transcribed decimal 5.6121412249647 for the defined fourth-moment series was incorrect. Re-evaluation of the unchanged series gives '+decimal+'... . The formula and the analytic tail estimate, not the old decimal, are authoritative. The maintained source and manuscript are corrected from the defining series. This high-precision decimal is not relabelled as an interval certificate.\n\n'
        'The earlier publication job stopped before verification at an assumed Markdown-function name. Integration now identifies the actual Markdown-link regex calls through the Python AST, excludes code while retaining a real missing-link control, and refuses an unrecognized structure. A failed historical workflow is not retrospectively marked successful.')
    # Avoid implying that an unintegrated new Lean module has been compiled.
    note=ROOT/'mathematics/pell_floquet_normal_form.md'
    text=note.read_text(encoding='utf-8')
    text=re.sub(r'The Lean module has general cleared-denominator identities for c_j and a\s+finite original-coordinate K=11 certificate\. Its compilation status must\s+be checked separately\. It does not formalize Duhamel estimates, Lemma 2,\s+Wasserstein convergence, or Theorem A\.',
        'The existing Lean finite-word certificates have a narrower scope. New analytic claims here are not declared Lean-formalized: the Duhamel estimate, Gaussian limit, spectral matching and Wasserstein arguments are ordinary proofs. Any added coefficient or pair-support module must have its own successful compilation record before being promoted.',text)
    note.write_text(text,encoding='utf-8')
    print('Reviewed source integration complete; no test or publication status inferred.')


if __name__=='__main__':
    main()
