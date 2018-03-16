import sys
from RamseyUtils import *
from RamseySolver import RamseySolver

if __name__ == "__main__":
    color1 = int(sys.argv[1])
    color2 = int(sys.argv[2])
    graphSize = int(sys.argv[3])
    solver = RamseySolver(color_1=color1, color_2=color2, graph_size=graphSize)
    combination_generator = solver.combination_generator(seed_combination=0, index=0)
    count = 0
    import time
    d = time.time()
    for combination,index in combination_generator:
        count += 1
        graph = edge_set_to_graph(combination, graphSize)
        if not check_graph(graph, color1, color2):
            solver.add_solution(graph)
            solver.checked_combinations[index] = True
        else:
            solver.checked_combinations[index] = False
    print(time.time()-d)
    print(len(solver.solution))
    print(count)
