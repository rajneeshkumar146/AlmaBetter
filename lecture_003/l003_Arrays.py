import numpy as np
from sqlalchemy import true


def inputEle_01():
    n = int(input())
    # take input in map and mapped to list
    a = list(map(int, input().split()))

    arr = np.array(a)  # convert list into array
    return arr


def inputEle_02():
    a = []
    n = int(input())
    for i in range(n):
        a.append(int(input()))

    arr = np.array(a)   # convert list into array
    print(arr)


def output(arr):
    l = len(arr)
    for i in range(l):
        print(arr[i])


def maximumEle(arr):
    l = len(arr)
    if l == 0:
        return -math.inf

    max = arr[0]
    for i in range(l):
        if arr[i] > max:
            max = arr[i]

    return max


def minimum(arr):
    l = len(arr)
    if l == 0:
        return math.inf

    min = arr[0]
    for i in range(l):
        if arr[i] < min:
            min = arr[i]

    return min


# T: O(N), where N is No of element, S: O(1)
def linearSearch(arr, data):
    l = len(arr)

    for i in range(l):
        if arr[i] == data:
            return True

    return False

# T: O(Log(N)), where N is No of element, S: O(1)


def binarySearch(arr, data):
    l = len(arr)
    si = 0
    ei = l - 1

    while si <= ei:
        mid = (si + ei) // 2
        if arr[mid] == data:
            return mid
        elif arr[mid] < data:
            si = mid + 1
        else:
            ei = mid - 1

    return -1


arr = inputEle_01()
output(arr)
