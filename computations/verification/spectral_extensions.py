#!/usr/bin/env python3
"""Three separate accepted spectral-extension exact replays.

Modes: cluster (finite input to uniform A_(7*5^e) simplicity), pivots
(four finite U cases), trace (one-step H and trace-square conclusion).
No generic U simplicity, quantitative estimate, BGS or Lean claim.
All scientific arithmetic is exact integer/rational/finite-field or outward
rational interval arithmetic; elapsed time is diagnostic only. Fixed bounds
are documented in each scoped proof. No source-directory outputs are written.
"""
from pathlib import Path
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import resource


def run(mode, root, overlay=None):
    def resolve(rel):
        if overlay is not None and (overlay/rel).is_file():
            return overlay/rel
        return root/rel
    prefix = Path('archive/evidence/spectral_extension_20261006')
    hashes = json.loads(resolve(prefix/'input_hashes.json').read_text())
    for rel, expected in hashes.items():
        if hashlib.sha256(resolve(Path(rel)).read_bytes()).hexdigest() != expected:
            raise RuntimeError('Source identity failed: '+rel)
    name = {'cluster':'cluster', 'pivots':'pivots', 'trace':'trace'}[mode]
    path = Path(__file__).resolve().parent/'spectral_extension'/f'{name}.py'
    spec = importlib.util.spec_from_file_location('spectral_check', path)
    module = importlib.util.module_from_spec(spec)
    exec(compile(path.read_bytes(), str(path), 'exec'), module.__dict__)
    folder = {'cluster':'cluster_inputs', 'pivots':'pivot_inputs', 'trace':'trace_inputs'}[mode]
    first = next(rel for rel in hashes if ('/'+folder+'/') in rel)
    inputs = resolve(Path(first)).parent
    with contextlib.redirect_stdout(io.StringIO()):
        result = module.run(inputs)
    return {'mode':mode, 'result':result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=['cluster','pivots','trace'], default=None)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--overlay', type=Path)
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_AS, (2*1024**3,2*1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (180,180))
    print(json.dumps([run(m,args.root,args.overlay) for m in ([args.mode] if args.mode else ['cluster','pivots','trace'])],indent=2))


if __name__ == '__main__':
    main()
