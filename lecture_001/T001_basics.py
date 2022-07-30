import math

from sympy import isprime


def printGreeting():
    print("Hello World!")


def printZ():
    print("*****")
    print("   *")
    print("  *")
    print(" *")
    print("*****")

# Grading System--------------------------------------


def gradingSystem(marks):
    if (marks > 90):
        print("excellent")
    elif (marks > 80):
        print("print good")
    elif (marks > 70):
        print("fair")
    elif (marks > 60):
        print("meets expectations")
    else:
        print("below par")


def gradingSystem():
    marks = input()
    gradingSystem(int(marks))

# Odd-Even--------------------------------------------


def isEven(num):
    if (num % 2 == 0):
        return True
    else:
        return False


def ifOdd(num):
    return (True if(num % 2 != 0) else False)

# calc-----------------------------------------------------


def calculator_(num1, num2, operator):
    if (operator == '+'):
        return num1 + num2
    elif (operator == '-'):
        return num1 - num2
    elif (operator == '*'):
        return num1 * num2
    else:
        return "Invalid Input"


def calculator():
    num1 = int(input())
    num2 = int(input())
    operator = input()

    print(calculator_(num1, num2, operator[0]))


# prime Number----------------------------------------------

def isPrimeNumber(num):
    i = 2
    while i * i <= num:
        if(num % i == 0):
            return False
        i += 1

    return True


def printAllPrimeNumbers():
    x = int(input())
    y = int(input())

    for num in range(x, y + 1):
        if(isPrimeNumber(num)):
            print(num)


# Leetcode 509------------------------------------------------

def printFibo(n):
    a = 0
    b = 1
    for i in range(n):
        # print(a)
        sum = a + b
        a = b
        b = sum

    return a

# Bulb_problem-------------------------------------------------

def bulbToggle(num):
    i = 1
    while i * i <= num:
        print(i)

