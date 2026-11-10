# Models

One test on public data lives here. The model code that mirrored the framework's equations retired with the math in the 2026-11 trim, and is in git history.

| File | What it is |
|---|---|
| `sat_bunching.py` | The simplified acquisition threshold test in [sat-threshold-test.md](../theory/02-research/sat-threshold-test.md). `--pull` fetches federal contract award counts from the USAspending API into `data/sat_counts.json`. A plain run computes the measures the test registered and prints the results table. Python, standard library only. |
| `data/sat_counts.json` | The counts pulled on 2026-11-09: 960 cells covering 1,244,037 awards. |

Run it from the repository root:

```bash
python3 models/sat_bunching.py
```

The output should match the table in section 4 of the test file. The script is not one of the three checks, because it reads data and not the documents.
