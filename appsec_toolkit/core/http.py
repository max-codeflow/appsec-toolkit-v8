import requests


class HTTPClient:
    def __init__(self, timeout=5):
        self.timeout = timeout

    def get(self, url, params=None):
        try:
            response = requests.get(
                url,
                params=params,
                timeout=self.timeout,
                headers={"User-Agent": "AppSecToolkit/v8"},
            )
            return response

        except requests.RequestException as e:
            print(f"[HTTP ERROR] {e}")
            return None