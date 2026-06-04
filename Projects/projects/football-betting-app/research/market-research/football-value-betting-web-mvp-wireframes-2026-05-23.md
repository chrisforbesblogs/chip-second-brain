# Web MVP Wireframes: Transparent Football Betting Analytics

Date: 2026-05-23  
Prepared by: ChipThink

## Product Positioning

Working product name: **LineValue Football**

One-line positioning:

> Transparent football value analysis for bettors who care about price, probability, bankroll, and closing-line proof.

Tone:

- Serious, calm, evidence-led.
- No "guaranteed wins," "beat the bookies," "VIP tips," or "daily acca" language.
- Use "estimated probability," "model edge," "closing-line value," "bankroll limits," and "decision support."
- Treat responsible gambling as part of the product, not footer compliance.

Competitor-informed stance:

- EYGEN and OddsIntel show there is demand for football value discovery and CLV.
- Predify shows the crowded consumer "AI acca" lane to avoid.
- OddsLab, RebelBetting, and OddsJam show the serious analytics/pro-tool lane.
- TIPSTOP and app-store products show the need for simple match cards and bankroll support.
- The website should bridge simple football usability with pro-grade trust signals.

## Information Architecture

Public site:

- Home
- Methodology
- Public record
- Pricing
- Responsible gambling
- Sign in / Join beta

Authenticated app:

- Dashboard / Value board
- Match detail
- Bet tracker
- Performance
- Bankroll settings
- Account settings

## Page 1: Home

### Purpose

Convert serious football bettors into beta signups by showing the product as a transparent analytics dashboard, not a tipster feed.

### Layout

Header:

- Left: LineValue Football
- Nav: Methodology, Public record, Pricing, Responsible gambling
- Right: Sign in, Join beta

Hero section:

- Left copy column
- Right embedded dashboard preview

Hero copy:

- Eyebrow: "Football betting analytics, not betting hype"
- H1: "Find where your football model disagrees with the market."
- Body: "Compare estimated probabilities with available bookmaker prices, log the odds you actually take, and track whether your bets beat the closing line."
- Primary CTA: "Join the beta"
- Secondary CTA: "View public record"
- Trust note: "18+. Decision-support only. No automated betting. No guarantees."

Dashboard preview cards:

- Today's value board
- Bankroll exposure
- CLV trend
- Public model record snippet

Section: What the dashboard shows

- Model probability vs implied probability
- Best available price and timestamp
- Estimated edge and confidence range
- Suggested stake range within user bankroll limits
- Closing-line result after settlement

Section: Why not acca-first?

Copy:

"Accumulators multiply variance. LineValue starts with singles because they are easier to evaluate, track, and learn from. Acca simulation is available as a risk tool, not a default recommendation."

Section: Built for proof

- Public pick log
- CLV tracking
- League and market breakdowns
- Losses visible alongside wins

Footer:

- Responsible gambling links
- Methodology
- Terms
- Privacy
- Contact

## Page 2: Dashboard / Value Board

### Purpose

Give users a daily working surface for finding actionable single bets and logging decisions.

### Layout

Top bar:

- Product name
- Date selector
- Bookmaker selector
- Bankroll status
- Account menu

Left filters:

- Country
- League
- Market
- Kickoff window
- Minimum edge
- Minimum confidence
- Odds range
- Bookmaker availability

Main board:

Opportunity row/card fields:

- Fixture and kickoff time
- Market and selection
- Model probability
- Best odds
- Market implied probability
- Edge
- Confidence band
- Suggested stake
- Bookmaker timestamp
- Buttons: "View detail" and "Log bet"

Right panel:

- Bankroll: current bankroll, daily exposure, stake cap
- CLV: last 30 logged bets
- Safety: "You are within your daily exposure limit"
- Responsible-gambling link

Empty state copy:

"No opportunities match these filters. Lower the edge threshold, broaden bookmakers, or check later when prices update."

Compliance note:

"Probabilities are estimates. Betting involves risk. Only bet what you can afford to lose."

## Page 3: Match Detail

### Purpose

Let the user understand why a match is flagged before they log anything.

### Layout

Header:

- Fixture
- Competition
- Kickoff time
- Market status

Primary panel:

- Selection
- Model probability
- Best odds
- Implied probability
- Estimated edge
- Suggested stake range

Odds panel:

- Bookmaker list
- Current odds
- Timestamp
- Movement since first observed
- Closing price placeholder if not settled

Model notes:

- Recent form
- Home/away adjustment
- Schedule congestion
- Data quality flag
- Market confidence

Log bet modal:

- Bookmaker
- Odds taken
- Stake
- Bet time
- Notes
- Confirmation checkbox: "I understand this is my decision and not a guarantee."

Secondary acca simulator entry:

- "Add to simulation"
- Warning: "Accumulator simulations increase variance and are not default recommendations."

## Page 4: Bet Tracker

### Purpose

Make value betting measurable and separate model quality from user execution.

### Layout

Summary row:

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

Filters:

- Date range
- League
- Market
- Bookmaker
- Result
- CLV positive/negative

Copy:

"The tracker is designed to show whether your process is improving. A winning bet can still be poor value, and a losing bet can still beat the closing line."

## Page 5: Public Record

### Purpose

Build trust before conversion and reduce black-box tipster scepticism.

### Layout

Top explanation:

"Every model opportunity is logged with timestamped odds and later compared against the closing line."

Metrics:

- Total logged opportunities
- Average CLV
- Yield
- ROI
- Drawdown
- Average odds
- Hit rate

Breakdowns:

- By league
- By market
- By odds band
- By month

Record table:

- Date
- Match
- Market
- Selection
- Recommended odds
- Closing odds
- CLV
- Result
- Profit/loss at flat stake

Required copy:

"Historical performance does not guarantee future outcomes. The public record includes losing periods and should be read as evidence of process, not certainty."

## Page 6: Methodology

### Purpose

Explain enough to earn trust without exposing implementation details that are not yet proven.

### Sections

- How model probability is estimated
- How implied probability is calculated from decimal odds
- How edge is calculated
- What CLV means and why it matters
- Why singles are the default
- What data is used
- Known limitations
- Update cadence
- Responsible use of the tool

Sample copy:

"LineValue does not claim to know the result of a match. It estimates whether the available price is higher than the model's fair price, then helps you track whether that judgment holds up against the closing market."

## Page 7: Pricing

### Purpose

Test willingness to pay without overselling outcomes.

### Tiers

Free / Watchlist:

- Limited fixture board
- Public record
- Education
- 20 manual tracked bets/month

Pro:

- GBP14.99-GBP24.99/month
- Full daily value board
- Bookmaker filters
- Unlimited bet tracking
- CLV tracking
- Bankroll rules
- Saved filters
- CSV export

Analyst:

- GBP49-GBP79/month
- Advanced filters
- Historical performance splits
- Strategy backtesting
- Alert thresholds
- Priority beta access

Pricing copy:

"Subscription pays for analytics, tracking, and data access. It does not buy guaranteed profit."

## Page 8: Responsible Gambling

### Purpose

Demonstrate compliance awareness and protect users.

### Required Elements

- 18+ notice
- "Only bet what you can afford to lose"
- Bankroll limits explanation
- Cooling-off explanation
- Self-exclusion and support resources by market
- No automated betting statement
- No guarantee statement
- Contact for support and account closure

Copy:

"The product is designed to slow betting decisions down, not speed them up. Bankroll limits, exposure warnings, and transparent loss history are core features."

## MVP Mockup Notes

The first standalone HTML mockup should show:

- Home/dashboard hybrid first screen.
- Value board rows.
- Bankroll and CLV side panel.
- Public record preview.
- Responsible-gambling strip.
- Pricing preview.

It should avoid:

- Casino-like colours.
- Flashing odds.
- Pushy urgency.
- Winner imagery.
- "Acca of the day" modules.
- Any copy that implies guaranteed returns.
