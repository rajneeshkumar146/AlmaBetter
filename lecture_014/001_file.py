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


def segregateElements_02(arr, index):
    n, pt, itr = len(arr), -1, 0

    data = arr[index]
    swap(arr, index, n - 1)

    while itr < n:
        if arr[itr] <= data:
            pt += 1
            swap(arr, pt, itr)

        itr += 1

    return pt

# T = O(NLog(N)), Worst Case is: T(N2)
# S =  O(Log(N)), Worrst Case is: T(N)
def quickSort(arr, si, ei):
    if si >= ei:
        return

    mid = (si + ei) // 2
    pivotIdx = segregateElements_02(arr, mid)   # O(N)

    quickSort(arr, si, pivotIdx - 1)
    quickSort(arr, pivotIdx + 1, ei)


def quickSort(arr):
    n = len(arr)
    quickSort(arr, 0, n - 1)


# https://leetcode.com/problems/kth-largest-element-in-an-array/
# T: O(NLogN)
# S: O(LogN)