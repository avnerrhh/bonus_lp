import copy
from RamseyUtils import *


class RamseySolver:
    def __init__(self, color_1, color_2, graph_size):
        self.color_1 = color_1
        self.color_2 = color_2
        self.graph_size = graph_size
        self.vertices = range(1, graph_size + 1)
        self.edges = self.get_all_edges()
        self.solution = []

    """
        Returns all edges in a complete graph of size n.
                Returns:
                A list of all edges in a complete graph.
        """
    def get_all_edges(self):
        return findsubsets(super_set=self.vertices, k=2)

    """
        Returns a if a bit is flagged.
                Parameters:
                num - a number
                bit - a bit index to check if flagged
                Returns:
                A boolean if the bit is set or not in a number.
        """
    def is_bit_set(self, num, bit):
        return num & (1 << bit) > 0

    """
    Generates all possibles coloring of graphs
            Yields:
            A possible graph coloring
        """
    def combination_genrator(self):
        for i in range((1 << len(self.edges)) / 2):
            subset = [self.edges[bit] for bit in range(len(self.edges)) if self.is_bit_set(i, bit)]
            yield subset

    """
        Adds a graph to the solution array.
                Parameters:
                graph - a legal graph that meets the condition of Ramsey Numbers
        """
    def add_solution(self, graph):
        self.solution.append(graph)
