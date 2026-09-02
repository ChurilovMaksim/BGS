# Public evidence review: GPT-5.6 Luna XHigh

Checked: 2026-09-01 (UTC date of this run).
Chat language: Russian. Work-product language: English.

## Executive finding

- [PROVEN] The exact composite string `GPT 5.6 Luna XHigh` / `GPT-5.6 Luna XHigh` was not found in the exact-match searches run against Bing, DuckDuckGo, arXiv, OpenAlex, Crossref, Hugging Face, GitHub repository search, or grep.app. This is a search result, not proof that an undiscoverable private page does not exist.
- [PROVEN] The public materials do contain the identifiers `GPT-5.6 Luna`, `GPT-5.6-Luna`, and the API-style identifier `gpt-5.6-luna`.
- [PROVEN] In the public evidence, `xhigh` is a reasoning-effort / product-configuration label, not part of the Luna model identifier. RuBench reports `Codex + GPT-5.6 Luna (xhigh)` and audits the requested/executing identifier as `gpt-5.6-luna`.
- [HEURISTIC] The safest classification is an undocumented provider/platform alias or API-served model identifier, not a publicly documented OpenAI model name. The external records are evidence that the identifier was accepted by an OpenAI endpoint during the cited runs, but they do not establish architecture, weights, release lineage, or a public model card.

## Official-source check

The following official URLs were checked or attempted on 2026-09-01:

- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/guides/latest-model
- https://developers.openai.com/api/docs/models/compare
- https://platform.openai.com/docs/models
- https://openai.com/

[OPEN] The environment received HTTP 403 / Cloudflare challenge responses for these pages (the API model endpoint also returned `unsupported_country_region_territory`). Therefore no official OpenAI page, official release date, model card, official context limit, official mode list, or official benchmark table for `GPT-5.6 Luna` or `GPT-5.6 Luna XHigh` is claimed here. The links are supplied for direct user verification.

## Direct identifier and configuration evidence

### Independent API package

Ahmed Aly, *GPT-5.6 API Benchmark: Neutral-Spanish Evaluation Suite and Results*, Zenodo record published 2026-08-17, version 1.0.0.

- DOI: https://doi.org/10.5281/zenodo.21978662
- Repository: https://github.com/chatgptenespanol/gpt-5.6-api-benchmark
- README: https://github.com/chatgptenespanol/gpt-5.6-api-benchmark/blob/main/README.md
- Exact config: https://github.com/chatgptenespanol/gpt-5.6-api-benchmark/blob/main/configs/gpt-5.6-luna.json
- Summary: https://github.com/chatgptenespanol/gpt-5.6-api-benchmark/blob/main/results/summary.json
- Source disclosure: https://github.com/chatgptenespanol/gpt-5.6-api-benchmark/blob/main/SOURCES.md

[PROVEN] The released configuration contains:

- `model`: `gpt-5.6-luna`
- `endpoint`: `https://api.openai.com/v1/responses`
- `reasoning.effort`: `low`
- `max_output_tokens`: `800`
- `store`: `false`; `stream`: `false`; no tools

[PROVEN] The released run metadata records HTTP 200 responses for this identifier, for example T01 repetition 1, started 2026-08-17T11:04:32Z, ended 2026-08-17T11:04:34Z, with an OpenAI request ID and `openai-version: 2020-10-01`. This is external run evidence, not an official OpenAI naming declaration.

[PROVEN] Its independent summary reports for Luna: 36 runs, 36 passed runs, 177/180 rules passed (98.3333%), 12/12 stable tasks, zero critical failures, latency p50 2308 ms and p95 6031 ms, and estimated cost USD 0.0113028 for the recorded package summary. The benchmark has 12 synthetic neutral-Spanish tasks, three repetitions per model, and explicitly states that it is independent and not an official OpenAI evaluation. These are package-specific measurements, not universal capability claims.

### RuBench

Evgeny Shilov, *RuBench: A Repository-Level Agentic Coding Benchmark with Natively Authored Russian Task Specifications*, arXiv:2607.06411v2, published 2026-07-07, updated 2026-07-19.

- Abstract: https://arxiv.org/abs/2607.06411
- DOI: https://doi.org/10.48550/arXiv.2607.06411
- Code/data: https://github.com/eugeneshilow/rubench
- Round-2 results: https://github.com/eugeneshilow/rubench/blob/main/1.0/rounds/round-02/RESULTS.md
- Author page: https://vibecoding.ru/rubench

[PROVEN] Round 2 reports `Codex + GPT-5.6 Luna (xhigh)`: pass@1 raw 75.4% over N=23 freshness-gated tasks and three repetitions, median 6.5 minutes per cell; the published honest sensitivity row is 65.2% with pooled Wilson 95% CI [53.4, 75.4]. The reported harness is Codex CLI 0.144.1.

[PROVEN] RuBench says the requested model matched the executing model as `gpt-5.6-luna` in all 69 cells, with no model substitutions. However, its audit found 8/69 HARD contamination cells for Luna, with 7 passes deducted in the honest row, plus two borderline cases. The raw score must not be treated as a clean model-only estimate.

[PROVEN] In this source, `xhigh` is the maximum reasoning-effort setting of the deployed Codex configuration. It is not shown as part of the model identifier, which remains `gpt-5.6-luna`.

### StateM / Terminal-Bench 2.1

Ziheng Qin, Yaxin Lu, Zhangyang Atlas Wang, Kai Wang, *StateM: Reaching 95.3% Raw Accuracy, or a $15 Frontier Run, on Terminal-Bench 2.1 via Harness Scaling*, arXiv:2608.15089v1, published 2026-08-15.

- Abstract: https://arxiv.org/abs/2608.15089
- DOI: https://doi.org/10.48550/arXiv.2608.15089
- Repository: https://github.com/henryqin1997/statem
- Paper PDF: https://henryqin1997.github.io/statem/statem-paper.pdf

[PROVEN] The paper reports that a frozen StateM profile raises `GPT-5.6 Luna` from 76.7% to 85.4% on Terminal-Bench 2.1. This is a combined system result (Codex-based agent plus StateM runtime/runbook), not a benchmark result for the base model alone. The paper explicitly warns that the results do not isolate the runtime from the evolved control profile. It does not establish an XHigh Luna model name, public model card, context window, or release date.

### Zero-Shot Self-Orchestration

Victor Gao et al., *Zero-Shot Self-Orchestration with Ledger-Based Control for Improved LLM Coding Performance*, arXiv:2608.26480v1, published 2026-08-27.

- Abstract: https://arxiv.org/abs/2608.26480
- DOI: https://doi.org/10.48550/arXiv.2608.26480
- The arXiv record is the primary public source; no dedicated experiment repository is claimed here because the paper text checked in this run does not identify one.

[PROVEN] The paper states that `GPT-5.6-Luna` was served on a pinned official OpenAI API backend. On 100 latest hard LiveCodeBench problems, at a 128k cap with thinking on and five paired passes, the reported manager-versus-single improvement is +10.6 percentage points (p=4.6e-4). This evaluates an orchestration scaffold and its token budget, not an isolated model capability. The paper does not use `XHigh` as the Luna model name.

### Additional independent uses

- [PROVEN] *Self-Evolving Code-with-Image Reasoning*, arXiv:2608.11292v1, 2026-08-11, https://arxiv.org/abs/2608.11292, reports GPT-5.6-luna below 30% tool-free, 43% with a bare interpreter, and 67% with self-evolved skills on its CwI-Bench. This is a specific visual/programming benchmark; no XHigh mode or official model card is supplied.
- [PROVEN] *Which Source Wins? Task-Dependent Reliance in Vision-Language Models*, arXiv:2608.17205v1, 2026-08-17, https://arxiv.org/abs/2608.17205, uses GPT-5.6-Luna as a frontier API model for behavioral cross-checks. It is not a general capability leaderboard and does not publish a Luna context limit.
- [PROVEN] *Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered*, arXiv:2608.29464v1, 2026-08-29, https://arxiv.org/abs/2608.29464, uses GPT-5.6-Luna as a transcript judge and reports monitor correlation -0.54. This is evidence of a use in an evaluation pipeline, not a model benchmark.

## Field status

| Requested field | Publicly verified finding |
|---|---|
| Exact name | `gpt-5.6-luna` / `GPT-5.6 Luna` observed; exact `GPT-5.6 Luna XHigh` not found |
| Provider | Independent run records identify the endpoint as OpenAI API; no official model-card attribution verified in this run |
| Release date/version | No official release date found; external records: Zenodo 2026-08-17, arXiv sources 2026-07-19 to 2026-08-29 |
| Official benchmarks | None verified for Luna or Luna XHigh |
| Independent evaluations | Yes; see RuBench, StateM, self-orchestration, CwI-Bench, modality and CoT papers above |
| Context | 128k cap in the self-orchestration experiment; this is an experimental cap, not a verified model maximum. No official context window verified |
| Modes | `xhigh` appears as Codex reasoning effort in RuBench; the API package uses `low`; self-orchestration uses thinking on. No canonical Luna mode taxonomy verified |
| DOI / URLs | DOI and direct URLs listed above |

## Bottom line

[OPEN] No public primary documentation was found for a model/configuration literally named `GPT-5.6 Luna XHigh`. [PROVEN] `gpt-5.6-luna` is a reproducibly observed API-style identifier in independent public artifacts and was reported as served through the OpenAI API. [HEURISTIC] Until an official OpenAI model catalog entry, release note, or model card is available, cite it as an undocumented API/platform alias and always report the complete serving configuration, date, endpoint, reasoning setting, token cap, harness, and benchmark artifact. Do not report the independent numbers above as official OpenAI benchmark results.
