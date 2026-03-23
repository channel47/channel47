# Extraction Patterns — Structuring Customer Voice Data

## Quote Tagging

Every customer quote gets a source quality tag. Downstream skills weight direct quotes more heavily.

```
- [Direct] "[exact quote]" — Source: [URL]
- [Search] "[exact quote]" — Source: [platform via search snippet]
- [Article] "[exact quote]" — Source: [article URL that quoted the customer]
- [Browser] "[exact quote]" — Source: [URL accessed via browser automation]
```

Tags:
- **[Direct]** — fetched the page directly and read the quote
- **[Search]** — quote appeared in a search result snippet
- **[Article]** — a fetchable article quoted a customer from another platform
- **[Browser]** — accessed via browser automation (Playwright, etc.)

## Per-Source Structure

```markdown
## Source: [URL or platform]
### Platform: [Trustpilot/Reddit/Amazon/Forum/etc.] | Access: [Direct/Search/Browser/Article]

### Pain Points
- [Tag] "[exact quote]" — context: [brief note]

### Desired Outcomes
- [Tag] "[exact quote]" — context: [brief note]

### Objections / Hesitations
- [Tag] "[exact quote]" — context: [brief note]

### Emotional Language
- [Tag] "[exact phrase]" — sentiment: [frustration/hope/anger/relief/etc.]

### Trigger Events
- [Tag] "[description of what made them buy/search]"

### Competitor Mentions
- [Tag] [Brand]: [positive/negative] — "[brief quote]"

### Demographic Signals
- Age indicators, gender indicators, life situation clues
```

## Synthesis Structure

After collecting from multiple sources, the final synthesis should follow this format:

```markdown
# [Product] — Customer Research Synthesis

## Top Pain Points
1. [Pain point] — frequency: [X mentions across Y sources]
   - "[example quote]" — [source]
   - "[example quote]" — [source]

## Customer Language Patterns
Recurring phrases to mirror in creative:
- "[phrase]" (appeared X times)
- "[phrase]" (appeared X times)

## Objection Map
| Objection | Frequency | Example Quote |
|-----------|-----------|---------------|
| [objection] | [count] | "[quote]" |

## Desire Map
| Stated Desire | Deeper Desire |
|---------------|---------------|
| "I want X" | They really mean Y |

## Trigger Events
- [Event] — pushes from passive to active searching

## Demographic Clusters
- [Cluster]: [description with supporting signals]

## Competitor Landscape
| Competitor | Perception | Key Quotes |
|------------|-----------|------------|
| [brand] | [positive/negative/mixed] | "[quote]" |

## Source Coverage
- [X] sources accessed directly
- [X] sources via browser automation
- [X] sources via search snippets
- [X] sources inaccessible (noted)
```
