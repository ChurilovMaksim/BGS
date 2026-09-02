"""
RUN 6 / form factor on the pooled campaign data, using the EXACT run-2
protocol (src/form_factor.py: value-space Gaussian window, norm=sum(w^2),
average of |sum w e^{2pi i u tau}|^2/norm over spectra), with matched
RMT controls at the median multiplet dimension.
Artifact: artifacts/campaign_form_factor.json (overwritten, v2 protocol)
Pre-registered expectations:
  P1: rms(K_sym, GOE-ctl) < rms(K_sym, GUE-ctl)   on tau in [0.1,0.9]
  P2: rms(K_gen, GUE-ctl) < rms(K_gen, GOE-ctl)
  P3: both rms < rms vs Poisson / 5
"""
import json, os, sys
import numpy as np

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from form_factor import form_factor, controls

st = json.load(open(os.path.join(ART, "campaign_state.json")))
taus = np.linspace(0.05, 1.45, 29)

pools = {"sym": [], "gen": []}
dims_all = []
for r in st["runs"]:
    dims_all.extend(r["dims"])
    for tag in ("sym", "gen"):
        pools[tag].extend(np.asarray(u) for u in r.get("unfs", {}).get(tag, []))

m_ref = int(np.median(dims_all))
print(f"branches: sym={len(pools['sym'])} gen={len(pools['gen'])}, "
      f"m_ref={m_ref}")

Ks = form_factor(pools["sym"], taus)
Kg = form_factor(pools["gen"], taus)
ctl = controls(m_ref, reps=len(pools["sym"]), taus=taus)

goe_th = np.where(taus <= 1, 2*taus - taus*np.log(1+2*taus), 1.0)
gue_th = np.where(taus <= 1, taus, 1.0)

def rms(a, b, lo=0.1, hi=0.9):
    mk = (taus >= lo) & (taus <= hi)
    return float(np.sqrt(np.mean((np.asarray(a)[mk] - np.asarray(b)[mk])**2)))

verdict = {
    "rms_sym_goe_ctl": rms(Ks, ctl["GOE"]),
    "rms_sym_gue_ctl": rms(Ks, ctl["GUE"]),
    "rms_gen_gue_ctl": rms(Kg, ctl["GUE"]),
    "rms_gen_goe_ctl": rms(Kg, ctl["GOE"]),
    "rms_sym_poi":     rms(Ks, ctl["Poisson"]),
    "rms_gen_poi":     rms(Kg, ctl["Poisson"]),
    "rms_sym_goe_th":  rms(Ks, goe_th),
    "rms_gen_gue_th":  rms(Kg, gue_th),
}
verdict["P1"] = bool(verdict["rms_sym_goe_ctl"] < verdict["rms_sym_gue_ctl"])
verdict["P2"] = bool(verdict["rms_gen_gue_ctl"] < verdict["rms_gen_goe_ctl"])
verdict["P3"] = bool(verdict["rms_sym_poi"] < verdict["rms_sym_goe_ctl"] * 5 and
                     verdict["rms_gen_poi"] < verdict["rms_gen_gue_ctl"] * 5)

out = {"taus": taus.tolist(), "K_sym": Ks.tolist(), "K_gen": Kg.tolist(),
       "controls": {k: v.tolist() for k, v in ctl.items()},
       "goe_theory": goe_th.tolist(), "gue_theory": gue_th.tolist(),
       "m_ref": m_ref, "verdict": verdict,
       "all_pass": bool(verdict["P1"] and verdict["P2"] and verdict["P3"])}
json.dump(out, open(os.path.join(ART, "campaign_form_factor.json"), "w"), indent=1)

print(json.dumps(verdict, indent=1))
print("ALL PASS" if out["all_pass"] else "SOME FAIL")
for i in range(0, len(taus), 4):
    print(f"tau={taus[i]:5.2f} sym={Ks[i]:7.4f} (GOEc {ctl['GOE'][i]:6.4f}) | "
          f"gen={Kg[i]:7.4f} (GUEc {ctl['GUE'][i]:6.4f})")
