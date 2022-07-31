# 1. focus on the first line
# 2. count no of stars and no of spaces
# 3. make it generic equation using table
# 4. right relation of rth line and (r+1)th line


def pattern_01(N):
    nst = 1
    nsp = N - 1

    for r in range (1, N + 1):
        # spaces
        for csp in range(1 , nsp + 1):
            print("  ", end = "")

        # stars
        for cst in range(1, nst + 1):
            print("* ", end = "")

        nst += 1
        nsp -= 1
        print()




