"""Rebuild the integer certificate from scratch. Run from any directory with Python 3."""
from pathlib import Path
import json
import subprocess
import sys

root=Path(__file__).resolve().parent
data=root/"data";data.mkdir(exist_ok=True)
def run(*args,stdout=None):
    subprocess.run(args,cwd=root,check=True,stdout=stdout)
run(sys.executable,"coefficients.py")
build=root/"build";build.mkdir(exist_ok=True)
binary=build/"trace"
run("g++","-O3","-std=c++17","-ftrapv","trace.cpp","-o",str(binary))
for sector in ("00","01","10","11"):
    dest=data/f"diag{sector}.txt"
    temp=dest.with_suffix(".tmp")
    with temp.open("w") as stream:
        run(str(binary),str(data/f"H{sector}.txt"),stdout=stream)
    temp.replace(dest)
run(sys.executable,"verify.py")
