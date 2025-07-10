# logic.py

# 📄 This file handles reading text from uploaded resume files (PDF or DOCX)
# and also provides a small text cleaning function.

import fitz  # This is from PyMuPDF — used to extract text from PDF files
import docx  # Used to extract text from Word (.docx) files


def extract_text(file):
    """
    Extracts raw text content from a resume file.
    Supports: PDF (.pdf) and Word documents (.docx)

    Parameters:
        file (UploadedFile): The uploaded resume file

    Returns:
        str: The extracted text as plain string
    """
    # Get file extension to check its type
    extension = file.name.split(".")[-1].lower()

    # ===== Handle PDF files =====
    if extension == "pdf":
        # Read the file using PyMuPDF (fitz)
        with fitz.open(stream=file.read(), filetype="pdf") as pdf_document:
            text = ""
            for page in pdf_document:
                text += page.get_text() + "\n"
            return text

    # ===== Handle DOCX (Word) files =====
    elif extension == "docx":
        # Read using python-docx
        doc = docx.Document(file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text

    # ===== Unsupported file =====
    else:
        return "Unsupported file format. Please upload a PDF or DOCX."


def clean_text(text):
    """
    Cleans up the extracted resume text.
    Removes invisible characters like zero-width spaces and trims extra space.

    Parameters:
        text (str): Raw text to be cleaned

    Returns:
        str: Cleaned text
    """
    # \u200b is a zero-width space that sometimes appears in copy-pasted resumes
    return text.replace("\u200b", "").strip()