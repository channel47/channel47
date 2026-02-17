# Ad Platform Connection Skill — Code Review

> **Spec:** `SPEC-ad-platform-connection.md` (v2)
> **Scope:** All 14 skill files + SKILL.md + plugin manifest
> **Structure compliance:** 100% — all spec files present, all function signatures match

---

## Review History

### Round 1 (2026-02-16) — 11 issues found

4 critical, 7 important. All were fixable in-place.

### Round 2 (2026-02-16) — All 11 fixed, 5 new issues found

All 11 original issues confirmed **FIXED**. Fixes introduced 5 new issues (1 critical, 2 important, 2 minor).

### Round 3 (2026-02-16) — All 5 fixed, 0 new issues

All 5 Round 2 issues confirmed **FIXED**. No new issues introduced. **Review complete.**

---

## Round 1 — Original Issues (all resolved)

| # | File | Severity | Issue | Status |
|---|------|----------|-------|--------|
| 1 | `google/mutate.py` | Critical | `_extract_mutation_result` oneof access — always returned None | FIXED |
| 2 | `google/mutate.py` | Critical | Fallback branch `client.get_type` crash | FIXED |
| 3 | `bing/report.py` | Critical | SUDS crash on 6/7 report types (`AdGroups` not nulled) | FIXED |
| 4 | `SKILL.md` | Critical | Interface pattern wrong for Bing (signatures mismatch) | FIXED |
| 5 | `google/report.py` | Important | Flattener `.name` check collapsed proto messages | FIXED |
| 6 | `google/report.py` | Important | `limit=100` silently capped all quick reports | FIXED |
| 7 | `google/auth.py` | Important | Token rotation was dead code (`oauth2_client`) | FIXED |
| 8 | `bing/auth.py` | Important | String passed where int expected in `verify_connection` | FIXED |
| 9 | `bing/report.py` | Important | `Last14Days` alias returned 28 days | FIXED |
| 10 | `bing/campaign-management.md` | Important | Broken cross-link path | FIXED |
| 11 | `google/auth.py` | Important | No permission enforcement on credential file | FIXED |
| 12 | `bing/report.py` | Minor | Dead imports (`time`, `csv`, `io`) | FIXED |
| 13 | `bing/{auth,report}.py` | Minor | Stale `exec(open(...))` docstrings | FIXED |
| 14 | `SKILL.md` | Minor | Bing reporting routed to wrong reference | FIXED |
| 15 | `google/mutate.py` | Minor | `_sanitize_customer_id` used for non-customer IDs | FIXED |

### Fix Quality Notes

- **Issue 1 fix** is more correct than the suggested approach — uses `DESCRIPTOR.fields` iteration with a safe fallback for non-proto objects.
- **Issue 2 fix** replaced the broken `get_type` branch with a `TypeError`-catching dict-based fallback. Clean.
- **Issue 3 fix** extracted a `_configure_report_scope` helper that conditionally nulls `AdGroups`. More robust than a one-line patch.
- **Issue 7 fix** reimplemented against `client._credentials` with an `ImportError` guard on the google-auth import. Good defensive addition.

---

## Round 2 — New Issues Introduced by Fixes (all resolved in Round 3)

### 1. `AuthorizationData` constructed with string IDs (Bing)

**File:** `scripts/bing/auth.py`, line 68
**Severity:** Critical — **FIXED**

The Round 1 fix for Issue 8 correctly cast `account_id` to `int` inside `verify_connection`, but the root cause was only partially addressed. The `AuthorizationData` object itself is still constructed with string values from JSON config:

```python
auth_data = AuthorizationData(
    account_id=config['account_id'],    # string from JSON
    customer_id=config['customer_id'],  # string from JSON
    developer_token=config['developer_token'],
    authentication=oauth
)
```

Every SDK service call made against this `auth_data` object passes string IDs where the SOAP layer expects `long` (int). `verify_connection` is now safe, but `report.py`'s `ReportingServiceManager` and any direct service calls from callers are still exposed.

**Fix:** Cast at the point of construction:

```python
auth_data = AuthorizationData(
    account_id=int(config['account_id']),
    customer_id=int(config['customer_id']),
    developer_token=config['developer_token'],
    authentication=oauth
)
```

---

### 2. `switch_account` re-introduces string type for `account_id`

**File:** `scripts/bing/auth.py`, lines 92-93
**Severity:** Important — **FIXED**

`switch_account` explicitly converts the new account ID to a string before assigning it to `auth_data.account_id`:

```python
auth_data.account_id = str(new_account_id)
config['account_id'] = str(new_account_id)
```

Even if Issue 1 above is fixed to cast at construction, any subsequent `switch_account` call re-introduces the string type on the live `auth_data` object.

**Fix:** Cast to int for the SDK object, keep string for config persistence:

```python
auth_data.account_id = int(new_account_id)
config['account_id'] = str(new_account_id)  # string in JSON config only
```

---

### 3. Token rotation can crash on network/auth errors

**File:** `scripts/google/auth.py`, lines 117-123
**Severity:** Important — **FIXED**

The reimplemented token rotation calls `credentials.refresh(request)` inside a `try` block that only catches `ImportError`. Any `google.auth.exceptions.RefreshError`, `TransportError`, or network timeout propagates uncaught and crashes the `get_auth()` call. The previous dead-code version at least couldn't crash at runtime.

**Fix:** Broaden the except clause:

```python
try:
    import google.auth.transport.requests as google_auth_requests
    request = google_auth_requests.Request()
    credentials.refresh(request)
except ImportError:
    return
except Exception:
    # Token rotation failed — non-fatal, continue with existing token
    return
```

---

### 4. Date parsing has no input validation (Bing)

**File:** `scripts/bing/report.py`, lines 127-136
**Severity:** Minor — **FIXED**

`start_date.split('-')` with direct index access (`parts[0]`, `parts[1]`, `parts[2]`) will raise unhandled `IndexError` or `ValueError` on malformed date strings (e.g., `'2025/01/15'`, `'Jan 15 2025'`). Since this is the public API surface for the plugin, a clear error message is warranted.

**Fix:** Add upfront validation:

```python
import re
_DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')

if start_date and not _DATE_RE.match(start_date):
    raise ValueError(f"start_date must be YYYY-MM-DD format, got: {start_date!r}")
```

---

### 5. `_extract_mutation_result` fallback still returns `None` for non-proto objects

**File:** `scripts/google/mutate.py`, lines 152-165
**Severity:** Minor — **FIXED**

The `DESCRIPTOR`-based iteration correctly handles protobuf responses. If `DESCRIPTOR` is absent (non-proto objects, mocks in tests), the code falls back to `getattr(item, "resource_name", None)` — the same path that was broken in Round 1. In production this fallback should never fire (the Google Ads SDK always returns protobufs), but in test environments it silently produces `None` results with no warning.

**Impact:** Low. Only affects test mocks, not production.

---

## Final Status

**All issues resolved.** Three rounds of review, 16 total issues found and fixed across 3 rounds. The ad-platform-connection skill is ready for use.
