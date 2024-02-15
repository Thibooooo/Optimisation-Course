import time
import matplotlib.pyplot as plt
from itertools import permutations

# Fonction pour résoudre le problème du voyageur de commerce
def travellingSalesmanProblem(graph, s): 
    vertex = [i for i in range(len(graph)) if i != s] 
    min_path = float('inf')
    next_permutation = permutations(vertex)
    
    start_time = time.time()
    for path in next_permutation:
        current_pathweight = 0
        k = s 
        for j in path: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
        min_path = min(min_path, current_pathweight) 
    
    end_time = time.time()
    return min_path, end_time - start_time

# Définition du graphe
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
starting_city = 0

# Test et enregistrement des temps
problem_sizes = [4, 5, 6, 7, 8]
tsp_times = []
for size in problem_sizes:
    graph = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            graph[i][j] = i + j  # Valeurs fictives, juste pour l'exemple
    min_path, time_taken = travellingSalesmanProblem(graph, starting_city)
    tsp_times.append(time_taken)

# Tracé du temps en fonction de la taille du problème
plt.plot(problem_sizes, tsp_times, marker='o', label='TSP Time')
plt.xlabel('Number of Cities')
plt.ylabel('Time (s)')
plt.title('Time Complexity of Travelling Salesman Problem')
plt.legend()
plt.show()
