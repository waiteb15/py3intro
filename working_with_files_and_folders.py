#!/usr/bin/env python
import os

from datetime import datetime

from pprint import pprint
FOLDER = 'DATA'
FILE_NAME = 'mary.txt'

file_path = os.path.join(FOLDER,FILE_NAME)
print("file path:", file_path)
print(f"file size: {os.path.getsize(file_path)}")
print(f"folder part: {os.path.dirname(file_path)}")
print(f"file part: {os.path.basename(file_path)}")
print(f"absolute path: {os.path.abspath(file_path)}")
print(f"exists?: {os.path.exists(file_path)}")
print(f"exists?: {os.path.exists('DATA/asdfasdfa')}")

#everything part of os.path
pprint(dir(os.path))
print("raw timestamp:", os.path.getmtime(file_path))

print("raw timestamp:", datetime.fromtimestamp(os.path.getmtime(file_path)))

