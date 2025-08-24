# AI Web Page Summarizer

This project is a simple AI-powered web page summarizer that leverages OpenAI's GPT models and local inference with Ollama to generate concise summaries of given text. The goal is to create a "Reader's Digest of the Internet" by summarizing web content efficiently.

## Features

- Summarize text using OpenAI's GPT models or local Ollama models.
- Flexible summarization engine selection (OpenAI API, Ollama API, or Ollama library).
- Simple and modular code structure.
- Error handling for better reliability.

## Project Structure

```txt
ai-summarizer/
│-- summarizer/
│   │-- __init__.py
│   │-- fetcher.py       # Web content fetching logic
│   │-- summarizer.py    # Main summarization logic
│-- utils/
│   │-- __init__.py
│   │-- logger.py        # Logging configuration
│-- main.py              # Entry point of the app
│-- .env                 # Environment variables
│-- requirements.txt     # Python dependencies
│-- README.md            # Project documentation
```

## Prerequisites

- Python 3.8 or higher
- OpenAI API Key (You can obtain it from [OpenAI](https://platform.openai.com/signup))
- Ollama installed locally ([Installation Guide](https://ollama.ai))
- `conda` for managing environments (optional)

## Usage

1. **Run the summarizer:**

   ```bash
   python main.py
   ```

2. **Sample Output:**

   ```shell
   Enter a URL to summarize: https://example.com
   Summary of the page:
   AI refers to machines demonstrating intelligence similar to humans and animals.
   ```

3. **Engine Selection:**

   The summarizer supports multiple engines. Modify `main.py` to select your preferred model:

   ```python
   summary = summarize_text(content, 'gpt-4o-mini', engine="openai")
   summary = summarize_text(content, 'deepseek-r1:1.5B', engine="ollama-api")
   summary = summarize_text(content, 'deepseek-r1:1.5B', engine="ollama-lib")
   ```

## Configuration

You can modify the model, max tokens, and temperature in `summarizer/summarizer.py`:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    max_tokens=300,
    temperature=0.7
)
```

## Error Handling

If any issues occur, the script will print an error message, for example:

```shell
Error during summarization: Invalid API key or Ollama not running.
```

## Dependencies

The required dependencies are listed in `requirements.txt`:

```txt
openai
python-dotenv
requests
ollama-api
```

Install them using:

```bash
pip install -r requirements.txt
```
