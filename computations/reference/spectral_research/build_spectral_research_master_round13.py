#!/usr/bin/env python3
"""Build the cumulative Round 13 Markdown with exact source inclusion."""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCES = ROOT / "research_round13_2026_10_21"
HISTORY = ROOT / "research_history_frozen" / "master_before_round13.md"
TARGET = ROOT / "Spectral_research_master.md"
MANIFEST = ROOT / "spectral_research_master_round13_manifest.json"
BASE_HASH = "10b90c7d12668cd7327bcc08bda292f4c7d6cf82218ee95d5d4f7603fac86cef"
MAIN_NAME = "round13_main_report.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def anchor(path: Path) -> str:
    try:
        label = path.relative_to(SOURCES).with_suffix("").as_posix()
    except ValueError:
        label = path.stem
    stem = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
    suffix = path.suffix.lower().lstrip(".")
    return "r13-source-" + stem + "-" + suffix


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

Версия: завершение тринадцатого исследовательского прохода,
21 октября 2026 года.

**Полного решения нет.** Для исходных
\(U_N=e^{i10^{-80}NA_N}M_N\), по всем нечётным \(N\),
не доказан и не опровергнут \(H_{\rm diag}\).
Один конкретный фиксированный парный тест, который всё ещё
не оценён, приведён в §1 актуального изложения.
Область исходной задачи не уменьшалась.

### Новые результаты для исходной семьи

Получена явная асимптотика первого следа с остатком \(O(N^{-1})\):
\[
\operatorname{Tr}U_N=
\zeta_N\left[
\mathsf A e^{i(9/10)\tau N}
+\mathsf B e^{-i\pi N/2}e^{-i(11/10)\tau N}
\right]+O(N^{-1}),
\]
где все коэффициенты точно определены в актуальном изложении.
В частности,
\[
\liminf_{N\ {\rm odd}}|\operatorname{Tr}U_N|
\ge1+\frac{12297\pi}{250}\tau>1.
\]
Это результат для фиксированного времени. Его вклад в
исходный парный функционал имеет порядок \(N^{-2}\) и
не опровергает требуемого предела.

Полностью вычислены действия шестнадцати защищённых
периодических точек. Различные примитивные циклы действительно
имеют совпадающие действия при исходной фиксированной
\(\tau\). Однако сумма их **полных точных следовых слагаемых**,
со всеми поперечными поправками, удовлетворяет
\[
|Q_{m,N}^{\rm full}|\le20(83/200)^m
\quad\text{для всех }m\ge1
\]
с единым достаточно большим порогом по нечётному \(N\).
Удаление этих слагаемых меняет любой соответствующий
парный функционал с ограниченными весами на \(O(N^{-1})\).
Все перекрёстные члены с остальным следом включены.

Для этого усиления не используются старое ранговое
расщепление и разложение скалярного модуля. Применяется
точное секторное произведение и равномерная одношаговая
оценка в следовой норме. Оставшаяся сумма по остальным
орбитам не оценена.

### Ограничение испробованного коэффициентного метода

Вспомогательный множитель \(K_N=M_N^*\) имеет
Weyl-коэффициенты постоянного модуля \(1/N\), удовлетворяет
точной унитарности и обладает глобально равномерным
предельным спектром; при этом \(K_NM_N=I\).
Тем самым одних этих свойств недостаточно для требуемой
локальной статистики произведения. Это не пример с
предписанным генератором и не опровержение исходного
\(H_{\rm diag}\).

Историческая новизна методов и фундаментальное закрытие
задачи не заявляются. Равновесные прямые и отмеченные
гессианы, известные внутри данного исследования с прохода 2,
не представлены как новые открытия прохода 13.

### Навигация

- [Актуальное изложение и первая недоказанная оценка](#r13-source-round13-main-report-md).
- [Полное доказательство действий и первого следа](#r13-source-orbit-correlations-protected-actions-and-one-step-trace-md).
- [Полные защищённые слагаемые при всех временах](#r13-source-root-exact-protected-sector-removal-md).
- [Точный контртест коэффициентной импликации](#r13-source-signed-sum-r13-exact-l2-resummation-test-md).
- [Корневая проверка результатов и зависимостей](#r13-source-root-root-round13-proof-audit-md).
- [Независимая проверка действий и следа](#r13-source-signed-sum-r13-independent-audit-protected-orbits-md).
- [Независимая проверка всех времён](#r13-source-counterexample-r13-audit-full-sector-removal-md).
- [Независимая проверка коэффициентного контртеста](#r13-source-counterexample-r13-audit-l2-resummation-test-md).
- [Независимая проверка актуального отчёта](#r13-source-orbit-correlations-r13-audit-main-report-md).
- [Что осталось в отрицательном маршруте](#r13-source-counterexample-r13-counterexample-attempt-md).
- [Точный объём проверки внешних теорем](#r13-source-root-root-literature-scope-md).
- [Состояние для следующего продолжения](#r13-source-round13-continuation-ledger-md).
- [Указатель всех текущих источников](#round13-source-index).
- [Весь предыдущий накопительный текст](#round13-complete-prior-master).
- [Состав и воспроизводимая сборка](#round13-build-integrity).

### Полнота и границы проверки

Все текущие полные источники, независимые внутренние
проверки и точные вычислительные исходники включены ниже.
Весь предыдущий накопительный текст сохранён с его
исходными байтами ровно один раз.

Актуальные выводы сформулированы перед историей.
Исторические условные формулировки и неудавшиеся попытки
сохраняются как запись исследования и не становятся
скрытыми предпосылками нынешних теорем. Согласие
внутренних проверяющих не заменяет записанных доказательств.
Формальная верификация Lean не проводилась; конечные
рациональные проверки не являются свидетельством
асимптотической универсальности.
"""


def main() -> None:
    historical = HISTORY.read_bytes()
    if sha(historical) != BASE_HASH:
        raise SystemExit("Frozen preceding master has changed.")
    paths = sorted(
        p for p in SOURCES.rglob("*")
        if p.is_file() and p.suffix.lower() in {".md", ".py", ".wl", ".json"}
    )
    priority = [
        MAIN_NAME,
        "orbit_correlations/protected_actions_and_one_step_trace.md",
        "root/exact_protected_sector_removal.md",
        "signed_sum/r13_exact_l2_resummation_test.md",
        "root/root_round13_proof_audit.md",
        "signed_sum/r13_independent_audit_protected_orbits.md",
        "counterexample/r13_audit_full_sector_removal.md",
        "counterexample/r13_audit_l2_resummation_test.md",
        "orbit_correlations/r13_audit_main_report.md",
        "counterexample/r13_counterexample_attempt.md",
        "root/root_literature_scope.md",
        "orbit_correlations/literature_scope.md",
        "round13_continuation_ledger.md",
    ]
    if SOURCES / MAIN_NAME not in paths:
        raise SystemExit("Missing current report.")
    rank = {name: i for i, name in enumerate(priority)}
    paths.sort(key=lambda p: (rank.get(p.relative_to(SOURCES).as_posix(), len(priority)), p.suffix != ".md", p.relative_to(SOURCES).as_posix()))
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
        '\n\n<a id="round13-source-index"></a>\n\n## Указатель новых полных источников\n',
        "\n| Источник | SHA256 | Байт |\n| --- | --- | ---: |\n",
    ]
    for item in records:
        name = Path(item["path"]).name
        index.append(f"| [{name}](#{item['anchor']}) | `{item['sha256']}` | {item['bytes']:,} |\n")
    parts = [FRONT, "".join(index)]
    parts.extend(include(p, sources[p]) for p in paths)
    old_text = historical.decode("utf-8")
    parts.append(
        '\n\n---\n\n<a id="round13-complete-prior-master"></a>\n\n'
        "## Полный предыдущий накопительный текст\n\n"
        f"SHA256 исходных байтов: `{BASE_HASH}`. Размер: {len(historical):,} байт.\n\n"
        "<!-- BEGIN COMPLETE PRECEDING MASTER ROUND13 -->\n\n"
        + old_text + ("" if old_text.endswith("\n") else "\n")
        + "\n<!-- END COMPLETE PRECEDING MASTER ROUND13 -->\n"
    )
    metadata = {
        "round": 13,
        "date": "2026-10-21",
        "status": "H_diag and the fixed original pair test remain unproved and undisproved",
        "prior_master": {"sha256": BASE_HASH, "bytes": len(historical)},
        "new_sources": records,
        "builder": record(builder_path, builder),
        "source_bytes_modified_when_included": False,
        "prior_master_inclusion_count": 1,
        "original_one_step_trace_asymptotic_error_O_inverse_N_proved": True,
        "explicit_strict_one_step_trace_liminf_proved": True,
        "one_step_remainder_prefactor_not_numerically_evaluated": True,
        "protected_sixteen_point_actions_exactly_enumerated": True,
        "distinct_primitive_action_phase_coincidences_proved": True,
        "full_protected_trace_terms_including_all_transverse_terms_bound": "20*(83/200)^m",
        "full_protected_term_bound_all_positive_integer_times": True,
        "single_dimension_threshold_independent_of_iterate_length": True,
        "all_original_pair_cross_terms_retained": True,
        "bounded_weight_termwise_difference_series_absolutely_summable": True,
        "no_subtraction_of_unproved_convergent_separate_infinite_sums": True,
        "norm_and_flatness_only_implication_refuted_by_auxiliary_M_adjoint": True,
        "auxiliary_countertest_is_not_an_original_counterexample": True,
        "full_remaining_original_signed_sum_not_estimated": True,
        "no_original_pair_asymptotic_estimate_obtained_this_round": True,
        "no_original_family_countersequence_obtained": True,
        "tau_and_all_odd_dimension_requirement_unchanged": True,
        "finite_exact_checks_not_asymptotic_evidence": True,
        "historical_novelty_and_formal_Lean_verification_not_claimed": True,
    }
    parts.append(
        '\n\n---\n\n<a id="round13-build-integrity"></a>\n\n'
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
    for ref in set(re.findall(rb"\]\(#(r13-source-[a-z0-9-]+)\)", result)):
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
