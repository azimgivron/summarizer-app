"""Controller module"""
from .model import TextSummarizer
from .view import TextSummarizerView


class TextSummarizerController:
    """
    Manages the interaction between the model and view.

    Attributes:
        model (TextSummarizer): The model responsible for text summarization.
        view (TextSummarizerView): The view responsible for handling user input
            and displaying the summary.
    """

    def __init__(self) -> None:
        """Initialize the controller with a model and a view."""
        self.model = TextSummarizer()
        self.view = TextSummarizerView()

    def summarize_text(self) -> None:
        """Handle the summarization logic by fetching input, processing it,
        and updating the view."""
        input_text = self.view.get_input_text()
        summary = self.model.summarize(input_text)
        self.view.display_summary(summary)

    def run(self) -> None:
        """Render the view and connect the interaction logic."""
        self.view.render(self.summarize_text)
