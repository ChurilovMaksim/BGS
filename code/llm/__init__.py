"""
BGS local-LLM integration (RING 1.2 Hecke evolve loop only).

Thin adapter over the universal `C:\Users\churi\llm-pool\clients\local_client.py`.
The local pool serves ONLY the three roles declared there. All other BGS
work — proof, literature, hypothesis, math, physics, numerics, review,
synthesis — routes through the OMP cloud subagent system
(`task(agent=...)` with role definitions from skill://discovery-subagents).
"""
from .local_client import (
    BgsLocalLLM,
    HeckeStepMutator,
    Role,
    SLOTS,
    LocalLLMConfig,
    DEFAULT_MODEL_NAME,
)

__all__ = [
    "BgsLocalLLM",
    "HeckeStepMutator",
    "Role",
    "SLOTS",
    "LocalLLMConfig",
    "DEFAULT_MODEL_NAME",
]
