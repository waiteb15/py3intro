#!/usr/bin/env python

x = 23.45

vals = [5.9,4.8,3.6,0,5.1,7.2, 'dumb']

print('-'*60)
for v in vals:
    try:
        result = x / v
        print(result)
    except (ZeroDivisionError,TypeError) as err:
        print(err)
print('-'*60)

for v in vals:
    try:
        result = x / v
        print(result)
    except TypeError as err:
        print(err)
    except ZeroDivisionError as err:
        print(err)

print('-' * 60)

for v in vals:
    try:
        result = x / v
        print(result)
    except Exception as err:
        print(err)
        print(type(err).__name__)
    else:
        pass
    finally:
        pass


print('-' * 60)