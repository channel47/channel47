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

        self.assertIn("allowed-tools: mcp__google-ads__list_accounts", skill_text)
        self.assertIn("mcp__google-ads__list_accounts", skill_text)
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
    def test_execution_skills_have_expected_allowed_tools(self):
        expected_allowed_tools = {
            "morning-brief": "mcp__google-ads__query, mcp__google-ads__list_accounts",
            "waste-detector": "mcp__google-ads__query, mcp__google-ads__mutate, mcp__google-ads__list_accounts",
            "search-term-verdict": "mcp__google-ads__query, mcp__google-ads__mutate, mcp__google-ads__list_accounts",
            "pmax-decoder": "mcp__google-ads__query, mcp__google-ads__mutate, mcp__google-ads__list_accounts",
        }

        for skill_name, allowed_tools in expected_allowed_tools.items():
            with self.subTest(skill=skill_name):
                skill_text = _read(SKILLS_ROOT / skill_name / "SKILL.md")
                self.assertIn(f"allowed-tools: {allowed_tools}", skill_text)

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
