import importlib.util
import inspect
import unittest
from pathlib import Path


SKILL_ROOT = Path("skills/ad-platform-connection")


def load_module(module_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Could not load module spec for {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestAdPlatformConnectionStructure(unittest.TestCase):
    def test_expected_files_exist(self):
        expected_files = [
            SKILL_ROOT / "SKILL.md",
            SKILL_ROOT / "scripts/google/auth.py",
            SKILL_ROOT / "scripts/google/report.py",
            SKILL_ROOT / "scripts/google/mutate.py",
            SKILL_ROOT / "scripts/bing/auth.py",
            SKILL_ROOT / "scripts/bing/report.py",
            SKILL_ROOT / "references/shared/config-patterns.md",
            SKILL_ROOT / "references/google/campaign-management.md",
            SKILL_ROOT / "references/google/shopping-campaigns.md",
            SKILL_ROOT / "references/google/reporting.md",
            SKILL_ROOT / "references/bing/campaign-management.md",
            SKILL_ROOT / "references/bing/shopping-campaigns.md",
            SKILL_ROOT / "references/bing/content-api.md",
            SKILL_ROOT / "references/bing/bulk-operations.md",
        ]
        missing = [str(path) for path in expected_files if not path.exists()]
        self.assertEqual([], missing, f"Missing expected files: {missing}")


class TestGoogleAuthScript(unittest.TestCase):
    def test_exports_required_functions(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/auth.py",
            "ad_platform_connection_google_auth",
        )
        for name in ("get_auth", "switch_customer", "verify_connection", "list_accounts"):
            self.assertTrue(hasattr(module, name), f"Missing export: {name}")


class TestGoogleReportScript(unittest.TestCase):
    def test_exports_required_functions(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/report.py",
            "ad_platform_connection_google_report",
        )
        for name in (
            "pull_report",
            "quick_campaign_summary",
            "quick_adgroup_summary",
            "quick_keyword_performance",
            "quick_search_terms",
            "quick_shopping_summary",
            "quick_wasted_spend",
        ):
            self.assertTrue(hasattr(module, name), f"Missing export: {name}")

    def test_date_clause_builder(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/report.py",
            "ad_platform_connection_google_report_dates",
        )
        self.assertEqual(
            "segments.date DURING LAST_30_DAYS",
            module._build_date_clause("LAST_30_DAYS"),
        )
        self.assertEqual(
            "segments.date BETWEEN '2026-01-01' AND '2026-01-31'",
            module._build_date_clause(("2026-01-01", "2026-01-31")),
        )
        self.assertEqual(
            "segments.date >= '2026-01-01'",
            module._build_date_clause(">= '2026-01-01'"),
        )


class TestGoogleMutateScript(unittest.TestCase):
    def test_exports_required_functions(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/mutate.py",
            "ad_platform_connection_google_mutate",
        )
        for name in (
            "execute_mutation",
            "create_campaign",
            "pause_entities",
            "add_negative_keywords",
            "create_rsa",
            "update_bids",
        ):
            self.assertTrue(hasattr(module, name), f"Missing export: {name}")

    def test_execute_mutation_is_dry_run_by_default(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/mutate.py",
            "ad_platform_connection_google_mutate_sig",
        )
        signature = inspect.signature(module.execute_mutation)
        self.assertTrue(signature.parameters["dry_run"].default)

    def test_entity_type_inference(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/mutate.py",
            "ad_platform_connection_google_mutate_infer",
        )
        self.assertEqual(
            "campaign",
            module.infer_entity_type("customers/1234567890/campaigns/111"),
        )
        self.assertEqual(
            "ad_group_ad",
            module.infer_entity_type("customers/1234567890/adGroupAds/111~222"),
        )
        self.assertEqual(
            "ad",
            module.infer_entity_type("customers/1234567890/ads/222"),
        )
        with self.assertRaises(ValueError):
            module.infer_entity_type("customers/1234567890/unknown/999")


if __name__ == "__main__":
    unittest.main()
