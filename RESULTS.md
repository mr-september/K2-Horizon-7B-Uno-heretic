# K2-Horizon-7B-Uno heretic — provenance record

Published: **https://huggingface.co/Flakily6416/K2-Horizon-7B-Uno-heretic** (public, Apache-2.0). Source: `hermitdave/K2-Horizon-7B-Uno-merged` @ `a831f34a5b35515a80fa1a373815e30a4b1065a0`. Full method/results claims live on the model card; workflow lessons live in skill `research/heretic-abliteration-workflow`. This file owns only reproduction provenance.

## Run

Heretic 2.0.0 (ARA, single combined pass), 2026-11-07. Scorers: refusal KeywordRate + sycophancy KeywordRate (`yco`, flattering system prompt) + KLDivergence. `run_heretic.py` is the trust_remote_code wrapper; `config.toml` the exact config; `checkpoints/study.jsonl` the 100-trial optuna study.

## Selected trial (#77)

| searched parameter | value | | outcome | value |
| --- | --- | --- | --- | --- |
| start_layer_index | 2 | | refusal rate | 3/100 (base 77/100) |
| end_layer_index | 34 | | sycophancy rate | 0/78 (base ≤22/78) |
| neighbor_count | 5 | | KL vs source | 0.191 |
| preserve_good_behavior_weight | 0.220 | | | |
| steer_bad_behavior_weight | 0.0002 | | | |
| overcorrect_relative_weight | 0.988 | | | |

Chosen from the 18-point Pareto front by behavior-per-KL (the 0/0 point cost KL 8.9). Dataset slices: harmful_behaviors train[:400] bad / harmless_alpaca train[:400] good / praise train[:210] bad(syc); eval on held-out test slices.

## What the 100 trials showed

Effective search space was 3-D: **aggression** (`overcorrect_relative_weight`, Pearson r −0.78 refusal / +0.51 KL; Spearman ρ −0.88 / +0.69) × **reach** (deep end-layers 32–36 needed for near-zero refusal) × **KL tax**. `neighbor_count`, `preserve_good_weight`, `steer_bad_weight` inert (steer driven to ~0). Tiny-KL trials (<0.06) are vacuous edits that kept refusing. Data: `trials.json` (dump via JournalStorage, study `heretic`); view: `trials.html` (linked 3D + KL×refusal plane + brushable parallel-coordinates strip (6 params → outcomes) + Spearman table; Pareto set recomputed in-page), built by `build_trials_html.py` from `trials_template.html` + `trials.json`. Superseded earlier views are in `archive_old_views/`.

