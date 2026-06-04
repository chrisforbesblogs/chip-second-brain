# App Marketing Agent Research And System Design

Date: 2026-05-25  
Project: `app-marketing-agent`  
Storage: `second-brain/Research/app-marketing-agent/`

## Executive Summary

Build the App Marketing Agent as an internal AI-assisted marketing system for launching and growing the mobile/web apps. The system should help with strategy, audience research, creative ideation, short-form scripts, image/video briefs, ASO/SEO, campaign calendars, competitor monitoring, analytics summaries, and outreach drafts.

The key design constraint: **agents may draft, schedule internally, analyse, and prepare assets, but they must not post publicly, spend ad budget, message influencers, or change store listings without explicit human approval.**

Recommended MVP:

1. A file-backed campaign workspace inside `second-brain/Research/`.
2. Agent roles for strategy, creative production, ASO/SEO, outreach, analytics, and compliance review.
3. A simple CLI/workflow for generating campaign briefs, post drafts, asset briefs, and approval packets.
4. Manual publishing first, with API integrations added only after the approval workflow is reliable.
5. Initial platform focus on TikTok, Instagram Reels, YouTube Shorts, Reddit, Product Hunt/Microlaunch, X, and app store pages.

## Recommended Agent Roles And Personas

### 1. Campaign Strategist

Default owner: ChipThink.

Responsibilities:

- Define launch positioning, audience, hooks, and campaign goals.
- Turn product reports into campaign briefs.
- Choose platforms and content angles.
- Maintain campaign calendar.
- Decide what to test next.

Primary outputs:

- Campaign brief.
- Audience personas.
- Messaging matrix.
- Weekly content plan.
- Test plan.

### 2. Creative Director

Responsibilities:

- Generate content angles, hooks, short-form video concepts, thumbnail ideas, and image prompts.
- Convert app features into social-native stories.
- Maintain brand voice and reusable creative patterns per app.

Primary outputs:

- Hook bank.
- Script bank.
- Image/video generation prompts.
- Shot lists.
- Creative QA notes.

### 3. Short-Form Video Producer

Responsibilities:

- Draft TikTok/Reels/Shorts scripts.
- Produce storyboard timings, captions, VO, B-roll, and edit notes.
- Repurpose one concept across vertical video formats.

Primary outputs:

- 15s, 30s, and 45s scripts.
- Caption packs.
- Voiceover scripts.
- Edit checklists.

### 4. ASO And SEO Specialist

Responsibilities:

- App Store and Google Play listing optimization.
- Keyword research.
- Screenshot messaging.
- Product page test hypotheses.
- Landing page SEO briefs.

Primary outputs:

- ASO keyword map.
- Store listing copy variants.
- Screenshot text variants.
- Product page optimization hypotheses.
- SEO landing page briefs.

### 5. Influencer And UGC Scout

Responsibilities:

- Identify creator categories and micro-influencer profiles.
- Draft outreach messages.
- Track UGC opportunities and creator fit.
- Prepare sponsorship/contra-deal briefs.

Primary outputs:

- Creator target list.
- Outreach drafts.
- Creator briefing docs.
- UGC usage-rights checklist.

### 6. Competitor And Trend Monitor

Responsibilities:

- Track competitor positioning, social content, store pages, pricing, launch channels, and review themes.
- Summarise trend patterns by niche.
- Feed learnings into campaign briefs.

Primary outputs:

- Weekly competitor digest.
- Trend board.
- Ad/creative swipe notes.
- Opportunity gaps.

### 7. Analytics Agent

Responsibilities:

- Consolidate platform metrics, store analytics, web analytics, and campaign outcomes.
- Summarise what worked and what to do next.
- Detect failing tests and promote winning variants.

Primary outputs:

- Weekly performance summary.
- Campaign scorecard.
- Test readout.
- Recommendations for next experiments.

### 8. Compliance And Approval Gatekeeper

Default owner: main agent plus Vance approval.

Responsibilities:

- Ensure no public post, ad spend, influencer message, or store listing change happens without approval.
- Check claims, platform policy, disclosure requirements, copyright, privacy, and brand safety.
- Require provenance for generated assets.

Primary outputs:

- Approval packet.
- Risk checklist.
- Final publish/reject decision.

## Platform Priorities For App Launches

### Tier 1: Primary Launch Channels

**TikTok**

- Best for consumer apps, games, novelty utilities, and quick visual demos.
- Use for rapid hook testing, UGC-style demos, creator outreach, and trend-based iterations.
- Prefer manual posting at MVP. TikTok has official Content Posting API support, but direct posting requires integration and account/platform review.

**Instagram Reels**

- Strong for polished visual demos, lifestyle framing, creator collaborations, and reusable vertical videos.
- Useful for app brands with character, design, or creator-friendly workflows.
- Meta publishing APIs are viable later, but Business/Creator account setup, permissions, and review add friction.

**YouTube Shorts**

- Stronger long-term content shelf life than purely feed-led platforms.
- Good for searchable demos, "how it works", comparison, and game clips.
- YouTube Data API supports uploads, but unverified API projects created after 28 July 2020 upload videos as private until audited.

**App Store And Google Play Listings**

- Treat as conversion surfaces, not admin afterthoughts.
- Every social campaign should map to a store-page claim, screenshot, or custom product page/listing test.
- Apple Product Page Optimization and Google Play Store Listing Experiments support testing store assets and copy.

### Tier 2: Useful Supporting Channels

**Reddit**

- Best for honest feedback, niche communities, founder updates, and validation.
- High spam risk. Use manual posting and community-specific contribution, not automation.
- Track target subreddits and draft posts, but require human approval before posting.

**X**

- Useful for build-in-public, indie app launches, dev tools, AI/web products, and founder networking.
- API posting exists, but paid API access and account reputation matter.
- Good for short update threads and launch-day amplification.

**Product Hunt / Microlaunch / Indie Hackers**

- Useful for launch spikes, feedback, and early adopter discovery.
- Manual launch preparation is more important than automation.

**LinkedIn**

- Strong for B2B, productivity, compliance, analytics, and professional tools.
- Lower priority for cute games unless discussing the build process.
- LinkedIn's Posts API can support publishing for approved use cases, but manual posting is enough for MVP.

### Tier 3: Paid Acquisition Later

**Meta Ads, TikTok Ads, Google App Campaigns, Reddit Ads, Apple Ads**

- Do not automate spend in the MVP.
- First build analytics and creative-learning loops.
- Add paid APIs after tracking, approval, budgets, and kill criteria are explicit.

## AI Techniques To Use

### Ideation

Use structured ideation rather than generic brainstorming.

Recommended techniques:

- Product-to-hook transformation: convert feature, pain, outcome, objection, and novelty into hooks.
- Persona x platform matrix: generate angles separately for TikTok, Reels, Shorts, Reddit, and store pages.
- Competitor gap prompting: compare competitor claims and find underused emotional or functional angles.
- Constraint prompts: "10 concepts using only real app footage", "10 no-face UGC demos", "10 founder-led posts".
- Prompt caching for repeated brand/project context to reduce cost and latency when generating many variants.

Output format:

- Hook
- Target platform
- Audience
- Creative format
- Proof needed
- Risk level
- Follow-up asset requirement

### Content Calendars

Generate rolling 2-week calendars, not giant quarterly plans.

Recommended structure:

- 3-5 posts per week per active app at early stage.
- 70% product demo/problem-solution content.
- 20% founder/build-in-public or learning content.
- 10% explicit launch/offer posts.
- Weekly review of performance before generating the next plan.

AI should produce:

- Calendar slots.
- Platform-specific captions.
- Creative briefs.
- Required assets.
- Approval deadlines.
- Test hypothesis for each post.

### Short-Form Video Scripts

Use modular script templates:

- Hook in first 1-2 seconds.
- Visual proof immediately after hook.
- Single feature or outcome.
- Caption-native, sound-off readable.
- Clear next action.

Suggested script fields:

- `hook_text`
- `first_frame`
- `shots`
- `voiceover`
- `on_screen_text`
- `caption`
- `hashtags`
- `cta`
- `variant_reason`

Recommended formats:

- "I tried to solve X with an app..."
- "POV: you need X but don't want Y"
- "Before vs after"
- "Tiny game mechanic demo"
- "3 things this app does"
- "Can you beat this score?"
- "We built this because..."

### Image And Video Generation

Use AI media generation for concept art, thumbnails, moodboards, UGC-style backdrops, store screenshot backgrounds, and rapid visual variants. Use real app footage/screenshots for anything claiming product behaviour.

Recommended workflow:

1. Generate a creative brief first.
2. Generate image/video prompts from the brief.
3. Produce assets into an `assets/generated/` folder.
4. Mark generated assets with provenance metadata.
5. Human review before use in public campaigns.

Current technical options:

- OpenAI `gpt-image-1` for image generation/editing and image understanding.
- OpenAI Sora 2 / Sora 2 Pro for video generation when available in the configured API account.
- Existing OpenClaw image/video generation tools for local asset drafts.
- Canva/Figma later for templated brand-safe layouts.

Guardrail:

- Generated visuals must not imply real UI, gameplay, user reviews, endorsements, or screenshots unless based on actual product assets.

### A/B Testing

Start with disciplined small tests:

- One variable per test where possible.
- Test hooks before testing whole campaigns.
- Compare creative angle, first frame, CTA, or screenshot headline.
- Avoid declaring winners from tiny samples.

Testing surfaces:

- Google Play Store Listing Experiments for Android listing text/graphics.
- Apple Product Page Optimization for App Store icons, screenshots, and app previews.
- Organic social post variants.
- Landing page headline/CTA tests.
- Paid ads only after conversion tracking is working.

Metrics:

- Impressions.
- 3-second hold / view rate.
- Average watch time.
- Completion rate.
- Click-through rate.
- Store page conversion rate.
- Install/start trial/sign-up.
- Retention or meaningful activation.

### Audience Research

Use a mix of desk research, social listening, reviews, and community observation.

Inputs:

- App store reviews for competitors.
- Reddit discussions.
- YouTube/TikTok comments on similar apps.
- Product Hunt comments.
- Search keyword suggestions.
- Creator content patterns.
- Existing project research retrieved through memory search and linked notes.

AI tasks:

- Cluster pains/desires.
- Extract language users naturally use.
- Identify objections.
- Build persona cards.
- Turn audience language into post hooks and store copy.

### SEO And ASO

ASO must be treated as a conversion and discovery system.

Apple focus:

- App name, subtitle, keyword field, screenshots, app previews, ratings/reviews, custom product pages, and Product Page Optimization.
- Use custom product pages for campaign-specific audiences or ad groups where appropriate.

Google Play focus:

- Title, short description, full description, screenshots, feature graphic, promo video, custom store listings, and Store Listing Experiments.
- Google Play custom store listings can target different countries, search keywords, pre-registration users, inactive users, unique URLs, or ad campaign traffic.

SEO focus:

- Build one simple landing page per serious app.
- Produce comparison pages only when accurate and fair.
- Publish changelogs, launch notes, and use-case pages.
- Use schema and app store links.

AI tasks:

- Keyword clustering.
- Store copy variants.
- Screenshot messaging.
- FAQ generation.
- Review mining.
- Landing page briefs.

### App Store Listing Optimization

Recommended process:

1. Extract current product positioning.
2. Mine competitor listings and reviews.
3. Generate 3 positioning hypotheses.
4. Draft listing copy and screenshot text variants.
5. Validate against store rules and actual app capabilities.
6. Run Apple/Google experiments when eligible.
7. Tie experiment results back to campaign records.

For new apps without traffic:

- Prioritise clarity over testing sophistication.
- Use screenshots that show the real app.
- Make the first screenshot communicate the core outcome.

### Influencer And UGC Outreach

Prioritise micro-creators and niche communities.

Workflow:

1. Define creator categories per app.
2. Build creator list manually or with approved discovery tools.
3. Score creators by audience fit, content quality, platform, engagement quality, and risk.
4. Draft outreach with a specific reason for fit.
5. Human approves before any message is sent.
6. Track rights, disclosure, payment/free access, and deliverables.

Required guardrails:

- Always disclose sponsorship/paid/free-product relationship as required.
- Do not imply creators endorse an app before they agree.
- Do not scrape personal contact details in ways that violate platform terms.
- Store outreach status and approval trail.

### Competitor Monitoring

Track enough to learn, not to copy.

Monitor:

- Store listing changes.
- Screenshot messaging.
- Pricing and subscription changes.
- Social post formats.
- Ad creative where visible.
- Review themes.
- Launch channels.
- Update cadence.

AI outputs:

- "What changed?"
- "What angle are they pushing?"
- "What complaints keep recurring?"
- "What can we credibly say that they cannot?"

### Analytics

The Analytics Agent should summarise performance weekly and after each campaign.

Data sources:

- App Store Connect Analytics.
- Google Play Console acquisition and store listing experiments.
- Website analytics.
- Social platform analytics exports.
- YouTube Data API / YouTube Analytics where configured.
- TikTok/Meta/Google Ads APIs only after accounts and approvals exist.
- Manual CSV imports for MVP.

Key principle:

- Optimise for installs and activated users, not vanity impressions.

## Required Tooling, Integrations, And APIs

### Core Internal Tooling

- Markdown/YAML/JSON campaign files in `second-brain/Research/`.
- Local asset folders for generated and approved media.
- A `marketing` CLI or scripts for creating briefs, calendars, approval packets, and analytics summaries.
- Git for audit trail.
- Project Tracker integration once available.

### AI And Generation

- OpenAI Responses API for structured ideation, campaign planning, classification, and summaries.
- Structured outputs for campaign/task/post JSON.
- OpenAI image generation for visual drafts.
- OpenAI video generation or OpenClaw video tools for concept videos.
- Prompt caching for repeated brand/context prompts.
- Embeddings/vector search later for brand memory, campaign history, and competitor notes.

### Publishing And Platform APIs

Use these only after manual workflow is proven:

- TikTok Content Posting API for creator-approved posting workflows.
- Instagram Graph API / Instagram Platform content publishing for Business/Creator accounts.
- YouTube Data API `videos.insert` for upload workflows, subject to API audit constraints.
- X API for posts where paid access and account authorization make sense.
- LinkedIn Posts API for B2B campaigns.

### Store And Analytics APIs

- App Store Connect API and Analytics Reports API.
- Google Play Console manual exports initially; Google Play Developer APIs later if needed.
- Google Play Store Listing Experiments and custom store listings through Play Console.
- Google Ads API for conversion management and later paid reporting.
- TikTok API for Business for ads/reporting later.
- Meta Marketing API for ads/reporting later.
- Reddit Ads API later if paid Reddit becomes relevant.

### Practical MVP Integrations

Start with:

- Local files.
- Manual CSV import/export.
- Screenshot and asset folder conventions.
- Human approval status fields.
- Optional browser-assisted research.

Avoid in MVP:

- Auto-posting.
- Auto-DM outreach.
- Auto-budget changes.
- Multi-platform OAuth complexity.
- Full paid ads automation.

## Guardrails And Approval Workflow

### Hard Rules

- Agents must not post publicly without explicit approval.
- Agents must not send outreach messages without explicit approval.
- Agents must not spend ad budget or modify campaign budgets.
- Agents must not publish or submit app store listing changes.
- Agents must not claim features, performance, ratings, testimonials, discounts, partnerships, or launch dates unless supported by source material.
- Agents must not use copyrighted music, celebrity likeness, brand marks, or competitor assets without permission.
- Agents must label generated assets and preserve prompts/provenance.

### Approval States

Recommended states:

- `draft`
- `internal_review`
- `needs_changes`
- `approved_to_prepare`
- `approved_to_publish`
- `published`
- `rejected`
- `archived`

### Approval Packet

Every public-facing item should have:

- Campaign ID.
- Post/asset ID.
- Platform.
- Final copy.
- Final asset links.
- Claims checklist.
- Source links for factual claims.
- Generated asset provenance.
- Risk notes.
- Publishing instructions.
- Human approver.
- Approval timestamp.

### Publishing Modes

**MVP mode: manual publish**

- Agent prepares packet.
- Human reviews.
- Human posts manually or explicitly asks main agent to publish through a connected tool.

**Later mode: assisted publish**

- Agent prepares packet.
- Human changes status to `approved_to_publish`.
- Publishing connector posts exactly the approved content.
- System logs platform post URL and metrics.

## Data Model

Use YAML for human-editable records and NDJSON for append-only events.

### Campaign

```yaml
id: campaign-20260525-chip-postman-streaks
project_id: chip-postman
name: Chip Postman Streak Feature Tease
status: planning
owner_agent: ChipThink
goal: Validate interest in delivery-streak arcade mechanic
audience:
  - casual mobile gamers
  - retro arcade fans
primary_platforms:
  - TikTok
  - Instagram Reels
  - YouTube Shorts
funnel_stage: awareness
start_date: 2026-06-01
end_date: 2026-06-14
budget_gbp: 0
approval_required: true
links:
  project: second-brain/Research/chip-postman
metrics:
  target_installs:
  target_waitlist_signups:
  target_ctr:
created_at: 2026-05-25T19:50:00+01:00
updated_at: 2026-05-25T19:50:00+01:00
```

### Asset

```yaml
id: asset-20260525-001
campaign_id: campaign-20260525-chip-postman-streaks
project_id: chip-postman
type: video
status: draft
path: assets/generated/asset-20260525-001.mp4
source_type: ai_generated
generation_tool: OpenAI Sora / OpenClaw video tool
prompt_path: prompts/asset-20260525-001.md
uses_real_app_footage: false
approved_for_public_use: false
rights_notes: Internal concept only
created_by_agent: Creative Director
created_at: 2026-05-25T19:50:00+01:00
```

### Post

```yaml
id: post-20260525-001
campaign_id: campaign-20260525-chip-postman-streaks
project_id: chip-postman
platform: TikTok
status: internal_review
format: short_video
scheduled_for:
copy:
  caption: "Can you keep the delivery streak alive?"
  hashtags:
    - mobilegame
    - arcadegame
    - indiedev
asset_ids:
  - asset-20260525-001
test_hypothesis: Score-challenge hook will drive higher completion than feature-description hook.
approval:
  required: true
  state: pending
  approved_by:
  approved_at:
publication:
  posted_by:
  posted_at:
  platform_url:
metrics:
  impressions:
  views_3s:
  completion_rate:
  clicks:
  installs:
```

### Outreach Target

```yaml
id: creator-20260525-001
platform: TikTok
handle: example_creator
creator_type: mobile_game_creator
fit_score: 4
status: draft
contact_method: platform_dm
approval_required: true
last_contacted_at:
notes:
  - Strong match for retro mobile game demos.
```

### Analytics Event

```json
{"ts":"2026-05-25T19:50:00+01:00","campaign_id":"campaign-20260525-chip-postman-streaks","post_id":"post-20260525-001","platform":"TikTok","metric":"views_3s","value":1200,"source":"manual_csv"}
```

## Recommended Folder Structure

```text
second-brain/Research/app-marketing-agent/
  README.md
  research/
    app-marketing-agent-research-2026-05-25.md
  product/
    marketing-agent-mvp-prd.md
  implementation/
    architecture/
      mvp-architecture.md
    data-models/
      campaign-schema.yaml
      post-schema.yaml
    plans/
      first-build-plan.md
  decisions/
    2026-05-25-manual-approval-first.md
  data/
    campaigns/
      chip-postman/
      football-betting-app/
      compliance-tracker/
    assets/
      generated/
      approved/
      rejected/
    prompts/
      brand-context/
      creative-generation/
    analytics/
      imports/
      summaries/
    approvals/
      pending/
      approved/
      rejected/
    competitor-monitoring/
      chip-postman/
      compliance-tracker/
```

## MVP Architecture

### MVP Components

1. **Campaign data store**
   - YAML/JSON files for campaigns, posts, assets, approvals, and analytics imports.

2. **Marketing CLI**
   - Commands for creating campaign briefs, generating post drafts, producing approval packets, and summarising analytics.

3. **Agent prompt library**
   - Reusable role prompts for strategist, creative director, ASO specialist, outreach scout, and analytics agent.

4. **Approval queue**
   - File-backed queue of public-facing drafts awaiting review.

5. **Asset registry**
   - Tracks generated/real assets, rights, provenance, approval state, and usage.

6. **Manual publishing handoff**
   - Approved packet tells the human exactly what to post, where, and with which asset.

7. **Analytics import**
   - Manual CSV/JSON import first.
   - Weekly AI summary generated from imported metrics.

### Later Architecture

After MVP:

- Add SQLite if file queries become painful.
- Add local web dashboard for calendar, approval queue, campaign performance, and asset library.
- Add OAuth/API connectors one at a time.
- Add read-only competitor monitoring automations.
- Add controlled publish connector that only posts content with `approved_to_publish`.

## Recommended First Build Plan

### Phase 1: Research And Operating Model

Deliverables:

- This report.
- Decision record: manual approval first.
- MVP PRD.
- Initial campaign schema.

Acceptance criteria:

- Roles, guardrails, data model, and first workflow are documented.
- Public-posting restrictions are explicit.

### Phase 2: File-Backed Campaign System

Deliverables:

- `data/campaigns/`
- `data/assets/`
- `data/approvals/`
- `data/analytics/imports/`
- seed campaign for `chip-postman`
- schema examples for campaign, post, asset, approval, analytics event

Acceptance criteria:

- An agent can create a campaign folder without inventing structure.
- Every public-facing draft has an approval state.
- Generated assets have provenance.

### Phase 3: CLI MVP

Commands:

```bash
marketing campaign new --project chip-postman --name "Launch teaser"
marketing brief generate --campaign campaign-id
marketing posts generate --campaign campaign-id --platform TikTok --count 5
marketing approval packet --post post-id
marketing analytics import --campaign campaign-id --file exports/tiktok.csv
marketing analytics summarize --campaign campaign-id
```

Acceptance criteria:

- CLI creates valid campaign/post files.
- CLI refuses to publish or mark as published without approval metadata.
- CLI can produce a review-ready Markdown approval packet.

### Phase 4: First Real Campaign Pilot

Recommended pilot: Chip Postman.

Why:

- Visual game loop suits short-form video.
- Recent feature work creates clear content hooks.
- Low regulatory risk compared with betting/compliance apps.

Deliverables:

- 2-week content calendar.
- 15 short-form post drafts.
- 5 video scripts.
- 5 image/thumbnail prompts.
- App store listing improvement notes.
- Approval packet for first 3 posts.

Acceptance criteria:

- Vance can approve/reject first posts from a single Markdown packet.
- Results can be manually recorded and summarised.

### Phase 5: Dashboard And Integrations

Deliverables:

- HTML dashboard or small local web app.
- Approval queue view.
- Campaign calendar view.
- Analytics summary view.
- Optional read-only API integrations.

Acceptance criteria:

- Human can see planned, approved, published, and blocked marketing items.
- No connector can post without approved packet status.

## Practical Operating Workflow

### Main Agent

- Receives product/launch request from Vance.
- Creates or updates project tracker task.
- Asks ChipThink to generate campaign brief and content plan.
- Ensures approval workflow is followed.
- Handles final user-facing summary and coordination.

### ChipThink

- Owns campaign strategy, positioning, personas, platform choices, and content calendar.
- Produces Markdown reports and campaign files.
- Drafts approval packets.
- Reviews analytics summaries and recommends next tests.

### ChipCode

- Builds the marketing CLI, schemas, dashboards, and integrations.
- Implements file validation and approval gates.
- Adds platform APIs only after manual workflow is stable.
- Ensures no command can publish without explicit approval state.

### Creative/Media Agent

- Generates image/video concepts and assets.
- Stores prompts and provenance.
- Produces variants for review.
- Marks generated assets as draft until approved.

### Human Approval

Vance approves:

- Public posts.
- Outreach messages.
- Paid budget.
- Store listing changes.
- Use of generated assets in public contexts.
- Any claim involving revenue, user numbers, rankings, reviews, or third-party endorsements.

## Risks And Costs

### Risks

- **Platform policy drift:** social APIs and app store rules change often.
- **Approval bypass:** strongest system risk; must be prevented in CLI and workflow.
- **Generated asset misuse:** AI visuals can accidentally imply fake product capabilities.
- **Low-quality content volume:** more AI content can mean more noise, not more growth.
- **Attribution gaps:** social views may not map cleanly to installs without good tracking.
- **Brand inconsistency:** multiple agents can create inconsistent tone unless brand context is centralised.
- **Community backlash:** Reddit and niche communities punish promotional automation.
- **API complexity:** Meta, TikTok, YouTube, X, and LinkedIn all have auth/review/rate-limit friction.
- **Legal/disclosure:** influencer outreach needs clear sponsorship/free-product disclosure.

### Costs

- LLM generation and summarisation costs.
- Image/video generation costs.
- Storage for media assets.
- Optional social scheduling/analytics tools.
- Possible API paid tiers, especially X and advanced social listening tools.
- Human review time.
- Creator payments or product/free-access costs.
- Paid acquisition budget if/when ads are introduced.

## Recommended Initial Policies

- Manual publishing only until at least one campaign has completed.
- Keep all public copy in approval packets.
- Use real app footage/screenshots for product claims.
- AI-generated media is allowed for concepts, thumbnails, stylised brand visuals, and moodboards only unless explicitly approved.
- One campaign owner per campaign.
- Weekly analytics review before generating the next calendar.
- Public-facing claims must link to source material or be removed.
- Outreach drafts must be approved individually or via an approved template plus approved target list.

## Recommended Next Action

Build the file-backed MVP for Chip Postman marketing first:

1. Create campaign/post/asset/approval schemas.
2. Seed one Chip Postman campaign.
3. Generate a 2-week content calendar and 10 short-form scripts.
4. Create approval packets for the first 3 posts.
5. Manually publish only after Vance approval.
6. Import metrics after one week and let the Analytics Agent recommend the next tests.

This gives the team a real marketing workflow without prematurely taking on risky auto-posting or paid ads integrations.

## Sources Checked

- OpenAI Images and Vision API guide: https://platform.openai.com/docs/guides/images
- OpenAI Video Generation guide: https://platform.openai.com/docs/guides/video-generation/
- OpenAI Prompt Caching guide: https://platform.openai.com/docs/guides/prompt-caching
- OpenAI Text Generation guide: https://platform.openai.com/docs/guides/text-generation
- TikTok Content Posting API product page: https://developers.tiktok.com/products/content-posting-api
- TikTok API for Business overview: https://ads.tiktok.com/help/article/marketing-api
- YouTube Data API `videos.insert`: https://developers.google.com/youtube/v3/docs/videos/insert
- X API Manage Posts: https://docs.x.com/x-api/posts/manage-tweets/introduction
- LinkedIn Posts API: https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api
- Reddit Advertising API: https://ads-api.reddit.com/docs/v3/
- Apple Product Page Optimization: https://developer.apple.com/app-store/product-page-optimization/
- Apple Custom Product Pages: https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions/
- Apple Analytics Reports API: https://developer.apple.com/help/app-store-connect-analytics/overview/analytics-reports-api
- Google Play Store Listing Experiments: https://play.google.com/console/about/store-listing-experiments/
- Google Play Custom Store Listings: https://support.google.com/googleplay/android-developer/answer/9867158
- Google Ads API conversion management: https://developers.google.com/google-ads/api/docs/conversions/overview
- Sprout Social 2026 social media trends: https://sproutsocial.com/insights/social-media-trends/
