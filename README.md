# PDF Cover Image Extractor

A Python script that extracts the first page (cover) from PDF files and saves them as high-quality PNG images with automatic border cropping.

## Features

- Extracts the first page from PDF files as images
- Automatically crops white borders from the extracted images
- Saves images in high-quality PNG format
- Batch processing of multiple PDF files
- Simple and easy to use

## Requirements

- Python 3.10 or higher
- poppler-utils (for PDF processing)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd pdf-cover-image
```

### 2. Create and activate virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install poppler-utils

#### On macOS:
```bash
brew install poppler
```

#### On Ubuntu/Debian:
```bash
sudo apt-get install poppler-utils
```

#### On Windows:
Download and install poppler from [poppler releases](https://github.com/oschwartz10612/poppler-windows/releases/)

## Usage

1. **Prepare your PDF files**: Place all PDF files you want to process in the `input` folder

2. **Run the script**:
```bash
python main.py
```

3. **Get your results**: Extracted cover images will be saved in the `output` folder with the naming pattern `{original_filename}_cover.png`

## Project Structure

```
pdf-cover-image/
├── main.py              # Main script
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── input/               # Place your PDF files here
└── output/              # Extracted cover images will be saved here
```

## How it works

1. The script scans the `input` directory for PDF files
2. For each PDF, it extracts the first page as a high-resolution image (300 DPI)
3. White borders are automatically detected and cropped
4. The processed image is saved as a PNG file in the `output` directory

## Configuration

You can modify the following variables in `main.py`:

- `input_dir`: Directory containing PDF files (default: "input")
- `output_dir`: Directory where cover images will be saved (default: "output")
- `border_color`: Color of borders to crop (default: white - (255, 255, 255))
- `dpi`: Resolution for image extraction (default: 300)

## Dependencies

- `pdf2image`: Converts PDF pages to images
- `Pillow`: Image processing and manipulation
- `poppler-utils`: PDF processing backend

## License

This project is licensed under the MIT License - see below for details.

---

## MIT License

Copyright (c) 2025 PDF Cover Image Extractor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
