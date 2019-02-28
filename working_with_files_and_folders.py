#!/usr/bin/env python
import os
from datetime import datetime

FOLDER = 'DATA'
FILE_NAME = 'mary.txt'

file_path = os.path.join(FOLDER, FILE_NAME)
print("file path:", file_path)
print("file size:", os.path.getsize(file_path))
print("folder part:", os.path.dirname(file_path))
print("file part:", os.path.basename(file_path))
print("absolute path:", os.path.abspath(file_path))
print("exists?", os.path.exists(file_path))
print("exists?", os.path.exists('DATA/rubblebubble'))
print(dir(os.path))
print(os.sep, os.pathsep)
print("stat:", os.stat(file_path))
raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)
timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)


