
# pip install pdf2docx
from collections.abc import Iterable
# imports
from pdf2docx import Converter


# Keeping the PDF's location in a seperate variable source file name
path_to_pdf =  "C:/Users/USE/Documents/GitHub/Linar_Python_Class/Test.pdf"

# Maintaing the Document's path in a seperate variable
path_to_docx =  "C:/Users/USE/Desktop.docx"

# using the builtin function , convert the PDF file to a document file by saving it in a variable
cv_obj = Converter(path_to_pdf)

# Storing the Document  in the variable's initialised path
cv_obj.convert(path_to_docx)

# Conversion closure through the function close()
cv_obj.close()



from pdf2docx import parse

pdf_file = r"C:\Users\USE\Documents\GitHub\Linar_Python_Class\Test.pdf"
docx_file = r"C:\Users\USE\Desktop.docx"

# convert pdf to docx
parse(pdf_file, docx_file)