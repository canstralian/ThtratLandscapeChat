# prompt_engine.py
"""Centralized prompt construction for the intelligence system."""

from textwrap import dedent


class PromptEngine:
    """
    Centralized prompt builder for the intelligence system.
    """

    def __init__(self):
        self.system_context = dedent("""
        You are an intelligence interpreter focused on APJ cybercrime signals.
        You read Mandarin, Cantonese, and English, and convert them into
        structured threat intelligence with cultural nuance preserved.
        """)

    def classify_threat(self, text):
        return dedent(f"""
        {self.system_context}

        TASK:
        Classify the following text into one or more categories:
        - stolen_data
        - malware_service
        - laundering_service
        - access_broker
        - scam_indicator
        - unknown

        Also extract:
        - slang terms
        - vendor signals
        - action verbs (buying, selling, promoting)
        - risk level (1–5)

        TEXT:
        {text}
        """)

    def translate_explain(self, text):
        return dedent(f"""
        {self.system_context}

        TASK:
        Translate this Mandarin/Cantonese text into English.
        Then explain: the idioms, cultural tone, and implied intent.

        TEXT:
        {text}
        """)


# Example usage:
# engine = PromptEngine()
# prompt = engine.classify_threat("專收黑料，秒到！")
