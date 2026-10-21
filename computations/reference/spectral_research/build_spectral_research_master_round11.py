#!/usr/bin/env python3
"""Build Round 11 as one cumulative Markdown, preserving all source bytes.

The frozen preceding master, each new raw source, and this builder appear
exactly once. No remote operation or account identifier occurs in this code.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCES = ROOT / "research_round11_2026_10_21"
HISTORY = ROOT / "research_history_frozen" / "master_before_round11.md"
TARGET = ROOT / "Spectral_research_master.md"
MANIFEST = ROOT / "spectral_research_master_round11_manifest.json"
BASE_HASH = "fe0812b16e1e559d596e8e848dea5d21cea6cf81aec05f39da7d44fc4bb6d45a"
MAIN_NAME = "round11_main_report.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def anchor(path: Path) -> str:
    stem = re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")
    suffix = path.suffix.lower().lstrip(".")
    return "r11-source-" + stem + "-" + suffix


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

Версия: завершение одиннадцатого исследовательского прохода,
21 октября 2026 года.

**Статус: полного решения нет.** Для исходных
\(U_N=e^{i10^{-80}NA_N}M_N\), по всем нечётным \(N\),
не доказан и не опровергнут \(H_{\mathrm{diag}}\).
В этом проходе не получена новая асимптотическая оценка
исходного парного функционала. Один конкретный недоказанный
фиксированный тест указан с точной нормировкой в §1
актуального изложения.

### Проверенный результат этого прохода

Положим для нечётного \(r\)
\[
x_r+y_r\sqrt2=(1+\sqrt2)^r,\quad N_r=x_ry_r,\quad
c_r=x_r^2+2y_r^2,\quad
X_j=M_{N_r}^jA_{N_r}M_{N_r}^{-j}.
\]
Тогда \(M_{N_r}^{2r}\) скалярна. Доказано для всех
нечётных \(r\ge25\), что полная сумма коммутаторов
\[
\mathcal C_{2,r}=\sum_{0\le i<j<2r}[X_i,X_j]
\]
удовлетворяет
\[
\frac1{N_r}\|\mathcal C_{2,r}\|_{\mathrm{HS}}^2
\ge\frac{81r}{500000}\sin^2(7\pi c_r/N_r).
\]
Это следствие единственности \(8r\) выбранных двухчастотных
разложений за весь период. Доказательство исключает все
потенциальные сокращения в этих коэффициентах, включая
совпадающие времена; оно не является экстраполяцией конечного
перебора.

Доказаны также точная дисперсия полного орбитального среднего,
предел всех фиксированных слов пары генераторов через половину
периода и локальная оценка начальной кривизны для каждого
скалярного возврата при всех нечётных \(N\ge101\).
Общие параметрические уравнения доказаны непосредственно;
их исторический приоритет не заявляется.

### Граница результата

Полная сумма коммутаторов — коэффициент вариационного ряда
при \(s=0\) в параметризации \(U_N(s)=e^{isA_N}M_N\).
Фактический квадратичный коэффициент равен
\(-\mathcal C_{2,r}/2\). Исходная точка задачи
\(s=N10^{-80}\) растёт, и полный остаток ряда там не оценён.
Кроме того, \(\operatorname{Tr}\mathcal C_{2,r}=0\), а
арифметический период имеет порядок \(\log N_r\).
Ни доказательство \(H_{\mathrm{diag}}\), ни допустимая
исходная контрпоследовательность из этих результатов
не получены.

### Навигация

- [Актуальное изложение и первая недоказанная оценка](#r11-source-round11-main-report-md).
- [Полные арифметические доказательства](#r11-source-r11-arithmetic-pell-magnus-md).
- [Точная параметрическая динамика и окно остатка](#r11-source-root-parametric-eigenphase-dynamics-md).
- [Независимая проверка и оценка всех скалярных возвратов](#r11-source-r11-coherent-parametric-audit-md).
- [Независимая проверка полной арифметической суммы](#r11-source-r11-resolvent-audit-arithmetic-md).
- [Независимая проверка актуального изложения](#r11-source-r11-arithmetic-main-report-audit-md).
- [Сводная проверка корневой ветви](#r11-source-root-round11-proof-audit-md).
- [Резольвентный маршрут и неоценённый знаменатель](#r11-source-r11-resolvent-ward-diagonal-route-md).
- [Реестр для следующего продолжения](#r11-source-round11-continuation-ledger-md).
- [Указатель всех новых полных источников](#round11-source-index).
- [Полный предыдущий накопительный текст](#round11-complete-prior-master).
- [Состав и воспроизводимая сборка](#round11-build-integrity).

### Как читать и проверять

Текущие формулировки стоят первыми. Далее включены полные
доказательства, независимые внутренние проверки, точные
вычислительные исходники и исходные ответы. Весь предыдущий
единый документ сохранён ровно один раз без изменения его
исходных байтов. Все текущие источники включены полностью.

Исторические неудавшиеся подходы и условные формулировки
сохранены как история исследования. Они не являются скрытыми
гипотезами новых утверждений. Внутренние проверки не выдаются
за опубликованное рецензирование или формализацию в Lean.
Конечные вычисления не подменяют исходный спектральный предел.
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
        MAIN_NAME, "r11_arithmetic_pell_magnus.md",
        "root_parametric_eigenphase_dynamics.md",
        "r11_coherent_parametric_audit.md", "r11_resolvent_audit_arithmetic.md",
        "r11_arithmetic_main_report_audit.md", "root_round11_proof_audit.md",
        "r11_resolvent_ward_diagonal_route.md", "r11_coherent_checkpoint.md",
        "root_round11_literature_scope.md", "round11_continuation_ledger.md",
        "round11_checkpoint.md",
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
        '\n\n<a id="round11-source-index"></a>\n\n## Указатель новых полных источников\n',
        "\n| Источник | SHA256 | Байт |\n| --- | --- | ---: |\n",
    ]
    for item in records:
        name = Path(item["path"]).name
        index.append(f"| [{name}](#{item['anchor']}) | `{item['sha256']}` | {item['bytes']:,} |\n")
    parts = [FRONT, "".join(index)]
    parts.extend(include(p, sources[p]) for p in paths)
    old_text = historical.decode("utf-8")
    parts.append(
        '\n\n---\n\n<a id="round11-complete-prior-master"></a>\n\n'
        "## Полный предыдущий накопительный текст\n\n"
        f"SHA256 исходных байтов: `{BASE_HASH}`. Размер: {len(historical):,} байт.\n\n"
        "<!-- BEGIN COMPLETE PRECEDING MASTER ROUND11 -->\n\n"
        + old_text + ("" if old_text.endswith("\n") else "\n")
        + "\n<!-- END COMPLETE PRECEDING MASTER ROUND11 -->\n"
    )
    metadata = {
        "round": 11,
        "date": "2026-10-21",
        "status": "H_diag and the fixed original pair test remain unproved and undisproved",
        "prior_master": {"sha256": BASE_HASH, "bytes": len(historical)},
        "new_sources": records,
        "builder": record(builder_path, builder),
        "source_bytes_modified_when_included": False,
        "prior_master_inclusion_count": 1,
        "full_second_commutator_bound_proved_for_all_odd_pell_indices_ge_25": True,
        "full_two_mode_pell_collision_classification_proved_for_odd_indices_ge_11": True,
        "all_odd_N_ge_101_scalar_return_initial_curvature_bound_proved": True,
        "finite_spectral_moments_of_original_U_not_estimated": True,
        "no_original_pair_asymptotic_estimate_obtained_this_round": True,
        "no_original_family_countersequence_obtained": True,
        "second_order_operator_bound_is_not_a_trace_or_H_diag_lower_bound": True,
        "full_remainder_at_physical_s_equals_N_tau_not_controlled": True,
        "tau_and_all_odd_dimension_requirement_unchanged": True,
        "finite_exact_checks_not_asymptotic_evidence": True,
    }
    parts.append(
        '\n\n---\n\n<a id="round11-build-integrity"></a>\n\n'
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
    for ref in set(re.findall(rb"\]\(#(r11-source-[a-z0-9-]+)\)", result)):
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
