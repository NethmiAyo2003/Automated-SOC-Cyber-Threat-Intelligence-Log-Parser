# Automated SOC Cyber Threat Intelligence & Log Parser

A Python-based **SIEM / SOAR (Security Orchestration, Automation, and Response)** automation script designed for Security Operations Center (SOC) environments. This tool automates the process of parsing massive server infrastructure logs, detecting security incidents via Regular Expressions (Regex), cross-matching source IPs with Threat Intelligence databases, and generating automated structured incident reports.

## ✨ Key Features
* **Log Management & Parsing:** Ingests raw server log streams and utilizes optimized `Regular Expressions (Regex)` to extract critical metadata such as Source IP addresses, HTTP status codes, and message strings.
* **Threat Intelligence Integration:** Automatically cross-references extracted external IPs against a simulated Cyber Threat Intel database to instantly identify known malicious hosts, botnets, and scanning entities.
* **Automated Incident Response (SOAR):** Automatically triggers high-severity security alerts (`CRITICAL` / `MALICIOUS`) based on indicator matches, tracking the attacker's country of origin and vector type.
* **Structured Report Generation:** Programmatically outputs a comprehensive, production-ready security report in `JSON` format (`security_incident_report.json`) for audit trails and management reviews.

## 🚀 How It Works & Execution
Execute the script natively within a Linux terminal:
```bash
python3 soc_automation.py
