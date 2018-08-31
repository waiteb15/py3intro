#!/usr/bin/env python

class Knight():

    def __init__(self, knightname):
        self._knightname = knightname

    @property #getter
    def knightname(self):
        return self._knightname

    @knightname.setter # setter
    def knightname(self,knightname):
        if isinstance(knightname,str):
            self._knightname = knightname
        else:
            raise TypeError("Dealer must be a string")
