#Ex.5 Is meant to Implement both Insertion sort and Binary Insertion sort. As well as find comparisons between the two
def insertion_sort(arr):
    '''Insertion sort is a sorting method which takes an array and sorts all the values.
    It has a time complexity of O(n^2)'''
    for i in range(1, len(arr)): #parse through the entire array
        
        key = arr[i] #denote a key, which will be used for sorting (starts at 2nd index)

        j = 1-i
        while j >= 0 and key <= arr[j]: #if j is the first element or if j is < arr[j] then arr[j] is sorted
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
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= key:
            left = mid
        else:
            right = mid
    return left


def binary_insertion_sort(arr):
    '''
    binary_insertion_sort is meant to sort an array using a mixture of the binary search algorithm and the insertion sorthing method.
    due to the combination of these methods. binary_insertion_sort has a complexity of nlog(n)
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







