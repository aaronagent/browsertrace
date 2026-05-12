"""Tests for the launch metrics helper script."""

from __future__ import annotations

from datetime import datetime, timezone


def test_collect_snapshot_calculates_goal_and_release_downloads():
    from scripts import launch_metrics

    def fake_runner(args: list[str]):
        if args[:2] == ["repo", "view"]:
            return {
                "stargazerCount": 42,
                "forkCount": 5,
                "watchers": {"totalCount": 3},
                "issues": {"totalCount": 7},
                "pullRequests": {"totalCount": 2},
                "url": "https://github.com/aaronlab/browsertrace",
            }
        if args[:1] == ["api"]:
            if args[1].endswith("/traffic/views"):
                return {"count": 48, "uniques": 25}
            if args[1].endswith("/traffic/clones"):
                return {"count": 100, "uniques": 52}
            return {
                "assets": [
                    {"name": "browsertrace-demo.html", "download_count": 10},
                    {"name": "demo.mp4", "download_count": 4},
                ]
            }
        raise AssertionError(f"unexpected args: {args}")

    snapshot = launch_metrics.collect_snapshot(
        runner=fake_runner,
        now=datetime(2026, 5, 9, 8, 30, tzinfo=timezone.utc),
    )

    assert snapshot.captured_at == "2026-05-09T08:30:00+00:00"
    assert snapshot.stars == 42
    assert snapshot.stars_to_goal == 959
    assert snapshot.goal_status == "incomplete"
    assert snapshot.release_downloads == 14
    assert snapshot.release_assets == 2
    assert snapshot.traffic_views == 48
    assert snapshot.traffic_view_uniques == 25
    assert snapshot.traffic_clones == 100
    assert snapshot.traffic_clone_uniques == 52


def test_default_launch_metrics_release_tag_matches_current_release():
    from scripts import launch_metrics

    assert launch_metrics.RELEASE_TAG == "v0.1.18"


def test_markdown_row_escapes_note_separator():
    from scripts import launch_metrics

    snapshot = launch_metrics.LaunchSnapshot(
        captured_at="2026-05-09T08:30:00+00:00",
        repo="aaronlab/browsertrace",
        url="https://github.com/aaronlab/browsertrace",
        stars=3,
        forks=0,
        watchers=0,
        issues=3,
        pull_requests=0,
        release_tag="v0.1.12",
        release_downloads=6,
        release_assets=4,
        traffic_views=48,
        traffic_view_uniques=25,
        traffic_clones=100,
        traffic_clone_uniques=52,
        stars_to_goal=998,
        goal_status="incomplete",
        note="after X | LinkedIn",
    )

    assert (
        launch_metrics.markdown_row(snapshot)
        == "| 2026-05-09T08:30:00+00:00 | 3 | 998 | 0 | 0 | 3 | 0 | 6 | after X \\| LinkedIn; traffic views 48/25 unique, clones 100/52 unique |"
    )
