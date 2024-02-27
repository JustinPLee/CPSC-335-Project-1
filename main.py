
def bubble_sort(L): # O(1)
    n = len(L)
    for i in range(n): # n-1 times O(n)
        for j in range(0, n - 1 - 1): # N-i-1 times O(n)
            if L[j] > L[j+1]: # 0(n)
                L[j], L[j+1], L[j] # O(N^2)
    return L # O(1)

def mergeSort(arr):
    if len(arr) > 1: #check if the array has more than one element
        mid = len(arr) // 2 #find the midpoint of array
        L = arr[:mid] # create left sublist and assigning the first half 
        R = arr[mid:] # create right sublsit and assign the second half 

        mergeSort(L) # recursively applies Merge sort to the left sublist 
        mergeSort(R) # recursively applies Merge sort to the right sublist 
    i = j = k = 0 # i for the current index of the left sublsit 
              # j for the current index if the right sublsit 
              # k for the current index of main arr

    while i < len(L) and j < len(R): #continue the loop as long as there are...
        if L[i] < R[j]: # check if the current elemnt in the left sublist...
            arr[k] = L[i] # if true, place the current left elemtn into the...
            i += 1 #moves the pointer in the left sublsit 
        else:
            arr[k] = R[j] # place the current element from right sublist 
            j += 1 # moves pointer in teh right sublist
        k += 1 #regardless of whre the elemnt was taken from, pointer of main array must move on.

    while i < len(L): #handle the scenario where one sublsit is exhauseted before
        arr[k] = L[i] # copy the remaining element from L or R into the arr
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[i]
        j += 1
        k += 1

def quick_sort(arr):
    # if the array is empty or has a single element, it's already sorted.
    if len(arr) <= 1:
        return arr
    else:
        # Choosing the middle element as the pivot.
        pivot = arr[len(arr) // 2]
        left = []  # Elements less than the pivot.
        middle = []  # Elements equal to the pivot.
        right = []  # Elements greater than the pivot.

        # Partitioning the array based on the pivot value.
        for x in arr:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                middle.append(x)

        # Recursively sorting the left and right parts of the array, and concatenating the results.
        return quick_sort(left) + middle + quick_sort(right)
