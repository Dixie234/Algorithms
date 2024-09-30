def bubblesort(arr):
    unsorted_index = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
        unsorted_index -= 1

def insertionsort(arr):
    for i in range(1, len(arr)):
        temp_val = arr[i]
        position = i - 1

        while position >= 0:
            if arr[position] > temp_val:
                arr[position + 1] = arr[position]
                position = position - 1
            else:
                break
        arr[position + 1] = temp_val

def selectionsort(arr):
    length = len(arr)
    for i in range(length):
        lowestNumIndex = i
        for j in range(i + 1, length):
            if arr[j] < arr[lowestNumIndex]:
                lowestNumIndex = j
            if lowestNumIndex != i:
                temp = arr[i]
                arr[i] = arr[lowestNumIndex]
                arr[lowestNumIndex] = temp


def quicksort(arr, left_index, right_index):
    if right_index - left_index <= 0:
        return
    
    pivot_index = partition(arr, left_index, right_index)

    quicksort(arr, left_index, pivot_index - 1)
    quicksort(arr, pivot_index + 1, right_index)

def partition(arr, left_pointer, right_pointer):
    pivot_index = right_pointer
    pivot = arr[pivot_index]
    right_pointer -= 1

    while True:
        while arr[left_pointer] < pivot:
            left_pointer += 1
        
        while arr[right_pointer] > pivot:
            right_pointer -= 1

        if left_pointer >= right_pointer:
            break
        else:
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]

        left_pointer += 1

    arr[left_pointer], arr[pivot_index] = arr[pivot_index], arr[left_pointer]

    return left_pointer

def mergesort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergesort(arr, left, mid)
        mergesort(arr, mid + 1, right)
        merge(arr, left, right, mid)

def merge(arr, left, right, mid):
    larr_length = mid - left + 1
    rarr_length = right - mid
    L = arr[left : mid + 1]
    R = arr[mid + 1 : right + rarr_length]

    i = 0
    j = 0
    k = left
    while i < larr_length and j < rarr_length:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < larr_length:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < rarr_length:
        arr[k] = R[j]
        j += 1
        k += 1
        
arr = [1,9,8,2,3,7,4,6,5]
#bubblesort(arr)
#insertionsort(arr)
#selectionsort(arr)
#quicksort(arr, 0, len(arr) - 1)
mergesort(arr, 0, len(arr) - 1)
