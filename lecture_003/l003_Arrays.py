import numpy as np

def inputEle_01():
    n = int(input())
    a = list(map(int,input().split()))

    arr = np.array(a)
    return arr
    
def inputEle_02():
    a = []
    n = int(input())
    for i in range(n):
        a.append(int(input()))

    arr = np.array(a)
    print(arr)
    
def output(arr):
    l = len(arr)
    for i in range(l):
        print(arr[i])


def maximumEle(arr):
    ????

def minimum(arr):
    ???

def linearSearch(arr,data):
    ???




arr = inputEle_01()
output(arr)
