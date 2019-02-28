#!/usr/bin/env python
#from module improt class


from pprint import pprint
import sys

print(sys.argv,'\n')

print(sys.prefix)

print(sys.executable)

for path in sys.path:
    print(path)

print()


print(sys.version,'\n')
print(sys.version_info, '\n')
print(sys.version_info.major)

pprint(sys.modules)


print(sys.modules['re'])

print(sys.platform, '\n')