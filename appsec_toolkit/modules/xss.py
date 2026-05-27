from appsec_toolkit.core.models import Finding
import requests


def check_xss(url):
    findings = []

    payload = "<script>alert(1)</script>"

    try:
        r = requests.get(url, params={"q": payload}, timeout=5)

        if payload in r.text:
            findings.append(
                Finding(
                    type="Reflected XSS",
                    severity="HIGH",
                    url=url,
                    description="Reflected XSS payload detected in response",
                    evidence=payload,
                    remediation="Sanitize and encode user input",
                    module="xss",
                )
            )

    except Exception:
        pass

    return findings
