import PyPDF2

new_pdf = open("main.pdf","rb")
reading_pdf = PyPDF2.PdfFileReader(new_pdf)
print(reading_pdf.numPages) #Prints the number of pages in the pdf

pdf_page = reading_pdf.getPage(0)
print(pdf_page.extractText()) # Extracts the data from pdf

new_pdf.close() #closes the pdf
