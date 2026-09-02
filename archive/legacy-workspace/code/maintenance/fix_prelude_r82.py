"""Corrective pass for repair_paths_r82 (RUN 82).

Three defects of the first pass are repaired here, idempotently:

 1. wrong nesting depth: the prelude was emitted with one `dirname` too few,
    so `_BGS_ROOT` pointed at the *containing* directory instead of the
    workspace root.  The prelude line is recomputed from the file's own
    position (one `dirname` per path component below the root).
 2. a UTF-8 BOM at byte 0 was pushed to line 3 by the insertion, which is a
    hard SyntaxError.  The BOM is stripped.
 3. one implicit string concatenation (`_BGS_ROOT` followed by a raw literal
    on the next line) lost its `+`.

Usage:  py src/maintenance/fix_prelude_r82.py [--apply]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKIP_DIRS = {"__pycache__", ".git"}
PRELUDE_RE = re.compile(r"^_BGS_ROOT = _os\.path\.[^\n]*$", re.M)


def correct_prelude(path: str) -> str:
    rel = os.path.relpath(path, ROOT).replace("\\", "/")
    n = len(rel.split("/"))          # one dirname per component, incl. the file
    expr = "_os.path.abspath(__file__)"
    for _ in range(n):
        expr = "_os.path.dirname(" + expr + ")"
    return "_BGS_ROOT = " + expr


def main() -> int:
    apply = "--apply" in sys.argv
    fixed = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            if not fn.endswith(".py"):
                continue
            path = os.path.join(base, fn)
            with open(path, "r", encoding="utf-8", errors="surrogateescape") as fh:
                src = fh.read()
            if "_BGS_ROOT" not in src:
                continue
            new = src
            want = correct_prelude(path)
            if PRELUDE_RE.search(new):
                new = PRELUDE_RE.sub(lambda _m: want, new, count=1)
            if "\ufeff" in new:
                new = new.replace("\ufeff", "")
            # implicit concatenation left by the first pass
            new = re.sub(r"_BGS_ROOT(\s*\n\s*)r\"", lambda m: "_BGS_ROOT +" + m.group(1) + 'r"', new)
            if new != src:
                fixed.append(os.path.relpath(path, ROOT))
                if apply:
                    with open(path, "w", encoding="utf-8", errors="surrogateescape") as fh:
                        fh.write(new)
    print(f"{'fixed' if apply else 'would fix'} {len(fixed)} files")
    if apply:
        bad = 0
        for base, dirs, files in os.walk(ROOT):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for fn in files:
                if not fn.endswith(".py"):
                    continue
                p = os.path.join(base, fn)
                with open(p, "r", encoding="utf-8", errors="surrogateescape") as fh:
                    txt = fh.read()
                if "_BGS_ROOT" not in txt:
                    continue
                try:
                    compile(txt, p, "exec")
                except SyntaxError as e:
                    bad += 1
                    print("SYNTAX BREAK", os.path.relpath(p, ROOT), e)
        print("compile check over repaired files:", "PASS" if bad == 0 else f"FAIL ({bad})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
