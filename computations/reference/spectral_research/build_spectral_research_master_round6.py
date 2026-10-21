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
SOURCES = ROOT / "research_round6_2026_10_21"
HISTORY = ROOT / "research_history_frozen" / "master_before_round6.md"
TARGET = ROOT / "Spectral_research_master.md"
MANIFEST = ROOT / "spectral_research_master_round6_manifest.json"
BASE_HASH = "f235e90db53c99a0b93cb42ff828c83af80b49064844f5e72a18fe51642cf2a2"
MAIN_NAME = "round6_main_report.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def anchor(path: Path) -> str:
    return "r6-source-" + re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")


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

    priority = [
        MAIN_NAME,
        "root_original_gap2_combined.md",
        "r6_original_fixed_powers_49.md",
        "r6_original_twostep_physical_mixing.md",
        "r6_occupation_twostep_gauss.md",
        "r6_occupation_minami_band_tail.md",
        "r6_occupation_rational_inner_kac.md",
        "root_all_orders_weighted_occupation_bound.md",
        "r6_original_isolated_cross_occupation.md",
        "r6_dense_phasechaos_isolated_all_orders.md",
        "r6_dense_bounded_runs_raw49.md",
        "r6_dense_renewal_long_return_obstruction.md",
        "r6_dense_principal_minors_generic_phase_returns.md",
        "r6_original_principal_minors_jacobian.md",
        "r6_dense_higher_block_involution.md",
        "root_literature_applicability.md",
        "round6_continuation_ledger.md",
    ]
    rank = {name: i for i, name in enumerate(priority)}
    all_paths.sort(key=lambda p: (rank.get(p.name, len(priority)), p.suffix != ".md", p.name))
    data_by_path = {p: p.read_bytes() for p in all_paths}
    records = [record(p, data_by_path[p]) for p in all_paths]

    front = r"""# Спектральная статистика точной детерминированной семьи

## Единый продолжаемый исследовательский документ

Версия: завершение шестого исследовательского прохода, 21 октября 2026 года.

**Статус: полного решения пока нет.** Для исходных
\(U_N=e^{i10^{-80}NA_N}M_N\), по всем нечётным \(N\),
не доказан и не опровергнут \(H_{\mathrm{diag}}\).
Первая конкретная недоказанная оценка находится в §9 актуального
изложения: это один фиксированный допустимый парный тест.

В этой версии добавлены полные доказательства:

- точного закона сдвига нелинейных ветвей и физических оценок первых
  49 фиксированных степеней исходной матрицы;
- настоящего сокращения полного класса с несоседними заменами при
  разных посещениях, включая линейное по длине число замен;
- экспоненциально взвешенной оценки полной знаковой суммы пар
  с любым числом последовательных участков несовпадения длины до 48;
- суммарной оценки полного сектора одинаковых посещений на временах
  порядка \(N\) и его бесконечного экспоненциального хвоста;
- нормировок и первых моментов через рациональные внутренние функции,
  а также оценок всей фазово-постоянной факториальной иерархии;
- точной непомеченной детерминантной инволюции и её связностного остатка;
- геометрии первых возвращений двойного оператора, с доказанным
  сохранением нормы до времён порядка \(N\) и длинным энергетическим
  хвостом для исходной семьи.
- ненулевости всех ведущих главных миноров исходной матрицы и
  точной энергии возвратов \(N^2\) почти всюду по вспомогательным
  координатным фазам, с доказательством всех необходимых предпосылок.

Все кванторы и ограничения сформулированы явно. Положительные энергии
не выдаются за знаковые спектральные оценки. Внутренние независимые
аудиты не являются опубликованным рецензированием или проверкой в Lean.
Исторический приоритет вспомогательных результатов не заявляется.

### Навигация

- [Актуальное связное изложение и первая открытая оценка](#r6-source-round6-main-report).
- [Полный объединённый результат с константой 776](#r6-source-root-original-gap2-combined).
- [Точные нелинейные ветви и 49 физических степеней](#r6-source-r6-original-fixed-powers-49).
- [Полное сокращение последовательных участков длины до 48](#r6-source-r6-dense-bounded-runs-raw49).
- [Оценка полного сектора посещений и бесконечного хвоста](#r6-source-r6-occupation-minami-band-tail).
- [Геометрия длинных возвращений](#r6-source-r6-dense-renewal-long-return-obstruction).
- [Точные главные миноры и полнота фазовых возвращений](#r6-source-r6-dense-principal-minors-generic-phase-returns).
- [Указатель всех новых доказательств, аудитов и проверок](#round6-source-index).
- [Полный предыдущий накопительный текст](#round6-complete-prior-master).
- [Проверка целостности текущей сборки](#round6-build-integrity).

### Как читать историю

Начинать следует с актуального изложения. Все полные источники этого
прохода включены далее; для проверки доказательств отдельные файлы не
нужны. Предыдущий накопительный текст сохранён целиком один раз.
Его ранние условные утверждения и неудавшиеся попытки остаются
историей исследования. Актуальные уточнения и явные границы результатов
имеют приоритет. В частности, старая оценка \(\mathcal O_n\le N^2\)
теперь усилена суммарной оценкой \(\sum_{n\le M}\mathcal O_n\le
(\pi^2/4)NM\), но предел этой суммы ещё не определён.
"""
    index = [
        '\n\n<a id="round6-source-index"></a>\n\n## Указатель новых полных источников\n',
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
        '\n\n---\n\n<a id="round6-complete-prior-master"></a>\n\n'
        "## Полный предыдущий накопительный текст\n\n"
        f"SHA256 исходных байтов: `{BASE_HASH}`. Размер: {len(historical):,} байт.\n\n"
        "Ниже сохранён весь предыдущий текст без изменения исходных байтов.\n\n"
        "<!-- BEGIN COMPLETE PRECEDING MASTER ROUND6 -->\n\n"
        + historical_text
        + ("" if historical_text.endswith("\n") else "\n")
        + "\n<!-- END COMPLETE PRECEDING MASTER ROUND6 -->\n"
    )

    metadata = {
        "round": 6,
        "date": "2026-10-21",
        "status": "H_diag and the explicit pair test remain unproved and undisproved",
        "prior_master": {"sha256": BASE_HASH, "bytes": len(historical)},
        "new_sources": records,
        "source_bytes_modified_when_included": False,
        "prior_master_inclusion_count": 1,
    }
    parts.append(
        '\n\n---\n\n<a id="round6-build-integrity"></a>\n\n'
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
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
