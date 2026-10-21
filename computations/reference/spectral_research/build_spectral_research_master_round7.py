#!/usr/bin/env python3
"""Build the single cumulative Markdown without altering frozen source bytes.

Only standard-library operations are used. The complete preceding master is
included once; new proof notes, audits, and code are included once each.
This script performs no remote operation and contains no account identifiers.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCES = ROOT / "research_round7_2026_10_21"
HISTORY = ROOT / "research_history_frozen" / "master_before_round7.md"
TARGET = ROOT / "Spectral_research_master.md"
MANIFEST = ROOT / "spectral_research_master_round7_manifest.json"
BASE_HASH = "3534e4d7aa97c2f8621050248652363c639aeedf723f8b7fe7a971dc01ac2302"
MAIN_NAME = "round7_main_report.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def anchor(path: Path) -> str:
    return "r7-source-" + re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")


def fence_for(text: str) -> str:
    runs = re.findall(r"`+", text)
    return "`" * max(4, 1 + max(map(len, runs), default=0))


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
        delimiter = fence_for(body)
        rendered = f"{delimiter}{language}\n{body}"
        if not rendered.endswith("\n"):
            rendered += "\n"
        rendered += delimiter + "\n"
    if not rendered.endswith("\n"):
        rendered += "\n"
    return heading + rendered + f"\n<!-- END INCLUDED SOURCE {item['anchor']} -->\n"


def main() -> None:
    historical = HISTORY.read_bytes()
    if sha(historical) != BASE_HASH:
        raise SystemExit("The frozen preceding master has changed; aborting.")

    all_paths = sorted(
        p for p in SOURCES.iterdir()
        if p.is_file() and p.suffix.lower() in {".md", ".py", ".wl", ".json"}
    )
    main_path = SOURCES / MAIN_NAME
    if main_path not in all_paths:
        raise SystemExit("Missing current report.")

    priority = ["round7_main_report.md","r7_return_uniform_stationary_dephasing.md","r7_return_all_fixed_powers_phase_separation.md","r7_return_quantitative_sheet_separation.md","root_original_intensity_at_prescribed_phase.md","r7_original_full_cyclicity_laurent_unit.md","r7_original_two_endpoint_layers.md","root_original_every_power_minors.md","r7_original_all_odd_component_minors.md","r7_return_schur_discriminant_identity.md","root_unipotent_flat_clock.md","r7_return_generic_microperturbation.md","root_stationary_projection_countermodel.md","root_round7_proof_audit.md","r7_audit_stationary_dephasing.md","r7_audit_all_fixed_powers.md","r7_audit_full_cyclicity.md","r7_original_intensity_jacobian_audit.md","r7_original_every_power_minors_audit.md","r7_audit_countermodel.md","r7_audit_physical_fixed_powers49.md","root_literature_applicability.md","round7_continuation_ledger.md","round7_research_checkpoint.md","r7_return_singer_research_checkpoint.md"]
    rank = {name: i for i, name in enumerate(priority)}
    all_paths.sort(key=lambda p: (rank.get(p.name, len(priority)), p.suffix != ".md", p.name))
    data_by_path = {p: p.read_bytes() for p in all_paths}
    for p, data in data_by_path.items():
        if any(b < 32 and b not in (9, 10) for b in data):
            raise SystemExit(f"Unexpected control byte in current source: {p.name}")
    records = [record(p, data_by_path[p]) for p in all_paths]

    front = r"""# Спектральная статистика точной детерминированной семьи

## Единый продолжаемый исследовательский документ

Версия: завершение седьмого исследовательского прохода, 21 октября 2026 года.

**Статус: полного решения пока нет.** Для исходных
\(U_N=e^{i10^{-80}NA_N}M_N\), по всем нечётным \(N\),
не доказан и не опровергнут \(H_{\mathrm{diag}}\).
Не предъявлена допустимая исходная контрпоследовательность.
Первая конкретная недоказанная оценка выделена в §10
актуального изложения: один фиксированный допустимый парный тест.

### Новые доказанные результаты

Для исходной семьи по всем нечётным размерам получены:

- сходимость в операторной норме вероятностной матрицы
  каждой фиксированной физической степени к гладкому
  классическому ядру;
- нормовая сходимость стационарной проекции двойного
  оператора, сжатой на координатную диагональ, к проекции
  на константы;
- следствия для произвольного выбора собственного базиса
  и малых сингулярных чисел дополнения \(I-S_N\);
- ненулевость миноров с произвольными физическими столбцами
  и строками внутри одной компоненты Якоби.

Для исходных размеров \(7\nmid N\) дополнительно доказаны:

- обратимость якобиана характеристических коэффициентов
  в исходной точке координатных фаз, простой спектр
  и обратимость матрицы интенсивностей;
- полная цикличность каждой физической координаты;
- ненулевость всех физических миноров всех ненулевых
  целых степеней \(U_N\);
- точные абсолютно сходящиеся знаковые суммы первых
  возвращений и их производных.

Доказано также общее конечномерное тождество, связывающее
определитель дополнения двойного оператора, диагональные
наблюдения и спектральный дискриминант.

Области действия различаются и нигде не объединяются
без доказательства. Ненулевость не объявляется количественной
оценкой, а все фиксированные времена не заменяют время,
растущее вместе с \(N\). Классическая эргодичность применяется
только после проверки гипотез точной опубликованной теоремы
и не подменяет спектральное сокращение.

### Проверенная граница достаточности

Включена отдельная детерминированная конечнополевая
последовательность и её алгебраическое возмущение.
Она сочетает многие из найденных свойств с неуниверсальным
спектром и расходящимся парным функционалом.
Это **не исходная семья** и не её опровержение.
Она доказывает, что обнаруженных абстрактных свойств
недостаточно без дополнительного контроля конкретных фаз.

Незавершённая идея с Singer-циклом включена только
как явно помеченная исследовательская запись;
ни один её ожидаемый вывод не используется как теорема.

### Навигация

- [Актуальное связное изложение](#r7-source-round7-main-report).
- [Нормовая теорема о стационарном сжатии](#r7-source-r7-return-uniform-stationary-dephasing).
- [Все фиксированные физические степени](#r7-source-r7-return-all-fixed-powers-phase-separation).
- [Якобиан интенсивностей в исходной точке](#r7-source-root-original-intensity-at-prescribed-phase).
- [Полная координатная цикличность и кольцо Лорана](#r7-source-r7-original-full-cyclicity-laurent-unit).
- [Все физические миноры всех степеней](#r7-source-root-original-every-power-minors).
- [Однокомпонентные миноры по всем нечётным размерам](#r7-source-r7-original-all-odd-component-minors).
- [Определитель Шура и дискриминант](#r7-source-r7-return-schur-discriminant-identity).
- [Проверенная вспомогательная контрмодель](#r7-source-root-unipotent-flat-clock).
- [Сводная проверка доказательств](#r7-source-root-round7-proof-audit).
- [Открытые переходы и карта продолжения](#r7-source-round7-continuation-ledger).
- [Указатель всех новых источников](#round7-source-index).
- [Полный предыдущий накопительный текст](#round7-complete-prior-master).
- [Состав и воспроизводимая сборка](#round7-build-integrity).

### Как читать этот документ

Начинать следует с актуального изложения. Все новые
полные доказательства, аудиты и вычислительные исходники
включены далее; отдельные файлы для их чтения не нужны.
Предыдущий накопительный текст сохранён целиком один раз.
Ранние условные утверждения, меньшие диапазоны и незавершённые
попытки остаются историей исследования. Текущие формулировки
и явные границы имеют приоритет.

Внутренний независимый аудит не является опубликованным
рецензированием или проверкой в Lean. Исторический приоритет
вспомогательных результатов не заявляется. Конечные вычисления
не выдаются за доказательство асимптотики.
"""
    index = [
        '\n\n<a id="round7-source-index"></a>\n\n## Указатель новых полных источников\n',
        "\n| Источник | SHA256 | Байт |\n| --- | --- | ---: |\n",
    ]
    for item in records:
        name = Path(item["path"]).name
        index.append(f"| [{name}](#{item['anchor']}) | `{item['sha256']}` | {item['bytes']:,} |\n")

    parts = [front, "".join(index)]
    for p in all_paths:
        parts.append(include(p, data_by_path[p]))

    historical_text = historical.decode("utf-8")
    parts.append(
        '\n\n---\n\n<a id="round7-complete-prior-master"></a>\n\n'
        "## Полный предыдущий накопительный текст\n\n"
        f"SHA256 исходных байтов: `{BASE_HASH}`. Размер: {len(historical):,} байт.\n\n"
        "Ниже сохранён весь предыдущий текст без изменения исходных байтов.\n\n"
        "<!-- BEGIN COMPLETE PRECEDING MASTER ROUND7 -->\n\n"
        + historical_text
        + ("" if historical_text.endswith("\n") else "\n")
        + "\n<!-- END COMPLETE PRECEDING MASTER ROUND7 -->\n"
    )

    metadata = {
        "round": 7,
        "date": "2026-10-21",
        "status": "H_diag and the explicit pair test remain unproved and undisproved",
        "prior_master": {"sha256": BASE_HASH, "bytes": len(historical)},
        "new_sources": records,
        "source_bytes_modified_when_included": False,
        "prior_master_inclusion_count": 1,
        "unproved_singer_checkpoint_is_not_a_theorem_input": True,
    }
    parts.append(
        '\n\n---\n\n<a id="round7-build-integrity"></a>\n\n'
        "## Проверка целостности и воспроизводимая сборка\n\n"
        "Ни один первичный текст при включении не исправлялся. "
        "Контрольные суммы выше относятся к полным исходным байтам. "
        "Протокол содержит состав текущего прохода; затем приведён код сборки.\n\n"
        "```json\n" + json.dumps(metadata, ensure_ascii=False, indent=2) + "\n```\n"
    )
    parts.append(include(Path(__file__).resolve(), Path(__file__).read_bytes()))

    result = "".join(parts).encode("utf-8")
    # The old master is a byte substring in exactly one new historical section.
    if result.count(historical) != 1:
        raise SystemExit("Historical master must be included exactly once.")
    for p, data in data_by_path.items():
        if sha(p.read_bytes()) != sha(data):
            raise SystemExit(f"Source changed during build: {p.name}")
        if data not in result:
            raise SystemExit(f"Source bytes not present in result: {p.name}")
    current_anchors = {item["anchor"] for item in records}
    current_anchors.add(anchor(Path(__file__).resolve()))
    for ref in set(re.findall(rb"\]\(#(r7-source-[a-z0-9-]+)\)", result)):
        if ref.decode() not in current_anchors:
            raise SystemExit(f"Missing current source anchor: {ref.decode()}")
    # Write to the existing inode so its local identity metadata is preserved.
    TARGET.write_bytes(result)
    metadata["current_master"] = {
        "path": TARGET.name,
        "sha256": sha(result),
        "bytes": len(result),
        "lines": result.count(b"\n"),
    }
    MANIFEST.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "file": str(TARGET),
        "new_source_count": len(records),
        "bytes": len(result),
        "lines": result.count(b"\n"),
        "sha256": sha(result),
        "prior_master_exactly_once": True,
        "all_source_bytes_present": True,
        "current_source_anchors_verified": True,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

