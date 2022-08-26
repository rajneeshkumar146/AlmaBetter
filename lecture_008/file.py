from cgitb import small


def ppppppp(a, b):
    print("Hi There I'm Base case, It's Time to go back Simon")
    return


def pppppp(a, b):
    print("hi: ", a)
    ppppppp(a+1, b)
    print("bye: ", a)


def ppppp(a, b):
    print("hi: ", a)
    pppppp(a+1, b)
    print("bye: ", a)


def pppp(a, b):
    print("hi: ", a)
    ppppp(a+1, b)
    print("bye: ", a)


def ppp(a, b):
    print("hi: ", a)
    pppp(a+1, b)
    print("bye: ", a)


def pp(a, b):
    print("hi: ", a)
    ppp(a+1, b)
    print("bye: ", a)


def p(a, b):
    print("hi: ", a)
    pp(a+1, b)
    print("bye: ", a)


# ===============================================================

# MLE : Memory Limit Exceed
# TLE: Time Limit Exceed
# Infinite Recursive Call
# Stack Overflow because of non terminating recusrive call

# Steps:
# 1. Make some Faith
# 2. complete your task by writing missing line
# 3. put some kind of breaker in your code which known as terminatingPoint/BaseCase

def printIncreasing(a, b):
    if a > b:
        return

    print(a)
    printIncreasing(a + 1, b)   # faith


def printDecreasing(a, b):
    if a > b:
        return

    printDecreasing(a + 1, b)   # faith
    print(a)


def printIncreasingDecreasing(a, b):
    if (a == b):
        print(a)
        return

    print(a)
    printIncreasingDecreasing(a + 1, b)
    print(a)


def printIncraesingDecreasing_02(a, b):
    if (a == b):
        print(a)
        return

    print(a)
    printIncraesingDecreasing_02(a + 1, b)
    print(a)


def printTable(a, i):
    if i > 10:
        return

    print(a, " X ", i, " = ", a * i)
    printTable(a, i + 1)


def printTableInRange(a, b):
    if a > b:
        return

    printTable(a, 1)
    print()
    printTableInRange(a + 1, b)

def factorial(n):
    if n == 0:
        return 1

    smallAns = factorial(n - 1)
    return smallAns * n


def factorial_02(n):
    return 1 if n == 0 else factorial_02(n - 1) * n


# T and S: O(N)
def power(a, b):
    if b == 0:
        return 1

    smallAns = power(a, b - 1)
    return smallAns * a

def power_02(a, b):
    return 1 if b == 0 else power_02(a, b - 1) * a


# T and S: O(Log(N))
def powerBtr(a, b):
    if b == 0:
        return 1


    smallAns = powerBtr(a, b // 2)
    smallAns *= smallAns

    return smallAns if (b % 2 == 0) else (smallAns * a)
