import os
import re

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "paper",
                 "exact_wd_and_subgroup_moments.tex")
lines = open(P, encoding="utf-8").read().split("\n")
fixed = 0
for i, l in enumerate(lines):
    s = l.rstrip()
    # a table/array row must end with a double backslash; repair single ones
    if s.endswith("\\") and not s.endswith("\\\\") and "&" in s:
        lines[i] = s + "\\"
        fixed += 1
    elif s.endswith("s.e.m.)\\") and not s.endswith("\\\\"):
        lines[i] = s + "\\"
        fixed += 1
open(P, "w", encoding="utf-8").write("\n".join(lines))
print("repaired", fixed, "row terminators")
