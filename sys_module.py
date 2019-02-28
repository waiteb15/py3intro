#!/usr/bin/env python
import sys
print(sys.argv, '\n')

print(sys.prefix)
print(sys.executable)
print()

for path in sys.path:
    print(path)
print()

print(sys.version, '\n')
print(sys.version_info, '\n')
print(sys.version_info.major)

print(sys.modules, '\n')

m = sys.modules['builtins']
print(m)
print(m.type(m))

import re

print(sys.modules['re'])
print(sys.modules['sys'], '\n')

print(sys.platform, '\n')
