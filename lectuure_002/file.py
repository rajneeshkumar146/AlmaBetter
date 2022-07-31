# 1. focus on the first line
# 2. count no of stars and no of spaces
# 3. make it generic equation using table
# 4. right relation of rth line and (r+1)th line


def pattern_01(N):
    nst = 1
    nsp = N - 1

    for r in range(1, N + 1):
        # spaces
        for csp in range(1, nsp + 1):
            print("  ", end="")

        # stars
        for cst in range(1, nst + 1):
            print("* ", end="")

        nst += 1
        nsp -= 1
        print()


def pattern_02(N):
    nst = N
    nsp = 0

    for r in range(1, N + 1):
        # spaces
        for csp in range(1, nsp + 1):
            print("  ", end="")

        # star
        for cst in range(1, nst + 1):
            print("* ", end="")

        nst -= 1
        nsp += 1
        print()


def pattern_03(N):
    nst = 1
    nsp = 0

    for r in range(1, N + 1):
        # spaces
        for csp in range(1, nsp + 1):
            print("  ", end="")

        # star
        for cst in range(1, nst + 1):
            print("* ", end="")

        nst += 1
        print()


def pattern_04(N):
    nst = N
    nsp = 0

    for r in range(1, N + 1):
        # spaces
        for csp in range(1, nsp + 1):
            print("  ", end="")

        # star
        for cst in range(1, nst + 1):
            print("* ", end="")

        nst -= 1
        print()


def pattern_05(N):
    nst = 1
    count = 1
    for r in range(1, N + 1):
        # star
        for cst in range(1, nst + 1):
            print(count, " ", end="")
            count += 1

        nst += 1
        print()


def pattern_06(N):
    nst = 1
    a = 0
    b = 1
    for r in range(1, N + 1):
        # star
        for cst in range(1, nst + 1):
            print(a, " ", end="")
            sum = a + b
            a = b
            b = sum

        nst += 1
        print()

def pattern_binomialSeries(N):
