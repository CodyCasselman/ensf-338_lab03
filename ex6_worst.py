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

def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def sort_and_search(arr, target):
    sorted_array = quicksort(arr.copy())
    binary_search(sorted_array, target)

def measure_execution_time(func, *args):
    start_time = timeit.default_timer()
    result = func(*args)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time

input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

linear_search_times = []
binary_search_times = []

for entry in input_sizes:
    for i in range(0, 100):
        array = [random.randint(1, 50) for _ in range(entry)] #random 100 element array from 1-50
        worst_array = sorted(array)
        target = random.randint(1, 50) #target from 1-50

        _, linear_search_time = measure_execution_time(linear_search, array, target)
        linear_search_times.append(linear_search_time)

        _, binary_search_time = measure_execution_time(sort_and_search, worst_array, target)
        binary_search_times.append(binary_search_time)

    plt.plot(linear_search_times, label='Linear Search')
    plt.plot(binary_search_times, label='Binary Search after Sorting')
    plt.xlabel('Iteration')
    plt.ylabel('Execution Time (seconds)')
    plt.title(f"Performance of Linear Search vs. Binary Search after Sorting {entry} Entries")
    plt.legend()
    plt.show()