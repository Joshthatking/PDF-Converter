# PDF to Word Converter

A simple desktop application built with Python and Tkinter that converts PDF files into Microsoft Word (.docx) documents.

There are two ways to use this app: run the **prebuilt .exe** (no Python required), or **run it from source** (useful for development).

## Option 1: Run the prebuilt .exe

1. Go to the `dist` folder in the project.
2. Double-click `converter.exe`.
3. If Windows SmartScreen shows a warning (since the app isn't code-signed), click **More info > Run anyway**.

That's it — no Python, virtual environment, or installed packages needed. Skip to [Using the application](#using-the-application) below.

## Option 2: Run from source

### Requirements

- Python 3.10 or newer (or Anaconda, which includes Python)
- Windows
- Git (only needed if cloning from the command line)

### 1. Get the project onto your computer

**Option A — Command Prompt or Anaconda Prompt**

Open Command Prompt (search "cmd" in the Start menu) or Anaconda Prompt (search "Anaconda Prompt"), then run:

```bash
git clone <your-repository-url>
cd "PDF Converter"
```

**Option B — VS Code**

1. Open VS Code.
2. Press `Ctrl+Shift+P` to open the Command Palette.
3. Type and select **Git: Clone**.
4. Paste your repository URL and choose a folder to save it in.
5. When prompted, click **Open** to open the cloned folder in VS Code.
6. Open a terminal inside VS Code: menu **Terminal > New Terminal**.

### 2. Create a virtual environment named `PDFenv`

In Command Prompt, Anaconda Prompt, or the VS Code terminal, make sure you're in the `PDF Converter` folder, then run:

**Using Command Prompt (plain Python)**
```bash
python -m venv PDFenv
```

**Using Anaconda Prompt**
```bash
conda create -n PDFenv python=3.10
```

### 3. Activate `PDFenv`

**Command Prompt / VS Code terminal**
```bash
PDFenv\Scripts\activate
```

**Anaconda Prompt**
```bash
conda activate PDFenv
```

You should now see `(PDFenv)` at the beginning of your prompt.

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

### 5. Run the program

```bash
python converter.py
```

A small window titled "PDF to Word Converter" should open.

## Using the application

1. Open the program (see step 5 above).
2. Click **Select PDF**.
3. Choose the PDF you want to convert.
4. Wait for the "Finished!" message.
5. The converted Word document (`.docx`) will be saved in the same folder as the selected PDF, using the same filename.

## Building the .exe yourself

If you've changed `converter.py` and want to rebuild the executable, run this from an activated `PDFenv` (see [Option 2](#option-2-run-from-source) above; `pyinstaller` is already listed in `requirements.txt`):

```bash
pyinstaller converter.spec
```

The new `converter.exe` will be written to the `dist` folder. The `build` folder and `converter.spec` are regenerated each time and are not tracked in git.

## Project structure

```
PDF Converter/
│
├── converter.py       # main application source
├── converter.spec      # PyInstaller build config
├── requirements.txt
├── README.md
├── dist/
│   └── converter.exe   # prebuilt executable
├── build/               (PyInstaller intermediate files, not tracked)
└── PDFenv/             (created after setting up the virtual environment)
```

## Deactivating the environment

When you're finished, deactivate with the command matching how you activated it:

**Command Prompt / VS Code terminal**
```bash
deactivate
```

**Anaconda Prompt**
```bash
conda deactivate
```
