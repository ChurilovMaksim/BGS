"""Line J integration check for J3-F8: block-basis provenance of the (+-2,16) certificates.
Records the sha256 of J3/logs/blocks16_exact.json (the basis that J3/code/gstates16_block.py loads by relative path for
every build) and checks:
 (1) it equals the author's v1 and v2 manifests;
 (2) gstates16_block.py loads exactly this file;
 (3) all 576 rest certificates are present and certified;
 (4) optional, if the author tree is given as argv[1]: the basis file's mtime precedes every (+-2,16) build log, so no
     build can have used a different basis file at that path.
The builders are not modified, because their code sha256 is recorded in each certificate."""
import hashlib, json, os, sys, glob
here = os.path.dirname(os.path.abspath(__file__)); J3 = os.path.join(here, '..', 'J3')
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
basis = os.path.join(J3, 'logs', 'blocks16_exact.json'); h = sha(basis); ok = True
man = {}
for mf in ('SHA256_J3.txt', 'SHA256_J3_v2.txt'):
    for line in open(os.path.join(J3, mf)):
        parts = line.split()
        if len(parts) == 2 and parts[1].endswith('logs/blocks16_exact.json'): man[mf] = parts[0]
print('blocks16_exact.json sha256', h)
for mf, v in sorted(man.items()):
    print(' manifest', mf, v, 'OK' if v == h else 'MISMATCH'); ok &= (v == h)
ok &= len(man) == 2
src = open(os.path.join(J3, 'code', 'gstates16_block.py')).read()
loads = "os.path.join(here,'../logs/blocks16_exact.json')" in src
print('gstates16_block.py loads ../logs/blocks16_exact.json:', loads); ok &= loads
certs = sorted(glob.glob(os.path.join(J3, 'logs', 'cert', '*_rest.json')))
cert_ok = all(json.load(open(c)).get('certified') is True for c in certs)
print('rest certificates:', len(certs), 'all certified:', cert_ok); ok &= (len(certs) == 576 and cert_ok)
if len(sys.argv) > 1:
    a = sys.argv[1]; tb = os.path.getmtime(os.path.join(a, 'J3', 'logs', 'blocks16_exact.json'))
    builds = glob.glob(os.path.join(a, 'J3', 'logs', 'cert', 'build_*.log'))
    first = min(os.path.getmtime(b) for b in builds)
    print('author tree: basis mtime precedes all %d build logs:' % len(builds), tb < first,
          '(basis %.0f s before the first build log)' % (first - tb)); ok &= (tb < first and len(builds) > 0)
open(os.path.join(J3, 'logs', 'SHA256_blocks16_basis.txt'), 'w').write(
    h + '  logs/blocks16_exact.json  (block basis loaded by code/gstates16_block.py for every (+-2,16) build; J3-F8)\n')
print('ALL_OK' if ok else 'FAIL'); sys.exit(0 if ok else 1)
