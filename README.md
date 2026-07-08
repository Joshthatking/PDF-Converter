PDF to Word Converter

A simple desktop application built with Python and Tkinter that converts PDF files into Microsoft Word (.docx) documents.

Requirements
Python 3.10 or newer
Windows, macOS, or Linux
1. Download the Project

Download or clone this repository.

git clone <your-repository-url>
cd <project-folder>
2. Create a Virtual Environment
Windows
python -m venv venv
macOS/Linux
python3 -m venv venv
3. Activate the Virtual Environment
Windows
venv\Scripts\activate
macOS/Linux
source venv/bin/activate

You should now see (venv) at the beginning of your terminal prompt.

4. Install the Required Packages
pip install -r requirements.txt
5. Run the Program
python main.py

If your main Python file has a different name, replace main.py with that filename.

6. Using the Application
Open the program.
Click Select PDF.
Choose the PDF you want to convert.
Wait for the conversion to finish.
The Word document (.docx) will be saved in the same folder as the selected PDF.
Project Structure
project/
│
├── main.py
├── requirements.txt
├── README.md
└── venv/          (created after setting up the virtual environment)
Deactivating the Virtual Environment

When you're finished, you can deactivate the virtual environment by running:

deactivate