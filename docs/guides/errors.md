# Errors

Every SDK failure derives from `GraphQLClientError`; the types below are importable from `netrise_turbine_sdk`. Transient HTTP failures (429, 502, 503, 504) are retried automatically before raising. `str(exc)` includes the operation name, endpoint, and `x-request-id` when the server sent one — that is the string to put in a support ticket.

| Exception | Raised when | Useful attributes |
| --- | --- | --- |
| `GraphQLClientHttpError` | Non-2xx HTTP response after retries — bad credentials, missing permission, wrong endpoint, rate limit | `.status_code`, `.response` |
| `GraphQLClientGraphQLMultiError` | Server rejected the operation — unknown IDs, invalid arguments | `.errors` (list of GraphQL errors), `.operation_name`, `.data` |
| `pydantic.ValidationError` | An input model was built with missing or mistyped fields | `.errors()` |

A 2xx body that is not a GraphQL result (HTML login page, JSON missing both `data` and `errors`) raises `GraphQLClientInvalidResponseError` from `netrise_turbine_sdk_graphql.exceptions`. It has `.reason` (`not_json` or `missing_data_and_errors`) and still subclasses `GraphQLClientError`.

```python
from netrise_turbine_sdk import (
    GraphQLClientError,
    GraphQLClientGraphQLMultiError,
    GraphQLClientHttpError,
)

try:
    asset = sdk.get_asset("no-such-asset")
except GraphQLClientHttpError as exc:
    print(exc)                                   # auth / rate limit / transport
except GraphQLClientGraphQLMultiError as exc:
    print(exc)                                   # bad IDs, invalid arguments
except GraphQLClientError as exc:
    print(exc)                                   # catch-all base class
```
