import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "Expected /app/report.json to be created"
    try:
        return json.loads(REPORT_PATH.read_text())
    except json.JSONDecodeError as exc:
        raise AssertionError("report.json must contain valid JSON") from exc


def test_report_has_exact_schema():
    """Verifies instruction criterion: report.json has exactly total_requests, unique_ips, and top_path."""
    report = load_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"
    assert set(report.keys()) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Verifies instruction criterion: total_requests is the number of non-blank log lines."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Verifies instruction criterion: unique_ips is the number of distinct client IP addresses."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Verifies instruction criterion: top_path is the most frequent request path with alphabetical tie-breaking."""
    report = load_report()
    assert report["top_path"] == "/index.html"
