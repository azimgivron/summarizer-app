# Hugging Face Text Summarizer (NiceGUI + MVC)

A modular and user-friendly web app for text summarization built using **NiceGUI** and **Hugging Face Transformers**, following the **Model-View-Controller (MVC)** design pattern. This project demonstrates the potential of AI-powered text summarization in a clean and maintainable structure.

## Features

- **AI-Powered Summarization**: Summarizes input text using the pre-trained `facebook/bart-large-cnn` model from Hugging Face.
- **NiceGUI Web Interface**: A responsive and minimalist UI designed with the NiceGUI framework.
- **Scalable Architecture**: Implements the MVC pattern for clean separation of concerns and easy maintainability.
- **Instant Feedback**: Processes and displays summaries in real time.
- **Customizable**: Easily extendable to incorporate new features, models, or additional functionality.

## How to Run

1. **Install the app**:
   ```bash
   pip install git+https://github.com/azimgivron/summarizer-app.git
   ```

2. **Start the app**:
   ```bash
   python -m summarizer-app.main
   ```

3. **Access the web interface**:
   Open your browser and navigate to:
   ```
   http://localhost:8080
   ```

## Folder Structure

```
.
├── app/
│   ├── __init__.py        # Initializes the app module
│   ├── model.py           # Summarization logic using Hugging Face
│   ├── view.py            # NiceGUI interface components
│   ├── controller.py      # Handles interactions between model and view
├── tests/                 # Tests directory
├── main.py                # Entry point for the app
└── pyproject.toml         # Project metadata and dependencies
```

## Contributions

Contributions are welcome! Whether it's adding new features, fixing bugs, or improving documentation, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
