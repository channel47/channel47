import unittest
from pathlib import Path

LEGACY_SKILL_ROOT = Path("skills") / ("ad-platform" + "-connection")


class TestPhase5RemoveAdPlatformConnection(unittest.TestCase):
    def test_legacy_skill_directory_is_removed(self):
        self.assertFalse(
            LEGACY_SKILL_ROOT.exists(),
            "Phase 5 requires deleting the removed legacy skill directory entirely",
        )


if __name__ == "__main__":
    unittest.main()
