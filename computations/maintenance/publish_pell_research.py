#!/usr/bin/env python3
"""Idempotent, explicit publication edits for the Pell research pass.

This script does not promote finite tests to theorem proofs. Unexpected
manuscript/audit anchors are errors rather than invitations to rewrite files.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def append_once(path: str, marker: str, addition: str) -> None:
    p = ROOT/path
    old = p.read_text(encoding='utf-8')
    if marker not in old:
        p.write_text(old.rstrip()+'\n\n'+addition.strip()+'\n', encoding='utf-8')


MARKDOWN_HELPER = r'''
def markdown_prose(text: str) -> str:
    """Exclude fenced and inline code before checking literal Markdown links."""
    lines = []
    fence_char = None
    fence_length = 0
    for line in text.splitlines(keepends=True):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\n"))
        if fence_char is not None:
            if match and match.group(1)[0] == fence_char and len(match.group(1)) >= fence_length and not match.group(2).strip():
                fence_char = None
            lines.append("\n")
            continue
        if match and not (match.group(1)[0] == "`" and "`" in match.group(2)):
            fence_char, fence_length = match.group(1)[0], len(match.group(1))
            lines.append("\n")
        else:
            lines.append(line)
    return re.sub(r"(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)", " ", "".join(lines), flags=re.S)


def _pell_markdown_parser_regression() -> None:
    pattern = r"!?\[[^\]]*\]\(([^)]+)\)"
    text = "`Z[T](w_e,w_f)` and [real](README.md)\n```text\n[x](not-a-link)\n```\n"
    assert re.findall(pattern, markdown_prose(text)) == ["README.md"]
    assert re.findall(pattern, markdown_prose("[broken](missing.md)")) == ["missing.md"]


_pell_markdown_parser_regression()

'''


def main() -> None:
    # The existing reviewed integration repairs the two-sided empirical-CDF
    # supremum, records the even-order Cayley boundary, and adds status notes.
    subprocess.run([sys.executable, str(ROOT/'computations/maintenance/integrate_magnetic_audit.py')], cwd=ROOT, check=True)
    append_once('README.md', '## Pell-period Gaussian observable blocks', '''
## Pell-period Gaussian observable blocks

The fixed map `T=((3,2),(4,3))` admits a deterministic Pell-period observable-block construction, including composite moduli. The project proof gives a global variance-one Gaussian limit, uniform over odd sectors, with fixed even-moment error `O_r(1/K)+O_r(K^(r+1)/N)`. The fourth moment is `3-gamma/K+O(K^3/N)`, where `gamma=5.6121412249647...`.

See [the complete Pell construction](mathematics/pell_cat_map_gaussian_blocks.md), [the summable-phase rate proof](mathematics/pell_phase_rate.md), and [the independent verifier](computations/verification/pell_gaussian_regression.py). Numerical evidence is in [the reproducible report](evidence/numerical/pell_gaussian_blocks.json).

These are global observable statistics, not microscopic BGS for the propagator. Priority remains unverified; the general limit has not been formalized in Lean. Finite Lean certificates and execution checks have their explicitly narrower scope.
''')
    append_once('record/claim_ledger.md', '## Pell spectral extension, 2026-09-05', '''
## Pell spectral extension, 2026-09-05

Project derivations: the fixed-map Pell observable-block Gaussian limit, a uniformly summable crossing-phase bound below 9, the fixed even-moment rate O_r(1/K), and the explicit fourth-moment correction. Complete arguments are in the two maintained Pell notes. No claim of mathematical priority or complete general Lean formalization is made.

Execution evidence: independent odd orbit matrices, nontrivial sectors, composite N=8119, eigenvalue/matrix-power agreement, exact Pell/unit arithmetic, and numerical phase checks. The numerical decimal for gamma has a separate analytic series-tail bound, not an interval-rounding certificate.

Still unresolved by this pass: microscopic propagator spacing statistics, Heisenberg-scale desymmetrized joint traces, the general Cayley-energy frontier, and full BGS. Execution of all maintained verifiers is not a line-by-line proof audit of every historical draft.
''')
    p = ROOT/'manuscript/arithmetic_cat_map_moments.tex'
    source = p.read_text(encoding='utf-8')
    command = r'\input{pell_gaussian_section.tex}'
    anchor = r'\begin{thebibliography}'
    if source.count(anchor) != 1:
        raise RuntimeError('unexpected manuscript bibliography structure')
    if command not in source or source.index(command) > source.index(anchor):
        source = source.replace(command+'\n', '').replace(command, '')
        source = source.replace(anchor, command+'\n\n'+anchor)
    if r'\usepackage{graphicx}' not in source:
        package = r'\usepackage{booktabs}'
        if source.count(package) != 1:
            raise RuntimeError('unexpected manuscript package anchor')
        source = source.replace(package, package+'\n'+r'\usepackage{graphicx}')
    def wrap_chain(match):
        body = match.group(1)
        if body.count(r'\longrightarrow') < 2:
            return match.group(0)
        body = body.replace('\n'+r'\longrightarrow'+'\n', '\n'+r'\\ \downarrow \\'+'\n')
        return '\\[\n'+r'\begin{gathered}'+'\n'+body+'\n'+r'\end{gathered}'+'\n\\]'
    source = re.sub(r'\\\[\n(\\boxed\{.*?)(?:\n\\\])', wrap_chain, source, flags=re.S)
    p.write_text(source, encoding='utf-8')
    p = ROOT/'mathematics/pell_cat_map_gaussian_blocks.md'
    source = p.read_text(encoding='utf-8').replace(
        'All operators below preserve the odd subspace f(-x)=-f(x).',
        'The symmetrized observables and spectral projectors below preserve the odd subspace f(-x)=-f(x). Individual Weyl translations need not preserve parity.')
    source = source.replace(
        'The companion certificate computes rational upper/lower enclosures for the\ncosine series and the geometric tail, not an uncertified floating-point claim.',
        'The maintained numerical companion computes a high-precision value and a separate analytic series-tail bound. It does not provide interval-certified floating-point rounding or rational upper/lower enclosures.')
    p.write_text(source, encoding='utf-8')
    p = ROOT/'computations/verification/repository_audit.py'
    source = p.read_text(encoding='utf-8')
    if 'def markdown_prose(' not in source:
        anchor = 'def _iter_markdown_targets('
        if source.count(anchor) != 1:
            raise RuntimeError('unexpected Markdown audit function layout')
        source = source.replace(anchor, MARKDOWN_HELPER+anchor)
    corrected = '_iter_markdown_targets(markdown_prose(text))'
    for old in ('_iter_markdown_targets(_markdown_without_code(text))', '_iter_markdown_targets(text)'):
        source = source.replace(old, corrected)
    if corrected not in source:
        raise RuntimeError('Markdown audit call-site was not recognized')
    p.write_text(source, encoding='utf-8')
    print('Pell source, paper, status, and Markdown corrections synchronized.')


if __name__ == '__main__':
    main()
