import sys
import pandas as pd

TRIAL_BLOCK_COUNTS = {
    "Agent-Utilitarian": 24,
    "Agent-Ethical": 24,
    "Team-Utilitarian": 36,
    "Team-Ethical": 36,
}

def fail(msg):
    raise AssertionError(msg)

def validate_trials(path):
    df = pd.read_csv(path)

    required = {
        "participant_id", "block_order_sequence", "block_position",
        "trial_index_global", "trial_index_block", "block", "decision_context",
        "target_level", "target_configuration", "outcome_valence",
        "outcome_valence_binary", "outcome_magnitude", "repetition",
        "acceptance", "rt_ms"
    }
    missing = required - set(df.columns)
    if missing:
        fail(f"Missing required columns: {sorted(missing)}")

    if df["participant_id"].nunique() != 120:
        fail(f"Expected 120 participants, found {df['participant_id'].nunique()}")

    if len(df) != 14400:
        fail(f"Expected 14,400 trial rows, found {len(df)}")

    if not set(df["acceptance"].dropna().unique()).issubset({0, 1}):
        fail("acceptance must be coded 0/1")

    if (df["rt_ms"].dropna() <= 0).any():
        fail("rt_ms must be positive")

    for pid, g in df.groupby("participant_id"):
        if len(g) != 120:
            fail(f"{pid}: expected 120 trials, found {len(g)}")
        counts = g["block"].value_counts().to_dict()
        for block, expected in TRIAL_BLOCK_COUNTS.items():
            if counts.get(block, 0) != expected:
                fail(f"{pid}: {block} expected {expected}, found {counts.get(block, 0)}")

    print("PASS: trial-level file satisfies the manuscript design constraints.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_release.py data/main_trials.csv")
        sys.exit(2)
    validate_trials(sys.argv[1])
