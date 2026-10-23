#!/usr/bin/env python3
"""Maintain literature/references.bib, the canonical bibliography source.

references.bib is the single bibliographic source of record. It was
reconciled from the two previously maintained surfaces,
literature/bibliography.md (the annotated theorem-technology map) and
manuscript/unified_bibliography.tex (the manuscript's manual \\bibitem
list), by package P2-BIB; every entry of both surfaces is accounted for
in it exactly once, and the duplicate DOI 10.4171/JEMS/409
(Corvaja--Zannier 2013, attested on both surfaces) is resolved as the
single entry CorvajaZannier2013.

Modes:
  (no flag)    rewrite references.bib in canonical form (idempotent);
  --check      verify canonical form and cross-surface coverage:
               no duplicate key, DOI or arXiv identifier; every
               manuscript \\bibitem key is present and agrees with the
               .bib on year and on every stated identifier; every DOI
               and arXiv identifier stated in bibliography.md is
               accounted for by exactly one entry; the entries not in
               the manuscript list are exactly the pinned MD_ONLY set
               below, with pinned year and identifiers;
  --emit-tex   print the thebibliography block rendered from the .bib
               (the phase-4 conversion source for the manuscript list;
               this package does not apply it to the manuscript).

The surfaces are not edited by this script. Registered external
dependencies live in literature/external_dependencies.json and are a
separate registry, not part of this bibliography.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BIB = ROOT / "literature" / "references.bib"
BIBLIOGRAPHY_MD = ROOT / "literature" / "bibliography.md"
MANUSCRIPT_BIB = ROOT / "manuscript" / "unified_bibliography.tex"

FIELD_ORDER = [
    "author", "title", "journal", "booktitle", "series", "volume",
    "number", "pages", "year", "publisher", "doi", "eprint",
    "archiveprefix", "note",
]

# Entries attested only in literature/bibliography.md (no \bibitem in
# the manuscript list): key -> (year, doi or None, arXiv id or None,
# locator in bibliography.md). This table is the reviewed reconciliation
# record for those entries; changing a pinned value requires the same
# source review as changing the entry itself.
MD_ONLY = {
    "Roy2016": (2016, None, "1607.00579",
                "section 'Exponential independence' (Roy)"),
    "Rains2000": (2000, None, "math/0008079",
                  "section 'Haar power-map reference'"),
    "CohnKumar2007": (2007, None, "math/0607446",
                      "section 'Universal energy floor for pair Abel sums'"),
    "BenArousBourgade2013": (2013, "10.1214/11-AOP710", None,
                             "section 'Small CUE gaps'"),
    "Pesin1977": (1977, None, None,
                  "section 'Thermodynamic formalism' (Pesin 1977)"),
    "Ruelle1978": (1978, None, None,
                   "section 'Thermodynamic formalism' (Ruelle 1978)"),
    "ParryPollicott1990": (1990, None, None,
                           "section 'Thermodynamic formalism' (Parry--Pollicott 1990)"),
    "KurlbergRudnick2001": (2001, None, "math-ph/0101008",
                            "numbered item 1 (cat maps)"),
    "Rosenzweig2009": (2009, None, "0909.1410",
                       "numbered item 4 (cat maps)"),
    "GurevichHadani2011": (2011, "10.4007/annals.2011.174.1.1", None,
                           "numbered item 5 (cat maps)"),
    "GamburdLaffertyRockmore2003": (2003, "10.1088/0305-4470/36/12/336", None,
                                    "numbered item 9 (spectral spacing)"),
    "Carmichael1913": (1913, "10.2307/1967797", None,
                       "numbered item 14 (Fibonacci/Lucas)"),
    "BiluHanrotVoutier2001": (2001, "10.1515/crll.2001.080", None,
                              "numbered item 16 (Fibonacci/Lucas)"),
    "Apostol1970": (1970, "10.1090/S0002-9939-1970-0251010-X", None,
                    "numbered item 17 (Fibonacci/Lucas)"),
    "Baker2025": (2025, "10.1080/00029890.2024.2439819", "2309.02512",
                  "numbered item 18 (Fibonacci/Lucas)"),
    "MacourtShkredovShparlinski2018": (2018, "10.4153/CJM-2017-044-2", None,
                                       "numbered item 20 (Cayley energy)"),
    "RudnevWheeler2022": (2022, "10.1016/j.ffa.2021.101978", "2104.10534",
                          "numbered item 21 (Cayley energy)"),
    "FKM2015": (2015, "10.1098/rsta.2014.0309", None,
                "numbered item 24 (trace functions)"),
    "FKM2017": (2017, "10.5802/aif.3087", None,
                "numbered item 25 (trace functions)"),
    "SawinForeyFresanKowalski2023": (2023, "10.1090/jams/1008", None,
                                     "numbered item 26 (trace functions)"),
    "Michel1995": (1995, None, None,
                   "numbered item 28 (elliptic families)"),
    "Zarhin2013": (2013, "10.1017/S1474748012000655", "1012.5083",
                   "numbered item 29 (elliptic families)"),
    "GroveSaad2025": (2025, "10.1007/s40687-025-00554-2", None,
                      "numbered item 30 (elliptic families)"),
    "KielerFritzschBaecker2026": (2026, None, "2605.27052",
                                  "source check, 8 September 2026 (Kieler et al.)"),
    "Forrester1996": (1996, None, "chao-dyn/9603010",
                      "quadratic-noise continuation sources (Forrester)"),
    "Faure2007": (2007, None, "nlin/0610004",
                  "quadratic-noise continuation sources (Faure)"),
    "ChenEngelbrechtMirollo2017": (2017, "10.1088/1751-8121/aa7e39", "1707.00713",
                                   "section 'Moebius geometry background'"),
    "DiaconisEvans2001": (2001, "10.1090/S0002-9947-01-02800-8", None,
                          "signed Heisenberg source audit"),
    "ProcacciYuhjtman2015": (2015, None, "1508.07379",
                             "6 October 2026 registration (Procacci--Yuhjtman)"),
    "Demni2016": (2016, None, "1606.03755",
                  "6 October 2026 registration (Demni)"),
    "DemniHmidi2011": (2011, None, "1103.4693",
                       "6 October 2026 registration (Demni--Hmidi)"),
    "CebronOliveiraSantosYoussef2024": (2024, None, "2411.13062",
                                        "6 October 2026 registration (Cebron et al.)"),
}

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s{}\"<>]+")
ARXIV_RE = re.compile(
    r"(?:arXiv:|arxiv\.org/(?:abs|pdf|html)/)"
    r"((?:[a-z][a-z0-9\-]*/)?\d{4,7}(?:\.\d{4,5})?)(v\d+)?",
    re.IGNORECASE,
)
BIBITEM_RE = re.compile(r"\\bibitem(?:\[[^\]]*\])?\s*\{([^{}]+)\}")


def clean_doi(token: str) -> str:
    value = token
    changed = True
    while changed and value:
        changed = False
        while value and value[-1] in "`.,;":
            value = value[:-1]
            changed = True
        while value.endswith(")") and value.count(")") > value.count("("):
            value = value[:-1]
            changed = True
    return value.lower()


def find_dois(text: str) -> set[str]:
    return {clean_doi(m.group(0)) for m in DOI_RE.finditer(text)}


def find_arxiv(text: str) -> set[str]:
    return {m.group(1).lower() for m in ARXIV_RE.finditer(text)}


# ---------------------------------------------------------------- .bib model

class Entry:
    def __init__(self, comments, etype, key, fields):
        self.comments = comments          # list of verbatim comment lines
        self.etype = etype                # lowercased entry type
        self.key = key
        self.fields = fields              # dict name -> value (names lowercase)

    def doi(self):
        return self.fields.get("doi", "").lower() or None

    def eprint(self):
        return self.fields.get("eprint", "").lower() or None

    def year(self):
        raw = self.fields.get("year", "")
        return int(raw) if raw.isdigit() else None

    def mentioned_dois(self):
        found = set()
        if self.doi():
            found.add(self.doi())
        found |= find_dois(self.fields.get("note", ""))
        return found


def parse_bib(text: str) -> list[Entry]:
    entries = []
    pos, n = 0, len(text)
    pending_comments: list[str] = []
    while pos < n:
        line_end = text.find("\n", pos)
        if line_end == -1:
            line_end = n
        line = text[pos:line_end]
        if line.strip() == "" :
            pos = line_end + 1
            continue
        if line.lstrip().startswith("%"):
            pending_comments.append(line)
            pos = line_end + 1
            continue
        if not line.lstrip().startswith("@"):
            raise SystemExit(f"references.bib: unexpected content: {line[:60]!r}")
        match = re.match(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", line)
        if not match:
            raise SystemExit(f"references.bib: malformed entry head: {line[:60]!r}")
        etype, key = match.group(1).lower(), match.group(2)
        pos = line_end + 1
        fields: dict[str, str] = {}
        while True:
            # one field per line in canonical form; parse robustly anyway
            end = text.find("\n", pos)
            if end == -1:
                end = n
            fline = text[pos:end]
            if fline.strip() == "}":
                pos = end + 1
                break
            fm = re.match(r"\s*(\w+)\s*=\s*", fline)
            if not fm:
                raise SystemExit(
                    f"references.bib: malformed field line in {key}: {fline[:60]!r}")
            name = fm.group(1).lower()
            rest = fline[fm.end():]
            if rest.startswith("{"):
                depth, i = 0, 0
                while i < len(rest):
                    if rest[i] == "{":
                        depth += 1
                    elif rest[i] == "}":
                        depth -= 1
                        if depth == 0:
                            break
                    i += 1
                if depth != 0:
                    raise SystemExit(f"references.bib: unbalanced braces in {key}.{name}")
                value = rest[1:i]
                tail = rest[i + 1:].strip()
                if tail not in ("", ","):
                    raise SystemExit(
                        f"references.bib: trailing content in {key}.{name}: {tail!r}")
                pos = end + 1
            else:
                value = rest.rstrip(",").strip().strip('"')
                pos = end + 1
            if name in fields:
                raise SystemExit(f"references.bib: duplicate field {name} in {key}")
            fields[name] = value
        entries.append(Entry(pending_comments, etype, key, fields))
        pending_comments = []
    if pending_comments:
        raise SystemExit("references.bib: trailing comments with no entry")
    return entries


def serialize(entries: list[Entry]) -> str:
    out: list[str] = []
    for entry in entries:
        out.extend(entry.comments)
        out.append(f"@{entry.etype}{{{entry.key},")
        names = [f for f in FIELD_ORDER if f in entry.fields]
        names += sorted(f for f in entry.fields if f not in FIELD_ORDER)
        for name in names:
            out.append(f"  {name} = {{{entry.fields[name]}}},")
        out.append("}")
        out.append("")
    return "\n".join(out)


# ------------------------------------------------------------- surface scans

def split_bibitems(tex: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    matches = list(BIBITEM_RE.finditer(tex))
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(tex)
        blocks[match.group(1)] = tex[match.start():end]
    return blocks


def _plausible_year(value: int) -> bool:
    return 1900 <= value <= 2099


def tex_stated_year(block: str) -> int | None:
    body = block.split("}", 1)[1] if "}" in block else block
    for match in re.finditer(r"\((\d{4})\)", body):
        if _plausible_year(int(match.group(1))):
            return int(match.group(1))
    for match in re.finditer(r"(?<![\d./:])(\d{4})(?![\d])", body):
        value = int(match.group(1))
        if not _plausible_year(value):
            continue
        before = body[max(0, match.start() - 2):match.start()]
        after = body[match.end():match.end() + 2]
        if before.endswith("--") or after.startswith("--"):
            continue  # page range, not a year
        if after.startswith(".") and len(after) > 1 and after[1].isdigit():
            continue  # leading fragment of an arXiv id (1304.4556)
        return value
    ids = find_arxiv(block)
    for ident in ids:
        digits = ident.split("/")[-1]
        if len(digits) >= 2 and digits[:2].isdigit():
            yy = int(digits[:2])
            return 1900 + yy if yy >= 90 else 2000 + yy
    return None


# -------------------------------------------------------------------- checks

def check() -> list[str]:
    errors: list[str] = []
    if not BIB.is_file():
        return ["literature/references.bib is missing"]
    raw = BIB.read_text(encoding="utf-8")
    entries = parse_bib(raw)
    if serialize(entries) != raw:
        errors.append(
            "references.bib is not in canonical form; run render_bibliography.py")
    by_key: dict[str, Entry] = {}
    for entry in entries:
        if entry.key in by_key:
            errors.append(f"duplicate entry key: {entry.key}")
        by_key[entry.key] = entry
        for required in ("author", "title", "year"):
            if required not in entry.fields:
                errors.append(f"{entry.key}: missing required field {required}")
    doi_owner: dict[str, str] = {}
    eprint_owner: dict[str, str] = {}
    for entry in entries:
        if entry.doi():
            if entry.doi() in doi_owner:
                errors.append(
                    f"DOI {entry.doi()} claimed by both "
                    f"{doi_owner[entry.doi()]} and {entry.key}")
            doi_owner[entry.doi()] = entry.key
        if entry.eprint():
            if entry.eprint() in eprint_owner:
                errors.append(
                    f"arXiv id {entry.eprint()} claimed by both "
                    f"{eprint_owner[entry.eprint()]} and {entry.key}")
            eprint_owner[entry.eprint()] = entry.key

    # --- manuscript surface -------------------------------------------------
    tex = MANUSCRIPT_BIB.read_text(encoding="utf-8")
    blocks = split_bibitems(tex)
    md = BIBLIOGRAPHY_MD.read_text(encoding="utf-8")
    md_dois, md_arxiv = find_dois(md), find_arxiv(md)
    for key, block in blocks.items():
        entry = by_key.get(key)
        if entry is None:
            errors.append(f"manuscript \\bibitem{{{key}}} has no references.bib entry")
            continue
        stated = tex_stated_year(block)
        if stated is not None and entry.year() is not None and stated != entry.year():
            errors.append(
                f"{key}: manuscript states year {stated}, references.bib has "
                f"{entry.year()}")
        for doi in find_dois(block):
            if doi != entry.doi() and doi not in entry.mentioned_dois():
                errors.append(
                    f"{key}: manuscript states DOI {doi}, references.bib does not")
        extra_dois = entry.mentioned_dois() - find_dois(block)
        for doi in extra_dois:
            if doi not in md_dois:
                errors.append(
                    f"{key}: references.bib DOI {doi} is attested on neither surface")
        tex_ids = find_arxiv(block)
        bib_ids = {entry.eprint()} if entry.eprint() else set()
        if not tex_ids <= bib_ids:
            errors.append(
                f"{key}: manuscript arXiv ids {sorted(tex_ids)} not matched by "
                f"references.bib {sorted(bib_ids)}")
        for ident in bib_ids - tex_ids:
            if ident not in md_arxiv:
                errors.append(
                    f"{key}: references.bib arXiv id {ident} is attested on "
                    "neither surface")

    # --- bibliography.md surface --------------------------------------------
    mention_owner: dict[str, set[str]] = {}
    for entry in entries:
        for doi in entry.mentioned_dois():
            mention_owner.setdefault(doi, set()).add(entry.key)
        if entry.eprint():
            mention_owner.setdefault(entry.eprint(), set()).add(entry.key)
    for doi in sorted(md_dois):
        owners = mention_owner.get(doi, set())
        if len(owners) != 1:
            errors.append(
                f"bibliography.md DOI {doi} is accounted for by "
                f"{len(owners)} references.bib entries (expected exactly 1)")
    for ident in sorted(md_arxiv):
        owners = mention_owner.get(ident, set())
        if len(owners) != 1:
            errors.append(
                f"bibliography.md arXiv id {ident} is accounted for by "
                f"{len(owners)} references.bib entries (expected exactly 1)")

    # --- md-only accounting ---------------------------------------------------
    extra_keys = set(by_key) - set(blocks)
    if extra_keys != set(MD_ONLY):
        errors.append(
            "references.bib entries outside the manuscript list differ from "
            f"the pinned MD_ONLY set: extra={sorted(extra_keys - set(MD_ONLY))}, "
            f"missing={sorted(set(MD_ONLY) - extra_keys)}")
    for key, (year, doi, eprint, locator) in MD_ONLY.items():
        entry = by_key.get(key)
        if entry is None:
            continue
        if entry.year() != year:
            errors.append(f"{key}: pinned year {year} ({locator}), "
                          f"references.bib has {entry.year()}")
        if (entry.doi() or None) != (doi.lower() if doi else None):
            errors.append(f"{key}: pinned DOI {doi} ({locator}), "
                          f"references.bib has {entry.doi()}")
        if (entry.eprint() or None) != eprint:
            errors.append(f"{key}: pinned arXiv id {eprint} ({locator}), "
                          f"references.bib has {entry.eprint()}")
    return errors


# ----------------------------------------------------------------- emit tex

def tex_authors(author_field: str) -> str:
    names = []
    for name in author_field.split(" and "):
        if "," in name:
            last, given = name.split(",", 1)
            initials = given.strip().replace(" ", "~")
            names.append(f"{initials}~{last.strip()}" if initials else last.strip())
        else:
            names.append(name.strip())
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return " and ".join(names)
    return ", ".join(names[:-1]) + " and " + names[-1]


def emit_tex(entries: list[Entry]) -> str:
    tex = MANUSCRIPT_BIB.read_text(encoding="utf-8")
    blocks = split_bibitems(tex)
    order = [key for key in blocks if key in {e.key for e in entries}]
    by_key = {e.key: e for e in entries}
    further_at = tex.find("Further reading")
    further_keys = set()
    if further_at != -1:
        further_keys = {k for k, blk in blocks.items()
                        if tex.find(blk) > further_at}
    out = ["\\begin{thebibliography}{99}", "\\small", ""]
    in_further = False
    for key in order:
        entry = by_key[key]
        if key in further_keys and not in_further:
            out += ["% --- Further reading "
                    "-------------------------------------------------",
                    "% The entries below are retained as background reading; "
                    "unlike the",
                    "% entries above, they are not cited in the text.",
                    "\\item[] \\textbf{Further reading.} The following entries "
                    "are retained",
                    "as background reading; they are not cited in the text.",
                    ""]
            in_further = True
        f = entry.fields
        lines = [f"\\bibitem{{{key}}}",
                 f"{tex_authors(f['author'])},",
                 f"\\emph{{{f['title']}}},"]
        if entry.etype == "article" and "journal" in f:
            venue = f["journal"]
            if "volume" in f:
                venue += f" \\textbf{{{f['volume']}}}"
            venue += f" ({f['year']})"
            if "pages" in f:
                venue += f", {f['pages']}"
            lines.append(venue + ",")
        elif entry.etype == "book":
            venue = f.get("series", f.get("publisher", ""))
            if "volume" in f:
                venue += f" \\textbf{{{f['volume']}}}"
            lines.append(venue + f", {f['year']},")
        else:
            lines.append(f"({f['year']}),")
        tail = []
        if entry.doi():
            tail.append(f"doi:{entry.doi()}")
        if entry.eprint():
            version = ""
            tail.append(f"arXiv:{entry.eprint()}{version}")
        if tail:
            lines.append("; ".join(tail) + ".")
        else:
            lines[-1] = lines[-1].rstrip(",") + "."
        if "note" in f:
            lines.append(f["note"] + ".")
        out += lines + [""]
    out.append("\\end{thebibliography}")
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--emit-tex", action="store_true")
    args = parser.parse_args()
    if args.emit_tex:
        entries = parse_bib(BIB.read_text(encoding="utf-8"))
        print(emit_tex(entries), end="")
        return 0
    if args.check:
        errors = check()
        if errors:
            for error in errors:
                print(f"render_bibliography: {error}")
            raise SystemExit(
                f"bibliography check failed with {len(errors)} error(s)")
        print("bibliography-render: OK")
        return 0
    entries = parse_bib(BIB.read_text(encoding="utf-8"))
    BIB.write_text(serialize(entries), encoding="utf-8")
    print(BIB.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
