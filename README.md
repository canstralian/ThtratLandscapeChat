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

# APJ Threat Intelligence System  
Mobile-First, Multilingual Cybercrime Intelligence Platform

## Overview
This project delivers a full-stack threat-intelligence console focused on
Asia-Pacific & Japan (APJ) cybercrime ecosystems. The system ingests
Mandarin/Cantonese underground-market chatter, interprets idioms and cultural
nuances, classifies threats using transformer models, and presents insights to
analysts through a mobile-first Gradio interface.

The design is modular, allowing you to use:
- Local Transformers models (HuggingFace)
- External LLM APIs
- Custom datasets
- A growing slang / idiom lexicon
- Marketplace monitoring pipelines

This repository is optimized for **GitHub** and **HuggingFace Spaces**.

---

## ✨ Features

### 🔍 Intelligence Layer
- Threat classification (Transformers)
- Vendor graph modeling
- Marketplace and trend analysis
- Slang & idiom identification

### 🌏 Multilingual Processing
- Mandarin + Cantonese dialect detection  
- Literal + functional translation  
- Cultural interpretation for cybercrime slang  

### 📱 Mobile-First UI
Built with Gradio 4.x:
- Single-column layout  
- Mode switcher (Threat Intel / Translation / Marketplace Watch / Analyst Tools)  
- File upload for logs, screenshots, raw text  
- Downloadable chat transcripts  
- Clean UX optimized for mobile operators  

### 🔧 Built With
- `transformers`
- `datasets`
- `gradio`
- Python 3.10+

---

## 🧩 Repository Structure

.
├── app.py                   # Main Gradio app
├── prompt_engine.py         # Centralized prompt construction
├── model_inference.py       # Transformers-based inference wrapper
├── datasets_loader.py       # HuggingFace datasets loader utilities
├── slang_lexicon.json       # Evolving idiom/slang dictionary
├── PROJECT_SPEC.md          # Architectural overview
├── HUGGINGFACE.md           # HF Spaces deployment instructions
├── GITHUB_SETUP.md          # Repo usage & development guide
├── requirements.txt
└── README.md

---

## 🚀 Running Locally

### 1. Clone the repo
```bash
git clone https://github.com/<yourname>/apj-threat-intel
cd apj-threat-intel

2. Install requirements

pip install -r requirements.txt

3. Launch the app

python app.py

The interface opens automatically in your browser.

⸻

🧠 Model Integration

You can plug your own HuggingFace model into model_inference.py:

ThreatModel(model_path="your-model-name")

Or use an API-driven LLM via prompt_engine.py.

⸻

🌐 Deploy on HuggingFace Spaces

See HUGGINGFACE.md in this repo for step-by-step instructions.

⸻

📄 Docs
	•	Project Spec￼
	•	HF Spaces Setup￼
	•	GitHub Setup Guide￼

⸻

📜 License

MIT (You may swap this with your preferred license.)

⸻

🤝 Contributing

Pull requests and issue reports are welcome.

⸻

🧭 Roadmap
	•	Vendor identity resolution model
	•	Marketplace scraping connectors
	•	Cantonese pretrained language model fine-tuning
	•	In-browser graph explorer
	•	Real-time alerting engine

⸻

✉️ Contact

For questions, enhancements, or collaboration, open an issue.

---
