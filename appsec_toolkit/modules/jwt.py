import re
import jwt

from appsec_toolkit.core.http import HTTPClient
from appsec_toolkit.core.models import Finding


JWT_REGEX = r"eyJ[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+"


client = HTTPClient()


def check_jwt(url):
    findings = []

    response = client.get(url)

    if not response:
        return findings

    matches = re.findall(JWT_REGEX, response.text)

    for token in matches:
        try:
            decoded = jwt.decode(
                token,
                options={"verify_signature": False},
                algorithms=["HS256", "none"],
            )

            findings.append(
                Finding(
                    type="JWT Token Detected",
                    severity="MEDIUM",
                    url=url,
                    description="JWT token discovered in HTTP response",
                    evidence=token[:40] + "...",
                    remediation="Avoid exposing sensitive JWTs in responses",
                    module="jwt",
                )
            )

            header = jwt.get_unverified_header(token)

            if header.get("alg") == "none":
                findings.append(
                    Finding(
                        type="Insecure JWT Algorithm",
                        severity="HIGH",
                        url=url,
                        description='JWT uses insecure "none" algorithm',
                        evidence=str(header),
                        remediation="Disallow unsigned JWT tokens",
                        module="jwt",
                    )
                )

        except Exception:
            continue

    return findings