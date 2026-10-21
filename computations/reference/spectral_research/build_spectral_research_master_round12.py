#!/usr/bin/env python3
"""Build the cumulative Round 12 Markdown with exact source inclusion."""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCES = ROOT / "research_round12_2026_10_21"
HISTORY = ROOT / "research_history_frozen" / "master_before_round12.md"
TARGET = ROOT / "Spectral_research_master.md"
MANIFEST = ROOT / "spectral_research_master_round12_manifest.json"
BASE_HASH = "b8b2741c3b15304e82cef77e0db517a6b9db23ffb22f7e49658b22ee5f900185"
MAIN_NAME = "round12_main_report.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def anchor(path: Path) -> str:
    stem = re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")
    suffix = path.suffix.lower().lstrip(".")
    return "r12-source-" + stem + "-" + suffix


def record(path: Path, data: bytes) -> dict:
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": sha(data),
        "bytes": len(data),
        "anchor": anchor(path),
    }


def include(path: Path, data: bytes) -> str:
    item = record(path, data)
    body = data.decode("utf-8")
    heading = (
        "\n\n---\n\n"
        f'<a id="{item["anchor"]}"></a>\n\n'
        f"## Полный источник: {path.name}\n\n"
        f"Путь исходного текста: `{item['path']}`.\n\n"
        f"SHA256: `{item['sha256']}`. Размер: {item['bytes']:,} байт.\n\n"
        f"<!-- BEGIN INCLUDED SOURCE {item['anchor']} -->\n\n"
    )
    if path.suffix.lower() == ".md":
        rendered = body
    else:
        language = {".py": "python", ".wl": "wolfram", ".json": "json"}.get(
            path.suffix.lower(), "text"
        )
        runs = re.findall(r"`+", body)
        fence = "`" * max(4, 1 + max(map(len, runs), default=0))
        rendered = f"{fence}{language}\n{body}"
        if not rendered.endswith("\n"):
            rendered += "\n"
        rendered += fence + "\n"
    if not rendered.endswith("\n"):
        rendered += "\n"
    return heading + rendered + f"\n<!-- END INCLUDED SOURCE {item['anchor']} -->\n"


FRONT = r"""# Спектральная статистика точной детерминированной семьи

## Единый продолжаемый исследовательский документ

Версия: завершение двенадцатого исследовательского прохода,
21 октября 2026 года.

**Статус: полного решения нет.** Для исходных
\(U_N=e^{i10^{-80}NA_N}M_N\), по всем нечётным \(N\),
не доказан и не опровергнут \(H_{\mathrm{diag}}\).
В этом проходе не получена новая асимптотическая оценка
исходного парного функционала. Один конкретный фиксированный
недоказанный тест приведён в §1 актуального изложения.

### Проверенный дополнительный результат

Для самого исходного толчка доказано, что
\[
\left|\frac1N\operatorname{Tr}e^{itNA_N}\right|
 \le C(N|t|)^{-1/25},\qquad
0<|t|\le10^{-20},\quad N|t|\ge1,
\]
по всем нечётным \(N\). Исходная константа
\(t=10^{-80}\) входит в указанный интервал и не заменяется
параметром, зависящим от размерности. Показатель и интервал
явные; конечный предмножитель \(C\) численно не вычислен.

Доказана также равномерная версия с некоторым положительным
показателем на любом ограниченном интервале физических времён.
Из неё следует
\[
\inf_{|z|=1}\|U_N-zM_N\|_{\mathrm{op}}\longrightarrow2.
\]
Это исключает почти скалярный возврат толчка при выборе
размерностей. Результат относится к самим матрицам после
скалярной поправки, а не к спектральному сравнению после
произвольного сопряжения.

### Полное произведение и неоценённая сумма

При фактическом аргументе \(N\tau\) построено полиномиальное
приближение экспоненты степени \(2(59/50)\tau N+O_K(\log N)\)
с операторной ошибкой \(N^{-K}\). Его подстановка во весь
парный функционал имеет доказанную ошибку \(O(N^{2-K})\).
Оставшаяся конечная знакопеременная сумма не оценена.
Остаток после конечного числа коэффициентов Magnus также
не оценён при физическом параметре.

На Pell-размерностях точно описано первое двухкопийное
модульное совпадение при длине \(\asymp\sqrt N\). Это
ограничение ранее рассмотренного метода; оно не является
контрпримером исходной спектральной задаче.

Общая следовая лемма и nilpotent shear уже встречались в
предыдущих материалах. Их происхождение указано явно.
Историческая новизна стандартных аппроксимаций не заявляется.
Ни один из дополнительных результатов не назван доказательством
универсальности или фундаментальным закрытием задачи.

### Навигация

- [Актуальное изложение и первая недоказанная оценка](#r12-source-round12-main-report-md).
- [Полное доказательство явного показателя 1/25](#r12-source-r12-signed-trace-explicit-kick-exponent-md).
- [Равномерная теорема о физическом толчке](#r12-source-r12-countersequence-kick-recurrence-md).
- [Полный экспоненциальный хвост, CRT и неоценённая сумма](#r12-source-r12-full-product-nonperturbative-attempt-md).
- [Корневая независимая проверка всех основных результатов](#r12-source-root-round12-proof-audit-md).
- [Независимая проверка явного показателя](#r12-source-r12-countersequence-audit-explicit-exponent-md).
- [Независимая проверка полного произведения](#r12-source-r12-countersequence-audit-full-product-md).
- [Независимая проверка актуального изложения](#r12-source-r12-countersequence-audit-main-report-md).
- [Предел прямой координатной попытки](#r12-source-r12-signed-trace-attempt-md).
- [Состояние для следующего продолжения](#r12-source-round12-continuation-ledger-md).
- [Указатель всех текущих источников](#round12-source-index).
- [Весь предыдущий накопительный текст](#round12-complete-prior-master).
- [Состав и воспроизводимая сборка](#round12-build-integrity).

### Полнота и проверяемость

Текущие утверждения стоят первыми. Далее включены все полные
доказательства, независимые внутренние проверки, точные
вычислительные исходники и исходные ответы текущего прохода.
Весь предыдущий единый документ включён ровно один раз,
с сохранением его исходных байтов.

Исторические условные формулировки и неудавшиеся подходы
сохранены как история исследования. Они не превращаются
в скрытые гипотезы текущих теорем. Внутренние проверки не
являются опубликованным рецензированием или формализацией
в Lean. Конечные вычисления не подменяют асимптотического
доказательства.
"""


def main() -> None:
    historical = HISTORY.read_bytes()
    if sha(historical) != BASE_HASH:
        raise SystemExit("Frozen preceding master has changed.")
    paths = sorted(
        p for p in SOURCES.iterdir()
        if p.is_file() and p.suffix.lower() in {".md", ".py", ".wl", ".json"}
    )
    priority = [
        MAIN_NAME, "r12_signed_trace_explicit_kick_exponent.md",
        "r12_countersequence_kick_recurrence.md",
        "r12_full_product_nonperturbative_attempt.md",
        "root_round12_proof_audit.md",
        "r12_countersequence_audit_explicit_exponent.md",
        "r12_signed_trace_kick_audit.md",
        "r12_full_product_audit_kick_recurrence.md",
        "r12_countersequence_audit_full_product.md",
        "r12_countersequence_audit_main_report.md",
        "r12_signed_trace_attempt.md",
        "root_round12_literature_scope.md",
        "round12_continuation_ledger.md", "round12_target_checkpoint.md",
    ]
    if SOURCES / MAIN_NAME not in paths:
        raise SystemExit("Missing current report.")
    rank = {name: i for i, name in enumerate(priority)}
    paths.sort(key=lambda p: (rank.get(p.name, len(priority)), p.suffix != ".md", p.name))
    sources = {p: p.read_bytes() for p in paths}
    for p, data in sources.items():
        data.decode("utf-8")
        if any(c < 32 and c not in (9, 10) for c in data):
            raise SystemExit(f"Unexpected control byte in {p.name}.")
    records = [record(p, sources[p]) for p in paths]
    if len({r["anchor"] for r in records}) != len(records):
        raise SystemExit("Duplicate current source anchors.")
    builder_path = Path(__file__).resolve()
    builder = builder_path.read_bytes()
    index = [
        '\n\n<a id="round12-source-index"></a>\n\n## Указатель новых полных источников\n',
        "\n| Источник | SHA256 | Байт |\n| --- | --- | ---: |\n",
    ]
    for item in records:
        name = Path(item["path"]).name
        index.append(f"| [{name}](#{item['anchor']}) | `{item['sha256']}` | {item['bytes']:,} |\n")
    parts = [FRONT, "".join(index)]
    parts.extend(include(p, sources[p]) for p in paths)
    old_text = historical.decode("utf-8")
    parts.append(
        '\n\n---\n\n<a id="round12-complete-prior-master"></a>\n\n'
        "## Полный предыдущий накопительный текст\n\n"
        f"SHA256 исходных байтов: `{BASE_HASH}`. Размер: {len(historical):,} байт.\n\n"
        "<!-- BEGIN COMPLETE PRECEDING MASTER ROUND12 -->\n\n"
        + old_text + ("" if old_text.endswith("\n") else "\n")
        + "\n<!-- END COMPLETE PRECEDING MASTER ROUND12 -->\n"
    )
    metadata = {
        "round": 12,
        "date": "2026-10-21",
        "status": "H_diag and the fixed original pair test remain unproved and undisproved",
        "prior_master": {"sha256": BASE_HASH, "bytes": len(historical)},
        "new_sources": records,
        "builder": record(builder_path, builder),
        "source_bytes_modified_when_included": False,
        "prior_master_inclusion_count": 1,
        "uniform_bounded_physical_time_single_kick_trace_decay_proved": True,
        "explicit_single_kick_exponent_one_over_25_proved": True,
        "explicit_time_interval_abs_t_le_1e_minus_20": True,
        "trace_bound_prefactor_not_numerically_evaluated": True,
        "original_fixed_tau_included_without_changing_family": True,
        "operator_distance_from_all_scalar_cat_multiples_tends_to_two": True,
        "complete_physical_exponential_polynomial_tail_controlled": True,
        "growing_linear_polynomial_degree_required_in_this_construction": True,
        "fixed_pair_polynomial_replacement_error_O_N_power_2_minus_K": True,
        "full_remaining_signed_sum_not_estimated": True,
        "fixed_order_magnus_remainder_at_physical_argument_not_controlled": True,
        "exact_first_two_copy_pell_alias_at_length_order_sqrt_N": True,
        "auxiliary_clock_coordinate_completion_not_an_original_counterexample": True,
        "no_original_pair_asymptotic_estimate_obtained_this_round": True,
        "no_original_family_countersequence_obtained": True,
        "tau_and_all_odd_dimension_requirement_unchanged": True,
        "finite_exact_checks_not_asymptotic_evidence": True,
    }
    parts.append(
        '\n\n---\n\n<a id="round12-build-integrity"></a>\n\n'
        "## Проверка целостности и воспроизводимая сборка\n\n"
        "Состав текущего прохода и контрольные суммы полных исходников "
        "приведены ниже. При включении исходные байты не изменялись.\n\n"
        "```json\n" + json.dumps(metadata, ensure_ascii=False, indent=2) + "\n```\n"
    )
    parts.append(include(builder_path, builder))
    result = "".join(parts).encode("utf-8")
    if result.count(historical) != 1:
        raise SystemExit("Preceding master must appear exactly once.")
    for p, data in sources.items():
        if p.read_bytes() != data:
            raise SystemExit(f"Source changed during build: {p.name}.")
        if result.count(data) != 1:
            raise SystemExit(f"Source must appear exactly once: {p.name}.")
    if builder_path.read_bytes() != builder or result.count(builder) != 1:
        raise SystemExit("Builder changed or was not included exactly once.")
    if sha(HISTORY.read_bytes()) != BASE_HASH:
        raise SystemExit("Frozen preceding master changed during build.")
    available_anchors = {item["anchor"] for item in records} | {anchor(builder_path)}
    for ref in set(re.findall(rb"\]\(#(r12-source-[a-z0-9-]+)\)", result)):
        if ref.decode() not in available_anchors:
            raise SystemExit(f"Missing source anchor: {ref.decode()}.")
    inode = TARGET.stat().st_ino
    attrs = {name: os.getxattr(TARGET, name) for name in os.listxattr(TARGET)}
    TARGET.write_bytes(result)
    if TARGET.stat().st_ino != inode:
        raise SystemExit("Target inode unexpectedly changed.")
    if any(os.getxattr(TARGET, k) != v for k, v in attrs.items()):
        raise SystemExit("Local target identity metadata unexpectedly changed.")
    metadata["current_master"] = {
        "path": TARGET.name, "sha256": sha(result),
        "bytes": len(result), "lines": result.count(b"\n"),
    }
    MANIFEST.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "file": str(TARGET), "new_source_count": len(records),
        **metadata["current_master"], "prior_master_exactly_once": True,
        "all_source_bytes_present_once": True,
        "current_source_anchors_unique_and_verified": True,
        "target_inode_and_identity_preserved": True,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
