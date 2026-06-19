# GitHub Repository Setup Guide

This document explains how to structure, develop, and maintain the
ThreatLandscapeChat / APJ Threat Intelligence System on GitHub.

---

## 1. Repository Description

**ThreatLandscapeChat** is a mobile-first, multilingual cybercrime intelligence platform focused on Asia-Pacific & Japan (APJ) threat landscapes. The system interprets Mandarin/Cantonese underground-market chatter, classifies threats using transformer models, and presents actionable insights through an intuitive Gradio interface.

---

## 2. Repository Topics/Tags

The following topics should be added to the repository for better discoverability:

- `threat-intelligence`
- `cybersecurity`
- `nlp`
- `transformers`
- `gradio`
- `machine-learning`
- `python`
- `huggingface`
- `apj`
- `multilingual`

To add topics:
1. Go to the repository's main page
2. Click the gear icon next to "About"
3. Add the topics listed above

---

## 3. Clone & Install

```bash
git clone https://github.com/canstralian/ThreatLandscapeChat
cd ThreatLandscapeChat
pip install -r required.txt
```

---

## 4. Recommended Repository Structure

```
├── app.py                   # Main Gradio application
├── prompt_engine.py         # Centralized prompt construction
├── model_inference.py       # Transformers-based inference wrapper
├── datasets_loader.py       # HuggingFace datasets loader utilities
├── slang_lexicon.json       # Evolving idiom/slang dictionary
├── PROJECT_SPEC.md          # Architectural overview
├── GITHUB_SETUP.md          # Repo usage & development guide
├── SECURITY.md              # Security policy
├── required.txt             # Python dependencies
└── README.md
```

---

## 5. Branching Strategy

### Main Branch (`main`)
- **Purpose**: Always deployable / stable production code
- **Protection**: Requires pull request reviews before merging
- **Auto-sync**: HuggingFace Space can auto-sync from `main`
- **Direct pushes**: Disabled for all contributors except administrators

### Development Branch (`dev`)
- **Purpose**: Active development and integration branch
- **Merge target**: Feature branches merge into `dev` via PR
- **Testing**: All new features should be tested here before `main`

### Feature Branches
- **Naming convention**: `feature/<feature-name>` (e.g., `feature/vendor-graph`)
- **Lifecycle**: Created from `dev`, merged back into `dev` via PR
- **Cleanup**: Deleted after successful merge

### Hotfix Branches
- **Naming convention**: `hotfix/<issue-description>`
- **Purpose**: Critical production fixes
- **Merge target**: Both `main` and `dev`

### Branch Flow

```
main ←────────────────────────────────────────┐
  ↑                                           │
  │ (PR with review)                          │ (hotfix)
  │                                           │
dev ←─────────────┬───────────────────────────┤
  ↑               ↑                           │
  │ (PR)          │ (PR)                      │
  │               │                           │
feature/a     feature/b                   hotfix/x
```

---

## 6. Branch Protection Rules

Recommended branch protection settings for `main`:

| Setting | Value |
|---------|-------|
| Require pull request reviews | ✅ Enabled |
| Required approving reviews | 1 |
| Dismiss stale reviews | ✅ Enabled |
| Require status checks | ✅ Enabled |
| Require branches to be up to date | ✅ Enabled |
| Include administrators | ✅ Enabled |

To configure:
1. Go to **Settings** → **Branches**
2. Click **Add branch protection rule**
3. Enter `main` as the branch name pattern
4. Configure the settings above

---

## 7. Security

See [SECURITY.md](SECURITY.md) for:
- Supported versions
- How to report vulnerabilities
- Security best practices

---

## 8. Adding New Components

### New Mode
To add a new mode to the application:
1. Create the component in a new Python file
2. Register the mode in `app.py`
3. Update the prompt templates in `prompt_engine.py`
4. Add any new dependencies to `required.txt`
5. Document the new mode in `PROJECT_SPEC.md`

### New Dependencies
1. Add the package to `required.txt`
2. Run `pip install -r required.txt` to verify installation
3. Dependabot will automatically monitor for security updates

---

## 9. Contributing

1. Fork the repository
2. Create a feature branch from `dev`
3. Make your changes
4. Submit a pull request to `dev`
5. Ensure all checks pass
6. Request review from maintainers

---

## 10. Issue Tracking

Use GitHub Issues for:
- Bug reports
- Feature requests
- Documentation improvements

Label your issues appropriately:
- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `security` - Security-related issues (see SECURITY.md for vulnerabilities)