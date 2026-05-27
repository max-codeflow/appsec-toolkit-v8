import argparse

from appsec_toolkit.core.validator import validate_modules
from appsec_toolkit.scanner import Scanner
from appsec_toolkit.core.crawler import Crawler
from appsec_toolkit.core.reporter import save_json_report, save_summary


def main():
    parser = argparse.ArgumentParser(description="AppSec Toolkit v8")

    parser.add_argument("command", help="scan command")
    parser.add_argument("--target", help="Target URL")
    parser.add_argument("--out-dir", default="output", help="Output directory")
    parser.add_argument("--max-pages", type=int, default=25, help="Max crawl pages")

    args = parser.parse_args()

    # -------------------------
    # 1. COMMAND CHECK
    # -------------------------
    if args.command != "scan":
        print("[!] Unknown command. Use: scan")
        return

    if not args.target:
        print("[!] Target URL is required")
        return

    print("\n[*] AppSec Toolkit v8 starting...\n")

    # -------------------------
    # 2. MODULE VALIDATION (IMPORTANT)
    # -------------------------
    valid, invalid = validate_modules()

    if not valid:
        print("\n[!] No valid modules found. Aborting scan.\n")
        return

    print(f"\n[*] Valid modules: {len(valid)}")
    if invalid:
        print(f"[!] Broken modules: {len(invalid)} (scan will continue)\n")

    # -------------------------
    # 3. CRAWLING
    # -------------------------
    print(f"[*] Crawling target: {args.target}")

    crawler = Crawler(max_pages=args.max_pages)
    urls = crawler.crawl(args.target)

    print(f"[*] Discovered URLs: {len(urls)}")

    if not urls:
        print("[!] No URLs found. Exiting.")
        return

    # -------------------------
    # 4. SCANNING
    # -------------------------
    print("[*] Scanning in progress...\n")

    scanner = Scanner()
    findings = scanner.run(urls)

    print(f"\n[*] Scan completed. Findings: {len(findings)}")

    # -------------------------
    # 5. REPORTING
    # -------------------------
    print("[*] Generating reports...")

    save_json_report(findings, args.out_dir)
    save_summary(findings, args.out_dir)

    print(f"\n[+] Done.")
    print(f"[+] Reports saved to: {args.out_dir}\n")


if __name__ == "__main__":
    main()