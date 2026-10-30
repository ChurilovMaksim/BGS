"""Static #print axioms coverage check (convention of main ed673b5b):
every `theorem`/`lemma` declared in formalization/Bgs/**/*.lean has a
matching `#print axioms <name>` line in the same file (bare inside the
namespace, or fully qualified after it; matched on the last name component).
Usage: python3 axioms_coverage.py [repo-root]   (exit 1 on any gap)."""
import re, sys, pathlib
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
decl = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*(?:theorem|lemma)\s+([^\s:({\[]+)', re.M)
prt = re.compile(r'^\s*#print\s+axioms\s+(\S+)', re.M)
tot = cov = 0; gaps = []
for f in sorted((root / 'formalization/Bgs').rglob('*.lean')):
    s = re.sub(r'/-.*?-/', '', f.read_text(), flags=re.S)
    s = re.sub(r'--[^\n]*', '', s)
    d = decl.findall(s); p = {x.split('.')[-1] for x in prt.findall(s)}
    tot += len(d)
    for n in d:
        if n.split('.')[-1] in p: cov += 1
        else: gaps.append(f'{f.relative_to(root)}: {n}')
print(f'axioms coverage: {cov}/{tot} theorem/lemma declarations')
for g in gaps: print('MISSING', g)
sys.exit(1 if gaps else 0)
