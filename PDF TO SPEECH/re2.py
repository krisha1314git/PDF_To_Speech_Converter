import PyPDF2
import pyttsx3
import re
from tkinter import filedialog, Tk, Label
from PIL import Image, ImageTk
from pdf2image import convert_from_path

def extract_text(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

def preprocess_text(text):
    text = re.sub(r'\.', '.   ', text)   # pause after full stops
    text = re.sub(r' ', '  ', text)      # slight pause between words
    return text

def speak_text(text):
    engine = pyttsx3.init()
    processed = preprocess_text(text)
    engine.say(processed)
    engine.runAndWait()

from tkinter import Tk
from tkPDFViewer import tkPDFViewer as pdf

def show_pdf(pdf_path):
    root = Tk()
    root.title("PDF Viewer")
    v1 = pdf.ShowPdf()
    v2 = v1.pdf_view(root, pdf_location=pdf_path, width=80, height=100)
    v2.pack()
    root.mainloop()

def main():
    print("=== PDF to Speech Converter ===")

    root = Tk()
    root.withdraw()
    pdf_path = filedialog.askopenfilename(
        title="Select PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not pdf_path:
        print("No file selected. Exiting.")
        return

    text = extract_text(pdf_path)

    while True:
        print("\n--- Menu ---")
        print("1. Read aloud")
        print("2. Show PDF")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == "1":
            speak_text(text)
        elif option == "2":
            show_pdf(pdf_path)
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
