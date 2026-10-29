#!/bin/bash
# isolated Lean build for Line D v2: fresh copy of /workspace/bgs-build/formalization, cache get, build module
set -x
rm -rf /workspace/bgs-lineD/lean_build_v2
cp -a /workspace/bgs-build/formalization /workspace/bgs-lineD/lean_build_v2
cp /workspace/bgs-lineD/lean/LineDCerts.lean /workspace/bgs-lineD/lean_build_v2/Bgs/LineDCerts.lean
cd /workspace/bgs-lineD/lean_build_v2
lake exe cache get > /workspace/bgs-lineD/logs/lean_v2_cache_get.log 2>&1; echo "cache_get exit $?" >> /workspace/bgs-lineD/logs/lean_v2_cache_get.log
( time lake build Bgs.LineDCerts ) > /workspace/bgs-lineD/logs/lean_v2_build.log 2>&1; echo "build exit $?" >> /workspace/bgs-lineD/logs/lean_v2_build.log
sha256sum Bgs/LineDCerts.lean /workspace/bgs-lineD/lean/LineDCerts.lean >> /workspace/bgs-lineD/logs/lean_v2_build.log
grep -nE "sorry|native_decide|admit|implemented_by|extern|unsafe|opaque|^axiom|^import" Bgs/LineDCerts.lean > /workspace/bgs-lineD/logs/lean_v2_grep.log; echo "grep exit $? (1 = nothing found)" >> /workspace/bgs-lineD/logs/lean_v2_grep.log
