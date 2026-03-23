#!/usr/bin/env python3
"""
Generate a blank customer research template markdown file.

Usage:
    python research_template.py <product-name> [output-dir]

Example:
    python research_template.py "ultrasonic-dog-trainer" ./
    python research_template.py "toilet-cleaning-tablets" /path/to/workspace/
"""

import sys
import os
from datetime import datetime


def slugify(name: str) -> str:
    """Convert product name to URL-friendly slug."""
    return name.lower().strip().replace(" ", "-").replace("_", "-")


def generate_template(product_name: str) -> str:
    slug = slugify(product_name)
    date = datetime.now().strftime("%Y-%m-%d")

    return f"""# Customer Research: {product_name}
## Date: {date}
## Product Slug: {slug}

---

## Research Parameters

- **Product/Category**: {product_name}
- **Known Competitors**: [list competitors here]
- **Target Audience Hypothesis**: [initial hypothesis]
- **Specific Questions**: [what do we want to learn?]

---

## Source Data

<!-- Copy the template below for each source fetched -->

---
### Source: [URL]
#### Platform: [Reddit / Amazon / Trustpilot / YouTube / Forum / Other]
#### Date Accessed: {date}

#### Pain Points Mentioned
- "[exact quote]" — Context: [brief note]

#### Desired Outcomes
- "[exact quote]" — Context: [situation]

#### Objections / Hesitations
- "[exact quote]" — Context: [what prompted it]

#### Emotional Language
- "[phrase]" — Sentiment: [frustration / hope / anger / relief / desperation]

#### Trigger Events
- "[what made them search/buy]"

#### Competitor Mentions
- [Brand]: [positive / negative / neutral] — "[quote]"

#### Demographic Signals
- [age/gender/location/income/life stage indicators]

#### Unique Insights
- [anything notable]
---

## Synthesis

### 1. Top Pain Points (by frequency)

| Rank | Pain Point | Frequency | Intensity | Example Quote |
|------|-----------|-----------|-----------|---------------|
| 1 | | | | "" |
| 2 | | | | "" |
| 3 | | | | "" |
| 4 | | | | "" |
| 5 | | | | "" |

### 2. Customer Language Patterns

#### Recurring Phrases
- "[phrase]" — appeared across [N] sources

#### Emotional Vocabulary
- Frustration:
- Hope:
- Skepticism:

#### Metaphors and Comparisons
-

### 3. Objection Map

| Objection | Frequency | Underlying Fear | Counter-Evidence |
|-----------|-----------|----------------|------------------|
| | | | |

### 4. Desire Map

| Stated Desire | Deeper Desire | Frequency |
|--------------|---------------|-----------|
| | | |

### 5. Trigger Events

| Trigger | Frequency | Persona Fit |
|---------|-----------|------------|
| | | |

### 6. Demographic Clusters

| Cluster | Age Signal | Gender Signal | Situation | Notable Behavior |
|---------|-----------|--------------|-----------|-----------------|
| | | | | |

### 7. Competitor Landscape

| Competitor | Sentiment | Strengths (per customers) | Weaknesses (per customers) |
|-----------|-----------|--------------------------|---------------------------|
| | | | |

### 8. Sources Used

| # | URL | Platform | Data Points | Notes |
|---|-----|----------|-------------|-------|
| 1 | | | | |

### 9. Sources That Were Inaccessible

| URL | Reason |
|-----|--------|
| | |
"""


def main():
    if len(sys.argv) < 2:
        print("Usage: python research_template.py <product-name> [output-dir]")
        sys.exit(1)

    product_name = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    slug = slugify(product_name)

    output_path = os.path.join(output_dir, f"{slug}-research.md")
    template = generate_template(product_name)

    with open(output_path, "w") as f:
        f.write(template)

    print(f"Research template created: {output_path}")


if __name__ == "__main__":
    main()
