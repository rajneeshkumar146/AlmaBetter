
# T: O(LogN), S: O(1)
from re import L


def findCorrectLocation(arr, data):
    l = len(arr)
    si = 0
    ei = l
    while si < ei:
        mid = (si + ei) // 2
        if arr[mid] < data:
            si = mid + 1
        else:
            ei = mid

    return ei

# ceil and floor


def nearestEle(arr, data):
    l = len(arr)
    if data < arr[0]:
        return 0
    elif data > arr[l - 1]:
        return l - 1

    si, ei = 0, l - 1
    while si <= ei:
        mid = (si + ei) // 2
        if arr[mid] == data:
            return mid
        elif arr[mid] < data:
            si = mid + 1
        else:
            ei = mid - 1

    if data - arr[ei] < arr[si] - data:
        return ei
    else:
        return si

# T: O(N)


def findRange_01(arr, data):
    l, sr, er = len(arr), -1, -1

    for idx in range(l):
        if(arr[idx] == data):
            if(sr == -1):
                sr = idx
            er = idx

        if(arr[idx] > data):
            break

    print("range: (", sr, ", ", er, ")")

# O(Log(N))


def findStartingIndex(arr, data):
    l, si, ei = len(arr), 0, l - 1

    while si <= ei:
        mid = (si + ei) // 2
        if arr[mid] == data:
            if mid - 1 >= 0 and arr[mid - 1] == data:
                ei = mid - 1
            else:
                return mid
        elif arr[mid] < data:
            si = mid + 1
        else:
            ei = mid - 1
    return -1

# O(Log(N))


def findEndingIndex(arr, data):
    l, si, ei = len(arr), 0, l - 1

    while si <= ei:
        mid = (si + ei) // 2
        if arr[mid] == data:
            if mid + 1 < l and arr[mid + 1] == data:
                si = mid + 1
            else:
                return mid
        elif arr[mid] < data:
            si = mid + 1
        else:
            ei = mid - 1
    return -1

# O(Log(N))


def findRange_02(arr, data):
    sr = findStartingIndex(arr, data)
    er = findEndingIndex(arr, data)
    print("range: (", sr, ", ", er, ")")


# https://leetcode.com/problems/merge-sorted-array/
