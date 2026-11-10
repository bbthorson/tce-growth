"""The simplified acquisition threshold test, theory/02-research/sat-threshold-test.md.

Pulls federal contract award counts around the SAT from the USAspending API,
then computes M1 (bunching at a threshold, net of round-number heaping) and M2
(the extensive margin) for each group the test file names.

    python3 models/sat_bunching.py --pull     # fetch counts, write the cache
    python3 models/sat_bunching.py            # analyze the cached counts

Standard library only. The cache is models/data/sat_counts.json.
"""

import argparse
import json
import math
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://api.usaspending.gov/api/v2/search/spending_by_award_count/"
CACHE = os.path.join(os.path.dirname(__file__), "data", "sat_counts.json")

YEARS = list(range(2008, 2014))          # fiscal years
PRE, POST = YEARS[:3], YEARS[3:]          # SAT $100k, then $150k from FY2011
BIN = 5000
EDGES = list(range(50000, 250000, BIN))   # lower edge of each bin
VEHICLES = {"open": ["B", "D"], "order": ["A", "C"]}
KINDS = ["Product", "Service"]


def fetch(year, vehicle, kind, lo):
    body = {"filters": {
        "time_period": [{"start_date": f"{year - 1}-10-01",
                         "end_date": f"{year}-09-30",
                         "date_type": "date_signed"}],
        "award_type_codes": VEHICLES[vehicle],
        "psc_codes": {"require": [[kind]]},
        "award_amounts": [{"lower_bound": lo, "upper_bound": lo + BIN - 0.01}],
    }}
    req = urllib.request.Request(API, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    last = None
    for attempt in range(8):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.load(r)["results"]["contracts"]
        except Exception as e:
            last = e
            time.sleep(min(60, 2 ** attempt))
    raise RuntimeError(f"failed: {year} {vehicle} {kind} {lo}: {last}")


def key(y, v, k, lo):
    return f"{y}|{v}|{k}|{lo}"


def pull():
    """Resumable: completed counts are kept in a partial file between runs."""
    partial = CACHE + ".partial"
    done = {}
    if os.path.exists(partial):
        with open(partial) as f:
            done = json.load(f)
    jobs = [(y, v, k, lo) for y in YEARS for v in VEHICLES for k in KINDS
            for lo in EDGES if key(y, v, k, lo) not in done]
    print(f"{len(done)} cached, {len(jobs)} to fetch")
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)

    def run(j):
        try:
            return j, fetch(*j)
        except RuntimeError as e:
            print(e, file=sys.stderr)
            return j, None

    with ThreadPoolExecutor(max_workers=2) as pool:
        for i, (j, n) in enumerate(pool.map(run, jobs), 1):
            if n is not None:
                done[key(*j)] = n
            if i % 20 == 0 or i == len(jobs):
                with open(partial, "w") as f:
                    json.dump(done, f)
    missing = len(YEARS) * len(VEHICLES) * len(KINDS) * len(EDGES) - len(done)
    if missing:
        print(f"{missing} counts still missing; rerun --pull to resume")
        sys.exit(1)
    rows = [{"fy": y, "vehicle": v, "kind": k, "lo": lo,
             "n": done[key(y, v, k, lo)]}
            for y in YEARS for v in VEHICLES for k in KINDS for lo in EDGES]
    with open(CACHE, "w") as f:
        json.dump({"source": API, "pulled": time.strftime("%Y-%m-%d"),
                   "rows": rows}, f, indent=0)
    os.remove(partial)
    print(f"wrote {len(rows)} rows to {CACHE}")


def load():
    with open(CACHE) as f:
        return json.load(f)["rows"]


def total(rows, years, vehicles, kinds, lo, hi):
    """Count of awards with lo <= amount < hi."""
    return sum(r["n"] for r in rows if r["fy"] in years
               and r["vehicle"] in vehicles and r["kind"] in kinds
               and lo <= r["lo"] < hi)


def log_ratio(a, b):
    """log(a/b) and its Poisson standard error."""
    return math.log(a / b), math.sqrt(1 / a + 1 / b)


def m1(rows, vehicles, kinds, threshold):
    """Bunching at a threshold, in the years it applied minus the years it did not."""
    on, off = (PRE, POST) if threshold == 100000 else (POST, PRE)
    def lr(years):
        below = total(rows, years, vehicles, kinds, threshold - BIN, threshold)
        above = total(rows, years, vehicles, kinds, threshold, threshold + BIN)
        return log_ratio(below, above)
    (a, sa), (b, sb) = lr(on), lr(off)
    return a - b, math.hypot(sa, sb)


def m2(rows, vehicles, kinds, ref=(50000, 90000)):
    """Log change in the $90k-$150k window, less the change in a reference band."""
    w = log_ratio(total(rows, POST, vehicles, kinds, 90000, 150000),
                  total(rows, PRE, vehicles, kinds, 90000, 150000))
    r = log_ratio(total(rows, POST, vehicles, kinds, *ref),
                  total(rows, PRE, vehicles, kinds, *ref))
    return w[0] - r[0], math.hypot(w[1], r[1])


def fmt(x):
    return f"{x[0]:+.3f} ({x[1]:.3f})"


def analyze():
    rows = load()
    groups = {
        "open market, products": (["open"], ["Product"]),
        "open market, services": (["open"], ["Service"]),
        "open market, all": (["open"], KINDS),
        "orders, products": (["order"], ["Product"]),
        "orders, services": (["order"], ["Service"]),
        "orders, all": (["order"], KINDS),
    }
    print("| Group | M1 at $100k | M1 at $150k | M2, lower ref | M2, upper ref |")
    print("|---|---|---|---|---|")
    res = {}
    for name, (v, k) in groups.items():
        out = (m1(rows, v, k, 100000), m1(rows, v, k, 150000),
               m2(rows, v, k), m2(rows, v, k, (200000, 250000)))
        res[name] = out
        print(f"| {name} | " + " | ".join(fmt(x) for x in out) + " |")
    for j, label in ((2, "lower ref"), (3, "upper ref")):
        s, p = res["open market, services"][j], res["open market, products"][j]
        d, se = s[0] - p[0], math.hypot(s[1], p[1])
        differ = abs(d) > 2 * se and abs(d) > 0.05
        print(f"\nP2 ({label}): services minus products M2 = {d:+.3f} "
              f"(SE {se:.3f}); differ by the stated rule: {differ}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pull", action="store_true")
    args = ap.parse_args()
    if args.pull:
        pull()
    else:
        analyze()
