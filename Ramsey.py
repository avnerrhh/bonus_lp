import sys
from RamseyUtils import *
from RamseySolver import RamseySolver

if __name__ == "__main__":
    color1 = int(sys.argv[1])
    color2 = int(sys.argv[2])
    graphSize = int(sys.argv[3])
    solver = RamseySolver(color_1=color1, color_2=color2, graph_size=graphSize)
    for combination in solver.combination_genrator():
        graph = edge_set_to_graph(combination, graphSize)
        if check_graph(graph, color1, color2):
            solver.add_solution(graph)
    print(len(solver.solution))
    # write_to_graph_to_file(graph)
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

# print check_graph({1: [3, 4, 5], 2: [4, 5, 6], 3: [1, 5, 6], 4: [1, 2, 6], 5: [1, 2 ,3],6: [2, 3, 4]}, 3, 3)
# print check_graph({1: [2,6], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [1, 5]}, 3, 3)
# write_to_graph_to_file({1: [2,6], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6],6: [1, 5]})
