import PyPDF2
import os
def merge_pdfs():
    print("\n=== PDF Merger ===")
    pdf_input = input("Enter the names of the PDF files to merge (separated by commas): ").strip()
    pdf_files = [file.strip() for file in pdf_input.split(",") if file.strip().endswith(".pdf")]
    if not pdf_files:
        print("No valid PDF files provided. Please try again.")
        return
    missing_files = [pdf for pdf in pdf_files if not os.path.exists(pdf)]
    if missing_files:
        print(f"Error: The following files do not exist: {', '.join(missing_files)}")
        return
    try:
        merger = PyPDF2.PdfMerger()
        for pdf in pdf_files:
            merger.append(pdf)
        output_file = input("Enter the name of the output merged PDF file (default: merged.pdf): ").strip()
        if not output_file:
            output_file = "merged.pdf"
        merger.write(output_file)
        merger.close()
        print(f"Merged PDF saved as '{output_file}'")
    except Exception as e:
        print(f"An error occurred while merging PDFs: {e}")
if __name__ == "__main__":
    merge_pdfs()
