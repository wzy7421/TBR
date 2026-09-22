# Data dictionary

This repository is structured around the main repeated-measures study reported in the manuscript.

## 1. Trial-level behavioral data

Recommended public file: `data/main_trials.csv`

Expected rows after release: **14,400** (120 participants × 120 formal trials).

| Variable | Type | Coding / meaning |
|---|---|---|
| participant_id | string | Pseudonymous ID, e.g. P001–P120 |
| block_order_sequence | integer | Balanced Latin-square sequence, 1–4 |
| block_position | integer | Position of current block, 1–4 |
| trial_index_global | integer | Formal-trial index within participant, 1–120 |
| trial_index_block | integer | Trial index within block |
| block | categorical | Agent-Utilitarian; Agent-Ethical; Team-Utilitarian; Team-Ethical |
| decision_context | categorical | Utilitarian; Ethical |
| target_level | categorical | Agent; Team |
| target_configuration | categorical | Human; AI; H-H; H-AI; AI-AI |
| outcome_valence | categorical | Gain; Loss; Reward; Blame |
| outcome_valence_binary | integer | 0 = favorable (Gain/Reward); 1 = adverse (Loss/Blame) |
| outcome_magnitude | categorical | Low; High |
| repetition | integer | 1–3 within each elementary cell |
| acceptance | integer | 0 = Reject; 1 = Accept |
| rt_ms | numeric | Reaction time in milliseconds |

Design constraints per participant:
- Agent-Utilitarian: 24 rows
- Agent-Ethical: 24 rows
- Team-Utilitarian: 36 rows
- Team-Ethical: 36 rows
- Total: 120 rows

Each execution-target × valence × magnitude cell contains three repeated decisions per participant.

## 2. Post-block responsibility measures

Recommended public file: `data/postblock_responsibility.csv`

The responsibility-perception instrument contains 7 cognitive items and 6 affective items, each rated 1–7.

| Variable | Type | Coding / meaning |
|---|---|---|
| participant_id | string | Same pseudonymous ID as trial data |
| block | categorical | One of the four blocks |
| decision_context | categorical | Utilitarian; Ethical |
| target_level | categorical | Agent; Team |
| target_configuration | categorical | Human; AI; H-H; H-AI; AI-AI |
| cog_1 ... cog_7 | integer | Cognitive-responsibility items, 1–7 |
| aff_1 ... aff_6 | integer | Affective-responsibility items, 1–7 |
| cognitive_mean | numeric | Mean of cog_1 ... cog_7 |
| affective_mean | numeric | Mean of aff_1 ... aff_6 |
| responsibility_attribution_pct | numeric | Context-specific responsibility attribution, 0–100 |

Expected row structure if one rating set is retained for every evaluated target within each block:
- 2 Agent-Utilitarian targets
- 2 Agent-Ethical targets
- 3 Team-Utilitarian targets
- 3 Team-Ethical targets
= 10 target-level post-block records per participant, or 1,200 rows total.

This expected count must be checked against the original experiment export before release.

## 3. Participant data

Recommended public file: `data/participants.csv`

Only variables needed for reproducibility should be released at participant level. Direct identifiers must not be included.

Suggested columns:
- participant_id
- block_order_sequence
- age_years, if ethics/consent permits
- gender, if ethics/consent permits
- work_experience_category
- industry_background
- job_role
- ai_use_frequency
- ai_assisted_decision_experience
- organizational_decision_experience
- ai_literacy_mean, if retained in the original analysis file

Sensitive screening information should remain aggregate unless participant-level public sharing was explicitly covered by consent and ethics approval.

## 4. Derived condition-level data

The manuscript aggregates the three binary decisions in each participant × target × valence × magnitude cell into an acceptance rate from 0 to 1. This creates:
- 8 cells per agent block
- 12 cells per team block
- 40 cells per participant
- 4,800 condition-level rows total

The supplied preparation script can generate this file from the real trial-level data.

## 5. Timing and interpretation

Acceptance and RT were recorded during behavioral trials. Responsibility perception and context-specific responsibility attribution were collected after the corresponding blocks. They should therefore be treated as post-block measures and not as temporally prior mediators of individual trial choices.
