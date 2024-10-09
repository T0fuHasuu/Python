from ebooklib import epub, ITEM_DOCUMENT
from fpdf import FPDF
from bs4 import BeautifulSoup
import warnings
import unicodedata
import os
import tkinter as tk
from tkinter import filedialog

# Specify Error
warnings.filterwarnings("ignore", category=UserWarning, module='ebooklib')
warnings.filterwarnings("ignore", category=FutureWarning)

# Set Text Default
def normalize_text(text):
    # Convert Unicode characters to closest ASCII equivalent or remove if no equivalent
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

# Extract text from Epub
def epub_to_text(epub_path):
    # Read Epub and Set warning to false to succeed
    book = epub.read_epub(epub_path, options={"ignore_ncx": False})
    text_content = []

    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT: 
            soup = BeautifulSoup(item.content, 'html.parser')
            text_content.append(soup.get_text())

    return '\n'.join(text_content)

# Convert Text - PDF
def text_to_pdf(text, pdf_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Normalize Text
    normalized_text = normalize_text(text)

    # Make it fit into the pdf Page
    lines = normalized_text.split('\n')
    for line in lines:
        pdf.multi_cell(0, 10, line)

    pdf.output(pdf_path)

# Convert Function
def epub_to_pdf(epub_path, pdf_path):
    text = epub_to_text(epub_path)
    text_to_pdf(text, pdf_path)

# Browse Folder
def select_epub_file():
    root = tk.Tk()
    root.withdraw()  
    epub_path = filedialog.askopenfilename(
        title="Select an EPUB file",
        filetypes=[("EPUB files", "*.epub")]
    )
    return epub_path

# Main execution
epub_path = select_epub_file()
if epub_path:
    base_name = os.path.splitext(os.path.basename(epub_path))[0]
    pdf_path = f"{base_name}.pdf"
    epub_to_pdf(epub_path, pdf_path)
    print(f"EPUB converted to PDF successfully: {pdf_path}")
else:
    print("No EPUB file selected.")
