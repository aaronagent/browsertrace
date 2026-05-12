# PyPI Trusted Publishing

BrowserTrace should use PyPI Trusted Publishing instead of long-lived API
tokens. The GitHub workflow is `.github/workflows/publish.yml`.

## Current Status

As of 2026-05-10:

- PyPI returns HTTP 200 for `https://pypi.org/pypi/browsertrace/json`.
- The package is published at `https://pypi.org/project/browsertrace/`.
- Current PyPI version: `0.1.18`.
- The GitHub repository has a `pypi` environment.
- The `Publish` workflow succeeded on run `25630390661`.
- The `publish` job has `contents: read` and `id-token: write`, so it can
  download the built artifact and request the PyPI Trusted Publisher token.

## Owner Setup

Completed. The first trusted publish created the PyPI project through a pending
trusted publisher configured from the owner's PyPI account.

The trusted publisher was configured with these values:

| Field | Value |
|---|---|
| PyPI project | `browsertrace` |
| GitHub owner | `aaronlab` |
| GitHub repository | `browsertrace` |
| Workflow filename | `publish.yml` |
| Environment name | PyPI shows `(Any)` for the pending publisher used on first publish; the GitHub job itself still uses `environment: pypi` |

For future releases, review the project's `Publishing` page in PyPI and tighten
the publisher environment to `pypi` if PyPI allows editing the active publisher.

## GitHub Setup

The repository has a `pypi` environment. Review it in GitHub repository
settings before the first publish:

1. Open `Settings -> Environments`.
2. Open `pypi`.
3. Add a required reviewer if you want manual approval before publishing.

## Publish

To publish a future release after bumping the version and creating the GitHub
release artifacts:

```bash
gh workflow run Publish --repo aaronlab/browsertrace
```

The workflow is manual on purpose. It builds the wheel and sdist, then publishes
with OpenID Connect.

## Verify

```bash
python -m pip index versions browsertrace
pipx run --spec "browsertrace[ui]" browsertrace --help
```

After verification, update README install commands from GitHub URLs to:

```bash
pip install browsertrace
pip install "browsertrace[ui]"
```

## Small Docs Fixes

PyPI account-side trusted publishing setup is owner-only. For small docs fixes
around release or packaging notes, use the
[First PR Recipe](https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe)
to keep the first contribution small and reviewable.
