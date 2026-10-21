"""Assemble a reviewable snapshot without modifying frozen research sources."""
from pathlib import Path
import hashlib
import json
import re

BASE = Path(__file__).resolve().parent
OUTPUT = BASE.parent / "Spectral_research_round4_2026-10-21.md"
MAIN = BASE / "report_main_ru.md"

PRIORITY = [
    "counter_one_step_pinching_hs.md",
    "audit_one_step_pinching_hs.md",
    "root_uniform_analytic_oscillation.md",
    "dual_audit_root_uniform_analytic_oscillation.md",
    "counter_center_phase_c17_bound.md",
    "dual_audit_center_phase_c17.md",
    "audit_explicit_symbol_finite_type16.md",
    "dual_audit_explicit_finite_type16.md",
    "root_all_entry_and_arbitrary_weyl_routes.md",
    "counter_all_entry_validation.md",
    "counter_audit_root_all_entry.md",
    "dual_audit_all_entry_arbitrary_routes.md",
    "dual_all_odd_sparse_cat_history_removal.md",
    "audit_all_odd_sparse_cat_history_removal.md",
    "dual_sparse_cat_schatten_trace_sharpening.md",
    "audit_sparse_cat_schatten_trace_sharpening.md",
    "root_arbitrary_routes_schatten_tail.md",
    "audit_arbitrary_routes_schatten_tail.md",
    "dual_arbitrary_routes_schatten_tail.md",
    "counter_no_exact_scalar_powers.md",
    "dual_audit_no_exact_scalar_powers.md",
    "counter_adjoint_reflection_obstruction.md",
    "dual_audit_adjoint_reflection_obstruction.md",
    "root_exact_identities_and_closure.md",
    "audit_exact_identities_and_closure.md",
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check_main(data):
    text = data.decode("utf-8")
    assert text.count(r"\[") == text.count(r"\]")
    for match in re.finditer(r"\\\[(.*?)\\\]", text, re.S):
        block = re.sub(r"\\[{}]", "", match.group(1))
        balance = 0
        for char in block:
            balance += (char == "{") - (char == "}")
            assert balance >= 0, ("negative TeX brace balance", match.start())
        assert balance == 0, ("TeX brace balance", match.start())
    assert "не получено" in text
    assert r"\Delta_{2,N}(b_*)" in text
    assert r"\tag{40}" in text


def main():
    missing = [name for name in PRIORITY if not (BASE / name).is_file()]
    if missing:
        raise SystemExit("Missing required frozen source/audit: " + ", ".join(missing))
    paths = [BASE / name for name in PRIORITY]
    extras = sorted(
        p for p in BASE.iterdir()
        if p.is_file() and p.suffix in {".md", ".py"}
        and p not in paths and p.name != MAIN.name
    )
    paths.extend(extras)
    main_data = MAIN.read_bytes()
    check_main(main_data)
    records = [
        {"file": MAIN.name, "bytes": len(main_data), "sha256": digest(main_data)}
    ]
    contents = []
    for path in paths:
        data = path.read_bytes()
        records.append(
            {"file": path.name, "bytes": len(data), "sha256": digest(data)}
        )
        contents.append((path, data))
    pieces = [main_data]
    preamble = (
        "\n\n# Приложения: зафиксированные доказательства и проверки\n\n"
        "Ниже включены полные текущие рукописи и независимые аудиты. "
        "Первые приложения образуют основную цепочку доказательств настоящей сводки; "
        "последующие сохраняют остальные ветви этого исследовательского прохода. "
        "Ранние промежуточные формулировки следует читать вместе с указанными аудитами "
        "и позднейшими усилениями. Никакое приложение не доказывает исходный "
        "спектральный предел. Имена файлов внутри рукописей обозначают источники "
        "в этой записи исследования; основной доказательный маршрут приведён выше.\n\n"
        "Рукописи сохраняются без редактирования. Контрольные суммы относятся "
        "к исходным UTF-8-файлам, а не к окружающим заголовкам приложения. "
        "Английский язык части приложений сохранён для точности записи; "
        "полное связное изложение основных результатов дано по-русски выше.\n\n"
        "## Реестр источников\n\n"
        "| № | Исходный файл | Байт | SHA-256 |\n"
        "|---:|---|---:|---|\n"
    )
    pieces.append(preamble.encode("utf-8"))
    for index, record in enumerate(records):
        row = (
            f"| {index} | {record['file']} | {record['bytes']} | "
            f"{record['sha256']} |\n"
        )
        pieces.append(row.encode("utf-8"))
    for index, (path, data) in enumerate(contents, 1):
        metadata = records[index]
        header = (
            f"\n\n# Приложение {index}. {path.name}\n\n"
            f"Контрольная сумма исходного текста: {metadata['sha256']}.\n\n"
            f"<!-- BEGIN SOURCE {path.name} -->\n"
        )
        pieces.append(header.encode("utf-8"))
        if path.suffix == ".py":
            pieces.append(bytes([96]) * 3 + b"python\n")
            pieces.append(data)
            pieces.append(b"\n" + bytes([96]) * 3 + b"\n")
        else:
            pieces.append(data)
        pieces.append(f"\n<!-- END SOURCE {path.name} -->\n".encode("utf-8"))
    result = b"".join(pieces)
    OUTPUT.write_bytes(result)
    manifest = {
        "artifact": str(OUTPUT),
        "artifact_bytes": len(result),
        "artifact_sha256": digest(result),
        "source_count": len(records),
        "sources": records,
        "status": "H_diag and its negation remain unproved for the prescribed family",
    }
    (BASE / "round4_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({k: v for k, v in manifest.items() if k != "sources"},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
