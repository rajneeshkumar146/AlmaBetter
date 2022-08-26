def ppppppp(a, b):
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



#===============================================================

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


def printIncraesingDecreasing(a,b):



def printIncraesingDecreasing_02(a,b):
