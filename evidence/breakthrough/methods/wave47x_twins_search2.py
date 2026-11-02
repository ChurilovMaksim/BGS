from wave47x_twins_search import search_split, search_inert
for (p, f) in [(7,2),(17,2),(23,2),(7,3)]:
    res = search_split(p, f, nonunits_only=True)
    print(f"split p={p} f={f} mod={res['mod']} T={res['T']} groups={res['ngroups']} twin_groups={len(res['twins'])}", flush=True)
    for tw in res['twins']:
        print("   per", tw['per'], "size", tw['size'], "pats", tw['pats'], "bad_sample", tw['bad'], "rep", tw['rep'], flush=True)
