# Custom GraphQL

When no pre-built query has the field combination you need, write your own. `sdk.graphql()` returns a client with managed auth and connection pooling; `execute()` accepts any valid query string.

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())
client = sdk.graphql()

# Request only the specific fields you need
response = client.execute(
    """
    query ($args: PaginatedVulnerabilitiesInput!) {
        vulnerabilities(args: $args) {
            edges {
                node {
                    id
                    cve
                    severity
                    cvssScore
                    correlations {
                        assetName
                        location
                    }
                }
            }
            pageInfo {
                endCursor
                hasNextPage
            }
        }
    }
    """,
    variables={
        "args": {
            "assetId": "abc123",
            "cursor": {"first": 50},
        }
    },
)
data = client.get_data(response)

for edge in data["vulnerabilities"]["edges"]:
    vuln = edge["node"]
    print(f"{vuln['cve']}  {vuln['severity']}  CVSS={vuln['cvssScore']}")
    for corr in vuln.get("correlations") or []:
        print(f"  also in: {corr['assetName']} at {corr['location']}")
```

## What to know

- **Responses are plain dicts**, not typed Pydantic models. You lose autocomplete and validation but gain full field-selection control.
- **Auth is still managed for you.** The `sdk.graphql()` client handles token refresh automatically.
- **Pagination is manual.** Check `pageInfo.hasNextPage` and pass `endCursor` yourself.
- **The schema is your reference.** The full GraphQL schema is bundled at `sdk-artifacts/schema.graphql`.
- **Input types still work.** Use the generated `input_types` module, then `.model_dump(by_alias=True)`:

```python
from netrise_turbine_sdk_graphql.input_types import PaginatedVulnerabilitiesInput, Cursor

args = PaginatedVulnerabilitiesInput(
    assetId="abc123",
    cursor=Cursor(first=50),
)
variables = {"args": args.model_dump(by_alias=True, exclude_unset=True)}
```

## Pagination

Include `pageInfo` in your selection and loop on `hasNextPage`:

```python
client = sdk.graphql()
cursor = None
all_vulns = []

while True:
    cursor_input = {"first": 100}
    if cursor:
        cursor_input["after"] = cursor

    data = client.get_data(client.execute(
        """
        query ($args: PaginatedVulnerabilitiesInput!) {
            vulnerabilities(args: $args) {
                edges { node { id, cve, severity, cvssScore } }
                pageInfo { endCursor, hasNextPage }
            }
        }
        """,
        variables={"args": {"assetId": "abc123", "cursor": cursor_input}},
    ))

    vulns = data["vulnerabilities"]
    for edge in vulns["edges"]:
        all_vulns.append(edge["node"])

    if not vulns["pageInfo"]["hasNextPage"]:
        break
    cursor = vulns["pageInfo"]["endCursor"]
```

## When to use each level

| | Lite iterators | Full iterators | Custom GraphQL |
| --- | --- | --- | --- |
| **Response type** | Typed Pydantic models | Typed Pydantic models | Plain dicts |
| **Pagination** | Automatic | Automatic | Manual |
| **Field selection** | Curated subset | Everything (depth 5) | You choose |
| **Best for** | Most workflows | Deep-dive analysis | Surgical queries, unique field combos |
