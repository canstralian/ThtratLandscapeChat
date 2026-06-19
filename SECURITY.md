# Security Policy

## Supported Versions

The following versions of ThreatLandscapeChat are currently being supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security issue, please report it responsibly.

### How to Report

1. **Do not** open a public GitHub issue for security vulnerabilities
2. Send a detailed report to the repository maintainers by opening a private security advisory via GitHub's [Security Advisories](https://github.com/canstralian/ThreatLandscapeChat/security/advisories/new) feature
3. Include the following information in your report:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact of the vulnerability
   - Any suggested fixes (if applicable)

### What to Expect

- **Acknowledgment**: We will acknowledge receipt of your report within 48 hours
- **Assessment**: We will assess the vulnerability and determine its severity
- **Updates**: We will keep you informed of our progress
- **Resolution**: We aim to resolve critical vulnerabilities within 30 days
- **Credit**: With your permission, we will credit you in the security advisory

### Scope

This security policy applies to:
- The main application code (`app.py`, `model_inference.py`, `prompt_engine.py`, `datasets_loader.py`)
- Configuration files
- Dependencies listed in `required.txt`

### Out of Scope

- Vulnerabilities in third-party services or dependencies (please report these to the respective maintainers)
- Social engineering attacks
- Physical security issues

## Security Best Practices

When contributing to this project, please ensure:

1. **No hardcoded credentials**: Never commit API keys, tokens, or passwords
2. **Input validation**: Always validate and sanitize user inputs
3. **Dependency management**: Keep dependencies up to date
4. **Secure coding**: Follow secure coding practices for Python

## Contact

For any security-related questions that don't involve reporting a vulnerability, please open a regular GitHub issue.

Thank you for helping keep ThreatLandscapeChat secure!
