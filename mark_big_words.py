#!/usr/bin/env python
import re

rx_code = re.compile(r'(?P<bigword>\b[A-Z]{8,}\b)', re.I)

def update_code(m):
    word = m.group('bigword')
    return f'*{word}*'

with open('DATA/parrot.txt') as parrot_in:
    with open('bigwords.txt','w') as bigwords_out:
        for line in parrot_in:
            line2 = rx_code.sub(update_code, line)
            bigwords_out.write(line2)
