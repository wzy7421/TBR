# TBR — The Burden of Responsibility in Human–AI Interaction

Public research materials and data-release package for:

**The Burden of Responsibility in Human–AI Interaction: How Outcome Valence Shapes Responsibility Attribution and Algorithmic Delegation**

Authors: Zhenyu Wang; Jianmin Wang

## Study overview

The main study used a repeated-measures design with **120 working professionals**. Each participant completed four experimental blocks:

1. Agent–Utilitarian: Human vs. AI × Gain vs. Loss × Low vs. High magnitude × 3 repetitions = 24 trials
2. Agent–Ethical: Human vs. AI × Reward vs. Blame × Low vs. High magnitude × 3 repetitions = 24 trials
3. Team–Utilitarian: H–H vs. H–AI vs. AI–AI × Gain vs. Loss × Low vs. High magnitude × 3 repetitions = 36 trials
4. Team–Ethical: H–H vs. H–AI vs. AI–AI × Reward vs. Blame × Low vs. High magnitude × 3 repetitions = 36 trials

This yields **120 formal trials per participant** and **14,400 trial-level behavioral observations** in the main study.

Primary behavioral outcome: task-allocation acceptance (0 = reject, 1 = accept).  
Secondary behavioral outcome: reaction time in milliseconds.  
Post-block measures: cognitive responsibility perception, affective responsibility perception, and context-specific responsibility attribution.

Ethics approval reported in the manuscript: Tongji University IRB, **tjdxsr2026050**.

## Repository contents

- `templates/` — schemas for the de-identified participant-level release
- `data/reported_summary/` — values already reported in the manuscript tables
- `materials/` — experimental scenarios and responsibility-perception items
- `scripts/` — validation and condition-level data preparation utilities
- `DATA_DICTIONARY.md` — variable definitions and coding
- `CITATION.cff` — citation metadata

## Important data-status note

The files under `data/reported_summary/` reproduce **reported aggregate/statistical values from the manuscript**. They are not reconstructed participant-level observations.

The files under `templates/` are **empty schemas** for release of the real de-identified source data. No synthetic or reconstructed participant-level observations are represented as empirical data in this repository.

Before using this repository as the final Data Availability link for the article, the authors should populate the templates from the original experimental records (or deposit an equivalent de-identified export), verify privacy/consent constraints, and run the validation script.

## Recommended archival release

For a journal data-availability statement, archive a tagged release of this repository in a recognized research-data repository such as **Zenodo** or **OSF** and cite the resulting persistent DOI/URL. A GitHub repository is useful for versioned materials and code, but an archival repository provides the persistent identifier expected by many journals.

## Privacy

Do not upload names, email addresses, telephone numbers, IP addresses, employer names, free-text identifiers, or other direct identifiers. Public participant-level files should use pseudonymous IDs only (for example, P001–P120). Sensitive screening information should remain aggregate unless the consent and ethics documentation explicitly permit participant-level sharing.
