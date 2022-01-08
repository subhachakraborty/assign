# write a function to read a word file .
import docx # pip install python-docx
def readtxt(filepath):
    """It will read a word file"""
    doc = docx.Document(filepath)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

if __name__ == "__main__":
    filepath = input("Enter the path of the docx file\n")
    print(readtxt(filepath))