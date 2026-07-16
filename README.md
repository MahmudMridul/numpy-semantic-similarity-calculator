# Numpy Semantic Similarity Calculator

A CLI tool that reads sentences from a text file, converts them into bag-of-words vectors using NumPy only, and computes cosine similarity between them — no ML libraries involved, just NumPy arrays, dot products, and norms.

## Project Structure

```
numpy_semantic_similarity_calculator/
├── config/
│   └── log_config.json
├── data/
│   └── sentences.txt
├── logs/
│   └── app.log
├── src/
│   ├── analyse.py
│   ├── app_logger.py
│   ├── constants.py
│   ├── file_reader.py
│   ├── main.py
│   ├── sentence_processor.py
│   └── vectorizer.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── PROJECT_SPECIFICATION.md
└── README.md
```

## Setup & Run

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and requires Python 3.14+.

1. **Install dependencies**

   ```bash
   uv sync
   ```

2. **Add input sentences**

   Put one sentence per line in `data/sentences.txt`.

3. **Run the app**

   ```bash
   uv run src/main.py
   ```

   Cosine similarity scores between sentence pairs are printed to the console. Logs are written to `logs/app.log`, configurable via `config/log_config.json`.
