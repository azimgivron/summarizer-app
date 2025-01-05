from summarizer.model import TextSummarizer
import pytest

@pytest.fixture(name="text_summarizer")
def get_text_summarizer():
    return TextSummarizer()

def test_translation(text_summarizer: TextSummarizer):
    with open("text_to_summarize.txt", "r", format="utf-8") as stream:
        text = stream.read()
    summary = text_summarizer.summarize(text)
    assert len(summary) < len(text)