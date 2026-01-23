# Ads Plugin Testing Notes

Living document tracking issues found during PMax campaign creation testing.

---

## Issues Found

### 1. Invalid Aspect Ratios in pmax-specs.md

**Location:** `plugins/ads/skills/assets/pmax-specs.md`

**Problem:** Documentation claims Nano Banana supports `2:1` and `21:9` aspect ratios, but Gemini API rejects them.

**Actual Gemini API ratios:** `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `9:16`, `16:9`

**Current (wrong):**
```markdown
Nano Banana supports: 1:1, 16:9, 9:16, 21:9, 4:3, 3:4, 2:1
Landscape mapping: 2:1
```

**Fix needed:**
- Line 29: Update supported ratios list
- Line 35: Change landscape from `2:1` → `16:9`
- Line 39: Change logo landscape from `21:9` → `4:3` or mark unsupported

**Upstream fix:** `nano-banana-mcp` repo AspectRatio enum advertises invalid values
- Repo: https://github.com/channel47/nano-banana-mcp

---

### 2. Portrait Aspect Ratio `4:5` Not Supported

**Location:** `plugins/ads/skills/assets/pmax-specs.md` + skill execution

**Problem:** Skill attempted `4:5` for portrait, but neither MCP nor Gemini supports it.

**MCP server enum:** `1:1`, `16:9`, `9:16`, `21:9`, `4:3`, `3:4`, `2:1`
**Gemini API actual:** `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `9:16`, `16:9`

**Note:** pmax-specs.md line 37 correctly says to use `3:4` for portrait, but the skill execution used `4:5` anyway. This suggests either:
- The skill isn't reading the reference doc
- The prompt phrasing "4:5 aspect ratio for 960x1200" led Claude to use literal `4:5`

**Fix needed:**
- Ensure SKILL.md explicitly states to use `3:4` (not `4:5`) for portrait
- Or add clearer mapping table that skill must follow

---

### 3. Text Assets Generated But Not Visible in Flow

**Location:** `plugins/ads/skills/pmax/SKILL.md`

**Status:** PARTIALLY RESOLVED - Text assets were written to `campaign-config.md` early in the flow, but user didn't see this happen (possibly during context crunch or rapid file writes).

**What WAS generated (in campaign-config.md):**
- 15 headlines with character counts (all compliant)
- 5 long headlines with character counts
- 5 descriptions with character counts
- Audience signals (custom segments, first-party, Google audiences)
- Comprehensive setup checklist

**What's MISSING from config:**
- Sitelink extensions
- Callout extensions
- Structured snippets
- Price extensions (if applicable)
- Promotion extensions

**Fix needed:**
- Make text asset generation more visible in conversation
- Add asset extensions section to skill output
- Query which extensions are relevant for PMax vs Search

---

### 6. Skills Should Teach Principles, Not Prescribe Content

**Philosophy:** Skills should guide toward better outcomes without baking in pre-written templates. The goal is capability to craft compelling, data-backed assets across any industry.

**What the research revealed - Winning headline patterns:**
- Price anchoring (compare to expensive alternatives)
- Social proof with specific numbers ("100,000+ sold")
- Simple benefit claims ("Hair-Free 6 Weeks" not "Up To 6 Weeks")
- Specific mechanism + results (not just feature name)

**The skill's generic headlines missed these patterns.** Fix is NOT to add template headlines, but to add principle-based guidance that teaches the AI to apply these patterns contextually.

**Implementation approach:**
- Add reference doc: `copywriting-principles.md` or similar
- Document patterns with examples, not templates
- Skill reads principles and applies to specific product/industry context
- Let AI synthesize, not copy-paste

---

### 7. Asset Quantity Gap - Skill Produces Minimums

**Problem:** Skill generated bare minimums when successful campaigns use much more.

**Current vs Successful PMax campaigns:**

| Asset Type | Skill Output | Successful Campaigns |
|------------|--------------|---------------------|
| Images | 4 total | 10-20 per format |
| Callouts | 0 | 10-15 |
| Sitelinks | 0 | 6-8 with descriptions |
| Structured Snippets | 0 | 3-4 headers |
| Promotion Assets | 0 | Active promotions |
| Videos | 0 | 3-5 minimum |

**Fix approach (grounded in real-world expertise, not user's account):**
- Don't assume user has existing data (new accounts exist)
- Don't assume user's existing data represents best practice
- Ground guidance in industry benchmarks, Google's recommendations, and cross-account research
- Add reference doc: `asset-benchmarks.md` with ranges from proven campaigns
- Present as "high-performing PMax campaigns typically have X" with source context
- Let user choose scope (minimum viable vs full build)

**Reference sources to incorporate:**
- Google Ads best practices documentation
- Aggregated learnings from successful campaigns (anonymized)
- Industry-specific benchmarks where available

---

### 4. Skill Punts to Manual UI Instead of Using MCP

**Location:** `plugins/ads/skills/pmax/SKILL.md` - "Next Steps" section

**Problem:** Final output says:
> "1. Create campaign in Google Ads UI
> 2. Upload the 4 images from assets/ folder
> 3. Copy text assets from config..."

**This defeats the purpose.** The plugin has Google Ads MCP with `mutate` capability. The skill should:
1. Build the campaign mutation payload
2. Execute via `mcp__google-ads__mutate` (with `dry_run: true` first)
3. Create the campaign programmatically

**Current state:** Skill is a "config generator" not a "campaign creator"

**Fix needed:**
- Add Phase 7: Campaign Creation via MCP
- Build proper mutation payload (campaign, asset groups, assets, audience signals)
- Dry run first, then execute with user confirmation
- Only fall back to "manual steps" if MCP unavailable

---

### 5. Asset Generation Lacks Quantity/Type Control

**Location:** `plugins/ads/skills/assets/SKILL.md`

**Problem:** Skill generated minimum assets (4 total) without asking user preferences for quantity or creative types.

**Generated:**
- 1 Landscape (product shot)
- 1 Square (product shot)
- 1 Portrait (product shot)
- 1 Logo

**Missing UX:**
1. No prompt for number of images per size (e.g., "How many landscape images? 1-10")
2. No prompt for creative types (product, lifestyle, before/after, social proof, promotional)
3. No context-aware suggestions based on product/campaign type

**Example gap:** For hair removal product (Glabrous Skin), before/after images are highly effective and relevant. Skill should have suggested this based on product category, but generated only standard product shots.

**Fix needed:**
- Add Phase 1 question: "How many images per size?" (default: 3-5)
- Add Phase 1 question: "Which creative types?" with context-aware defaults
- Build product-category → suggested-types mapping:
  - Beauty/skincare → before/after, lifestyle, social proof
  - Electronics → product hero, lifestyle, feature callouts
  - Food/beverage → lifestyle, seasonal, social proof
  - Services → social proof, lifestyle, outcome-focused

---

### 8. Skill Must Ruthlessly Verify Facts Before Campaign Creation

**Observation:** When prompted, AI used Playwright to verify checkout page pricing and found discrepancy:
- Assumed: $39 / 60% off
- Actual: $59.99 / 50% off (1x), $109.99 / 56% off (2x bestseller)

**This verification happened only when user prompted.** Should be automatic.

**Fix needed - mandatory verification phase before campaign creation:**
- Price points (visit checkout/product page)
- Discount percentages (verify against actual offers)
- Shipping claims (free shipping thresholds, delivery times)
- Stock/availability status
- Any numeric claims in headlines (social proof numbers, time claims)

**Implementation:**
- Add verification phase after asset generation, before campaign creation
- Use Playwright to scrape actual offer details
- Flag any discrepancies between generated copy and real data
- Block campaign creation if critical facts unverified

**Why this matters:**
- Ads with wrong prices = policy violations, wasted spend, customer complaints
- Wrong discount percentages = misleading advertising
- This is a trust/quality gate, not optional

---

### 9. Skipped dry_run Safety Check on Campaign Creation

**Problem:** When user said "yes create it", AI went straight to `dry_run: false` without first validating with `dry_run: true`.

**Earlier behavior:** AI did use `dry_run: true` initially (good), but when proceeding to actual creation, skipped the validation step.

**Expected flow:**
1. User confirms readiness
2. Execute with `dry_run: true` to validate payload
3. Show user what WOULD be created
4. Get explicit confirmation
5. Execute with `dry_run: false`

**Fix needed:**
- Skill must ALWAYS dry_run before live execution
- Present dry_run results to user for review
- Require explicit "execute for real" confirmation after seeing dry_run output
- Never go straight to `dry_run: false` even if user says "create it"

**Why this matters:**
- Mutations are hard/impossible to undo
- Dry run catches payload errors before they create broken campaigns
- User should see exactly what will be created before it happens

---

### 10. Query Existing Assets BEFORE Generating New Ones

**Problem:** Skill generated a new logo when account already had usable logos.

**What happened:**
- Skill generated `logo-1200x1200.png` using Nano Banana
- Later discovered account already had 5 existing logo assets
- Existing logo + business name assets could have been reused

**Wasted effort:**
- AI image generation API call (cost)
- User time reviewing unnecessary asset
- Potential for inconsistent branding (new vs existing logo)

**Fix needed - pre-generation inventory check:**
1. Before asset generation phase, query account for existing assets:
   - Logos (square and landscape)
   - Business name
   - Existing image assets that could be reused
2. Present inventory to user: "Found existing logo. Use it or generate new?"
3. Only generate what's actually needed

**Query to run early in flow:**
```sql
SELECT asset.name, asset.resource_name, asset.type, asset.image_asset.full_size.url
FROM asset
WHERE asset.type IN ('IMAGE', 'LOGO')
```

---

### 11. Mutate Payload Errors - Skill Lacks API Schema Knowledge

**Problem:** Multiple failed mutate attempts before getting payload structure correct.

**Errors encountered:**
1. "Campaign CREATE requires a bidding strategy" - used `bidding_strategy_type` instead of `maximize_conversions: {}`
2. "Invalid enum value: BUSINESS_NAME" - wrong query syntax for asset types
3. "Field must be present in SELECT clause: campaign.id" - GAQL join requirements
4. Multiple validation errors even after fixes

**Root cause:** Skill/AI doesn't have reliable knowledge of Google Ads API schema and GAQL quirks.

**Fix needed:**
- Add reference doc: `google-ads-api-schemas.md` with correct payload structures
- Include common mutation patterns with working examples
- Document GAQL gotchas (required fields in SELECT, valid enum values)
- Consider: MCP server could expose schema validation endpoint

---

### 12. Skill Asks "API or UI?" After Already Committing to API

**Problem:** After successfully:
- Creating campaign via API
- Validating 15 headlines
- Validating 5 long headlines + 5 descriptions

...the skill asks user: "Continue via API, complete in UI, or hybrid?"

**This is issue #4 resurfacing.** The skill should commit to the API approach and execute, not punt the decision back to user mid-flow.

**What should happen:**
- Skill commits to API execution from the start
- Executes all mutations sequentially (campaign → assets → asset group → asset links)
- Only offers UI fallback if API fails completely
- Never asks "which approach?" after already making API calls

**Positive observations from this flow:**
- AI learned to use `dry_run: true` after being rejected
- AI discovered `partial_failure: false` was needed for certain operations
- AI correctly sequenced: campaign first, then text assets, then asset group
- Validation working properly

**The execution engine is there, but skill doesn't commit to using it.**

---

### 13. Nano Banana Saves JPEGs with .png Extension

**Problem:** Generated images failed upload with "not a valid PNG"

**What happened:**
```bash
file *.png
# landscape-1200x628.png: JPEG image data, JFIF standard 1.01
# (all files were actually JPEGs)
```

**Root cause:** Nano Banana MCP saves JPEG files but gives them `.png` extension.

**Workaround AI used:** Renamed files to `.jpg`, upload succeeded.

**Upstream fix needed:** `nano-banana-mcp` should either:
1. Actually generate PNGs when output_path ends in `.png`
2. Or: force correct extension based on actual format
3. Or: add format parameter to control output type

**Location:** https://github.com/channel47/nano-banana-mcp

---

### 14. Nano Banana Doesn't Generate Exact Pixel Dimensions

**Problem:** Asset group creation failed with "aspect ratio does not match"

**Requested vs Actual:**
| Asset | Requested | Generated |
|-------|-----------|-----------|
| Landscape | 1200 x 628 | 1376 x 768 |
| Square | 1200 x 1200 | 1024 x 1024 |
| Portrait | 960 x 1200 | 768 x 1376 |

**Root cause:** Gemini generates images at aspect ratio, not exact dimensions. MCP doesn't post-process to resize.

**Impact:** Google Ads rejects images that don't match exact spec (1.91:1 for landscape = 1200x628, not 1376x768).

**Fix options:**
1. **MCP-level:** Add post-processing to resize to exact requested dimensions
2. **Skill-level:** Add image processing step after generation (resize/crop)
3. **Workflow:** Skill should verify dimensions after generation, before upload

**Workaround AI used:** Queried existing images in account with correct dimensions and used those instead.

---

### 15. Full API Execution Chain SUCCEEDED

**CAMPAIGN CREATED VIA API:**

| Component | ID |
|-----------|-----|
| Campaign | 23498301265 |
| Budget | 15310727999 ($165/day) |
| Asset Group | 6663766911 (Core Glabrous) |

**Assets linked (30 operations):**
- 15 headlines
- 5 long headlines
- 5 descriptions
- 1 landscape image (1200x628) - reused from account
- 1 square image (1200x1200) - reused from account
- 1 logo - reused from account
- 1 business name - reused from account

**What the execution required:**
- Multiple dry_run cycles to validate payloads
- File format diagnosis and fix (JPEG→PNG extension)
- Fallback to existing account images (dimension mismatch)
- Proper sequencing: campaign → text assets → image assets → asset group + links

**Still noted as "manual in UI":**
- More images (5-10 per format)
- Portrait images
- Callouts, sitelinks, structured snippets
- Audience signals (custom segments)
- Geo targeting
- Enable campaign (currently PAUSED)

**Assessment:** The execution engine IS capable of full campaign creation. Issues are:
1. Upstream MCP bugs (file format, dimensions)
2. Skill guidance gaps (doesn't commit to API, missing asset types)
3. Schema knowledge (multiple failed mutations before success)

**User requested analyst subagent to verify:** Spawned to check that no other campaigns/assets were affected.

**ANALYST AUDIT RESULTS: PASS WITH WARNINGS**

| Category | Status |
|----------|--------|
| Unintended Changes | NONE DETECTED |
| Campaign Created | CORRECT |
| Asset Group Created | CORRECT |
| Text Assets Linked | 25/25 PASS |
| Existing Campaigns | UNCHANGED |
| Existing Budgets | UNCHANGED |

**Verified Safe:**
- Existing PMax campaign (23456417403) - UNCHANGED
- All 8 active campaigns - UNCHANGED
- All existing budgets - UNCHANGED
- All existing asset groups - UNCHANGED
- No UPDATE or REMOVE operations - Only CREATE

**Warnings (known issues):**
- 4 uploaded images not linked (dimension mismatch - Issue #14)
- Portrait image missing (0 linked)

**Bottom line:** MCP mutate tool worked correctly and safely. No collateral damage. Only known image dimension issues.

---

## Observations

### Working Well

- Skill loading (`/ads:pmax`)
- Context gathering from `meta.yaml` and landing page
- Proactive account analysis (checking existing campaigns)
- GAQL queries via Google Ads MCP
- Fact verification via Playwright (when prompted)
- User question flow (budget, etc.)
- Adaptive workflow (not rigid phase-following)

### To Verify

- [ ] Full asset generation workflow after ratio fix
- [ ] Text asset generation (headline/description character limits)
- [ ] Campaign configuration output document
- [ ] `/ads:assets` handoff from pmax skill

---

## Test Session Info

**Date:** 2025-01-23
**Product:** Glabrous Skin (epilator)
**Campaign Type:** PMax
**Budget:** $5,000+/month
**Market:** US

---

## Change Log

| Date | Issue | Status |
|------|-------|--------|
| 2025-01-23 | Aspect ratio mapping incorrect | Noted |
