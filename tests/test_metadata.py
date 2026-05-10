"""Package metadata consistency tests."""

from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path

import browsertrace


def test_package_version_matches_module_version():
    project_root = Path(__file__).resolve().parents[1]
    pyproject = tomllib.loads((project_root / "pyproject.toml").read_text())

    assert pyproject["project"]["version"] == "0.1.15"
    assert pyproject["project"]["version"] == browsertrace.__version__


def test_public_docs_do_not_reference_stale_v011_release():
    project_root = Path(__file__).resolve().parents[1]
    public_docs = [
        project_root / "README.md",
        project_root / "LAUNCH.md",
        *sorted((project_root / "docs").rglob("*.md")),
        *sorted((project_root / "docs").rglob("*.html")),
        project_root / "docs" / "llms.txt",
    ]

    stale_release = re.compile(r"v0\.1\.1(?!\d)")
    stale_mentions = [
        str(path.relative_to(project_root))
        for path in public_docs
        if stale_release.search(path.read_text())
    ]

    assert stale_mentions == []


def test_pyproject_has_launch_discovery_metadata():
    project_root = Path(__file__).resolve().parents[1]
    pyproject = tomllib.loads((project_root / "pyproject.toml").read_text())
    project = pyproject["project"]

    keywords = set(project["keywords"])
    assert {
        "ai-agent-debugging",
        "browser-agent",
        "browser-agents",
        "computer-use",
        "llm-observability",
    } <= keywords

    classifiers = set(project["classifiers"])
    assert "Topic :: Scientific/Engineering :: Artificial Intelligence" in classifiers
    assert "Topic :: Software Development :: Testing" in classifiers

    urls = project["urls"]
    assert urls["Debugging Guide"] == "https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html"
    assert urls["Computer Use Guide"] == "https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html"
    assert urls["Browser Use Guide"] == "https://aaronlab.github.io/browsertrace/browser-use-debugging.html"
    assert urls["Changelog"] == "https://github.com/aaronlab/browsertrace/blob/main/CHANGELOG.md"
    assert urls["Roadmap"] == "https://github.com/aaronlab/browsertrace/blob/main/ROADMAP.md"
    assert urls["Discussions"] == "https://github.com/aaronlab/browsertrace/discussions/6"


def test_publish_workflow_is_ready_for_trusted_publishing():
    project_root = Path(__file__).resolve().parents[1]
    workflow = (project_root / ".github" / "workflows" / "publish.yml").read_text()

    assert "workflow_dispatch:" in workflow
    assert re.search(r"publish:\n(?: {4}.*\n)* {4}environment: pypi", workflow)
    assert re.search(
        r"publish:\n(?: {4}.*\n)* {4}permissions:\n"
        r"(?: {6}.*\n)* {6}contents: read\n"
        r"(?: {6}.*\n)* {6}id-token: write",
        workflow,
    )
    assert "pypa/gh-action-pypi-publish@release/v1" in workflow


def test_homepage_has_software_source_code_json_ld():
    project_root = Path(__file__).resolve().parents[1]
    homepage = (project_root / "docs" / "index.html").read_text()

    match = re.search(
        r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
        homepage,
        re.S,
    )

    assert match is not None
    metadata = json.loads(match.group(1))
    assert metadata["@context"] == "https://schema.org"
    assert metadata["@type"] == "SoftwareSourceCode"
    assert metadata["name"] == "BrowserTrace"
    assert metadata["codeRepository"] == "https://github.com/aaronlab/browsertrace"
    assert metadata["programmingLanguage"] == "Python"
    assert metadata["license"] == "https://opensource.org/license/mit"


def test_core_guides_have_tech_article_json_ld():
    project_root = Path(__file__).resolve().parents[1]
    guide_pages = [
        ("debug-browser-agent-failure.html", "How to debug an AI browser-agent failure"),
        ("browser-use-debugging.html", "Debug Browser Use failures with BrowserTrace"),
        ("stagehand-debugging.html", "Debug Stagehand runs with BrowserTrace"),
        ("skyvern-debugging.html", "Debug Skyvern task failures with BrowserTrace"),
        (
            "playwright-llm-debugging.html",
            "Debug Playwright + LLM browser-agent failures with BrowserTrace",
        ),
        (
            "computer-use-agent-debugging.html",
            "Debug custom computer-use agent failures with BrowserTrace",
        ),
    ]

    for filename, headline in guide_pages:
        page = (project_root / "docs" / filename).read_text()
        match = re.search(
            r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
            page,
            re.S,
        )

        assert match is not None, filename
        metadata = json.loads(match.group(1))
        assert metadata["@context"] == "https://schema.org", filename
        assert metadata["@type"] == "TechArticle", filename
        assert metadata["headline"] == headline, filename
        assert metadata["isPartOf"]["name"] == "BrowserTrace", filename
        assert metadata["codeRepository"] == "https://github.com/aaronlab/browsertrace", filename


def test_windows_powershell_first_run_docs_cover_env_vars():
    project_root = Path(__file__).resolve().parents[1]
    docs_text = "\n".join(
        [
            (project_root / "README.md").read_text(),
            (project_root / "examples" / "README.md").read_text(),
        ]
    )

    assert 'powershell' in docs_text.lower()
    assert '$env:BROWSERTRACE_HOME = "$env:TEMP\\browsertrace-demo"' in docs_text
    assert '$env:BROWSERTRACE_PORT = "4000"' in docs_text
    assert "BROWSERTRACE_HOME=/tmp/browsertrace-demo" in docs_text
    assert "BROWSERTRACE_PORT=4000 browsertrace" in docs_text


def test_examples_readme_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    examples = (project_root / "examples" / "README.md").read_text()

    assert "First PR Recipe" in examples
    assert "CONTRIBUTING.md#first-pr-recipe" in examples
    assert "first contribution small and reviewable" in examples
    assert "stars" not in examples.lower()
    assert "upvotes" not in examples.lower()
    assert "reposts" not in examples.lower()


def test_issue_chooser_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    config = (
        project_root / ".github" / "ISSUE_TEMPLATE" / "config.yml"
    ).read_text()

    assert "name: First PR Recipe" in config
    assert (
        "url: https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in config
    )
    assert "first contribution small and reviewable" in config
    assert "stars" not in config.lower()
    assert "upvotes" not in config.lower()
    assert "reposts" not in config.lower()


def test_issue_chooser_links_code_of_conduct_for_issue_expectations():
    project_root = Path(__file__).resolve().parents[1]
    config = (
        project_root / ".github" / "ISSUE_TEMPLATE" / "config.yml"
    ).read_text()

    assert "name: Code of Conduct" in config
    assert (
        "url: https://github.com/aaronlab/browsertrace/blob/main/CODE_OF_CONDUCT.md"
        in config
    )
    assert "constructive issues, discussions, reviews, and pull requests" in config


def test_issue_chooser_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    config = (
        project_root / ".github" / "ISSUE_TEMPLATE" / "config.yml"
    ).read_text()

    assert "name: Security Policy" in config
    assert (
        "url: https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md"
        in config
    )
    assert "sensitive issues" in config
    assert "private trace data" in config


def test_homepage_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    homepage = (project_root / "docs" / "index.html").read_text()

    assert "First PR Recipe" in homepage
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in homepage
    )
    assert "first contribution small and reviewable" in homepage
    assert "stars" not in homepage.lower()
    assert "upvotes" not in homepage.lower()
    assert "reposts" not in homepage.lower()


def test_homepage_names_current_adapter_surfaces():
    project_root = Path(__file__).resolve().parents[1]
    homepage = (project_root / "docs" / "index.html").read_text()

    assert "Browser Use run hooks" in homepage
    assert "Stagehand wrapper" in homepage
    assert "Skyvern task/workflow wrapper" in homepage


def test_integrations_page_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    integrations = (project_root / "docs" / "integrations.html").read_text()

    assert "First PR Recipe" in integrations
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in integrations
    )
    assert "first contribution small and reviewable" in integrations
    assert "stars" not in integrations.lower()
    assert "upvotes" not in integrations.lower()
    assert "reposts" not in integrations.lower()


def test_browser_use_guide_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    guide = (project_root / "docs" / "browser-use-debugging.html").read_text()

    assert "First PR Recipe" in guide
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in guide
    )
    assert "first contribution small and reviewable" in guide
    assert "stars" not in guide.lower()
    assert "upvotes" not in guide.lower()
    assert "reposts" not in guide.lower()


def test_stagehand_guide_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    guide = (project_root / "docs" / "stagehand-debugging.html").read_text()

    assert "First PR Recipe" in guide
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in guide
    )
    assert "first contribution small and reviewable" in guide
    assert "stars" not in guide.lower()
    assert "upvotes" not in guide.lower()
    assert "reposts" not in guide.lower()


def test_skyvern_guide_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    guide = (project_root / "docs" / "skyvern-debugging.html").read_text()

    assert "First PR Recipe" in guide
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in guide
    )
    assert "first contribution small and reviewable" in guide
    assert "stars" not in guide.lower()
    assert "upvotes" not in guide.lower()
    assert "reposts" not in guide.lower()


def test_playwright_llm_guide_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    guide = (project_root / "docs" / "playwright-llm-debugging.html").read_text()

    assert "First PR Recipe" in guide
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in guide
    )
    assert "first contribution small and reviewable" in guide
    assert "stars" not in guide.lower()
    assert "upvotes" not in guide.lower()
    assert "reposts" not in guide.lower()


def test_computer_use_guide_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    guide = (project_root / "docs" / "computer-use-agent-debugging.html").read_text()

    assert "First PR Recipe" in guide
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in guide
    )
    assert "first contribution small and reviewable" in guide
    assert "stars" not in guide.lower()
    assert "upvotes" not in guide.lower()
    assert "reposts" not in guide.lower()


def test_failure_walkthrough_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    guide = (project_root / "docs" / "debug-browser-agent-failure.html").read_text()

    assert "First PR Recipe" in guide
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in guide
    )
    assert "first contribution small and reviewable" in guide
    assert "stars" not in guide.lower()
    assert "upvotes" not in guide.lower()
    assert "reposts" not in guide.lower()


def test_comparison_page_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    page = (project_root / "docs" / "compare-browser-agent-debugging.html").read_text()

    assert "First PR Recipe" in page
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in page
    )
    assert "first contribution small and reviewable" in page
    assert "stars" not in page.lower()
    assert "upvotes" not in page.lower()
    assert "reposts" not in page.lower()


def test_trace_demo_page_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    page = (project_root / "docs" / "trace.html").read_text()

    assert "First PR Recipe" in page
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in page
    )
    assert "first contribution small and reviewable" in page
    assert "stars" not in page.lower()
    assert "upvotes" not in page.lower()
    assert "reposts" not in page.lower()


def test_launch_kit_page_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    page = (project_root / "docs" / "launch" / "index.html").read_text()

    assert "First PR Recipe" in page
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in page
    )
    assert "first contribution small and reviewable" in page
    assert "stars" not in page.lower()
    assert "upvotes" not in page.lower()
    assert "reposts" not in page.lower()


def test_docs_include_uvx_github_quickstart_before_pypi():
    project_root = Path(__file__).resolve().parents[1]
    docs_text = "\n".join(
        [
            (project_root / "README.md").read_text(),
            (project_root / "docs" / "llms.txt").read_text(),
        ]
    )

    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )
    assert f'uvx --from "{github_spec}" browsertrace demo' in docs_text
    assert f'uvx --from "{github_spec}" browsertrace list' in docs_text
    assert "before PyPI publishing is enabled" in docs_text


def test_owner_launch_checklists_include_doctor_fallback_before_pypi():
    project_root = Path(__file__).resolve().parents[1]
    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )

    for relpath in [
        "LAUNCH.md",
        "docs/launch/owner-next-actions.md",
        "docs/launch/owner-next-actions.zh-CN.md",
    ]:
        text = (project_root / relpath).read_text()
        assert f'uvx --from "{github_spec}" browsertrace doctor' in text, relpath
        assert f'uvx --from "{github_spec}" browsertrace demo' in text, relpath
        assert "pypi" in text.lower(), relpath


def test_pypi_publishing_notes_link_first_pr_recipe_for_small_docs_fixes():
    project_root = Path(__file__).resolve().parents[1]
    notes = (project_root / "docs" / "release" / "pypi-publishing.md").read_text()

    assert "First PR Recipe" in notes
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in notes
    )
    assert "first contribution small and reviewable" in notes
    assert "owner-only" in notes.lower()
    assert "stars" not in notes.lower()
    assert "upvotes" not in notes.lower()
    assert "reposts" not in notes.lower()


def test_changelog_links_first_pr_recipe_for_small_docs_fixes():
    project_root = Path(__file__).resolve().parents[1]
    changelog = (project_root / "CHANGELOG.md").read_text()

    assert "First PR Recipe" in changelog
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in changelog
    )
    assert "first contribution small and reviewable" in changelog
    assert "stars" not in changelog.lower()
    assert "upvotes" not in changelog.lower()
    assert "reposts" not in changelog.lower()


def test_code_of_conduct_links_first_pr_recipe_for_small_docs_fixes():
    project_root = Path(__file__).resolve().parents[1]
    code_of_conduct = (project_root / "CODE_OF_CONDUCT.md").read_text()

    assert "First PR Recipe" in code_of_conduct
    assert (
        "https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe"
        in code_of_conduct
    )
    assert "first contribution small and reviewable" in code_of_conduct
    assert "stars, upvotes, vote swaps" in code_of_conduct
    assert "fake engagement" in code_of_conduct


def test_github_profile_draft_links_current_trial_and_contribution_paths():
    project_root = Path(__file__).resolve().parents[1]
    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )
    profile_draft = (
        project_root / "docs" / "launch" / "github-profile-readme.md"
    ).read_text()

    assert "https://github.com/aaronlab/browsertrace" in profile_draft
    assert "https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html" in profile_draft
    assert f'uvx --from "{github_spec}" browsertrace doctor' in profile_draft
    assert f'uvx --from "{github_spec}" browsertrace demo' in profile_draft
    assert "Browser Use callback and run-hook tracing" in profile_draft
    assert "https://github.com/aaronlab/browsertrace/issues/3" in profile_draft
    assert "https://github.com/aaronlab/browsertrace/issues/225" in profile_draft
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in profile_draft
    assert "First PR Recipe" in profile_draft
    assert "CONTRIBUTING.md#first-pr-recipe" in profile_draft
    assert "first contribution small and reviewable" in profile_draft
    assert "stars" not in profile_draft.lower()
    assert "upvotes" not in profile_draft.lower()
    assert "reposts" not in profile_draft.lower()


def test_github_profile_draft_includes_json_cli_troubleshooting_note():
    project_root = Path(__file__).resolve().parents[1]
    profile_draft = (
        project_root / "docs" / "launch" / "github-profile-readme.md"
    ).read_text()
    assert "## Troubleshooting" in profile_draft
    note = profile_draft.split("## Troubleshooting", 1)[1].split(
        "## Current Focus", 1
    )[0]

    assert (
        "profile-reader follow-up, local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in note
    )
    assert "browsertrace doctor --json" in note
    assert "browsertrace list --status failed --json" in note
    assert "browsertrace show <run_id> --json" in note
    assert "debugging/workflow details" in note
    assert "stars" not in note.lower()
    assert "upvotes" not in note.lower()
    assert "reposts" not in note.lower()


def test_readme_has_public_safe_export_sharing_example():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "## Share A Public-Safe Trace" in readme
    assert "browsertrace demo" in readme
    assert "browsertrace list" in readme
    assert "browsertrace export <run_id> --public -o public.html" in readme
    assert "prompts/model I/O, screenshots, and URLs" in readme
    assert "hosted upload" in readme


def test_readme_has_browser_agent_feedback_checklist():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "## Report A Browser-Agent Failure" in readme
    assert "Browser Use, Stagehand, Skyvern, Playwright + LLM, or custom computer-use" in readme
    assert "agent framework" in readme
    assert "failure symptom" in readme
    assert "browsertrace show <run_id>" in readme
    assert "public-safe export" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_launch_discussion_near_feedback():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    feedback_section = readme.split("## Report A Browser-Agent Failure", 1)[1].split(
        "## Why not just use ___?", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/discussions/6" in feedback_section
    assert "browser-agent workflow feedback" in feedback_section
    assert "stars" not in feedback_section.lower()
    assert "upvotes" not in feedback_section.lower()
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_private_reports_near_feedback():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    feedback_section = readme.split("## Report A Browser-Agent Failure", 1)[1].split(
        "## Why not just use ___?", 1
    )[0]

    assert "[SECURITY.md](SECURITY.md)" in feedback_section
    assert "ordinary workflow feedback" in feedback_section
    assert "private or sensitive reports" in feedback_section
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_clarifies_cloud_features_are_not_required_for_local_oss():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    cloud_section = readme.split("## Cloud / Team (coming soon)", 1)[1].split(
        "## Roadmap", 1
    )[0]

    assert (
        "None of these hosted features are required for the current local OSS "
        "workflow"
    ) in cloud_section
    assert "Local BrowserTrace will always be free OSS" in cloud_section
    assert "open a cloud/team interest issue" in cloud_section
    assert "stars" not in cloud_section.lower()
    assert "upvotes" not in cloud_section.lower()


def test_roadmap_contribution_guidelines_link_first_pr_recipe():
    project_root = Path(__file__).resolve().parents[1]
    roadmap = (project_root / "ROADMAP.md").read_text()
    guidelines = roadmap.split("## Contribution Guidelines", 1)[1].split(
        "## Success Signals", 1
    )[0]

    assert "Good roadmap PRs are narrow and testable" in guidelines
    assert "CONTRIBUTING.md#first-pr-recipe" in guidelines
    assert "first contribution small and reviewable" in guidelines
    assert "stars" not in guidelines.lower()
    assert "upvotes" not in guidelines.lower()


def test_readme_links_contributor_guide_near_contributing():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    contributing_section = readme.split("## Contributing", 1)[1].split(
        "## License", 1
    )[0]

    assert "[CONTRIBUTING.md](CONTRIBUTING.md)" in contributing_section
    assert "small, issue-based contribution path" in contributing_section
    assert "First PR Recipe" in contributing_section
    assert "first contribution small and reviewable" in contributing_section
    assert "https://github.com/aaronlab/browsertrace/issues/225" in contributing_section
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in contributing_section
    assert "good first issue" in contributing_section
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_contributing_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    contributing_section = readme.split("## Contributing", 1)[1].split(
        "## License", 1
    )[0]

    assert "[SECURITY.md](SECURITY.md)" in contributing_section
    assert "security-sensitive reports" in contributing_section
    assert "private trace data" in contributing_section


def test_contributing_includes_json_cli_troubleshooting_checks():
    project_root = Path(__file__).resolve().parents[1]
    contributing = (project_root / "CONTRIBUTING.md").read_text()
    local_checks = contributing.split("## Useful Local Checks", 1)[1].split(
        "## Contribution Areas", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert "issue reports, CI, or AI/coding-agent troubleshooting" in local_checks
    assert recipe in local_checks
    assert "stars" not in local_checks.lower()
    assert "upvotes" not in local_checks.lower()


def test_contributing_includes_first_pr_recipe():
    project_root = Path(__file__).resolve().parents[1]
    contributing = (project_root / "CONTRIBUTING.md").read_text()
    assert "## First PR Recipe" in contributing
    recipe = contributing.split("## First PR Recipe", 1)[1].split(
        "## Useful Local Checks", 1
    )[0]

    assert "docs fix or small example" in recipe
    assert "Comment on the good first issue" in recipe
    assert "https://github.com/aaronlab/browsertrace/issues/225" in recipe
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in recipe
    assert "Create a branch" in recipe
    assert "uv run --python 3.11 --extra dev pytest -q" in recipe
    assert "Fixes #<issue>" in recipe
    assert "small enough to review in one pass" in recipe
    assert "stars" not in recipe.lower()
    assert "upvotes" not in recipe.lower()
    assert "reposts" not in recipe.lower()


def test_contributing_sets_good_first_issue_claim_window():
    project_root = Path(__file__).resolve().parents[1]
    contributing = (project_root / "CONTRIBUTING.md").read_text()
    recipe = contributing.split("## First PR Recipe", 1)[1].split(
        "## Useful Local Checks", 1
    )[0]

    assert "active claim" in recipe
    assert "short claim window" in recipe
    assert "before maintainers take the same issue directly" in recipe


def test_first_pr_recipe_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    contributing = (project_root / "CONTRIBUTING.md").read_text()
    recipe = contributing.split("## First PR Recipe", 1)[1].split(
        "## Useful Local Checks", 1
    )[0]

    assert "[SECURITY.md](SECURITY.md)" in recipe
    assert "security-sensitive reports" in recipe
    assert "private trace data" in recipe


def test_readme_links_code_of_conduct_near_contributing():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    contributing_section = readme.split("## Contributing", 1)[1].split(
        "## License", 1
    )[0]

    assert "[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)" in contributing_section
    assert "concise contributor expectations" in contributing_section
    assert "welcoming baseline" in contributing_section
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_issue_template_chooser_near_contributing():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    contributing_section = readme.split("## Contributing", 1)[1].split(
        "## License", 1
    )[0]

    assert (
        "https://github.com/aaronlab/browsertrace/issues/new/choose"
        in contributing_section
    )
    assert "bug, feature, integration, or cloud/team template" in contributing_section
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_pull_request_template_near_contributing():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    contributing_section = readme.split("## Contributing", 1)[1].split(
        "## License", 1
    )[0]

    assert (
        "[pull request template](.github/PULL_REQUEST_TEMPLATE.md)"
        in contributing_section
    )
    assert "linked issue and test commands" in contributing_section
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_release_notes_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "https://github.com/aaronlab/browsertrace/releases/tag/v0.1.15"
        in install_section
    )
    assert "v0.1.15 release notes" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_release_notes_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "https://github.com/aaronlab/browsertrace/releases/tag/v0.1.15"
        in install_section
    )
    assert (
        "The v0.1.15 release notes summarize what changed in the pinned "
        "GitHub tag"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_links_pypi_tracking_issue_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/5" in install_section
    assert "PyPI tracking issue" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_pypi_tracking_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/5" in install_section
    assert (
        "The PyPI tracking issue is the source for publishing status while "
        "install commands stay pinned to the GitHub tag"
    ) in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_uvx_trial_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`uvx` is the no-install trial path, and pinned GitHub-tag "
        "`pip install` is the persistent install path"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_ui_extra_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`[ui]` is needed for the local web UI, while SDK-only install is enough "
        "for trace capture integrations"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_sdk_only_terminal_commands_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "SDK-only install can still use terminal commands like `browsertrace list`, "
        "`browsertrace show`, and `browsertrace export`; `[ui]` is only needed "
        "for the local web UI"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_mentions_python_version_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "Requires Python 3.11+" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_python_version_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "The pinned GitHub-tag install path requires Python 3.11+"
        in install_section
    )
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_links_first_run_troubleshooting_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "examples/#first-run-troubleshooting-checklist" in install_section
    assert "first-run troubleshooting checklist" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_first_run_troubleshooting_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "examples/#first-run-troubleshooting-checklist" in install_section
    assert "first-run troubleshooting checklist walks through" in install_section
    for command in [
        "`browsertrace doctor`",
        "`browsertrace demo`",
        "`browsertrace list`",
        "`browsertrace show`",
        "public-safe export",
    ]:
        assert command in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_links_static_demo_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "https://aaronlab.github.io/browsertrace/" in install_section
    assert (
        "https://github.com/aaronlab/browsertrace/releases/download/v0.1.15/"
        "browsertrace-demo-public.html"
    ) in install_section
    assert (
        "The live static demo and public-safe demo export let you inspect a trace "
        "before installing anything"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_links_command_cheat_sheet_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "examples/#browsertrace-command-cheat-sheet" in install_section
    assert "The command cheat sheet summarizes" in install_section
    for command in [
        "`browsertrace doctor`",
        "`browsertrace demo`",
        "`browsertrace list`",
        "`browsertrace show`",
        "public-safe export commands",
    ]:
        assert command in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_doctor_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "`browsertrace doctor` is a safe local status check" in install_section
    assert "install and trace-store status" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_links_healthy_doctor_output_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "examples/#check-a-healthy-local-install" in install_section
    assert "healthy doctor output recipe shows expected" in install_section
    for status_line in ["`Home:`", "`Database:`", "`Runs:`", "`UI dependencies:`"]:
        assert status_line in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_list_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "`browsertrace list` shows demo run IDs" in install_section
    assert "`browsertrace demo`" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_list_output_fields_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`browsertrace list` shows run IDs with timestamps and status"
    ) in install_section
    assert "`browsertrace demo`" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_list_json_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "`browsertrace list --json` prints recent runs as JSON" in install_section
    assert "id, name, status, and created timestamp" in install_section
    assert "`browsertrace list` shows run IDs with timestamps and status" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_list_status_filter_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "`browsertrace list --status failed` filters recent runs by status" in install_section
    assert "`browsertrace list --status completed --json`" in install_section
    assert "`browsertrace list --json`" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_includes_json_cli_automation_recipe_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert "For scripts, CI, or AI/coding-agent troubleshooting" in install_section
    assert recipe in install_section
    assert "hosted sharing" not in readme


def test_readme_links_llms_troubleshooting_context_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "[`docs/llms.txt`](docs/llms.txt)" in install_section
    assert "AI/coding-agent troubleshooting context" in install_section
    assert "JSON CLI checks" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_demo_run_id_output_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`browsertrace demo` prints a `Run ID:` line you can copy into "
        "`browsertrace show` or `browsertrace export`"
    ) in install_section
    assert "`browsertrace list` shows demo run IDs" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_demo_needs_no_api_keys_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "`browsertrace demo` runs without API keys or external services" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_no_api_demo_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "The deterministic no-API demo creates a trace without a browser, "
        "network, or API key"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_no_signup_trial_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "The local trial requires no signup, cloud account, or hosted browser "
        "service"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_links_first_run_feedback_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "First-run feedback after `browsertrace demo`" in install_section
    assert "https://github.com/aaronlab/browsertrace/issues/3" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_links_launch_discussion_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "Workflow discussion after `browsertrace demo`" in install_section
    assert "https://github.com/aaronlab/browsertrace/discussions/6" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_links_example_matrix_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "examples/#example-matrix" in install_section
    assert "choose another runnable demo after `browsertrace demo`" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_no_service_examples_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "The example matrix lists no-service examples" in install_section
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_links_recent_runs_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "examples/#show-only-recent-runs" in install_section
    assert "`browsertrace list --limit 5` narrows recent runs" in install_section
    assert "before choosing one to inspect or export" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_links_run_id_prefix_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "examples/#run-id-prefixes-for-export" in install_section
    assert "A longer run ID prefix fixes ambiguous" in install_section
    assert "`browsertrace show` or `browsertrace export` matches" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_show_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "`browsertrace show <run_id>` inspects a listed run" in install_section
    assert "from the terminal" in install_section
    assert "action labels, status, and errors" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_show_json_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "`browsertrace show <run_id> --json` prints one run as JSON" in install_section
    assert "run details and step actions" in install_section
    assert "`browsertrace list --json`" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_public_safe_export_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`browsertrace export <run_id> --public -o public.html` creates a "
        "public-safe HTML export"
    ) in install_section
    assert "from a listed run" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_public_safe_export_privacy_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "Public-safe export omits model I/O, screenshots, and URLs" in install_section
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_redact_export_distinction_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`--redact` only omits model I/O, while `--public` also omits "
        "screenshots and URLs"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_self_contained_export_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`browsertrace export <run_id> --public -o public.html` writes a "
        "self-contained HTML report you can attach to a bug report or issue"
    ) in install_section
    assert "Public-safe export omits model I/O, screenshots, and URLs" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_export_output_path_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`-o public.html` chooses the export filename; without `-o`, "
        "`browsertrace export` writes `<run_id>.html`"
    ) in install_section
    assert "`browsertrace export <run_id> --public -o public.html`" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_export_success_output_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`browsertrace export` prints `Wrote <path>` after writing the HTML file"
    ) in install_section
    assert "`browsertrace export <run_id> --public -o public.html`" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_port_override_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`BROWSERTRACE_PORT=3001 browsertrace` starts the local UI on another port"
        in install_section
    )
    assert "when 3000 is busy" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_localhost_ui_binding_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "The local UI binds to `127.0.0.1` by default; `BROWSERTRACE_PORT` "
        "changes only the port"
    ) in install_section
    assert "http://127.0.0.1:3000" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_local_ui_url_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "After `browsertrace` starts the local UI, open "
        "`http://127.0.0.1:3000` and inspect the demo run"
    ) in install_section
    assert (
        "`browsertrace` prints `BrowserTrace UI: http://127.0.0.1:<port>` "
        "when the local server starts"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_demo_run_title_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "The demo run is named `demo: checkout agent fails on disabled button` "
        "in the local UI"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_isolated_trace_storage_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`BROWSERTRACE_HOME=/tmp/browsertrace-demo browsertrace demo` writes "
        "demo traces to an isolated trace store"
    ) in install_section
    assert (
        "By default, BrowserTrace stores local traces under `~/.browsertrace/`; "
        "set `BROWSERTRACE_HOME` to use an isolated trace store"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_windows_trace_home_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        'Windows PowerShell users can set `$env:BROWSERTRACE_HOME = '
        '"$env:TEMP\\browsertrace-demo"` before running BrowserTrace commands'
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "PyPI publishing is not enabled yet" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_cli_help_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "`browsertrace --help` lists local CLI commands and options" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_explains_export_help_near_install_tag():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert (
        "`browsertrace export --help` lists export options before creating a "
        "public-safe HTML report"
    ) in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_groups_install_tips_as_compact_list():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "Useful local checks:" in install_section
    for tip in [
        "- `browsertrace doctor` is a safe local status check",
        "- `browsertrace doctor --json` prints install and trace-store status as JSON",
        "- The healthy doctor output recipe shows expected `Home:`, `Database:`, `Runs:`, and `UI dependencies:` status lines",
        "- `browsertrace demo` runs without API keys or external services",
        "- After `browsertrace demo`, `browsertrace list` shows demo run IDs",
        "- `browsertrace list` shows run IDs with timestamps and status",
        "- `browsertrace list --json` prints recent runs as JSON",
        "- `browsertrace list --status failed` filters recent runs by status",
        "- `browsertrace demo` prints a `Run ID:` line",
        "- The first-run troubleshooting checklist walks through `browsertrace doctor`, `browsertrace demo`, `browsertrace list`, `browsertrace show`, and public-safe export",
        "- The live static demo and public-safe demo export let you inspect a trace before installing anything",
        "- The command cheat sheet summarizes `browsertrace doctor`, `browsertrace demo`, `browsertrace list`, `browsertrace show`, and public-safe export commands",
        "- The v0.1.15 release notes summarize what changed in the pinned GitHub tag",
        "- The PyPI tracking issue is the source for publishing status while install commands stay pinned to the GitHub tag",
        "- `uvx` is the no-install trial path, and pinned GitHub-tag `pip install` is the persistent install path",
        "- `[ui]` is needed for the local web UI, while SDK-only install is enough for trace capture integrations",
        "- SDK-only install can still use terminal commands like `browsertrace list`, `browsertrace show`, and `browsertrace export`",
        "- The pinned GitHub-tag install path requires Python 3.11+",
        "- The deterministic no-API demo creates a trace without a browser, network, or API key",
        "- The local trial requires no signup, cloud account, or hosted browser service",
        "- First-run feedback after `browsertrace demo`: https://github.com/aaronlab/browsertrace/issues/3",
        "- Workflow discussion after `browsertrace demo`: https://github.com/aaronlab/browsertrace/discussions/6",
        "- Use the [example matrix](examples/#example-matrix) to choose another runnable demo after `browsertrace demo`",
        "- The example matrix lists no-service examples",
        "- `browsertrace list --limit 5` narrows recent runs before choosing one to inspect or export",
        "- A longer run ID prefix fixes ambiguous `browsertrace show` or `browsertrace export` matches",
        "- `browsertrace show <run_id>` inspects a listed run",
        "- `browsertrace show <run_id>` prints the selected run's step timeline, including action labels, status, and errors",
        "- `browsertrace show <run_id> --json` prints one run as JSON",
        "- `browsertrace export <run_id> --public -o public.html` creates a public-safe HTML export",
        "- `browsertrace export <run_id> --public -o public.html` writes a self-contained HTML report",
        "- `-o public.html` chooses the export filename",
        "- `browsertrace export` prints `Wrote <path>`",
        "- Public-safe export omits model I/O, screenshots, and URLs",
        "- `--redact` only omits model I/O, while `--public` also omits screenshots and URLs",
        "- `BROWSERTRACE_PORT=3001 browsertrace` starts the local UI on another port",
        "- The local UI binds to `127.0.0.1` by default",
        "- After `browsertrace` starts the local UI, open `http://127.0.0.1:3000` and inspect the demo run",
        "- `browsertrace` prints `BrowserTrace UI: http://127.0.0.1:<port>` when the local server starts",
        "- The demo run is named `demo: checkout agent fails on disabled button` in the local UI",
        "- `BROWSERTRACE_HOME=/tmp/browsertrace-demo browsertrace demo` writes demo traces to an isolated trace store",
        "- By default, BrowserTrace stores local traces under `~/.browsertrace/`; set `BROWSERTRACE_HOME` to use an isolated trace store",
        '- Windows PowerShell users can set `$env:BROWSERTRACE_HOME = "$env:TEMP\\browsertrace-demo"` before running BrowserTrace commands',
        "- `browsertrace --help` lists local CLI commands and options",
        "- `browsertrace export --help` lists export options before creating a public-safe HTML report",
    ]:
        assert tip in install_section

    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_readme_links_browser_use_debugging_guide():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "https://aaronlab.github.io/browsertrace/browser-use-debugging.html" in readme
    assert "Browser Use callback compatibility" in readme
    assert "register_new_step_callback" in readme
    assert "create_run_hooks" in readme
    assert "agent.run(on_step_start=hooks.on_step_start" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_stagehand_debugging_guide():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "https://aaronlab.github.io/browsertrace/stagehand-debugging.html" in readme
    assert "Stagehand `act` and `extract` debugging" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_skyvern_debugging_guide():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "https://aaronlab.github.io/browsertrace/skyvern-debugging.html" in readme
    assert "Skyvern task and workflow debugging" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_playwright_llm_debugging_guide():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html" in readme
    assert "prompt, DOM, selector, retry, and error fields" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_integrations_overview():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "https://aaronlab.github.io/browsertrace/integrations.html" in readme
    assert "Browser Use, Stagehand, Skyvern, and Playwright guide paths" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_adapter_request_near_integrations():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert (
        "https://github.com/aaronlab/browsertrace/issues/new?template=integration_request.yml"
        in readme
    )
    assert "Browser Use, Stagehand, Skyvern, or Playwright adapter requests" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_comparison_guide_with_named_text():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert (
        "[browser-agent debugging comparison](https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html)"
        in readme
    )
    assert "LLM tracing" in readme
    assert "hosted browser/runtime tools" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_llms_txt_for_ai_coding_agents():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "docs/llms.txt" in readme
    assert "AI/coding agents" in readme
    assert "concise project context" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_examples_command_cheat_sheet():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#browsertrace-command-cheat-sheet" in readme
    assert "command cheat sheet" in readme
    assert "browsertrace doctor" in readme
    assert "browsertrace demo" in readme
    assert "browsertrace list" in readme
    assert "browsertrace show" in readme
    assert "public-safe export" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_example_matrix():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#example-matrix" in readme
    assert "no-service examples" in readme
    assert "commands" in readme
    assert "runnable demo" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_first_run_troubleshooting_checklist():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#first-run-troubleshooting-checklist" in readme
    assert "first-run troubleshooting checklist" in readme
    assert "browsertrace doctor" in readme
    assert "browsertrace demo" in readme
    assert "browsertrace list" in readme
    assert "browsertrace show" in readme
    assert "public-safe export" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_doctor_output_example():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#check-a-healthy-local-install" in readme
    assert "healthy `browsertrace doctor` output" in readme
    assert "Home:" in readme
    assert "Database:" in readme
    assert "Runs:" in readme
    assert "UI dependencies:" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_public_safe_attachment_note():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#attach-a-public-safe-export-to-an-issue" in readme
    assert "public-safe export" in readme
    assert "omits prompt/model I/O, screenshots, and URLs" in readme
    assert "GitHub issue or PR comment" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_share_safe_export_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#creating-a-share-safe-export" in readme
    assert "browsertrace export <run_id> --public -o public.html" in readme
    assert "omits prompt/model I/O, screenshots, and URLs" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_github_actions_public_export_artifact_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#github-actions-artifact-for-public-safe-exports" in readme
    assert "GitHub Actions artifact" in readme
    assert "public.html" in readme
    assert "BrowserTrace does not upload traces by itself" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_gitlab_ci_public_export_artifact_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#gitlab-ci-artifact-for-public-safe-exports" in readme
    assert "GitLab CI artifact" in readme
    assert "public.html" in readme
    assert "BrowserTrace does not upload traces by itself" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_isolated_trace_storage_testing_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#testing-with-isolated-trace-storage" in readme
    assert "isolated trace storage" in readme
    assert "BROWSERTRACE_HOME" in readme
    assert "temp directory" in readme
    assert "pytest" in readme
    assert "no browser, network, or API key" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_trace_storage_location_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#where-traces-are-stored" in readme
    assert "~/.browsertrace/" in readme
    assert "BROWSERTRACE_HOME" in readme
    assert "local traces" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_playwright_sync_snapshot_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#playwright-sync-api-snapshot" in readme
    assert "snapshot_sync" in readme
    assert "sync Playwright" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_environment_variable_quick_reference():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#environment-variable-quick-reference" in readme
    assert "environment variable quick reference" in readme
    assert "BROWSERTRACE_HOME" in readme
    assert "BROWSERTRACE_PORT" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_cli_help_discovery_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#discover-cli-options" in readme
    assert "CLI help" in readme
    assert "browsertrace --help" in readme
    assert "browsertrace export --help" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_run_id_prefix_troubleshooting_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#run-id-prefixes-for-export" in readme
    assert "run ID prefix" in readme
    assert "browsertrace export <run_id>" in readme
    assert "longer unique prefix" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_failed_run_terminal_inspection_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#inspect-a-failed-run-in-the-terminal" in readme
    assert "failed step timeline" in readme
    assert "browsertrace show <run_id>" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_recent_runs_list_limit_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#show-only-recent-runs" in readme
    assert "recent runs" in readme
    assert "browsertrace list --limit 5" in readme
    assert "inspect or export" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_demo_run_lookup_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#finding-your-demo-run" in readme
    assert "browsertrace list" in readme
    assert "run IDs" in readme
    assert "timestamps" in readme
    assert "status" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_readme_links_port_already_in_use_recipe():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()

    assert "examples/#port-already-in-use" in readme
    assert "port already in use" in readme
    assert "local UI port" in readme
    assert "BROWSERTRACE_PORT" in readme
    assert "@v0.1.15" in readme
    assert "hosted sharing" not in readme


def test_examples_readme_includes_windows_public_safe_export_flow():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "## Public Export Flow" in examples_readme
    assert (
        "```powershell\n"
        "browsertrace demo\n"
        "browsertrace list\n"
        "browsertrace export <run_id> --public -o public.html\n"
        "```"
    ) in examples_readme
    assert "`--public` omits prompts/model I/O, screenshots, and URLs" in examples_readme
    assert "BrowserTrace does not upload" in examples_readme


def test_examples_readme_includes_export_run_id_prefix_troubleshooting():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### Run ID Prefixes For Export" in examples_readme
    assert "browsertrace list" in examples_readme
    assert "browsertrace export <run_id> --public -o public.html" in examples_readme
    assert "unique prefix" in examples_readme
    assert "copy more characters" in examples_readme
    assert "hosted sharing" not in examples_readme


def test_examples_readme_includes_browsertrace_show_failed_run_recipe():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### Inspect a failed run in the terminal" in examples_readme
    assert "browsertrace show <run_id>" in examples_readme
    assert "browsertrace list" in examples_readme
    assert "browsertrace export <run_id> --public -o public.html" in examples_readme
    assert "failed step" in examples_readme


def test_examples_readme_includes_list_limit_recent_runs_recipe():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### Show only recent runs" in examples_readme
    assert "browsertrace list --limit 5" in examples_readme
    assert "most recent runs" in examples_readme
    assert "browsertrace show <run_id>" in examples_readme
    assert "browsertrace export <run_id> --public -o public.html" in examples_readme
    assert "hosted sharing" not in examples_readme


def test_examples_readme_includes_doctor_output_example():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### Check a healthy local install" in examples_readme
    assert "browsertrace doctor" in examples_readme
    assert "BrowserTrace doctor" in examples_readme
    assert "Home:" in examples_readme
    assert "Database:" in examples_readme
    assert "Runs:" in examples_readme
    assert "UI dependencies:" in examples_readme
    assert "@v0.1.15" in examples_readme
    assert "hosted sharing" not in examples_readme


def test_examples_readme_includes_cli_help_discovery_recipe():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### Discover CLI options" in examples_readme
    assert "browsertrace --help" in examples_readme
    assert "browsertrace export --help" in examples_readme
    assert "browsertrace export <run_id> --public -o public.html" in examples_readme
    assert "@v0.1.15" in examples_readme
    assert "hosted sharing" not in examples_readme


def test_examples_readme_includes_environment_variable_quick_reference():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### Environment variable quick reference" in examples_readme
    assert "`BROWSERTRACE_HOME`" in examples_readme
    assert "`BROWSERTRACE_PORT`" in examples_readme
    assert "changes the trace store" in examples_readme
    assert "changes the local UI port" in examples_readme
    assert "@v0.1.15" in examples_readme
    assert "hosted sharing" not in examples_readme


def test_examples_readme_includes_public_safe_attachment_note():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### Attach a public-safe export to an issue" in examples_readme
    assert "public.html" in examples_readme
    assert "GitHub issue or PR comment" in examples_readme
    assert "browsertrace export <run_id> --public -o public.html" in examples_readme
    assert "prompt/model I/O, screenshots, and URLs" in examples_readme
    assert "@v0.1.15" in examples_readme
    assert "hosted sharing" not in examples_readme


def test_examples_readme_includes_first_run_troubleshooting_checklist():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### First-run troubleshooting checklist" in examples_readme
    assert "browsertrace doctor" in examples_readme
    assert "browsertrace demo" in examples_readme
    assert "browsertrace list" in examples_readme
    assert "browsertrace show <run_id>" in examples_readme
    assert "browsertrace export <run_id> --public -o public.html" in examples_readme
    assert "@v0.1.15" in examples_readme
    assert "hosted sharing" not in examples_readme


def test_examples_readme_includes_json_cli_checks_recipe():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()
    troubleshooting_section = examples_readme.split("## Troubleshooting", 1)[1].split(
        "### Environment variable quick reference", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert "### JSON CLI checks for automation" in troubleshooting_section
    assert "scripts, CI, or AI/coding-agent troubleshooting" in troubleshooting_section
    assert recipe in troubleshooting_section
    assert "@v0.1.15" in examples_readme
    assert "hosted sharing" not in examples_readme


def test_examples_readme_links_llms_troubleshooting_context():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()
    troubleshooting_section = examples_readme.split("## Troubleshooting", 1)[1].split(
        "### Environment variable quick reference", 1
    )[0]

    assert "[`docs/llms.txt`](../docs/llms.txt)" in troubleshooting_section
    assert "AI/coding-agent troubleshooting context" in troubleshooting_section
    assert "JSON CLI checks" in troubleshooting_section
    assert "@v0.1.15" in examples_readme
    assert "hosted sharing" not in examples_readme


def test_examples_readme_includes_command_cheat_sheet():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### BrowserTrace command cheat sheet" in examples_readme
    assert "| Command | Use when |" in examples_readme
    assert "`browsertrace doctor`" in examples_readme
    assert "`browsertrace demo`" in examples_readme
    assert "`browsertrace list`" in examples_readme
    assert "`browsertrace show <run_id>`" in examples_readme
    assert "`browsertrace export <run_id> --public -o public.html`" in examples_readme
    assert "@v0.1.15" in examples_readme
    assert "hosted sharing" not in examples_readme


def test_examples_readme_includes_pytest_isolated_storage_recipe():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### Testing with isolated trace storage" in examples_readme
    assert "def test_browsertrace_trace_uses_temp_store" in examples_readme
    assert 'monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))' in examples_readme
    assert "Tracer()" in examples_readme
    assert "no browser, network, or API key" in " ".join(examples_readme.split())


def test_examples_readme_includes_github_actions_public_export_artifact_recipe():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### GitHub Actions artifact for public-safe exports" in examples_readme
    assert "actions/upload-artifact@v4" in examples_readme
    assert (
        "RUN_ID=$(browsertrace demo | awk -F': ' '/Run ID:/ {print $2}')"
        in examples_readme
    )
    assert 'browsertrace export "$RUN_ID" --public -o public.html' in examples_readme
    assert "BrowserTrace does not upload traces by itself" in examples_readme
    assert (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
        in examples_readme
    )


def test_examples_readme_includes_gitlab_ci_public_export_artifact_recipe():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### GitLab CI artifact for public-safe exports" in examples_readme
    assert "browsertrace-public-export:" in examples_readme
    assert (
        "RUN_ID=$(browsertrace demo | awk -F': ' '/Run ID:/ {print $2}')"
        in examples_readme
    )
    assert 'browsertrace export "$RUN_ID" --public -o public.html' in examples_readme
    assert "artifacts:" in examples_readme
    assert "public.html" in examples_readme
    assert "BrowserTrace does not upload traces by itself" in examples_readme


def test_examples_readme_includes_playwright_sync_snapshot_recipe():
    project_root = Path(__file__).resolve().parents[1]
    examples_readme = (project_root / "examples" / "README.md").read_text()

    assert "### Playwright sync API snapshot" in examples_readme
    assert "from playwright.sync_api import sync_playwright" in examples_readme
    assert "run.snapshot_sync(page, action=\"opened example.com\")" in examples_readme
    assert "sync Playwright" in examples_readme


def test_owner_profile_actions_include_browsertrace_pin_step():
    project_root = Path(__file__).resolve().parents[1]
    owner_docs = {
        "LAUNCH.md": "Pin BrowserTrace",
        "docs/launch/owner-next-actions.md": "Pin BrowserTrace",
        "docs/launch/owner-next-actions.zh-CN.md": "置顶 BrowserTrace",
        "docs/launch/owner-publish-queue.md": "Pin BrowserTrace",
    }

    for relpath, phrase in owner_docs.items():
        text = (project_root / relpath).read_text()
        assert phrase in text, relpath
        assert "aaronlab/browsertrace" in text, relpath
        assert "https://github.com/aaronlab/browsertrace/issues/24" in text, relpath


def test_first_run_docs_include_doctor_command():
    project_root = Path(__file__).resolve().parents[1]
    docs_text = "\n".join(
        [
            (project_root / "README.md").read_text(),
            (project_root / "docs" / "llms.txt").read_text(),
        ]
    )

    assert "browsertrace doctor" in docs_text
    assert "Print local install and trace-store status" in docs_text


def test_readme_explains_doctor_json_near_install_checks():
    project_root = Path(__file__).resolve().parents[1]
    readme = (project_root / "README.md").read_text()
    install_section = readme.split("## Install From The Release Tag", 1)[1].split(
        "For a walkthrough", 1
    )[0]

    assert "`browsertrace doctor --json` prints install and trace-store status as JSON" in install_section
    assert "database, run, step, and UI dependency fields" in install_section
    assert "`browsertrace doctor` is a safe local status check" in install_section
    assert "@v0.1.15" in install_section
    assert "hosted sharing" not in readme


def test_llms_txt_points_to_current_contribution_path():
    project_root = Path(__file__).resolve().parents[1]
    llms = (project_root / "docs" / "llms.txt").read_text()

    assert "Good first issue: https://github.com/aaronlab/browsertrace/issues/225" in llms
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in llms
    assert "First PR Recipe" in llms
    assert "CONTRIBUTING.md#first-pr-recipe" in llms
    assert "first contribution small and reviewable" in llms
    assert "stars" not in llms.lower()
    assert "upvotes" not in llms.lower()
    assert "reposts" not in llms.lower()
    assert (
        "Integration request: https://github.com/aaronlab/browsertrace/issues/new?template=integration_request.yml"
        in llms
    )


def test_llms_txt_includes_troubleshooting_prompt_snippet():
    project_root = Path(__file__).resolve().parents[1]
    llms = (project_root / "docs" / "llms.txt").read_text()

    assert "## Troubleshooting Prompt" in llms
    assert "browsertrace doctor" in llms
    assert "browsertrace demo" in llms
    assert "browsertrace list" in llms
    assert "browsertrace show <run_id>" in llms
    assert "browsertrace export <run_id> --public -o public.html" in llms
    assert "Good first issue: https://github.com/aaronlab/browsertrace/issues/225" in llms
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in llms
    assert "@v0.1.15" in llms
    assert "hosted sharing" not in llms


def test_llms_txt_includes_json_cli_troubleshooting_snippet():
    project_root = Path(__file__).resolve().parents[1]
    llms = (project_root / "docs" / "llms.txt").read_text()
    troubleshooting_prompt = llms.split("## Troubleshooting Prompt", 1)[1].split(
        "## Positioning", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert "For scripts, CI, or AI/coding-agent troubleshooting" in troubleshooting_prompt
    assert recipe in troubleshooting_prompt
    assert "Good first issue: https://github.com/aaronlab/browsertrace/issues/225" in llms
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in llms
    assert "@v0.1.15" in llms
    assert "hosted sharing" not in llms


def test_press_kit_includes_current_trial_and_contribution_paths():
    project_root = Path(__file__).resolve().parents[1]
    press_kit = (project_root / "docs" / "launch" / "press-kit.md").read_text()
    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )
    contribution_links = press_kit.split("## Contribution Links", 1)[1].split(
        "## Troubleshooting Reply", 1
    )[0]

    assert f'uvx --from "{github_spec}" browsertrace doctor' in press_kit
    assert f'uvx --from "{github_spec}" browsertrace demo' in press_kit
    assert "Good first issue: https://github.com/aaronlab/browsertrace/issues/225" in press_kit
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in press_kit
    assert "First PR Recipe" in contribution_links
    assert "first contribution small and reviewable" in contribution_links
    assert "stars" not in contribution_links.lower()
    assert "upvotes" not in contribution_links.lower()
    assert "reposts" not in contribution_links.lower()


def test_press_kit_includes_json_cli_troubleshooting_reply():
    project_root = Path(__file__).resolve().parents[1]
    press_kit = (project_root / "docs" / "launch" / "press-kit.md").read_text()
    assert "## Troubleshooting Reply" in press_kit
    reply = press_kit.split("## Troubleshooting Reply", 1)[1].split(
        "## Safe Ask", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "press/editorial follow-up, local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply
    )
    assert recipe in reply
    assert "debugging/workflow details" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_core_guides_advertise_llms_txt():
    project_root = Path(__file__).resolve().parents[1]

    for filename in [
        "debug-browser-agent-failure.html",
        "browser-use-debugging.html",
        "stagehand-debugging.html",
        "skyvern-debugging.html",
        "playwright-llm-debugging.html",
        "computer-use-agent-debugging.html",
    ]:
        page = (project_root / "docs" / filename).read_text()
        assert (
            '<link rel="alternate" type="text/plain" title="llms.txt" href="./llms.txt">'
            in page
        ), filename


def test_browser_use_guide_has_troubleshooting_section():
    project_root = Path(__file__).resolve().parents[1]
    page = (project_root / "docs" / "browser-use-debugging.html").read_text()

    assert "Troubleshooting Browser Use traces" in page
    assert "Could not attach to this Agent" in page
    assert "register_new_step_callback" in page
    assert "No screenshots appear" in page
    assert "browsertrace export &lt;run_id&gt; --public -o public.html" in page


def test_browser_use_guide_documents_callback_compatibility():
    project_root = Path(__file__).resolve().parents[1]
    page = (project_root / "docs" / "browser-use-debugging.html").read_text()

    assert "Callback compatibility" in page
    assert "on_step_start" in page
    assert "on_step_end" in page
    assert "register_new_step_callback" in page
    assert "run-hook-only" in page
    assert "create_run_hooks" in page
    assert "agent.run(on_step_start=hooks.on_step_start" in page


def test_sitemap_exposes_llms_txt_and_core_discovery_pages():
    project_root = Path(__file__).resolve().parents[1]
    sitemap = (project_root / "docs" / "sitemap.xml").read_text()

    for path in [
        "",
        "llms.txt",
        "debug-browser-agent-failure.html",
        "browser-use-debugging.html",
        "stagehand-debugging.html",
        "skyvern-debugging.html",
        "playwright-llm-debugging.html",
        "computer-use-agent-debugging.html",
        "integrations.html",
        "launch/",
    ]:
        assert f"https://aaronlab.github.io/browsertrace/{path}" in sitemap, path


def test_sitemap_lastmod_matches_current_launch_refresh():
    project_root = Path(__file__).resolve().parents[1]
    sitemap = (project_root / "docs" / "sitemap.xml").read_text()

    assert "<lastmod>2026-05-10</lastmod>" in sitemap
    assert "<lastmod>2026-05-09</lastmod>" not in sitemap


def test_launch_copy_includes_uvx_github_trial_before_pypi():
    project_root = Path(__file__).resolve().parents[1]
    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )

    for relpath in [
        "docs/launch/channel-copy.md",
        "docs/launch/day-1-publish-packet.md",
        "docs/launch/day-2-show-hn-packet.md",
    ]:
        text = (project_root / relpath).read_text()
        assert f'uvx --from "{github_spec}" browsertrace doctor' in text, relpath
        assert f'uvx --from "{github_spec}" browsertrace demo' in text, relpath
        assert "before pypi publishing is enabled" in text.lower(), relpath


def test_longform_launch_posts_include_uvx_github_trial_before_pypi():
    project_root = Path(__file__).resolve().parents[1]
    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )

    for relpath in [
        "docs/launch/tutorial-post.md",
        "docs/launch/chinese-tutorial-post.md",
        "docs/launch/response-templates.md",
    ]:
        text = (project_root / relpath).read_text()
        assert f'uvx --from "{github_spec}" browsertrace doctor' in text, relpath
        assert f'uvx --from "{github_spec}" browsertrace demo' in text, relpath
        assert "pypi" in text.lower(), relpath


def test_response_templates_include_json_cli_diagnostics_reply():
    project_root = Path(__file__).resolve().parents[1]
    templates = (
        project_root / "docs" / "launch" / "response-templates.md"
    ).read_text()
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert "local first-run issues, CI failures, or AI/coding-agent troubleshooting" in templates
    assert recipe in templates
    assert "workflow/debugging details" in templates
    assert "stars" not in templates.lower()
    assert "upvotes" not in templates.lower()
    assert "reposts" not in templates.lower()


def test_response_templates_link_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    templates = (
        project_root / "docs" / "launch" / "response-templates.md"
    ).read_text()
    assert "## Can I contribute a small fix?" in templates
    reply = templates.split("## Can I contribute a small fix?", 1)[1].split(
        "## Can you share JSON diagnostics?", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/225" in reply
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in reply
    assert "First PR Recipe" in reply
    assert "CONTRIBUTING.md#first-pr-recipe" in reply
    assert "first contribution small and reviewable" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_response_templates_link_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    templates = (
        project_root / "docs" / "launch" / "response-templates.md"
    ).read_text()
    reply = templates.split("## Can I contribute a small fix?", 1)[1].split(
        "## Can you share JSON diagnostics?", 1
    )[0]

    assert "SECURITY.md" in reply
    assert "security-sensitive reports" in reply
    assert "private trace data" in reply


def test_owner_publish_queue_includes_json_cli_reply_workflow():
    project_root = Path(__file__).resolve().parents[1]
    queue = (project_root / "docs" / "launch" / "owner-publish-queue.md").read_text()
    reply_workflow = queue.split("## Reply Workflow", 1)[1].split(
        "## Metrics Check", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply_workflow
    )
    assert recipe in reply_workflow
    assert "debugging/workflow details" in reply_workflow
    assert "https://github.com/aaronlab/browsertrace/issues/225" in reply_workflow
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in reply_workflow
    assert "First PR Recipe" in reply_workflow
    assert "CONTRIBUTING.md#first-pr-recipe" in reply_workflow
    assert "first contribution small and reviewable" in reply_workflow
    assert "stars" not in reply_workflow.lower()
    assert "upvotes" not in reply_workflow.lower()
    assert "reposts" not in reply_workflow.lower()


def test_owner_publish_queue_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    queue = (project_root / "docs" / "launch" / "owner-publish-queue.md").read_text()
    reply_workflow = queue.split("## Reply Workflow", 1)[1].split(
        "## Metrics Check", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md" in reply_workflow
    assert "security-sensitive reports or changes" in reply_workflow
    assert "private trace data" in reply_workflow


def test_owner_publish_queue_records_current_awesome_list_pr_count():
    project_root = Path(__file__).resolve().parents[1]
    queue = (project_root / "docs" / "launch" / "owner-publish-queue.md").read_text()

    assert "nine high-fit PRs are already open" in queue
    assert "the three prepared PRs" not in queue
    assert "ai-boost/awesome-harness-engineering#23" in queue
    assert "Agent-Tools/awesome-autonomous-web#21" in queue
    assert "e2b-dev/awesome-ai-sdks#187" in queue
    assert "CLA signature" in queue
    assert "steel-dev/awesome-web-agents#56" in queue


def test_day_1_publish_packet_includes_json_cli_reply_shortcut():
    project_root = Path(__file__).resolve().parents[1]
    packet = (project_root / "docs" / "launch" / "day-1-publish-packet.md").read_text()
    reply_shortcuts = packet.split("## Reply Shortcuts", 1)[1].split(
        "## Day 1 Log", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply_shortcuts
    )
    assert recipe in reply_shortcuts
    assert "debugging/workflow details" in reply_shortcuts
    assert "https://github.com/aaronlab/browsertrace/issues/225" in reply_shortcuts
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in reply_shortcuts
    assert "First PR Recipe" in reply_shortcuts
    assert "CONTRIBUTING.md#first-pr-recipe" in reply_shortcuts
    assert "first contribution small and reviewable" in reply_shortcuts
    assert "stars" not in reply_shortcuts.lower()
    assert "upvotes" not in reply_shortcuts.lower()
    assert "reposts" not in reply_shortcuts.lower()


def test_day_1_publish_packet_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    packet = (project_root / "docs" / "launch" / "day-1-publish-packet.md").read_text()
    reply_shortcuts = packet.split("## Reply Shortcuts", 1)[1].split(
        "## Day 1 Log", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md" in reply_shortcuts
    assert "security-sensitive reports or changes" in reply_shortcuts
    assert "private trace data" in reply_shortcuts


def test_day_3_targeted_communities_include_json_cli_reply_note():
    project_root = Path(__file__).resolve().parents[1]
    packet = (
        project_root / "docs" / "launch" / "day-3-targeted-communities-packet.md"
    ).read_text()
    triage = packet.split("## Triage After Posting", 1)[1].split("## Stop Rules", 1)[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in triage
    )
    assert recipe in triage
    assert "debugging/workflow details" in triage
    assert "https://github.com/aaronlab/browsertrace/issues/225" in triage
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in triage
    assert "First PR Recipe" in triage
    assert "CONTRIBUTING.md#first-pr-recipe" in triage
    assert "first contribution small and reviewable" in triage
    assert "stars" not in triage.lower()
    assert "upvotes" not in triage.lower()
    assert "reposts" not in triage.lower()


def test_directory_submission_sheet_includes_uvx_trial_before_pypi():
    project_root = Path(__file__).resolve().parents[1]
    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )
    sheet = (project_root / "docs" / "launch" / "directory-submission-sheet.md").read_text()

    assert "before pypi publishing is enabled" in sheet.lower()
    assert f'uvx --from "{github_spec}" browsertrace doctor' in sheet
    assert f'uvx --from "{github_spec}" browsertrace demo' in sheet


def test_directory_submission_sheet_records_agentfirst_pr_submission():
    project_root = Path(__file__).resolve().parents[1]
    sheet = (project_root / "docs" / "launch" / "directory-submission-sheet.md").read_text()

    assert "agentfirst.directory" in sheet
    assert "https://github.com/bradvin/agentfirst.directory/pull/30" in sheet
    assert "Submitted PR" in sheet


def test_directory_submission_sheet_records_current_awesome_list_pr_count():
    project_root = Path(__file__).resolve().parents[1]
    sheet = (project_root / "docs" / "launch" / "directory-submission-sheet.md").read_text()

    assert "9 PRs open; monitor feedback; e2b CLA blocked" in sheet
    assert "3 PRs open" not in sheet
    assert "github-awesome-list-submissions.md" in sheet


def test_directory_submission_sheet_records_current_directory_submission_blockers():
    project_root = Path(__file__).resolve().parents[1]
    sheet = (project_root / "docs" / "launch" / "directory-submission-sheet.md").read_text()

    assert "AgentKart" in sheet
    assert "Sign-in button present; static form has no usable submit handler" in sheet
    assert "OSS AI Hub" in sheet
    assert "login required before submitting tools" in sheet
    assert "AgentsTide" in sheet
    assert "contact email only" in sheet
    assert "BuilderAI Tools" in sheet
    assert "owner email and Cloudflare Turnstile required" in sheet


def test_directory_submission_sheet_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    sheet = (project_root / "docs" / "launch" / "directory-submission-sheet.md").read_text()
    assert "## Contribution Reply" in sheet
    contribution_reply = sheet.split("## Contribution Reply", 1)[1].split(
        "## Troubleshooting Reply", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/225" in contribution_reply
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in contribution_reply
    assert "First PR Recipe" in contribution_reply
    assert "CONTRIBUTING.md#first-pr-recipe" in contribution_reply
    assert "first contribution small and reviewable" in contribution_reply
    assert "stars" not in contribution_reply.lower()
    assert "upvotes" not in contribution_reply.lower()
    assert "reposts" not in contribution_reply.lower()


def test_product_hunt_packet_includes_current_trial_and_contribution_paths():
    project_root = Path(__file__).resolve().parents[1]
    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )
    packet = (project_root / "docs" / "launch" / "day-4-product-hunt-packet.md").read_text()
    contributor_block = packet.split("Good first issue for contributors:", 1)[
        1
    ].split("Description:", 1)[0]

    assert f'uvx --from "{github_spec}" browsertrace doctor' in packet
    assert f'uvx --from "{github_spec}" browsertrace demo' in packet
    assert "https://github.com/aaronlab/browsertrace/issues/225" in packet
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in packet
    assert "First PR Recipe" in contributor_block
    assert "CONTRIBUTING.md#first-pr-recipe" in contributor_block
    assert "first contribution small and reviewable" in contributor_block
    assert "stars" not in contributor_block.lower()
    assert "upvotes" not in contributor_block.lower()
    assert "reposts" not in contributor_block.lower()


def test_show_hn_packet_links_current_good_first_issue():
    project_root = Path(__file__).resolve().parents[1]
    packet = (project_root / "docs" / "launch" / "day-2-show-hn-packet.md").read_text()
    contribution_reply = packet.split("Can I contribute a small fix?", 1)[
        1
    ].split("## Troubleshooting Reply", 1)[0]

    assert "current one is #225" in packet
    assert "#213" not in packet
    assert "First PR Recipe" in contribution_reply
    assert "CONTRIBUTING.md#first-pr-recipe" in contribution_reply
    assert "first contribution small and reviewable" in contribution_reply
    assert "stars" not in contribution_reply.lower()
    assert "upvotes" not in contribution_reply.lower()
    assert "reposts" not in contribution_reply.lower()


def test_product_hunt_packet_includes_json_cli_reply_note():
    project_root = Path(__file__).resolve().parents[1]
    packet = (project_root / "docs" / "launch" / "day-4-product-hunt-packet.md").read_text()
    reply_notes = packet.split("## Reply Notes", 1)[1].split("## Metrics", 1)[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply_notes
    )
    assert recipe in reply_notes
    assert "debugging/workflow details" in reply_notes
    assert "upvotes" not in reply_notes.lower()
    assert "reposts" not in reply_notes.lower()


def test_product_hunt_packet_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    packet = (project_root / "docs" / "launch" / "day-4-product-hunt-packet.md").read_text()
    reply_notes = packet.split("## Reply Notes", 1)[1].split("## Metrics", 1)[0]

    assert "https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md" in reply_notes
    assert "security-sensitive reports or changes" in reply_notes
    assert "private trace data" in reply_notes


def test_show_hn_packet_includes_json_cli_troubleshooting_reply():
    project_root = Path(__file__).resolve().parents[1]
    packet = (project_root / "docs" / "launch" / "day-2-show-hn-packet.md").read_text()
    assert "## Troubleshooting Reply" in packet
    reply = packet.split("## Troubleshooting Reply", 1)[1].split("## Metrics", 1)[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "Show HN technical follow-up, local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply
    )
    assert recipe in reply
    assert "debugging/workflow details" in reply
    assert "human-written" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_show_hn_packet_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    packet = (project_root / "docs" / "launch" / "day-2-show-hn-packet.md").read_text()
    reply = packet.split("## Troubleshooting Reply", 1)[1].split("## Metrics", 1)[0]

    assert "https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md" in reply
    assert "security-sensitive reports or changes" in reply
    assert "private trace data" in reply


def test_channel_copy_includes_json_cli_troubleshooting_reply():
    project_root = Path(__file__).resolve().parents[1]
    copy = (project_root / "docs" / "launch" / "channel-copy.md").read_text()
    assert "## Troubleshooting Reply" in copy
    reply = copy.split("## Troubleshooting Reply", 1)[1].split("## X", 1)[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply
    )
    assert "https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md" in reply
    assert "security-sensitive reports or changes" in reply
    assert "private trace data" in reply
    assert recipe in reply
    assert "debugging/workflow details" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_channel_copy_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    copy = (project_root / "docs" / "launch" / "channel-copy.md").read_text()
    reply = copy.split("## Troubleshooting Reply", 1)[1].split("## X", 1)[0]

    assert "https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md" in reply
    assert "security-sensitive reports or changes" in reply
    assert "private trace data" in reply


def test_channel_copy_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    copy = (project_root / "docs" / "launch" / "channel-copy.md").read_text()
    assert "## Contribution Reply" in copy
    contribution_reply = copy.split("## Contribution Reply", 1)[1].split(
        "## Troubleshooting Reply", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/225" in contribution_reply
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in contribution_reply
    assert "First PR Recipe" in contribution_reply
    assert "CONTRIBUTING.md#first-pr-recipe" in contribution_reply
    assert "first contribution small and reviewable" in contribution_reply
    assert "stars" not in contribution_reply.lower()
    assert "upvotes" not in contribution_reply.lower()
    assert "reposts" not in contribution_reply.lower()


def test_tutorial_post_includes_json_cli_troubleshooting_reply():
    project_root = Path(__file__).resolve().parents[1]
    tutorial = (project_root / "docs" / "launch" / "tutorial-post.md").read_text()
    assert "## Reply To Troubleshooting Questions" in tutorial
    reply = tutorial.split("## Reply To Troubleshooting Questions", 1)[1].split(
        "## Try it", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply
    )
    assert recipe in reply
    assert "debugging/workflow details" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_tutorial_post_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    tutorial = (project_root / "docs" / "launch" / "tutorial-post.md").read_text()
    reply = tutorial.split("## Reply To Troubleshooting Questions", 1)[1].split(
        "## Try it", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md" in reply
    assert "security-sensitive reports or changes" in reply
    assert "private trace data" in reply


def test_tutorial_post_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    tutorial = (project_root / "docs" / "launch" / "tutorial-post.md").read_text()
    assert "## Reply To Contribution Questions" in tutorial
    reply = tutorial.split("## Reply To Contribution Questions", 1)[1].split(
        "## Reply To Troubleshooting Questions", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/225" in reply
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in reply
    assert "First PR Recipe" in reply
    assert "CONTRIBUTING.md#first-pr-recipe" in reply
    assert "first contribution small and reviewable" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_chinese_tutorial_post_includes_json_cli_troubleshooting_reply():
    project_root = Path(__file__).resolve().parents[1]
    tutorial = (
        project_root / "docs" / "launch" / "chinese-tutorial-post.md"
    ).read_text()
    assert "## 回复本地首跑 / CI / agent 调试问题" in tutorial
    reply = tutorial.split("## 回复本地首跑 / CI / agent 调试问题", 1)[1].split(
        "## Links", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply
    )
    assert recipe in reply
    assert "debugging/workflow details" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_chinese_tutorial_post_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    tutorial = (
        project_root / "docs" / "launch" / "chinese-tutorial-post.md"
    ).read_text()
    reply = tutorial.split("## 回复本地首跑 / CI / agent 调试问题", 1)[1].split(
        "## Links", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md" in reply
    assert "security-sensitive reports or changes" in reply
    assert "private trace data" in reply


def test_chinese_tutorial_post_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    tutorial = (
        project_root / "docs" / "launch" / "chinese-tutorial-post.md"
    ).read_text()
    assert "## 回复小贡献问题" in tutorial
    reply = tutorial.split("## 回复小贡献问题", 1)[1].split(
        "## 回复本地首跑 / CI / agent 调试问题", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/225" in reply
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in reply
    assert "First PR Recipe" in reply
    assert "CONTRIBUTING.md#first-pr-recipe" in reply
    assert "first contribution small and reviewable" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_owner_next_actions_include_json_cli_troubleshooting_reply():
    project_root = Path(__file__).resolve().parents[1]
    checklist = (project_root / "docs" / "launch" / "owner-next-actions.md").read_text()
    assert "## Reply To Troubleshooting Questions" in checklist
    reply = checklist.split("## Reply To Troubleshooting Questions", 1)[1].split(
        "## 8. Record Metrics After Each Action", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply
    )
    assert recipe in reply
    assert "debugging/workflow details" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_owner_next_actions_preserves_external_awesome_list_pr_numbers():
    project_root = Path(__file__).resolve().parents[1]
    checklist = (project_root / "docs" / "launch" / "owner-next-actions.md").read_text()
    awesome_prs = checklist.split(
        "## 7. Monitor High-Fit GitHub Awesome List PRs", 1
    )[1].split("## Reply To Contribution Questions", 1)[0]

    assert "angrykoala/awesome-browser-automation#112" in awesome_prs
    assert "mxschmitt/awesome-playwright#136" in awesome_prs
    assert "Jenqyang/Awesome-AI-Agents#220" in awesome_prs
    assert "wjhou/awesome-computer-use-agents#2" in awesome_prs
    assert "cdxeve/awesome-computer-use-agents#2" in awesome_prs
    assert "steel-dev/awesome-web-agents#56" in awesome_prs
    assert "ai-boost/awesome-harness-engineering#23" in awesome_prs
    assert "Agent-Tools/awesome-autonomous-web#21" in awesome_prs
    assert "e2b-dev/awesome-ai-sdks#187" in awesome_prs
    assert "CLA signature" in awesome_prs
    assert "Jenqyang/Awesome-AI-Agents#221" not in awesome_prs
    assert "Jenqyang/Awesome-AI-Agents#222" not in awesome_prs


def test_chinese_owner_next_actions_preserves_external_awesome_list_pr_numbers():
    project_root = Path(__file__).resolve().parents[1]
    checklist = (
        project_root / "docs" / "launch" / "owner-next-actions.zh-CN.md"
    ).read_text()
    awesome_prs = checklist.split("已经打开的 PR：", 1)[1].split(
        "目录/newsletter 跟踪 issue", 1
    )[0]

    assert "angrykoala/awesome-browser-automation/pull/112" in awesome_prs
    assert "mxschmitt/awesome-playwright/pull/136" in awesome_prs
    assert "Jenqyang/Awesome-AI-Agents/pull/220" in awesome_prs
    assert "wjhou/awesome-computer-use-agents/pull/2" in awesome_prs
    assert "cdxeve/awesome-computer-use-agents/pull/2" in awesome_prs
    assert "steel-dev/awesome-web-agents/pull/56" in awesome_prs
    assert "ai-boost/awesome-harness-engineering/pull/23" in awesome_prs
    assert "Agent-Tools/awesome-autonomous-web/pull/21" in awesome_prs
    assert "e2b-dev/awesome-ai-sdks/pull/187" in awesome_prs
    assert "CLA" in awesome_prs
    assert "Jenqyang/Awesome-AI-Agents/pull/221" not in awesome_prs
    assert "Jenqyang/Awesome-AI-Agents/pull/222" not in awesome_prs


def test_owner_next_actions_link_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    checklist = (project_root / "docs" / "launch" / "owner-next-actions.md").read_text()
    reply = checklist.split("## Reply To Troubleshooting Questions", 1)[1].split(
        "## 8. Record Metrics After Each Action", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md" in reply
    assert "security-sensitive reports or changes" in reply
    assert "private trace data" in reply


def test_owner_next_actions_link_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    checklist = (project_root / "docs" / "launch" / "owner-next-actions.md").read_text()
    assert "## Reply To Contribution Questions" in checklist
    reply = checklist.split("## Reply To Contribution Questions", 1)[1].split(
        "## Reply To Troubleshooting Questions", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/225" in reply
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in reply
    assert "First PR Recipe" in reply
    assert "CONTRIBUTING.md#first-pr-recipe" in reply
    assert "first contribution small and reviewable" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_owner_next_actions_set_good_first_issue_claim_window():
    project_root = Path(__file__).resolve().parents[1]
    checklist = (project_root / "docs" / "launch" / "owner-next-actions.md").read_text()
    reply = checklist.split("## Reply To Contribution Questions", 1)[1].split(
        "## Reply To Troubleshooting Questions", 1
    )[0]

    assert "short claim window" in reply
    assert "before implementing it yourself" in reply
    assert "already finished" in reply
    assert "current good first issue" in reply


def test_chinese_owner_next_actions_include_json_cli_troubleshooting_reply():
    project_root = Path(__file__).resolve().parents[1]
    checklist = (
        project_root / "docs" / "launch" / "owner-next-actions.zh-CN.md"
    ).read_text()
    assert "## 回复本地首跑 / CI / agent 调试问题" in checklist
    reply = checklist.split("## 回复本地首跑 / CI / agent 调试问题", 1)[1].split(
        "## 7. 每做完一个动作就记录指标", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply
    )
    assert recipe in reply
    assert "debugging/workflow details" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_chinese_owner_next_actions_link_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    checklist = (
        project_root / "docs" / "launch" / "owner-next-actions.zh-CN.md"
    ).read_text()
    reply = checklist.split("## 回复本地首跑 / CI / agent 调试问题", 1)[1].split(
        "## 7. 每做完一个动作就记录指标", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md" in reply
    assert "security-sensitive reports or changes" in reply
    assert "private trace data" in reply


def test_chinese_owner_next_actions_link_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    checklist = (
        project_root / "docs" / "launch" / "owner-next-actions.zh-CN.md"
    ).read_text()
    assert "## 回复小贡献问题" in checklist
    reply = checklist.split("## 回复小贡献问题", 1)[1].split(
        "## 回复本地首跑 / CI / agent 调试问题", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/225" in reply
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in reply
    assert "First PR Recipe" in reply
    assert "CONTRIBUTING.md#first-pr-recipe" in reply
    assert "first contribution small and reviewable" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_chinese_owner_next_actions_set_good_first_issue_claim_window():
    project_root = Path(__file__).resolve().parents[1]
    checklist = (
        project_root / "docs" / "launch" / "owner-next-actions.zh-CN.md"
    ).read_text()
    reply = checklist.split("## 回复小贡献问题", 1)[1].split(
        "## 回复本地首跑 / CI / agent 调试问题", 1
    )[0]

    assert "短的认领窗口" in reply
    assert "不要马上自己实现同一个 issue" in reply
    assert "如果这个任务已经完成" in reply
    assert "当前 good first issue" in reply


def test_directory_submission_sheet_includes_json_cli_troubleshooting_reply():
    project_root = Path(__file__).resolve().parents[1]
    sheet = (project_root / "docs" / "launch" / "directory-submission-sheet.md").read_text()
    assert "## Troubleshooting Reply" in sheet
    reply = sheet.split("## Troubleshooting Reply", 1)[1].split("## Tracking", 1)[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply
    )
    assert recipe in reply
    assert "debugging/workflow details" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_outreach_targets_include_json_cli_troubleshooting_reply():
    project_root = Path(__file__).resolve().parents[1]
    targets = (project_root / "docs" / "launch" / "outreach-targets.md").read_text()
    assert "## Troubleshooting Reply" in targets
    reply = targets.split("## Troubleshooting Reply", 1)[1].split(
        "## First Targeted Community Posts", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply
    )
    assert recipe in reply
    assert "debugging/workflow details" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_outreach_targets_records_current_awesome_list_pr_count():
    project_root = Path(__file__).resolve().parents[1]
    targets = (project_root / "docs" / "launch" / "outreach-targets.md").read_text()

    assert "Nine focused PRs are already open" in targets
    assert "one blocked on owner CLA signature" in targets
    assert "Three focused PRs" not in targets
    assert "Do not open more list PRs unless the target is clearly high-fit" in targets


def test_outreach_targets_link_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    targets = (project_root / "docs" / "launch" / "outreach-targets.md").read_text()
    assert "## Contribution Reply" in targets
    contribution_reply = targets.split("## Contribution Reply", 1)[1].split(
        "## Troubleshooting Reply", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/225" in contribution_reply
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in contribution_reply
    assert "First PR Recipe" in contribution_reply
    assert "CONTRIBUTING.md#first-pr-recipe" in contribution_reply
    assert "first contribution small and reviewable" in contribution_reply
    assert "stars" not in contribution_reply.lower()
    assert "upvotes" not in contribution_reply.lower()
    assert "reposts" not in contribution_reply.lower()


def test_search_indexing_submission_links_first_pr_recipe_for_small_contributions():
    project_root = Path(__file__).resolve().parents[1]
    submission = (
        project_root / "docs" / "launch" / "search-indexing-submission.md"
    ).read_text()
    assert "## Contribution Reply" in submission
    contribution_reply = submission.split("## Contribution Reply", 1)[1].split(
        "## Troubleshooting Reply", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/225" in contribution_reply
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in contribution_reply
    assert "First PR Recipe" in contribution_reply
    assert "CONTRIBUTING.md#first-pr-recipe" in contribution_reply
    assert "first contribution small and reviewable" in contribution_reply
    assert "stars" not in contribution_reply.lower()
    assert "upvotes" not in contribution_reply.lower()
    assert "reposts" not in contribution_reply.lower()


def test_search_indexing_submission_includes_json_cli_troubleshooting_reply():
    project_root = Path(__file__).resolve().parents[1]
    submission = (
        project_root / "docs" / "launch" / "search-indexing-submission.md"
    ).read_text()
    assert "## Troubleshooting Reply" in submission
    reply = submission.split("## Troubleshooting Reply", 1)[1].split(
        "## Google Search Console", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "crawl/indexing follow-up, local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply
    )
    assert recipe in reply
    assert "debugging/workflow details" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_bug_report_template_requests_json_cli_troubleshooting_checks():
    project_root = Path(__file__).resolve().parents[1]
    template = (
        project_root / ".github" / "ISSUE_TEMPLATE" / "bug_report.yml"
    ).read_text()

    assert "issue reports, CI, or AI/coding-agent troubleshooting" in template
    assert "CONTRIBUTING.md#first-pr-recipe" in template
    assert "first contribution small and reviewable" in template
    assert "browsertrace doctor --json" in template
    assert "browsertrace list --status failed --json" in template
    assert "browsertrace show <run_id> --json" in template
    assert "stars" not in template.lower()
    assert "upvotes" not in template.lower()


def test_bug_report_template_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    template = (
        project_root / ".github" / "ISSUE_TEMPLATE" / "bug_report.yml"
    ).read_text()

    assert "SECURITY.md" in template
    assert "security-sensitive reports" in template
    assert "private trace data" in template


def test_integration_request_template_requests_json_cli_troubleshooting_checks():
    project_root = Path(__file__).resolve().parents[1]
    template = (
        project_root / ".github" / "ISSUE_TEMPLATE" / "integration_request.yml"
    ).read_text()

    assert "integration requests, CI, or AI/coding-agent troubleshooting" in template
    assert "CONTRIBUTING.md#first-pr-recipe" in template
    assert "first contribution small and reviewable" in template
    assert "browsertrace doctor --json" in template
    assert "browsertrace list --status failed --json" in template
    assert "browsertrace show <run_id> --json" in template
    assert "stars" not in template.lower()
    assert "upvotes" not in template.lower()


def test_integration_request_template_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    template = (
        project_root / ".github" / "ISSUE_TEMPLATE" / "integration_request.yml"
    ).read_text()

    assert "SECURITY.md" in template
    assert "security-sensitive reports" in template
    assert "private trace data" in template


def test_feature_request_template_links_first_pr_recipe():
    project_root = Path(__file__).resolve().parents[1]
    template = (
        project_root / ".github" / "ISSUE_TEMPLATE" / "feature_request.yml"
    ).read_text()

    assert "Describe the smallest useful version of the feature." in template
    assert "CONTRIBUTING.md#first-pr-recipe" in template
    assert "first contribution small and reviewable" in template
    assert "stars" not in template.lower()
    assert "upvotes" not in template.lower()
    assert "reposts" not in template.lower()


def test_feature_request_template_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    template = (
        project_root / ".github" / "ISSUE_TEMPLATE" / "feature_request.yml"
    ).read_text()

    assert (
        "[Security Policy](https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md)"
        in template
    )
    assert "security-sensitive reports" in template
    assert "private trace data" in template
    assert "stars" not in template.lower()
    assert "upvotes" not in template.lower()
    assert "reposts" not in template.lower()


def test_cloud_interest_template_links_first_pr_recipe():
    project_root = Path(__file__).resolve().parents[1]
    template = (
        project_root / ".github" / "ISSUE_TEMPLATE" / "cloud_interest.yml"
    ).read_text()

    assert "Team workflow" in template
    assert "Data and security constraints" in template
    assert "privacy, retention, customer-data, or deployment constraints" in template
    assert "CONTRIBUTING.md#first-pr-recipe" in template
    assert "first contribution small and reviewable" in template
    assert "stars" not in template.lower()
    assert "upvotes" not in template.lower()


def test_cloud_interest_template_links_security_policy_for_sensitive_reports():
    project_root = Path(__file__).resolve().parents[1]
    template = (
        project_root / ".github" / "ISSUE_TEMPLATE" / "cloud_interest.yml"
    ).read_text()

    assert "SECURITY.md" in template
    assert "security-sensitive reports" in template
    assert "private trace data" in template


def test_pull_request_template_requests_json_cli_troubleshooting_checks():
    project_root = Path(__file__).resolve().parents[1]
    template = (project_root / ".github" / "PULL_REQUEST_TEMPLATE.md").read_text()

    assert "issue reports, CI, or AI/coding-agent troubleshooting" in template
    assert "browsertrace doctor --json" in template
    assert "browsertrace list --status failed --json" in template
    assert "browsertrace show <run_id> --json" in template
    assert "stars" not in template.lower()
    assert "upvotes" not in template.lower()


def test_pull_request_template_prompts_for_real_contributor_details():
    project_root = Path(__file__).resolve().parents[1]
    template = (project_root / ".github" / "PULL_REQUEST_TEMPLATE.md").read_text()

    assert "<summary>" not in template
    assert "Replace every placeholder before requesting review." in template
    assert "CONTRIBUTING.md#first-pr-recipe" in template
    assert "first contribution small and reviewable" in template
    assert "CODE_OF_CONDUCT.md" in template
    assert "PR discussions and reviews" in template
    assert "Fixes #123 or Refs #123" in template
    assert "I ran `uv run --python 3.11 --extra dev pytest -q`" in template


def test_pull_request_template_links_security_policy_for_sensitive_changes():
    project_root = Path(__file__).resolve().parents[1]
    template = (project_root / ".github" / "PULL_REQUEST_TEMPLATE.md").read_text()

    assert "SECURITY.md" in template
    assert "security-sensitive changes" in template
    assert "private trace data" in template


def test_security_policy_has_private_report_path_without_email_placeholder():
    project_root = Path(__file__).resolve().parents[1]
    policy = (project_root / "SECURITY.md").read_text()
    normalized = " ".join(policy.split())

    assert "private GitHub vulnerability report" in normalized
    assert "open a minimal public issue without exploit details" in normalized
    assert "emailing the maintainer" not in policy
    assert "browsertrace export <run_id> --public -o public.html" in policy


def test_awesome_list_submission_notes_include_trial_and_demo_links():
    project_root = Path(__file__).resolve().parents[1]
    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )
    notes = (
        project_root / "docs" / "launch" / "github-awesome-list-submissions.md"
    ).read_text()

    assert "https://aaronlab.github.io/browsertrace/" in notes
    assert "browsertrace-demo-public.html" in notes
    assert f'uvx --from "{github_spec}" browsertrace doctor' in notes
    assert f'uvx --from "{github_spec}" browsertrace demo' in notes


def test_awesome_list_submission_notes_link_first_pr_recipe_for_contributors():
    project_root = Path(__file__).resolve().parents[1]
    notes = (
        project_root / "docs" / "launch" / "github-awesome-list-submissions.md"
    ).read_text()
    assert "## Contribution Reply" in notes
    contribution_reply = notes.split("## Contribution Reply", 1)[1].split(
        "## Troubleshooting Reply", 1
    )[0]

    assert "https://github.com/aaronlab/browsertrace/issues/225" in contribution_reply
    assert "https://github.com/aaronlab/browsertrace/issues/213" not in contribution_reply
    assert "First PR Recipe" in contribution_reply
    assert "CONTRIBUTING.md#first-pr-recipe" in contribution_reply
    assert "first contribution small and reviewable" in contribution_reply
    assert "stars" not in contribution_reply.lower()
    assert "upvotes" not in contribution_reply.lower()
    assert "reposts" not in contribution_reply.lower()


def test_awesome_list_submission_notes_include_json_cli_reviewer_reply():
    project_root = Path(__file__).resolve().parents[1]
    notes = (
        project_root / "docs" / "launch" / "github-awesome-list-submissions.md"
    ).read_text()
    assert "## Troubleshooting Reply" in notes
    reply = notes.split("## Troubleshooting Reply", 1)[1].split(
        "## Recommended Order", 1
    )[0]
    recipe = """```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```"""

    assert (
        "awesome-list reviewer follow-up, local first-run issues, CI failures, or AI/coding-agent troubleshooting replies"
        in reply
    )
    assert "https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md" in reply
    assert "security-sensitive reports or changes" in reply
    assert "private trace data" in reply
    assert recipe in reply
    assert "debugging/workflow details" in reply
    assert "stars" not in reply.lower()
    assert "upvotes" not in reply.lower()
    assert "reposts" not in reply.lower()


def test_awesome_list_submission_notes_record_steel_web_agents_pr():
    project_root = Path(__file__).resolve().parents[1]
    notes = (
        project_root / "docs" / "launch" / "github-awesome-list-submissions.md"
    ).read_text()

    assert "steel-dev/awesome-web-agents" in notes
    assert "https://github.com/steel-dev/awesome-web-agents/pull/56" in notes
    assert "Dev Tools" in notes
    assert "action_required" in notes
    assert "GITHUB_TOKEN=$(gh auth token) npx -y awesome-lint@2.2.3 README.md" in notes


def test_awesome_list_submission_notes_record_harness_engineering_pr():
    project_root = Path(__file__).resolve().parents[1]
    notes = (
        project_root / "docs" / "launch" / "github-awesome-list-submissions.md"
    ).read_text()

    assert "ai-boost/awesome-harness-engineering" in notes
    assert "https://github.com/ai-boost/awesome-harness-engineering/pull/23" in notes
    assert "Debugging & Developer Experience" in notes
    assert "browser-agent and computer-use runs" in notes
    assert "curl -L -s -o /dev/null" in notes


def test_awesome_list_submission_notes_record_autonomous_web_pr():
    project_root = Path(__file__).resolve().parents[1]
    notes = (
        project_root / "docs" / "launch" / "github-awesome-list-submissions.md"
    ).read_text()

    assert "Agent-Tools/awesome-autonomous-web" in notes
    assert "https://github.com/Agent-Tools/awesome-autonomous-web/pull/21" in notes
    assert "Debugging & Trace Viewers" in notes
    assert "AI browser-agent runs" in notes
    assert "awesome-lint README.md" in notes


def test_awesome_list_submission_notes_record_e2b_ai_sdks_pr():
    project_root = Path(__file__).resolve().parents[1]
    notes = (
        project_root / "docs" / "launch" / "github-awesome-list-submissions.md"
    ).read_text()

    assert "e2b-dev/awesome-ai-sdks" in notes
    assert "https://github.com/e2b-dev/awesome-ai-sdks/pull/187" in notes
    assert "creating, monitoring, debugging and deploying autonomous AI agents" in notes
    assert "verification/cla-signed" in notes
    assert "@cla-bot check" in notes


def test_targeted_outreach_copy_includes_uvx_trial_before_pypi():
    project_root = Path(__file__).resolve().parents[1]
    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )

    for relpath in [
        "docs/launch/day-3-targeted-communities-packet.md",
        "docs/launch/outreach-targets.md",
    ]:
        text = (project_root / relpath).read_text()
        assert f'uvx --from "{github_spec}" browsertrace doctor' in text, relpath
        assert f'uvx --from "{github_spec}" browsertrace demo' in text, relpath
        assert "before pypi publishing is enabled" in text.lower(), relpath


def test_owner_next_actions_include_uvx_fallback_before_pypi():
    project_root = Path(__file__).resolve().parents[1]
    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )

    for relpath in [
        "docs/launch/owner-next-actions.md",
        "docs/launch/owner-next-actions.zh-CN.md",
    ]:
        text = (project_root / relpath).read_text()
        assert f'uvx --from "{github_spec}" browsertrace demo' in text, relpath
        assert "pypi" in text.lower(), relpath


def test_launch_control_room_has_current_audit_and_uvx_fallback():
    project_root = Path(__file__).resolve().parents[1]
    github_spec = (
        'browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15'
    )
    launch = (project_root / "LAUNCH.md").read_text()

    assert "2026-05-10T11:19:35+00:00" in launch
    assert "after repo topic open-source replaced with trace-viewer" in launch
    assert f'uvx --from "{github_spec}" browsertrace doctor' in launch
    assert f'uvx --from "{github_spec}" browsertrace demo' in launch
