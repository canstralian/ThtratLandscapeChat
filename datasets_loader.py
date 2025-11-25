# datasets_loader.py
"""Dataset loading utilities for threat intelligence data."""

from datasets import load_dataset, DatasetDict
from transformers import AutoTokenizer


def load_threat_dataset(path: str, tokenizer_name="bert-base-chinese"):
    """
    Loads a dataset of Chinese cybercrime posts with labels.
    Expects columns: text, label
    """
    raw = load_dataset("csv", data_files=path)

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    def tokenize(batch):
        return tokenizer(
            batch["text"],
            truncation=True,
            padding="max_length",
            max_length=256
        )

    tokenized = raw.map(tokenize, batched=True)

    return DatasetDict({
        "train": tokenized["train"],
        "test": tokenized["test"]
    })


# Example:
# ds = load_threat_dataset("dataset/threat_samples.csv")
# print(ds["train"][0])
