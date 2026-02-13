# Keyword Match Types

Understanding and strategically using exact, phrase, and broad match in Google Ads Search campaigns.

---

## Match Type Overview

| Match Type | Symbol | Behavior | Control | Reach |
|------------|--------|----------|---------|-------|
| Exact | [keyword] | Matches meaning of keyword | Highest | Lowest |
| Phrase | "keyword" | Contains meaning of keyword | Medium | Medium |
| Broad | keyword | Related to keyword meaning | Lowest | Highest |

---

## Exact Match

### How It Works

Matches searches that have the **same meaning or intent** as your keyword.

**Example keyword:** `[running shoes]`

**Will match:**
- running shoes
- shoes for running
- running shoe
- jogging shoes (same intent)

**Won't match:**
- best running shoes (modified intent)
- running shoes review (different intent)
- trail running shoes (too specific)

### When to Use Exact Match

- High-value keywords you want precise control over
- Brand terms
- Top-converting keywords
- Keywords where you want to set specific bids
- Limited budget (maximize relevance)

### Pros and Cons

**Pros:**
- Highest relevance
- Most control over spend
- Clear performance data per keyword
- Best for tight budgets

**Cons:**
- Lowest reach
- May miss valuable variations
- Requires more keyword research upfront
- Close variants still match (less exact than before)

---

## Phrase Match

### How It Works

Matches searches that **include the meaning of your keyword** with additional words before, after, or within.

**Example keyword:** `"running shoes"`

**Will match:**
- running shoes for flat feet
- best running shoes 2024
- buy running shoes online
- where to get running shoes

**Won't match:**
- shoes for running (may or may not match)
- running sneakers for hiking (different intent)
- shoe running brands (different meaning)

### When to Use Phrase Match

- Core keywords where you want balanced reach/control
- Keywords where modifiers are valuable
- Mid-funnel discovery
- When you want to capture question-based searches

### Pros and Cons

**Pros:**
- Good balance of reach and relevance
- Captures valuable long-tail variations
- More data for optimization
- Easier to manage than pure exact

**Cons:**
- Less control than exact
- Need negative keywords to filter unwanted matches
- Some irrelevant traffic possible
- Performance varies by variation

---

## Broad Match

### How It Works

Matches searches **related to your keyword** including synonyms, related topics, and variations Google's AI deems relevant.

**Example keyword:** `running shoes`

**Will match:**
- running shoes (exact)
- best marathon footwear
- athletic shoes for jogging
- cross training sneakers
- running gear
- Nike running shoes

**May match (surprisingly):**
- hiking boots (related activity)
- sports apparel (broad relation)
- fitness equipment (very broad)

### When to Use Broad Match

- Combined with Smart Bidding (essential)
- Discovery of new keywords
- High-budget campaigns
- When confident in conversion tracking
- Mature accounts with good historical data

### Pros and Cons

**Pros:**
- Maximum reach
- Discovers new converting terms
- Works well with machine learning bidding
- Less keyword research needed

**Cons:**
- Requires Smart Bidding to work well
- Can waste budget on irrelevant terms
- Needs aggressive negative keyword management
- Less control over exact search terms

---

## Close Variants

Google automatically matches close variants across all match types:

- Misspellings (runing shoes)
- Singular/plural (shoe vs shoes)
- Abbreviations (CA vs California)
- Stemming (run vs running)
- Reordering (shoes running)
- Implied words (running [shoes] near me)

**You cannot disable close variants.**

---

## Negative Match Types

Negatives block your ads from showing for specific terms.

### Negative Exact

**Symbol:** `[negative keyword]`
- Blocks only that exact term
- Most precise blocking

### Negative Phrase

**Symbol:** `"negative keyword"`
- Blocks searches containing that phrase
- Medium blocking scope

### Negative Broad

**Symbol:** `negative keyword`
- Blocks searches containing all words (any order)
- Broadest blocking
- Most commonly used

### Negative Keyword Best Practices

1. Start with known irrelevant terms
2. Review search terms report weekly
3. Add negatives at campaign level for broad exclusions
4. Add at ad group level for fine-tuning
5. Create shared negative lists for common exclusions

---

## Match Type Strategy

### Conservative Strategy

**Best for:** Limited budgets, new campaigns, high-value conversions

```
Match Type Mix:
- 70% Exact
- 30% Phrase
- 0% Broad
```

Start narrow, expand based on performance data.

### Balanced Strategy

**Best for:** Most advertisers, moderate budgets, established tracking

```
Match Type Mix:
- 30% Exact (high-value terms)
- 50% Phrase (core terms)
- 20% Broad (discovery, with Smart Bidding)
```

### Aggressive Strategy

**Best for:** Large budgets, strong conversion tracking, Smart Bidding enabled

```
Match Type Mix:
- 10% Exact (brand and top converters)
- 30% Phrase (core themes)
- 60% Broad (maximum discovery)
```

Requires mature account and active negative keyword management.

---

## Keyword Duplication Strategy

### Same Keyword, Multiple Match Types

Running exact and phrase versions of the same keyword:

```
[running shoes] - Exact
"running shoes" - Phrase
```

**Pros:**
- Bid more for exact matches
- See performance by match type
- Capture close and expanded matches

**Cons:**
- Keywords compete against each other
- More complex management
- Redundant with Google's serving logic

**Recommendation:** Generally not needed. Google prioritizes exact matches automatically. Use single match type per keyword unless testing specific bid strategies.

---

## Match Type Migration Path

### Starting a New Campaign

1. **Week 1-2:** Exact + Phrase only
   - Establish baseline
   - Identify converting terms

2. **Week 3-4:** Add selective Broad (with Smart Bidding)
   - Test top themes
   - Monitor search terms closely

3. **Month 2+:** Optimize mix
   - Shift budget toward what converts
   - Expand or restrict based on data

### Mature Account Optimization

1. Review search terms report
2. Identify high-converting terms not in exact match
3. Add as exact match with higher bids
4. Add poor-performing terms as negatives
5. Test broad match for saturated ad groups

---

## Common Mistakes

1. **Using broad match without Smart Bidding** - Will waste significant budget
2. **No negative keywords** - Pays for irrelevant clicks
3. **Ignoring search terms report** - Missing optimization opportunities
4. **Over-relying on exact match** - Missing valuable traffic
5. **Too many keyword variations** - Complicates management
6. **Not segmenting by match type** - Can't analyze performance
7. **Assuming match types are "exact"** - Close variants always apply

---

## Search Terms Report

### How to Use It

1. Go to Keywords > Search Terms
2. Filter by conversions, cost, impressions
3. Look for:
   - Converting terms not in your keywords (add them)
   - Irrelevant terms with spend (add as negatives)
   - New themes to explore

### Frequency

- Weekly for new campaigns
- Bi-weekly for established campaigns
- After budget increases
- After adding broad match keywords
