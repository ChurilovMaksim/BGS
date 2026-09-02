# Maintenance

Run `python code/maintenance/repo_health.py` before committing research changes. It checks the canonical file layout, rejects known quarantined/generated paths, rejects old `src/`/`artifacts/` path conventions in active Python code, parses current JSON results and compiles active Python sources without producing bytecode.
