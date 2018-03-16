import copy
import sys
from RamseyUtils import *

def is_bit_set(num, bit):
    return num & (1 << bit) > 0


def subsets(s):
    sets = []
    for i in range(1 << len(s)):
        subset = [s[bit] for bit in range(len(s)) if is_bit_set(i, bit)]
        sets.append(subset)
    return sets





def check_graph(graph, color1, color2):
    for key in graph:
        if len(graph[key]) >= color1 - 1:
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

                    if good_neighbors_count < color1 - 1:
                        good_set_flag = False
                        break
                if good_set_flag:
                    return True
    for key in graph:
        if (len(graph.keys()) - len(graph[key])) >= color2 - 1:
            solution = []
            get_subset(list(set(graph.keys()) - set(graph[key]) - set([key])), color2 - 1, 0, [])
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
            for i in range(2, len(graph.keys())+1):
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
    for i in range (1,graphSize+1):
        ans[i] = []

    for edge in edge_set:
        ans[edge[0]].append(edge[1])
        ans[edge[1]].append(edge[0])
    return ans

#get a subset from all the edges by the index in a binary manner
# e.g index = 64 -> only the edge at the 6th place will return, index = 127 -> 1 - 6 edges will return
def get_subset_by_number(all_edges, index):
    ans = []
    for i in range(0,len(all_edges)):
        if (1 & index >> i):
            ans.append(all_edges[i])
    return ans



if __name__ == "__main__":
    color1 = int(sys.argv[1])
    color2 = int(sys.argv[2])
    graphSize = int(sys.argv[3])
    vertex = range(1, graphSize + 1)
    global solution
    solution = []

    # gets all the edges and put them in solution (solution is global because this code origin is from java)
    get_subset(vertex, 2, 0, [])
    all_edges = subsets(solution)
    graph = edge_set_to_graph([[1, 2], [1, 5], [2, 3], [3, 4], [4, 5]], graphSize)
    print graph,color1,color2
    if check_graph(graph, color1, color2):
        print "hello"
    write_to_graph_to_file(graph)
    # print all_edges
    # answer_flag = True
    # for edge_set in all_edges:
    #     graph = edge_set_to_graph(edge_set, graphSize)
    #     print graph
    #     if not check_graph(graph, color1, color2):
    #         write_to_graph_to_file(graph)
    #         answer_flag = False
    #         break
    # if answer_flag:
    #     with open('OUTPUT.txt', 'w') as output:
    #         output.write("NO SOLUTION")

#print check_graph({1: [3, 4, 5], 2: [4, 5, 6], 3: [1, 5, 6], 4: [1, 2, 6], 5: [1, 2 ,3],6: [2, 3, 4]}, 3, 3)
#print check_graph({1: [2,6], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [1, 5]}, 3, 3)
#write_to_graph_to_file({1: [2,6], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6],6: [1, 5]})