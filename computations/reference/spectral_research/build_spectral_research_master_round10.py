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
SOURCES = ROOT / "research_round10_2026_10_21"
HISTORY = ROOT / "research_history_frozen" / "master_before_round10.md"
TARGET = ROOT / "Spectral_research_master.md"
MANIFEST = ROOT / "spectral_research_master_round10_manifest.json"
BASE_HASH = "e338400f1f360b680ea74c739283b296c9c67eb4e598c2067b136f9f29773777"
MAIN_NAME = "round10_main_report.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def anchor(path: Path) -> str:
    return "r10-source-" + re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")


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

    priority = ['round10_main_report.md', 'r10_weyl_orderwise_repulsion_stability.md', 'r10_weyl_downward_moment_heredity.md', 'r10_mixed_shrinking_isospectral_noise.md', 'r10_mixed_isospectral_twirl_obstruction.md', 'r10_arithmetic_stationary_rational_test.md', 'root_round10_proof_audit.md', 'r10_arithmetic_audit_orderwise_repulsion.md', 'r10_arithmetic_audit_downward_heredity.md', 'r10_mixed_main_report_audit.md', 'root_operator_route_scope.md', 'r10_mixed_operator_scope_independent_audit.md', 'round10_continuation_ledger.md', 'r10_weyl_route_ledger.md', 'round10_target_checkpoint.md', 'r10_arithmetic_exact_checks.py', 'r10_arithmetic_exact_checks.json']
    rank = {name: i for i, name in enumerate(priority)}
    all_paths.sort(key=lambda p: (rank.get(p.name, len(priority)), p.suffix != ".md", p.name))
    data_by_path = {p: p.read_bytes() for p in all_paths}
    for p, data in data_by_path.items():
        if any(b < 32 and b not in (9, 10) for b in data):
            raise SystemExit(f"Unexpected control byte in current source: {p.name}")
    records = [record(p, data_by_path[p]) for p in all_paths]

    front = r"""
# Спектральная статистика точной детерминированной семьи

## Единый продолжаемый исследовательский документ

Версия: завершение десятого исследовательского прохода, 21 октября 2026 года.

**Статус: полного решения нет.** Для исходных
\(U_N=e^{i10^{-80}NA_N}M_N\), по всем нечётным \(N\),
не доказан и не опровергнут \(H_{\mathrm{diag}}\).
Не предъявлена и допустимая бесконечная контрпоследовательность
исходной семьи. В этом проходе не получено новой оценки
первого исходного парного функционала. Он точно указан
в §8 актуального изложения.

### Доказанные результаты этого прохода

Пусть \(H_k\) означает исходный критерий при одном фиксированном
порядке \(k\), но при всех допустимых тестах и всех фиксированных
полосах. Доказано, что \(H_k\) само обеспечивает равномерную
интегрируемость локальных счётчиков в степени \(k\).
Дополнительный момент порядка \(k+1\) для этого не нужен.

Ключевая оценка получена из конечномерного граммова представления
CUE и разделённых разностей экспоненциальных векторов. Положительный
тест окна длины \(\delta\) имеет CUE-момент не более
\(C_{k,\beta}\delta^{k^2}\). Разбиение фиксированного интервала
на \(M\) ячеек даёт точную оценку хвоста
\[
\limsup_N\mathbb E\!\left[
X_N(I)^k\mathbf1_{\{X_N(I)>2kM\}}
\right]
\le C_{k,\beta}|I|^{k^2}M^{-k(k-1)}.
\]
Каждый параметр окна фиксируется до предела по размерности.

При согласовании собственных углов с ограниченным максимальным
развёрнутым сдвигом и с \(\sum_j|\varepsilon_{j,N}|\to0\)
получена эквивалентность \(H_k(U)\iff H_k(V)\)
для каждого порядка отдельно. Затем доказано
\[
H_k\Longrightarrow H_j\qquad(1\le j\le k).
\]
Восстановление меньших порядков использует точную поправку
на выбранные метки и явную оценку свёртки синусного определителя.
Ни эргодичность, ни заранее существующий предельный процесс,
ни более высокий момент не предполагаются.

Эти теоремы уточняют силу и устойчивость критерия. Они не
устанавливают его предпосылку для исходной семьи. В частности,
ни \(H_2\), ни даже один зафиксированный в §8 парный тест
не доказан.

### Проверенные препятствия для операторного усреднения

Доказано точное различие между средним степеней одной
сопряжённой матрицы и степенями её среднего действия.
Даже ошибка \(O(N^{-1})\) в операторной норме на матричном
пространстве может потерять весь конечный парный член.

Для вспомогательных изоспектральных сопряжений невозмущённого
\(M_N\) построен случайный сдвиг, исчезающий на классическом
масштабе. Усреднённое действие после независимого перевыбора
сжимается на всех временах, тогда как истинная парная статистика
на явной нечётной арифметической подпоследовательности расходится.
Этот пример доказывает необходимость отдельной оценки при
снятии усреднения. Он не является контрпримером для
\(e^{i10^{-80}NA_N}M_N\).

Проверены также рациональные неподвижные точки правильного
обычного символа и точные области применимости опубликованных
операторных сравнений. Переноса к исходной микроскопической
оценке из них не получено.

### Навигация

- [Актуальное связное изложение](#r10-source-round10-main-report).
- [Интегрируемость и устойчивость одного порядка](#r10-source-r10-weyl-orderwise-repulsion-stability).
- [Восстановление меньших порядков](#r10-source-r10-weyl-downward-moment-heredity).
- [Исчезающий изоспектральный шум](#r10-source-r10-mixed-shrinking-isospectral-noise).
- [Точное усреднение сопряжений и потеря масштаба](#r10-source-r10-mixed-isospectral-twirl-obstruction).
- [Рациональные точки исходного символа](#r10-source-r10-arithmetic-stationary-rational-test).
- [Сводная проверка доказательств](#r10-source-root-round10-proof-audit).
- [Независимая проверка интегрируемости](#r10-source-r10-arithmetic-audit-orderwise-repulsion).
- [Независимая проверка меньших порядков](#r10-source-r10-arithmetic-audit-downward-heredity).
- [Операторный поиск: точная область применимости](#r10-source-root-operator-route-scope).
- [Реестр результата и незакрытой оценки](#r10-source-round10-continuation-ledger).
- [Указатель всех новых источников](#round10-source-index).
- [Полный предыдущий накопительный текст](#round10-complete-prior-master).
- [Состав и воспроизводимая сборка](#round10-build-integrity).

### Как читать и проверять

Актуальное изложение задаёт действующие формулировки. Далее
включены полные доказательства, независимые внутренние проверки,
исходники точных конечных вычислений и полученный протокол.
Весь предыдущий единый документ сохранён один раз без изменения
его исходных байтов. Ни один новый источник не изменён
при включении в этот документ.

Исторические условные формулировки и неудавшиеся попытки
остаются историей исследования. Они не являются скрытыми
гипотезами новых утверждений. Внутренняя проверка не означает
внешнего опубликованного рецензирования или формализации в Lean.
Исторический приоритет вспомогательных теорем не заявляется.
Конечные вычисления не подменяют исходный асимптотический предел.
"""
    index = [
        '\n\n<a id="round10-source-index"></a>\n\n## Указатель новых полных источников\n',
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
        '\n\n---\n\n<a id="round10-complete-prior-master"></a>\n\n'
        "## Полный предыдущий накопительный текст\n\n"
        f"SHA256 исходных байтов: `{BASE_HASH}`. Размер: {len(historical):,} байт.\n\n"
        "Ниже сохранён весь предыдущий текст без изменения исходных байтов.\n\n"
        "<!-- BEGIN COMPLETE PRECEDING MASTER ROUND10 -->\n\n"
        + historical_text
        + ("" if historical_text.endswith("\n") else "\n")
        + "\n<!-- END COMPLETE PRECEDING MASTER ROUND10 -->\n"
    )

    metadata = {
        "round": 10,
        "date": "2026-10-21",
        "status": "H_diag and the explicit pair test remain unproved and undisproved",
        "prior_master": {"sha256": BASE_HASH, "bytes": len(historical)},
        "new_sources": records,
        "source_bytes_modified_when_included": False,
        "prior_master_inclusion_count": 1,
        "original_family_countersequence_not_obtained": True,
        "same_order_uniform_integrability_proved_conditionally_on_full_H_k": True,
        "same_order_spectral_matching_equivalence_proved": True,
        "downward_H_k_heredity_proved": True,
        "no_original_pair_estimate_obtained_this_round": True,
        "full_H_k_premise_not_established_for_original_family": True,
        "auxiliary_bare_cat_noise_is_not_original_counterexample": True,
        "higher_moment_or_ergodicity_not_assumed_in_downward_proof": True,
        "finite_exact_checks_not_asymptotic_evidence": True,
    }
    parts.append(
        '\n\n---\n\n<a id="round10-build-integrity"></a>\n\n'
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
    builder_bytes = Path(__file__).read_bytes()
    if result.count(builder_bytes) != 1:
        raise SystemExit("The full builder must be included exactly once.")
    current_anchors = {item["anchor"] for item in records}
    current_anchors.add(anchor(Path(__file__).resolve()))
    for ref in set(re.findall(rb"\]\(#(r10-source-[a-z0-9-]+)\)", result)):
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


