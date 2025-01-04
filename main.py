from nicegui import ui
from summarizer.controller import TextSummarizerController

def main():
    """
    Entry point for the text summarization app.

    Starts the NiceGUI server and initializes the controller to handle the app logic.
    """
    controller = TextSummarizerController()
    controller.run()
    ui.run(title="Hugging Face Summarizer", port=8080)

if __name__ in {"__main__", "__mp_main__"}:
    main()
