from appsec_toolkit.core.http import HTTPClient
from appsec_toolkit.core.models import Finding


def check_headers(url):
    client = HTTPClient()
    findings = []

    response = client.get(url)

    if not response:
        return findings

    required_headers = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Strict-Transport-Security",
    ]

    for header in required_headers:
        if header not in response.headers:
            findings.append(
                Finding(
                    type="Missing Security Header",
                    severity="LOW",
                    url=url,
                    description=f"{header} is missing",
                    evidence="Header not found",
                    remediation=f"Add {header}",
                    module="headers",
                )
            )

    return findings