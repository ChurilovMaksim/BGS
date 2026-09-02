"""Literature harvest via the OpenAlex API (BGS project).

Usage:
    python lit_harvest.py             # bulk metadata for all queries
    python lit_harvest.py abstracts   # reconstruct abstracts for saved works

Raw JSON per query -> ../review/lit/<slug>.json ; consolidated index
-> ../review/lit/_index.json.  Re-runnable; deterministic order.
"""
import json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "review", "lit")
os.makedirs(OUT, exist_ok=True)

UA = {"User-Agent": "bgs-research/0.1 (mailto:research@example.org)"}

QUERIES = {
    "spacing":      "quantized cat map eigenvalue statistics level spacings",
    "kurlberg":     "Kurlberg Rudnick quantized cat maps distribution",
    "hecke":        "Hecke theory distribution eigenvalues quantized cat maps",
    "perturbed_wd": "perturbed cat maps spectral statistics degeneracy lifting",
    "formfactor":   "cat map form factor exponential sums moments Deligne",
    "que":          "quantum unique ergodicity linear maps Hecke eigenfunctions",
    "period":       "quantum period cat maps Faure Nonnenmacher De Bievre",
    "bgs_general":  "Bohigas Giannoni Schmit conjecture rigorous results",
}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)


def abstract_from_inverted(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))[:1200]


def bulk():
    index = {}
    for slug, q in QUERIES.items():
        url = ("https://api.openalex.org/works?search="
               + urllib.parse.quote(q) + "&per-page=10&mailto=r@example.org")
        try:
            d = fetch(url)
        except Exception as e:
            print(f"[FAIL] {slug}: {e}")
            continue
        json.dump(d, open(os.path.join(OUT, slug + ".json"), "w"))
        print(f"== {slug} (total {d.get('meta', {}).get('count')}) ==")
        for w in d.get("results", []):
            ids = w.get("ids", {}) or {}
            index[w["id"]] = {"title": w.get("title"), "year":
                              w.get("publication_year"), "slug": slug,
                              "cites": w.get("cited_by_count")}
            print(f"  {w.get('publication_year')} | c={w.get('cited_by_count'):>4}"
                  f" | {(w.get('title') or '')[:88]} | {ids.get('arxiv') or ''}")
        time.sleep(1.0)
    json.dump(index, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
    print(f"index: {len(index)} works")


def abstracts():
    index = json.load(open(os.path.join(OUT, "_index.json")))
    notes = []
    # shortlist: highest-cited works per query slug
    best = {}
    for wid, meta in index.items():
        s = meta["slug"]
        if s not in best or meta["cites"] > best[s]["cites"]:
            best[s] = {"id": wid, **meta}
    for slug, meta in sorted(best.items()):
        wid = meta["id"].rsplit("/", 1)[-1]
        try:
            d = fetch(f"https://api.openalex.org/works/{wid}?mailto=r@example.org")
        except Exception as e:
            print(f"[FAIL] {slug}: {e}")
            continue
        ab = abstract_from_inverted(d.get("abstract_inverted_index"))
        notes.append(f"## {slug} — {meta['title']} ({meta['year']}, "
                     f"cited {meta['cites']})\n{wid}\n{ab}\n")
        print(f"[ok] {slug}: {ab[:80]}...")
        time.sleep(1.0)
    open(os.path.join(OUT, "ABSTRACTS.md"), "w", encoding="utf-8").write(
        "# OpenAlex abstracts (shortlist)\n\n" + "\n".join(notes))
    print("saved ABSTRACTS.md")


if __name__ == "__main__":
    bulk() if len(sys.argv) < 2 else abstracts()
