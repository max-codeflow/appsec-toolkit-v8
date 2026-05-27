# 🛡 AppSec Toolkit v8

A modular Application Security scanning engine for crawling, vulnerability detection, and security reporting.

Designed for learning real-world AppSec engineering:
- web crawling
- vulnerability scanning
- plugin-based architecture
- structured reporting

---

# 🚀 Features

## 🧭 Crawling Engine
- URL discovery
- same-domain filtering
- depth-limited scanning

## 🧩 Security Modules
- Security headers analysis
- JWT inspection (basic validation checks)
- Secrets detection (regex-based)
- Reflected XSS detection (heuristic)
- SQLi detection (error-based signals)

## 📊 Reporting
- JSON structured report
- human-readable summary
- grouped findings by severity

---

# ⚙️ Installation

```bash
git clone https://github.com/max-codeflow/appsec-toolkit-v8.git
cd appsec-toolkit-v8

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

🚀 Usage

python appsec_toolkit/cli.py scan \
  --target https://example.com \
  --max-pages 25 \
  --out-dir output
📦 Output
output/
├── report.json
└── summary.txt

🧠 Architecture

Modular design:

CLI → Crawler → Scanner → Modules → Reporter

Each module is independent and extendable.

See docs/ARCHITECTURE.md for details.

🎯 Design Goals

clean modular architecture
extensibility via modules
reproducible scanning pipeline
educational AppSec simulation tool

⚠️ Disclaimer

This tool is intended for educational and authorized security testing only.
Do not use it on systems without permission.