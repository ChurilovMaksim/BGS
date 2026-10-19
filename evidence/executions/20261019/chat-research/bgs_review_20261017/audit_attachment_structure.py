#!/usr/bin/env python3
"""Read-only attachment audit and a separately validated correction patch."""
from pathlib import Path
from collections import Counter
import ast,difflib,hashlib,json,re,subprocess,sys,tempfile


def sha(data):return hashlib.sha256(data).hexdigest()


def main():
    root=Path(__file__).resolve().parent
    original=Path(sys.argv[1]).resolve()
    data=original.read_bytes();text=data.decode('utf-8')
    assert sha(data)=='4440d3c931195cdd837192f97ad07501a290649d18c5d1f88a4afaac4d111ef4'
    tags=re.findall(r'\\tag\{([^}]+)\}',text)
    blocks=[]
    for match in re.finditer(r'^```python[^\n]*\n([\s\S]*?)^```\s*$',text,re.M):
        code=match.group(1);ast.parse(code)
        blocks.append({'start_line':text.count('\n',0,match.start())+1,
                       'source_sha256':sha(code.encode()),'python_ast':'passed',
                       'executed':False})
    fixed=text.replace('**Latest verified extension:** CE1 and QC1--QC7',
                       '**Latest verified extension:** CL1 and QC1--QC7')
    start=fixed.index('## CE1. Classical absorption Schur complements are uniformly equidistributed')
    fixed=fixed[:start]+re.sub(r'\bCE(\d+)\b',r'CL\1',fixed[start:])
    historical=next(line for line in fixed.splitlines() if line.startswith('Техническая проверка этой редакции охватила 5 779'))
    replacement=('Числа математических фрагментов и сведения о XeLaTeX-компиляции в предыдущем checkpoint относятся к прежней редакции и здесь не считаются сертификатом обновлённого файла. В предоставленном файле текущая структурная проверка насчитала 597 вхождений формульных тегов, 591 различную метку и 12 Python-блоков; повторялись CE1–CE6. В этой исправленной версии классические метки переименованы в CL1–CL17, так что все 597 формульных тегов различны. Все 12 Python-блоков проверены синтаксическим разбором AST без исполнения. XeLaTeX-компиляция текущей версии не повторялась. Структурная проверка и компиляция не заменяют математических доказательств.')
    fixed=fixed.replace(historical,replacement)
    old=r'''Since `(g^k)'=k g^{k-1}g'`, its Dirichlet energy satisfies

$$
\sum_{L\ge1}L|[t^L]g^k|^2
\le k^2\sum_{L\ge1}L|[t^L]g|^2
\le k^2(N-2).
\tag{QC35}
$$

The last inequality follows from the **exact** matrix degree/quantum-Kac identity (AP30), by keeping just the entry `(a,b)`. Finally average over independent uniform relative phases, identifying squared coefficient norms at each total degree. This yields'''
    new=r'''The sharper linear bound already established earlier in this document also applies here. The rational numerator and denominator of `g` have degree at most `N-2`, so the rational degree of `g^k` is at most `k(N-2)`. If it is nonconstant, the area formula with multiplicities and `|g^k|<=1` give

$$
\sum_{L\ge1}L|[t^L]g^k|^2
=\int_{|t|<1}|(g^k)'(t)|^2\frac{dA(t)}\pi
\le k(N-2).
\tag{QC35}
$$

Indeed, almost every target value has at most `k(N-2)` preimages in the disk. For a constant function the integral is zero. Finally average over independent uniform relative phases, identifying squared coefficient norms at each total degree. This yields'''
    assert fixed.count(old)==1
    fixed=fixed.replace(old,new)
    qc=fixed.index('## QC7. New all-moment time-window theorem')
    fixed=fixed[:qc]+fixed[qc:].replace(r'\frac{k^2(N-2)}{L_+}',r'\frac{k(N-2)}{L_+}').replace(r'k=o(\sqrt{\log N})',r'k=o(\log N)')
    fixed_tags=re.findall(r'\\tag\{([^}]+)\}',fixed)
    assert len(fixed_tags)==len(set(fixed_tags))==597
    assert len(blocks)==12
    patch=''.join(difflib.unified_diff(text.splitlines(keepends=True),fixed.splitlines(keepends=True),
                                    fromfile='a/two_channel_transmission(4).md',
                                    tofile='b/two_channel_transmission(4).md'))
    outpath=root/'attachment_corrections.patch';outpath.write_text(patch)
    # Validate the actual patch using the system patch tool on a disposable copy only.
    with tempfile.TemporaryDirectory(prefix='patch_check_',dir=root) as tmp:
        target=Path(tmp)/original.name;target.write_bytes(data)
        run=subprocess.run(['patch','--batch','-p1','-i',str(outpath)],cwd=tmp,capture_output=True,text=True,check=True)
        assert target.read_bytes()==fixed.encode('utf-8')
    assert original.read_bytes()==data
    result={'status':'passed','original_sha256':sha(data),'original_unchanged':True,
            'formula_tag_occurrences':len(tags),'unique_original_formula_tags':len(set(tags)),
            'duplicate_original_tags':{k:v for k,v in Counter(tags).items() if v>1},
            'python_blocks':blocks,'proposed_corrected_unique_tags':len(set(fixed_tags)),
            'patch_sha256':sha(outpath.read_bytes()),'proposed_corrected_file_sha256':sha(fixed.encode()),
            'patch_applied_and_compared_on_temporary_copy':True,
            'latex_compilation_repeated':False,
            'non_claims':['AST parsing does not certify the numerical outputs or mathematics.',
                          'The original attachment and BGS were not edited.']}
    (root/'structure_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','duplicate_tag_names':list(result['duplicate_original_tags']),
                      'python_AST_blocks':len(blocks),'patch_validated_without_editing_original':True}))


if __name__=='__main__':main()
