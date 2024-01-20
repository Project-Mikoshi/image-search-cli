# InkSpotter CLI

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![openCV](https://img.shields.io/badge/openCV-4.7-5C3EE8?logo=openCV)](https://python-poetry.org/)
[![python](https://img.shields.io/badge/python-3.12-3776AB?logo=python)](https://www.python.org/downloads/release/python-3120/)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview
InkSpotter CLI is a powerful and user-friendly command-line tool designed for searching text within images. Leveraging Tesseract OCR (Optical Character Recognition), InkSpotter CLI scans a given directory for images, extracts text, and highlights instances of specified search phrases. This tool is ideal for users needing to quickly search and identify text across numerous image files.

## Features
- **Text Search in Images:** Search for any text across multiple image formats.
- **Recursive Directory Scanning:** Scans specified directory and its subdirectories for images.
- **Text Highlighting:** Highlights found text directly on the image.
- **Interactive and Command Mode:** Offers both interactive prompts and direct command mode for flexibility.

## Installation
### Prerequisites
- Python 3.12 or higher
- [Tesseract OCR](https://tesseract-ocr.github.io/tessdoc/Installation.html) installed and accessible in PATH

## Usage
### Interactive Mode
Run the script and follow the interactive prompts:
```
python inkspotter.py interactive
```

### Command Mode
Directly provide the parameters:
```
python inkspotter.py scan --search_text "Your Text" --search_directory "/path/to/directory" --output_directory "/path/to/output"
```

## License
[MIT License](LICENSE)
