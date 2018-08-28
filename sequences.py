#!/usr/bin/python3

ctemps = [ -40, 0, 37, 75, 100 ]

for cels in ctemps:
    fahrs = ((9 * cels) / 5) + 32
    print(f"{cels} Celsius is {fahrs} Fahrenheit")

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]
print(fruits)
clean_fruits = [f.lower().strip() for f in fruits]
print(clean_fruits)