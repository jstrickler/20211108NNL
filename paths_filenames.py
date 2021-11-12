import os
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "mary.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print(file_path)
print(os.path.exists(file_path))
print(os.path.basename(file_path))
print(os.path.dirname(file_path))
print(os.path.abspath(file_path))

file_size = os.path.getsize(file_path)
print("file size:", file_size)
print(os.path.split(file_path))
print(os.path.splitext(file_path))

file_mtime = os.path.getmtime(file_path)
print("raw timestamp:", file_mtime)
file_mod_time = datetime.fromtimestamp(file_mtime)
print(file_mod_time)
print(file_mod_time.year)

