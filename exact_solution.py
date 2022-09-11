from numpy import loadtxt
from sys import maxsize
from itertools import permutations
import time

PATH1 = 'tsp_data/tsp1_253.txt'
PATH2 = 'tsp_data/tsp2_1248.txt'
PATH3 = 'tsp_data/tsp3_1194.txt'
PATH4 = 'tsp_data/tsp4_7013.txt'
PATH5 = 'tsp_data/tsp5_27603.txt'

if __name__ == "__main__":
    graph = loadtxt(PATH2, dtype=int)

    start_time = time.time()
    matrix_length = len(graph)
    vertex = []

    for index in range(matrix_length):
        if index != 0:
            vertex.append(index)

    min_path = maxsize
    perms = permutations(vertex)         #mostra todas as combinações possíveis entre os indices do grafo

    for index in perms:
        weight = 0
        k = 0

        for j in index:
            weight += graph[k][j]
            k = j

        weight += graph[k][0]
        min_path = min(min_path, weight)

    print(f"tempo: {time.time() - start_time:.4f}s")
    print(f"solução: {min_path}")
