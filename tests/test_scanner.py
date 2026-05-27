from appsec_toolkit.scanner import Scanner


def test_scanner_runs():
    scanner = Scanner()

    urls = ["https://example.com"]

    findings = scanner.run(urls)

    assert isinstance(findings, list)