#!/usr/bin/env python3
"""Stop hook: auto-update account profile watch list and decision log.

Meta Ads variant — includes platform-specific patterns for creative fatigue,
frequency, audience exhaustion, and Meta-specific actions.
Runs async so it never blocks session exit.
"""

import json
import os
import re
import sys
from datetime import date


def main():
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    # Prevent infinite loops — if stop hook is already active, bail
    if hook_input.get("stop_hook_active"):
        sys.exit(0)

    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
    profile_path = os.path.join(plugin_root, "profile", "account-profile.md")

    # If profile doesn't exist, skip silently
    if not os.path.isfile(profile_path):
        sys.exit(0)

    last_message = hook_input.get("last_assistant_message", "")
    if not last_message:
        sys.exit(0)

    watch_items = extract_watch_items(last_message)
    decision_items = extract_decision_items(last_message)
    test_items = extract_test_items(last_message)

    # Nothing to update
    if not watch_items and not decision_items and not test_items:
        sys.exit(0)

    try:
        with open(profile_path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError:
        sys.exit(0)

    today = date.today().isoformat()

    if watch_items:
        content = append_to_section(content, "## Watch List", watch_items, today)

    if decision_items:
        content = append_to_section(
            content, "## Decision Log", decision_items, today
        )

    if test_items:
        content = append_to_section(
            content, "## Active Tests", test_items, today
        )

    # Update last-updated date
    content = update_last_updated(content, today)

    try:
        with open(profile_path, "w", encoding="utf-8") as f:
            f.write(content)
    except OSError:
        pass

    # Always exit 0 — never block stop
    sys.exit(0)


def extract_watch_items(text: str) -> list[str]:
    """Extract watch-list-worthy items — includes Meta-specific patterns.

    Uses negative lookbehind for negation and sentence-bounded matching.
    """
    patterns = [
        # General patterns
        r"(?i)(?<!no )(?<!not )flag(?:ged|ging)?\b[^.!?\n]{5,80}",
        r"(?i)(?<!no )(?<!not )anomal(?:y|ies)\b[^.!?\n]{5,80}",
        r"(?i)(?<!no )(?<!not )(?<!stop )monitor(?:ing)?\b[^.!?\n]{5,80}",
        r"(?i)(?<!not )trending\b[^.!?\n]{5,80}",
        r"(?i)(?<!no )spike\b[^.!?\n]{5,80}",
        r"(?i)(?<!no )(?<!not )drop(?:ped|ping)?\b[^.!?\n]{5,80}",
        r"(?i)(?<!not )unusual\b[^.!?\n]{5,80}",
        # Meta-specific patterns (all use negation guards)
        r"(?i)(?<!no )(?<!not )creative fatigue\b[^.!?\n]{5,80}",
        r"(?i)(?<!no )(?<!not )frequency (?:spike|issue|concern|rising|high)\b[^.!?\n]{5,80}",
        r"(?i)(?<!no )(?<!not )CPM spike\b[^.!?\n]{5,80}",
        r"(?i)(?<!no )(?<!not )audience exhaustion\b[^.!?\n]{5,80}",
        r"(?i)(?<!no )(?<!not )hook rate (?:drop|declin|low)\b[^.!?\n]{5,80}",
        r"(?i)(?<!no )(?<!not )thruplay (?:drop|declin|low)\b[^.!?\n]{5,80}",
    ]
    items = []
    for pattern in patterns:
        for match in re.findall(pattern, text):
            cleaned = match.strip().rstrip(".")
            if len(cleaned) > 10 and cleaned not in items:
                items.append(cleaned)
    return _dedup_overlaps(items)[:5]  # Cap at 5 per session


def extract_decision_items(text: str) -> list[str]:
    """Extract decision-log-worthy items — includes Meta-specific actions.

    Patterns require action-verb context to avoid matching status reports.
    """
    patterns = [
        # Meta-specific patterns (checked first — more specific)
        r"(?i)paused creative\b[^.!?\n]{5,80}",
        r"(?i)refreshed audience\b[^.!?\n]{5,80}",
        r"(?i)adjusted budget\b[^.!?\n]{5,80}",
        r"(?i)new lookalike\b[^.!?\n]{5,80}",
        r"(?i)changed (?:bid|budget|optimization)\b[^.!?\n]{5,80}",
        r"(?i)updated (?:targeting|audience|creative)\b[^.!?\n]{5,80}",
        r"(?i)excluded (?:placement|audience)\b[^.!?\n]{5,80}",
        # General patterns (broader — checked after specific)
        r"(?i)paused (?:campaign|ad set|ad)\b[^.!?\n]{5,80}",
        r"(?i)enabled (?:campaign|ad set|ad)\b[^.!?\n]{5,80}",
        r"(?i)disabled (?:campaign|ad set|ad)\b[^.!?\n]{5,80}",
        r"(?i)removed (?:audience|placement|creative)\b[^.!?\n]{5,80}",
    ]
    items = []
    for pattern in patterns:
        for match in re.findall(pattern, text):
            cleaned = match.strip().rstrip(".")
            if len(cleaned) > 10 and cleaned not in items:
                items.append(cleaned)
    return items[:5]


def extract_test_items(text: str) -> list[str]:
    """Extract test-related items — includes Meta-specific test types."""
    patterns = [
        # General patterns
        r"(?i)started test\b[^.!?\n]{5,80}",
        r"(?i)completed test\b[^.!?\n]{5,80}",
        r"(?i)test results?\b[^.!?\n]{5,80}",
        r"(?i)launched experiment\b[^.!?\n]{5,80}",
        r"(?i)ended? test\b[^.!?\n]{5,80}",
        # Meta-specific test types
        r"(?i)creative test\b[^.!?\n]{5,80}",
        r"(?i)audience test\b[^.!?\n]{5,80}",
        r"(?i)placement test\b[^.!?\n]{5,80}",
        r"(?i)CBO test\b[^.!?\n]{5,80}",
    ]
    items = []
    for pattern in patterns:
        for match in re.findall(pattern, text):
            cleaned = match.strip().rstrip(".")
            if len(cleaned) > 10 and cleaned not in items:
                items.append(cleaned)
    return items[:3]


def _dedup_overlaps(items: list[str]) -> list[str]:
    """Remove items that are substrings of other items (keep the longer one)."""
    deduped = []
    for item in items:
        if not any(item in other and item != other for other in items):
            deduped.append(item)
    return deduped


def append_to_section(
    content: str, section_header: str, items: list[str], today: str
) -> str:
    """Append items to a profile section."""
    section_idx = content.find(section_header)
    if section_idx == -1:
        return content

    next_section = re.search(
        r"\n## ", content[section_idx + len(section_header) :]
    )
    if next_section:
        insert_pos = section_idx + len(section_header) + next_section.start()
    else:
        insert_pos = len(content)

    # Avoid blank line drift by checking existing newline
    new_entries = ""
    if insert_pos > 0 and content[insert_pos - 1] != "\n":
        new_entries = "\n"
    for item in items:
        new_entries += f"- [{today}] {item}\n"

    content = content[:insert_pos] + new_entries + content[insert_pos:]
    return content


def update_last_updated(content: str, today: str) -> str:
    """Update the Last updated date in the profile."""
    pattern = r"(?i)last updated:?\s*\d{4}-\d{2}-\d{2}"
    replacement = f"Last updated: {today}"
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
    return content


if __name__ == "__main__":
    main()
