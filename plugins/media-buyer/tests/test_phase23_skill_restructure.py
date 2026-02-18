import unittest
from pathlib import Path


SKILLS_ROOT = Path("skills")


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class TestPhase2PlatformSetupSkill(unittest.TestCase):
    def test_platform_setup_files_exist(self):
        expected_paths = [
            SKILLS_ROOT / "platform-setup/SKILL.md",
            SKILLS_ROOT / "platform-setup/references/google-setup.md",
            SKILLS_ROOT / "platform-setup/references/bing-setup.md",
            SKILLS_ROOT / "platform-setup/references/config-patterns.md",
        ]
        missing = [str(path) for path in expected_paths if not path.exists()]
        self.assertEqual([], missing, f"Missing expected files: {missing}")

    def test_platform_setup_has_mcp_verification_guidance(self):
        skill_text = _read(SKILLS_ROOT / "platform-setup/SKILL.md")

        self.assertIn("mcp__google-ads__list_accounts", skill_text)
        self.assertIn("mcp__bing-ads__list_accounts", skill_text)
        self.assertIn("connect to Google Ads", skill_text)
        self.assertIn("set up Bing", skill_text)
        self.assertIn("verify connection", skill_text)
        self.assertIn("configure my ad accounts", skill_text)

    def test_platform_setup_uses_env_var_based_configuration(self):
        config_patterns = _read(SKILLS_ROOT / "platform-setup/references/config-patterns.md")
        self.assertIn("GOOGLE_ADS_DEVELOPER_TOKEN", config_patterns)
        self.assertIn("GOOGLE_ADS_CLIENT_ID", config_patterns)
        self.assertIn("GOOGLE_ADS_CLIENT_SECRET", config_patterns)
        self.assertIn("GOOGLE_ADS_REFRESH_TOKEN", config_patterns)
        self.assertIn("GOOGLE_ADS_LOGIN_CUSTOMER_ID", config_patterns)


class TestPhase3ExecutionSkillsUseMcp(unittest.TestCase):
    def test_execution_skills_have_google_allowed_tools(self):
        """All execution skills must include Google Ads MCP tools."""
        google_tools = {
            "morning-brief": ["mcp__google-ads__query", "mcp__google-ads__list_accounts"],
            "waste-detector": ["mcp__google-ads__query", "mcp__google-ads__mutate", "mcp__google-ads__list_accounts"],
            "search-term-verdict": ["mcp__google-ads__query", "mcp__google-ads__mutate", "mcp__google-ads__list_accounts"],
            "pmax-decoder": ["mcp__google-ads__query", "mcp__google-ads__mutate", "mcp__google-ads__list_accounts"],
        }

        for skill_name, tools in google_tools.items():
            with self.subTest(skill=skill_name):
                skill_text = _read(SKILLS_ROOT / skill_name / "SKILL.md")
                for tool in tools:
                    self.assertIn(tool, skill_text, f"{skill_name} missing {tool}")

    def test_cross_platform_skills_have_bing_allowed_tools(self):
        """Cross-platform skills must include Bing Ads MCP tools."""
        bing_tools = {
            "morning-brief": ["mcp__bing-ads__report", "mcp__bing-ads__query", "mcp__bing-ads__list_accounts"],
            "waste-detector": ["mcp__bing-ads__report", "mcp__bing-ads__query", "mcp__bing-ads__list_accounts"],
            "search-term-verdict": ["mcp__bing-ads__report", "mcp__bing-ads__query", "mcp__bing-ads__list_accounts"],
        }

        for skill_name, tools in bing_tools.items():
            with self.subTest(skill=skill_name):
                skill_text = _read(SKILLS_ROOT / skill_name / "SKILL.md")
                for tool in tools:
                    self.assertIn(tool, skill_text, f"{skill_name} missing {tool}")

    def test_pmax_decoder_is_google_only(self):
        """PMax Decoder should NOT reference Bing tools (PMax is Google-only)."""
        skill_text = _read(SKILLS_ROOT / "pmax-decoder/SKILL.md")
        self.assertNotIn("mcp__bing-ads__", skill_text)

    def test_cross_platform_skills_have_bing_reference_docs(self):
        """Cross-platform skills must have bing-queries.md reference."""
        for skill_name in ("morning-brief", "waste-detector", "search-term-verdict"):
            with self.subTest(skill=skill_name):
                bing_ref = SKILLS_ROOT / skill_name / "references/bing-queries.md"
                self.assertTrue(bing_ref.exists(), f"{skill_name} missing bing-queries.md")

    def test_execution_skills_drop_python_foundation_dependency_pattern(self):
        legacy_skill_name = "ad-platform" + "-connection"
        table_lib_name = "pan" + "das"
        for skill_name in (
            "morning-brief",
            "waste-detector",
            "search-term-verdict",
            "pmax-decoder",
        ):
            with self.subTest(skill=skill_name):
                skill_text = _read(SKILLS_ROOT / skill_name / "SKILL.md")
                self.assertIn("## Data Access", skill_text)
                self.assertIn("mcp__google-ads__query", skill_text)
                self.assertNotIn("Foundation Dependency", skill_text)
                self.assertNotIn("sys.path", skill_text)
                self.assertNotIn(legacy_skill_name, skill_text)
                self.assertNotIn("pull_report(", skill_text)
                self.assertNotIn(table_lib_name, skill_text)
                self.assertNotIn("DataFrame", skill_text)


if __name__ == "__main__":
    unittest.main()
