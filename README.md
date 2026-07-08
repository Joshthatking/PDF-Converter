# PDF to Word Converter

A simple desktop application built with Python and Tkinter that converts PDF files into Microsoft Word (.docx) documents.

## Requirements

- Python 3.10 or newer
- Windows, macOS, or Linux

## Setup

### 1. Download the project

Clone this repository, then move into the project folder:

```bash
git clone <your-repository-url>
cd "PDF Converter"
```

### 2. Create a virtual environment

**Windows**
```bash
python -m venv venv
```

**macOS/Linux**
```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

You should now see `(venv)` at the beginning of your terminal prompt.

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

### 5. Run the program

```bash
python converter.py
```

## Using the application

1. Open the program.
2. Click **Select PDF**.
3. Choose the PDF you want to convert.
4. Wait for the "Finished!" message.
5. The converted Word document (`.docx`) will be saved in the same folder as the selected PDF, using the same filename.

## Project structure

```
PDF Converter/
│
├── converter.py       # main application
├── requirements.txt
├── README.md
└── venv/               (created after setting up the virtual environment)
```

## Deactivating the virtual environment

When you're finished, you can deactivate the virtual environment by running:

```bash
deactivate
```
