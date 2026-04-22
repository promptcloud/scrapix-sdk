# Contributing

Thanks for your interest in improving the Scrapix Python SDK.

## How this package is produced

The source tree shipped to PyPI is **auto-generated** from the Scrapix OpenAPI specification using [openapi-generator-cli](https://openapi-generator.tech/). The files in this directory are regenerated from scratch on every release — direct edits here will be overwritten on the next build.

## How to contribute

| What you'd like to change | Where it lives |
|---------------------------|----------------|
| A bug in a generated model, method, or HTTP behaviour | Upstream — open an issue at <https://github.com/promptcloud/scrapix-sdk/issues> with the endpoint, payload, and traceback. |
| The convenience helper (`create_client`) or the rendered README | Open a PR against the helper/template sources (we maintain them separately and re-apply on each release). |
| Missing endpoint, wrong field type, incorrect schema | Backend/spec fix — file an issue; we'll coordinate the spec update and roll it into the next SDK release. |

## Reporting issues

When filing a bug, please include:

- Package version (`pip show scrapix`)
- Python version (`python --version`)
- A minimal reproduction: the exact `ScrapeInput` / `CollectInput` / etc. you passed, and the full exception or response body you got back.

## Security

Do not report security issues on the public issue tracker. Email **security@promptcloud.com** instead.
