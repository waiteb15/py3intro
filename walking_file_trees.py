#!/usr/bin/env python
import os
from zipfile import ZipFile


with ZipFile('myfiles.zip', 'w') as zip:
#    target_dir = os.path.abspath('.')
    target_dir = '.'
    for curr_dir, dir_list, file_list in os.walk(target_dir):
        if 'git' in curr_dir:
            continue
        print(curr_dir)
        for file_name in file_list:
            if file_name.endswith('.py'):
                file_path = os.path.join(curr_dir, file_name)
                file_size = os.path.getsize(file_path)
                if file_size >= 1000:
                    zip.write(file_path) # add to .zip file
