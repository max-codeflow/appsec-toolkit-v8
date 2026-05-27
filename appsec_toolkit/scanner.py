from appsec_toolkit.modules.headers import check_headers
from appsec_toolkit.modules.jwt import check_jwt
from appsec_toolkit.modules.secrets import check_secrets
from appsec_toolkit.modules.xss import check_xss
from appsec_toolkit.modules.sqli import check_sqli


class Scanner:
    def __init__(self):
        # registry of modules (plugin-style)
        self.modules = [
            check_headers,
            check_jwt,
            check_secrets,
            check_xss,
            check_sqli,
        ]

    def run(self, urls):
        findings = []

        for url in urls:
            for module in self.modules:
                try:
                    result = module(url)

                    # normalize module output
                    if result:
                        if isinstance(result, list):
                            findings.extend(result)
                        else:
                            findings.append(result)

                except Exception as e:
                    # never crash whole scan because of one module
                    print(f"[MODULE ERROR] {module.__name__}: {e}")
                    continue

        return findings