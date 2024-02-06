import sys 
sys.setrecursionlimit(20000)

def merge(arr,low,mid,high):
    '''merges sorted arrays'''
    left_half = arr[low:mid + 1]
    right_half = arr[mid+1:high+1]
    left_ind, right_ind, index = 0, 0, low
    while left_ind < len(left_half) and right_ind < len(right_half):
        if left_half[left_ind] <= right_half[right_ind]:
            arr[index] = left_half[left_ind]
            left_ind += 1
        else:
            arr[index] = right_half[right_ind]
            right_ind += 1
        index +=1

    # Copy any remaining elements from the left half
    while left_ind < len(left_half):
        arr[index] = left_half[left_ind]
        left_ind += 1
        index += 1

    # Copy any remaining elements from the right half
    while right_ind < len(right_half):
        arr[index] = right_half[right_ind]
        right_ind += 1
        index += 1

        

def merge_sort(arr, low, high):
    '''splits the array into seperate smaller arrays. Then merges each array'''
    if low < high:
        mid = (low+high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)

arr = [8,42,25,3,3,2,27,3]
merge_sort(arr,0,len(arr)+1)
print(arr)