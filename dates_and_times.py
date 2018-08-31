#!/usr/bin/env python

from datetime import date, timedelta
#datetime, date, time, timedelta


today = date.today()

print(today.year, today.month)
print(today)

brian_bd= date(1991, 7, 2)
crys_bd = date(1992, 2, 7)

diff = today - brian_bd
print(diff)

myten = brian_bd + timedelta(10000)
print(myten)



