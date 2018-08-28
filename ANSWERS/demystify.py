#!/usr/bin/env python

with open("../DATA/mystery", "rb") as m:
    d = m.read()[0::3]  # get every other byte
    print((d.decode()))  # decode from bytes to printable string
