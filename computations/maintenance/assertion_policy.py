#!/usr/bin/env python3
"""Fail-closed static coverage for assertion-dependent maintained computations.

Guards must precede imports and side effects, after docstrings/future imports.
Historical record/ and evidence/ are outside this maintained-code inventory.
Explicit-check-only modules remain usable under optimized Python.
"""
from __future__ import annotations
import ast
from pathlib import Path

MESSAGE = 'Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.'
GUARD = f'if not __debug__:\n    raise RuntimeError({MESSAGE!r})\n'
EXPECTED = ast.dump(ast.parse(GUARD).body[0], include_attributes=False)


def required(path: Path, tree: ast.Module) -> bool:
    return any(isinstance(node, ast.Assert) for node in ast.walk(tree))


def guarded(tree: ast.Module) -> bool:
    body = list(tree.body)
    if (body and isinstance(body[0], ast.Expr)
            and isinstance(body[0].value, ast.Constant)
            and isinstance(body[0].value.value, str)):
        body.pop(0)
    while body and isinstance(body[0], ast.ImportFrom) and body[0].module == '__future__':
        body.pop(0)
    return bool(body and ast.dump(body[0], include_attributes=False) == EXPECTED)


def inventory(root: Path) -> list[tuple[Path, ast.Module]]:
    return [(p.relative_to(root), ast.parse(p.read_text(encoding='utf-8')))
            for directory in ('computations', 'supplement')
            for p in sorted((root / directory).rglob('*.py'))
            if not {'__pycache__', 'tests'}.intersection(p.relative_to(root).parts)]


def protected_entries(root: Path) -> list[tuple[Path, ast.Module]]:
    entries = inventory(root)
    # Conservative static import closure: ambiguous local basenames include all
    # matches. Dynamic imports cannot be exhaustively resolved by this scanner;
    # imported assertion-bearing modules nevertheless enforce their own guard.
    by_name = {}
    for path, tree in entries:
        by_name.setdefault(path.stem, set()).add(path)
        if path.name == '__init__.py':
            by_name.setdefault(path.parent.name, set()).add(path)
    dependencies = {}
    protected = {path for path, tree in entries if required(path, tree)}
    for path, tree in entries:
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                # Importing a.b.c executes each package prefix, not only c.
                for alias in node.names:
                    names.update(alias.name.split('.'))
            elif isinstance(node, ast.ImportFrom):
                names.update((node.module or '').split('.'))
                names.update(alias.name for alias in node.names)
        dependencies[path] = set().union(*(by_name.get(name, set()) for name in names))
        # Package import of this module also executes existing parent inits.
        # Include these conservatively even for direct-file executions.
        dependencies[path].update(parent / '__init__.py' for parent in path.parents
                                  if any(p == parent / '__init__.py' for p, _ in entries))
    while True:
        expanded = protected | {path for path, deps in dependencies.items() if deps & protected}
        if expanded == protected:
            break
        protected = expanded
    return [(path, tree) for path, tree in entries if path in protected]


def violations(root: Path) -> list[str]:
    return [str(path) for path, tree in protected_entries(root) if not guarded(tree)]


if __name__ == '__main__':
    failures = violations(Path(__file__).resolve().parents[2])
    if failures:
        raise SystemExit('Missing early assertion guards: ' + ', '.join(failures))
    print('Assertion-entry static coverage passed (not a mathematical certificate).')
