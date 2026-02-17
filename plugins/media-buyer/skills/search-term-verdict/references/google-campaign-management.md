# Google Campaign Management (Search Term Verdict)

Use `mcp__google-ads__mutate` to apply negative keyword actions derived from verdict output.

## Safety workflow

1. Run search term queries with `mcp__google-ads__query`.
2. Build negative keyword operations from `NEGATE` verdicts.
3. Run `mcp__google-ads__mutate` with `dry_run: true`.
4. Show grouped preview by campaign/ad group.
5. Ask for explicit approval before `dry_run: false`.

## Negative keyword strategy

- `EXACT`: block only a specific query.
- `PHRASE`: block the core irrelevant phrase in broader contexts.
- `BROAD`: use rarely, only for unambiguously irrelevant tokens.

## Level strategy

- Ad-group level for local theme mismatch.
- Campaign level for broad mismatch across ad groups.
- Account-wide exclusions should be recommended via shared negative lists in the Google Ads UI.

## Preview requirements

Every preview row should include:

- keyword text
- match type
- level (`campaign` or `ad_group`)
- parent ID/name
- recent spend and conversion context
- rationale summary
