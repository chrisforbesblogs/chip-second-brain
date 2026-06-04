# Sports Prediction Model Working Folder

This folder contains the working documents for the scalable league-sports prediction model project.

## Files

- `soccer-results-model-proposal-2026-05-24.md`  
  Main proposal and implementation direction.

- `football-probability-model-research-2026-05-24.md`  
  Research note on football probability models, including Sumpter/Soccermatics, Elo, Poisson, Dixon-Coles, Bayesian approaches and model ranking.

- `chipthink-scalable-sports-prediction-platform-research-2026-05-24.md`  
  ChipThink second-opinion research on the broader product/model strategy.

- `chipthink-sports-prediction-feature-data-layers-2026-05-24.md`  
  ChipThink research on xG, player/lineup and context feature data sources and ingestion.

- `data-model-and-ingestion-implementation-plan-2026-05-24.md`  
  Concrete data model, ingestion architecture, provider adapter plan, tooling stack, quality checks and implementation phases.

## Current Direction

Build a calibrated probability infrastructure platform for league-based sports, starting with football/soccer:

1. Base model: Elo/team strength plus Dixon-Coles football scoring.
2. Feature layers: context everywhere, player/lineup where coverage exists, xG/event data for rich leagues.
3. Ingestion: provider adapters, raw payload store, canonical normalization, entity resolution, feature snapshots and quality monitoring.
4. Evaluation: log loss, Brier score, ranked probability score, calibration plots and closing-line comparison.
