#!/usr/bin/env python3
"""Regenerate the CSV certificates for Supplementary Material S1.
This script uses only the Python standard library and writes all outputs to ../output.
"""
from pathlib import Path
import csv, math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
CONFIG = ROOT / "config"
OUT.mkdir(exist_ok=True)

def read_caps():
    with open(CONFIG / "capabilities.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for key in ["alpha", "eta", "c_plus", "c_minus"]:
            r[key] = float(r[key])
    return rows

def write_csv(path, fields, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

def main():
    caps = read_caps()
    table2, table3, tableS1 = [], [], []
    for c in caps:
        phi = c["alpha"] / c["eta"]
        a = c["c_plus"] / c["eta"]
        b = c["c_minus"] / c["eta"]
        tplus = phi - a
        tminus = phi + b
        rho = tminus - tplus
        # Use a tolerance-aware ceiling so exact theoretical integers such as 2.0
        # are not rounded upward by binary floating-point artifacts.
        ceil_tplus = math.ceil(round(tplus, 12))
        ceil_tminus = math.ceil(round(tminus, 12))
        err = abs((ceil_tminus - ceil_tplus) - rho)
        table2.append({"capability": c["capability"], "description": c["description"], "d": c["d"], "alpha": c["alpha"], "eta": c["eta"], "c_plus": c["c_plus"], "c_minus": c["c_minus"], "phi": round(phi,4), "prerequisites": c["prerequisites"] or "-"})
        table3.append({"capability": c["capability"], "T_plus": round(tplus,4), "T_minus": round(tminus,4), "ceil_T_plus": ceil_tplus, "ceil_T_minus": ceil_tminus, "rho": round(rho,4), "abs_error": round(err,4)})
        tableS1.append({"capability": c["capability"], "phi": round(phi,4), "a": round(a,4), "b": round(b,4), "T_plus": round(tplus,4), "T_minus": round(tminus,4)})
    write_csv(OUT / "manuscript_table2_capability_parameters.csv", list(table2[0].keys()), table2)
    write_csv(OUT / "manuscript_table3_threshold_verification.csv", list(table3[0].keys()), table3)
    write_csv(OUT / "supplementary_tableS1_frictionless_friction_decomposition.csv", list(tableS1[0].keys()), tableS1)
    # Static certificates used in the manuscript trace.
    write_csv(OUT / "greedy_acquisition_path.csv", ["step","current_set","chosen_trigger","added_package","cumulative_cost"], [
        {"step":0,"current_set":"{}","chosen_trigger":"c1","added_package":"{c1}","cumulative_cost":1.0},
        {"step":1,"current_set":"{c1}","chosen_trigger":"c3","added_package":"{c3}","cumulative_cost":1.8},
        {"step":2,"current_set":"{c1,c3}","chosen_trigger":"c5","added_package":"{c2,c5}","cumulative_cost":5.3},
    ])
    print("Regenerated CEJOR Supplementary Material S1 outputs in", OUT)

if __name__ == "__main__":
    main()
