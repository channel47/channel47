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

    def test_google_ads_server_config_matches_plan(self):
        with MCP_CONFIG_PATH.open("r", encoding="utf-8") as handle:
            config = json.load(handle)

        self.assertEqual(
            {
                "google-ads": {
                    "command": "npx",
                    "args": ["-y", "@channel47/google-ads-mcp@latest"],
                    "env": {
                        "GOOGLE_ADS_DEVELOPER_TOKEN": "${GOOGLE_ADS_DEVELOPER_TOKEN}",
                        "GOOGLE_ADS_CLIENT_ID": "${GOOGLE_ADS_CLIENT_ID}",
                        "GOOGLE_ADS_CLIENT_SECRET": "${GOOGLE_ADS_CLIENT_SECRET}",
                        "GOOGLE_ADS_REFRESH_TOKEN": "${GOOGLE_ADS_REFRESH_TOKEN}",
                        "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "${GOOGLE_ADS_LOGIN_CUSTOMER_ID}",
                    },
                }
            },
            config,
        )


if __name__ == "__main__":
    unittest.main()
