#!/usr/bin/env python

x = 5
y = 10
thing = 'Wankel rotary engine'

result = x + y

print(result)
print("wankel rotary engine", result, "engine")
print(f"wankel {result} engine")
print("wankel rotary engine {} engine".format(result))
print(f"wankel {result} engine")

#cat strings
result = thing + thing
print("result is", result)
#doesnt work-- cant add string and ints
#result = x + thing
#print("result is", result)

#python owns class and break
#class = 'Freshman'
#break exits a loop
#break = "10 AM"

