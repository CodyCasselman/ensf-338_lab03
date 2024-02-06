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

worst_bubble = sum(bubble_sort(reversed_array.copy()) for _ in range(10)) / 10  # 10 measurements
worst_quick = sum(quick_sort(reversed_array.copy()) for _ in range(10)) / 10  # 10 measurements

avg_bubble = sum(bubble_sort(random_array.copy()) for _ in range(10)) / 10
best_bubble = sum(bubble_sort(sorted_array.copy()) for _ in range(10)) / 10

avg_quick = sum(quick_sort(random_array.copy()) for _ in range(10)) / 10
best_quick = sum(quick_sort(sorted_array.copy()) for _ in range(10)) / 10

print("Bubble Sort:")
print("Worst-case times:", worst_bubble)
print("Average-case time:", avg_bubble)
print("Best-case time:", best_bubble)

print("\nQuick Sort:")
print("Worst-case times:", worst_quick)
print("Average-case time:", avg_quick)
print("Best-case time:", best_quick)

