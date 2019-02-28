#!/usr/bin/env python
from datetime import date, timedelta
#  datetime, date, time, timedelta

today = date.today()
print(today.year, today.month)
print(today)

brit_bd = date(1990, 8, 27)
print(brit_bd)

diff = today - brit_bd
print(diff)
print("Britomarte is {:.1f} years and {} days old".format(
    diff.days/365.25, diff.days % 365
))

tp = timedelta(100)  # 100 days

x = brit_bd + tp

print(x)




