import numpy as np

arr = np.sort(np.array([np.random.randint(1, 1000) for i in range(100)]))

def binary_search(value, arr):
    low = 0
    med = 0
    high = len(arr) - 1
    while (high >= low):
        med = (high + low) // 2
        if (value > arr[med]):
            low = med + 1
        elif (value < arr[med]):
            high = med - 1
        else:
            return med
    return -1

def binary_search_recur(value, arr, high, low):
    if(high >= low):
        med = (high + low) // 2
        if(value == arr[med]):
            return med
        elif (value > arr[med]):
            return binary_search_recur(value, arr, high, med + 1)
        else:
            return binary_search_recur(value, arr, med - 1, low)
    else:
        return -1
    
binary_search(arr[0], arr)
binary_search(arr[20], arr)
binary_search(arr[99], arr)
binary_search_recur(arr[0], arr, len(arr) - 1, 0)
binary_search_recur(arr[20], arr, len(arr) - 1, 0)
binary_search_recur(arr[99], arr, len(arr) - 1, 0)