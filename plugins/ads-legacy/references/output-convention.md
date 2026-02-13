# Output Directory Convention

All generated files follow a consistent structure for organization and discoverability.

## Directory Structure

```
./ads-output/
├── YYYY-MM-DD-[project-name]/
│   ├── research/
│   │   ├── keyword-research.md
│   │   ├── keywords.csv
│   │   ├── keywords-copypaste.txt
│   │   ├── negatives.csv
│   │   └── competitor-research.md
│   ├── campaigns/
│   │   ├── search-campaign.md
│   │   ├── search-keywords.csv
│   │   ├── search-ads.csv
│   │   ├── search-negatives.csv
│   │   └── pmax-campaign.md
│   ├── copy/
│   │   ├── ad-copy.md
│   │   └── ad-copy.csv
│   ├── audit/
│   │   └── audit-report.md
│   └── assets/
│       ├── landscape-1200x628.png
│       ├── square-1200x1200.png
│       └── asset-manifest.md
└── YYYY-MM-DD-[another-project]/
    └── ...
```

## Naming Conventions

### Project Folder

Format: `YYYY-MM-DD-[project-name]`

Examples:
- `2026-01-30-acme-widgets`
- `2026-01-30-notion-competitor`
- `2026-01-30-summer-campaign`

The project name should be:
- Lowercase
- Hyphens instead of spaces
- Derived from product/brand name or campaign purpose
- Max 30 characters

### File Names

| Type | Pattern | Example |
|------|---------|---------|
| Research report | `keyword-research.md` | `keyword-research.md` |
| Keywords CSV | `keywords.csv` | `keywords.csv` |
| Negatives CSV | `negatives.csv` | `negatives.csv` |
| Campaign strategy | `[type]-campaign.md` | `search-campaign.md` |
| Ad copy | `ad-copy.md` | `ad-copy.md` |
| Audit report | `audit-report.md` | `audit-report.md` |
| Assets | `[format]-[dimensions].png` | `landscape-1200x628.png` |

## Implementation

### Phase 0: Directory Setup

At the start of any skill that generates files, establish the output location:

```markdown
### Determine Output Location

1. Check if user specified a location
2. If not, ask:

> "Where should I save the output files?
>
> 1. **Default** - `./ads-output/[date]-[project]/` (recommended)
> 2. **Current directory** - Save files here
> 3. **Custom path** - Specify a location
>
> Which option?"

3. If default selected, derive project name from:
   - Product/brand name from landing page
   - User's stated project name
   - Fallback: "campaign"

4. Create directory structure:
   - `./ads-output/YYYY-MM-DD-[project]/`
   - Subdirectory based on skill type (research/, campaigns/, etc.)
```

### Creating the Directory

Use Bash to create the directory:

```bash
mkdir -p ./ads-output/2026-01-30-acme-widgets/campaigns
```

### File References in Output

When generating markdown reports, use relative paths to reference related files:

```markdown
## Related Files

- Keywords: [keywords.csv](./keywords.csv)
- Negatives: [negatives.csv](./negatives.csv)
```

## Settings Override

Users can customize the output directory in `.claude/ads.local.md`:

```yaml
---
output_directory: "./ads-output"
---
```

Skills should check for this setting and use it as the base path.

## Benefits

1. **Discoverability** - All outputs in one predictable location
2. **Organization** - Date-prefixed folders prevent overwriting
3. **Portability** - Relative paths work when folder is moved
4. **History** - Easy to compare outputs across dates
5. **Cleanup** - Simple to archive or delete old outputs
