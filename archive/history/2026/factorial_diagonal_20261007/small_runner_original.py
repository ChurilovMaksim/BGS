from exact_mixed_fast import physical
from pathlib import Path
import json,time
start=time.monotonic();out={'physical':[physical(2,[1,1],[2],True),physical(2,[1,2],[3],True),physical(2,[1,1]),physical(2,[1,2])],'seconds':time.monotonic()-start}
Path('checks/small_physical_run/results.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',out['seconds'])
