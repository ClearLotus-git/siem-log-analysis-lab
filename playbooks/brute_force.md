# Brute Force Attack Response Playbook

## Detection

- Multiple failed login attempts detected from the same IP address.
- Unusual user login patterns.

## Response Steps

1. Identify the source IP address involved.
2. Block the offending IP on firewall and IDS.
3. Review logs for any successful access following failed attempts.
4. Notify the security team and affected users.
5. Increase monitoring on targeted accounts.
6. Review and tighten account lockout policies.
