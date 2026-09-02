# Model benchmark comparison evidence (2026-09-01)

## Scope
Requested comparison: `DeepSeek V4 Pro 0813 Max` vs `GPT 5.6 Luna XHigh`.

## Identity / provenance

### DeepSeek
- Official Hugging Face model card: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813
- Official org/repository: `deepseek-ai/DeepSeek-V4-Pro-0813`
- Card states it is the official DeepSeek-V4-Pro release, superseding preview, with DSpark speculative decoding attached.
- Card metadata: `lastModified=2026-08-13T16:28:28Z`, MIT license, `DeepseekV4ForCausalLM`, MoE, FP4 expert dtype / FP8 quantization config.
- Technical report: https://arxiv.org/abs/2606.19348
- Preview card: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro

### GPT Luna
- Hugging Face results card: https://huggingface.co/crosbylegal/gpt-5.6-luna
- Repository owner: `crosbylegal`; no weights; card describes itself as a results-tracking card for an API model.
- Only listed evaluation artifact: `.eval_results/redlinebench.yaml`.
- No official OpenAI page, model weights, architecture, tokenizer, context limit, or standard benchmark suite found for the exact alias.
- External benchmark report link in card: https://intelligence.crosby.ai/benchmark/ (the accessible Crosby page did not display GPT-5.6 Luna; it displayed other model labels and a different `crosby.ai/benchmark` page was not sufficient evidence).
- Reported score in card: RedlineBench `redline_overall = 55.5`.

## DeepSeek-V4-Pro-0813 benchmark table (official card)

Evaluation setup from README: public code-agent tasks use minimal DeepSeek Harness, `reasoning_effort=max`, `temperature=1.0`, `top_p=0.95`; DSBench-FullStack and DSBench-Hard are internal datasets.

| Benchmark | V4-Pro-0813 | V4-Flash-0731 | V4-Pro Preview | GLM-5.2 | Kimi K3 | Opus-4.8 | Fable-5 (fallback) |
|---|---:|---:|---:|---:|---:|---:|---:|
| HLE (without / with tools) | 42.7 / 60.0 | 37.8 / 51.5 | 37.7 / 48.2 | 40.5 / 54.7 | 43.5 / 56.0 | 49.8 / 57.9 | 53.3 / 63.0 |
| Terminal Bench 2.1 | 87.9 | 82.7 | 72.1 | 81.0 | 88.3 | 85.0 | 88.0 |
| NL2Repo | 61.5 | 54.2 | 38.5 | 48.9 | - | 69.7 | - |
| Cybergym | 83.3 | 76.7 | 52.7 | - | 80.0 | 78.3 | 83.1 |
| DeepSWE | 62.7 | 54.4 | 12.8 | 46.2 | 67.5 | 58.0 | 70.0 |
| Toolathlon-Verified | 74.1 | 70.3 | 55.9 | 59.9 | 76.5 | 76.2 | 77.9 |
| Agents' Last Exam | 25.7 | 25.2 | 16.5 | 23.8 | 27.6 | 25.7 | - |
| AutomationBench (Public) | 31.8 | 25.1 | 12.8 | 12.9 | 30.8 | 27.2 | 29.1 |
| DSBench-FullStack (internal) | 71.1 | 68.7 | 41.8 | 61.8 | 73.7 | 71.6 | 77.2 |
| DSBench-Hard (internal) | 67.2 | 59.6 | 31.1 | 54.5 | 63.0 | 71.7 | 68.3 |

## DeepSeek-V4-Pro-Max table from preview technical report card

Source: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro (README lines 130-185).

| Benchmark | Opus-4.6 Max | GPT-5.4 xHigh | Gemini-3.1-Pro High | K2.6 Thinking | GLM-5.1 Thinking | DS-V4-Pro Max |
|---|---:|---:|---:|---:|---:|---:|
| MMLU-Pro (EM) | 89.1 | 87.5 | 91.0 | 87.1 | 86.0 | 87.5 |
| GPQA Diamond (Pass@1) | 91.3 | 93.0 | 94.3 | 90.5 | 86.2 | 90.1 |
| LiveCodeBench (Pass@1) | 88.8 | - | 91.7 | 89.6 | - | 93.5 |
| IMOAnswerBench (Pass@1) | 75.3 | 91.4 | 81.0 | 86.0 | 83.8 | 89.8 |
| SWE Verified (Resolved) | 80.8 | - | 80.6 | 80.2 | - | 80.6 |
| SWE Pro (Resolved) | 57.3 | 57.7 | 54.2 | 58.6 | 58.4 | 55.4 |
| SWE Multilingual (Resolved) | 77.5 | - | - | 76.7 | 73.3 | 76.2 |

## Specs from DeepSeek preview card
- Pro: 1.6T total / 49B activated parameters; Flash: 284B total / 13B activated.
- Context length: 1,000,000 tokens.
- Pro-Max is described as the maximum reasoning-effort mode.
- Suggested max output for high/max: 384K tokens.

## What is directly comparable?
- Nothing in the exact public evidence is a matched benchmark between `DeepSeek V4 Pro 0813 Max` and `GPT 5.6 Luna XHigh`.
- DeepSeek has scores on HLE, Terminal Bench, NL2Repo, Cybergym, DeepSWE, Toolathlon, Agents' Last Exam, AutomationBench and internal DSBench; GPT Luna has one reported RedlineBench score only.
- RedlineBench is a contract-negotiation/legal workflow benchmark; it is not interchangeable with HLE, SWE, MMLU-Pro, GPQA, or coding-agent scores.
- The word `XHigh` is not documented in the GPT Luna results card. DeepSeek's documented effort labels are `low`, `high`, and `max`; therefore `GPT 5.6 Luna XHigh` cannot be mapped to a documented inference setting from the available evidence.

## Search limits and negative evidence
- Hugging Face search returned `deepseek-ai/DeepSeek-V4-Pro-0813` and `crosbylegal/gpt-5.6-luna`.
- Exact GPT Luna identity search produced no authoritative OpenAI result in Google/Bing/DuckDuckGo fetches; GitHub code search API required authorization.
- OpenRouter catalog and Artificial Analysis pages were inaccessible/no exact match in fetches.
- Do not turn these limits into a claim that GPT-5.6 Luna does not exist; only state that its exact provenance and comparable benchmark record are unverified publicly.
