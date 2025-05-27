#!/usr/bin/env python3
import sys
import re
from datetime import datetime

def parse_log_line(line):
    # Simple parser for timestamp + event summary
    # Handles syslog and sysmon formats (basic)
    timestamp_regex = r'^([A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2})'
    sysmon_regex = r'^<\d+>1 (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)'

    ts_match = re.match(timestamp_regex, line)
    if ts_match:
        ts_str = ts_match.group(1)
        ts = datetime.strptime(ts_str, '%b %d %H:%M:%S')
        event = line[ts_match.end():].strip()
        return (ts.strftime('%Y-%m-%d %H:%M:%S'), event)
    ts_match = re.match(sysmon_regex, line)
    if ts_match:
        ts_str = ts_match.group(1)
        ts = datetime.strptime(ts_str, '%Y-%m-%dT%H:%M:%SZ')
        event = line[ts_match.end():].strip()
        return (ts.strftime('%Y-%m-%d %H:%M:%S'), event)
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: timeline_gen.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]
    timeline = []

    with open(logfile, 'r', errors='ignore') as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                timeline.append(parsed)

    timeline.sort(key=lambda x: x[0])

    print("# Incident Timeline\n")
    for ts, event in timeline:
        print(f"- **{ts}**: {event}")

if __name__ == "__main__":
    main()
