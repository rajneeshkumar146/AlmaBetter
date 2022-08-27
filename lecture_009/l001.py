import math
# https://codingbat.com/prob/p192383


def count8(num):
    if num == 0:
        return 0

    counts = count8(num // 10)
    digit = num % 10

    return counts if (num % 10 != 8) else counts + 1

# https://codingbat.com/prob/p184029


def countHi(str):
    if len(str) < 2:
        return 0

    if str[0] == 'h' and str[1] == 'i':
        return countHi(str[2:]) + 1
    else:
        return countHi(str[1:])


# https://codingbat.com/prob/p143900
def countHi2(str):
    return 1


# https://codingbat.com/prob/p170924
def changePI(str):
    return 1


# display List using Recursion
def display(arr, idx):
    if idx == len(arr):
        return

    print(arr[idx])
    display(arr, idx + 1)


# display List in reverse order using Recursion
def displayReverse(arr, idx):
    if idx == len(arr):
        return

    displayReverse(arr, idx + 1)
    print(arr[idx])


def findData(arr, idx, data):
    if idx == len(arr):
        return False

    return arr[idx] == data or findData(arr, idx + 1, data)


def maximum(arr, idx):
    if idx == len(arr):
        return -math.inf

    return max(arr[idx], maximum(arr, idx + 1))

# https://leetcode.com/problems/fibonacci-number/


def fibo(n):
    return 1


# https://leetcode.com/problems/climbing-stairs/
def climbingStairs():
    return 1
