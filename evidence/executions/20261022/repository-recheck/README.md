# Repository recheck execution scope

[Review and mathematical limits](../../../../record/audits/repository_recheck_20261022/report.md) ·
[Commands, outputs and source hashes](manifest.json) · [Environment](environment.json)

The final maintenance suite passed **244 tests**. The registry contains
197 claims and 57 external dependencies; no claim state was changed.
The bibliography guard passed 515 mutation tests. Exact imported-source
preservation, generated-section synchronization, local links and bounded
trace/Hessian checks passed. Initial failures are retained as losslessly
compressed logs with both compressed and original byte hashes.

The [manuscript receipt](manuscript_build.json) records three passes, 324 pages,
no unresolved references and no overfull boxes. Six rendered pages were
visually self-reviewed. [Local formula parsing](math_render.json) covers
34,576 expressions; it is not a mathematical proof or a live GitHub-page check.

CMake configuration was attempted and blocked by missing Boost development
files. The separate C++ return-word certificate passed. Full-workspace replay
and Lean compilation were not run. The local Python version differs from CI;
the pinned package set was installed without changing repository requirements.
