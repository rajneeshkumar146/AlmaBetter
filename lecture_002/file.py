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


def pattern07_binomialSeries(N):
    nst = 1
    for n in range(0, N):
        # star
        val = 1
        for r in range(0, nst):
            print(val, " ", end="")
            val = (n - r) * val / (r + 1)

        nst += 1
        print()


def pattern08_pyramid(N):
    nst = 1
    nsp = N - 1

    for r in range(1, N + 1):
        # spaces
        for csp in range(1, nsp + 1):
            print("  ", end="")

        # star
        for cst in range(1, nst + 1):
            print("* ", end="")

        nst += 2
        nsp -= 1
        print()


def pattern09_inversePyramid(N):
    nst = 2 * N - 1
    nsp = 0

    for r in range(1, N + 1):
        # spaces
        for csp in range(1, nsp + 1):
            print("  ", end="")

        # star
        for cst in range(1, nst + 1):
            print("* ", end="")

        nst -= 2
        nsp += 1
        print()


def pattern09_NumberPyramid(N):
    nst = 1
    nsp = N - 1

    for r in range(1, N + 1):
        # spaces
        for csp in range(1, nsp + 1):
            print("  ", end="")

        # star
        count = 1
        for cst in range(1, nst + 1):
            print(count, " ", end="")
            if cst <= nst / 2:
                count += 1
            else:
                count -= 1

        nst += 2
        nsp -= 1
        print()


def pattern10_NumberPyramid_02(N):
    nst = 1
    nsp = N - 1

    for r in range(1, N + 1):
        # spaces
        for csp in range(1, nsp + 1):
            print("  ", end="")

        # star
        val = 1
        for cst in range(1, nst + 1):
            print(val, " ", end="")
            if cst <= nst / 2:
                val *= 2
            else:
                val /= 2

        nst += 2
        nsp -= 1
        print()


def pattern11_diamond(N):
    nst = 1
    nsp = N / 2

    for r in range(1, N + 1):
        # spaces
        for csp in range(1, nsp + 1):
            print("  ", end="")

        # star
        for cst in range(1, nst + 1):
            print("* ", end="")

        if r <= N / 2:
            nst += 2
            nsp -= 1
        else:
            nsp += 1
            nst -= 2
        print()
