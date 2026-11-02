from wave47x_twins_search import search_inert
for (p, f) in [(11,2),(13,2)]:
    res = search_inert(p, f)
    print(f"inert p={p} f={f} mod={res['mod']} T={res['T']} groups={res['ngroups']} twin_groups={len(res['twins'])}", flush=True)
    for tw in res['twins'][:5]:
        print("   per", tw['per'], "size", tw['size'], "bad", tw['bad'], "rep", tw['rep'], flush=True)
