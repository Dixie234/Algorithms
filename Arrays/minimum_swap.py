# Temporary array to store elements in sorted order
# Hashing elements with their correct positions
# Index of the element that should be at index i.
# Update the indices in the dictionary
def minSwaps(arr):
    temp = sorted(arr) #if the number list was always 1 to n, then this can be O(n): [i for i in range(1, len(arr) + 1)]
    pos = { k: i for i, k in enumerate(arr) }
    
    swaps = 0
    for i in range(len(arr)):
        if temp[i] != arr[i]:       
            ind = pos[temp[i]]
            arr[i], arr[ind] = arr[ind], arr[i]

            pos[arr[i]] = i
            pos[arr[ind]] = ind

            swaps += 1
    return swaps