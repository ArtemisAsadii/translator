# Text Translator to Persian

A simple Python project to translate any text into Persian (Farsi) using the `deep-translator` library. The translator automatically detects the source language.

## Features

- Translate text from any language to Persian.
- Automatic detection of the source language.
- Handles errors gracefully.
- Easy to use and lightweight.

## About the Library

This project uses the [deep-translator](https://github.com/nidhaloff/deep-translator) library, which acts as an interface to online translation services such as Google Translate, Microsoft Translator, and others.  

**Important Notes:**
- **Online Required:** deep-translator relies on internet access to connect to translation services.
- **No Built-in Models:** The library does not perform translation locally; it sends requests to online APIs.
- **Supported Services:** You can choose different translation providers if needed (e.g., Google, Pons, Linguee).

## Requirements

- Python 3.7 or higher
- `deep-translator` library

Install the required packages with:

```bash
pip install -r requirements.txt
