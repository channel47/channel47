import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch


SKILL_ROOT = Path("skills/ad-platform-connection")


def load_module(module_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Could not load module spec for {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestCleanupReviewFixes(unittest.TestCase):
    def test_bing_scripts_use_import_pattern_in_usage_docs(self):
        auth_content = (SKILL_ROOT / "scripts/bing/auth.py").read_text(encoding="utf-8")
        report_content = (SKILL_ROOT / "scripts/bing/report.py").read_text(encoding="utf-8")

        self.assertNotIn("exec(open(", auth_content)
        self.assertNotIn("exec(open(", report_content)
        self.assertIn("from scripts.bing.auth import get_auth", auth_content)
        self.assertIn("from scripts.bing.report import pull_report", report_content)

    def test_bing_report_removes_dead_imports(self):
        report_content = (SKILL_ROOT / "scripts/bing/report.py").read_text(encoding="utf-8")
        self.assertNotIn("import time", report_content)
        self.assertNotIn("import csv", report_content)
        self.assertNotIn("import io", report_content)

    def test_skill_routing_table_clarifies_bing_reporting_source(self):
        skill_content = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn(
            "| Reporting | `scripts/bing/report.py` (source of truth) | `scripts/bing/report.py` |",
            skill_content,
        )
        self.assertNotIn(
            "| Reporting | `references/bing/campaign-management.md` | `scripts/bing/report.py` |",
            skill_content,
        )

    def test_negative_keyword_parent_id_rejects_resource_names(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/mutate.py",
            "ad_platform_connection_google_mutate_batch3_parent_guard",
        )
        with patch.object(module, "execute_mutation", return_value={"success": True}):
            with self.assertRaises(ValueError):
                module.add_negative_keywords(
                    client=object(),
                    customer_id="1234567890",
                    keywords=["free"],
                    level="campaign",
                    parent_id="customers/1234567890/campaigns/999",
                    dry_run=True,
                )


if __name__ == "__main__":
    unittest.main()
