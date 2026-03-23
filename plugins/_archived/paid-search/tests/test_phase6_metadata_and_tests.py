import json
import unittest
from pathlib import Path


PLUGIN_JSON = Path(".claude-plugin/plugin.json")
README = Path("README.md")
HOOKS = Path("hooks/hooks.json")
GITIGNORE = Path(".gitignore")


class TestPhase6Metadata(unittest.TestCase):
    def test_plugin_json_version_and_description(self):
        data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
        self.assertEqual("7.0.0", data.get("version"))
        self.assertNotIn("Python scripts", data.get("description", ""))
        self.assertIn("MCP", data.get("description", ""))

    def test_readme_mcp_install_and_architecture(self):
        old_dependency_line = "pip" + " install " + "google-ads bingads " + ("pan" + "das")
        legacy_skill_name = "ad-platform" + "-connection"
        content = README.read_text(encoding="utf-8")
        self.assertIn("7.0.0", content)
        self.assertIn(".mcp.json", content)
        self.assertIn("platform-setup", content)
        self.assertNotIn(old_dependency_line, content)
        self.assertNotIn(legacy_skill_name, content)

    def test_readme_documents_bing(self):
        content = README.read_text(encoding="utf-8")
        self.assertIn("BING_ADS_DEVELOPER_TOKEN", content)
        self.assertIn("Bing Ads", content)
        self.assertIn("cross-platform", content.lower())

    def test_hooks_include_both_mutation_matchers(self):
        hooks_data = json.loads(HOOKS.read_text(encoding="utf-8"))
        pre_tool_use = hooks_data["hooks"]["PreToolUse"]
        matchers = [item.get("matcher") for item in pre_tool_use]
        self.assertIn("mcp__google-ads__mutate", matchers)
        self.assertIn("mcp__bing-ads__mutate", matchers)
        self.assertNotIn("Bash", matchers)

    def test_gitignore_drops_python_cache_patterns_and_mentions_mcp(self):
        content = GITIGNORE.read_text(encoding="utf-8")
        self.assertNotIn("__pycache__", content)
        self.assertNotIn("*.pyc", content)
        self.assertNotIn("*.pyo", content)
        self.assertIn(".mcp.json", content)


class TestPhase6TestsMigration(unittest.TestCase):
    def test_legacy_ad_platform_connection_tests_removed(self):
        legacy_tests = [
            Path("tests/test_ad_platform_connection.py"),
            Path("tests/test_ad_platform_connection_review_batch1.py"),
            Path("tests/test_ad_platform_connection_review_batch2.py"),
            Path("tests/test_ad_platform_connection_review_batch3.py"),
            Path("tests/test_ad_platform_connection_review_batch4.py"),
        ]
        existing = [str(path) for path in legacy_tests if path.exists()]
        self.assertEqual([], existing, f"Legacy tests should be removed: {existing}")


if __name__ == "__main__":
    unittest.main()
