import docx
from docx import Document

#file=open("Data/data1.docx", 'r')

def ReadDocFile(FileName):
    doc = docx.Document((FileName))

    List1=[]

    for paragraph in doc
        List1.append(paragraph)

    return '\n' .join(List1)

print(ReadDocFile("Data/data1.docx"))





