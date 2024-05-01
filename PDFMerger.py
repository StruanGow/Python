import PyPDF2

def merge_files(pdf_files: list):
#making object
pdf_merger = PyPDF2.PdfFileMerger()
for pdf_file in pdf_files:
  pdf_merger.append(pdf_file)
output_pdf = "merged_file.pdf"
pdf_merger.write(output_pdf)
pdf_merger.close()

pdf_files = ["ExampleFile1", "ExampleFile2"]

if __name__ == "__main__":
  merge_files(pdf_files)
  print("PDFs merged successfully!")
