# design-drift

> Lock your design system. Enforce it automatically. Stop AI drift.

**design-drift** is a Claude Code plugin that prevents AI agents from drifting
away from your design system — in real time, on every write.

```
ihlamury/design-skills   →   87 brands, MUST/SHOULD/NEVER constraint layer
VoltAgent/awesome-design-md  →   59 brands, visual atmosphere + token layer
design-drift             →   121 brands total, enforcement on every UI write
```

## Install

```bash
claude --plugin-dir https://github.com/ihlamury/design-drift
# or
/plugin install design-drift@ihlamury
```

## Usage

```bash
/design-drift:lock linear      # lock a brand
/design-drift:check            # audit all UI files
/design-drift:diff src/Button.tsx  # token diff on one file
/design-drift:fetch cursor     # preview any brand's DESIGN.md
```

Once locked, the drift scanner fires automatically on every Write/Edit. No prompting needed.

## Brand coverage — 121 brands

### Full enrichment (25) — SKILL.md + DESIGN.md
airbnb · airtable · anthropic · apple · cal · discord · figma · framer · github · intercom · linear · miro · monzo · notion · openai · pinterest · posthog · raycast · resend · shopify · slack · spotify · stripe · supabase · vercel

### Constraint-only (62) — SKILL.md
amplitude · arc · ashby · awwwards · bear · beehiiv · brex · clerk · coda · codeium · convertkit · convex · copy-ai · craft · deel · descript · dribbble · front · ghost · gumroad · gusto · hugging-face · jasper · lattice · launchdarkly · lemonsqueezy · liveblocks · loom · loops · mailchimp · matter · mem · mercury · mixpanel · mobbin · n26 · neon · obsidian · paddle · pitch · plaid · planetscale · railway · ramp · readwise · replit · retool · rippling · robinhood · segment · shortcut · substack · superhuman · things · ticktick · tldraw · todoist · upstash · warp · webflow · weights-biases · wise

### Token-only (34) — DESIGN.md via awesome-design-md
binance · bmw · bugatti · clay · clickhouse · cohere · coinbase · composio · cursor · elevenlabs · expo · ferrari · ibm · lamborghini · lovable · meta · minimax · mintlify · mistral · mongodb · nike · renault · replicate · revolut · runway · sanity · sentry · spacex · tesla · the-verge · uber · voltagent · wired · zapier

## How it works

**1. Lock** — `/design-drift:lock stripe`
Fetches DESIGN.md from awesome-design-md → cached to `.design-cache/stripe.md`
Loads bundled SKILL.md constraint layer → `skills/brands/stripe/SKILL.md`
Writes `.design-lock` with brand + coverage tier

**2. Enforce** — automatic on every write
`PostToolUse` hook fires after every Write/Edit to a UI file
Scanner reads `.design-lock`, loads available sources (SKILL.md + cached DESIGN.md)
Tokens extracted dynamically — colors, fonts, spacing grid, border-radius
Violations surface inline with line numbers and exact fix hints

**3. Audit** — `/design-drift:check`
Scans all UI files, returns structured violation report, offers auto-fix

## Why dynamic extraction

The scanner has zero hardcoded brand data. It parses whatever SKILL.md and DESIGN.md
text is available and extracts tokens at runtime. Adding a new brand requires only
adding a SKILL.md — no scanner changes needed.

## Powered by

- [ihlamury/design-skills](https://github.com/ihlamury/design-skills) — 87 brands, constraint enforcement layer
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — 59 brands, DESIGN.md layer (MIT)

## License

MIT
