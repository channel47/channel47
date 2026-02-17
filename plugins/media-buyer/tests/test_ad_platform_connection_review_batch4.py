import importlib.util
import json
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


class _FakeAuthorizationData:
    def __init__(self, account_id, customer_id, developer_token, authentication):
        self.account_id = account_id
        self.customer_id = customer_id
        self.developer_token = developer_token
        self.authentication = authentication


class _FakeOAuthDesktopMobileAuthCodeGrant:
    def __init__(self, client_id, env):
        self.client_id = client_id
        self.env = env
        self.oauth_tokens = types.SimpleNamespace(
            refresh_token="initial-refresh-token",
            access_token="access-token",
        )

    def request_oauth_tokens_by_refresh_token(self, refresh_token):
        self.oauth_tokens.refresh_token = refresh_token


class _FakeCredentialsRefreshError:
    refresh_token = "existing-token"

    def refresh(self, _request):
        raise RuntimeError("simulated network/auth failure")


class _FakeGoogleClientWithCredentials:
    def __init__(self):
        self._credentials = _FakeCredentialsRefreshError()


class _FakeNonProtoMutateResponseItem:
    pass


class _FakeMutateResponse:
    def __init__(self):
        self.mutate_operation_responses = [_FakeNonProtoMutateResponseItem()]
        self.partial_failure_error = None


class TestRoundTwoFollowUpFixes(unittest.TestCase):
    def test_bing_get_auth_builds_authorization_data_with_int_ids(self):
        module = load_module(
            SKILL_ROOT / "scripts/bing/auth.py",
            "ad_platform_connection_bing_auth_batch4_constructor_ints",
        )

        bingads_module = types.ModuleType("bingads")
        bingads_module.AuthorizationData = _FakeAuthorizationData
        bingads_module.ServiceClient = object

        bingads_auth_module = types.ModuleType("bingads.authorization")
        bingads_auth_module.OAuthDesktopMobileAuthCodeGrant = _FakeOAuthDesktopMobileAuthCodeGrant

        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "msads_config.json"
            config_path.write_text(
                json.dumps(
                    {
                        "client_id": "cid",
                        "developer_token": "dev-token",
                        "refresh_token": "initial-refresh-token",
                        "customer_id": "2002",
                        "account_id": "1001",
                    }
                ),
                encoding="utf-8",
            )

            with patch.dict(
                sys.modules,
                {"bingads": bingads_module, "bingads.authorization": bingads_auth_module},
            ):
                auth_data, _headers, _config = module.get_auth(config_path=config_path)

        self.assertIsInstance(auth_data.account_id, int)
        self.assertIsInstance(auth_data.customer_id, int)
        self.assertEqual(1001, auth_data.account_id)
        self.assertEqual(2002, auth_data.customer_id)

    def test_bing_switch_account_keeps_sdk_id_numeric(self):
        module = load_module(
            SKILL_ROOT / "scripts/bing/auth.py",
            "ad_platform_connection_bing_auth_batch4_switch_numeric",
        )
        auth_data = types.SimpleNamespace(account_id=111)
        config = {"account_id": "111"}

        updated_auth_data, updated_config = module.switch_account(
            auth_data=auth_data,
            config=config,
            new_account_id="222",
        )

        self.assertIs(updated_auth_data, auth_data)
        self.assertIsInstance(updated_auth_data.account_id, int)
        self.assertEqual(222, updated_auth_data.account_id)
        self.assertEqual("222", updated_config["account_id"])

    def test_google_token_rotation_tolerates_refresh_failures(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/auth.py",
            "ad_platform_connection_google_auth_batch4_refresh_errors",
        )
        client = _FakeGoogleClientWithCredentials()
        config = {"refresh_token": "existing-token"}
        config_path = Path("/tmp/test-google-ads-config-batch4.json")

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

        self.assertEqual("existing-token", config["refresh_token"])
        mock_save.assert_not_called()

    def test_bing_report_validates_iso_date_format(self):
        module = load_module(
            SKILL_ROOT / "scripts/bing/report.py",
            "ad_platform_connection_bing_report_batch4_date_validation",
        )

        with self.assertRaises(ValueError) as exc_info:
            module._parse_yyyy_mm_dd("2025/01/15", label="start_date")

        self.assertIn("start_date", str(exc_info.exception))
        self.assertIn("YYYY-MM-DD", str(exc_info.exception))

        with self.assertRaises(ValueError):
            module._parse_yyyy_mm_dd("2025-13-01", label="start_date")

    def test_mutation_result_fallback_logs_warning_for_non_proto_items(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/mutate.py",
            "ad_platform_connection_google_mutate_batch4_warning_fallback",
        )

        with self.assertLogs(module.LOGGER.name, level="WARNING") as logs:
            result = module._extract_mutation_result(_FakeMutateResponse())

        self.assertEqual([{"resource_name": None}], result["results"])
        self.assertTrue(
            any("DESCRIPTOR" in line for line in logs.output),
            msg=f"Expected warning mentioning DESCRIPTOR; got {logs.output!r}",
        )


if __name__ == "__main__":
    unittest.main()
