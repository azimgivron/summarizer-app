"""View module"""
from typing import Callable
from nicegui import ui


class TextSummarizerView:
    """Defines the user interface for the text summarization app."""

    def __init__(self) -> None:
        """Initialize UI components."""
        self.input_area = None
        self.output_label = None

    def render(self, summarize_callback: Callable[[], None]) -> None:
        """
        Render the user interface.

        Args:
            summarize_callback (Callable[[], None]): The function to call
                when the summarize button is clicked.
        """
        ui.label("Text Summarizer").classes("text-2xl font-bold text-center mt-5")

        with ui.card().classes("w-1/2 mx-auto mt-5"):
            ui.label("Input Text").classes("text-lg font-medium mb-2")
            self.input_area = ui.textarea(placeholder="Enter text here...").classes(
                "w-full mb-4"
            )

            self.output_label = ui.label("Summary will appear here").classes(
                "text-lg font-medium mt-4"
            )

            ui.button("Summarize", on_click=summarize_callback).classes(
                "mt-4 bg-blue-500 text-white rounded-lg px-4 py-2"
            )

    def get_input_text(self) -> str:
        """
        Retrieve the text from the input area.

        Returns:
            str: The input text entered by the user.
        """
        return self.input_area.value

    def display_summary(self, summary: str) -> None:
        """
        Display the summarized text in the output area.

        Args:
            summary (str): The summarized text to display.
        """
        self.output_label.text = summary
