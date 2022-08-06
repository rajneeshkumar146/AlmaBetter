import numpy as np
import sys

def testList():
    list = []
    list.append(9999999999999999999999999999999999999999999999999999)
    print("size consumed: ", sys.getsizeof(list))
    print(list[0])
    val = 9999999999999999999999999999999999999
    print(val)

def testArray():
    array = np.arange(1000)
    array[0] = 999
    print("size consumed: ", array.itemsize)
    print(array[0])


testList()

