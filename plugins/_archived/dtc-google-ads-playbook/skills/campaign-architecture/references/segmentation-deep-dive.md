# Audience Segmentation Deep Dive

## Segmentation by Vertical

### Health / Telehealth / Weight Loss
| Segment | Why It Works | Offer Angle | Campaign Modifier |
|---------|-------------|-------------|-------------------|
| Women 25-54 | Largest market, highest intent | "Her Reset", empowerment | `-women-` |
| Seniors 55+ | High disposable income, Medicare-adjacent | "Senior Discount", affordability | `-senior-` |
| Moms 30-45 | Identity-triggered, "post-baby" motivation | "Mom Reset", reclaim body | `-mom-` |
| Men 35-55 | Lower competition, willing to pay premium | "Reclaim", transformation | `-men-` |
| Geographic (state) | Compliance, localized offers | State-specific savings | `-California-`, `-Texas-` |

### Supplements / Wellness
| Segment | Why It Works | Offer Angle | Campaign Modifier |
|---------|-------------|-------------|-------------------|
| Fitness enthusiasts | Already spending on wellness | Performance + science | `-fitness-` |
| Over 40 | Age-related health concerns | Anti-aging, vitality | `-over40-` |
| Women (hormonal health) | Underserved market | Balance, natural solutions | `-womens-health-` |
| Biohackers | Early adopters, high AOV | Cutting-edge, data-driven | `-biohack-` |

### Beauty / Skincare DTC
| Segment | Why It Works | Offer Angle | Campaign Modifier |
|---------|-------------|-------------|-------------------|
| Women 25-35 | Peak skincare spending | Glow-up, routine | `-young-women-` |
| Women 45+ | Anti-aging willingness to pay | Renewal, transformation | `-mature-` |
| Acne sufferers | High pain point, active searchers | Clear skin guarantee | `-acne-` |
| Men (grooming) | Growing market, less competition | Simple, effective | `-mens-groom-` |

### Pet / Pet Health DTC
| Segment | Why It Works | Offer Angle | Campaign Modifier |
|---------|-------------|-------------|-------------------|
| Dog owners | Largest pet market | Health, happiness, longevity | `-dog-` |
| Cat owners | Loyal, repeat purchasers | Indoor health, wellness | `-cat-` |
| Senior pet owners | Willing to spend on pet health | Senior pet care, mobility | `-senior-pet-` |
| New pet parents | Setup purchases, high initial spend | Starter bundle, essentials | `-new-pet-` |

## Segmentation Layering

The most effective approach layers audience + device + offer:

```
Primary:   gpm-$149-women-4                    (audience)
Variant:   gpm-$149-women-4-phone-excl         (audience + device)
Sub-test:  gpm-$149-women-4-California         (audience + geo)
Seasonal:  gpm-$149-women-feb-1                (audience + timing)
```

## When to Create Geographic Campaigns

Create state-level campaigns when:
- Product has state-specific compliance (telehealth, cannabis, supplements)
- Certain states show 2x+ conversion rate in location reports
- Running localized offers or promotions
- Testing state-specific landing pages

**Top-performing states for telehealth DTC (from Medvi data):**
- California, Texas, Florida, New York, North Carolina
- Start with top 5 states by population, expand based on performance

## Audience Signal Configuration for PMax

For each audience segment, configure PMax audience signals:

**Women segment signals:**
- Custom segments: weight loss, fitness, wellness, healthy eating
- In-market: health & fitness, weight management, nutrition
- Demographics: Female, 25-54
- Your data: website visitors, customer lists (if available)

**Senior segment signals:**
- Custom segments: Medicare, senior health, retirement wellness
- In-market: health insurance, pharmacy, senior services
- Demographics: 55+, both genders
- Your data: website visitors aged 55+

**Mom segment signals:**
- Custom segments: parenting, baby care, postpartum fitness
- In-market: baby & children's products, family health
- Demographics: Female, 25-45, parents
- Life events: Recently became a parent

## Budget Allocation by Segment

Initial budget split for a new DTC health account ($10K/day):

| Segment | % Budget | Daily Budget | Rationale |
|---------|----------|-------------|-----------|
| Women (broad) | 35% | $3,500 | Largest addressable market |
| Seniors | 25% | $2,500 | High intent, proven converter |
| Moms | 15% | $1,500 | Identity-driven, good CVR |
| Men | 10% | $1,000 | Test market, lower volume |
| Geographic tests | 10% | $1,000 | 2-3 state campaigns |
| Demand Gen | 5% | $500 | YouTube supplementary |

Adjust within 2 weeks based on CPA and volume data.
