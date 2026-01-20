# Changelog

All notable changes to the Prompt Plugin will be documented in this file.

## [2.1.1] - 2026-01-19

### Changed
- **Prompt-enhancer skill:** Added `allowed-tools` restriction (Read, Grep, Glob) for improved security

## [2.1.0] - 2026-01-16

### Changed
- **Renamed plugin:** `prompt-enhancer` → `prompt` for simpler, more direct naming

## [2.0.0] - 2026-01-10

### Changed
- BREAKING: Removed build-prompt wizard command
- Consolidated Claude 4.x tips into main SKILL.md
- Reduced XML tag library to 10 essential tags (from 50+)
- Reduced task templates from 7 to 3 (Document Analysis, Code Review, Data Analysis)

### Removed
- `commands/build-prompt.md` - wizard command
- `skills/prompt-enhancer/technique-loader.md` - redundant
- `skills/prompt-enhancer/model-specific-tips.md` - merged into SKILL.md
- `GETTING_STARTED.md` - redundant with README
- `assets/examples/common-patterns.md` - redundant
- `assets/examples/before-after-gallery.md` - examples in SKILL.md sufficient
- `assets/reference/new-techniques.md` - merged into SKILL.md
- `assets/reference/claude-4x-tips.md` - merged into SKILL.md

## [1.0.0] - 2025-12-27

### Added
- Initial release of Prompt Enhancer plugin
- `/prompt-enhancer` skill with systematic optimization workflow
- `/build-prompt` interactive wizard command
- Comprehensive before/after examples gallery (8-10 examples)
- Task-type specific templates (7 types: data-analysis, legal, creative, code-gen, customer-feedback, qa, summarization)
- Common patterns reference (8 patterns)
- XML tag library with comprehensive catalog
- 2025 techniques guide (prefilling, extended thinking, prompt chaining, long context)
- Claude 4.x optimization tips (Sonnet 4.5, Haiku 4.5)
- Quick reference cheat sheet

### Features
- Mandatory technique enforcement (XML tags, role, format, data separation)
- Contextual technique application (CoT, examples, prefilling, extended thinking)
- Progressive disclosure for efficient token usage
- Model-specific optimization (Sonnet 4.5 vs Haiku 4.5)
- Before/after comparison with explanations
- Production-ready output
- Interactive 8-phase wizard for building prompts

### Documentation
- README with quick start guide
- GETTING_STARTED with detailed usage patterns
- Usage examples
- Comprehensive reference materials
- Migration guide from Claude 3.x to Claude 4.x

### Techniques Covered
- **Mandatory:** XML tags, specific role, clear output format, data separation
- **Contextual:** Chain of thought, few-shot examples (with nuanced guidance)
- **New (2025):** Prefilling, extended thinking, prompt chaining, long context tips
- **Claude 4.x:** Literal interpretation, model-specific optimization, migration guidance
