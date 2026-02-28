import json
import unittest
from pathlib import Path


MCP_CONFIG_PATH = Path(".mcp.json")


class TestPhase1McpConfig(unittest.TestCase):
    def test_mcp_config_exists(self):
        self.assertTrue(
            MCP_CONFIG_PATH.exists(),
            "Phase 1 requires .mcp.json at plugin root",
        )

    def test_google_ads_server_present(self):
        config = json.loads(MCP_CONFIG_PATH.read_text(encoding="utf-8"))
        self.assertIn("google-ads", config)
        ga = config["google-ads"]
        self.assertEqual("npx", ga["command"])
        self.assertTrue(
            any("@channel47/google-ads-mcp" in arg for arg in ga["args"]),
            "Google Ads MCP package must be referenced in args",
        )
        required_env = [
            "GOOGLE_ADS_DEVELOPER_TOKEN",
            "GOOGLE_ADS_CLIENT_ID",
            "GOOGLE_ADS_CLIENT_SECRET",
            "GOOGLE_ADS_REFRESH_TOKEN",
            "GOOGLE_ADS_LOGIN_CUSTOMER_ID",
        ]
        for var in required_env:
            self.assertIn(var, ga["env"])

    def test_bing_ads_server_present(self):
        config = json.loads(MCP_CONFIG_PATH.read_text(encoding="utf-8"))
        self.assertIn("bing-ads", config)
        ba = config["bing-ads"]
        self.assertEqual("npx", ba["command"])
        self.assertTrue(
            any("@channel47/bing-ads-mcp" in arg for arg in ba["args"]),
            "Bing Ads MCP package must be referenced in args",
        )
        required_env = [
            "BING_ADS_DEVELOPER_TOKEN",
            "BING_ADS_CLIENT_ID",
            "BING_ADS_REFRESH_TOKEN",
            "BING_ADS_CUSTOMER_ID",
            "BING_ADS_ACCOUNT_ID",
        ]
        for var in required_env:
            self.assertIn(var, ba["env"])

    def test_no_at_latest_pinning(self):
        content = MCP_CONFIG_PATH.read_text(encoding="utf-8")
        self.assertNotIn(
            "@latest",
            content,
            "MCP packages should use semver pinning (e.g., @^1.0.0), not @latest",
        )


if __name__ == "__main__":
    unittest.main()
