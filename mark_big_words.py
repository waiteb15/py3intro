#!/usr/bin/env python
import re

input_file_name = 'DATA/parrot.txt'
output_file_name = 'bigwords.txt'

pattern = r'\w{8,}'

def doit(m):
    return f"**{m.group(0)}**"

with open(input_file_name) as parrot_in:
    with open(output_file_name, 'w') as bigwords_out:
        text = parrot_in.read()
        new_text = re.sub(pattern, doit, text)
        bigwords_out.write(new_text)
