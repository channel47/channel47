# DTC Research Engine

A Claude Code plugin that fetches real customer voice data from public sources and transforms it into customer personas, selling angles, ad scripts, and ad copy for DTC products.

## What's Inside

### Skills (auto-activate on relevant conversations)

- **Customer Research** — Voice of customer data extraction from Reddit, Amazon, Trustpilot, and forums via WebSearch and WebFetch
- **Persona Builder** — Data-driven customer avatars built from real research data, not marketer assumptions
- **Angle Generator** — Research-backed advertising angles scored across 8 categories (pain, failed-solution, trigger, identity, social proof, discovery, comparison, specificity)
- **Copy Writer** — Platform-specific ad copy for Meta, Google, TikTok, email, and landing pages
- **Script Writer** — Production-ready video scripts (UGC, VSL, YouTube pre-roll, TikTok native)

### Commands

- `/research [product]` — Fetch customer voice data from multiple public platforms
- `/persona [product]` — Build data-driven personas from research
- `/angles [product]` — Generate scored advertising angles
- `/copy [product] [platform]` — Write platform-specific ad copy
- `/scripts [product] [format]` — Write direct response ad scripts
- `/full-pipeline [product]` — Run the complete research → personas → angles → scripts → copy pipeline

### Agent

- **Research Crawler** — Autonomously fetches data from Trustpilot, Reddit (via search), Amazon (via search), forums, and complaint sites

## Installation

```bash
claude plugin install dtc-research-engine@channel47
```

Or copy to your project's plugins directory.

## Usage Examples

**Research a product:**
```
/research ultrasonic dog training devices
```

**Run the full pipeline:**
```
/full-pipeline toilet cleaning tablets
```

**Generate angles from existing research:**
```
/angles dog-training-device
```

## The Pipeline

Each stage feeds the next:

1. **Research** — Fetch 30+ real customer quotes from public sources
2. **Personas** — Build 2-4 distinct buyer personas from the data
3. **Angles** — Generate 5-8 scored advertising angles across 8 categories
4. **Scripts** — Write UGC, VSL, and platform-native video scripts
5. **Copy** — Write headlines, primary text, descriptions for Meta, Google, TikTok, email

## Core Principles

1. **Real data, not assumptions** — Every persona, angle, and piece of copy traces back to actual customer quotes
2. **Source transparency** — Every quote is tagged [Direct], [Search], or [Article] with source URLs
3. **Resonance over cleverness** — Mirror the customer's internal monologue, don't try to be creative
4. **Platform-specific** — Copy respects character limits and conventions for each platform
5. **Structured pipeline** — Each stage builds on the last, creating compounding insight
