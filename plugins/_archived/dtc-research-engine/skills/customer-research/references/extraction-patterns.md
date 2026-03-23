# Data Extraction Patterns

## Per-Source Extraction Template

When extracting data from each source, use this structure:

```markdown
---
## Source: [Full URL]
### Platform: [Reddit / Amazon / Trustpilot / YouTube / Forum / Other]
### Date Accessed: [YYYY-MM-DD]
### Source Type: [Thread / Review Page / Forum Post / Video Page]

### Pain Points Mentioned
- "[exact customer quote]" — Context: [who said it, what they were responding to]
- "[exact customer quote]" — Context: [brief note]

### Desired Outcomes
- "[what they want in their words]" — Context: [situation]
- "[what they want]" — Context: [situation]

### Objections / Hesitations
- "[skepticism or concern expressed]" — Context: [what prompted it]
- "[objection]" — Context: [brief note]

### Emotional Language
- "[vivid phrase]" — Sentiment: [frustration / anger / hope / relief / desperation / joy]
- "[metaphor or exclamation]" — Sentiment: [category]

### Trigger Events
- "[what happened that made them search/buy]"
- "[life event or moment]"

### Competitor Mentions
- [Brand Name]: [positive / negative / neutral] — "[brief quote about them]"
- [Brand Name]: [sentiment] — "[quote]"

### Demographic Signals
- [Any age, gender, location, income, life stage indicators]

### Unique Insights
- [Anything surprising or novel that doesn't fit above categories]
---
```

## Synthesis Template

After collecting from all sources, synthesize:

```markdown
# Customer Research Synthesis: [Product/Category]
## Date: [YYYY-MM-DD]
## Sources Analyzed: [count]
## Total Data Points: [count]

---

## 1. Top Pain Points (by frequency)

| Rank | Pain Point | Frequency | Intensity | Example Quote |
|------|-----------|-----------|-----------|---------------|
| 1 | [pain] | [X mentions] | [High/Med/Low] | "[quote]" |
| 2 | [pain] | [X mentions] | [intensity] | "[quote]" |

## 2. Customer Language Patterns

### Recurring Phrases
- "[phrase]" — appeared across [N] sources
- "[phrase]" — appeared across [N] sources

### Emotional Vocabulary
- [Category: frustration]: "[word/phrase]", "[word/phrase]"
- [Category: hope]: "[word/phrase]", "[word/phrase]"
- [Category: skepticism]: "[word/phrase]", "[word/phrase]"

### Metaphors and Comparisons
- "[metaphor customers use]"
- "[comparison they make]"

## 3. Objection Map

| Objection | Frequency | Underlying Fear | Counter-Evidence |
|-----------|-----------|----------------|------------------|
| [objection] | [common/occasional/rare] | [what they're really afraid of] | [if found] |

## 4. Desire Map

| Stated Desire | Deeper Desire | Frequency |
|--------------|---------------|-----------|
| "[surface want]" | [underlying emotional need] | [common/occasional] |

## 5. Trigger Events

| Trigger | Frequency | Persona Fit |
|---------|-----------|------------|
| [life event/moment] | [common/occasional] | [who this triggers] |

## 6. Demographic Clusters

| Cluster | Age Signal | Gender Signal | Situation | Notable Behavior |
|---------|-----------|--------------|-----------|-----------------|
| [name] | [range] | [if clear] | [life context] | [buying/research behavior] |

## 7. Competitor Landscape

| Competitor | Sentiment | Strengths (per customers) | Weaknesses (per customers) |
|-----------|-----------|--------------------------|---------------------------|
| [brand] | [pos/neg/mixed] | [what customers like] | [what they complain about] |

## 8. Sources Used

| # | URL | Platform | Data Points | Notes |
|---|-----|----------|-------------|-------|
| 1 | [url] | [platform] | [count] | [any notes] |

## 9. Sources That Were Inaccessible

| URL | Reason |
|-----|--------|
| [url] | [blocked / timeout / empty] |
```

## Tips for High-Quality Extraction

### Quote Selection
- Prefer quotes that are vivid, specific, and emotional over bland statements
- Include enough context that the quote makes sense on its own
- Long quotes (2-3 sentences) are fine if they're valuable
- Don't trim quotes to the point where meaning is lost

### Pain Point Ranking
- Frequency = how many distinct sources mention it
- Intensity = how emotionally charged the language is
- Both matter, but intensity is more useful for ad creative

### Demographic Inference
- Be honest about confidence level — "likely 35-55" is fine, don't fake precision
- Look for clues: mentions of kids' ages, job descriptions, housing situations, product budgets
- Note when you're inferring vs. when someone directly states demographics

### Competitor Analysis
- Capture both positive and negative sentiment — knowing what competitors do RIGHT is useful
- Note when customers compare specific features vs. overall brand sentiment
- Price comparisons are especially valuable
