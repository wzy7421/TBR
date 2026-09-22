import sys
import numpy as np
import pandas as pd

if len(sys.argv) != 3:
    print("Usage: python scripts/prepare_condition_level.py data/main_trials.csv data/condition_level.csv")
    raise SystemExit(2)

src, out = sys.argv[1], sys.argv[2]
df = pd.read_csv(src)

df["log_rt"] = np.log(df["rt_ms"])

group_cols = [
    "participant_id",
    "block",
    "decision_context",
    "target_level",
    "target_configuration",
    "outcome_valence",
    "outcome_valence_binary",
    "outcome_magnitude",
]

agg = (
    df.groupby(group_cols, as_index=False)
      .agg(
          n_trials=("acceptance", "size"),
          acceptance_rate=("acceptance", "mean"),
          mean_rt_ms=("rt_ms", "mean"),
          mean_log_rt=("log_rt", "mean"),
      )
)

if len(agg) != 4800:
    raise AssertionError(f"Expected 4,800 condition-level rows, found {len(agg)}")

if not (agg["n_trials"] == 3).all():
    raise AssertionError("Every participant × target × valence × magnitude cell should contain 3 trials.")

agg.to_csv(out, index=False)
print(f"Wrote {len(agg)} rows to {out}")
