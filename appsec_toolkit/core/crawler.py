import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


class Crawler:
    def __init__(self, max_pages=25, timeout=5):
        self.max_pages = max_pages
        self.timeout = timeout
        self.visited = set()

    def crawl(self, base_url):
        to_visit = [base_url]

        while to_visit and len(self.visited) < self.max_pages:
            url = to_visit.pop()

            if url in self.visited:
                continue

            try:
                response = requests.get(
                    url,
                    timeout=self.timeout,
                    headers={"User-Agent": "AppSecToolkit/v8"},
                )

                self.visited.add(url)

                soup = BeautifulSoup(response.text, "html.parser")

                for a in soup.find_all("a", href=True):
                    full_url = urljoin(base_url, a["href"])

                    # stay in same domain
                    if self._is_same_domain(base_url, full_url):
                        to_visit.append(full_url)

            except Exception:
                continue

        return list(self.visited)

    def _is_same_domain(self, base, url):
        return urlparse(base).netloc == urlparse(url).netloc