import copy
from RamseyUtils import *
import random


class RamseySolver:
    def __init__(self, color_1, color_2, graph_size):
        self.color_1 = color_1
        self.color_2 = color_2
        self.graph_size = graph_size
        self.vertices = range(1, graph_size + 1)
        self.edges = self.get_all_edges()
        self.checked_combinations = {}
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
        Calculates the size of the sub graph
                Yields:
                A possible graph coloring
            """

    def size_of_subtree(self, node):
        return len(self.edges) - bin(node).count('1')

    """
    Generates all possibles coloring of graphs
    This generator allows to iterate over a tree of all possible combinations and prune the "bad branches".
    If a branches is flagged as a bad branch (using the checked_combinations dictionary) the branch will be
    cut and the subtree will be iterated.
            Yields:
            A possible graph coloring
        """

    def combination_generator(self, seed_combination, index):
        amount_of_edges = len(self.edges)
        current_combination = seed_combination
        subset = [self.edges[bit] for bit in range(amount_of_edges) if self.is_bit_set(current_combination, bit)]
        yield subset, seed_combination

        next_combination_1 = current_combination + 2 ** index
        if next_combination_1 < 2 ** len(self.edges):
            for combi_1 in self.combination_generator(seed_combination=next_combination_1,
                                                    index=index + 1):
                yield combi_1
                if not self.checked_combinations[next_combination_1]:
                    break

        next_combination_2 = current_combination + 2 ** (index + 1)
        if next_combination_2 < 2 ** len(self.edges):
            for combi_2 in self.combination_generator(seed_combination=next_combination_2,
                                                    index=index + 1):
                yield combi_2
                if not self.checked_combinations[next_combination_2]:
                    break

    """
        Adds a graph to the solution array.
                Parameters:
                graph - a legal graph that meets the condition of Ramsey Numbers
        """

    def add_solution(self, graph):
        self.solution.append(graph)
