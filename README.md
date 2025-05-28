# SIEM Log Analysis Lab (Mini-SOC Simulator) 

A practical, hands-on SOC simulation designed to develop skills in log analysis, threat detection, and incident response. Completed as part of a class assignment, this project offers realistic scenarios for practicing critical SOC functions. Please note that the work may be incomplete or somewhat outdated, as it was recently recovered from archived materials.

---

## Project Overview

This lab simulates common SOC workflows using sample logs from Windows, Linux, and web servers. You can practice:

- Analyzing logs with Splunk SPL queries
- Detecting brute force attempts, privilege escalation, and suspicious PowerShell activity
- Following incident response playbooks
- Generating incident timelines from log data

---

## Directory Structure

```
siem-log-analysis-lab/
├── logs/
│   ├── windows/sysmon_logs.txt
│   ├── linux/auth.log
│   └── web/access.log
├── detections/
│   ├── failed_login.spl
│   ├── privilege_escalation.spl
│   └── suspicious_powershell.spl
├── playbooks/
│   ├── brute_force.md
│   ├── malware_execution.md
│   └── lateral_movement.md
├── screenshots/
│   └── dashboard_placeholder.png
├── timeline-generator/
│   └── timeline_gen.py
└── README.md
```

---

## How to Use

1. Load logs into your SIEM tool (Splunk, ELK, etc.).
2. Run SPL queries in the /detections folder to identify suspicious activity.
3. Follow response steps in /playbooks for each alert type.
4. Use the timeline generator to produce incident timelines.

---

## Technologies Used

- Splunk SPL queries
- Windows Sysmon event logs
- Linux syslogs
- Apache web logs
- Python scripting

---

## Author

Nicholas D'Acri  
Cybersecurity Researcher | SOC & Threat Detection | Python & Splunk
