from exact_mixed_fast import ports,shared_moments
from pathlib import Path
import json,time
start=time.monotonic()
out={'ports':[ports(3,2,2),ports(3,2,3),ports(3,2,2,True),ports(4,2,2)],'shared_Haar_controls':shared_moments(),'seconds':time.monotonic()-start}
Path('checks/ports_run/results.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',out['seconds'])
