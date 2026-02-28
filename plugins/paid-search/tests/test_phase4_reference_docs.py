import unittest
from pathlib import Path


SKILLS_ROOT = Path("skills")


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class TestPhase4ReferenceMigrations(unittest.TestCase):
    def test_migrated_reference_files_exist(self):
        expected_paths = [
            SKILLS_ROOT / "platform-setup/references/config-patterns.md",
            SKILLS_ROOT / "platform-setup/references/google-shopping-campaigns.md",
            SKILLS_ROOT / "platform-setup/references/bing-campaign-management.md",
            SKILLS_ROOT / "platform-setup/references/bing-shopping-campaigns.md",
            SKILLS_ROOT / "platform-setup/references/bing-content-api.md",
            SKILLS_ROOT / "platform-setup/references/bing-bulk-operations.md",
            SKILLS_ROOT / "platform-setup/references/bing-reporting.md",
            SKILLS_ROOT / "morning-brief/references/google-reporting.md",
            SKILLS_ROOT / "waste-detector/references/google-campaign-management.md",
            SKILLS_ROOT / "search-term-verdict/references/google-campaign-management.md",
        ]
        missing = [str(path) for path in expected_paths if not path.exists()]
        self.assertEqual([], missing, f"Missing expected files: {missing}")

    def test_rewritten_references_remove_table_lib_patterns(self):
        import_keyword = "import " + ("pan" + "das")
        anomaly = _read(SKILLS_ROOT / "morning-brief/references/anomaly-formulas.md")
        pmax_queries = _read(SKILLS_ROOT / "pmax-decoder/references/gaql-queries.md")
        waste_queries = _read(SKILLS_ROOT / "waste-detector/references/gaql-queries.md")

        self.assertNotIn(import_keyword, anomaly)
        self.assertNotIn("DataFrame", anomaly)

        self.assertNotIn("iterrows(", pmax_queries)
        self.assertNotIn("concat(", pmax_queries)
        self.assertNotIn("nlargest(", pmax_queries)

        self.assertNotIn("groupby(", waste_queries)

    def test_phase4_docs_drop_script_path_coupling(self):
        legacy_skill_name = "ad-platform" + "-connection"
        docs = [
            SKILLS_ROOT / "morning-brief/references/anomaly-formulas.md",
            SKILLS_ROOT / "pmax-decoder/references/gaql-queries.md",
            SKILLS_ROOT / "waste-detector/references/gaql-queries.md",
            SKILLS_ROOT / "morning-brief/references/google-reporting.md",
            SKILLS_ROOT / "waste-detector/references/google-campaign-management.md",
            SKILLS_ROOT / "search-term-verdict/references/google-campaign-management.md",
        ]
        for path in docs:
            with self.subTest(path=str(path)):
                content = _read(path)
                self.assertNotIn(legacy_skill_name, content)
                self.assertNotIn("sys.path", content)


if __name__ == "__main__":
    unittest.main()
