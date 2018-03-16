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

def write_to_graphs_to_file(graphs):
    with open('OUTPUT.txt', 'w') as output:
        output.write("\n\n\n\n")
        for i in range(0, len(graphs)):
            graph = edge_set_to_graph(graphs[i], len(graphs[i]))
            if not check_graph(graph, 3, 3):
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
                output.write("]).\n\n")


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


def check_all_6_graphs():
    vertex = []
    for i in range(0, 6):
        vertex.append(i+1)
    solution = []
    get_subset(vertex, 2, 0, [], solution)
    with open('OUTPUT.txt', 'w') as output:
        output.write("\n\n\n\n")
        for i in range(0, pow(2, len(solution))):
            edges_graph = get_subset_by_number(solution, i)
            graph = edge_set_to_graph(edges_graph, 6)
            if not check_graph(graph, 3, 5):
                print graph
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
                output.write("]).\n\n")


def get_matrix(file_name):
    with open(file_name, 'r') as file_solution:
        file_solution.readline()
        file_solution.readline()
        file_solution.readline()
        file_solution.readline()
        file_solution.readline()
        line = file_solution.readline()
        solutions = []
        while line != "":
            matrix = []
            while line != "]).\n":
                row = []
                for i in range(0, len(line)):
                    if line[i] == '1':
                        row.append(1)
                    elif line[i] == '0':
                        row.append(0)
                matrix.append(copy.deepcopy(row))
                line = file_solution.readline()
            solutions.append(copy.deepcopy(matrix))
            file_solution.readline()
            file_solution.readline()
            line = file_solution.readline()
    return solutions


def equle_matrix(matrix, matrix_to_check):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if matrix[i][j] != matrix_to_check[i][j]:
                return False
    return True


def graph_comp(file_name_solution,file_name_to_check):
    matrices_to_check = get_matrix(file_name_to_check)
    matrix_solution = get_matrix(file_name_solution)
    i=0
    for matrix in matrices_to_check:
        find_matrix_flag = False
        i+=1
        for matrix_to_check in matrix_solution:
            if equle_matrix(matrix, matrix_to_check):
                find_matrix_flag = True
                print i
                break
        if not find_matrix_flag:
            print matrix
            print(matrix_to_check)
            return False
    return True


