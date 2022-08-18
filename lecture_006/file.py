import numpy as np


def display1D(arr):

    for data in arr:
        print(data, end="")


def inverseOfArray(arr):
    l = len(arr)
    res_arr = np.array(l, dtype=int)
    for i in len(arr):
        index = arr[i]
        res_arr[index] = i
        # res_arr[arr[i]] = i

    return res_arr