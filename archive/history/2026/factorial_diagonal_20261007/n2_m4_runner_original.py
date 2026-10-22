from exact_mixed_fast import physical
from pathlib import Path
import json,time
start=time.monotonic();out={'physical':[physical(2,[2,2],[4],True),physical(2,[2,2]),physical(2,[1,1,2])],'seconds':time.monotonic()-start}
Path('checks/n2_m4_run/results.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',out['seconds'])
