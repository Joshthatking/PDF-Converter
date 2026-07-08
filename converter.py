import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

def convert():
    pdf = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not pdf:
        return

    output = pdf.replace(".pdf", ".docx")

    cv = Converter(pdf)
    cv.convert(output)
    cv.close()

    status.config(text="Finished!")

root = tk.Tk()
root.title("PDF to Word Converter")

button = tk.Button(root, text="Select PDF", command=convert)
button.pack(padx=20, pady=20)

status = tk.Label(root, text="")
status.pack()

root.mainloop()