#!/usr/bin/env python

#this variation does not import _xxxx functions
from KAPL_UTIL import *
import numpy as np

print(dir(np)[8])



ham()
spam()

# DON't do this, its supposed to be private...ssshhhh!
#KAPL_UTIL._eggs()

