#!/bin/sh
# Append one false variant at a time to the definitions (theorems stripped) and check that decide rejects it.
cd /workspace/bgs-lineC/lean/controls
python3 - <<'PY'
import re
src=open('/workspace/bgs-lineC/lean/LineCEncounter.lean').read()
pat=r'(/-- [^\n]*-/\n)?theorem (\w+)\s*:([\s\S]*?):= by\s*\n?\s*decide'
base=re.sub(pat,'',src).replace('end Bgs.LineCEncounter','')
ctrls={
 'c1_aut5_11':'theorem bad : autCount 5 = 11 := by decide',
 'c2_ham6_61':'theorem bad : (hamCycles 6).length = 61 := by decide',
 'c3_coeff':'theorem bad : (List.range 296).all (fun j => c1formula ((j : Int) + 5) == -2 * ((j : Int) + 5) ^ 2 + 1) = true := by decide',
 'c4_hyp':'theorem bad : hypCount 7 0 = 2 * 7 := by decide',
 'c5_exact73':'theorem bad : certVal (aggregate 7 2 parts3) = 236 * 6 * 7 := by decide',
 'c6_fig8':'theorem bad : fig8Words 6 3 = 6 * d 3 * d 3 + 1 := by decide',
 'c7_rank2':'theorem bad : countRank2 6 4 = 4 := by decide',
}
for k,v in ctrls.items():
    open(f'{k}.lean','w').write(base+'\n'+v+'\n\nend Bgs.LineCEncounter\n')
PY
for f in c*.lean; do
  if timeout 1200 ~/.elan/bin/lean $f > ${f%.lean}.out 2>&1; then echo "$f ACCEPTED (BAD)"; else echo "$f rejected: $(grep -m1 -o 'error.*' ${f%.lean}.out | cut -c1-90)"; fi
done
