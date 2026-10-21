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
SOURCES = ROOT / "research_round9_2026_10_21"
HISTORY = ROOT / "research_history_frozen" / "master_before_round9.md"
TARGET = ROOT / "Spectral_research_master.md"
MANIFEST = ROOT / "spectral_research_master_round9_manifest.json"
BASE_HASH = "b1dc28374e62fb77c59d7da04f638916e43e0ac5809c68ea02c501fb92436a20"
MAIN_NAME = "round9_main_report.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def anchor(path: Path) -> str:
    return "r9-source-" + re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")


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

    priority = ["round9_main_report.md","root_diagonal_cocycle_normalization.md","r9_sector_continuous_symbol_stability.md","r9_arithmetic_galois_obstruction.md","r9_determinant_exact_cue_detdet_counterexample.md","r9_determinant_nonzero_minors_addendum.md","r9_determinant_braun_haake_and_contraction_audit.md","root_round9_proof_audit.md","r9_sector_analytic_normalization_independent_audit.md","r9_arithmetic_audit_continuous_selection.md","r9_determinant_audit_galois.md","r9_sector_deleted_clock_independent_audit.md","r9_sector_main_report_audit.md","r9_determinant_main_report_audit.md","round9_continuation_ledger.md","r9_sector_route_ledger.md","round9_research_checkpoint.md"]
    rank = {name: i for i, name in enumerate(priority)}
    all_paths.sort(key=lambda p: (rank.get(p.name, len(priority)), p.suffix != ".md", p.name))
    data_by_path = {p: p.read_bytes() for p in all_paths}
    for p, data in data_by_path.items():
        if any(b < 32 and b not in (9, 10) for b in data):
            raise SystemExit(f"Unexpected control byte in current source: {p.name}")
    records = [record(p, data_by_path[p]) for p in all_paths]

    front = r"""# Спектральная статистика точной детерминированной семьи

## Единый продолжаемый исследовательский документ

Версия: завершение девятого исследовательского прохода, 21 октября 2026 года.

**Статус: полного решения нет.** Для исходных
\(U_N=e^{i10^{-80}NA_N}M_N\), по всем нечётным \(N\),
не доказан и не опровергнут \(H_{\mathrm{diag}}\).
Допустимая бесконечная контрпоследовательность исходной семьи
также не предъявлена. Точная первая недоказанная оценка
приведена в §10 актуального изложения.

### Основной новый доказанный результат

Для первой непрерывной квантовой фазы построена настоящая
унитарная поправка с точным аналитическим ядром. Одна
последовательность таких поправок охватывает все нечётные
размерности и делает относительную скалярную ошибку \(o(N^{-1})\)
на каждом ребре. Произведения этих множителей стремятся к
единице равномерно на орбитах длины до \(BN\), при каждом
фиксированном \(B\).

Переход к новой семье сохраняет локальные слабые предельные
законы без дополнительных моментных предположений. Полный
\(H_{\mathrm{diag}}\) для исходной семьи эквивалентен полному
критерию для новой семьи. Отдельный парный момент без
равномерной интегрируемости автоматически не переносится.

Ключевой новый технический шаг — работа с непрерывным символом
через фиксированные полиномы Фейера и один совместный выбор
порогов. В квантовую эргодичность не подставляются символы
с растущими производными. Для положительного квантования
непрерывного символа получена настоящая операторная ошибка
\(o(N^{-1})\) между двумя точно унитарными реализациями.

Этот результат снимает оставшийся барьер регулярности и
реальной реализации фазовой нормализации. Он не оценивает
полную знакопеременную сумму экспоненциально многих
орбитальных вкладов. Такой переход явно остаётся недоказанным.

### Другие новые результаты и их границы

Построена явная вспомогательная семья, у которой полный
det–det коррелятор точно совпадает с CUE при всех аргументах,
но фиксированный парный тест имеет ненулевой предельный
дефект, а локальный процесс сходится к случайно сдвинутой
единичной решётке. Отдельное усиление сохраняет этот
контрмеханизм при ненулевых физических минорах всех
ненулевых степеней. Обе семьи являются проверкой способа
доказательства, а не контрпримерами к исходной постановке.

Для исходного гамильтониана и явного Galois-спутника доказан
разрыв кубических моментов \(>3/10000\) по всем нечётным
\(N\ge75\), а также положительная нижняя граница расстояния
после любого унитарного сопряжения. Дополнительно при
\(7\nmid N\) исключена точная проективная изоспектральность
со спутником при ненулевом алгебраическом параметре.
Микроскопическое различие локальных пределов отсюда не следует.

Все конечные тождества и замыкание
\(H_{\mathrm{diag}}\Rightarrow\mathrm{Sine}_2\)
сохранены с доказательствами. Они не устанавливают
недостающую оценку для заданного оператора.

### Навигация

- [Актуальное связное изложение](#r9-source-round9-main-report).
- [Точная аналитическая нормализация](#r9-source-root-diagonal-cocycle-normalization).
- [Непрерывный символ и спектральная устойчивость](#r9-source-r9-sector-continuous-symbol-stability).
- [Galois-спутник исходной семьи](#r9-source-r9-arithmetic-galois-obstruction).
- [Точный det–det контрмеханизм](#r9-source-r9-determinant-exact-cue-detdet-counterexample).
- [Ненулевые миноры всех степеней](#r9-source-r9-determinant-nonzero-minors-addendum).
- [Проверка опубликованного детерминантного подхода](#r9-source-r9-determinant-braun-haake-and-contraction-audit).
- [Сводная проверка доказательств](#r9-source-root-round9-proof-audit).
- [Независимая аналитическая проверка](#r9-source-r9-sector-analytic-normalization-independent-audit).
- [Независимая спектральная проверка](#r9-source-r9-arithmetic-audit-continuous-selection).
- [Реестр точного незакрытого перехода](#r9-source-round9-continuation-ledger).
- [Указатель всех новых источников](#round9-source-index).
- [Полный предыдущий накопительный текст](#round9-complete-prior-master).
- [Состав и воспроизводимая сборка](#round9-build-integrity).

### Как читать и проверять

Актуальное связное изложение задаёт действующие формулировки.
Далее включены полные новые доказательства, независимые внутренние
аудиты, вычислительные исходники и фактически полученные ответы.
Предыдущая накопительная версия сохранена целиком один раз,
без изменения её исходных байтов. Все новые источники включены
без изменения и снабжены контрольными суммами.

Старые условные формулировки и незавершённые попытки остаются
историей исследования. Они не являются скрытыми гипотезами
новых теорем. Внутренний аудит не означает внешнего опубликованного
рецензирования или формализации в Lean. Исторический приоритет
вспомогательных результатов не заявляется; конечные вычисления
не выдаются за доказательство исходной асимптотики.
"""
    index = [
        '\n\n<a id="round9-source-index"></a>\n\n## Указатель новых полных источников\n',
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
        '\n\n---\n\n<a id="round9-complete-prior-master"></a>\n\n'
        "## Полный предыдущий накопительный текст\n\n"
        f"SHA256 исходных байтов: `{BASE_HASH}`. Размер: {len(historical):,} байт.\n\n"
        "Ниже сохранён весь предыдущий текст без изменения исходных байтов.\n\n"
        "<!-- BEGIN COMPLETE PRECEDING MASTER ROUND9 -->\n\n"
        + historical_text
        + ("" if historical_text.endswith("\n") else "\n")
        + "\n<!-- END COMPLETE PRECEDING MASTER ROUND9 -->\n"
    )

    metadata = {
        "round": 9,
        "date": "2026-10-21",
        "status": "H_diag and the explicit pair test remain unproved and undisproved",
        "prior_master": {"sha256": BASE_HASH, "bytes": len(historical)},
        "new_sources": records,
        "source_bytes_modified_when_included": False,
        "prior_master_inclusion_count": 1,
        "original_family_countersequence_not_obtained": True,
        "all_odd_diagonal_normalization_preserved": True,
        "unconditional_local_law_equivalence_proved": True,
        "full_H_diag_equivalence_is_not_its_unconditional_proof": True,
        "individual_pair_moment_transfer_not_asserted_unconditionally": True,
        "auxiliary_clock_family_is_not_original_counterexample": True,
    }
    parts.append(
        '\n\n---\n\n<a id="round9-build-integrity"></a>\n\n'
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
        if result.count(data) != 1:
            raise SystemExit(f"Source bytes must be present exactly once: {p.name}")
    current_anchors = {item["anchor"] for item in records}
    current_anchors.add(anchor(Path(__file__).resolve()))
    for ref in set(re.findall(rb"\]\(#(r9-source-[a-z0-9-]+)\)", result)):
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


