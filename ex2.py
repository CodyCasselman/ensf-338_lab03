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

def generate_arrays(length): #Function to make random, sorted, and reverse arrays
    random_array = [random.randint(1, 100) for _ in range(length)]
    sorted_array = sorted(random_array)
    reversed_array = sorted_array[::-1]
    return random_array, sorted_array, reversed_array

def measure_times(sort_function, array, num_measurements): #Measures times for specified sorting and saves in a list
    times = [sort_function(array.copy()) for _ in range(num_measurements)]
    return times

random_array, sorted_array, reversed_array = generate_arrays(20) #Length = 20

num_measurements = 20

# Measure times for Bubble Sort
worst_bubble = measure_times(bubble_sort, reversed_array, num_measurements)
avg_bubble = measure_times(bubble_sort, random_array, num_measurements)
best_bubble = measure_times(bubble_sort, sorted_array, num_measurements)

# Measure times for Quick Sort
worst_quick = measure_times(quick_sort, reversed_array, num_measurements)
avg_quick = measure_times(quick_sort, random_array, num_measurements)
best_quick = measure_times(quick_sort, sorted_array, num_measurements)

# Plotting individual plots
plt.figure(figsize=(10, 12))

# Bubble Sort Plots
plt.subplot(3, 2, 1)
plt.plot(range(num_measurements), worst_bubble, label='Worst Bubble Sort')
plt.title('Worst Case - Bubble Sort')
plt.xlabel('Measurement')
plt.ylabel('Time (seconds)')
plt.legend()

plt.subplot(3, 2, 2)
plt.plot(range(num_measurements), avg_bubble, label='Average Bubble Sort')
plt.title('Average Case - Bubble Sort')
plt.xlabel('Measurement')
plt.ylabel('Time (seconds)')
plt.legend()

plt.subplot(3, 2, 3)
plt.plot(range(num_measurements), best_bubble, label='Best Bubble Sort')
plt.title('Best Case - Bubble Sort')
plt.xlabel('Measurement')
plt.ylabel('Time (seconds)')
plt.legend()

# Quick Sort Plots
plt.subplot(3, 2, 4)
plt.plot(range(num_measurements), worst_quick, label='Worst Quick Sort')
plt.title('Worst Case - Quick Sort')
plt.xlabel('Measurement')
plt.ylabel('Time (seconds)')
plt.legend()

plt.subplot(3, 2, 5)
plt.plot(range(num_measurements), avg_quick, label='Average Quick Sort')
plt.title('Average Case - Quick Sort')
plt.xlabel('Measurement')
plt.ylabel('Time (seconds)')
plt.legend()

plt.subplot(3, 2, 6)
plt.plot(range(num_measurements), best_quick, label='Best Quick Sort')
plt.title('Best Case - Quick Sort')
plt.xlabel('Measurement')
plt.ylabel('Time (seconds)')
plt.legend()

plt.tight_layout()
plt.show()


