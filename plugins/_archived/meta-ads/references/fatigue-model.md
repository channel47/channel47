# Creative Fatigue Model

## Lifecycle Stages

| Stage | Criteria | Action |
|-------|----------|--------|
| Testing | <500 impressions OR <$25 spend | Wait — insufficient data |
| Rising | Frequency <2.0, CTR improving or stable, CPA at/below target | Scale — increase budget |
| Peak | Best 7d CTR in ad's history, frequency 1.5-2.5 | Maintain — don't touch |
| Fatiguing | Frequency >2.5, CTR declined >15% from peak 7d, CPM rising >10% | Plan replacement — 5-10 days remaining |
| Dead | Frequency >4.0 OR CTR declined >40% from peak OR CPA >2x target | Replace immediately |

## Days Remaining Formula

For ads in Fatiguing stage:

```
daily_ctr_decay = (peak_7d_ctr - current_7d_ctr) / days_since_peak
days_to_dead = (current_7d_ctr - dead_threshold_ctr) / daily_ctr_decay
dead_threshold_ctr = peak_7d_ctr * 0.60  (40% decline = Dead)
```

If daily_ctr_decay <= 0 (CTR not declining), days_remaining = "Stable" (re-evaluate in 7 days).

## Frequency-CTR Decay Correlation

Typical decay curve by vertical:

| Vertical | Frequency at Peak CTR | Frequency at 50% CTR | Typical Peak-to-Dead Days |
|----------|---------------------:|---------------------:|--------------------------:|
| E-commerce | 2.0-2.5 | 4.0-5.0 | 14-21 |
| B2B/SaaS | 2.5-3.0 | 5.0-7.0 | 21-35 |
| Local Services | 1.5-2.0 | 3.0-4.0 | 10-14 |
| Education | 2.0-3.0 | 4.5-6.0 | 18-28 |

These are directional benchmarks. Account history always takes precedence.

## CPM Inflation Signal

Rising CPM without audience size changes suggests:
1. Creative fatigue (Meta charges more to show stale ads)
2. Auction competition increase
3. Seasonal demand shifts

Distinguish by checking: if frequency is rising alongside CPM, it's likely fatigue. If frequency is stable but CPM rises, it's auction competition.
