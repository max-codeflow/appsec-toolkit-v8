from appsec_toolkit.core.models import Finding
import re


SECRET_PATTERNS = [
    r"api_key\s*=\s*['\"][A-Za-z0-9_\-]{10,}['\"]",
    r"secret\s*=\s*['\"][A-Za-z0-9_\-]{10,}['\"]",
    r"token\s*=\s*['\"][A-Za-z0-9_\-]{10,}['\"]",
]


def check_secrets(url):
    findings = []

    try:
        import requests
        r = requests.get(url, timeout=5)

        text = r.text.lower()

        for pattern in SECRET_PATTERNS:
            if re.search(pattern, text):
                findings.append(
                    Finding(
                        type="Possible Secret Exposure",
                        severity="HIGH",
                        url=url,
                        description="Sensitive pattern detected in response",
                        evidence=pattern,
                        remediation="Remove secrets from client-side responses",
                        module="secrets",
                    )
                )

    except Exception:
        pass

    return findings