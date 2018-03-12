import copy
import sys

import itertools
import scipy.special


def is_bit_set(num, bit):
    return num & (1 << bit) > 0


def subsets(s):
    sets = []
    for i in range(1 << len(s)):
        subset = [s[bit] for bit in range(len(s)) if is_bit_set(i, bit)]
        sets.append(subset)
    return sets


solution = []


def get_subset(super_set, k, idx, current):
    if len(current) == k:
        x = copy.deepcopy(current)
        solution.append(x)
        return
    if idx == len(super_set):
        return
    current.append(super_set[idx])
    get_subset(super_set, k, idx + 1, current)
    current.remove(super_set[idx])
    get_subset(super_set, k, idx + 1, current)


def check_graph(graph, color1, color2):
    for key in graph:
        if (len(graph[key]) >= color1 - 1) | (len(graph.keys()) - len(graph[key]) >= color2 - 1):
            global solution
            solution = []
            get_subset(graph[key], color1 - 1, 0, [])
            for i in range(0, len(solution)):
                set_to_check = solution.pop()
                good_set_flag = True
                for vertex in set_to_check:
                    good_neighbors_count = 1
                    for neighbor in graph[vertex]:
                        if neighbor in set_to_check:
                            good_neighbors_count += 1
                    if good_neighbors_count != color1 - 1:
                        good_set_flag = False
                        break
                if good_set_flag:
                    return True
            solution = []
            get_subset(list(set(graph.keys()) - set(graph[key])), color2 - 1, 0, [])
            for i in range(0, len(solution)):
                set_to_check = solution.pop()
                good_set_flag = True
                for vertex in set_to_check:
                    good_neighbors_count = 1
                    for neighbor in list(set(graph.keys()) - set(graph[vertex])):
                        if neighbor in set_to_check:
                            good_neighbors_count += 1
                    if good_neighbors_count != color2 - 1:
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
                output.write("0")
            else:
                output.write("1")
            for i in range(2, len(graph.keys())):
                output.write(",")
                if i in graph[key]:
                    output.write("0")
                else:
                    output.write("1")
            output.write("]")
            first_flag = True
        output.write("\n")
        output.write("]).")

if __name__ == "__main__":
    color1 = int(sys.argv[1])
    color2 = int(sys.argv[2])
    graphSize = int(sys.argv[3])
    graph = {}
print check_graph({1: [3, 4, 5], 2: [4, 5, 6], 3: [1, 5, 6], 4: [1, 2, 6], 5: [1, 2 ,3],6: [2, 3, 4]}, 3, 3)
print check_graph({1: [2,6], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6],6: [1, 5]}, 3, 3)
write_to_graph_to_file({1: [2,6], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6],6: [1, 5]})