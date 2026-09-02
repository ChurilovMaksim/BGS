import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "paper",
                 "exact_wd_and_subgroup_moments.tex")
s = open(p, encoding="utf-8").read()
bad = "\\DeclareMathOperator{\tr}{tr}"
good = r"\DeclareMathOperator{\tr}{tr}"
if bad in s:
    s = s.replace(bad, good)
    print("repaired the tab-mangled DeclareMathOperator")
if good not in s:
    s = s.replace(r"\DeclareMathOperator{\Tr}{Tr}",
                  r"\DeclareMathOperator{\Tr}{Tr}" + "\n" + good, 1)
    print("inserted \\tr operator")
open(p, "w", encoding="utf-8").write(s)
print("ok:", good in s)
