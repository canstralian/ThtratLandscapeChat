# model_inference.py
"""Transformer-based inference wrapper for threat classification."""

from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch


class ThreatModel:
    """
    Wraps a transformer classifier for threat categorization.
    """

    def __init__(self, model_path="bert-base-chinese", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.model.to(self.device)

    def predict(self, text):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probs = torch.softmax(logits, dim=-1).cpu().tolist()[0]

        return probs  # list of probabilities per class
