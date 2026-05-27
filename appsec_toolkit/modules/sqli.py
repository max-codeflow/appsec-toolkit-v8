from appsec_toolkit.core.models import Finding
import requests


def check_sqli(url):
    findings = []

    payload = "' OR '1'='1"

    try:
        r = requests.get(url, params={"id": payload}, timeout=5)

        errors = [
            "sql syntax",
            "mysql",
            "postgres",
            "sqlite",
            "database error",
        ]

        response_text = r.text.lower()

        if any(err in response_text for err in errors):
            findings.append(
                Finding(
                    type="SQL Injection (Error-based)",
                    severity="HIGH",
                    url=url,
                    description="Possible SQL error leakage detected",
                    evidence="Database error keywords found",
                    remediation="Use parameterized queries",
                    module="sqli",
                )
            )

    except Exception:
        pass

    return findings
