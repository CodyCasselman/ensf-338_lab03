if (len(my_list) < 20):
    bubble_sort(my_list)
    print("With bubble sort:", my_list)
elif (len(my_list) >= 20):
    quick_sort(my_list)
    print("With quick sort:", my_list)