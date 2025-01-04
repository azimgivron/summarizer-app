from transformers import pipeline

class TextSummarizer:
    """Handles text summarization using Hugging Face's Transformers library."""

    def __init__(self, max_tokens: int = 1024) -> None:
        """
        Initialize the summarizer pipeline.

        Args:
            max_tokens (int): Maximum number of tokens supported by the model.
        """
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.max_tokens = max_tokens

    def split_text(self, text: str, max_length: int) -> list:
        """
        Split text into chunks that fit within the model's maximum token limit.

        Args:
            text (str): The input text to split.
            max_length (int): Maximum length of each chunk.

        Returns:
            list: A list of text chunks.
        """
        sentences = text.split(". ")
        chunks = []
        current_chunk = []

        for sentence in sentences:
            if len(" ".join(current_chunk + [sentence])) <= max_length:
                current_chunk.append(sentence)
            else:
                chunks.append(". ".join(current_chunk))
                current_chunk = [sentence]

        if current_chunk:
            chunks.append(". ".join(current_chunk))

        return chunks

    def summarize(self, text: str, min_ratio: float = 0.3, max_ratio: float = 0.5) -> str:
        """
        Summarize the given text.

        Args:
            text (str): Input text to summarize.
            min_ratio (float): Minimum ratio of output length to input length for summaries.
            max_ratio (float): Maximum ratio of output length to input length for summaries.

        Returns:
            str: The summarized text or an error message if the operation fails.
        """
        if not text.strip():
            return "Please provide input text to summarize."

        try:
            # Split the text if it exceeds the token limit
            chunks = self.split_text(text, self.max_tokens)
            summaries = []

            for chunk in chunks:
                input_length = len(chunk.split())
                # Calculate max_length dynamically
                max_length = max(int(input_length * max_ratio), 30)
                min_length = max(int(input_length * min_ratio), 10)

                # Summarize the chunk
                summary = self.summarizer(
                    chunk, max_length=max_length, min_length=min_length, do_sample=False
                )[0]["summary_text"]
                summaries.append(summary)

            # Combine all summaries
            return " ".join(summaries)

        except Exception as e:
            return f"An error occurred: {e}"

