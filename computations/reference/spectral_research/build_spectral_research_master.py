#!/usr/bin/env python3
"""Build one continuing Markdown with full source snapshots and explicit errata."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROUND = ROOT / "research_round5_2026_10_21"
DEST = ROOT / "Spectral_research_master.md"
MANIFEST = ROOT / "spectral_research_master_manifest.json"
MAIN = ROUND / "round5_main_report.md"
ADDENDUM = ROUND / "round5_post_audit_addendum.md"
BOOKS = [
    ROOT / "Spectral_proofs_2026-10-21.md",
    ROOT / "Spectral_research_round4_2026-10-21.md",
]
EXPECTED = {
    "round5_main_report.md":
        "8a4629d270c1b70e2478ce98cc2ed66b8e4a6c836cc27c35fbaf1555587420c2",
    "Spectral_proofs_2026-10-21.md":
        "e3adece0122c75da67600bffddbf53ed17e513ec437f9543f7e6f1e7436fa470",
    "Spectral_research_round4_2026-10-21.md":
        "e74f697134ea0d7d0ad5776c118ac267cf4999ae029e5b1f0252de364596fa4a",
}
TICK = chr(96)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def code(value: object) -> str:
    return TICK + str(value) + TICK


def get_source(path: Path) -> dict:
    raw = path.read_bytes()
    raw_hash = sha(raw)
    if path.name in EXPECTED:
        assert raw_hash == EXPECTED[path.name], (path, raw_hash)
    original = raw.decode("utf-8")
    rendered = original
    corrections: list[str] = []
    if path.name == "Spectral_proofs_2026-10-21.md":
        edits = [
            (
                "\\mathcal E_7=\x0crac{81}{16000}",
                r"\mathcal E_7=\frac{81}{16000}",
                "U+000C перед rac исправлен на команду \\frac в формуле E_7 "
                "в embedded adversarial_oldspace_audit.md.",
            ),
            (
                "d_{j+1}-Ld_j-\x08igl(v(x_j+d_j)-v(x_j)\\bigr)",
                r"d_{j+1}-Ld_j-\bigl(v(x_j+d_j)-v(x_j)\bigr)",
                "U+0008 перед igl исправлен на \\bigl в (4.2) embedded "
                "fermionic_twisted_pressure.md.",
            ),
        ]
        for old, new, note in edits:
            assert rendered.count(old) == 1, (path, repr(old))
            rendered = rendered.replace(old, new)
            corrections.append(note)
    if path.name == "Spectral_research_round4_2026-10-21.md":
        old = r"\le2\|h-b_B\|_1+sum_{k=2}^{J}|\Delta_{k,N}(b_B)|+H^J/J!."
        new = r"\le2\|h-b_B\|_1+\sum_{k=2}^{J}|\Delta_{k,N}(b_B)|+H^J/J!."
        assert rendered.count(old) == 1, path
        rendered = rendered.replace(old, new)
        corrections.append(
            "В (5.3) embedded root_exact_identities_and_closure.md "
            "добавлена пропущенная обратная косая черта перед sum. "
            "Это исправление уже описано в соседнем историческом аудите."
        )
    controls = [
        (i, ord(c)) for i, c in enumerate(rendered)
        if (ord(c) < 32 and c not in "\n\t") or ord(c) == 127
    ]
    assert not controls, (path, controls[:10])
    return {
        "path": str(path.relative_to(ROOT)),
        "name": path.name,
        "original_bytes": len(raw),
        "original_sha256": raw_hash,
        "embedded_bytes": len(rendered.encode("utf-8")),
        "embedded_sha256": sha(rendered.encode("utf-8")),
        "corrections": corrections,
        "text": rendered,
    }


def category(path: Path) -> str:
    if path.suffix in {".py", ".wl"}:
        return "Исследовательский пробный код" if "probe" in path.name else "Код конечной проверки"
    if "audit" in path.name:
        return "Аудит или отдельная доказательная проверка"
    if "collision_moment" in path.name:
        return "Доказательство для помеченных наблюдаемых"
    if "occupation_resummation" in path.name:
        return "Точные тождества и их ограниченная область вывода"
    if "cubic_character" in path.name:
        return "Вспомогательная другая семья, не контрпример исходной задаче"
    if "computation_note" in path.name:
        return "Протокол конечных вычислений"
    return "Первичная доказательная записка; область действия указана внутри"


def fenced_code(text: str, language: str) -> str:
    runs = [len(m.group(0)) for m in re.finditer(TICK + "+", text)]
    fence = TICK * max(3, 1 + max(runs, default=0))
    return fence + language + "\n" + text + ("" if text.endswith("\n") else "\n") + fence + "\n"


def source_block(rec: dict, anchor: str) -> str:
    name = rec["name"]
    warning = ""
    if name == "dual_directed_encounter_marked_unitarity_resummation.md":
        warning = (
            "> Поправка к замороженному первичному тексту: в (33) для "
            "произвольных ограниченных весов требуется множитель "
            "\\(W=\\sup|w_{n,N}|\\), то есть "
            "\\(O_{B,C}(W N^{-13})\\). Исходная запись корректна при "
            "\\(W\\le1\\). Эта поправка имеет приоритет над формулой ниже.\n\n"
        )
    corrections = ""
    if rec["corrections"]:
        corrections = (
            "Включённая копия содержит только следующие явно объявленные "
            "типографические исправления; исходный файл оставлен неизменным:\n\n"
            + "\n".join("- " + c for c in rec["corrections"]) + "\n\n"
        )
    body = rec["text"]
    ext = Path(name).suffix
    if ext in {".py", ".wl"}:
        body = fenced_code(body, "python" if ext == ".py" else "wolfram")
    return (
        f'\n\n---\n\n<a id="{anchor}"></a>\n\n'
        f"## Полный источник: {name}\n\n"
        f"Относительный путь источника: {code(rec['path'])}.\n\n"
        f"SHA256 исходных байтов: {code(rec['original_sha256'])}. "
        f"Размер: {rec['original_bytes']:,} байт.\n\n"
        f"SHA256 включённого текста: {code(rec['embedded_sha256'])}.\n\n"
        + corrections + warning
        + f"<!-- BEGIN INCLUDED SOURCE {anchor} -->\n\n"
        + body
        + ("" if body.endswith("\n") else "\n")
        + f"\n<!-- END INCLUDED SOURCE {anchor} -->\n"
    )


def main() -> None:
    main_rec, add_rec = get_source(MAIN), get_source(ADDENDUM)
    raw_paths = sorted(
        p for p in ROUND.iterdir()
        if p.is_file() and p.suffix in {".md", ".py", ".wl"}
        and p not in {MAIN, ADDENDUM}
    )
    raw_paths.sort(key=lambda p: (p.suffix != ".md", p.name))
    raw_recs = [get_source(p) for p in raw_paths]
    book_recs = [get_source(p) for p in BOOKS]
    builder_rec = get_source(Path(__file__))
    records = [main_rec, add_rec] + raw_recs + book_recs + [builder_rec]
    front = r"""# Спектральная статистика точной детерминированной семьи

## Единый продолжаемый исследовательский документ

Версия: завершение пятого исследовательского прохода, 21 октября 2026 года.

**Статус: полного решения пока нет.** Для исходных
\(U_N=e^{i10^{-80}NA_N}M_N\), по всем нечётным \(N\),
не доказан и не опровергнут \(H_{\rm diag}\). Даже один
явный парный тест из §9 актуальной части остаётся незакрытым.
Документ содержит полученные результаты, полные доказательства,
точные ограничения каждого вывода и историю исправлений.

Самые существенные результаты этого прохода:

- Для исходной семьи доказаны оценки физического ядра
  \(\max|U_{xy}|\le3/\sqrt N\), \(\|P-J\|<1/2\),
  \(\|Q\|\to0\), где \(P_{xy}=|U_{xy}|^2\),
  \(Q_{xy}=U_{xy}\overline{U_{yx}}\).
- Получено настоящее знакопеременное сокращение суммы по различным
  парам траекторий при числе длинных переподключаемых участков
  до порядка \(\sqrt N\). Большие положительные и отрицательные
  части порядка \(N^2\) и \(N^3\) выделены и вычислены.
- Доказана экспоненциальная положительная сумма пар с одинаковыми
  направленными кратностями рёбер. Экспоненциальный подкласс
  требует изменения переходов в фиксированной положительной
  доле вершин и потому не покрывается перестановками только длинных
  участков. Это утверждение о покрытии и положительной сумме;
  оно не является нижней оценкой всего знакопеременного остатка.
- Последнее дополнение локализует полную компенсацию:
  уже внутри одинаковых чисел посещений вершин
  \(\mathcal R_n^{\rm occ}=-\mathcal F_n+\mathcal O_n\),
  \(0\le\mathcal O_n\le N^2\). Тем самым
  экспоненциально большая положительная часть компенсируется
  там же с экспоненциально малой относительной ошибкой.
  Малый в сравнении с ней абсолютный остаток ещё не вычислен
  с точностью, необходимой для \(H_{\rm diag}\).
- Для специальных **помеченных** моментов числа повторяющихся
  подслов получены оценки вплоть до порядка \(N/\log N\)
  переподключений. Переход от этих моментов к индикатору отсутствия
  повторений не доказан; это не теорема о различных парах в таком
  более широком диапазоне.

Исторический приоритет этих вспомогательных результатов не заявляется.
Внутренние независимые аудиты не являются опубликованным рецензированием
или формальной проверкой в Lean. Конечные вычисления проверяют формулы
и кратности и не заменяют асимптотические доказательства.

### Навигация

- [Актуальное связное изложение](#current-exposition):
  исходная семья, физическое ядро, точные классы траекторий,
  растущий порядок, экспоненциальные классы, арифметика,
  первая недоказанная оценка и полное замыкание при \(H_{\rm diag}\).
- [Последнее дополнение](#last-addendum):
  полное суммирование внутри посещений, локализация компенсации
  и новая теорема для помеченных моментов.
- [Указатель полных источников этого прохода](#source-index).
- [Все первичные доказательства, аудиты и код текущего прохода](#round5-sources).
- [Полный предыдущий накопительный сборник](#historical-book-1).
- [Полный сборник четвёртого прохода](#historical-book-2).
- [Правила продолжения, журнал исправлений и сборка](#continuation-and-integrity).

### Как читать историю

Начинать следует с актуального изложения и последнего дополнения.
После них идут полные первичные тексты: это позволяет проверить детали
без обращения к отдельным рабочим файлам. Исторические сборники
сохраняют также условные маршруты, отвергнутые попытки и ранние
формулировки. Их наличие не превращает недоказанное утверждение
в теорему. Явные поправки и ограничения в актуальной части
и соответствующих аудитах имеют приоритет.

Все опубликованные теоремы, используемые как внешние входы, снабжены
точными ссылками и проверкой нужных гипотез в своих доказательных
записках. Ссылки на литературные подходы без доказанной ошибки
для исходной семьи не закрывают спектральную задачу.

"""
    chunks = [
        front,
        source_block(main_rec, "current-exposition"),
        source_block(add_rec, "last-addendum"),
        '\n\n---\n\n<a id="source-index"></a>\n\n'
        "## Указатель полных источников текущего прохода\n\n"
        "Все перечисленные тексты включены целиком ниже. Названия с "
        "*probe* обозначают исследовательский код; выводы такого кода "
        "принимаются только там, где имеется отдельное доказательство "
        "или проверенный конечный сертификат.\n\n"
        "| № | Источник | Вид записи | Байты исходника | SHA256 исходника |\n"
        "|---|---|---|---:|---|\n",
    ]
    for i, (p, rec) in enumerate(zip(raw_paths, raw_recs), 1):
        chunks.append(
            f"| {i} | [{p.name}](#round5-source-{i:02d}) | "
            f"{category(p)} | {rec['original_bytes']} | "
            f"{code(rec['original_sha256'])} |\n"
        )
    chunks.append(
        '\n<a id="round5-sources"></a>\n\n'
        "## Полные первичные тексты пятого прохода\n\n"
        "У каждого источника указаны исходный хеш и хеш включённого "
        "текста. Совпадение хешей означает дословное включение. "
        "Зависимости между записками сохраняют указанную внутри область "
        "действия; новая область не выводится из одного имени файла.\n"
    )
    for i, rec in enumerate(raw_recs, 1):
        chunks.append(source_block(rec, f"round5-source-{i:02d}"))
    for i, rec in enumerate(book_recs, 1):
        chunks.append(source_block(rec, f"historical-book-{i}"))
    chunks.append(r"""

---

<a id="continuation-and-integrity"></a>

## Правила продолжения этого же документа

Дальнейшие проходы должны обновлять актуальное изложение и статус
незакрытых оценок в начале этого файла, а новые полные доказательства
и проверки добавлять отдельными датированными источниками. Исправление
ошибки нужно записывать явно, с указанием затронутой формулы и области
действия. Не следует вновь объявлять уже полученную условную редукцию
решением исходной задачи.

Ближайшее точное незакрытое обязательство остаётся формулой (9.3)
актуальной части, эквивалентной (Д.9) дополнения. Для полного
\(H_{\rm diag}\) после этого всё равно нужны все фиксированные
порядки \(k\ge3\) и все предусмотренные в условии Fourier-полосы.
Никаких новых предположений, усреднений по \(N\), замены \(\tau\)
или ограничения исходной задачи на простые размеры не введено.

### Явный журнал исправлений при объединении

1. В историческом накопительном сборнике исправлены ровно два
   повреждённых управляющими символами LaTeX-слова: команда frac
   в формуле \(\mathcal E_7\) и команда bigl в формуле (4.2)
   записи о скрученном давлении. Точные места и исходные/включённые
   хеши указаны перед исторической копией.
2. В сборнике четвёртого прохода в формуле (5.3) доказательства
   замыкания добавлена отсутствовавшая обратная косая черта перед
   sum. Её отсутствие уже было отмечено в его историческом аудите.
3. Замороженная записка о трёх участках включена дословно, но
   снабжена поправкой непосредственно перед текстом: в (33)
   нужно учитывать \(W=\sup|w_{n,N}|\). Та же поправка дана
   в актуальном изложении.
4. Актуальное изложение включено в точно проверенной версии
   SHA256 8a4629d270c1b70e2478ce98cc2ed66b8e4a6c836cc27c35fbaf1555587420c2.
   Последующие результаты вынесены в отдельное дополнение, поэтому
   контрольный хеш проверенного текста не подменён.

Исходные исторические файлы не изменены. Их текстовые копии в этом
сборнике отличаются только тремя перечисленными типографическими
исправлениями; они не являются дословными на уровне этих байтов.
Полные математические записи сохранены. Следующий раздел включает
скрипт сборки, чтобы правила объединения и исправлений были проверяемы.
""")
    chunks.append(source_block(builder_rec, "builder-source"))
    output = "".join(chunks)
    assert not [
        c for c in output
        if (ord(c) < 32 and c not in "\n\t") or ord(c) == 127
    ]
    for rec in [main_rec, add_rec] + raw_recs + book_recs:
        assert rec["text"] in output, rec["path"]
    navigable = output.split("<!-- BEGIN INCLUDED SOURCE builder-source -->")[0]
    anchors = re.findall(r'<a id="([^"]+)"></a>', navigable)
    own_anchors = [
        "current-exposition", "last-addendum", "source-index", "round5-sources",
        "historical-book-1", "historical-book-2", "continuation-and-integrity",
        "builder-source",
    ] + [f"round5-source-{i:02d}" for i in range(1, len(raw_recs)+1)]
    for anchor in own_anchors:
        assert anchors.count(anchor) == 1, (anchor, anchors.count(anchor))
    raw_output = output.encode("utf-8")
    DEST.write_bytes(raw_output)
    metadata = {
        "destination": str(DEST),
        "date": "2026-10-21",
        "round5_primary_count": len(raw_recs),
        "complete_source_count": len(records),
        "bytes": len(raw_output),
        "lines": output.count("\n"),
        "sha256": sha(raw_output),
        "status": "H_diag for the prescribed family remains unproved and unrefuted",
        "sources": [{k: v for k, v in rec.items() if k != "text"} for rec in records],
    }
    MANIFEST.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    print(json.dumps({k: v for k, v in metadata.items() if k != "sources"},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
