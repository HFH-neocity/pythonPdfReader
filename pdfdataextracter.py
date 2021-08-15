import PyPDF2

pdfFileObj = open('Zeynel A. Karcioglu - Orbital Tumors_ Diagnosis and Treatment-Springer (2005).pdf', 'rb')
currentpage = 0
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numofpages = pdfReader.numPages

for numofpages in range(0, numofpages):
    pageObj = pdfReader.getPage(currentpage)
    content = pageObj.extractText()
    print(content, numofpages)
    currentpage += 1