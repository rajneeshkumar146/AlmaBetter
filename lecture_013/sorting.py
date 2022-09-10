# TC = O(N2), SC = O(1)
from heapq import merge


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

# TC in Avg case: O(K.N) where k is no of element which is not at there correct position, TC in Worst case: O(N^2)


def insertionSort(arr):
    l = len(arr)

    for i in range(1, l):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1


def mergeTwoSortedList(A, B):
    myAns = []
    i, j = 0, 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            myAns.append(A[i])
            i += 1
        else:
            myAns.append(B[j])
            j += 1

    while i < len(A):
        myAns.append(A[i])
        i += 1

    while j < len(B):
        myAns.append(B[j])
        j += 1

    return myAns

def mergeSort(arr, si, ei):
    if si == ei:
        return [arr[si]]

    mid = (si + ei) // 2
    leftHalf = mergeSort(arr, si , mid)
    rightHalf = mergeSort(arr, mid + 1 , ei)

    return mergeTwoSortedList(leftHalf, rightHalf)

def mergeSort(arr):
    return mergeSort(arr, 0, len(arr) - 1)
