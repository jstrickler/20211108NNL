import requests
from zipfile import ZipFile
import os

URL = "https://www.python.org"

response = requests.get(URL)
print(response.status_code)
print(response.text)

PDF_URL = "https://docs.python.org/3/archives/python-3.10.0-docs-pdf-letter.zip"

response = requests.get(PDF_URL)
print(response.status_code)

zip_name = "pydocs.zip"
with open(zip_name, 'wb') as pydocs_in:
    pydocs_in.write(response.content)

zip_file = ZipFile(zip_name)
print(zip_file.namelist())
member_name = "docs-pdf/howto-unicode.pdf"
zip_file.extract(member_name)
os.system(member_name.replace('/', "\\"))
