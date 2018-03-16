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
        self.check_combinations = {}
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
            Yields:
            A possible graph coloring
        """

    def combination_genrator(self, seed_combination, range_to_go_over, index):
        amount_of_edges = len(self.edges)
        current_combination = seed_combination
        # TODO: Update run ammount by 2**number_of_zeros - 2 (size of tree under node)
        subset = [self.edges[bit] for bit in range(amount_of_edges) if self.is_bit_set(current_combination, bit)]
        yield subset

        next_combination_1 = current_combination + 2 ** index
        if index == len(self.edges):
            return
        for combi1 in self.combination_genrator(seed_combination=next_combination_1,
                                                range_to_go_over=self.size_of_subtree(next_combination_1),
                                                index=index + 1):
            yield combi1
        next_combination_2 = current_combination + 2 ** (index + 1)
        for combi2 in self.combination_genrator(seed_combination=next_combination_2,
                                                range_to_go_over=self.size_of_subtree(next_combination_2),
                                                index=index + 1):
            yield combi2

        # amount_of_edges = len(self.edges)
        # current_combination = seed_combination
        # # TODO: Update run ammount by 2**number_of_zeros - 2 (size of tree under node)
        # while range_to_go_over != 0:
        #     subset = [self.edges[bit] for bit in range(amount_of_edges) if self.is_bit_set(current_combination, bit)]
        #     yield subset
        #     result = yield
        #     if not result:
        #         range_to_go_over -= self.size_of_subtree(current_combination)
        #         return
        #     else:
        #         next_combination_1 = current_combination + 2 ** index
        #         self.combination_genrator(seed_combination=next_combination_1,
        #                                   range_to_go_over=self.size_of_subtree(next_combination_1),
        #                                   index=index + 1)
        #         next_combination_2 = current_combination + 2 ** (index + 1)
        #         self.combination_genrator(seed_combination=next_combination_1,
        #                                   range_to_go_over=self.size_of_subtree(next_combination_1),
        #                                   index=index + 2)

        # for i in range(1 << len(self.edges)):
        #     subset = [self.edges[bit] for bit in range(amount_of_edges) if self.is_bit_set(i, bit)]
        #     yield subset

    """
        Adds a graph to the solution array.
                Parameters:
                graph - a legal graph that meets the condition of Ramsey Numbers
        """

    def add_solution(self, graph):
        self.solution.append(graph)
