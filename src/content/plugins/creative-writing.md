---
featured: false
draft: false
---

## What it does

Transform your writing from AI-generated patterns to clear, honest prose. This plugin helps you write with your own voice. Use it to edit AI drafts or create content from scratch.

## Key Features

- **Edit drafts**: Rewrite content to remove AI tells and improve clarity
- **Generate content**: Create first drafts that match your style guide
- **Review writing**: Get specific, actionable feedback without automatic rewrites
- **Improve sections**: Fix openings, strengthen endings, or clean specific problems
- **Custom style guides**: Create personalized guides through interactive questionnaire
- **Smart chunking**: Loads only relevant style guide sections to keep token usage efficient

## Real-world use cases

Daily uses:

- Cleaning up AI-generated blog drafts (removing em-dashes, hype words, and other tells)
- Getting feedback on technical writing without automatic rewrites
- Fixing weak introductions that bury the lead
- Strengthening conclusions that trail off
- Generating initial drafts that already sound like me

## What makes it different

Most writing tools either give you vague feedback or rewrite everything automatically. This plugin does both. You choose the approach.

Use `/review-writing` to get specific problems to fix yourself. Use `/edit-draft` to rewrite everything to match your style. Use `/improve-opening` or `/strengthen-ending` to focus on specific sections. Use `/remove-ai-tells` to quickly strip common AI patterns.

All skills work with custom style guides. The more you use it, the better it gets at matching your voice.

## Setup

1. Install: `/plugin install creative-writing@channel47`
2. Try it immediately with `/edit-draft` or `/review-writing`
3. (Optional) Create a custom style guide with `/generate-style-guide`

## Example workflows

**Quick cleanup:**

```
/remove-ai-tells
```

Paste your AI-generated draft. Gets back clean prose in seconds.

**Thoughtful revision:**

```
/review-writing
```

Get specific feedback on what to change and why. You make the edits.

**Full rewrite:**

```
/edit-draft
```

Paste your draft. The plugin rewrites it following style guide principles.

**Custom style:**

```
/generate-style-guide
```

Answer questions about your preferences. Save the guide, then use:

```
/edit-draft --style-guide docs/my-guide.md
```

## Available skills

- `/edit-draft` - Rewrite content to match style guide
- `/generate-content` - Create first drafts from prompts
- `/review-writing` - Get feedback without automatic rewrites
- `/improve-opening` - Fix first 1-3 paragraphs
- `/strengthen-ending` - Improve conclusions
- `/remove-ai-tells` - Strip common AI patterns (em-dashes, hype, etc.)
- `/generate-style-guide` - Create personalized style guide via questionnaire

See the [Getting Started Guide](https://github.com/ctrlswing/channel47-marketplace/blob/main/plugins/creative-writing/GETTING_STARTED.md) for workflow tips and customization options.
