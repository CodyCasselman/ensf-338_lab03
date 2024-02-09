import random
import matplotlib.pyplot as plt

def bubble_sort(arr):

    n = len(arr)
    num_swaps = 0
    num_comparisons = 0
    for i in range(n):
        for j in range(0, n-i-1):
            num_comparisons += 1
            if arr[j] > arr[j+1]:
                num_swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return num_swaps, num_comparisons

# Vary the number of elements from 10 to 210, in increments of 10 for 20 tests
element_counts = list(range(10, 210, 10))
#instantiate plotting elements
num_swap = []
num_comparisons = []
array_len = []
#get data for number of swaps depending on array size
for length in element_counts:
    #create a random array with elements 1-100
    random_array = [random.randint(1, 100) for _ in range(length)]
    s, c = bubble_sort(random_array)
    #add number of swap, number of comparisons, and length of arrays to plotting lists
    num_swap.append(s)
    num_comparisons.append(c)
    array_len.append(length)

plt.figure()
plt.plot(array_len, num_comparisons, label="Number of Comparisons")
plt.title("Number of Comparisons vs Length of Array")
plt.xlabel("Length of Array")
plt.ylabel("Number of Comparisons")

plt.figure()
plt.plot(array_len, num_swap, label="Number of Swaps")
plt.title("Number of Swaps vs Length of Array")
plt.xlabel("Length of Array")
plt.ylabel("Number of Swaps")


plt.show()
    


