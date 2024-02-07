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

    def _quick_sort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return _quick_sort(left) + middle + _quick_sort(right)

    _quick_sort(arr)
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


# Vary the number of elements from 10 to 210, in increments of 10 for 20 tests
element_counts = list(range(10, 210, 10))

# Measure execution times for bubble sort
avg_bubble = [bubble_sort(generate_arrays(n)[0].copy()) for n in element_counts] #Random input
best_bubble = [bubble_sort(generate_arrays(n)[1].copy()) for n in element_counts] #Sorted input
worst_bubble = [bubble_sort(generate_arrays(n)[2].copy()) for n in element_counts] #Reverse input

# Measure execution times for quick sort
avg_quick = [quick_sort(generate_arrays(n)[0].copy()) for n in element_counts] #Random input
#best_quick = [quick_sort(generate_arrays(n)[3].copy()) for n in element_counts] #Sorted input
#worst_quick = [quick_sort(generate_arrays(n)[4].copy()) for n in element_counts] #Reverse input

# Plots
def plot_results(title, worst_case, avg_case, best_case, algorithm):
    plt.figure(figsize=(8, 5))
    plt.plot(element_counts, worst_case, label='Worst-case')
    plt.plot(element_counts, avg_case, label='Average-case')
    plt.plot(element_counts, best_case, label='Best-case')
    plt.title(title)
    plt.xlabel('Number of Elements')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.show()

# Plot for Bubble Sort
plot_results("Bubble Sort", worst_bubble, avg_bubble, best_bubble, "Bubble Sort")

# Plot for Quick Sort
#plot_results("Quick Sort", worst_quick, avg_quick, best_quick, "Quick Sort")
