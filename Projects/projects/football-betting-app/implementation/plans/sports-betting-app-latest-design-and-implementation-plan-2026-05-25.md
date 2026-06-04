# Sports Betting App: Latest Design And Implementation Plan

Date: 2026-05-25

Working product name: **LineValue Football**

## Product Direction

Build a web-first football betting analytics product, not a generic "AI acca tips" app.

The product should help disciplined bettors:

- Compare model-estimated probabilities against bookmaker odds.
- Find possible value where the model disagrees with the market.
- Log the odds and stake they actually take.
- Track closing-line value, profit/loss, drawdown and bankroll exposure.
- Understand uncertainty and avoid irresponsible betting behaviour.

Accumulators should not be the main product promise. They can exist later as a simulation/risk-education feature.

## Positioning

One-line positioning:

> Transparent football value analysis for bettors who care about price, probability, bankroll and closing-line proof.

Tone:

- Serious, calm and evidence-led.
- Use "estimated probability", "model edge", "closing-line value", "bankroll limits" and "decision support".
- Avoid "guaranteed wins", "beat the bookies", "VIP tips", "daily acca" and income-style language.
- Treat responsible gambling as a core product feature, not footer compliance.

## Core MVP Screens

### 1. Home / Landing Page

Purpose: convert serious football bettors into beta users by showing a credible analytics product.

Key sections:

- Header: LineValue Football, Methodology, Public Record, Pricing, Responsible Gambling, Sign In, Join Beta.
- Hero: "Find where your football model disagrees with the market."
- Dashboard preview: today's value board, bankroll exposure, CLV trend, public record snippet.
- Explanation of model probability vs implied probability, edge, odds timestamp, stake range and CLV.
- "Why not acca-first?" section explaining variance and why singles are easier to evaluate.
- Responsible gambling note: 18+, decision-support only, no automated betting, no guarantees.

### 2. Dashboard / Value Board

Purpose: give users a daily working surface for finding and evaluating possible single-bet value.

Filters:

- Country
- League
- Market
- Kickoff window
- Minimum edge
- Minimum confidence
- Odds range
- Bookmaker availability

Opportunity row fields:

- Fixture and kickoff time
- Market and selection
- Model probability
- Best odds
- Market implied probability
- Estimated edge
- Confidence band
- Suggested stake range
- Bookmaker timestamp
- Actions: View Detail, Log Bet

Side panel:

- Current bankroll
- Daily exposure
- Stake cap
- Last 30 logged bets CLV
- Responsible-gambling link

### 3. Match Detail

Purpose: explain why an opportunity is flagged before the user logs anything.

Core fields:

- Fixture, competition and kickoff time
- Selection, market, model probability, best odds, implied probability and estimated edge
- Odds movement by bookmaker
- Model notes: recent form, home/away adjustment, schedule congestion, data quality flag and confidence
- Log bet modal: bookmaker, odds taken, stake, bet time, notes and confirmation checkbox

Accumulator entry:

- "Add to simulation"
- Warning: "Accumulator simulations increase variance and are not default recommendations."

### 4. Bet Tracker

Purpose: separate model quality from user execution.

Summary:

- Current bankroll
- Total stake
- Profit/loss
- Yield
- ROI
- Drawdown
- Average CLV

Table:

- Date
- Fixture
- Market
- Selection
- Odds taken
- Closing odds
- CLV
- Stake
- Result
- Profit/loss
- Notes

### 5. Public Record

Purpose: build trust before conversion and reduce black-box tipster scepticism.

Metrics:

- Total logged opportunities
- Average CLV
- Yield
- ROI
- Drawdown
- Average odds
- Hit rate

Breakdowns:

- League
- Market
- Odds band
- Month

Required copy:

> Historical performance does not guarantee future outcomes. The public record includes losing periods and should be read as evidence of process, not certainty.

### 6. Methodology

Purpose: explain enough to earn trust without overclaiming.

Sections:

- How model probability is estimated
- How implied probability is calculated from decimal odds
- How edge is calculated
- What CLV means and why it matters
- Why singles are the default
- What data is used
- Known limitations
- Update cadence
- Responsible use of the tool

### 7. Pricing

Initial pricing hypothesis:

- Free / Watchlist: limited fixture board, public record, education, 20 manual tracked bets per month.
- Pro: GBP14.99-GBP24.99/month, full value board, bookmaker filters, unlimited bet tracking, CLV tracking, bankroll rules, saved filters, CSV export.
- Analyst: GBP49-GBP79/month, advanced filters, historical splits, strategy backtesting, alert thresholds, priority beta access.

Pricing copy:

> Subscription pays for analytics, tracking and data access. It does not buy guaranteed profit.

### 8. Responsible Gambling

Required elements:

- 18+ notice
- "Only bet what you can afford to lose"
- Bankroll limits
- Cooling-off explanation
- Self-exclusion and support resources by market
- No automated betting statement
- No guarantee statement
- Contact for support and account closure

## Implementation Status

Done:

- Product research report exists: `reports/football-value-betting-acca-app-research-2026-05-23.md`.
- Web MVP wireframe/design plan exists: `reports/football-value-betting-web-mvp-wireframes-2026-05-23.md`.
- Data model and ingestion implementation plan exists: `sports-prediction-model/data-model-and-ingestion-implementation-plan-2026-05-24.md`.

Not yet done before this document:

- A full end-to-end app implementation plan tying frontend, backend, modelling, ingestion, auth, payments and launch sequencing together.
- A build-ready PRD with milestones and acceptance criteria.
- A technical repo scaffold for this specific product.

This document fills the implementation-plan gap at MVP level.

## Recommended MVP Architecture

### Frontend

- Web-first app.
- React / Next.js is the practical default unless an existing repo dictates otherwise.
- Responsive dashboard layout for desktop first, with mobile support for tracker and match detail.
- UI should feel like a quiet analytics console, not a casino or tipster site.

### Backend

- API service for fixtures, odds, model opportunities, bet logs, public record and account settings.
- Postgres for canonical app data.
- Object storage or local raw-file storage for provider payloads.
- Background jobs for ingestion and settlement.

### Data / Modelling Layer

Use the existing data-model plan as the foundation:

- Store raw provider payloads unchanged.
- Normalize into canonical competitions, seasons, teams, fixtures, odds snapshots and results.
- Build time-aware feature snapshots so backtests only use data known at prediction time.
- Keep closing odds separate from prediction-time odds to avoid leakage.
- Track source, timestamp, confidence and missing reason for important features.

### Suggested Initial Stack

- Next.js + TypeScript for the web app.
- Postgres for app and canonical betting data.
- Python 3.12 for ingestion and modelling jobs.
- DuckDB/Parquet for offline modelling datasets.
- `httpx`, `pydantic`, `tenacity`, `pandas` or `polars` for provider adapters and transforms.
- `pytest` for ingestion/model tests.
- GitHub Actions for CI.

## Build Milestones

### Milestone 0: Product Skeleton

Deliver:

- Repo scaffold.
- Landing page shell.
- Auth placeholder or real auth decision.
- Dashboard shell using mocked data.
- Responsible-gambling footer and disclaimer copy.

Acceptance criteria:

- App runs locally.
- User can view home/dashboard hybrid first screen.
- Mock value board, bankroll panel and public record preview render cleanly.

### Milestone 1: Bet Tracker MVP

Deliver:

- User-created manual bet log.
- Bankroll settings.
- Profit/loss, ROI, yield and drawdown calculations.
- CSV export.

Acceptance criteria:

- User can add, edit and delete logged bets.
- Settlement state updates metrics.
- Bankroll exposure warnings display.

### Milestone 2: Static Data Ingestion

Deliver:

- Import historical football results and odds from prototype sources such as Football-Data.co.uk.
- Canonical fixture, team, competition, odds and result tables.
- Basic data quality checks.

Acceptance criteria:

- Historical fixtures and odds can be loaded repeatably.
- Provider IDs map to canonical entities.
- Backtest queries can access only time-appropriate rows.

### Milestone 3: Baseline Model And Value Board

Deliver:

- Simple baseline probability model.
- Implied probability and bookmaker margin removal.
- Edge calculation.
- Value board powered by stored odds and model probabilities.

Acceptance criteria:

- Each opportunity shows model probability, implied probability, edge and confidence.
- Opportunities can be filtered by league, market, odds range and minimum edge.
- Model outputs are labelled as estimates with confidence and limitations.

### Milestone 4: Closing-Line Value And Public Record

Deliver:

- Closing odds capture.
- CLV calculation.
- Public record page.
- Performance splits by league, market, odds band and month.

Acceptance criteria:

- Logged opportunities can be compared with closing odds.
- Public record includes losing periods as well as wins.
- Metrics do not overclaim profitability.

### Milestone 5: Live Odds Trial

Deliver:

- Trial one odds provider.
- Scheduled odds ingestion.
- Odds freshness timestamps.
- Basic provider reliability and cost report.

Acceptance criteria:

- Fresh odds appear in the value board with provider and timestamp.
- Stale odds are flagged or excluded.
- Provider coverage is measured against target leagues.

### Milestone 6: Beta Launch

Deliver:

- Pricing page.
- Beta signup.
- Account settings.
- Responsible-gambling settings.
- Terms/privacy/compliance review checklist.

Acceptance criteria:

- Beta users can sign up, track bets and use the value board.
- All screens carry suitable risk language.
- No automated betting or bookmaker affiliate flow is enabled without legal review.

## Compliance Notes

This product should be treated as betting-adjacent and compliance-sensitive.

Before public launch:

- Get specialist gambling/legal review for target markets.
- Avoid placing bets for users, handling stakes, pooling funds or automating execution.
- Avoid aggressive performance claims.
- Avoid bookmaker affiliate links until legal/compliance review approves the exact flow.
- Add age gating, responsible-gambling resources and account closure/cooling-off support.

## Immediate Next Build Step

Build a clickable web MVP shell with mocked data:

- Home/dashboard hybrid first screen.
- Value board.
- Match detail modal/page.
- Manual bet tracker.
- Bankroll and CLV side panel.
- Public record preview.
- Responsible-gambling strip.

This validates the product workflow before spending money on live odds/data feeds.
