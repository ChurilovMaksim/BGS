r"""
BGS adapter for the universal churi local-LLM pool.

This module is a thin facade: it re-exports the universal `BgsLocalLLM`
class from `C:\Users\churi\llm-pool\clients\local_client.py` and adds BGS-
specific helpers (e.g. `HeckeStepMutator` for the `hecke_resolvent_m210.py`
evolve loop in RING 1.2). The infrastructure is project-agnostic; BGS
specifics live here.

Routing rules (apply to BGS just as to any other project — see the
universal module docstring for the full contract):

  - mutator / refuter / synth → local pool (3 slots, 8 GB RAM, churi).
  - scout / literature-miner / prover / hypothesis-generator / mathematician /
    physicist / numerical-runner / algorithm-evolver (coordinator) / reviewer /
    synthesizer (for top-venue polish) → cloud subagent system
    (`task(agent="task" | "scout" | "librarian" | "reviewer", ...)` with
    role definition from skill://discovery-subagents).

The local pool must NEVER be used for load-bearing math, formal proofs,
or literature synthesis. The cloud frontier models beat any 3-8B local model
on those tasks; the local pool is a latency weapon for batch operations only.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Locate the universal client. We add the directory to sys.path so that
# `from local_client import BgsLocalLLM` works in any project that drops
# this adapter in their src tree. The pool itself is at C:\Users\churi\llm-pool\.
_POOL_CLIENTS = Path(r"C:\Users\churi\llm-pool\clients")
if str(_POOL_CLIENTS) not in sys.path:
    sys.path.insert(0, str(_POOL_CLIENTS))

# Re-export the universal class. Importing it under its original name keeps
# the surface area stable for any BGS-side callers and matches the docstring
# at the top of the file.
from local_client import (  # type: ignore
    BgsLocalLLM,
    Role,
    SLOTS,
    LocalLLMConfig,
    DEFAULT_MODEL_NAME,
)

__all__ = [
    "BgsLocalLLM",
    "Role",
    "SLOTS",
    "LocalLLMConfig",
    "DEFAULT_MODEL_NAME",
    "HeckeStepMutator",
]


class HeckeStepMutator:
    """
    BGS-specific convenience wrapper for the RING 1.2 Hecke-symmetrization
    evolve loop. Holds a `mutator` slot, generates N candidate perturbations
    of a candidate Python snippet, and returns them as a list of strings.

    Usage in `src/hecke_resolvent_m210.py` (or successor):
        m = HeckeStepMutator()
        candidates = m.mutate(candidate_src, n=4)
    """

    def __init__(self, timeout_s: int = 120) -> None:
        self._llm = BgsLocalLLM(role="mutator", timeout_s=timeout_s)

    def alive(self) -> bool:
        return self._llm.alive()

    def mutate(self, snippet: str, n: int = 4) -> list[str]:
        return self._llm.code_mutate(snippet, n=n)


if __name__ == "__main__":
    # `python -m src.llm.local_client` — diagnostics.
    import json
    report = {}
    for role in ("mutator", "refuter", "synth"):
        c = BgsLocalLLM(role=role, timeout_s=15)
        report[role] = {"alive": c.alive(), "port": SLOTS[role]}
    print(json.dumps(report, indent=2))
