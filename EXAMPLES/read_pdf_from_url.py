#!/usr/bin/env python

import sys
import os
from urllib.request import urlopen
from urllib.error import HTTPError

# url to download a PDF file of a NASA ISS brochure

url = 'https://www.nasa.gov/pdf/739318main_ISS%20Utilization%20Brochure%202012%20Screenres%203-8-13.pdf'
saved_pdf_file = 'nasa_iss.pdf'

try:
    URL = urlopen(url)
except HTTPError as e:
    print("Unable to open URL:",e)
    sys.exit(1)
    
pdf_contents = URL.read()
URL.close()
    
with open(saved_pdf_file,'wb') as pdf_in:
    pdf_in.write(pdf_contents)


if sys.platform == 'win32':
    cmd = saved_pdf_file
elif sys.platform == 'darwin':
    cmd = 'open ' + saved_pdf_file
else:
    cmd = 'acroread ' + saved_pdf_file

os.system(cmd)
