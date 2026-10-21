#!/usr/bin/env python3
"""Build the cumulative Round 14 Markdown with exact source inclusion."""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCES = ROOT / "research_round14_2026_10_21"
HISTORY = ROOT / "research_history_frozen" / "master_before_round14.md"
TARGET = ROOT / "Spectral_research_master.md"
MANIFEST = ROOT / "spectral_research_master_round14_manifest.json"
BASE_HASH = "ef38464d8e2b6ad3e917547e3437dcd53ed7c28dd39c4818faa29e5eb7cf6d43"
MAIN_NAME = "round14_main_report.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def anchor(path: Path) -> str:
    try:
        label = path.relative_to(SOURCES).with_suffix("").as_posix()
    except ValueError:
        label = path.stem
    stem = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
    suffix = path.suffix.lower().lstrip(".")
    return "r14-source-" + stem + "-" + suffix


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
        language = {".py": "python", ".wl": "wolfram", ".json": "json", ".patch": "diff"}.get(
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

Версия: завершение четырнадцатого исследовательского прохода,
21 октября 2026 года.

**Исходная задача остаётся нерешённой.** Для
\(U_N=e^{i10^{-80}NA_N}M_N\), по всем нечётным \(N\ge3\),
не доказан и не опровергнут \(H_{\rm diag}\).
Первая конкретная невыполненная оценка — формула (1.4)
актуального изложения. Ниже находятся полные доказательства
полученных дополнительных результатов и выполненных попыток.

### Результаты текущего прохода для исходной семьи

Для координатного возврата вычислен строгий предел
\[
\sum_x|U_N(x,x)|^2\longrightarrow
1-\frac{25823\pi^4}{4800000000000}\tau^4+E,\qquad
|E|\le10^{56}\tau^5.
\]
Точные модульные фазы, четыре ветви, все дискретные алиасы
и аналитический остаток включены в доказательство.
Вместе с формулой первого следа это даёт
\[
\liminf\left(|\operatorname{Tr}U_N|^2-
\sum_x|U_N(x,x)|^2\right)\ge200\tau.
\]
Это препятствие поточечной замене общей фазы независимыми
координатными фазами. Фиксированный одношаговый вклад,
нормированный для исходного \(H_2\), всё равно исчезает.

Пусть \(\lambda=3+2\sqrt2\),
\(N_r=(\lambda^r-\lambda^{-r})/(4\sqrt2)\), \(r\ge3\) нечётно.
Для
\[
d_N=\inf_{W\in U(N),\,|z|=1}\|U_N-zWM_NW^*\|
\]
доказано \(d_N=O(1/\log N)\) по всем нечётным размерам и
\[
\liminf_r(\log N_r)d_{N_r}\ge\pi\log\lambda/4>0.
\]
Следовательно, \(d_{N_r}\asymp1/\log N_r\). Это исключает
наследование полного линейного спектра с точностью
\(o(1/N_r)\), но не устанавливает локальной универсальности.

Доказана собственная вставленная асимптотика
\(\operatorname{Tr}(A_NU_N)\) с остатком \(O(N^{-1})\)
и нижней границей \(c_*>11/10\).
Она даёт ненулевую проекцию на полный коммутант
и препятствие полному кограничному устранению физически
масштабированного двухкопийного генератора.
Норма этой проекции не заменяет требуемого знака полной
взвешенной корреляции.

### Что осталось после дальнейших попыток

Полный положительный класс циклически совпадающих
координатных траекторий уже в проходе 5 был просуммирован.
Его вклад продолжает линейную зависимость после \(m=N\);
остальные траектории должны дать определённую отрицательную
константу. Новая одношаговая поправка этого не доказывает.
Одношаговую матричную ошибку можно сделать достаточно малой
для всей суммы \(m<2N\), но её когерентный остаток пока
не оценён.

В параметрическом подходе выполнено полное суммирование
градиента и второй производной при нулевом толчке на
Pell-размерах. Получены сверхполиномиально малый градиент,
расходящееся начальное значение и отрицательная кривизна
порядка не меньше \(N^5/(\log N)^2\).
Неотрицательность полной суммы затем вынуждает положительную
кривизну уже при \(t=O((\log N)^3/N^2)\). Это исключает
продолжение начальной вогнутости до фиксированного \(\tau\),
но значение функционала в физической точке остаётся
неоценённым. Все межблочные остатки и ограничения
аналитического переноса доказаны отдельно.

### Навигация

- [Актуальное изложение, доказательства и первая недоказанная оценка](#r14-source-round14-main-report-md).
- [Спектральное расстояние после сопряжения и поворота](#r14-source-obstruction-r14-original-spectral-orbit-barrier-md).
- [Точный координатный возврат и все алиасы](#r14-source-structural-r14-original-coordinate-phase-bridge-test-md).
- [Коэффициент четвёртого порядка](#r14-source-structural-r14-quartic-return-addendum-md).
- [Вставленный след и двухкопийная проекция](#r14-source-signed-sum-r14-inserted-trace-and-two-copy-coboundary-md).
- [Выполненная попытка на временах порядка N](#r14-source-structural-r14-heisenberg-sum-attempt-md).
- [Полное суммирование градиента и Hessian при нулевом толчке](#r14-source-signed-sum-r14-full-weighted-gradient-and-hessian-attempt-md).
- [Обязательная смена кривизны и аналитический перенос](#r14-source-obstruction-r14-pell-curvature-inflection-and-analytic-window-md).
- [Независимая проверка полного Hessian и его остатка](#r14-source-structural-r14-full-weighted-t0-hessian-audit-md).
- [Независимая проверка перегиба и аналитического ограничения](#r14-source-structural-r14-inflection-and-analytic-window-audit-md).
- [Совместная арифметика tau, размеров и нулей hopping](#r14-source-obstruction-r14-final-arithmetic-tau-pell-attempt-md).
- [Корневая проверка новых и прежних доказательств](#r14-source-root-root-round14-proof-audit-md).
- [Независимая проверка спектрального расстояния](#r14-source-signed-sum-r14-independent-audit-spectral-orbit-barrier-md).
- [Независимая проверка четырёх ветвей](#r14-source-obstruction-r14-independent-coordinate-phase-audit-md).
- [Независимая ручная проверка четвёртого коэффициента](#r14-source-signed-sum-r14-independent-audit-quartic-return-md).
- [Независимая проверка вставки и всех вырождений](#r14-source-obstruction-r14-independent-inserted-trace-audit-md).
- [Независимая проверка актуального изложения и замыкания](#r14-source-structural-r14-main-report-audit-md).
- [Точная область применения внешних теорем](#r14-source-root-root-literature-scope-md).
- [Состояние для продолжения](#r14-source-round14-continuation-ledger-md).
- [Все текущие полные источники](#round14-source-index).
- [Полный предыдущий накопительный текст](#round14-complete-prior-master).
- [Состав и воспроизводимая сборка](#round14-build-integrity).

### Полнота и границы доказанного

Все текущие полные тексты, независимые внутренние аудиты,
точные вычислительные исходники и результаты включены
ниже. Весь предыдущий master сохранён с исходными байтами
ровно один раз.

История содержит также неудачные и условные маршруты.
Их сохранение не превращает отсутствующие оценки в
гипотезы нынешних теорем. Формальная проверка Lean не
проводилась. Точные конечные вычисления проверяют
алгебру и не служат доказательством микроскопического
спектрального предела. Исторический приоритет новых
внутри исследования результатов не заявляется.
"""



def main() -> None:
    historical = HISTORY.read_bytes()
    if sha(historical) != BASE_HASH:
        raise SystemExit("Frozen preceding master has changed.")
    paths = sorted(
        p for p in SOURCES.rglob("*")
        if p.is_file() and p.suffix.lower() in {".md", ".py", ".wl", ".json", ".patch", ".txt"}
    )
    priority = [
        'round14_main_report.md',
        'obstruction/r14_original_spectral_orbit_barrier.md',
        'structural/r14_original_coordinate_phase_bridge_test.md',
        'structural/r14_quartic_return_addendum.md',
        'signed_sum/r14_inserted_trace_and_two_copy_coboundary.md',
        'structural/r14_heisenberg_sum_attempt.md',
        'signed_sum/r14_full_weighted_gradient_and_hessian_attempt.md',
        'obstruction/r14_pell_curvature_inflection_and_analytic_window.md',
        'obstruction/r14_final_arithmetic_tau_pell_attempt.md',
        'root/root_round14_proof_audit.md',
        'structural/r14_main_report_audit.md',
        'structural/r14_full_weighted_t0_hessian_audit.md',
        'structural/r14_inflection_and_analytic_window_audit.md',
        'signed_sum/r14_independent_audit_spectral_orbit_barrier.md',
        'obstruction/r14_independent_coordinate_phase_audit.md',
        'signed_sum/r14_independent_audit_quartic_return.md',
        'obstruction/r14_independent_inserted_trace_audit.md',
        'root/root_literature_scope.md',
        'round14_continuation_ledger.md',
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
        '\n\n<a id="round14-source-index"></a>\n\n## Указатель новых полных источников\n',
        "\n| Источник | SHA256 | Байт |\n| --- | --- | ---: |\n",
    ]
    for item in records:
        name = Path(item["path"]).name
        index.append(f"| [{name}](#{item['anchor']}) | `{item['sha256']}` | {item['bytes']:,} |\n")
    parts = [FRONT, "".join(index)]
    parts.extend(include(p, sources[p]) for p in paths)
    old_text = historical.decode("utf-8")
    parts.append(
        '\n\n---\n\n<a id="round14-complete-prior-master"></a>\n\n'
        "## Полный предыдущий накопительный текст\n\n"
        f"SHA256 исходных байтов: `{BASE_HASH}`. Размер: {len(historical):,} байт.\n\n"
        "<!-- BEGIN COMPLETE PRECEDING MASTER ROUND14 -->\n\n"
        + old_text + ("" if old_text.endswith("\n") else "\n")
        + "\n<!-- END COMPLETE PRECEDING MASTER ROUND14 -->\n"
    )
    metadata = {
        "round": 14,
        "date": "2026-10-21",
        "status": "H_diag and the fixed original pair test remain unproved and undisproved",
        "prior_master": {"sha256": BASE_HASH, "bytes": len(historical)},
        "new_sources": records,
        "builder": record(builder_path, builder),
        "source_bytes_modified_when_included": False,
        "prior_master_inclusion_count": 1,
        "all_current_sources_included_in_unique_delimited_blocks": True,
        "spectral_conjugacy_distance_all_odd_upper_bound": "O(1/log N)",
        "spectral_conjugacy_distance_pell_lower_liminf": "pi*log(3+2sqrt(2))/4",
        "pell_subsequence_seven_adic_valuation_unbounded": True,
        "original_coordinate_return_quartic_coefficient": "-25823*pi^4/4800000000000",
        "original_coordinate_return_remainder": "at most 10^56*tau^5",
        "four_sheet_gauss_identity_all_odd_dimensions_checked": True,
        "all_discrete_aliases_in_coordinate_return_controlled": True,
        "original_common_vs_coordinate_phase_one_step_gap": "liminf at least 200*tau",
        "one_step_gap_is_not_an_H2_counterexample": True,
        "inserted_original_trace_has_own_O_inverse_N_remainder_proof": True,
        "full_commutant_projection_including_all_degeneracies": True,
        "two_copy_physical_generator_coboundary_distance_lower_bound_proved": True,
        "unscaled_coboundary_upper_bound_not_claimed": True,
        "old_physical_pressure_trace_chain_raw_reaudited": True,
        "old_rotation_class_recognized_as_old_and_raw_reaudited": True,
        "required_nonrotation_limit_is_strictly_negative": True,
        "one_step_h2_amplitude_replacement_full_pair_error": "O(1/N)",
        "coherent_sum_of_approximating_matrix_not_evaluated": True,
        "parameter_zero_diagnostics_not_original_tau_results": True,
        "full_parameter_zero_weighted_gradient_and_hessian_sums_proved": True,
        "all_cross_clock_hessian_terms_controlled_without_eigenvalue_branches": True,
        "parameter_curve_inflection_before_every_fixed_positive_tau_proved": True,
        "inflection_does_not_determine_original_fixed_tau_statistic": True,
        "entire_parameter_extension_not_confused_with_uniform_analytic_control": True,
        "full_remaining_original_signed_sum_not_estimated": True,
        "no_original_pair_asymptotic_estimate_obtained_this_round": True,
        "no_original_family_countersequence_obtained": True,
        "H_diag_to_Sine2_closure_checked_including_Haar_normalization": True,
        "tau_and_all_odd_dimension_requirement_unchanged": True,
        "finite_exact_checks_not_asymptotic_evidence": True,
        "historical_novelty_and_formal_Lean_verification_not_claimed": True,
    }
    parts.append(
        '\n\n---\n\n<a id="round14-build-integrity"></a>\n\n'
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
        block_marker = ("<!-- BEGIN INCLUDED SOURCE " + anchor(p) + " -->").encode()
        if result.count(block_marker) != 1:
            raise SystemExit(f"Source block must appear exactly once: {p.name}.")
        if p.read_bytes() != data:
            raise SystemExit(f"Source changed during build: {p.name}.")
        if data and result.count(data) != 1:
            raise SystemExit(f"Source must appear exactly once: {p.name}.")
    if builder_path.read_bytes() != builder or result.count(builder) != 1:
        raise SystemExit("Builder changed or was not included exactly once.")
    if sha(HISTORY.read_bytes()) != BASE_HASH:
        raise SystemExit("Frozen preceding master changed during build.")
    available_anchors = {item["anchor"] for item in records} | {anchor(builder_path)}
    for ref in set(re.findall(rb"\]\(#(r14-source-[a-z0-9-]+)\)", result)):
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
        "all_nonempty_source_bytes_present_once": True,
        "all_source_blocks_present_once_including_empty_logs": True,
        "current_source_anchors_unique_and_verified": True,
        "target_inode_and_identity_preserved": True,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
