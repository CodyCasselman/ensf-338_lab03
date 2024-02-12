import random
import matplotlib.pyplot as plt
import scipy.optimize
import timeit

def quadratic(x, A, B, C):
    return (A*(x**2) + B*x + C)


#Ex.5 Is meant to Implement both Insertion sort and Binary Insertion sort. As well as find comparisons between the two
def insertion_sort(arr):
    '''Insertion sort is a sorting method which takes an array and sorts all the values.
    It has a time complexity of O(n^2)'''
    
    for i in range(1, len(arr)): #parse through the entire array
        key = arr[i] #denote a key, which will be used for sorting (starts at 2nd index)
        j = i-1
        while j >= 0 and key < arr[j]: #if j is the first element or if j is < arr[j] then arr[j] is sorted
            arr[j+1] = arr[j] #shift each element of the array 1 to the right
            j -= 1
        arr[j+1] = key #place key 1 to the right of arr[j]

def binary_search(arr, n, key):
    '''
    binary_search is mean to find the position of the element just above key. This is a binary searching method
    which gives it a complexity of log(n)
    arr: array to be searched
    n: final index of subarray
    key: value to be searched for
    returns: position of the value just above the key
    '''
    left = 0
    right = n
    while (left < right):
        mid = (left + right) // 2
        if (arr[mid] <= key):
            left = mid + 1
        else:
            right = mid
    return left


def binary_insertion_sort(arr):
    '''
    binary_insertion_sort is meant to sort an array using a mixture of the binary search algorithm and the insertion sorthing method.
    due to the combination of these methods. binary_insertion_sort has a better number of comparisons, but the swap complexity stays O(n^2)
    arr: array to be sorted
    returns: none
    '''
    for i in range(1, len(arr)):
        #iterate through the entire array starting from the 2nd element
        key = arr[i]
        pos = binary_search(arr, i, key)
        #pos now contains the index to where key should be placed
        j = i
        while(j > pos):
            #shift each value to the right
            arr[j] = arr[j-1]
            j -= 1
        #since each value is shifted to the right we are safe to insert the key into its sorted position
        arr[pos] = key



#For question 2. We have chosen to compute the average time taken for each length of array when sorted 100 times.
#And then plot the times against the lengths of array.

# Vary the number of elements from 10 to 500, in increments of 10
element_counts = list(range(10, 500, 10))
#instantiate plotting elements
time_taken_bin = []
time_taken_ins = []
array_len = []

#this is for finding the time it takes for the functions to complete 100 times. It does this for every length of array
for length in element_counts:
    time_taken_bin.append(timeit.timeit(lambda: binary_insertion_sort(arr=[random.randint(1, 100) for _ in range(length)]), number = 100))
    time_taken_ins.append(timeit.timeit(lambda: insertion_sort(arr=[random.randint(1, 100) for _ in range(length)]), number=100))
    array_len.append(length)

#curve_fitting each function and finding the assosciated interpolated function
popt_bin, pcov_bin = scipy.optimize.curve_fit(quadratic, array_len, time_taken_bin)
popt_ins, pcov_ins = scipy.optimize.curve_fit(quadratic, array_len, time_taken_ins)


plt.figure()
plt.plot(array_len, time_taken_bin, 'r-', label="Binary Insertion Sort")
plt.plot(array_len, [quadratic(arr, *popt_bin) for arr in array_len], 'r--', label="Binary Fit. A=%5.4f B=%5.4f C=%5.4f" % tuple(popt_bin))
plt.plot(array_len, time_taken_ins, 'b-', label="Traditional Insertion Sort")
plt.plot(array_len, [quadratic(arr, *popt_ins) for arr in array_len], 'b--', label="Insertion Fit. A=%5.4f B=%5.4f C=%5.4f" % tuple(popt_ins))
plt.xlabel("Length of Array")
plt.ylabel("Time Taken to Sort Array")
plt.title("Time Complexity of Binary Insertion Sort and Traditional Insertion Sort")
plt.legend()

plt.show()

'''
Question 4: Discuss the Results. Which Algorithm was Faster? Why?

From our graphs we can deduce a few interesting aspects about the speed of each algorithm. We can conclude firstly,
that for significantly large arrays, binary insertion sort will outperform traditional insertion sort. We can make this conclusion
by making the observation that traditional insertion has a consistently higher y value than that of its binary counterpart.
However, in smaller array sizes (ideally <~25), traditional insertion sort performs better. I believe that this is due to the
increased chance of there being a best-case sort. In which during a best case sort, insertion sort has the ability to outperfrom binary
insertion sort.

Each sorting method has a time complexity of O(n^2). Binary insertion sort slightly outperforms insertion sort due to it having a
comparison complexity of O(nlogn) (due to the splitting nature of binary search).However, this edge in comparisons does not prove to
lead to a significant time advantage for the algorithm. As both algorithms have a swapping complexity of O(n**2).
'''
