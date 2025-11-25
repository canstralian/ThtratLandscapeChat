#!/usr/bin/env python3
"""Script to update the PR checklist with project status."""

import os
from datetime import datetime, timezone


def get_checklist_content() -> str:
    """Generate the PR checklist content with current status."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    checklist = f"""# PR Checklist

Last updated: {timestamp}

## Code Quality
- [ ] Code follows project style guidelines
- [ ] No linting errors
- [ ] Tests pass locally

## Documentation
- [ ] README updated if needed
- [ ] Code comments added for complex logic

## Security
- [ ] No secrets committed
- [ ] Dependencies checked for vulnerabilities

## Review
- [ ] Self-review completed
- [ ] Ready for peer review
"""
    return checklist


def main() -> None:
    """Main function to update the PR checklist file."""
    # Get the repository root (parent of scripts directory)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    checklist_path = os.path.join(repo_root, "PR_Checklist.md")

    content = get_checklist_content()

    with open(checklist_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated {checklist_path}")


if __name__ == "__main__":
    main()
