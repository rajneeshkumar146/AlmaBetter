# TC = O(N2), SC = O(1)
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
                isSorted = False

        if isSorted:
            break

# TC = O(N2), SC = O(1)
def selectionSort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(i + 1, l):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def insertionSort(arr):