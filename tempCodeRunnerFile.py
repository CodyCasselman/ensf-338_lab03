import random
import timeit
import matplotlib.pyplot as plt

def bubble_sort(arr):
    start_time = timeit.default_timer()

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    elapsed_time = timeit.default_timer() - start_time
    return elapsed_time

def quick_sort(arr):
    start_time = timeit.default_timer()

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    elapsed_time = timeit.default_timer() - start_time
    return elapsed_time

def generate_arrays(length):
    # Generate a random array
    random_array = [random.randint(1, 100) for _ in range(length)]

    # Sort the random array to create a sorted array
    sorted_array = sorted(random_array)

    # Reverse the sorted array to create a reversed array
    reversed_array = sorted_array[::-1]

    return random_array, sorted_array, reversed_array

random_array, sorted_array, reversed_array = generate_arrays(20)

worst_bubble = [bubble_sort(reversed_array.copy()) for _ in range(20)]  # 10 measurements
worst_quick = [quick_sort(reversed_array.copy()) for _ in range(20)]  # 10 measurements

avg_bubble = [bubble_sort(random_array.copy()) for _ in range(20)]
best_bubble = [bubble_sort(sorted_array.copy()) for _ in range(20)]

avg_quick = [quick_sort(random_array.copy()) for _ in range(20)]
best_quick = [quick_sort(sorted_array.copy()) for _ in range(20)]

def plot_results(title, worst_case, avg_case, best_case, algorithm):
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 21), worst_case, label='Worst-case')
    plt.plot(range(1, 21), avg_case, label='Average-case')
    plt.plot(range(1, 21), best_case, label='Best-case')
    plt.title(title)
    plt.xlabel('Measurement')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.show()

# Plot for Bubble Sort
plot_results("Bubble Sort", worst_bubble, avg_bubble, best_bubble, "Bubble Sort")

# Plot for Quick Sort
plot_results("Quick Sort", worst_quick, avg_quick, best_quick, "Quick Sort")