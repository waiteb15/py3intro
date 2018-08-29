#!/usr/bin/env python

with open('DATA/alt.txt') as alt_in:
    with open('a.txt','w') as a_out:
        with open('b.txt','w') as b_out:
            for raw_line in alt_in:
                line = raw_line.strip()
                if line[0] == 'a':
                    a_out.write(raw_line)
                elif line[0] == 'b':
                    b_out.write(raw_line)
                else:
                    print(raw_line.rsplit())




