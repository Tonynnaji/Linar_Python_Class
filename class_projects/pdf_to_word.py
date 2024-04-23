
# pip install pdf2word
from collections.abc import Iterable
# imports
from pdf2docx import Converter
from docx2python import docx2python

# Keeping the PDF's location in a seperate variable source file name
path_to_pdf =  "C:/Users/USE/Desktop/path.pdf"

# Maintaing the Document's path in a seperate variable
path_to_docx =  "C:/Users/USE/Desktop.docx"

# using the builtin function , convert the PDF file to a document file by saving it in a variable
cv_obj = Converter(path_to_pdf)

# Storing the Document  in the variable's initialised path
cv_obj.convert(path_to_docx)

# Conversion closure through the function close()
cv_obj.close()


# extract docx content
with docx2python("C:/Users/USE/Desktop.docx") as docx_content:
    print(docx_content.text)

docx_content = docx2python("C:/Users/USE/Desktop.docx")
print(docx_content.text)
docx_content.close()

# extract docx content, write images to image_directory
with docx2python("C:/Users/USE/Desktop.docx", 'path/to/image_directory') as docx_content:
    print(docx_content.text)

# extract docx content with basic font styles converted to html
with docx2python("C:/Users/USE/Desktop.docx", html=True) as docx_content:
    print(docx_content.text)

