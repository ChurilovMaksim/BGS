"""Idempotent repair of stale absolute paths (RUN 82).

Rewrites every hard-coded reference to the dead roots

    C:\\Users\\churi\\Desktop\\BGS                              (pre-OneDrive layout)
    C:\\Users\\churi\\Desktop\\BGS\\BGS_portable_20260827\\BGS   (deleted snapshot)

into an expression relative to the file being executed, so the workspace can be
relocated without another repair round.  A prelude

    import os as _os
    _BGS_ROOT = _os.path.dirname(... _os.path.abspath(__file__) ...)

is inserted after the module docstring (AST-located) exactly once per file.

Usage:  py src/maintenance/repair_paths_r82.py [--apply]
Without --apply the script only reports what it would change.
"""
import ast
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEAD = [
    r"C:\Users\churi\Desktop\BGS\BGS_portable_20260827\BGS",
    r"C:\Users\churi\Desktop\BGS",
]
PRELUDE_MARK = "_BGS_ROOT ="
SKIP_DIRS = {"_archive", "__pycache__", ".git"}


def depth_to_root(path: str) -> int:
    """Number of dirname() applications from the file to the workspace root."""
    rel = os.path.relpath(path, ROOT)
    return len(rel.replace("\\", "/").split("/")) - 1


def prelude(d: int) -> str:
    expr = "_os.path.abspath(__file__)"
    for _ in range(d):
        expr = "_os.path.dirname(" + expr + ")"
    return "import os as _os\n_BGS_ROOT = " + expr + "\n"


def insert_line(src: str) -> int:
    """Line index (0-based) at which the prelude may be inserted."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 0
    if tree.body and isinstance(tree.body[0], ast.Expr) and isinstance(
            getattr(tree.body[0], "value", None), ast.Constant) and isinstance(
            tree.body[0].value.value, str):
        return tree.body[0].end_lineno
    return 0


def rewrite(text: str) -> str:
    """Replace r"<dead root>\\rest" literals with _BGS_ROOT + r"\\rest"."""
    for dead in DEAD:
        # r"<dead>"  ->  _BGS_ROOT
        text = text.replace('r"' + dead + '"', "_BGS_ROOT")
        # r"<dead>\rest"  ->  _BGS_ROOT + r"\rest"
        pat = re.compile(r'r"' + re.escape(dead) + r'(\\[^"]*)"')
        text = pat.sub(lambda m: '_BGS_ROOT + r"' + m.group(1) + '"', text)
        # plain (non-raw) string form, backslashes doubled
        dd = dead.replace("\\", "\\\\")
        text = text.replace('"' + dd + '"', "_BGS_ROOT")
        pat2 = re.compile(r'"' + re.escape(dd) + r'((?:\\\\[^"]*))"')
        text = pat2.sub(lambda m: '_BGS_ROOT + "' + m.group(1) + '"', text)
    return text


def main() -> int:
    apply = "--apply" in sys.argv
    changed, scanned = [], 0
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            if not fn.endswith(".py"):
                continue
            path = os.path.join(base, fn)
            if os.path.abspath(path) == os.path.abspath(__file__):
                continue
            scanned += 1
            with open(path, "r", encoding="utf-8", errors="surrogateescape") as fh:
                src = fh.read()
            if not any(d in src for d in DEAD):
                continue
            new = rewrite(src)
            if new == src:
                print("UNMATCHED literal form in", os.path.relpath(path, ROOT))
                continue
            if PRELUDE_MARK not in new:
                lines = new.splitlines(keepends=True)
                at = insert_line(new)
                lines.insert(at, prelude(depth_to_root(path)))
                new = "".join(lines)
            changed.append(os.path.relpath(path, ROOT))
            if apply:
                with open(path, "w", encoding="utf-8", errors="surrogateescape") as fh:
                    fh.write(new)
    print(f"scanned {scanned} .py files; {'repaired' if apply else 'would repair'} "
          f"{len(changed)}")
    for c in changed:
        print("  ", c)
    if apply:
        bad = 0
        for c in changed:
            p = os.path.join(ROOT, c)
            with open(p, "r", encoding="utf-8", errors="surrogateescape") as fh:
                try:
                    compile(fh.read(), p, "exec")
                except SyntaxError as e:
                    bad += 1
                    print("SYNTAX BREAK", c, e)
        print("post-repair compile check:", "PASS" if bad == 0 else f"FAIL ({bad})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
