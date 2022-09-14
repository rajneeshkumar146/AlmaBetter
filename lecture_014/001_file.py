def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def sort01(arr):
    n, pt, itr = len(arr), -1, 0
    while itr < n:
        if arr[itr] == 0:
            pt += 1
            swap(arr, pt, itr)

        itr += 1

def segregateElements(arr, index):
    data = arr[index]
    n, pt, itr = len(arr), -1, 0
    while itr < n:
        if arr[itr] <= data:
            pt += 1
            swap(arr, pt, itr)

        itr += 1
    
# segregate your entire array in such a way that your index data will at there correct sorted place.
def segregateElementsWithSortedPlace(arr, index):
    data = arr[index]
    n, pt, itr = len(arr), -1, 0
    while itr < n:
        if arr[itr] <= data:
            pt += 1
            swap(arr, pt, itr)

        itr += 1