from nicegui import ui
from app.controller import TextSummarizerController

if __name__ == "__main__":
    """
    Entry point for the text summarization app.

    Starts the NiceGUI server and initializes the controller to handle the app logic.
    """
    controller = TextSummarizerController()
    controller.run()
    ui.run(title="Hugging Face Summarizer", port=8080)
