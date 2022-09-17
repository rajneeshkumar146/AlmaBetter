def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


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


def isSubArraySorted(arr, si, ei):
    prevEle = arr[si]
    si += 1
    while si <= ei:
        if prevEle > arr[si]:
            return False

        prevEle = arr[si]
        si += 1

    return True


# T = O(NLog(N)), Worst Case is: T(N2)
# S =  O(Log(N)), Worrst Case is: T(N)
def quickSort(arr, si, ei):
    if si >= ei:
        return

    if isSubArraySorted(arr,si,ei):
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

def kthLargest_01(arr, maxlEle):


def kthLargest(arr,k):
    maxEle = 1e9

    for i in range(k):
        maxEle = kthLargest_01(arr, maxEle)


    