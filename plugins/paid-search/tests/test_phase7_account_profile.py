import unittest
from pathlib import Path


PROFILE_TEMPLATE = Path(
    "skills/platform-setup/references/profile-template.md"
)
PLATFORM_SETUP_SKILL = Path("skills/platform-setup/SKILL.md")
GITIGNORE = Path(".gitignore")

ANALYSIS_SKILLS = [
    Path("skills/morning-brief/SKILL.md"),
    Path("skills/waste-detector/SKILL.md"),
    Path("skills/search-term-verdict/SKILL.md"),
    Path("skills/pmax-decoder/SKILL.md"),
]

MAINTENANCE_SKILLS = [
    Path("skills/morning-brief/SKILL.md"),
    Path("skills/waste-detector/SKILL.md"),
]

REQUIRED_PROFILE_SECTIONS = [
    "## Accounts",
    "## Targets",
    "## Active Tests",
    "## Watch List",
    "## Preferences",
    "## Decision Log",
]


class TestProfileTemplate(unittest.TestCase):
    def test_profile_template_exists(self):
        self.assertTrue(
            PROFILE_TEMPLATE.exists(),
            f"Profile template not found at {PROFILE_TEMPLATE}",
        )

    def test_profile_template_contains_required_sections(self):
        content = PROFILE_TEMPLATE.read_text(encoding="utf-8")
        for section in REQUIRED_PROFILE_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, content)


class TestPlatformSetupProfileGeneration(unittest.TestCase):
    def test_platform_setup_references_profile_generation(self):
        content = PLATFORM_SETUP_SKILL.read_text(encoding="utf-8")
        self.assertIn("profile-template.md", content)
        self.assertIn("profile/account-profile.md", content)


class TestAccountContextInAnalysisSkills(unittest.TestCase):
    def test_analysis_skills_contain_account_context(self):
        for skill_path in ANALYSIS_SKILLS:
            with self.subTest(skill=str(skill_path)):
                content = skill_path.read_text(encoding="utf-8")
                self.assertIn(
                    "## Account Context",
                    content,
                    f"{skill_path} missing Account Context section",
                )


class TestProfileMaintenanceInSkills(unittest.TestCase):
    def test_maintenance_skills_contain_profile_maintenance(self):
        for skill_path in MAINTENANCE_SKILLS:
            with self.subTest(skill=str(skill_path)):
                content = skill_path.read_text(encoding="utf-8")
                self.assertIn(
                    "## Profile Maintenance",
                    content,
                    f"{skill_path} missing Profile Maintenance section",
                )


class TestGitignoreProfile(unittest.TestCase):
    def test_gitignore_includes_profile(self):
        content = GITIGNORE.read_text(encoding="utf-8")
        self.assertIn("profile/", content)


if __name__ == "__main__":
    unittest.main()
