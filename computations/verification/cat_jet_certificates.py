#!/usr/bin/env python3
"""Ten bounded exact cat/jet replays for scoped FM-026 supporting inputs.

No floating diagnostic source is executed. Reviewed modules are isolated in
scratch directories; all original input bytes are verified before use.
Each finite computation supports its separately reviewed uniform argument;
it is not extrapolation to arbitrary N. Rank transfer uses inherited LW.
"""
from pathlib import Path
import argparse
import base64
import contextlib
import gc
import hashlib
import importlib.util
import io
import json
import os
import resource
import tempfile


def run(root):
    config=json.loads((root/'archive/evidence/cat_jet_20261006/input_map.json').read_text())
    outputs={}
    with tempfile.TemporaryDirectory(prefix='bgs-cat-jet-') as directory:
        scratch=Path(directory)
        for group,files in config['groups'].items():
            for rel,h in files.items():
                record=json.loads((root/config['blobs'][h]).read_text())
                data=base64.b64decode(record['payload'])
                if hashlib.sha256(data).hexdigest()!=h:
                    raise RuntimeError('Input identity failed: '+rel)
                p=scratch/group/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
        helpers=None
        for step in config['steps']:
            p=Path(__file__).resolve().parent/'cat_jet'/step['module']
            spec=importlib.util.spec_from_file_location('cat_check',p)
            module=importlib.util.module_from_spec(spec)
            exec(compile(p.read_bytes(),str(p),'exec'),module.__dict__)
            work=scratch/step['group'];work.mkdir(exist_ok=True)
            with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
                local=module.run(work,helpers if step['group']=='newest' else None)
            if step['module']=='newest_replay.py':helpers=local
            outputs[step['group']+'/'+step['result']]=json.loads((work/step['result']).read_text())
            if step['module']!='newest_replay.py':del local
            gc.collect()
    return outputs


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    args=parser.parse_args()
    for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
    resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
    resource.setrlimit(resource.RLIMIT_CPU,(240,240))
    print(json.dumps(run(args.root),indent=2))


if __name__=='__main__':main()
