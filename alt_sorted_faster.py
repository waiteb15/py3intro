#!/usr/bin/env python
a_list = []
b_list = []

with open('DATA/alt.txt') as alt_in:
    for raw_line in alt_in:
         line = raw_line.strip()
         if line[0] == 'a':
            a_list.append(raw_line)
         elif line[0] == 'b':
            b_list.append(raw_line)
         else:
            print(raw_line.rsplit())

# a_list = sorted(a_list,reverse=True)
# b_list = sorted(b_list,reverse=True)

with open('a_sort.txt','w') as a_out:
    a_out.writelines(sorted(a_list,reverse=True))

with open('b_sort.txt','w') as b_out:
    b_out.writelines(sorted(b_list, reverse=True))