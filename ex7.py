import json
import random
import timeit
import matplotlib.pyplot as plt

with open('ex7data.json', 'r', encoding='utf-8') as f:
    data = f.read()

js = json.loads(data)

with open('ex7tasks.json', 'r', encoding='utf-8') as f2:
    data2 = f2.read()

js2 = json.loads(data2)

def binary_search(arr, target, initial_midpoint):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

        if low == 0 and high == len(arr) - 1:
            mid = initial_midpoint

    return -1

results = []

for entry in js2:
    best_midpoint = None
    best_time = float('inf')

    for _ in range(10):  
        initial_midpoint = random.randint(0, len(js) - 1)
        
        time_taken = timeit.timeit(lambda: binary_search(js, entry, initial_midpoint), number=1000)

        if time_taken < best_time:
            best_time = time_taken
            best_midpoint = initial_midpoint

    results.append((entry, best_midpoint, best_time))

# Unpack results into separate lists for plotting
entries, midpoints, times = zip(*results)

# Scatterplot
plt.scatter(times, midpoints, c='orange')
plt.title('Time vs Chosen Midpoint')
plt.xlabel('Time taken (seconds)')
plt.ylabel('Chosen Midpoint')
plt.show()
