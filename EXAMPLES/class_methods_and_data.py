#!/usr/bin/env python

class Rabbit:
    LOCATION = "the Cave of Caerbannog" # <1>

    def __init__(self, weapon):
        self.weapon = weapon
        
    def display(self):
        print("This rabbit guarding {} uses {} as a weapon".
              format(self.LOCATION, self.weapon))

    @classmethod # <2>
    def get_location(cls):  # <3>
        return cls.LOCATION   # <4>

r = Rabbit("a nice cup of tea")
print(Rabbit.get_location()) # <5>
print(r.get_location())  # <6>
