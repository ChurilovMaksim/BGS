#!/bin/bash
# Builds the zres kernel used by cert_class.py with the flags its a-priori error bound assumes,
# and refuses the binary if its disassembly contains any FMA instruction.
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd)
gcc -O3 -march=native -ffp-contract=off -fno-fast-math -fopenmp -o "$here/zres" "$here/zres.c" -lm
n=$(objdump -d "$here/zres" | grep -ciE '\bv?fn?m(add|sub)[0-9a-z]*' || true)
if [ "$n" -ne 0 ]; then echo "FMA instructions found ($n); refusing this build" >&2; rm -f "$here/zres"; exit 1; fi
echo "zres built; 0 FMA instructions"
