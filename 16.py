# write a function to read a complete PDf file .
# pip install PyPDF2
from PyPDF2 import PdfFileReader
def readpdf(path):
	"""Read a pdf and display text in console"""
	object_pdf = open(path,"r+b") # open pdf in read mode & binary mode
	pdf = PdfFileReader(object_pdf)
	x = pdf.numPages
	for i in range(x):
		pageobject = pdf.getPage(i)
		print(pageobject.extractText())
	object_pdf.close()

if __name__ == "__main__":
	readpdf(input("Enter the path of the pdf\n"))


	