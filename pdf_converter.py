import PyPDF2
import os


def merge_pdfs():
    pdf_files = [f for f in os.listdir() if f.endswith(".pdf")]
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return

    merger = PyPDF2.PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write("merged.pdf")
    merger.close()
    print("Merged PDF saved as 'merged.pdf'.")
