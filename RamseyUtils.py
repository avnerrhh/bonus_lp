import copy
import sys

import itertools

"""
    Returns a list of all subsets of size k.
            Parameters:
            super_set - a list of objects
            k - the size of the output sub sets
            Returns:
            A list of all subsets of size k.
    """


def findsubsets(super_set, k):
    return list(set(itertools.combinations(super_set, k)))


def get_subset(super_set, k, idx, current, solution):
    if len(current) == k:
        x = copy.deepcopy(current)
        solution.append(x)
        return
    if idx == len(super_set):
        return
    current.append(super_set[idx])
    get_subset(super_set, k, idx + 1, current, solution)
    current.remove(super_set[idx])
    get_subset(super_set, k, idx + 1, current, solution)


def check_graph(graph, color1, color2):
    for node, neighboors in graph.iteritems():
        if len(neighboors) >= color1 - 1:
            solution = []
            get_subset(neighboors, color1 - 1, 0, [], solution)
            for i in range(0, len(solution)):
                set_to_check = solution.pop()
                good_set_flag = True
                for vertex in set_to_check:
                    good_neighbors_count = 1
                    for neighbor in graph[vertex]:
                        if neighbor in set_to_check:
                            good_neighbors_count += 1
                    if good_neighbors_count < color1 - 1:
                        good_set_flag = False
                        break
                if good_set_flag:
                    return True
    for node, neighboors in graph.iteritems():
        if (len(graph.keys()) - len(neighboors)) >= color2 - 1:
            solution = []
            get_subset(list(set(graph.keys()) - set(neighboors) - set([node])), color2 - 1, 0, [], solution)
            for i in range(0, len(solution)):
                set_to_check = solution.pop()
                good_set_flag = True
                for vertex in set_to_check:
                    good_neighbors_count = 1
                    for neighbor in list(set(graph.keys()) - set(graph[vertex]) - set([vertex])):
                        if neighbor in set_to_check:
                            good_neighbors_count += 1
                    if good_neighbors_count < color2 - 1:
                        good_set_flag = False
                        break
                if good_set_flag:
                    return True
    return False


def write_to_graph_to_file(graph):
    with open('OUTPUT.txt', 'w') as output:
        output.write("matrix([\n")
        output.write("     [")
        first_flag = False
        for key in graph:
            if first_flag:
                output.write(",\n")
                output.write("     [")
            if 1 in graph[key]:
                output.write("1")
            else:
                output.write("0")
            for i in range(2, len(graph.keys()) + 1):
                output.write(",")
                if i in graph[key]:
                    output.write("1")
                else:
                    output.write("0")
            output.write("]")
            first_flag = True
        output.write("\n")
        output.write("]).")


def edge_set_to_graph(edge_set, graphSize):
    ans = {}
    for i in range(1, graphSize + 1):
        ans[i] = []

    for edge in edge_set:
        ans[edge[0]].append(edge[1])
        ans[edge[1]].append(edge[0])
    return ans


# get a subset from all the edges by the index in a binary manner
# e.g index = 64 -> only the edge at the 6th place will return, index = 127 -> 1 - 6 edges will return
def get_subset_by_number(all_edges, index):
    ans = []
    for i in range(0, len(all_edges)):
        if (1 & index >> i):
            ans.append(all_edges[i])
    return ans

