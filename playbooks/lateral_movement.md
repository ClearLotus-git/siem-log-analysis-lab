# Lateral Movement Response Playbook

## Detection

- Use of remote admin tools such as PsExec or net use.
- New administrative logins on multiple hosts.

## Response Steps

1. Identify source host and impacted hosts.
2. Review authentication and authorization logs.
3. Block lateral traffic at network segmentation points.
4. Notify the incident response team.
5. Conduct a full internal network scan for other compromised hosts.
6. Change all privileged account credentials.
