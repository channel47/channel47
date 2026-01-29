---
name: copy
description: |
  Polish ad copy with landing page message match. Extracts exact language from LPs,
  applies direct response frameworks, validates character limits, and outputs
  production-ready headlines and descriptions for PMax, Search, and Display.
---

# Ad Copy Polish

Create message-matched ad copy by extracting landing page language and applying direct response frameworks.

## Reference Files

This skill uses these reference documents:
- [Frameworks](./frameworks.md) - Direct response frameworks (AIDA, PAS, FAB, 4Ps, Offer-First)
- [Headline Formulas](./headline-formulas.md) - Fill-in-the-blank patterns, psychological triggers, DKI
- [Character Limits](./character-limits.md) - Platform specifications by campaign type
- [Quality Patterns](./quality-patterns.md) - Good vs bad copy patterns, headline categories

---

## Required Inputs

Before starting, you MUST collect:

1. **Landing Page URL** (required) - Source for message-matched copy
2. **Campaign Type** (required) - PMax, Search RSA, or Display
3. **Existing Copy** (optional) - Current headlines/descriptions to improve
4. **Brand Name** (optional) - Will extract from LP if not provided

If not provided, ask:

> "I need these inputs to polish your ad copy:
> 1. Landing page URL
> 2. Campaign type (PMax / Search RSA / Display)
> 3. Any existing copy to improve? (optional)
>
> Which can you provide?"

---

## Phase 1: Input Collection

### Validate Campaign Type

Confirm campaign type and load corresponding requirements:

| Campaign Type | Headlines | Long Headlines | Descriptions |
|--------------|-----------|----------------|--------------|
| PMax | 3-15 (30 char) | 1-5 (90 char) | 2-5 (90 char) |
| Search RSA | 3-15 (30 char) | N/A | 2-4 (90 char) |
| Display | 1-5 (30 char) | N/A | 1-5 (90 char) |

### Collect Existing Copy (if provided)

If user has existing copy:
- List all current headlines with character counts
- List all current descriptions with character counts
- Flag any that exceed limits

---

## Phase 2: Landing Page Extraction

Use WebFetch on the landing page URL to extract all usable copy elements.

### Extraction Prompt

```
Extract all advertising-usable text from this landing page. Return in this format:

HEADLINES (exact phrases, 1-5 words):
- [list all short punchy phrases, titles, button text]

VALUE PROPOSITIONS (complete claims):
- [list all benefit statements and USPs]

SOCIAL PROOF (specific numbers/claims):
- [testimonial quotes, review counts, customer numbers, ratings, certifications]

PRODUCT DETAILS:
- Brand name:
- Product name:
- Key features:
- Price/offer:

OBJECTION HANDLERS (guarantee/risk reversal language):
- [return policies, guarantees, warranties]

URGENCY/SCARCITY:
- [limited time, limited quantity, deadlines]

CALL TO ACTION PHRASES:
- [all CTA button and link text]
```

### Summarize Extraction

Present to user:
- Brand name identified
- Number of usable headline phrases found
- Key value propositions
- Social proof elements available
- Any urgency/scarcity language

---

## Phase 3: Message Inventory

Categorize extracted language by ad copy usage:

### Headline Candidates (30 char or less)

Sort by category:

| Category | Examples from LP |
|----------|------------------|
| Problem Acknowledgement | [extracted phrases about the problem] |
| Outcome/Benefit | [extracted benefit phrases] |
| Objection Handling | [guarantee, risk reversal phrases] |
| Price/Value | [price points, discounts, value statements] |
| Trust/Proof | [testimonials, ratings, certifications] |

### Description Candidates (90 char or less)

Sort by purpose:
- **Lead with benefit** - strongest value proposition statements
- **Include proof** - social proof + benefit combinations
- **Handle objections** - risk reversal + benefit
- **Drive action** - urgency + CTA

### Identify Gaps

Flag missing elements:
- [ ] No social proof numbers found
- [ ] No price/offer extracted
- [ ] No guarantee language
- [ ] No urgency elements

If critical gaps, ask user:
> "I couldn't find [element] on your landing page. Can you provide:
> - [specific question]"

---

## Phase 4: Framework Selection

Reference: [Frameworks](./frameworks.md)

### Determine Audience Awareness Level

Ask user if unclear:

> "Which best describes your target audience?
> 1. **Unaware** - Don't know they have the problem
> 2. **Problem-aware** - Know the problem, not your solution
> 3. **Solution-aware** - Know solutions exist, comparing options
> 4. **Product-aware** - Know your product, considering purchase
> 5. **Most-aware** - Past customers or remarketing"

### Framework Assignment

| Awareness Level | Primary Framework | Headline Approach |
|----------------|-------------------|-------------------|
| Unaware | AIDA | Attention-grabbing, curiosity |
| Problem-aware | PAS | Problem acknowledgement, agitation |
| Solution-aware | FAB | Features → advantages → benefits |
| Product-aware | 4Ps | Promise, picture, proof, push |
| Most-aware | Offer-First | Lead with discount/offer |

### Select Framework

Confirm with user:
> "Based on [awareness level], I'll use the [framework] framework. This means:
> - Headlines focus on: [framework focus]
> - Descriptions follow: [structure pattern]
>
> Should I proceed or use a different approach?"

---

## Phase 5: Copy Generation

Generate headlines and descriptions using LP language + selected framework + headline formulas.

Reference: [Headline Formulas](./headline-formulas.md)

### Headlines

Generate based on campaign type requirements.

**Formula Selection:**

For each headline angle, select formulas that:
1. Fit the LP language extracted
2. Match the selected framework
3. Apply relevant psychological triggers

| Angle | Recommended Formulas | Psych Triggers |
|-------|---------------------|----------------|
| Problem | Question ("Still [X]?"), Negative ("Stop [X]") | Loss aversion |
| Benefit | Transformation ("From [A] to [B]"), How-To | Commitment |
| Proof | Authority ("[#]+ Customers"), Numbers | Social proof |
| Value | Number ("[%] Off"), Negative ("No [Fees]") | Reciprocity |
| Objection | Negative ("No [Risk]"), Authority | Trust |

**PMax/Search (generate 10-15):**

```markdown
## Headlines (30 char max)

### Problem/Pain (2-3) - Use Question or Negative formulas
1. [formula + LP problem language] [XX chars]
2. [formula + LP problem language] [XX chars]

### Benefit/Outcome (3-4) - Use Transformation or Number formulas
1. [formula + LP benefit language] [XX chars]
2. [formula + LP benefit language] [XX chars]
3. [formula + LP benefit language] [XX chars]

### Social Proof (2-3) - Use Authority or Number formulas
1. [formula + LP proof numbers] [XX chars]
2. [formula + LP testimonial snippet] [XX chars]

### Offer/Value (2-3) - Use Number or Urgency formulas
1. [formula + LP price/discount] [XX chars]
2. [formula + LP value proposition] [XX chars]

### Objection/Trust (1-2) - Use Negative or Authority formulas
1. [formula + LP guarantee language] [XX chars]
2. [formula + LP trust element] [XX chars]
```

**Character Count Validation:**
After each headline, show: `[XX chars]`
Flag any exceeding 30 chars with: `[XX chars - OVER LIMIT]`

### Dynamic Keyword Insertion (Search RSA only)

If creating Search RSA copy, consider DKI for 2-3 headlines:

```markdown
### DKI Headlines (Search RSA only)

Before using DKI, verify:
- [ ] Ad group has similar, grammatically compatible keywords
- [ ] No keywords with typos in the ad group
- [ ] Keywords are not emotional/problem-focused

If DKI appropriate:
1. Shop {KeyWord:[LP Category]} [XX chars w/ default]
2. Best {KeyWord:[LP Product]} [XX chars w/ default]
3. {KeyWord:[LP Default]} - [LP Offer] [XX chars w/ default]
```

If DKI not appropriate, note why and skip.

### Long Headlines (PMax only)

Generate 3-5 long headlines (90 char max):

```markdown
## Long Headlines (90 char max)

1. [expanded benefit + proof from LP] [XX chars]
2. [outcome + trust statement from LP] [XX chars]
3. [value prop + CTA from LP] [XX chars]
```

### Descriptions

Generate based on campaign type:

```markdown
## Descriptions (90 char max)

1. [Lead benefit from LP] + [CTA] [XX chars]
2. [Social proof from LP] + [benefit] [XX chars]
3. [Objection handler from LP] + [trust] [XX chars]
4. [Urgency from LP] + [action phrase] [XX chars]
```

### Framework Compliance

Verify each copy element follows selected framework structure:

| Framework | Headline Pattern | Description Pattern |
|-----------|-----------------|---------------------|
| AIDA | Attention → Interest | Desire + Action |
| PAS | Problem → Agitation | Solution + CTA |
| FAB | Feature/Advantage | Benefit + CTA |
| 4Ps | Promise | Picture + Proof + Push |
| Offer-First | Offer | Value + Action |

---

## Phase 6: Character Validation

Reference: [Character Limits](./character-limits.md)

### Validate All Copy

Run validation on generated copy:

```markdown
## Validation Report

### Headlines
| # | Headline | Chars | Status |
|---|----------|-------|--------|
| 1 | [headline] | 28 | PASS |
| 2 | [headline] | 32 | FAIL - trim 2 chars |

### Long Headlines (if PMax)
| # | Long Headline | Chars | Status |
|---|---------------|-------|--------|
| 1 | [long headline] | 87 | PASS |

### Descriptions
| # | Description | Chars | Status |
|---|-------------|-------|--------|
| 1 | [description] | 89 | PASS |
```

### Fix Violations

For each over-limit item:
1. Suggest shortened version
2. Preserve core message and LP language
3. Re-validate

### Additional Validation Rules

Check for:
- [ ] No trailing punctuation on headlines
- [ ] No excessive punctuation (!!! or ???)
- [ ] No ALL CAPS words (except acronyms)
- [ ] No phone numbers in text
- [ ] No trademark symbols in text (R, TM)

---

## Phase 7: Quality Review

Reference: [Quality Patterns](./quality-patterns.md)

### Quality Gate 1: Generic Claims Check

Scan all copy for generic phrases:

| Generic (Flag) | Specific (Pass) |
|---------------|-----------------|
| "Best quality" | Use LP-specific claim |
| "Fast results" | Use LP-specific timeframe |
| "Affordable" | Use LP-specific price |
| "Many customers" | Use LP-specific number |

**If generic claim found:** Replace with specific LP language or flag for user.

### Quality Gate 2: Message Match Percentage

Calculate LP language reuse:
- Count unique phrases from LP used in copy
- Target: >60% of copy uses exact or close LP language

```
LP Language Reuse: [X]%
Exact LP quotes used: [N]
```

If under 60%: Revise to use more LP language.

### Quality Gate 3: Benefit Ratio

Analyze all headlines and descriptions:
- Count benefit-focused statements
- Count feature-focused statements
- Target: 70%+ benefits

```
Benefit statements: [N] ([X]%)
Feature statements: [N] ([Y]%)
```

If under 70% benefits: Revise feature statements to lead with benefits.

### Quality Gate 4: Framework Compliance

Verify copy follows selected framework:
- [ ] Headlines follow framework pattern
- [ ] Descriptions follow framework structure
- [ ] CTA matches framework push

### Quality Gate 5: Headline Diversity

Check headline categories covered:
- [ ] Problem acknowledgement (at least 1)
- [ ] Outcome/benefit (at least 2)
- [ ] Objection handling (at least 1)
- [ ] Price/value (at least 1)
- [ ] Trust/proof (at least 1)

No duplicate angles: Each headline should cover unique angle.

### Quality Gate 6: Formula Variety

Reference: [Headline Formulas](./headline-formulas.md)

Check formula types used:

| Formula Type | Count | Minimum |
|--------------|-------|---------|
| Number headlines | [N] | 2 |
| Question headlines | [N] | 1 |
| Negative/Contrast | [N] | 1 |
| Transformation | [N] | 1 |
| Authority/Proof | [N] | 1 |

Check psychological triggers applied:
- [ ] Loss aversion (at least 1 headline)
- [ ] Social proof (at least 1 headline)
- [ ] Urgency/scarcity (at least 1 headline, if legitimate)

### Quality Gate 7: DKI Validation (Search RSA only)

If DKI headlines included:
- [ ] Default text makes grammatical sense alone
- [ ] Verified keywords are compatible (no typos, similar structure)
- [ ] Character limit math is correct
- [ ] Not used for brand terms or emotional keywords

---

## Phase 8: Output Delivery

### Output 1: Markdown Document

```markdown
# Ad Copy: [Brand/Product Name]

**Campaign Type:** [PMax/Search RSA/Display]
**Framework Used:** [Framework name]
**Landing Page:** [URL]
**Generated:** [Date]

---

## Headlines (30 char max)

| # | Headline | Chars | Category |
|---|----------|-------|----------|
| 1 | [headline] | 28 | Benefit |
| 2 | [headline] | 30 | Problem |
...

## Long Headlines (90 char max)
[If PMax]

| # | Long Headline | Chars |
|---|---------------|-------|
| 1 | [long headline] | 87 |
...

## Descriptions (90 char max)

| # | Description | Chars |
|---|-------------|-------|
| 1 | [description] | 89 |
...

---

## Quality Scores

- LP Message Match: [X]%
- Benefit Ratio: [X]%
- Framework Compliance: PASS/FAIL
- Character Limits: ALL PASS / [N] violations
- Headline Diversity: [N]/5 categories covered

---

## LP Language Used

Exact quotes incorporated:
1. "[quote from LP]" → used in headline [N]
2. "[quote from LP]" → used in description [N]
...
```

### Output 2: Copy-Paste Block

```markdown
## Quick Copy (ready to paste)

### Headlines
[headline 1]
[headline 2]
[headline 3]
...

### Long Headlines
[long headline 1]
...

### Descriptions
[description 1]
[description 2]
...
```

### Output 3: CSV Export (optional)

If user requests:

```csv
Type,Text,Characters,Category
Headline,[headline],28,Benefit
Headline,[headline],30,Problem
Long Headline,[long headline],87,
Description,[description],89,
```

---

## Quality Checklist

Before delivering, verify:

**Character & Compliance:**
- [ ] All character limits validated (no violations)
- [ ] No trailing punctuation on headlines
- [ ] No prohibited patterns (ALL CAPS, emojis, phone numbers)

**Message Match:**
- [ ] >60% LP language reused
- [ ] >3 exact LP quotes used
- [ ] Offer matches LP exactly
- [ ] Social proof numbers match LP

**Copy Quality:**
- [ ] 70%+ benefit-focused copy
- [ ] Framework structure followed
- [ ] No generic claims without specifics

**Headline Diversity:**
- [ ] No duplicate headline angles
- [ ] All 5 required angles covered (problem, benefit, proof, value, objection)
- [ ] At least 2 number headlines
- [ ] At least 1 question headline
- [ ] At least 1 psychological trigger applied (loss aversion, social proof, scarcity)

**DKI (Search RSA only):**
- [ ] Default text grammatically standalone
- [ ] Keywords verified compatible
- [ ] Character math correct

---

## What You Don't Do

- Generate copy without first extracting LP content
- Use generic claims not backed by LP specifics
- Exceed character limits
- Promise specific ad performance results
- Include trademarked competitor names without user confirmation
- Skip the quality review gates
- Output copy that contradicts LP messaging
- Use phone numbers in ad text
- Generate misleading claims
- Ignore the selected framework structure
