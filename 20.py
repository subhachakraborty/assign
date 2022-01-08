# write a function by which you will be able to append two PDF files .
import PyPDF2 
def pdfmerge(file1,file2,name="Appended file.pdf"):
    """It wll append two PDF files.Default name is 'Appended file.pdf' """
    file = PyPDF2.PdfFileMerger() # Empty file object
    file.append(file1,"r+b")
    file.append(file2,"r+b")
    file.write(name)

if __name__ == "__main__":
    file1 = input("Enter path of first file\n")
    file2 = input("Enter path of second file\n")
    pdfmerge(file1,file2)