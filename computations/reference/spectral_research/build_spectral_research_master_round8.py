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
SOURCES = ROOT / "research_round8_2026_10_21"
HISTORY = ROOT / "research_history_frozen" / "master_before_round8.md"
TARGET = ROOT / "Spectral_research_master.md"
MANIFEST = ROOT / "spectral_research_master_round8_manifest.json"
BASE_HASH = "2dc062a1124fc2d84fe026ff54eb9a806a1aaa49733c3a4d71f918be56662b13"
MAIN_NAME = "round8_main_report.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def anchor(path: Path) -> str:
    return "r8-source-" + re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")


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

    priority = ['round8_main_report.md', 'r8_original_uniform_clifford_symmetry_gap.md', 'r8_original_uniform_antiunitary_clifford_gap.md', 'r8_weyl_full_weight_relative_path_cancellation.md', 'r8_weyl_all_odd_endpoint_fiber_identity.md', 'r8_original_uniform_weyl_self_overlap.md', 'r8_original_uniform_metaplectic_symmetry_gap.md', 'r8_return_uniform_shrinking_windows.md', 'r8_return_approximate_eigenoperator_addendum.md', 'r8_weyl_sublinear_polynomial_obstruction.md', 'r8_weyl_quantitative_band_escape.md', 'r8_weyl_explicit_linear_degree_corollary.md', 'r8_weyl_three_time_resonance_and_exact_recursion.md', 'root_sharp_microscopic_perturbation_threshold.md', 'r8_return_sharp_stability_clock_addendum.md', 'root_round8_proof_audit.md', 'r8_return_audit_uniform_clifford_gap.md', 'r8_return_audit_uniform_antiunitary_clifford_gap.md', 'r8_return_audit_full_weight_cancellation.md', 'r8_return_audit_all_odd_endpoint_fibers.md', 'r8_weyl_audit_uniform_self_overlap.md', 'r8_return_audit_uniform_metaplectic_gap.md', 'r8_weyl_audit_uniform_shrinking_windows.md', 'r8_return_audit_weyl_polynomial_obstruction.md', 'root_audit_quantitative_band_escape.md', 'r8_return_audit_three_time_resonance.md', 'r8_return_audit_sharp_perturbation_threshold.md', 'r8_original_obstruction_audit.md', 'root_literature_applicability_round8.md', 'round8_continuation_ledger.md', 'round8_research_checkpoint.md']
    rank = {name: i for i, name in enumerate(priority)}
    all_paths.sort(key=lambda p: (rank.get(p.name, len(priority)), p.suffix != ".md", p.name))
    data_by_path = {p: p.read_bytes() for p in all_paths}
    for p, data in data_by_path.items():
        if any(b < 32 and b not in (9, 10) for b in data):
            raise SystemExit(f"Unexpected control byte in current source: {p.name}")
    records = [record(p, data_by_path[p]) for p in all_paths]

    front = r"""# Спектральная статистика точной детерминированной семьи

## Единый продолжаемый исследовательский документ

Версия: завершение восьмого исследовательского прохода, 21 октября 2026 года.

**Статус: полного решения нет.** Для исходных
\(U_N=e^{i10^{-80}NA_N}M_N\), по всем нечётным \(N\),
не доказан и не опровергнут \(H_{\mathrm{diag}}\).
Допустимая бесконечная контрпоследовательность исходной
семьи также не предъявлена. Первая конкретная недоказанная
оценка приведена в §12 актуального изложения.

### Новые доказанные результаты для исходной семьи

Доказаны равномерные разрывы со всем унитарным и антиунитарным
Clifford-нормализатором, включая произвольные меняющиеся с размером
модульные матрицы и характеры. Они действуют по всем нечётным
размерам. Для антиунитарного результата отдельно доказано отсутствие
всех аффинных обращений времени точной классической карты: четыре
неподвижные точки и их различные производные оставляют две
кандидатуры, обе исключаются прямым вычислением.

Для полной экспоненты толчка получены точные знакопеременные
сокращения каждого ненулевого замкнутого относительного Weyl-пути
до учёта терминального множителя.
Терминальные множители и все оставшиеся фазы вычислены для
каждого нечётного модуля и любого времени, включая вырожденное
\(S_f^m-I\). Полная сумма разделена по его арифметическим
прообразам. Остаток содержит когерентные степени
\(\operatorname{Ad}U_N\); требуемая оценка их совместной взвешенной
суммы при временах порядка \(N\) не получена.

Дополнительно установлены точная асимптотическая константа
наибольшего Weyl-самоперекрытия и его единственные максимизаторы;
равномерная малость всех сжимающихся спектральных окон после
сжатия на бесследовую координатную диагональ; соответствующая
сжатая резольвента \(o(N)\); количественная невозможность
полиномиальной аппроксимации толчка степени \(o(N)\), включая
необходимую нижнюю границу степени \(\tau N/40\); точная
трёхвременная знаковая корреляция исходного генератора.

### Доказанная граница этих выводов

Для любого \(C>0\) спектральное округление на расстоянии
\(C/N\) даёт другую семью, сохраняющую Clifford-разрывы и
сжатые оконные оценки, но не имеющую предела Sine₂.
Для этой вспомогательной семьи предъявлены фиксированные
допустимые тесты с дефектом \(H_{\mathrm{diag}}\).
Она не объявляется исходным контрпримером.
Отдельная явная пара последовательностей доказывает остроту
универсального масштаба устойчивости функционалов Лапласа
\(o(1/N)\), без предположения об исходном неизвестном пределе.

Все точные конечные формулы и замыкание
\(H_{\mathrm{diag}}\Rightarrow\mathrm{Sine}_2\)
проверены и включены. Сами по себе они не устанавливают
недостающую гипотезу для заданного оператора.

### Навигация

- [Актуальное связное изложение](#r8-source-round8-main-report).
- [Весь унитарный Clifford-нормализатор](#r8-source-r8-original-uniform-clifford-symmetry-gap).
- [Все антиунитарные Clifford-обращения времени](#r8-source-r8-original-uniform-antiunitary-clifford-gap).
- [Полные веса относительных путей](#r8-source-r8-weyl-full-weight-relative-path-cancellation).
- [Все нечётные модули и все времена](#r8-source-r8-weyl-all-odd-endpoint-fiber-identity).
- [Точный максимум Weyl-самоперекрытия](#r8-source-r8-original-uniform-weyl-self-overlap).
- [Сжимающиеся окна и сжатая резольвента](#r8-source-r8-return-uniform-shrinking-windows).
- [Количественная граница полиномиальной аппроксимации](#r8-source-r8-weyl-quantitative-band-escape).
- [Микроскопический масштаб возмущения](#r8-source-root-sharp-microscopic-perturbation-threshold).
- [Сводный аудит доказательств](#r8-source-root-round8-proof-audit).
- [Реестр точного незакрытого перехода](#r8-source-round8-continuation-ledger).
- [Указатель всех новых источников](#round8-source-index).
- [Полный предыдущий накопительный текст](#round8-complete-prior-master).
- [Состав и воспроизводимая сборка](#round8-build-integrity).

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
        '\n\n<a id="round8-source-index"></a>\n\n## Указатель новых полных источников\n',
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
        '\n\n---\n\n<a id="round8-complete-prior-master"></a>\n\n'
        "## Полный предыдущий накопительный текст\n\n"
        f"SHA256 исходных байтов: `{BASE_HASH}`. Размер: {len(historical):,} байт.\n\n"
        "Ниже сохранён весь предыдущий текст без изменения исходных байтов.\n\n"
        "<!-- BEGIN COMPLETE PRECEDING MASTER ROUND8 -->\n\n"
        + historical_text
        + ("" if historical_text.endswith("\n") else "\n")
        + "\n<!-- END COMPLETE PRECEDING MASTER ROUND8 -->\n"
    )

    metadata = {
        "round": 8,
        "date": "2026-10-21",
        "status": "H_diag and the explicit pair test remain unproved and undisproved",
        "prior_master": {"sha256": BASE_HASH, "bytes": len(historical)},
        "new_sources": records,
        "source_bytes_modified_when_included": False,
        "prior_master_inclusion_count": 1,
        "original_family_countersequence_not_obtained": True,
        "all_odd_endpoint_fibers_preserved": True,
        "auxiliary_rounded_family_is_not_original_counterexample": True,
    }
    parts.append(
        '\n\n---\n\n<a id="round8-build-integrity"></a>\n\n'
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
    for ref in set(re.findall(rb"\]\(#(r8-source-[a-z0-9-]+)\)", result)):
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

