# DeepSeek V4 Pro 0813 Max: source audit

**Research date:** 2026-09-01  
**Chat language:** Russian  
**Work-product language:** English  
**Scope:** public, checkable identity, release/version date, official benchmarks, independent evaluations, context, modes, and platform-alias status.

## Executive finding

[PROVEN] The exact string **"DeepSeek V4 Pro 0813 Max"** is not the official model identifier found in the primary sources. The public release/checkpoint is **DeepSeek-V4-Pro-0813**; the API identifier is **deepseek-v4-pro**. `max` is a reasoning-effort setting, not a separately named checkpoint in the current API/catalog documentation.

[PROVEN] The April 2026 technical report uses the compound label **DeepSeek-V4-Pro-Max** to mean **the maximum reasoning-effort mode of DeepSeek-V4-Pro**. This is the likely origin of the queried wording, combined with the later `0813` GA checkpoint name. It should therefore be rendered as a configuration: `DeepSeek-V4-Pro-0813` + `reasoning_effort=max`, not as a distinct model called "0813 Max".

## Primary sources

1. **DeepSeek API Docs: GA release**  
   URL: https://api-docs.deepseek.com/news/news260813  
   Date shown: **2026-08-13**.  
   The GA release was rolled out to app, web, and API; the calling model name remains `deepseek-v4-pro`. The page states three thinking-effort levels: `low`, `high`, and `max`.

2. **DeepSeek API Docs: models and pricing**  
   URL: https://api-docs.deepseek.com/quick_start/pricing  
   Checked: 2026-09-01.  
   The table maps API model `deepseek-v4-pro` to model version **DeepSeek-V4-Pro-0813**; it lists 1M context, maximum 384K output, thinking/non-thinking modes, tool calls, Responses API, Anthropic API, JSON output, chat-prefix completion beta, and FIM beta in non-thinking mode. Current listed peak prices are $1.32 per 1M cached-miss input tokens and $3.96 per 1M output tokens; these prices are operational metadata, not a benchmark result.

3. **Official Hugging Face checkpoint/model card**  
   URL: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813  
   API metadata checked: 2026-09-01.  
   Repository created **2026-08-13 03:05:06 UTC**, last modified **2026-08-13 16:28:28 UTC**, author `deepseek-ai`; revision SHA `72e1d3230f6c080a530b0a1d46f8eb4602340597`. The identifier contains `0813` but **does not contain `Max`**. The card says this is the official DeepSeek-V4-Pro release superseding Preview and includes a DSpark speculative-decoding module.

4. **DeepSeek-V4 technical report (arXiv)**  
   Title: *DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence*  
   URL: https://arxiv.org/abs/2606.19348  
   DOI: https://doi.org/10.48550/arXiv.2606.19348  
   Published/updated record checked: **2026-04-26** (v1).  
   The abstract states: DeepSeek-V4-Pro has 1.6T total / 49B activated parameters; the family supports a one-million-token context; and **DeepSeek-V4-Pro-Max is the maximum reasoning-effort mode of DeepSeek-V4-Pro**. It also claims 27% of V3.2 single-token inference FLOPs and 10% of its KV cache at one-million-token context. These are report-level claims for the V4 family/preview context, not evidence of a separate `0813 Max` checkpoint.

5. **DeepSeek thinking-mode documentation**  
   URL: https://api-docs.deepseek.com/guides/thinking_mode  
   Checked: 2026-09-01.  
   OpenAI control: `reasoning_effort=low/high/max`; Responses API: `reasoning.effort=none/low/high/max`; Anthropic format: `output_config.effort=low/high/max`. Thinking is enabled by default with default effort `high`; the docs map requested `max` to actual `max`. Non-thinking can be disabled with the documented toggle.

6. **Official model collection**  
   URL: https://huggingface.co/collections/deepseek-ai/deepseek-v4  
   Checked: 2026-09-01.  
   The collection exposes separate entries including `DeepSeek-V4-Pro`, `DeepSeek-V4-Pro-DSpark`, and `DeepSeek-V4-Pro-0813`; no official collection entry named `DeepSeek-V4-Pro-0813-Max` was found.

## Official benchmark results

[PROVEN] The official `DeepSeek-V4-Pro-0813` model card reports the following table. The scores are reported as percentages/benchmark scores by the card; the card does not provide a peer-reviewed independent replication.

| Benchmark | DeepSeek-V4-Pro-0813 | Evaluation condition / note |
|---|---:|---|
| HLE, without tools / with tools | 42.7 / 60.0 | Both conditions shown |
| Terminal Bench 2.1 | 87.9 | Agent evaluation |
| NL2Repo | 61.5 | Agent/code evaluation |
| Cybergym | 83.3 | Agent/security evaluation |
| DeepSWE | 62.7 | Agent/code evaluation |
| Toolathlon-Verified | 74.1 | Tool-use evaluation |
| Agents' Last Exam | 25.7 | Agent evaluation |
| AutomationBench (Public) | 31.8 | Public set |
| DSBench-FullStack | 71.1 | Internal test set, marked with dagger |
| DSBench-Hard | 67.2 | Internal test set, marked with dagger |

The card specifies that public code-agent benchmarks used **DeepSeek Harness minimal mode**, `max` reasoning effort, `temperature=1.0`, and `top_p=0.95`. It identifies DSBench-FullStack and DSBench-Hard as internal sets. The card recommends `temperature=1.0`, `top_p=0.95` for agentic scenarios and `top_p=1.0` otherwise; for `high` and `max`, recommended maximum output length is 384K tokens.

[PROVEN] The official API documentation independently confirms the release/version mapping, 1M context, 384K maximum output, and the `low/high/max` mode family, but does **not** publish the benchmark table.

## Independent/public evaluations

[NUM-SUPPORTED, limited] **Lastprismer, DeepSeek V4 Pro Harness Analysis**  
Repository: https://github.com/Lastprismer/deepseek-v4-pro-harness-analysis  
Blog results: https://lastprismer.github.io/blog/deepseek-v4-pro/  
Release/repository dates: **2026-08-28 to 2026-08-29**.  
The study ran a subset of Terminal Bench 2.1: 20 manually selected tasks out of 89, five runs per task per mode, 100 trajectories per mode and 200 total, comparing DeepSeek V4 Pro with DeepSeek Harness minimal versus standard mode. Its stated conclusion is that the two modes did not show a stable score lead on this subset. The author explicitly says the full benchmark was not run, the released repository does not contain complete sessions/raw API returns/task containers/statistical source, and future exact reproduction is not guaranteed. This is useful exploratory evidence about harness sensitivity, not a full independent replication of the official 87.9 score.

[NUM-SUPPORTED, narrow exploratory test] **Karminski scaffold/stop 3x2 validation**  
Repository: https://github.com/karminski/deepseek-v4-pro-0813-scaffold-stop-3x2-validation  
Batch/report dates: **2026-08-15 to 2026-08-16**.  
It tested one `vector-db-bench` task with `deepseek-v4-pro-0813`, three scaffolds, two stop prompts, and three repetitions (18 runs; 17 evaluable for one metric). The visible report states: strict healthy stop 0/17; budget-contained active 10K 7/17; active finish 3/18; four runs reached the target but exhausted the budget. The repository itself notes limited repetitions, possible parallel/QPS effects, a project-specific adapter rather than native DSH, and one-task scope. This supports a narrow stopping-control observation only; it is not a general capability benchmark.

[NUM-SUPPORTED, author-reported and non-peer-reviewed] **QNFO LiveBench-grounded audit**  
Zenodo DOI: https://doi.org/10.5281/zenodo.21920913  
Record/API: https://zenodo.org/api/records/21920913  
Issued/created: **2026-08-13**; author Rowan Brad Quni-Gudzinas / QNFO Research Collective; version v0.2.  
The abstract claims a mathematics score of **95.1 at USD 0.044/run** for “DeepSeek V4 Pro 0813” and describes a LiveBench 2026-06-25 basis. The Zenodo record is publicly checkable and supplies Markdown/HTML/PDF, but this is a single-author self-published audit, not an official DeepSeek benchmark or peer-reviewed replication. The record does not establish that `95.1` is a score for a separately named `0813 Max` model; treat it as an author-reported configuration/result until the underlying LiveBench row, prompt, endpoint, and run data are independently verified.

[OPEN] The public search/API sweep found no peer-reviewed paper or canonical independent leaderboard entry whose exact model identifier is `DeepSeek-V4-Pro-0813-Max`. Crossref and Semantic Scholar returned no reliable exact-match evaluation record; OpenAlex exact search mainly surfaced the QNFO Zenodo records and unrelated/adjacent DeepSeek V4 material. OpenRouter's public catalog endpoint returned HTTP 403 in this environment, so no claim is made about its current catalog contents.

## Configuration summary

- **Checkpoint/release:** `deepseek-ai/DeepSeek-V4-Pro-0813`; GA date 2026-08-13.
- **API alias:** `deepseek-v4-pro` at `https://api.deepseek.com` (OpenAI-compatible) or `https://api.deepseek.com/anthropic` (Anthropic-compatible).
- **Context:** 1,000,000 tokens in official API docs/model-family report.
- **Maximum output:** 384,000 tokens in official API docs.
- **Thinking:** non-thinking and thinking; `low`, `high`, `max` effort. Default thinking effort documented as `high`.
- **Agent benchmark configuration in official card:** DeepSeek Harness minimal, `max`, temperature 1.0, top-p 0.95.
- **Other official features:** tool calls, JSON output, Responses API, Anthropic API, beta chat-prefix completion; FIM beta in non-thinking mode only.
- **Architecture metadata in checkpoint config:** 1.6T total / 49B activated is reported by the technical report for V4-Pro; 1M `max_position_embeddings`; 384 routed experts, six experts per token, 61 hidden layers; FP8 quantization metadata and BF16 torch dtype. These are checkpoint/config metadata, not independent performance measurements.

## Conclusion

[PROVEN] The safest exact designation for the requested object is **DeepSeek-V4-Pro-0813 with `reasoning_effort=max`**. `DeepSeek-V4-Pro-Max` is an official technical-report label for the maximum-effort mode, while `DeepSeek-V4-Pro-0813-Max` is not an independently documented checkpoint or API model identifier in the checked primary sources.

[HEURISTIC] A platform UI may display “DeepSeek V4 Pro 0813 Max” as a convenience label combining model version and effort setting. Without the platform URL or a captured model-list/API response, the specific platform alias cannot be identified further.

## Search coverage and boundaries

Exact and variant searches were run against arXiv API, OpenAlex, Crossref, Semantic Scholar (rate-limited/403), Hugging Face API, GitHub API, official DeepSeek docs, official DeepSeek Hugging Face collection, Zenodo/DataCite, and public provider endpoints. Web search pages were intermittently blocked or challenged. Absence claims above are limited to these public endpoints and the 2026-09-01 snapshot.
