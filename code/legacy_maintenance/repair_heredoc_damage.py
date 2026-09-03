"""Repair the control-character damage from the heredoc-fed lemma insertion
(\\begin -> 0x08+egin; \\neq -> newline+eq) in the paper .tex, per AGENTS.md
rule: byte-level repair, written as a FILE not a heredoc."""
import io

P = "paper/exact_wd_and_subgroup_moments.tex"
data = open(P, "rb").read()

# count the damage
bs = data.count(b"\x08")
ff = data.count(b"\x0c")
print("0x08 count:", bs, " 0x0c count:", ff)

# repair: 0x08 + "egin" -> \begin ; 0x08 elsewhere -> \b ; 0x0c -> \f
data = data.replace(b"\x08egin", b"\\begin")
data = data.replace(b"\x08", b"\\b")
data = data.replace(b"\x0c", b"\\f")

# repair \neq damage: a newline immediately followed by "eq" INSIDE math that
# was meant to be \neq — the insertion block only; identify by context:
# the lemma text had "u\neq0" and "v\neq0" — after damage: "u" newline "eq0".
# In the file the pattern is "u\x0a eq0"? Actually python '\neq' -> chr(10)+'eq'.
# Search for the damaged pattern around 'sum_{u' and 'v':
import re
n_before = data.count(b"eq0")
# heuristic: newline directly followed by "eq" where preceded by 'u' or 'v' backslash-less
data2 = data.replace(b"u\x0aeq", b"u\\neq")
data2 = data2.replace(b"v\x0aeq", b"v\\neq")
data2 = data2.replace(b"}\x0aeq", b"}\\neq")
print("eq-damage spots fixed:", n_before)

open(P, "wb").write(data2)
print("repaired; new size", len(data2))

# verify no control chars remain (except the intended \n)
bad = [(i, b) for i, b in enumerate(data2) if b < 9 or (10 < b < 32)]
print("remaining control bytes:", len(bad))
