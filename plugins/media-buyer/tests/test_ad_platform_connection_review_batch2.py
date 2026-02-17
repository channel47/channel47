import importlib.util
import inspect
import os
import stat
import sys
import tempfile
import types
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


class _FakeProtoMessage:
    name = "Campaign Alpha"

    def to_dict(self):
        return {"id": 123, "name": "Campaign Alpha", "status": "ENABLED"}


class _FakeCredentials:
    def __init__(self):
        self.refresh_token = "token-before"

    def refresh(self, _request):
        self.refresh_token = "token-after"


class _FakeGoogleClient:
    def __init__(self):
        self._credentials = _FakeCredentials()


class _FakeCustomerService:
    def __init__(self):
        self.last_account_id = None

    def GetAccount(self, AccountId):
        self.last_account_id = AccountId
        return types.SimpleNamespace(
            Name="Demo Account",
            Id=AccountId,
            AccountLifeCycleStatus="Active",
        )


class TestImportantReviewFixes(unittest.TestCase):
    def test_flatten_record_prefers_to_dict_over_name_attribute(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/report.py",
            "ad_platform_connection_google_report_batch2_flatten",
        )
        flattened = module._flatten_record(_FakeProtoMessage(), prefix="campaign")

        self.assertEqual(123, flattened["campaign.id"])
        self.assertEqual("Campaign Alpha", flattened["campaign.name"])
        self.assertEqual("ENABLED", flattened["campaign.status"])
        self.assertNotIn("campaign", flattened)

    def test_pull_report_default_limit_is_unbounded(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/report.py",
            "ad_platform_connection_google_report_batch2_limit",
        )
        signature = inspect.signature(module.pull_report)
        self.assertIsNone(signature.parameters["limit"].default)

    def test_google_token_rotation_uses_client_credentials_and_persists_updates(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/auth.py",
            "ad_platform_connection_google_auth_batch2_rotate",
        )
        client = _FakeGoogleClient()
        config = {"refresh_token": "token-before"}
        config_path = Path("/tmp/test-google-ads-config.json")

        google_mod = types.ModuleType("google")
        google_auth_mod = types.ModuleType("google.auth")
        google_transport_mod = types.ModuleType("google.auth.transport")
        google_requests_mod = types.ModuleType("google.auth.transport.requests")
        google_requests_mod.Request = lambda: object()
        google_transport_mod.requests = google_requests_mod
        google_auth_mod.transport = google_transport_mod
        google_mod.auth = google_auth_mod

        with patch.dict(
            sys.modules,
            {
                "google": google_mod,
                "google.auth": google_auth_mod,
                "google.auth.transport": google_transport_mod,
                "google.auth.transport.requests": google_requests_mod,
            },
        ):
            with patch.object(module, "_save_config") as mock_save:
                module._maybe_rotate_refresh_token(client, config, config_path)

        self.assertEqual("token-after", config["refresh_token"])
        mock_save.assert_called_once_with(config_path, config)

    def test_google_save_config_restricts_permissions_to_owner_only(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/auth.py",
            "ad_platform_connection_google_auth_batch2_permissions",
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "google_ads_config.json"
            old_umask = os.umask(0)
            try:
                module._save_config(
                    config_path,
                    {
                        "client_id": "id",
                        "client_secret": "secret",
                        "developer_token": "token",
                        "refresh_token": "refresh",
                    },
                )
            finally:
                os.umask(old_umask)

            mode = stat.S_IMODE(config_path.stat().st_mode)
            self.assertEqual(0o600, mode)

    def test_bing_verify_connection_casts_account_id_to_int(self):
        module = load_module(
            SKILL_ROOT / "scripts/bing/auth.py",
            "ad_platform_connection_bing_auth_batch2_account_cast",
        )
        fake_customer_service = _FakeCustomerService()
        bingads_mod = types.ModuleType("bingads")
        bingads_mod.ServiceClient = lambda **_kwargs: fake_customer_service

        with patch.dict(sys.modules, {"bingads": bingads_mod}):
            ok = module.verify_connection(
                auth_data=object(),
                config={"environment": "production", "account_id": "1001"},
            )

        self.assertTrue(ok)
        self.assertIsInstance(fake_customer_service.last_account_id, int)
        self.assertEqual(1001, fake_customer_service.last_account_id)

    def test_last14days_alias_is_not_silently_mapped(self):
        module = load_module(
            SKILL_ROOT / "scripts/bing/report.py",
            "ad_platform_connection_bing_report_batch2_alias",
        )
        self.assertEqual("Last14Days", module._normalize_time_period("Last14Days"))
        self.assertEqual("LastFourWeeks", module._normalize_time_period("Last30Days"))

    def test_bing_campaign_reference_links_to_bulk_operations_doc(self):
        content = (
            SKILL_ROOT / "references/bing/campaign-management.md"
        ).read_text(encoding="utf-8")
        self.assertIn("references/bing/bulk-operations.md", content)
        self.assertNotIn("references/bulk_operations.md", content)


if __name__ == "__main__":
    unittest.main()
