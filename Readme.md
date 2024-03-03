# PDF Question Answer System

This project provides a Flask API for asking questions based on text extracted from PDF documents. It utilizes OpenAI's language model for question answering.

## Installation

1. Install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

2. Set up your OpenAI API key by creating a `.env` file in the project root directory and adding your API key:

    ```
    OPENAI_API_KEY=<your_openai_api_key>
    ```

## Usage

1. Add your PDF files to the `app.py` list in the Flask API script:

    ```python
    pdf_files = ["first.pdf", "second.pdf"]  # Add more PDF files as needed
    ```

2. Start the Flask API:

    ```bash
    python app.py
    ```

3. Send a POST request to the `/ask` endpoint with a JSON payload containing the question:

    ```json
    {
        "question": "Your question here"
    }
    ```

## Example

```bash
curl -X POST -H "Content-Type: application/json" -d '{"question": "Who is Vishal Sharma?"}' http://127.0.0.1:5000/ask
```

# Happy coding!
