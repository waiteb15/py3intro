#!/usr/bin/env python



brian = """MEX
USA
CAN
JAM
SUI
DOM
GER""".split('\n')

crystal = """USA
CAN
SUI
GER""".split('\n')

bc = set(brian)
cc = set(crystal)


# INTERSECTION OF SETS
print("both:", bc & cc)
# unique union of both sets
print("either:", bc | cc)

print("just one:", bc ^ cc)
print("just bri:", bc - cc )
print("just cry", cc - bc)


# would be an easy way to get a list of values without duplicates
bcl = list(bc)
print(bcl)

#frozen set is likely the only for validation
