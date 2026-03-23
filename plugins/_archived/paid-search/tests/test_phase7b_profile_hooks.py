"""Phase 7b: Profile hooks and profile-review skill tests.

Validates:
- SessionStart hook (inject-profile.sh) exists and is executable
- Stop hook (update-profile.py) exists
- hooks.json contains SessionStart and Stop entries
- hooks.json preserves existing PreToolUse entries (no regression)
- profile-review skill exists with required sections
- Hook scripts handle missing profile gracefully
"""

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


HOOKS_DIR = Path("hooks")
HOOKS_JSON = HOOKS_DIR / "hooks.json"
INJECT_SCRIPT = HOOKS_DIR / "inject-profile.sh"
UPDATE_SCRIPT = HOOKS_DIR / "update-profile.py"
PROFILE_REVIEW_SKILL = Path("skills/profile-review/SKILL.md")


class TestSessionStartHook(unittest.TestCase):
    def test_inject_profile_script_exists(self):
        self.assertTrue(
            INJECT_SCRIPT.exists(),
            f"SessionStart hook script not found at {INJECT_SCRIPT}",
        )

    def test_inject_profile_script_is_executable(self):
        self.assertTrue(
            os.access(INJECT_SCRIPT, os.X_OK),
            f"{INJECT_SCRIPT} is not executable",
        )

    def test_inject_profile_handles_missing_profile(self):
        """Script exits 0 with no output when profile doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            env = os.environ.copy()
            env["CLAUDE_PLUGIN_ROOT"] = tmpdir  # No profile/ dir
            result = subprocess.run(
                ["bash", str(INJECT_SCRIPT)],
                input='{"source": "user"}',
                capture_output=True,
                text=True,
                env=env,
                timeout=5,
            )
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "")

    def test_inject_profile_skips_on_compact(self):
        """Script exits 0 with no output when source is compact."""
        result = subprocess.run(
            ["bash", str(INJECT_SCRIPT)],
            input='{"source": "compact"}',
            capture_output=True,
            text=True,
            timeout=5,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")

    def test_inject_profile_outputs_valid_json(self):
        """Script outputs valid JSON with profile content when profile exists."""
        with tempfile.TemporaryDirectory() as tmpdir:
            profile_dir = Path(tmpdir) / "profile"
            profile_dir.mkdir()
            profile_file = profile_dir / "account-profile.md"
            profile_file.write_text("# Test Profile\n## Accounts\n- test")

            env = os.environ.copy()
            env["CLAUDE_PLUGIN_ROOT"] = tmpdir
            result = subprocess.run(
                ["bash", str(INJECT_SCRIPT)],
                input='{"source": "user"}',
                capture_output=True,
                text=True,
                env=env,
                timeout=5,
            )
            self.assertEqual(result.returncode, 0)
            output = json.loads(result.stdout)
            self.assertIn("hookSpecificOutput", output)
            self.assertEqual(
                output["hookSpecificOutput"]["hookEventName"], "SessionStart"
            )
            self.assertIn(
                "# Test Profile",
                output["hookSpecificOutput"]["additionalContext"],
            )


class TestStopHook(unittest.TestCase):
    def test_update_profile_script_exists(self):
        self.assertTrue(
            UPDATE_SCRIPT.exists(),
            f"Stop hook script not found at {UPDATE_SCRIPT}",
        )

    def test_update_profile_handles_missing_profile(self):
        """Script exits 0 when profile doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            env = os.environ.copy()
            env["CLAUDE_PLUGIN_ROOT"] = tmpdir  # No profile/ dir
            result = subprocess.run(
                ["python3", str(UPDATE_SCRIPT)],
                input=json.dumps({
                    "stop_hook_active": False,
                    "last_assistant_message": "flagged a CPA spike",
                }),
                capture_output=True,
                text=True,
                env=env,
                timeout=10,
            )
            self.assertEqual(result.returncode, 0)

    def test_update_profile_exits_on_stop_hook_active(self):
        """Script exits 0 immediately when stop_hook_active is true."""
        result = subprocess.run(
            ["python3", str(UPDATE_SCRIPT)],
            input=json.dumps({
                "stop_hook_active": True,
                "last_assistant_message": "flagged a CPA spike",
            }),
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0)


class TestHooksJsonRegistration(unittest.TestCase):
    def setUp(self):
        with open(HOOKS_JSON, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        self.hooks = self.config.get("hooks", {})

    def test_session_start_entry_exists(self):
        self.assertIn(
            "SessionStart",
            self.hooks,
            "hooks.json missing SessionStart entry",
        )

    def test_session_start_references_inject_script(self):
        entries = self.hooks["SessionStart"]
        commands = []
        for entry in entries:
            for hook in entry.get("hooks", []):
                commands.append(hook.get("command", ""))
        self.assertTrue(
            any("inject-profile.sh" in cmd for cmd in commands),
            "SessionStart entry does not reference inject-profile.sh",
        )

    def test_stop_entry_exists(self):
        self.assertIn("Stop", self.hooks, "hooks.json missing Stop entry")

    def test_stop_references_update_script(self):
        entries = self.hooks["Stop"]
        commands = []
        for entry in entries:
            for hook in entry.get("hooks", []):
                commands.append(hook.get("command", ""))
        self.assertTrue(
            any("update-profile.py" in cmd for cmd in commands),
            "Stop entry does not reference update-profile.py",
        )

    def test_stop_hook_is_async(self):
        entries = self.hooks["Stop"]
        async_flags = []
        for entry in entries:
            for hook in entry.get("hooks", []):
                if "update-profile.py" in hook.get("command", ""):
                    async_flags.append(hook.get("async", False))
        self.assertTrue(
            any(async_flags),
            "Stop hook for update-profile.py should have async: true",
        )

    def test_pretooluse_entries_preserved(self):
        """Ensure existing PreToolUse entries are not removed (regression test)."""
        self.assertIn(
            "PreToolUse",
            self.hooks,
            "hooks.json missing PreToolUse — regression!",
        )
        entries = self.hooks["PreToolUse"]
        self.assertGreater(
            len(entries), 0, "PreToolUse has no entries — regression!"
        )


class TestProfileReviewSkill(unittest.TestCase):
    def test_skill_exists(self):
        self.assertTrue(
            PROFILE_REVIEW_SKILL.exists(),
            f"profile-review skill not found at {PROFILE_REVIEW_SKILL}",
        )

    def test_skill_has_frontmatter(self):
        content = PROFILE_REVIEW_SKILL.read_text(encoding="utf-8")
        self.assertTrue(
            content.startswith("---"),
            "SKILL.md missing YAML frontmatter",
        )
        self.assertIn("name:", content)
        self.assertIn("description:", content)

    def test_skill_contains_required_audit_sections(self):
        content = PROFILE_REVIEW_SKILL.read_text(encoding="utf-8")
        required = [
            "Audit Watch List",
            "Audit Active Tests",
            "Audit Decision Log",
        ]
        for section in required:
            with self.subTest(section=section):
                self.assertIn(
                    section,
                    content,
                    f"SKILL.md missing required section: {section}",
                )

    def test_skill_contains_validate_sections(self):
        content = PROFILE_REVIEW_SKILL.read_text(encoding="utf-8")
        self.assertIn("Validate Accounts", content)
        self.assertIn("Validate Targets", content)


if __name__ == "__main__":
    unittest.main()
