import timeit
import random
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def generate_worst_case_input(size):
    return list(range(size, 0, -1))

def measure_execution_time(func, *args):
    start_time = timeit.default_timer()
    result = func(*args)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time

input_sizes = list(range(10, 510, 10))
execution_times = []

for size in input_sizes:
    input_data = generate_worst_case_input(size)
    _, execution_time = measure_execution_time(quicksort, input_data)
    execution_times.append(execution_time)

plt.plot(input_sizes, execution_times, linestyle='-', label='Quicksort')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Quicksort Execution Time on Worst-case Inputs')
plt.legend()
plt.show()


