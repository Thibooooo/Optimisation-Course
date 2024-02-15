import time
import matplotlib.pyplot as plt

# Fonction pour résoudre le problème de la somme des sous-ensembles
def print_subset_sum(i, n, _set, target_sum, subset):
    if target_sum == 0:
        return True

    if i == n:
        return False

    if _set[i] <= target_sum:
        subset.append(_set[i])
        if print_subset_sum(i + 1, n, _set, target_sum - _set[i], subset):
            return True
        subset.pop()

    return print_subset_sum(i + 1, n, _set, target_sum, subset)

# Test des cas et enregistrement des temps
set_1 = [1, 2, 1]
set_2 = [3, 34, 4, 12, 5, 2]
sum_1 = 3
sum_2 = 30
problem_sizes = [len(set_1), len(set_2)]
subset_sum_times = []

for _set, target_sum in [(set_1, sum_1), (set_2, sum_2)]:
    start_time = time.time()
    subset = []
    print_subset_sum(0, len(_set), _set, target_sum, subset)
    end_time = time.time()
    subset_sum_times.append(end_time - start_time)

# Tracé du temps en fonction de la taille du problème
plt.plot(problem_sizes, subset_sum_times, marker='o', label='Subset Sum Time')
plt.xlabel('Size of Set')
plt.ylabel('Time (s)')
plt.title('Time Complexity of Subset Sum Problem')
plt.legend()
plt.show()
