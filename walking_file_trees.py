#!/usr/bin/env python

import os
from zipfile import ZipFile

target_dir = './ANSWERS'
for curr_dir, dir_list, file_list in os.walk(target_dir):
    if 'git' in curr_dir:
        continue
    print(curr_dir)
    for file_name in file_list:
        if file_name.endswith(".py"):
            file_path = os.path.join(curr_dir,file_name)
            file_size = os.path.getsize(file_path)
            print(file_size, file_path)

