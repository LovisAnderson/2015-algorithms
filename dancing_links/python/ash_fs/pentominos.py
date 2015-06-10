import copy
from array import *
import numpy as np
from sets import ImmutableSet

class Pentomino(object):
    def __init__(self, name, coos):
        self.name = name
        self.coos = coos
        self.dim = len(coos[0])
        
    def normalize_coo(self, coo):
        minimum = min([c[coo] for c in self.coos])
        for c in self.coos:
            c[coo] -= minimum 

    def normalize(self):
        for i in range(self.dim):
            self.normalize_coo(i)
        return self

    def flip(self, coo):
        minimum = min([c[coo] for c in self.coos])
	for c in self.coos:
            c[coo] -= (c[coo] - minimum) * 2
        self.normalize()
        return self    
    
    def translate_one(self, coo):
        for c in self.coos:
            c[coo] += 1
        return self

    def translate_coo(self, coo, amount):
        for c in self.coos:
            c[coo] += amount
        return self

    def translate_by(self, by_vector):
        for c in self.coos:
            c += by_vector
        return self

    def turn90(self, coo1=0, coo2=1):
        for c in self.coos:
            tmp = c[coo1]
            c[coo1] = c[coo2]
            c[coo2] = tmp*(-1)
        self.normalize()
        return self

    def max(self):
        l = []
        for coo in range(self.dim):
            a = max([c[coo] for c in self.coos])
            l.append(a)
        return l

    def __hash__(self):
        h = 0 
        for p in self.coos:
            h += hash(str(p))   
        return hash((h,self.name))

    def __eq__(self, other):
        return isinstance(other,self.__class__) and self.coosToSet() == other.coosToSet() and self.name == other.name        

    def coosToSet(self):
        s = set()
	for p in self.coos:
            s.add(str(p))
        return s

    def representation(self):
        return "[" + self.name + ":" + str(self.coos) + "]"
    

class F(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "F", [[0,1],[1,0],[1,1],[1,2],[2,2]])

class I(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "I", [[0,0],[0,1],[0,2],[0,3],[0,4]])

class L(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "L", [[0,0],[0,1],[0,2],[0,3],[1,0]])

class N(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "N", [[0,0],[0,1],[1,1],[1,2],[1,3]])

class P(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "P", [[0,0],[0,1],[0,2],[1,1],[1,2]])

class T(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "T", [[0,2],[1,0],[1,1],[1,2],[2,2]])

class U(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "U", [[0,0],[0,1],[1,0],[2,0],[2,1]])

class V(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "V", [[0,0],[1,0],[2,0],[2,1],[2,2]])

class W(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "W", [[0,0],[1,0],[1,1],[2,1],[2,2]])

class X(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "X", [[0,1],[1,0],[1,1],[1,2],[2,1]])

class Y(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "Y", [[0,0],[1,0],[2,0],[2,1],[3,0]])

class Z(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "Z", [[0,2],[1,0],[1,1],[1,2],[2,0]])


def all_pentominos():
    return [F(), I(), L(), P(), N(), T(), U(), V(), W(), X(), Y(), Z()]


def fixed_pentominos_of(p):
    ts = TileSet() 
    for i in range(4):
	ts.add(p.turn90())
        for i in range(2):
            ts.add(p.flip(i))
    return ts

def all_fixed_pentominos():
    ts = TileSet()
    for p in all_pentominos():
        for q in fixed_pentominos_of(p): 
            ts.add(q)
    return ts

class TileSet(object):
    def __init__(self, plist=[]):
        self.set = set()
        for p in plist:
            self.add(p)

    def __iter__(self):
        return iter(self.set)
        
    def add(self, p):
        self.set.add(copy.deepcopy(p))

    def union(self, s):
        self.set.union(s.set)

    def size(self):
        return len(self.set)

    def representation(self):
        rep = "["
        i = 0
        for p in self.set:
            if i>0:
                rep += ","
            else:
                i = 1
            rep += str(p.coos)
        rep += "]"
        return rep

