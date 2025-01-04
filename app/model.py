from transformers import pipeline

class TextSummarizer:
    """Handles text summarization using Hugging Face's Transformers library."""

    def __init__(self) -> None:
        """Initialize the summarizer pipeline."""
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def summarize(self, text: str) -> str:
        """
        Summarize the given text.

        Args:
            text (str): Input text to summarize.

        Returns:
            str: The summarized text or an error message if the operation fails.
        """
        if not text.strip():
            return "Please provide input text to summarize."
        try:
            summary = self.summarizer(text, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
            return summary
        except Exception as e:
            return f"An error occurred: {e}"
