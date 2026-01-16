# Changelog

All notable changes to the Copy Plugin will be documented in this file.

## [2.1.0] - 2026-01-16

### Changed
- **Renamed plugin:** `copywriting-expert` → `copy` for simpler, more direct naming

## [2.1.0] - 2026-01-16

### Changed
- Revised email command to be less prescriptive with flexible guidance
- Revised headline command to use flexible output guidance instead of rigid templates
- Revised landing-page command to replace rigid section templates with adaptable components
- Revised swipe and weakness analyze commands with flexible output guidance
- Added product type variations (SaaS, physical products, services) to landing-page
- Added audience sophistication guidance (expert, general, mixed) to landing-page
- Added "Variations by Context" sections (premium/mass market, audience awareness levels)
- Added "When to Adapt" sections for deviating from standard patterns (short copy, specific focus, quick vs deep)
- Converted rigid templates to adaptable approaches across commands
- Formula categories repositioned as inspiration examples rather than requirements

## [2.0.0] - 2026-01-10

### Changed
- BREAKING: Simplified to 3 core frameworks (Schwartz, Hemingway, Halbert)
- Consolidated commands to 5 essentials (headline, email, landing-page, swipe, weakness)

### Removed
- All agents (headline-generator, email-sequencer, copy-doctor)
- Mode commands (fusion, hemingway, schwartz, halbert)
- Transform commands (compress, add-proof, raise-stakes)
- 8 frameworks: Homer, Dickens, Chekhov, Campbell, Ogilvy, Carlton, Sugarman, Bencivenga
- All fusion templates (origin-story-sales, metaphor-first-landing, character-email-sequence)
- Reference library (headline-formulas, emotional-triggers, proof-hierarchy, swipe-file-anatomy)
- lead.md command (merged into landing-page)
- GETTING_STARTED.md

## [1.0.0] - 2024-12-29

### Added

#### Skill
- Main copywriting skill with auto-detection for persuasive writing tasks
- Decision framework for selecting appropriate copywriting approach
- Integration with all frameworks, references, and tools

#### Storyteller Frameworks
- **Homer Mode** (`frameworks/storytellers/homer.md`)
  - Epic narrative structure
  - Transformation arc templates
  - Before/after examples
- **Hemingway Mode** (`frameworks/storytellers/hemingway.md`)
  - Iceberg theory principles
  - Compression techniques
  - Edit process guidelines
- **Dickens Mode** (`frameworks/storytellers/dickens.md`)
  - Sensory specificity techniques
  - Character-in-action methods
  - Environmental storytelling
- **Chekhov Mode** (`frameworks/storytellers/chekhov.md`)
  - Subtext principles
  - Show-don't-tell techniques
  - Earned emotion guidelines
- **Campbell Mode** (`frameworks/storytellers/campbell.md`)
  - Hero's journey for copy
  - 11-stage adaptation
  - Prospect-as-hero positioning

#### Direct Response Frameworks
- **Schwartz** (`frameworks/direct-response/schwartz.md`)
  - Five levels of awareness
  - Sophistication spectrum
  - Lead type matching
- **Halbert** (`frameworks/direct-response/halbert.md`)
  - A-pile concept
  - Conversational urgency
  - P.S. techniques
- **Ogilvy** (`frameworks/direct-response/ogilvy.md`)
  - Research methodology
  - Proof hierarchy
  - Long copy principles
- **Carlton** (`frameworks/direct-response/carlton.md`)
  - Sales detective approach
  - Voice development
  - Hook creation
- **Sugarman** (`frameworks/direct-response/sugarman.md`)
  - Slippery slide technique
  - 24 psychological triggers
  - First sentence rules
- **Bencivenga** (`frameworks/direct-response/bencivenga.md`)
  - Emotional logic
  - Hidden benefit discovery
  - Reason-why principle

#### Fusion Frameworks
- **Origin Story + Sales** (`frameworks/fusion/origin-story-sales.md`)
  - Homer + Halbert + Bencivenga combination
  - Brand story templates
- **Metaphor-First Landing** (`frameworks/fusion/metaphor-first-landing.md`)
  - Chekhov + Homer + Sugarman combination
  - Premium brand approach
- **Character Email Sequence** (`frameworks/fusion/character-email-sequence.md`)
  - Dickens + Schwartz + Sugarman combination
  - 6-email sequence templates

#### Reference Materials
- **Swipe File Anatomy** (`reference/swipe-file-anatomy.md`)
  - 7-layer analysis framework
  - Quick analysis template
  - Swipe file organization
- **Headline Formulas** (`reference/headline-formulas.md`)
  - 10 formula categories
  - 100+ headline templates
  - Power-up techniques
- **Emotional Triggers** (`reference/emotional-triggers.md`)
  - 7 core emotional drivers
  - Secondary triggers
  - Emotional progression mapping
- **Proof Hierarchy** (`reference/proof-hierarchy.md`)
  - 10-level proof ranking
  - Stacking strategies
  - Acquisition techniques

#### Slash Commands
- **Modes**
  - `/hemingway` - Activate sparse mode
  - `/halbert` - Activate conversational mode
  - `/schwartz [level]` - Apply awareness strategy
  - `/fusion [storyteller] [marketer]` - Combine frameworks
- **Write**
  - `/headline [product] [angle]` - Generate 20+ headlines
  - `/lead [type]` - Craft compelling leads
  - `/email [position]` - Write sequence emails
  - `/landing-page [product]` - Full page copy
- **Analyze**
  - `/swipe [copy]` - Deconstruct any copy
  - `/weakness [copy]` - Find and fix holes
- **Transform**
  - `/raise-stakes` - Amplify emotional tension
  - `/add-proof` - Layer in credibility
  - `/compress` - Hemingway reduction

#### Agents
- **Copy Doctor** (`agents/copy-doctor/agent.md`)
  - Diagnoses copy weaknesses
  - Provides specific fixes
  - Prioritizes improvements
- **Headline Generator** (`agents/headline-generator/agent.md`)
  - Produces 20+ variations
  - Covers multiple formulas
  - Ranks recommendations
- **Email Sequencer** (`agents/email-sequencer/agent.md`)
  - Plans complete sequences
  - Writes full email copy
  - Maps emotional arcs

#### Utility Scripts
- `scripts/analyze_swipe.py` - Automated copy analysis
- `scripts/awareness_check.py` - Awareness level assessment

#### Documentation
- README.md - Overview and quick reference
- GETTING_STARTED.md - Learning path and tutorials
- CHANGELOG.md - Version history

---

## Future Roadmap

### Planned for v1.1
- Voice profile system for brand consistency
- Additional fusion frameworks
- VSL-specific templates
- Social media ad frameworks

### Planned for v1.2
- Swipe file database integration
- A/B test tracking
- Performance analytics
- Custom framework creation

### Under Consideration
- AI-powered headline scoring
- Competitive analysis tools
- Multi-language support
- Team collaboration features
