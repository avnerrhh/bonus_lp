import copy
from RamseyUtils import *

class RamseySolver:
    def __init__(self,color_1,color_2,graph_size):
        self.color_1 = color_1
        self.color_2 = color_2
        self.graph_size = graph_size
        self.solution = []

    def get_subset(self,super_set, k, idx, current):
        get_subset(super_set, k, idx + 1, current,self.solution)

    def subsets(self):
        s = self.solution
        sets = []
        for i in range(1 << len(s)):
            subset = [s[bit] for bit in range(len(s)) if self.is_bit_set(i, bit)]
            sets.append(subset)
        return sets

    def is_bit_set(self,num, bit):
        return num & (1 << bit) > 0
