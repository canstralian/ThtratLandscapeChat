# HuggingFace Spaces Deployment Guide

This document provides step-by-step instructions for deploying the APJ Threat
Intelligence System to HuggingFace Spaces.

---

## Prerequisites

1. A HuggingFace account ([signup](https://huggingface.co/join))
2. Access to the repository on GitHub
3. (Optional) A HuggingFace Access Token for private repos or API usage

---

## 1. Create a New Space

1. Navigate to [HuggingFace Spaces](https://huggingface.co/spaces)
2. Click **Create new Space**
3. Configure your Space:
   - **Owner**: Your username or organization
   - **Space name**: `ThtratLandscapeChat` (or your preferred name)
   - **License**: MIT
   - **SDK**: Gradio
   - **Hardware**: CPU Basic (free tier is sufficient for demo)
   - **Visibility**: Public or Private

---

## 2. Connect to GitHub Repository

### Option A: Automatic Sync via GitHub Actions

This repository includes a workflow (`.github/workflows/hf-sync-dev.yml`) that
automatically syncs pull requests to a development Space.

To enable it:

1. Create a HuggingFace Access Token:
   - Go to [Settings > Access Tokens](https://huggingface.co/settings/tokens)
   - Create a token with **write** permissions

2. Add the token to GitHub Secrets:
   - Go to your GitHub repository Settings > Secrets and variables > Actions
   - Add a new secret named `HF_TOKEN` with your HuggingFace token

3. Update the workflow file with your Space ID:
   ```yaml
   env:
     HF_SPACE_ID: your-username/ThtratLandscapeChat-dev
   ```

### Option B: Manual Sync via HuggingFace CLI

```bash
# Install the HuggingFace Hub CLI
pip install huggingface_hub

# Login to HuggingFace
huggingface-cli login

# Clone and push to Space
git clone https://github.com/your-username/ThtratLandscapeChat
cd ThtratLandscapeChat
git remote add space https://huggingface.co/spaces/your-username/ThtratLandscapeChat
git push space main
```

---

## 3. Configure Space Settings

### Required Files

Ensure these files exist in your repository root:

| File | Purpose |
|------|---------|
| `app.py` | Main Gradio application entry point |
| `requirements.txt` | Python dependencies |
| `README.md` | Must contain Space metadata (see below) |

### Space Metadata in README.md

The README.md must begin with YAML front matter:

```yaml
---
title: ThtratLandscapeChat
emoji: 💬
colorFrom: yellow
colorTo: purple
sdk: gradio
sdk_version: 6.0.0
app_file: app.py
pinned: false
hf_oauth: true
hf_oauth_scopes:
- inference-api
license: mit
---
```

---

## 4. Environment Variables (Optional)

If your application requires secrets (API keys, etc.):

1. Go to your Space **Settings**
2. Navigate to **Repository Secrets**
3. Add key-value pairs as needed

Access them in Python:

```python
import os

api_key = os.environ.get("MY_API_KEY")
```

---

## 5. Using HuggingFace Models

The Intelligence Console can leverage HuggingFace models for:

- Threat classification
- Language translation
- Text embeddings

### Example: Using Inference API

```python
from huggingface_hub import InferenceClient

client = InferenceClient(token="hf_xxx")
result = client.text_classification("可疑文本")
```

### Example: Local Transformers

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="bert-base-chinese")
result = classifier("input text")
```

---

## 6. Monitoring & Logs

- View runtime logs in the **Logs** tab of your Space
- Monitor resource usage in the **Settings** tab
- Enable persistent storage if needed for caching models

---

## 7. Upgrading Hardware

For production workloads or large models:

1. Go to Space **Settings**
2. Under **Hardware**, select a higher tier (GPU, etc.)
3. Note: Upgraded hardware incurs costs

---

## 8. Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Build fails | Check `requirements.txt` for valid packages |
| App crashes | Review logs for Python errors |
| Slow startup | Reduce model size or enable caching |
| Out of memory | Upgrade hardware or optimize code |

### Useful Commands

```bash
# Rebuild Space
huggingface-cli repo create --type space -n your-space --rebuild

# Check Space status
huggingface-cli repo info spaces/your-username/your-space
```

---

## 9. Best Practices

1. **Pin dependency versions** in `requirements.txt`
2. **Use environment variables** for secrets
3. **Test locally** before pushing to Space
4. **Enable auto-rebuild** for continuous deployment
5. **Monitor logs** for errors and performance issues

---

## Resources

- [HuggingFace Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [Gradio Documentation](https://gradio.app/docs/)
- [HuggingFace Hub Python Library](https://huggingface.co/docs/huggingface_hub/)

---

## Support

For issues with this repository, please open a GitHub issue.
For HuggingFace Spaces issues, consult the
[HuggingFace Forum](https://discuss.huggingface.co/).
