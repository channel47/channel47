import importlib.util
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


class _FakeField:
    def __init__(self, name):
        self.name = name


class _FakeDescriptor:
    def __init__(self, names):
        self.fields = [_FakeField(name) for name in names]


class _FakeNestedResult:
    def __init__(self, resource_name):
        self.resource_name = resource_name


class _FakeMutationItem:
    DESCRIPTOR = _FakeDescriptor(["campaign_result", "ad_group_result"])

    def __init__(self, campaign_resource_name):
        self.campaign_result = _FakeNestedResult(campaign_resource_name)
        self.ad_group_result = None


class _FakeMutationResponse:
    def __init__(self, items):
        self.mutate_operation_responses = items
        self.partial_failure_error = None


class _FakeGoogleAdsServiceMutateOnly:
    def __init__(self):
        self.last_kwargs = None

    def Mutate(self, **kwargs):
        self.last_kwargs = kwargs
        return _FakeMutationResponse([])


class _FakeClientForMutate:
    def __init__(self, service):
        self._service = service

    def get_service(self, service_name):
        if service_name != "GoogleAdsService":
            raise AssertionError(f"Unexpected service request: {service_name}")
        return self._service

    def get_type(self, type_name):
        raise AssertionError(f"Unexpected get_type call: {type_name}")


class _FakeScope:
    def __init__(self):
        self.AccountIds = None
        self.Campaigns = {"unexpected": True}
        self.AdGroups = {"unexpected": True}


class TestCriticalReviewFixes(unittest.TestCase):
    def test_extract_mutation_result_reads_nested_oneof_resource_name(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/mutate.py",
            "ad_platform_connection_google_mutate_batch1_extract",
        )
        response = _FakeMutationResponse(
            [_FakeMutationItem("customers/123/campaigns/456")]
        )

        result = module._extract_mutation_result(response)

        self.assertEqual(
            [{"resource_name": "customers/123/campaigns/456"}],
            result["results"],
        )
        self.assertTrue(result["success"])
        self.assertEqual([], result["errors"])

    def test_execute_mutation_mutate_branch_does_not_build_request_wrapper(self):
        module = load_module(
            SKILL_ROOT / "scripts/google/mutate.py",
            "ad_platform_connection_google_mutate_batch1_mutate_branch",
        )
        fake_service = _FakeGoogleAdsServiceMutateOnly()
        client = _FakeClientForMutate(fake_service)

        operation_token = object()
        module.execute_mutation(
            client=client,
            customer_id="123-456-7890",
            operations=[operation_token],
            dry_run=False,
            partial_failure=False,
        )

        self.assertIsNotNone(fake_service.last_kwargs)
        self.assertEqual("1234567890", fake_service.last_kwargs["customer_id"])
        self.assertEqual([operation_token], fake_service.last_kwargs["mutate_operations"])
        self.assertFalse(fake_service.last_kwargs["partial_failure"])
        self.assertFalse(fake_service.last_kwargs["validate_only"])

    def test_bing_scope_helper_clears_campaigns_and_adgroups(self):
        module = load_module(
            SKILL_ROOT / "scripts/bing/report.py",
            "ad_platform_connection_bing_report_batch1_scope",
        )
        scope = _FakeScope()

        module._configure_report_scope(scope=scope, account_id="42")

        self.assertEqual({"long": [42]}, scope.AccountIds)
        self.assertIsNone(scope.Campaigns)
        self.assertIsNone(scope.AdGroups)

    def test_skill_interface_includes_platform_specific_examples(self):
        content = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("### Authentication - Google", content)
        self.assertIn("### Authentication - Bing", content)
        self.assertIn("auth_data, content_api_headers, config = get_auth()", content)
        self.assertIn("verify_connection(auth_data, config)", content)
        self.assertIn("### Reporting - Google", content)
        self.assertIn("### Reporting - Bing", content)
        self.assertIn("quick_campaign_summary(auth_data, account_id", content)


if __name__ == "__main__":
    unittest.main()
