# TC?, SC?
def bubbleSort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(1, l - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


def bubbleSort_opti(arr):
    l = len(arr)
    for i in range(l):
        isSorted = True
        for j in range(1, l - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

        if isSorted:
            break
