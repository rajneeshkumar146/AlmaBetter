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



# https://codingbat.com/prob/p170924
def changePI(str):



# display List using Recursion
def display(arr):


# display List in reverse order using Recursion
def displayReverse(arr):


def findData(arr,data):


def maximum(arr):
    