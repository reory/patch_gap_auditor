# 🛡️ Patch Gap Auditor

![Last Commit](https://img.shields.io/github/last-commit/reory/patch_gap_auditor?cacheSeconds=60)
![Repo Size](https://img.shields.io/github/repo-size/reory/patch_gap_auditor?cacheSeconds=60)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/OSV-Audited-red)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

The Patch-Gap Auditor is a Software Composition Analysis (SCA) tool. It performs a "Digital Roll Call" of every library in your Python environment and cross-references them against Google's Open Source Vulnerabilities (OSV) database.

---

## 📑 Table of Contents

- [Why This Project Exists](#-why-this-project-exists)
- [Key Features](#-key-features)
- [Installation & Setup](#️-installation--setup)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Challenges & Solutions](#-challenges--solutions)
- [Roadmap Features](#️-roadmap)

---

## 🎯 Why This Project Exists

Modern applications often depend on dozens or even hundreds of third-party packages.

Whilst these dependencies accelerate development, they can also introduce known vulnerabilities into a system without developers being aware.

Patch Gap Auditor was created to provide a lightweight Software Composition Analysis (SCA) solution capable of auditing a live Python environment against Google's Open Source Vulnerabilities (OSV) database and producing actionable security reports.

---

## ✨ Key Features

- Automatic package inventory discovery
- Runtime environment inspection
- Google OSV integration
- Batch vulnerability lookups
- JSON audit report generation
- Security compliance support
- Software supply chain analysis
- Dependency vulnerability detection

---

## 🛠️ Installation & Setup

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the auditor:

- Execution
```bash
python patch_gap_auditor.py
```
The tool will:

- Discover installed packages.
- Collect package version metadata.
- Query the OSV database.
- Match vulnerabilities against installed components.
- Generate a structured audit report.
- Export findings to security_audit.json.

---

## 📁 Project Structure
```
patch_gap_auditor/
├── venv/ 
├── patch_gap_auditor.py   # Main logic (Harvester, Negotiator, Reporter)
├── security_audit.json    # Generated audit artefact (Snapshot)
└── README.md              # Project documentation
```

---

## 👨🏽‍💻 Tech Stack

### Python 
- Core application and security tooling. 
### Requests 
- Handles communication with Google's OSV API. 
### Loguru 
- Structured logging and diagnostic output. 
### OSV API 
- Provides vulnerability intelligence for open-source packages. 
### JSON 
- Used for report generation and audit artefacts.

---

## 👨🏽‍💻 Challenges & Solutions

### API Performance: 
- Individual package queries were slow.
- Solution: Implemented the querybatch endpoint to audit all packages in a
single network round-trip.

### Environment Awareness:
- Scanning static files (requirements.txt) often
misses sub-dependencies.
- Solution: Used importlib.metadata to query the live runtime
environment.

### Data Integrity: 
- Matching API responses to local packages.
- Solution: Leveraged the zip() function to ensure 1-to-1 mapping between
queries and results.
- Compliance: Generates a security_audit.json artifact for security logs.

---

## 🛣️ Roadmap Features

- [ ] Historical analysis and snapshot comparison
- [ ] HTML dashboard visualisations
- [ ] Slack and Discord notifications
- [ ] CVSS severity filtering
- [ ] CSV export support
- [ ] GitHub Actions integration
- [ ] pyproject.toml auditing

---

* **Built by Roy Peters**😁

Contact details
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/roy-p-74980b382/)