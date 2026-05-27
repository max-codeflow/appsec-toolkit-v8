# 🛡 AppSec Toolkit v8

A modular Application Security scanning framework designed for learning security engineering, automation, and vulnerability research.

It simulates real-world AppSec tooling architecture: crawler, scanner engine, plugin-based detection modules, structured findings, and reproducible CLI workflows.

---

## 🚀 Features

- Modular plugin-based architecture for security checks  
- Bounded crawler with scope control  
- Unified HTTP client layer  
- Structured findings schema (severity, evidence, remediation)  
- CLI-driven scanning workflow  
- JSON + human-readable reporting  
- Extensible design for custom modules  

---

## ⚙️ Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r v8/requirements.txt

🚀 Usage

Basic scan
python -m v8.appsec_toolkit.cli scan --target "https://example.com" --out-dir output
Config-based scan
python -m v8.appsec_toolkit.cli scan --config examples/config.json

📦 Output

After execution, results are stored in:

output/
├── report.json
└── summary.txt

🧠 Architecture

See docs/ARCHITECTURE.md

🧩 Modules

Module	Purpose
headers	Missing security headers detection
xss	Reflected input analysis
sqli	SQL injection indicators
secrets	Sensitive data exposure detection
jwt	JWT risk and misconfiguration analysis

🎯 Design Goals

Separation of concerns (core vs modules)
Reproducible scanning pipeline
Structured findings schema
Extensible security research framework
CLI-first design

⚠️ Disclaimer

This tool is intended for educational and authorized security testing purposes only.