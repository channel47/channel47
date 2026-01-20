# Copywriting Expert

A focused copywriting skill built on three proven frameworks from history's greatest direct response masters.

## The Three Frameworks

### Eugene Schwartz — Awareness Levels
The foundation of all effective copy. Schwartz identified five levels of prospect awareness, each requiring a different approach:

1. **Most Aware** — Knows your product, just needs the deal
2. **Product Aware** — Knows what you sell, not convinced it works
3. **Solution Aware** — Knows solutions exist, not yours specifically
4. **Problem Aware** — Feels the pain, doesn't know solutions exist
5. **Unaware** — Doesn't recognize the problem yet

Match your copy's sophistication to your prospect's awareness level.

### Ernest Hemingway — Economy of Language
Every word earns its place. The iceberg theory: show 10%, imply 90%. Strip away:
- Unnecessary adjectives
- Weasel words
- Passive constructions
- Anything that doesn't advance the sale

What remains is copy that hits like a punch.

### Gary Halbert — Conversational Urgency
Write like you're talking to one person across a kitchen table. The A-pile principle: make your copy feel personal enough to open first. Build urgency through:
- Specificity over generality
- Stories over claims
- Deadlines that matter
- Reasons why

## Commands

| Command | Purpose |
|---------|---------|
| `/headline` | Generate compelling headlines for any product or angle |
| `/email` | Write conversion-focused email copy |
| `/landing-page` | Create complete landing page copy |
| `/swipe` | Analyze and deconstruct existing copy |
| `/weakness` | Diagnose copy problems and suggest fixes |

## Quick Start

### Generate Headlines
```
/headline [product] [angle]
```
Creates multiple headline variations applying Schwartz's awareness targeting and Halbert's specificity principles.

### Write Email Copy
```
/email [product] [context]
```
Produces email copy using Halbert's conversational style with Hemingway's economy.

### Build Landing Pages
```
/landing-page [product] [audience]
```
Generates full landing page copy structured around awareness levels.

### Analyze Existing Copy
```
/swipe [paste copy here]
```
Deconstructs copy to identify techniques, strengths, and what makes it work.

### Find Weaknesses
```
/weakness [paste copy here]
```
Diagnoses problems in copy and provides actionable fixes.

## Utility Scripts

### analyze_swipe.py
Automated swipe file analysis for pattern recognition.

```bash
python scripts/analyze_swipe.py path/to/swipe.txt
```

Outputs structural analysis, technique identification, and framework alignment.

### awareness_check.py
Validates copy against Schwartz's awareness levels.

```bash
python scripts/awareness_check.py path/to/copy.txt --level 3
```

Checks whether your copy appropriately targets the specified awareness level.

## When It Activates

The skill engages automatically when Claude detects:
- Sales copy requests
- Email marketing tasks
- Landing page creation
- Headline generation
- Copy analysis or review

## Best Practices

1. **Identify awareness level first** — Everything flows from this
2. **Cut ruthlessly** — If a word doesn't sell, delete it
3. **Write to one person** — Specificity beats generality
4. **Analyze before creating** — Use `/swipe` to study what works
5. **Diagnose before rewriting** — Use `/weakness` to find real problems

## File Structure

```
copy/
├── skills/copywriting/
│   ├── SKILL.md
│   └── frameworks/
│       ├── schwartz.md
│       ├── hemingway.md
│       └── halbert.md
├── commands/
│   ├── headline.md
│   ├── email.md
│   ├── landing-page.md
│   ├── swipe.md
│   └── weakness.md
└── scripts/
    ├── analyze_swipe.py
    └── awareness_check.py
```

---

**v2.0.0** — Streamlined to three essential frameworks and five core commands.
