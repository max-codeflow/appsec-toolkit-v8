# 🏗 AppSec Toolkit v8 — Architecture

## Overview

AppSec Toolkit is a modular Application Security scanning framework designed to simulate real-world security tooling.

It follows a clean separation of concerns between crawling, scanning, detection modules, and reporting.

---

## 🔄 System Flow


Target URL
↓
Crawler (scope-limited discovery)
↓
HTTP Client (request abstraction layer)
↓
Scanner Engine (orchestration layer)
↓
Modules (security checks)
↓
Findings Model (normalized schema)
↓
Reporter (output generation)
↓
Artifacts (JSON / TXT reports)


---

## 🧩 Core Components

### 1. CLI Layer
- Entry point for scan execution
- Parses arguments and config
- Starts scanning pipeline

---

### 2. Crawler
- Discovers in-scope URLs
- Prevents external domain leakage
- Limits crawl size and depth

---

### 3. HTTP Client
- Centralized request handling
- Timeout management
- Consistent headers (User-Agent, etc.)

---

### 4. Scanner Engine
- Orchestrates module execution
- Collects findings
- Handles module errors safely

---

### 5. Modules (Plugins)

Independent vulnerability detection components:

| Module  | Purpose |
|--------|--------|
| headers | Missing security headers detection |
| xss     | Reflected input analysis |
| sqli    | SQL injection indicators |
| secrets | Sensitive data exposure detection |
| jwt     | JWT risk and misconfiguration analysis |

---

### 6. Findings Model
Normalized vulnerability structure:

- type
- severity
- url
- evidence
- remediation
- module

---

### 7. Reporter
- Generates `report.json`
- Generates `summary.txt`
- Aggregates findings statistics

---

## 🎯 Design Principles

- Modular architecture (plugin-based checks)
- Separation of concerns (core vs modules)
- Reproducible execution pipeline
- Structured output format
- Easy extensibility for new security checks

---

## 📦 Output Structure


output/
├── report.json # structured findings
└── summary.txt # human-readable summary


---

## ⚠️ Security Notice

This tool is intended for educational and authorized security testing purposes only.