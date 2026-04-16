# 🛡️ Patch Gap Auditor

![Last Commit](https://img.shields.io/github/last-commit/reory/patch_gap_auditor?cacheSeconds=60)
![Repo Size](https://img.shields.io/github/repo-size/reory/patch_gap_auditor?cacheSeconds=60)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/OSV-Audited-red)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

The Patch-Gap Auditor is a Software Composition Analysis (SCA) tool. It performs a "Digital Roll Call" of every library in your Python environment and cross-references them against Google's Open Source Vulnerabilities (OSV) database.

---

## 🧠 Why It's Used
- Supply Chain Security: 
Hackers increasingly target third-party libraries (like
requests or urllib3 ) rather than the main application code.
- Audit Readiness: 
Generates automated JSON reports required for
compliance in regulated industries (Finance, Health, Defense).
- Continuous Monitoring: 
Bridges the gap between "it worked yesterday" and
"it's vulnerable today" due to a new Zero-Day discovery.

---

# ⚒️ How to Run
- Prerequisites
```bash
pip install requests loguru
```
- Execution
```bash
python patch_gap_auditor.py
```
- The script will automatically scan your venv , query the Google OSV database
via batch request, and output a security_audit.json file.

---

# 📁 Project Structure
```
patch_gap_auditor/
├── venv/ 
├── patch_gap_auditor.py # Main logic (Harvester, Negotiator, Reporter)
├── security_audit.json # Generated audit artifact (Snapshot)
└── README.md # Project documentation
```

---

# 👨🏽‍💻 Challenges & Solutions

## API Performance: 
- Individual package queries were slow.
- Solution: Implemented the querybatch endpoint to audit all packages in a
single network round-trip.
## Environment Awareness: 
- Scanning static files (requirements.txt) often
misses sub-dependencies.
- Solution: Used importlib.metadata to query the live runtime
environment.
## Data Integrity: 
- Matching API responses to local packages.
- Solution: Leveraged the zip() function to ensure 1-to-1 mapping between
queries and results.
- Compliance: Generates a security_audit.json artifact for security logs.

---

# 🛣️ Roadmap Features

- [ ] Auto-Remediation: Add a --fix flag to automatically run pip install
--upgrade on vulnerable packages.
- [ ] Slack/Discord Integration: Send real-time alerts to dev channels when a
"Critical" vulnerability is detected.
- [ ] Historical Analysis: Compare the current audit against previous JSON
snapshots to track security improvements.
- [ ] HTML Dashboard: Visualizing the audit results in a browser-based pie chart.

---

* **Built by Roy Peters**😁

Contact details
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/roy-p-74980b382/)