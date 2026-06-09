import re
import json
from datetime import datetime

# 1. Mock Server Logs 
server_logs = [
    '2026-06-10 10:15:30 | IP: 192.168.1.50 | STATUS: 200 | MSG: Login Successful',
    '2026-06-10 10:16:22 | IP: 185.220.101.5 | STATUS: 401 | MSG: Failed Login Attempt - Warning',
    '2026-06-10 10:17:05 | IP: 192.168.1.55 | STATUS: 200 | MSG: Dashboard Opened',
    '2026-06-10 10:18:12 | IP: 45.145.185.10 | STATUS: 403 | MSG: SQL Injection Detected in URL',
    '2026-06-10 10:19:00 | IP: 185.220.101.5 | STATUS: 401 | MSG: Failed Login Attempt - Warning'
]

# Known Threat Intel Database 
threat_intel_db = {
    "185.220.101.5": {"status": "MALICIOUS", "country": "Russia", "type": "Brute Force Botnet"},
    "45.145.185.10": {"status": "CRITICAL", "country": "Unknown", "type": "Exploit Scanner"}
}

def analyze_logs():
    print("=" * 60)
    print(f"🚀 SOC AUTOMATION & LOG PARSER SCRIPT STARTED")
    print(f"⏱️ Timestamp: {datetime.now()}")
    print("=" * 60)
    
    security_alerts = []

    # 2. Log Management & Parsing 
    for log in server_logs:
        # IP 
        ip_match = re.search(r'IP:\s([\d\.]+)', log)
        if ip_match:
            ip = ip_match.group(1)
            
            # 3. Automation Logic
            if ip in threat_intel_db:
                intel = threat_intel_db[ip]
                alert = {
                    "timestamp": log.split(' | ')[0],
                    "attacker_ip": ip,
                    "severity": intel["status"],
                    "country": intel["country"],
                    "attack_type": intel["type"],
                    "raw_log": log
                }
                security_alerts.append(alert)
                print(f"[🚨 ALERT - {intel['status']}] Threat Found from {ip} ({intel['country']}) -> {intel['type']}")

    # 4. Automated Report Generation 
    report_data = {
        "scan_info": {"total_logs_analyzed": len(server_logs), "alerts_triggered": len(security_alerts)},
        "alerts": security_alerts
    }
    
    with open("security_incident_report.json", "w") as f:
        json.dump(report_data, f, indent=4)
        
    print("=" * 60)
    print("✨ SEC_REPORT GENERATED: security_incident_report.json")
    print("=" * 60)

if __name__ == "__main__":
    analyze_logs()
