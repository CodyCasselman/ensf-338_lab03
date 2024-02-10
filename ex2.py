import random
import time
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
        end_time = timeit.default_timer()
        return end_time - start_time
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        time_less = quick_sort(less)
        time_greater = quick_sort(greater)
        end_time = timeit.default_timer()
        return end_time - start_time


def generate_arrays(length):
    random_array = [random.randint(1, 100) for _ in range(length)] #random array

    sorted_array = sorted(random_array) #sort array

    reversed_array = sorted_array[::-1] #reverse array

    best_case_quick = random_array.copy() #best case array for quick
    temp = best_case_quick[0]
    best_case_quick[0] = best_case_quick[len(best_case_quick) // 2]
    best_case_quick[len(best_case_quick) // 2] = temp



    return random_array, sorted_array, reversed_array, best_case_quick


# 20 tests from from 10 to 210 in increments of 10
element_counts = list(range(10, 210, 10))

# Measure execution times for bubble sort
avg_bubble = [bubble_sort(generate_arrays(n)[0].copy()) for n in element_counts] #Random input
best_bubble = [bubble_sort(generate_arrays(n)[1].copy()) for n in element_counts] #Sorted input
worst_bubble = [bubble_sort(generate_arrays(n)[2].copy()) for n in element_counts] #Reverse input

# Measure execution times for quick sort
avg_quick = [quick_sort(generate_arrays(n)[0].copy()) for n in element_counts]  # Random input
best_quick = [quick_sort(generate_arrays(n)[3].copy()) for n in element_counts]  # Best case (Pivot is median)
worst_quick = [quick_sort(generate_arrays(n)[1].copy()) for n in element_counts]  # Sorted input


def plot_results(title, worst_case, avg_case, best_case, algorithm):
    plt.figure(figsize=(8, 5))
    plt.plot(element_counts, worst_case, label='Worst-case')
    plt.plot(element_counts, avg_case, label='Average-case')
    plt.plot(element_counts, best_case, label='Best-case')
    plt.title(f"{title}")
    plt.xlabel('Number of Elements')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.show()

plot_results("Bubble Sort", worst_bubble, avg_bubble, best_bubble, "Bubble Sort")

plot_results("Quick Sort", worst_quick, avg_quick, best_quick, "Quick Sort")
