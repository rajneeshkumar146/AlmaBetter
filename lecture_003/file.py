def pattern11_numberDiamond(N):
    nst = 1
    nsp = N // 2

    for r in range(1, N + 1):
        # spaces
        for csp in range(1, nsp + 1):
            print("  ", end="")

        # star
        if r <= int(N / 2):
            val = r
        else:
            val = N - r + 1

        for cst in range(1, nst + 1):
            print(val, " ", end="")
            if cst <= int(nst / 2):
                val += 1
            else:
                val -= 1

        if r <= N / 2:
            nst += 2
            nsp -= 1
        else:
            nsp += 1
            nst -= 2
        print()
